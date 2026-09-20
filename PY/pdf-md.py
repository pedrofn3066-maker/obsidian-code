#!/usr/bin/env python3
"""
Extrai o texto de um PDF para um Markdown de trabalho, com marcador de página
(<!-- p.N -->) pra manter o lastro. É a etapa 1 do fluxo "PDF → análise →
distribuição no cofre": o .md gerado NÃO é conteúdo final, é insumo pra leitura
por blocos. Nada em MATERIAS/ é tocado.

    python3 PY/pdf-md.py inbox/L6830.pdf                 # grava em .vault-meta/pdf-md/L6830.md
    python3 PY/pdf-md.py arquivo.pdf -o saida.md
    python3 PY/pdf-md.py arquivo.pdf --diag              # só o diagnóstico, sem gravar

O que faz:
  - junta as linhas de cada parágrafo (o PDF quebra no meio da frase) e refaz
    hifenização de fim de linha
  - descarta cabeçalho/rodapé repetido (linha que aparece em ≥40% das páginas)
    e número de página solto
  - negrito → **negrito**; texto sobre retângulo de fundo amarelo/colorido
    (marca-texto do PDF) → <mark>. Cor da letra NÃO conta: cinza e azul são
    texto normal e link
  - fonte maior que o corpo → heading; linha que abre com "Art. N" ou
    inciso/alínea começa parágrafo novo
  - página com pouquíssimo texto é sinalizada (provável escaneada → precisa OCR)
"""
import argparse
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

import pymupdf

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / ".vault-meta" / "pdf-md"
NOVO_PARAGRAFO = re.compile(
    r"^(\*{0,2}(Art\.?\s*\d|§\s*\d|Parágrafo único|[IVXLC]+\s*[-–—.]|[a-z]\)|\d+\s*[-–.)]\s"
    r"|Biz[úu]|Cuidado|Atenção|Obs\b|Importante))", re.I
)
SO_NUMERO = re.compile(r"^\s*(p[áa]g(ina)?\.?\s*)?\d{1,4}(\s*(/|de)\s*\d{1,4})?\s*$", re.I)


def norm_cabecalho(t: str) -> str:
    return re.sub(r"\d+", "#", re.sub(r"\s+", " ", t)).strip().lower()


def retangulos_de_destaque(pg):
    """Retângulos de fundo coloridos e baixos = marca-texto (branco/cinza/preto não contam)."""
    rs = []
    for dr in pg.get_drawings():
        f = dr.get("fill")
        if not f or len(f) < 3 or dr["rect"].height > 40:
            continue
        if max(f) - min(f) > 0.3:  # tem saturação: amarelo, verde, rosa...
            rs.append(dr["rect"])
    return rs


def linhas_da_pagina(pg):
    """[(y0, tamanho, texto_md)] — uma por linha visual."""
    saida = []
    destaques = retangulos_de_destaque(pg)
    for b in pg.get_text("dict")["blocks"]:
        if b.get("type") != 0:
            continue
        for ln in b["lines"]:
            partes, tam = [], []
            for sp in ln["spans"]:
                t = sp["text"]
                if not t.strip():
                    partes.append(t)
                    continue
                tam.append(sp["size"])
                negrito = bool(sp["flags"] & 16) or "bold" in sp["font"].lower()
                cx = pymupdf.Point((sp["bbox"][0] + sp["bbox"][2]) / 2, (sp["bbox"][1] + sp["bbox"][3]) / 2)
                colorido = any(r.contains(cx) for r in destaques)
                if colorido:
                    t = f"<mark>{t.strip()}</mark> " if t.endswith(" ") else f"<mark>{t}</mark>"
                elif negrito:
                    t = f"**{t.strip()}** " if t.endswith(" ") else f"**{t}**"
                partes.append(t)
            txt = "".join(partes).strip()
            if txt:
                saida.append((ln["bbox"][1], statistics.mean(tam) if tam else 0, txt))
    saida.sort(key=lambda x: x[0])
    return saida


def limpa_marcas(t: str) -> str:
    t = re.sub(r"</mark>(\s*)<mark>", r"\1", t)
    t = re.sub(r"\*\*(\s*)\*\*", r"\1", t)
    t = re.sub(r"\.{5,}", " … ", t)
    return re.sub(r"[ \t]+", " ", t)


