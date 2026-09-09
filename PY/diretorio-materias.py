#!/usr/bin/env python3
"""
Lista as 28 notas de MATERIAS/ com disciplina, bloco, peso e prioridade —
uma tabela compacta pra decidir a QUAL matéria uma captura pertence, sem
abrir 28 frontmatters.

    python3 PY/diretorio-materias.py
    python3 PY/diretorio-materias.py contribuição   # filtra por palavra no nome/disciplina
"""
import re
import sys
from pathlib import Path

PULAR = {"MOC - Direito Tributário.md"}  # mapa de conteúdo, não matéria


def campo(fmatter, nome):
    m = re.search(rf"^{nome}:\s*(.+)$", fmatter, re.M)
    return m.group(1).strip().strip('"') if m else "—"


def linhas():
    out = []
    for f in sorted(Path("MATERIAS").glob("*.md")):
        if f.name in PULAR:
            continue
        txt = f.read_text(encoding="utf-8")
        fim = txt.find("\n---", 3)
        fmatter = txt[3:fim] if txt.startswith("---") and fim > 0 else ""
        out.append({
            "arquivo": f.name,
            "disciplina": campo(fmatter, "disciplina"),
            "bloco": campo(fmatter, "bloco"),
            "peso": campo(fmatter, "peso"),
            "prioridade": campo(fmatter, "prioridade"),
        })
    return out


if __name__ == "__main__":
    filtro = sys.argv[1].lower() if len(sys.argv) > 1 else None
    for r in linhas():
        alvo = f"{r['arquivo']} {r['disciplina']} {r['bloco']}".lower()
        if filtro and filtro not in alvo:
            continue
        print(f"  peso {r['peso']}  {r['prioridade']:<12}  {r['bloco']:<28}  {r['arquivo']}")
