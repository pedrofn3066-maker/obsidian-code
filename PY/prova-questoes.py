#!/usr/bin/env python3
"""
Separa uma prova antiga em questões (enunciado + alternativas + gabarito) num Markdown
de trabalho, com a página de cada uma. É a etapa 1 do /absorver-provas: o .md gerado NÃO
é conteúdo final, é insumo pra classificar cada questão contra as notas de MATERIAS/.

    python3 PY/prova-questoes.py "<prova.pdf|prova.md>" [--gabarito "<gab.pdf|gab.md|'01:A 02:B ...'>"]
                                 [--tipo N] [-o saida.md] [--diag]

Grava em .vault-meta/provas/<nome>.md (ignorado pelo git) e imprime o diagnóstico.
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
RE_ALT = re.compile(r"(?:(?<=\s)|^)\*{0,2}\(?([A-E])\)\*{0,2}\s+(?=\S)")
RE_TITULO = re.compile(r"^#{1,4}\s+(.{3,70})$")
RE_TIPO_CAPA = re.compile(r"TIPO\s*(?:DE PROVA)?\s*[:\-]?\s*(\d)\b", re.I)
RE_GAB = re.compile(r"\b0*(\d{1,3})\s*[:\-–.)]?\s*([A-E]|ANULADA|X)\b")
RE_RODAPE = re.compile(r"\s+[A-ZÀ-Ú][A-ZÀ-Ú ,.\-]{15,}\s-\s\d{1,3}\s*$")
IGNORA_TITULO = re.compile(r"ANTES DE INICIAR|INSTRU|TIPO|CADERNO|CONCURSO|PREFEITURA|EDITAL|Quest[ãa]o", re.I)


def texto_de(caminho: str) -> str:
    p = Path(caminho)
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
            linhas.append(f"- ({a.group(1)}) {corpo[a.end():fim].strip()}")
    else:
        enun, linhas = corpo, []
    g = gab.get(q["n"], "?") if gab else "?"
    cab = f"### Q{q['n']:02d} · {q['disc']} · p.{q['pag']} · gab: {g}"
    return cab + "\n\n" + enun + ("\n\n" + "\n".join(linhas) if linhas else "") + "\n", len(alts)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prova")
    ap.add_argument("--gabarito")
    ap.add_argument("--tipo", type=int)
    ap.add_argument("-o", "--saida")
    ap.add_argument("--diag", action="store_true", help="só o diagnóstico, sem gravar")
    a = ap.parse_args()

    txt = texto_de(a.prova)
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


if __name__ == "__main__":
    main()
