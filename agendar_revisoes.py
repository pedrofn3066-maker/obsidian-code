#!/usr/bin/env python3
"""
agendar_revisoes.py — motor de revisão por tags para o cofre SEFAZ-BA

O QUE FAZ
---------
Varre o cofre procurando linhas marcadas com tags de revisão e escreve, no fim
da linha, dois campos inline do Dataview:

    [cad:: 7d] [prox:: 2026-08-28]

`cad` guarda a cadência que gerou a data. `prox` é a data em que aquilo volta.
O painel filtra por `prox <= date(today)`.

COMO O CICLO FECHA
------------------
Quando você revisa, você PROMOVE a tag: #revisar/3d -> #revisar/7d -> /15d -> /30d.
Na próxima execução o script percebe que a cadência mudou (tag diz 7d, campo cad
diz 3d), recalcula `prox` a partir de hoje e atualiza `cad`. Se errou muito na
revisão, rebaixe a tag — funciona igual, para baixo.

Se a cadência NÃO mudou, o script não mexe em `prox`. Rodar o script várias vezes
no mesmo dia não empurra suas datas para frente.

TAGS RECONHECIDAS
-----------------
Explícitas (você escolhe a cadência):
    #revisar/3d  #revisar/7d  #revisar/15d  #revisar/30d
    (#revisar sem sufixo entra na cadência padrão definida em CADENCIA_REVISAR_SIMPLES)

Herdadas (cadência automática, definida em CADENCIAS_AUXILIARES):
    #dominio/baixo   #acao/decorar   #tec/erro

Se uma linha tiver mais de uma tag, vence a cadência MAIS CURTA.

USO
---
    python3 agendar_revisoes.py --vault "/caminho/vault-ba"            # simulação
    python3 agendar_revisoes.py --vault "/caminho/vault-ba" --apply    # grava

Rode sempre sem --apply primeiro.
"""

import argparse
import re
from datetime import date, timedelta
from pathlib import Path

# ---------------------------------------------------------------------------
# CONFIGURAÇÃO — ajuste aqui
# ---------------------------------------------------------------------------

# Cadências das tags auxiliares, em dias.
# ATENÇÃO: estes valores são uma PROPOSTA minha, não uma regra sua. Ajuste.
CADENCIAS_AUXILIARES = {
    "#dominio/baixo": 3,   # ponto fraco: volta rápido
    "#tec/erro": 3,        # erro recente de questão: volta rápido
    "#acao/decorar": 7,    # decoreba: espaçamento maior
}

# Cadência para um #revisar sem sufixo (você tem 9 dessas hoje no cofre).
CADENCIA_REVISAR_SIMPLES = 7

# Pastas ignoradas (configuração do Obsidian, plugins, lixeira).
PASTAS_IGNORADAS = {".obsidian", ".smart-env", ".trash", ".git", "Excalidraw"}

# Arquivos ignorados: painéis (contêm nomes de tags dentro de queries) e a
# documentação da taxonomia. Marcá-los quebraria as próprias consultas.
ARQUIVOS_IGNORADOS = {"SEFAZ BA.md", "PAINEL.md", "TAGs.md", "COMO USAR.md"}

# ---------------------------------------------------------------------------

RE_REVISAR_SUFIXO = re.compile(r"#revisar/(\d+)(?:dias|dia|d)(?![\w/-])")
RE_REVISAR_SIMPLES = re.compile(r"#revisar(?![/\w])")
RE_CAD = re.compile(r"\[cad::\s*(\d+)d\s*\]")
RE_PROX = re.compile(r"\[prox::\s*(\d{4}-\d{2}-\d{2})\s*\]")
RE_CODIGO_INLINE = re.compile(r"`[^`]*`")


def remover_codigo_inline(linha: str) -> str:
    """Neutraliza trechos entre crases, para não capturar tags citadas como exemplo
    (ex.: a linha `#tec/erro` que aparece nos templates da pasta QUESTÕES)."""
    return RE_CODIGO_INLINE.sub("", linha)


def cadencia_da_linha(linha: str):
    """Retorna (dias, origem) da cadência mais curta encontrada, ou (None, None)."""
    limpa = remover_codigo_inline(linha)
    candidatas = []

    for m in RE_REVISAR_SUFIXO.finditer(limpa):
        candidatas.append((int(m.group(1)), f"#revisar/{m.group(1)}d"))

    if RE_REVISAR_SIMPLES.search(limpa):
        candidatas.append((CADENCIA_REVISAR_SIMPLES, "#revisar"))

    for tag, dias in CADENCIAS_AUXILIARES.items():
        if re.search(re.escape(tag) + r"(?![\w/-])", limpa):
            candidatas.append((dias, tag))

    if not candidatas:
        return None, None
    return min(candidatas, key=lambda c: c[0])


