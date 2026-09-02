#!/usr/bin/env python3
"""
revisoes.py — utilitário de revisão para o cofre SEFAZ-BA (Obsidian)

TRÊS COMANDOS
-------------
    agendar     lê tags de revisão e escreve [cad:: Nd] [prox:: data] na linha
    escalonar   encurta a cadência de revisões muito atrasadas
    cobertura   relatório dos tópicos nunca tocados (dom 0 e sem marcação)

USO
---
    python3 revisoes.py agendar    --vault "/caminho/vault-ba"
    python3 revisoes.py agendar    --vault "/caminho/vault-ba" --apply
    python3 revisoes.py escalonar  --vault "/caminho/vault-ba"
    python3 revisoes.py escalonar  --vault "/caminho/vault-ba" --apply
    python3 revisoes.py cobertura  --vault "/caminho/vault-ba"

Sem --apply, todo comando roda em simulação e não grava nada.
`cobertura` é somente leitura e nunca grava.

COMO O CICLO FECHA
------------------
Revisou? Promova a tag: #revisar/3d -> /7d -> /15d -> /30d. Na próxima execução
o script vê que a cadência mudou, recalcula prox a partir de hoje e atualiza cad.
Errou muito? Rebaixe a tag. Funciona igual, para baixo.

Se a cadência não mudou, prox não é tocado — rodar o script várias vezes no mesmo
dia não empurra suas datas para frente.
"""

import argparse
import re
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

# =============================================================================
# CONFIGURAÇÃO
# =============================================================================

# Cadências das tags auxiliares, em dias.
# Estes valores são uma PROPOSTA. Ajuste após uma ou duas semanas de uso.
CADENCIAS_AUXILIARES = {
    "#dominio/baixo": 3,
    "#tec/erro": 3,
    "#acao/decorar": 7,
}

# Cadência para um #revisar sem sufixo.
CADENCIA_REVISAR_SIMPLES = 7

# Escada válida de cadências (usada pelo escalonamento).
ESCADA = [3, 7, 15, 30]

# Escalonamento: atraso a partir do qual a cadência é rebaixada um degrau.
DIAS_PARA_ESCALONAR = 7

# Pastas e arquivos ignorados. Os painéis e a nota de taxonomia contêm nomes
# de tags dentro de consultas — marcá-los quebraria as próprias consultas.
PASTAS_IGNORADAS = {".obsidian", ".smart-env", ".trash", ".git", "Excalidraw"}
ARQUIVOS_IGNORADOS = {"SEFAZ BA.md", "PAINEL.md", "TAGs.md", "COMO USAR.md", "system.md"}

# =============================================================================

RE_REVISAR_SUFIXO = re.compile(r"#revisar/(\d+)(?:dias|dia|d)(?![\w/-])")
RE_REVISAR_SIMPLES = re.compile(r"#revisar(?![/\w])")
RE_CAD = re.compile(r"\[cad::\s*(\d+)d\s*\]")
RE_PROX = re.compile(r"\[prox::\s*(\d{4}-\d{2}-\d{2})\s*\]")
RE_DOM = re.compile(r"\[dom::\s*(\d+)\s*\]")
RE_PESO = re.compile(r"\[peso::\s*(\d+)\s*\]")
RE_CODIGO = re.compile(r"`[^`]*`")
RE_ASPAS = re.compile(r'"#[^"]*"')
RE_H3 = re.compile(r"^###\s+-?\s*(.+?)\s*$")


def limpar(linha: str) -> str:
    """Neutraliza tags citadas como exemplo (entre crases ou aspas retas)."""
    return RE_ASPAS.sub("", RE_CODIGO.sub("", linha))


def arquivos_do_cofre(raiz: Path):
    for md in sorted(raiz.rglob("*.md")):
        if any(p in PASTAS_IGNORADAS for p in md.parts):
            continue
        if md.name in ARQUIVOS_IGNORADOS:
            continue
        yield md


def linhas_uteis(caminho: Path):
    """Itera (indice, linha) pulando blocos de código."""
    try:
        linhas = caminho.read_text(encoding="utf-8").splitlines(keepends=True)
    except (UnicodeDecodeError, OSError):
        return [], []
    uteis = []
    dentro = False
    for i, l in enumerate(linhas):
        if l.lstrip().startswith("```"):
            dentro = not dentro
            continue
        if not dentro:
            uteis.append((i, l))
    return linhas, uteis


