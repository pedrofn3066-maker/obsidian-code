#!/usr/bin/env python3
"""
Separa uma prova antiga em questões (enunciado + alternativas + gabarito) num Markdown
de trabalho, com a página de cada uma. É a etapa 1 do /absorver-provas: o .md gerado NÃO
é conteúdo final, é insumo pra classificar cada questão contra as notas de MATERIAS/.

    python3 PY/prova-questoes.py "<prova.pdf|prova.md>" [--colunas] [--gabarito "<gab.pdf|gab.md|'01:A 02:B ...'>"]
                                 [--tipo N] [-o saida.md] [--diag] [--esqueleto "<título da prova>"]

Grava em .vault-meta/provas/<nome>.md (ignorado pelo git) e imprime o diagnóstico.
Com --esqueleto grava também <nome>.resolvida.md: um bloco "### Qn" por questão, no layout de
TEMPLATE/Prova resolvida.md (enunciado, alternativas com o gabarito em verde, placeholders de
Resposta e Na matéria). É o ponto de partida da prova resolvida; o texto vem do PDF, a resolução
é trabalho do /absorver-provas.
Só lê: nada em MATERIAS/ ou Erradas/ é tocado.

O que faz:
  - PDF → passa por PY/pdf-md.py (mesmo extrator do /absorver-pdf), guarda <!-- p.N -->
  - acha "Questão N" / "QUESTÃO N" (título, negrito ou no meio do parágrafo) e corta o bloco
  - separa as alternativas "(A)" / "A)" / "**A)**"; a disciplina vem do último título curto
  - gabarito: "NN: X" / "NN - X" / "NN X"; se houver "TIPO N" (provas com caderno embaralhado),
    escolhe o tipo do caderno (lido de "TIPO:N" na capa) ou o de --tipo. Sem certeza, PARA.
  - o gabarito pode vir no próprio arquivo da prova ou num PDF separado (--gabarito)

O que NÃO faz (avisa no diagnóstico): PDF escaneado / manuscrito (sem texto), prova em duas
colunas embaralhada, questão sem marcador reconhecível. Nesses casos leia o PDF direto
(Read com pages) e monte a lista à mão — não invente questão.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
PDF_MD = VAULT / "PY" / "pdf-md.py"
SAIDA = VAULT / ".vault-meta" / "provas"

RE_PAG = re.compile(r"<!-- p\.(\d+) -->")
RE_QUESTAO = re.compile(r"(?:#{1,4}\s*)?\*{0,2}\s*(?:QUEST[ÃA]O|Quest[ãa]o)\s+0*(\d{1,3})\b\s*\*{0,2}[.:)\s]")
RE_ALT = re.compile(r"(?:(?<=\s)|^)(?:\*{0,2}\(?([A-E])\)\*{0,2}|([A-E])\s*\(\s*\))\s+(?=\S)")
RE_TITULO = re.compile(r"^#{1,4}\s+(.{3,70})$")
RE_TIPO_CAPA = re.compile(r"TIPO\s*(?:DE PROVA)?\s*[:\-]?\s*(\d)\b", re.I)
RE_GAB = re.compile(r"\b0*(\d{1,3})\s*[:\-–.)]?\s*([A-E]|ANULADA|X)\b")
RE_RODAPE = re.compile(r"\s+[A-ZÀ-Ú]{4,}[A-ZÀ-Ú ,.\-]{12,}\s[-–]\s\d{1,3}\s*$")
IGNORA_TITULO = re.compile(r"ANTES DE INICIAR|INSTRU|TIPO|CADERNO|CONCURSO|PREFEITURA|EDITAL|Quest[ãa]o", re.I)


RE_LIXO = re.compile(r"^(GABARITO PRELIMINAR|voltar|20\d\d\s*©\s*\w+)\s*$")  # ruído de página impressa do site da banca


def colunas_md(pdf: Path) -> str:
    """PDF em duas colunas: linhas da coluna esquerda e depois da direita, cada uma de cima para baixo.
    Linhas em negrito, curtas, sem pontuação e na margem esquerda (título de disciplina) viram '### título'."""
    import pymupdf
    out = [f"<!-- fonte: {pdf.name} (colunas) -->"]
    for i, pg in enumerate(pymupdf.open(str(pdf)), 1):
        meio = pg.rect.width / 2
        ls = []
        for b in pg.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                t = "".join(sp["text"] for sp in l["spans"]).strip()
                if t and not RE_LIXO.match(t):
                    x0, y0 = l["bbox"][0], l["bbox"][1]
                    negrito = all(sp["flags"] & 16 for sp in l["spans"] if sp["text"].strip())
                    ls.append((0 if x0 < meio else 1, round(y0, 1), x0, t, negrito))
        out.append(f"<!-- p.{i} -->\n")
        for _, _, x0, t, negrito in sorted(ls):
            if negrito and x0 < 60 and len(t) < 45 and not re.search(r"[.:;,?]$", t) and not re.match(r"^(Quest|[A-E]\))", t):
                out.append(f"### {t}\n")
            else:
                out.append(re.sub(r"^(Quest[ãa]o\s+\d+)\s*$", r"### \1", t) + ("\n" if t.startswith("Quest") else ""))
    return "\n".join(out)


def gabarito_caixas(pdf: Path) -> dict:
    """PDF que é impressão de página do site da banca: a alternativa do gabarito vem numa caixa verde
    (retângulo vetorial de contorno verde, com 'GABARITO PRELIMINAR'). Devolve {n: letra}. É o gabarito
    PRELIMINAR da página; caixa cortada na quebra de página não é lida (a questão fica de fora)."""
    import pymupdf
    ev = []
    for pi, pg in enumerate(pymupdf.open(str(pdf))):
        for bl in pg.get_text("dict")["blocks"]:
            for ln in bl.get("lines", []):
                t = "".join(sp["text"] for sp in ln["spans"]).strip()
                m = re.match(r"Quest[ãa]o\s+(\d+)\s*$", t)
                if m:
                    ev.append((pi, ln["bbox"][1], "Q", int(m.group(1))))
        for dr in pg.get_drawings():
            c, r = dr.get("color"), dr["rect"]
            if c and abs(c[0]) < 0.1 and 0.4 < c[1] < 0.6 and abs(c[2]) < 0.1 and r.width > 300:
                letra = None
                for bl in pg.get_text("dict", clip=r)["blocks"]:
                    for ln in bl.get("lines", []):
                        t = "".join(sp["text"] for sp in ln["spans"]).strip()
                        m = re.match(r"^([A-E])\)", t) or re.search(r"\s([A-E])\)\s*$", t)
                        if m and letra is None:
                            letra = m.group(1)
                if letra:
                    ev.append((pi, r.y0, "G", letra))
    ev.sort(key=lambda e: (e[0], e[1]))
    res, q = {}, None
    for _, _, tipo, v in ev:
        if tipo == "Q":
            q = v
        elif q is not None and q not in res:
            res[q] = v
    return res


def texto_de(caminho: str, colunas: bool = False) -> str:
    p = Path(caminho)
    if colunas and p.suffix.lower() == ".pdf":
        md = VAULT / ".vault-meta" / "pdf-md" / (p.stem + ".colunas.md")
        md.parent.mkdir(parents=True, exist_ok=True)
        md.write_text(colunas_md(p), encoding="utf-8")
        print(f"{p.name}: extraído por colunas → {md}")
        return md.read_text(encoding="utf-8")
    if p.suffix.lower() == ".pdf":
        SAIDA.parent.mkdir(exist_ok=True)
        tmp = VAULT / ".vault-meta" / "pdf-md" / (p.stem + ".md")
        r = subprocess.run([sys.executable, str(PDF_MD), str(p), "-o", str(tmp)], capture_output=True, text=True)
        print(r.stdout.strip() or r.stderr.strip())
        return tmp.read_text(encoding="utf-8")
    return p.read_text(encoding="utf-8")


def gabaritos(txt: str):
    """{tipo|None: {n: letra}} — quebra por 'TIPO N' quando existir."""
    partes = re.split(r"(?i)\bTIPO\s+(\d)\b\s*[-–:]?", txt)
    if len(partes) == 1:
        return {None: {int(n): l for n, l in RE_GAB.findall(txt)}}
    res = {}
    for i in range(1, len(partes), 2):
        res[int(partes[i])] = {int(n): l for n, l in RE_GAB.findall(partes[i + 1])}
    return {t: g for t, g in res.items() if len(g) >= 5}


def separar(txt: str):
    """Lista de dicts {n, pag, disc, corpo}. A página é a do marcador de questão."""
    pos_pag = [(m.start(), int(m.group(1))) for m in RE_PAG.finditer(txt)]

    def pagina(i):
        p = 1
        for s, n in pos_pag:
            if s <= i:
                p = n
            else:
                break
        return p

    # disciplina = último título curto antes da questão (fora os de cabeçalho/instrução)
    titulos = []
    for m in re.finditer(r"^#{1,4}\s+(.{3,70})$", txt, re.M):
        if not IGNORA_TITULO.search(m.group(1)):
            titulos.append((m.start(), m.group(1).strip("*# ").strip()))

    def disciplina(i):
        d = "?"
        for s, t in titulos:
            if s <= i:
                d = t
            else:
                break
        return d

    marcas = [(m.start(), m.end(), int(m.group(1))) for m in RE_QUESTAO.finditer(txt)]
    out = []
    for k, (ini, fim, n) in enumerate(marcas):
        prox = marcas[k + 1][0] if k + 1 < len(marcas) else len(txt)
        corpo = RE_PAG.sub(" ", txt[fim:prox]).strip()
        corpo = re.sub(r"(?m)^#{1,4}\s+.*$", "", corpo).strip()  # título de disciplina do PDF no fim do bloco
        corpo = RE_RODAPE.sub("", corpo)  # rodapé de página colado no fim ("CARGO ... - 3")
        out.append({"n": n, "pag": pagina(ini), "disc": disciplina(ini), "corpo": corpo})
    return out


def formatar(q, gab):
    corpo = q["corpo"]
    alts = list(RE_ALT.finditer(corpo))
    if len(alts) >= 4:
        enun = corpo[: alts[0].start()].strip()
        linhas = []
        for i, a in enumerate(alts):
            fim = alts[i + 1].start() if i + 1 < len(alts) else len(corpo)
            linhas.append(f"- ({(a.group(1) or a.group(2))}) {corpo[a.end():fim].strip()}")
    else:
        enun, linhas = corpo, []
    g = gab.get(q["n"], "?") if gab else "?"
    cab = f"### Q{q['n']:02d} · {q['disc']} · p.{q['pag']} · gab: {g}"
    return cab + "\n\n" + enun + ("\n\n" + "\n".join(linhas) if linhas else "") + "\n", len(alts)


VERDE = '<mark style="background:#affad1">'


def esqueleto(qs, gab, titulo):
    """Um bloco por questão no layout da prova resolvida; o gabarito em verde, o resto a preencher."""
    out = []
    for q in qs:
        corpo = q["corpo"]
        alts = list(RE_ALT.finditer(corpo))
        g = gab.get(q["n"], "?") if gab else "?"
        if len(alts) >= 4:
            enun = corpo[: alts[0].start()].strip()
            ls = []
            for i, a in enumerate(alts):
                fim = alts[i + 1].start() if i + 1 < len(alts) else len(corpo)
                t = corpo[a.end():fim].strip()
                ls.append(f"> ({(a.group(1) or a.group(2))}) " + (f"{VERDE}{t}</mark>" if (a.group(1) or a.group(2)) == g else t))
            alt_txt = "\n".join(ls)
        else:
            enun, alt_txt = corpo, "> (alternativas: conferir no PDF)"
        enun = "\n>\n".join("> " + ln.strip() for p in enun.split("\n\n") if p.strip() for ln in [" ".join(p.split())]) or "> " + enun
        out.append(
            f"### Q{q['n']}\n\n"
            f"> [!question]- Q{q['n']} · {q['disc']} · {titulo} — <tema>\n"
            f"{enun}\n>\n{alt_txt}\n>\n"
            f"> **Gabarito:** 🟩 {g} · **Minha resolução:** <🟩 X (concorda) | ⚠️ X (diverge)>\n>\n"
            f"> > [!success] ✅ Resposta — {g}\n> > <núcleo da regra; por que cada errada erra>\n>\n"
            f"> > [!info] 🔗 Na matéria\n> > <[[Nota#Heading]] — marcado | lacuna>\n"
            f"> > **Fonte:** <cofre `nota.md:L` | internet URL | resolução própria>\n")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prova")
    ap.add_argument("--gabarito")
    ap.add_argument("--tipo", type=int)
    ap.add_argument("--colunas", action="store_true", help="PDF em duas colunas: extrai coluna esquerda e depois direita")
    ap.add_argument("-o", "--saida")
    ap.add_argument("--diag", action="store_true", help="só o diagnóstico, sem gravar")
    ap.add_argument("--esqueleto", metavar="TÍTULO", help="grava também <nome>.resolvida.md (layout da prova resolvida)")
    a = ap.parse_args()

    txt = texto_de(a.prova, a.colunas)
    qs = separar(txt)
    if not qs:
        sys.exit("⚠️ nenhum marcador 'Questão N' achado — prova escaneada, em colunas ou com outro formato. "
                 "Leia o PDF direto (Read com pages) e monte a lista à mão.")

    # gabarito: arquivo separado, texto solto, ou o próprio arquivo da prova
    if a.gabarito:
        if re.search(r"\d\s*[:\-]\s*[A-E]", a.gabarito) and not Path(a.gabarito).exists():
            fonte_gab = a.gabarito
        else:
            fonte_gab = texto_de(a.gabarito)
    else:
        fonte_gab = txt
    gabs = gabaritos(fonte_gab)
    total = len({q["n"] for q in qs})
    gabs = {t: {n: l for n, l in g.items() if n > 0} for t, g in gabs.items()}
    gabs = {t: g for t, g in gabs.items() if len(g) >= 0.8 * total}  # cobertura mínima: senão é ruído do texto
    tipo_capa = RE_TIPO_CAPA.search(txt[:4000])
    tipo = a.tipo or (int(tipo_capa.group(1)) if tipo_capa else None)
    if not gabs and not a.gabarito and Path(a.prova).suffix.lower() == ".pdf":
        cx = gabarito_caixas(Path(a.prova))
        if len(cx) >= 0.8 * total:
            gabs = {None: cx}
            print(f"gabarito lido das caixas verdes do PDF: {len(cx)} respostas (é o PRELIMINAR da página impressa; "
                  "confira a grade definitiva no site da banca e o edital de recursos)")
    gab = None
    if not gabs:
        print("⚠️ SEM gabarito confiável (nem no arquivo, nem em --gabarito). Passe o PDF/edital do gabarito com --gabarito.")
    elif None in gabs:
        gab = gabs[None]
    else:
        if tipo in gabs:
            gab = gabs[tipo]
        else:
            sys.exit(f"⚠️ gabarito tem tipos {sorted(gabs)} e não achei o tipo do caderno na capa. Rode com --tipo N. "
                     "Provas com caderno embaralhado têm gabaritos diferentes: usar o tipo errado inverte o certo/errado.")

    nums = [q["n"] for q in qs]
    if nums != sorted(nums):
        print("⚠️ questões fora de ordem no texto: PDF em duas colunas embaralhado. Refaça a extração por coluna "
              "(pymupdf, ordenando blocos por coluna e depois por y) ou leia o PDF direto (Read com pages).")
    faltam = sorted(set(range(1, max(nums) + 1)) - set(nums))
    dup = sorted({n for n in nums if nums.count(n) > 1})
    blocos, sem_alt = [], []
    for q in qs:
        b, n_alt = formatar(q, gab)
        blocos.append(b)
        if n_alt < 4:
            sem_alt.append(q["n"])

    print(f"questões: {len(qs)} (nº {min(nums)}–{max(nums)})"
          + (f" · tipo do caderno: {tipo}" if tipo else "")
          + (f" · gabarito: {len(gab)} respostas" if gab else " · SEM gabarito"))
    if faltam:
        print(f"⚠️ números sem bloco: {faltam}")
    if dup:
        print(f"⚠️ números repetidos (marcador de questão citado no meio do texto?): {dup}")
    if sem_alt:
        print(f"⚠️ sem 4+ alternativas separadas (certo/errado, asserção ou quebra ruim — confira no PDF): {sem_alt}")
    if gab and set(gab) != set(nums):
        print(f"⚠️ gabarito × questões não batem: só no gabarito {sorted(set(gab) - set(nums))}, só na prova {sorted(set(nums) - set(gab))}")
    discs = {}
    for q in qs:
        discs.setdefault(q["disc"], []).append(q["n"])
    for d, ns in discs.items():
        print(f"  {d}: Q{ns[0]}–Q{ns[-1]} ({len(ns)})")

    if a.diag:
        return
    destino = Path(a.saida) if a.saida else SAIDA / (Path(a.prova).stem + ".md")
    destino.parent.mkdir(parents=True, exist_ok=True)
    cab = f"<!-- fonte: {Path(a.prova).name}" + (f" · gabarito tipo {tipo}" if tipo else "") + " -->\n\n"
    destino.write_text(cab + "\n".join(blocos), encoding="utf-8")
    print(f"→ {destino}")
    if a.esqueleto:
        esq = destino.with_suffix(".resolvida.md")
        esq.write_text(esqueleto(qs, gab, a.esqueleto), encoding="utf-8")
        print(f"→ {esq}")


if __name__ == "__main__":
    main()