def converte(caminho: Path):
    doc = pymupdf.open(caminho)
    paginas = [linhas_da_pagina(p) for p in doc]
    n = len(paginas)

    # cabeçalho/rodapé: normaliza e conta em quantas páginas cada linha aparece
    cont = Counter()
    for ls in paginas:
        for t in {norm_cabecalho(re.sub(r"[*]|</?mark>", "", l[2])) for l in ls}:
            cont[t] += 1
    # ≥12 caracteres: "I", "II", "a)" repetem em toda página mas são incisos, não rodapé
    repetidas = {t for t, c in cont.items() if n >= 4 and c >= max(3, 0.4 * n) and len(t) >= 12}

    tamanhos = [round(l[1]) for ls in paginas for l in ls if l[1]]
    corpo = statistics.mode(tamanhos) if tamanhos else 10

    out, diag = [], {"paginas": n, "corpo_pt": corpo, "esparsas": [], "descartadas": 0}
    for i, ls in enumerate(paginas, 1):
        chars = sum(len(re.sub(r"[*]|</?mark>", "", l[2])) for l in ls
                    if norm_cabecalho(re.sub(r"[*]|</?mark>", "", l[2])) not in repetidas)
        if chars < 80:
            diag["esparsas"].append(i)
        out.append(f"\n<!-- p.{i} -->\n")
        buf, anterior = "", ""

        def fecha():
            nonlocal buf
            if buf.strip():
                out.append(limpa_marcas(buf).strip() + "\n")
            buf = ""

        for k, (_, tam, txt) in enumerate(ls):
            puro = re.sub(r"[*]|</?mark>", "", txt).strip()
            # número solto só é nº de página se for o da página ou estiver na borda dela;
            # um "2027" no meio do texto é ano de vigência e NÃO pode sumir
            eh_pagina = False
            if SO_NUMERO.match(puro):
                nums = [int(x) for x in re.findall(r"\d+", puro)]
                na_borda = k in (0, 1, len(ls) - 2, len(ls) - 1)
                if len(nums) == 2:  # "3 de 51" / "3/51": só se for exatamente página/total
                    eh_pagina = nums == [i, n]
                else:  # nº solto: o da página, ou na borda e plausível como página
                    eh_pagina = nums[0] == i or (na_borda and nums[0] <= n)
            if norm_cabecalho(puro) in repetidas or eh_pagina:
                diag["descartadas"] += 1
                continue
            if tam >= corpo + 2 and len(puro) < 120:
                fecha()
                nivel = "#" if tam >= corpo + 6 else "##" if tam >= corpo + 4 else "###"
                out.append(f"{nivel} {puro}\n")
                continue
            if NOVO_PARAGRAFO.match(puro) and buf:
                fecha()
            if buf.endswith("-") and not buf.endswith(" -"):
                buf = buf[:-1] + txt
            elif re.fullmatch(r"[A-ZÁÉÍÓÚÂÊÔ]", anterior) and puro[:1].islower():
                buf = buf.rstrip() + txt  # letra capitular em linha própria: "N" + "ão"
            else:
                buf = f"{buf} {txt}" if buf else txt
            anterior = puro
        fecha()
    return "\n".join(out).strip() + "\n", diag


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("-o", "--saida", type=Path)
    ap.add_argument("--diag", action="store_true", help="só diagnóstico, não grava")
    a = ap.parse_args()
    if not a.pdf.exists():
        sys.exit(f"não achei {a.pdf}")

    md, d = converte(a.pdf)
    print(f"{a.pdf.name}: {d['paginas']} págs · corpo {d['corpo_pt']}pt · "
          f"{d['descartadas']} linhas de cabeçalho/nº descartadas · {len(md.split())} palavras")
    if d["esparsas"]:
        ps = ", ".join(map(str, d["esparsas"][:15])) + ("…" if len(d["esparsas"]) > 15 else "")
        print(f"⚠️ {len(d['esparsas'])} pág(s) com pouco texto (escaneada/figura?): {ps}")
    if a.diag:
        return
    destino = a.saida or SAIDA / (a.pdf.stem + ".md")
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(f"<!-- fonte: {a.pdf.name} -->\n{md}", encoding="utf-8")
    print(f"→ {destino}")


if __name__ == "__main__":
    main()
