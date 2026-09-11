#!/usr/bin/env python3
"""
Conta e valida os grifos semânticos que a triagem (/triar-inbox) põe nas
notas — <span class="g-prazo|g-cond|g-comp|g-num">…</span>, coloridos pelo
snippet .obsidian/snippets/grifos.css.

    python3 PY/grifos.py "MATERIAS/<nota>.md"      contagem por categoria + problemas
    python3 PY/grifos.py MATERIAS                  idem, somando todas as notas da pasta
    python3 PY/grifos.py --limpo "MATERIAS/<nota>.md"   imprime a nota sem os grifos
    git show HEAD:"<nota>" | python3 PY/grifos.py --limpo -

--limpo existe pra conferir o lastro: o texto sem os spans tem que ser
palavra por palavra o que estava antes de grifar.

Sai com código 1 se achar problema: classe g-* desconhecida, grifo não
fechado na mesma linha, grifo dentro de grifo, grifo vazio.
"""
import re
import sys
from pathlib import Path

CATEGORIAS = {  # classe -> rótulo, na ordem da barra "Térmico"
    "g-prazo": "prazos",
    "g-cond": "condições/ressalvas",
    "g-comp": "competências",
    "g-num": "números",
}
TAG = re.compile(r"<span\b([^>]*)>|</span\s*>", re.IGNORECASE)
CLASSE = re.compile(r"""class\s*=\s*["']([^"']*)["']""", re.IGNORECASE)


def classe_grifo(attrs):
    """'g-prazo' se o span é grifo, '?g-xyz' se é g-* desconhecido, None se não é grifo."""
    m = CLASSE.search(attrs or "")
    if not m:
        return None
    for c in m.group(1).split():
        if c in CATEGORIAS:
            return c
        if c.startswith("g-"):
            return "?" + c
    return None


def analisa_linha(linha):
    """-> (contagem {classe: n}, problemas [str], linha_sem_grifos)"""
    contagem, problemas = {}, []
    pilha = []     # (classe_ou_None, inicio_tag, fim_tag, fim_conteudo_aberto)
    cortes = []    # (inicio, fim) de tags de grifo a remover no --limpo
    for m in TAG.finditer(linha):
        if m.group(0).startswith("</"):
            if not pilha:
                continue  # </span> de um span comum aberto em outra linha
            classe, ini, fim, _ = pilha.pop()
            if classe:
                if not linha[fim:m.start()].strip():
                    problemas.append(f"grifo {classe} vazio")
                contagem[classe] = contagem.get(classe, 0) + 1
                cortes += [(ini, fim), (m.start(), m.end())]
            continue
        classe = classe_grifo(m.group(1))
        if classe and classe.startswith("?"):
            problemas.append(f"classe desconhecida {classe[1:]!r} (use {', '.join(CATEGORIAS)})")
            classe = None
        if classe and any(c for c, *_ in pilha):
            problemas.append(f"{classe} dentro de outro grifo")
        pilha.append((classe, m.start(), m.end(), None))
    for classe, *_ in pilha:
        if classe:
            problemas.append(f"{classe} aberto e não fechado na mesma linha")
    limpo = linha
    for ini, fim in sorted(cortes, reverse=True):
        limpo = limpo[:ini] + limpo[fim:]
    return contagem, problemas, limpo


def analisa_texto(texto):
    total, problemas, limpas = {}, [], []
    em_codigo = False
    for n, linha in enumerate(texto.split("\n"), 1):
        if linha.lstrip().startswith("```"):
            em_codigo = not em_codigo
        if em_codigo:
            limpas.append(linha)
            continue
        contagem, probs, limpa = analisa_linha(linha)
        for c, k in contagem.items():
            total[c] = total.get(c, 0) + k
        problemas += [(n, p) for p in probs]
        limpas.append(limpa)
    return total, problemas, "\n".join(limpas)


def barra(contagem):
    return "  ".join(f"{rot} {contagem.get(c, 0)}" for c, rot in CATEGORIAS.items())


def main(args):
    limpo = "--limpo" in args
    alvos = [a for a in args if a != "--limpo"]
    if not alvos:
        print(__doc__.strip())
        return 1

    if limpo:
        if len(alvos) != 1:
            print("--limpo aceita um arquivo só (ou - pra stdin).")
            return 1
        texto = sys.stdin.read() if alvos[0] == "-" else Path(alvos[0]).read_text(encoding="utf-8")
        sys.stdout.write(analisa_texto(texto)[2])
        return 0

    arquivos = []
    for a in alvos:
        p = Path(a)
        arquivos += sorted(p.rglob("*.md")) if p.is_dir() else [p]

    geral, ruim = {}, False
    for arq in arquivos:
        contagem, problemas, _ = analisa_texto(arq.read_text(encoding="utf-8"))
        for c, k in contagem.items():
            geral[c] = geral.get(c, 0) + k
        if contagem or problemas:
            print(f"{arq}\n  {barra(contagem)}")
        for n, p in problemas:
            ruim = True
            print(f"  ! linha {n}: {p}")
    if len(arquivos) > 1:
        print(f"TÉRMICO (total)  {barra(geral)}")
    elif not geral and not ruim:
        print(f"{arquivos[0]}\n  nenhum grifo.")
    return 1 if ruim else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
