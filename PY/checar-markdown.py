#!/usr/bin/env python3
"""
Confere se o Markdown que acabou de entrar numa nota de MATERIAS vai renderizar
no Obsidian. Pega o que já quebrou de fato: tabela recuada dentro de item de
lista (vira bloco de código ou texto solto).

    python3 PY/checar-markdown.py "MATERIAS/<nota>.md"           # só linhas alteradas vs HEAD
    python3 PY/checar-markdown.py "MATERIAS/<nota>.md" --tudo    # arquivo inteiro

Verifica:
  1. linha de tabela com recuo (tabela precisa ficar na margem, com linha em branco antes)
  2. tabela sem linha em branco antes
  3. tabela com nº de colunas diferente do cabeçalho
Sai com código 1 se achar problema.
"""
import re
import subprocess
import sys
from pathlib import Path


def linhas_novas(caminho: Path):
    r = subprocess.run(["git", "diff", "-U0", "--", str(caminho)], capture_output=True, text=True)
    novas = set()
    for m in re.finditer(r"^@@ -\S+ \+(\d+)(?:,(\d+))? @@", r.stdout, re.M):
        ini, n = int(m.group(1)), int(m.group(2) or 1)
        novas.update(range(ini, ini + n))
    return novas


def colunas(l: str) -> int:
    return len(re.findall(r"(?<!\\)\|", l.strip())) - 1


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    caminho = Path(args[0])
    linhas = caminho.read_text(encoding="utf-8").split("\n")
    escopo = None if "--tudo" in sys.argv else linhas_novas(caminho)
    problemas = []
    ncol = None
    for i, l in enumerate(linhas, 1):
        eh_tabela = bool(re.match(r"^\s*\|.*\|\s*$", l))
        if not eh_tabela:
            ncol = None
            continue
        anterior_tabela = i > 1 and re.match(r"^\s*\|.*\|\s*$", linhas[i - 2])
        if not anterior_tabela:
            ncol = colunas(l)
        if escopo is not None and i not in escopo:
            continue
        if re.match(r"^\s+\|", l):
            problemas.append((i, "tabela recuada: vira código/texto solto; ponha na margem"))
        if not anterior_tabela and i > 1 and linhas[i - 2].strip():
            problemas.append((i, "tabela sem linha em branco antes"))
        if ncol is not None and colunas(l) != ncol:
            problemas.append((i, f"{colunas(l)} colunas; cabeçalho tem {ncol}"))
    for i, msg in problemas:
        print(f"linha {i}: {msg}  — {linhas[i-1].strip()[:60]}")
    print("OK" if not problemas else f"{len(problemas)} problema(s)")
    sys.exit(1 if problemas else 0)


main()