def cadencia_da_linha(linha: str):
    """Cadência mais curta encontrada na linha: (dias, tag) ou (None, None)."""
    l = limpar(linha)
    cands = []
    for m in RE_REVISAR_SUFIXO.finditer(l):
        cands.append((int(m.group(1)), f"#revisar/{m.group(1)}d"))
    if RE_REVISAR_SIMPLES.search(l):
        cands.append((CADENCIA_REVISAR_SIMPLES, "#revisar"))
    for tag, dias in CADENCIAS_AUXILIARES.items():
        if re.search(re.escape(tag) + r"(?![\w/-])", l):
            cands.append((dias, tag))
    return min(cands, key=lambda c: c[0]) if cands else (None, None)


def escrever_campos(linha: str, dias: int, quando: date) -> str:
    fim = ""
    corpo = linha
    if corpo.endswith("\n"):
        corpo, fim = corpo[:-1], "\n"
    if RE_CAD.search(corpo):
        corpo = RE_CAD.sub(f"[cad:: {dias}d]", corpo)
    else:
        corpo = corpo.rstrip() + f" [cad:: {dias}d]"
    if RE_PROX.search(corpo):
        corpo = RE_PROX.sub(f"[prox:: {quando.isoformat()}]", corpo)
    else:
        corpo = corpo.rstrip() + f" [prox:: {quando.isoformat()}]"
    return corpo + fim


def eh_item_lista(linha: str) -> bool:
    return bool(re.match(r"\s*(?:[-*+]|\d+\.)\s", linha))


# =============================================================================
# COMANDO: agendar
# =============================================================================

def cmd_agendar(raiz: Path, aplicar: bool):
    hoje = date.today()
    registro = []

    for md in arquivos_do_cofre(raiz):
        linhas, uteis = linhas_uteis(md)
        alterado = False
        for i, linha in uteis:
            dias, tag = cadencia_da_linha(linha)
            if dias is None:
                continue
            cad = RE_CAD.search(linha)
            prox = RE_PROX.search(linha)
            cad_val = int(cad.group(1)) if cad else None
            prox_val = prox.group(1) if prox else None

            if cad_val == dias and prox_val:
                acao, quando = "inalterado", date.fromisoformat(prox_val)
            else:
                quando = hoje + timedelta(days=dias)
                acao = "novo" if cad_val is None else f"recadenciado {cad_val}d->{dias}d"
                linhas[i] = escrever_campos(linha, dias, quando)
                alterado = True

            registro.append({
                "arq": md.name, "ln": i + 1, "tag": tag, "cad": dias,
                "prox": quando.isoformat(), "acao": acao,
                "lista": eh_item_lista(linha),
            })
        if alterado and aplicar:
            md.write_text("".join(linhas), encoding="utf-8")

    if not registro:
        print("Nenhuma linha com tag de revisão encontrada.")
        return

    registro.sort(key=lambda r: (r["prox"], r["arq"]))
    print(f"{'Arquivo':<44} {'ln':>5}  {'tag':<16} {'cad':>4}  {'vence':<11} situação")
    print("-" * 110)
    for r in registro:
        marca = "" if r["lista"] else "   [nao-lista]"
        print(f"{r['arq'][:43]:<44} {r['ln']:>5}  {r['tag']:<16} {str(r['cad'])+'d':>4}  "
              f"{r['prox']:<11} {r['acao']}{marca}")

    fora = [r for r in registro if not r["lista"]]
    print(f"\n{len(registro)} linha(s). Modo: {'APLICADO' if aplicar else 'SIMULAÇÃO — nada gravado (use --apply)'}")
    if fora:
        print(f"\nAviso: {len(fora)} linha(s) [nao-lista] não são itens de lista. Consultas com")
        print("FLATTEN file.lists não as enxergam. Acrescente '- ' no início delas.")


# =============================================================================
# COMANDO: escalonar
# =============================================================================