def escrever_campos(linha: str, dias: int, nova_data: date) -> str:
    """Insere ou atualiza [cad:: Nd] [prox:: data] no fim da linha, preservando
    a quebra de linha original."""
    fim = ""
    corpo = linha
    if corpo.endswith("\n"):
        corpo, fim = corpo[:-1], "\n"

    if RE_CAD.search(corpo):
        corpo = RE_CAD.sub(f"[cad:: {dias}d]", corpo)
    if RE_PROX.search(corpo):
        corpo = RE_PROX.sub(f"[prox:: {nova_data.isoformat()}]", corpo)

    if not RE_CAD.search(corpo):
        corpo = corpo.rstrip() + f" [cad:: {dias}d]"
    if not RE_PROX.search(corpo):
        corpo = corpo.rstrip() + f" [prox:: {nova_data.isoformat()}]"

    return corpo + fim


def processar_arquivo(caminho: Path, hoje: date, aplicar: bool, registro: list):
    try:
        texto = caminho.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return

    linhas = texto.splitlines(keepends=True)
    alterado = False
    dentro_de_bloco = False

    for i, linha in enumerate(linhas):
        # Ignora tudo dentro de blocos de código (as queries do painel vivem lá).
        if linha.lstrip().startswith("```") or linha.lstrip().startswith("> ```"):
            dentro_de_bloco = not dentro_de_bloco
            continue
        if dentro_de_bloco:
            continue

        dias, origem = cadencia_da_linha(linha)
        if dias is None:
            continue

        cad_atual = RE_CAD.search(linha)
        prox_atual = RE_PROX.search(linha)

        cad_valor = int(cad_atual.group(1)) if cad_atual else None
        prox_valor = prox_atual.group(1) if prox_atual else None

        # Recalcula só se a cadência mudou ou se ainda não havia agendamento.
        if cad_valor == dias and prox_valor is not None:
            acao = "inalterado"
            nova_data = date.fromisoformat(prox_valor)
        else:
            nova_data = hoje + timedelta(days=dias)
            acao = "novo" if cad_valor is None else f"recadenciado {cad_valor}d->{dias}d"
            linhas[i] = escrever_campos(linha, dias, nova_data)
            alterado = True

        # Sinaliza linhas que não são item de lista: as consultas do painel que
        # usam file.lists não enxergam essas.
        eh_lista = bool(re.match(r"\s*[-*+]\s|\s*\d+\.\s", linha))

        registro.append({
            "arquivo": caminho.name,
            "linha": i + 1,
            "tag": origem,
            "cad": f"{dias}d",
            "prox": nova_data.isoformat(),
            "acao": acao,
            "lista": eh_lista,
            "texto": remover_codigo_inline(linha).strip()[:60],
        })

    if alterado and aplicar:
        caminho.write_text("".join(linhas), encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description="Agenda revisões por tags no cofre Obsidian.")
    p.add_argument("--vault", required=True, help="Caminho da raiz do cofre.")
    p.add_argument("--apply", action="store_true", help="Grava as mudanças. Sem isso, só simula.")
    args = p.parse_args()

    raiz = Path(args.vault)
    if not raiz.exists():
        print(f"Caminho não encontrado: {raiz}")
        return

    hoje = date.today()
    registro = []

    for md in sorted(raiz.rglob("*.md")):
        if any(parte in PASTAS_IGNORADAS for parte in md.parts):
            continue
        if md.name in ARQUIVOS_IGNORADOS:
            continue
        processar_arquivo(md, hoje, args.apply, registro)

    if not registro:
        print("Nenhuma linha com tag de revisão encontrada.")
        return

    registro.sort(key=lambda r: (r["prox"], r["arquivo"]))

    print(f"{'Arquivo':<42} {'ln':>4}  {'tag':<16} {'cad':>4}  {'próxima':<11} {'situação'}")
    print("-" * 108)
    for r in registro:
        marca = "" if r["lista"] else "  [nao-lista]"
        print(f"{r['arquivo'][:41]:<42} {r['linha']:>4}  {r['tag']:<16} {r['cad']:>4}  {r['prox']:<11} {r['acao']}{marca}")

    fora_de_lista = [r for r in registro if not r["lista"]]
    modo = "APLICADO" if args.apply else "SIMULAÇÃO — nada foi gravado (use --apply)"

    print(f"\n{len(registro)} linha(s) agendada(s). Modo: {modo}")
    if fora_de_lista:
        print(f"\nAviso: {len(fora_de_lista)} linha(s) marcadas com [nao-lista] não são itens de lista.")
        print("As consultas do painel que usam FLATTEN file.lists não enxergam essas linhas.")
        print("Para aparecerem, converta em item de lista acrescentando '- ' no início.")


if __name__ == "__main__":
    main()
