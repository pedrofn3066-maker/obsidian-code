#!/usr/bin/env python3
"""
validar-cadernos.py — confere se o frontmatter das notas de Questoes/Diario é YAML válido.

Nota com YAML inválido perde as propriedades no Obsidian e some das consultas do
Dataview (painéis de Diagnóstico, Ganho potencial, Agenda de releitura). O erro que
mais aparece: valor de `obs` que abre com aspas, fecha, e continua com texto
(`obs: "Tópico" é o erro ...`), ou texto solto com `: ` no meio.

Uso:  python3 PY/validar-cadernos.py                    (todas as notas do Diario)
      python3 PY/validar-cadernos.py <nota.md> [...]    (só as indicadas)

Sai com código 1 se achar algum problema. Sem dependências (não usa PyYAML): confere
o formato das linhas `chave: valor` e `- item`, que é tudo que o schema do Diario usa.
"""

import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
RE_ASPAS_DUPLAS = re.compile(r'^"(?:[^"\\]|\\.)*"\s*$')
RE_ASPAS_SIMPLES = re.compile(r"^'(?:[^']|'')*'\s*$")
RE_CHAVE = re.compile(r"^([A-Za-z_][\w-]*):(?:\s+(.*))?$")
RE_ITEM = re.compile(r"^\s+-\s+(.*)$")


def problema_no_valor(v):
    """None se o escalar é válido; senão, o motivo."""
    v = v.strip()
    if not v or v[0] in "[{|>&*!%@`":  # vazio, flow, bloco, âncora: fora do escopo
        return None
    if v[0] == '"':
        if RE_ASPAS_DUPLAS.match(v):
            return None
        return ('abre com aspas duplas mas não fecha no fim do valor — '
                'cite o valor inteiro e escape as aspas internas como \\"')
    if v[0] == "'":
        return None if RE_ASPAS_SIMPLES.match(v) else "aspas simples mal fechadas"
    if ": " in v or v.endswith(":"):
        return "tem dois-pontos sem aspas — o YAML lê como mapa; cite o valor inteiro"
    if " #" in v:
        return "tem ' #' sem aspas — o YAML lê como comentário; cite o valor inteiro"
    return None


def validar(caminho):
    linhas = caminho.read_text(encoding="utf-8").split("\n")
    if not linhas or linhas[0].strip() != "---":
        return [(1, "sem frontmatter")]
    try:
        fim = linhas.index("---", 1)
    except ValueError:
        return [(1, "frontmatter não fecha (falta o segundo ---)")]

    erros = []
    for n, linha in enumerate(linhas[1:fim], start=2):
        if not linha.strip():
            continue
        m_item = RE_ITEM.match(linha)
        m_chave = RE_CHAVE.match(linha)
        if m_item:
            motivo = problema_no_valor(m_item.group(1))
        elif m_chave:
            motivo = problema_no_valor(m_chave.group(2) or "")
        else:
            motivo = "linha que não é `chave: valor` nem `- item`"
        if motivo:
            erros.append((n, motivo))
    return erros


def main():
    if len(sys.argv) > 1:
        alvos = [Path(a) for a in sys.argv[1:]]
    else:
        alvos = sorted((VAULT / "Questoes" / "Diario").glob("*.md"))

    total = 0
    for f in alvos:
        if f.name == "Diario.md":
            continue
        for n, motivo in validar(f):
            total += 1
            print(f"{f.name}:{n}: {motivo}")
    print(f"{total} problema(s) em {len(alvos)} nota(s)." if total else f"OK — {len(alvos)} nota(s) válidas.")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
