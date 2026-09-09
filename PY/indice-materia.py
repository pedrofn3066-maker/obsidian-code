#!/usr/bin/env python3
"""
Índice compacto de uma nota de MATERIAS: tabela VINTEUM (peso do edital + dom)
e a árvore de headings do corpo (onde cada assunto mora, com linha exata).

Existe pra evitar ler a nota inteira só pra achar um heading — nota como
Contabilidade Avançada tem 1400+ linhas. Uso:

    python3 PY/indice-materia.py "MATERIAS/P1 - Direito Financeiro.md"
"""
import re
import sys
from pathlib import Path


def normaliza(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def indice(caminho: Path) -> str:
    txt = caminho.read_text(encoding="utf-8")
    linhas = txt.split("\n")
    fim_fm = txt.find("\n---", 3)
    fmatter = txt[3:fim_fm] if txt.startswith("---") and fim_fm > 0 else ""
    peso_nota = (re.search(r"^peso:\s*(\S+)", fmatter, re.M) or [None, "?"])[1]
    prioridade = (re.search(r"^prioridade:\s*(\S+)", fmatter, re.M) or [None, "?"])[1]

    out = [f"# {caminho.name}  (peso {peso_nota} · prioridade {prioridade})\n"]

    # --- tabela VINTEUM: linhas "- [ ] Tópico [dom:: N] [peso:: P]" dentro
    #     da seção "## Checklist por importância" ---
    m = re.search(r"^## Checklist por importância.*?\n(.*?)(?=\n#{1,4}\s|\Z)", txt, re.S | re.M)
    if m:
        out.append("## VINTEUM (peso do edital × domínio atual)\n")
        linhas_chk = re.findall(
            r"^- \[.\]\s+(.+?)\s*\[dom::\s*(\d+)\]\s*\[peso::\s*([\d.]+)\]",
            m.group(1), re.M,
        )
        linhas_chk.sort(key=lambda r: -float(r[2]))
        for topico, dom, peso in linhas_chk:
            out.append(f"  {peso:>5}%  dom {dom}  {topico}")
        out.append("")

    # --- árvore de headings do corpo, pulando a seção VINTEUM/Checklist ---
    out.append("## Estrutura do corpo (heading → linha → dom)\n")
    fim_meta = 0
    m2 = re.search(r"^## Checklist por importância.*?(?=\n#{1,4}\s)", txt, re.S | re.M)
    if m2:
        fim_meta = txt[: m2.end()].count("\n")

    for i, l in enumerate(linhas):
        if i <= fim_meta:
            continue
        hm = re.match(r"^(#{1,4})\s+(.+)$", l)
        if not hm:
            continue
        nivel, titulo = len(hm.group(1)), normaliza(hm.group(2))
        prox = linhas[i + 1].strip() if i + 1 < len(linhas) else ""
        dm = re.match(r"^- \[.\] status \[dom::\s*(\d+)\]", prox)
        marca = f"  dom {dm.group(1)}" if dm else "  (contêiner)"
        out.append(f"  {'  ' * (nivel - 1)}{'#' * nivel} {titulo}   — linha {i+1}{marca}")

    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("uso: python3 PY/indice-materia.py \"MATERIAS/<nota>.md\"")
        sys.exit(1)
    print(indice(Path(sys.argv[1])))