def degrau_abaixo(dias: int) -> int:
    """Rebaixa um degrau na escada. Se já está no menor, permanece."""
    menores = [d for d in ESCADA if d < dias]
    return max(menores) if menores else min(ESCADA)


def cmd_escalonar(raiz: Path, aplicar: bool, limite: int):
    hoje = date.today()
    registro = []

    for md in arquivos_do_cofre(raiz):
        linhas, uteis = linhas_uteis(md)
        alterado = False
        for i, linha in uteis:
            cad = RE_CAD.search(linha)
            prox = RE_PROX.search(linha)
            if not (cad and prox):
                continue
            atraso = (hoje - date.fromisoformat(prox.group(1))).days
            if atraso < limite:
                continue

            cad_val = int(cad.group(1))
            novo = degrau_abaixo(cad_val)
            nova_data = hoje + timedelta(days=novo)

            if novo == cad_val:
                acao = f"já no piso ({novo}d), só reagendado"
            else:
                acao = f"rebaixado {cad_val}d -> {novo}d"

            nova_linha = escrever_campos(linha, novo, nova_data)

            # A tag precisa passar a declarar a nova cadência explicitamente.
            # Sem isso, o comando `agendar` releria a tag original e desfaria
            # o rebaixamento na execução seguinte.
            tag_explicita = f"#revisar/{novo}d"
            if RE_REVISAR_SUFIXO.search(nova_linha):
                nova_linha = RE_REVISAR_SUFIXO.sub(tag_explicita, nova_linha)
            elif RE_REVISAR_SIMPLES.search(nova_linha):
                nova_linha = RE_REVISAR_SIMPLES.sub(tag_explicita, nova_linha)
            else:
                # Linha marcada só por tag auxiliar (#dominio/baixo etc.):
                # acrescenta a tag explícita sem remover a original.
                corpo, fim = (nova_linha[:-1], "\n") if nova_linha.endswith("\n") else (nova_linha, "")
                corpo = re.sub(r"(\s*)(\[cad::)", rf" {tag_explicita}\1\2", corpo, count=1)
                nova_linha = corpo + fim

            linhas[i] = nova_linha
            alterado = True

            registro.append({
                "arq": md.name, "ln": i + 1, "atraso": atraso,
                "de": cad_val, "para": novo, "nova": nova_data.isoformat(), "acao": acao,
            })
        if alterado and aplicar:
            md.write_text("".join(linhas), encoding="utf-8")

    if not registro:
        print(f"Nenhuma revisão atrasada há {limite}+ dias. Fila em dia.")
        return

    registro.sort(key=lambda r: -r["atraso"])
    print(f"{'Arquivo':<44} {'ln':>5}  {'atraso':>7}  {'nova data':<11} ação")
    print("-" * 100)
    for r in registro:
        print(f"{r['arq'][:43]:<44} {r['ln']:>5}  {str(r['atraso'])+'d':>7}  {r['nova']:<11} {r['acao']}")
    print(f"\n{len(registro)} linha(s). Modo: {'APLICADO' if aplicar else 'SIMULAÇÃO — nada gravado (use --apply)'}")


# =============================================================================
# COMANDO: cobertura
# =============================================================================

def ler_frontmatter(linhas):
    meta = {}
    if not linhas or not linhas[0].startswith("---"):
        return meta
    for l in linhas[1:]:
        if l.startswith("---"):
            break
        if ":" in l:
            k, v = l.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta


