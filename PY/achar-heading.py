#!/usr/bin/env python3
"""
Acha um heading numa nota de MATERIAS tolerando NBSP e outras variações de
espaço — o Edit tool por string exata já quebrou 3 vezes nesta sessão porque
o vault tem \\xa0 escondido em headings que parecem normais no Obsidian.

Devolve a linha exata (1-indexed) e se o heading tem tracker "- [ ] status"
logo abaixo — a informação que qualquer edição de MATERIAS precisa antes de
tocar no arquivo.

    python3 PY/achar-heading.py "MATERIAS/P1 - Auditoria.md" "Auditoria Fiscal"
"""
import re
import sys
from pathlib import Path


def normaliza(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def acha(caminho: Path, trecho: str):
    linhas = caminho.read_text(encoding="utf-8").split("\n")
    alvo = normaliza(trecho)
    achados = []
    for i, l in enumerate(linhas):
        m = re.match(r"^(#{1,6})\s+(.+)$", l)
        if not m:
            continue
        if alvo in normaliza(m.group(2)):
            prox = linhas[i + 1].strip() if i + 1 < len(linhas) else ""
            tem_tracker = prox.startswith("- [ ] status")
            achados.append((i + 1, len(m.group(1)), m.group(2), tem_tracker))
    return achados


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('uso: python3 PY/achar-heading.py "MATERIAS/<nota>.md" "<trecho do heading>"')
        sys.exit(1)
    resultado = acha(Path(sys.argv[1]), sys.argv[2])
    if not resultado:
        print("nenhum heading bateu.")
        sys.exit(1)
    for linha, nivel, titulo, tem_tracker in resultado:
        marca = "com tracker" if tem_tracker else "SEM tracker (contêiner ou precisa criar)"
        print(f"  linha {linha}  H{nivel}  {marca}  — {titulo!r}")