def cmd_cobertura(raiz: Path):
    disciplinas = []
    sem_checklist = []

    for md in arquivos_do_cofre(raiz):
        linhas, uteis = linhas_uteis(md)
        if not linhas:
            continue
        meta = ler_frontmatter(linhas)
        if "disciplina" not in meta:
            continue

        topicos = []
        titulo_atual = None
        for i, linha in uteis:
            h3 = RE_H3.match(linha.rstrip())
            if h3:
                titulo_atual = h3.group(1)
                continue
            m_dom = RE_DOM.search(linha)
            if m_dom and eh_item_lista(linha):
                m_peso = RE_PESO.search(linha)
                topicos.append({
                    "titulo": titulo_atual or "(sem cabeçalho)",
                    "dom": int(m_dom.group(1)),
                    "peso": int(m_peso.group(1)) if m_peso else 0,
                })

        if not topicos:
            sem_checklist.append(f"{meta.get('disciplina', md.stem)} ({md.name})")
            continue

        # Tags de estudo presentes no arquivo inteiro (sinal de que foi tocado).
        corpo = "".join(limpar(l) for _, l in uteis)
        marcado = bool(re.search(r"#revisar|#dominio/|#status/|#acao/|#tec/", corpo))

        disciplinas.append({
            "disciplina": meta.get("disciplina", md.stem),
            "prova": meta.get("prova", "?"),
            "peso": meta.get("peso", "?"),
            "prioridade": meta.get("prioridade", "?"),
            "total": len(topicos),
            "zerados": sum(1 for t in topicos if t["dom"] == 0),
            "marcado": marcado,
            "topicos": topicos,
        })

    if not disciplinas:
        print("Nenhuma nota de disciplina encontrada (frontmatter sem campo 'disciplina').")
        return

    # Valores reais usados no frontmatter do cofre: crítico, importante, complementar.
    ordem_prio = {"crítico": 0, "critico": 0, "crítica": 0, "critica": 0,
                  "importante": 1, "complementar": 2, "baixa": 3}
    disciplinas.sort(key=lambda d: (ordem_prio.get(d["prioridade"].lower(), 9), -d["total"]))

    print("RELATÓRIO DE COBERTURA — tópicos por disciplina\n")
    print(f"{'Disciplina':<44} {'P':<3} {'peso':<5} {'prioridade':<12} {'zerados/total':<14} tocada")
    print("-" * 100)
    tot_z = tot_t = 0
    for d in disciplinas:
        tot_z += d["zerados"]
        tot_t += d["total"]
        frac = f"{d['zerados']}/{d['total']}"
        print(f"{d['disciplina'][:43]:<44} {d['prova']:<3} {d['peso']:<5} "
              f"{d['prioridade']:<12} {frac:<14} {'sim' if d['marcado'] else 'NÃO'}")

    pct = (tot_z / tot_t * 100) if tot_t else 0
    print(f"\nTotal: {tot_z} de {tot_t} tópicos com dom 0 ({pct:.0f}% intocados).")

    intocadas = [d for d in disciplinas if not d["marcado"]]
    if intocadas:
        print(f"\n{len(intocadas)} disciplina(s) sem NENHUMA tag de estudo:")
        for d in intocadas:
            print(f"  - {d['disciplina']} (prova {d['prova']}, peso {d['peso']}, {d['prioridade']})")

    if sem_checklist:
        print(f"\n{len(sem_checklist)} nota(s) de disciplina sem checklist de tópicos")
        print("(têm frontmatter mas nenhuma linha '- [ ] ... [dom:: N]'), fora da contagem:")
        for s_ in sem_checklist:
            print(f"  - {s_}")

    print("\nEste comando é somente leitura. Nada foi gravado.")


# =============================================================================

def main():
    p = argparse.ArgumentParser(description="Utilitário de revisão para o cofre Obsidian.")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("agendar", help="Escreve cad/prox a partir das tags.")
    a.add_argument("--vault", required=True)
    a.add_argument("--apply", action="store_true")

    e = sub.add_parser("escalonar", help="Rebaixa cadência de revisões atrasadas.")
    e.add_argument("--vault", required=True)
    e.add_argument("--apply", action="store_true")
    e.add_argument("--limite", type=int, default=DIAS_PARA_ESCALONAR,
                   help=f"Dias de atraso para rebaixar (padrão: {DIAS_PARA_ESCALONAR}).")

    c = sub.add_parser("cobertura", help="Relatório de tópicos intocados (somente leitura).")
    c.add_argument("--vault", required=True)

    args = p.parse_args()
    raiz = Path(args.vault)
    if not raiz.exists():
        print(f"Caminho não encontrado: {raiz}")
        return

    if args.cmd == "agendar":
        cmd_agendar(raiz, args.apply)
    elif args.cmd == "escalonar":
        cmd_escalonar(raiz, args.apply, args.limite)
    elif args.cmd == "cobertura":
        cmd_cobertura(raiz)


if __name__ == "__main__":
    main()
