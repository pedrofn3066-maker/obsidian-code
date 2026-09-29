#!/usr/bin/env python3
"""
Lê as provas resolvidas (Questoes/Provas/*.md, feitas pelo /absorver-provas) e responde
"quantas provas cobraram este heading?" — a conta por trás do [prova:: N] nas notas.
Não há arquivo de mapa: cada questão diz sozinha quais headings marca.

    python3 PY/provas-recorrencia.py                        # heading → nº de provas, em ordem
    python3 PY/provas-recorrencia.py <termo> [<termo> ...]  # questões cujo heading/tema casa com TODOS os termos
    python3 PY/provas-recorrencia.py --heading "Nota#Heading"   # provas que cobraram exatamente esse heading
    python3 PY/provas-recorrencia.py --conferir             # [prova:: N] nos trackers × provas resolvidas
    python3 PY/provas-recorrencia.py --limpo "<nota>"       # a nota sem nenhuma marca de prova ("-" = stdin)
    python3 PY/provas-recorrencia.py --dir <pasta> ...      # outra pasta de provas (teste)

O que ele lê em cada bloco "### Q<n>" da prova resolvida:
    - o gabarito:  "**Gabarito:** 🟩 D (oficial)"  ou  "⬛ ANULADA (…)"
    - os headings marcados, no bloco "Na matéria":  "> > [[Nota#Heading]] — marcado (callout `Prova anterior`)"
      (também "— mapeado" (questão anulada, sem marca) e "— aviso `Gabarito × nota`"; "— vizinho" não conta)
    - o tema, do título do callout:  "> [!question]- Q31 · Disciplina · Prova — <tema>"

Conta como "cobrou" só a prova com pelo menos uma questão de gabarito A–E (anulada ou sem gabarito
aparece na listagem com marca, mas não entra na contagem). Busca tolera NBSP/acentos.
--limpo existe pra conferir o lastro: o texto sem as marcas tem que ser palavra por palavra o que estava antes:
    python3 PY/provas-recorrencia.py --limpo "$TMPDIR/provas/<nome>.antes.md" > $TMPDIR/A.txt
    python3 PY/provas-recorrencia.py --limpo "<nota>" > $TMPDIR/D.txt
    cmp $TMPDIR/A.txt $TMPDIR/D.txt                      # tem que sair sem diferença
Só lê. Sai com código 1 no --conferir se achar divergência.
"""
import re
import sys
import unicodedata
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
PASTA = VAULT / "Questoes" / "Provas"  # notas de prova resolvida (só questões)
NOTAS = [VAULT / "MATERIAS", VAULT / "LTM ISS SANTOS"]
RE_LINK = re.compile(r"\[\[([^\]|#]+)#([^\]|]+)(?:\|[^\]]*)?\]\]")
RE_TRACKER = re.compile(r"^- \[.\] status\b")
RE_PROVA = re.compile(r"\[prova::\s*(\d+)\]")
# heading marcado numa questão: linha "> > [[Nota#Heading]] — marcado (…)" do bloco "Na matéria"
RE_MARCADO = re.compile(r"(?m)^> > \[\[([^\]#|]+)#([^\]|]+)\]\] — (?:marcado|mapeado|aviso)")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.replace("\xa0", " "))
    return re.sub(r"\s+", " ", "".join(c for c in s if not unicodedata.combining(c))).strip().lower()


def linhas_registro(pasta: Path):
    """Uma linha por heading marcado em cada questão de cada prova resolvida (Questoes/Provas/*.md)."""
    for arq in sorted(pasta.glob("*.md")):
        txt = arq.read_text(encoding="utf-8")
        for m in re.finditer(r"(?m)^### Q(\d+)$\n(.*?)(?=^### Q\d+$|\Z)", txt, re.S):
            q, corpo = m.group(1), m.group(2)
            t = re.search(r"^> \[!question\]-? Q\d+ · ([^·]+) · [^\n]*? — (.*)$", corpo, re.M)
            g = re.search(r"\*\*Gabarito:\*\* (?:🟩 ([A-E])|⬛ (ANULADA))\s*\(([^)]*)\)", corpo)
            if not (t and g):
                continue
            for nota, head in RE_MARCADO.findall(corpo):
                yield {
                    "prova": arq.stem, "q": q, "disc": t.group(1).strip(), "gab": g.group(1) or "ANULADA",
                    "nota": nota, "heading": head, "regra": t.group(2).strip(), "angulo": "", "cob": "",
                    "gab_fonte": g.group(3).strip(),
                }


def valida(r):
    return r["gab"] in list("ABCDE")


def chave(r):
    return f"{r['nota']}#{r['heading']}" if r["nota"] else "(sem heading)"


def por_heading(rows):
    d = {}
    for r in rows:
        d.setdefault(norm(chave(r)), {"rot": chave(r), "provas": set(), "qs": []})
        d[norm(chave(r))]["qs"].append(r)
        if valida(r):
            d[norm(chave(r))]["provas"].add(r["prova"])
    return d


def conferir(rows):
    """[prova:: N] no tracker do heading × contagem dos registros."""
    esperado = {k: len(v["provas"]) for k, v in por_heading(rows).items()}
    achado, ruim = {}, 0
    for raiz in NOTAS:
        for nota in raiz.glob("*.md"):
            heading = None
            for l in nota.read_text(encoding="utf-8").split("\n"):
                m = re.match(r"^#{1,6}\s+(.+)$", l)
                if m:
                    heading = m.group(1).strip()
                    continue
                if heading and RE_TRACKER.match(l):
                    mm = RE_PROVA.search(l)
                    if mm:
                        achado[norm(f"{nota.stem}#{heading}")] = (int(mm.group(1)), f"{nota.stem}#{heading}")
                    heading = None  # só o primeiro tracker do bloco
    for k, (n, rot) in achado.items():
        if esperado.get(k, 0) != n:
            print(f"! {rot}: nota diz [prova:: {n}], registros dizem {esperado.get(k, 0)}")
            ruim += 1
    for k, n in esperado.items():
        if n and k not in achado:
            print(f"? {por_heading(rows)[k]['rot']}: {n} prova(s) nos registros, sem [prova:: N] no tracker "
                  "(heading sem tracker → só o callout aponta; ou marca esquecida)")
    print("OK" if not ruim else f"{ruim} divergência(s)")
    return 1 if ruim else 0


RE_MARCA = re.compile(r'<mark class="prova"[^>]*>(.*?)</mark>')
RE_INICIO_CALLOUT = re.compile(r"^> \[!(?:example|tip|warning)\]-? (?:Prova anterior|Lupa de prova|Gabarito × nota)")


def limpo(txt: str) -> str:
    """Tira o que o /absorver-provas acrescenta: grifo teal, [prova:: N], callouts de prova, linha nas Erradas."""
    saida, dentro = [], False
    for l in txt.split("\n"):
        if dentro and l.startswith(">"):
            continue
        dentro = False
        if RE_INICIO_CALLOUT.match(l):
            dentro = True
            if saida and not saida[-1].strip():
                saida.pop()  # o branco que separava o callout do bloco anterior
            continue
        if l.startswith("> **Prova anterior"):
            if saida and saida[-1].strip() == ">":
                saida.pop()  # o ">" separador que precede a linha nas Erradas
            continue
        l = RE_MARCA.sub(r"\1", l)
        l = re.sub(r" \[prova::\s*\d+\]", "", l)
        saida.append(l)
    return "\n".join(saida)


def main():
    a = sys.argv[1:]
    if a[:1] == ["--limpo"] and len(a) > 1:
        print(limpo(sys.stdin.read() if a[1] == "-" else Path(a[1]).read_text(encoding="utf-8")), end="")
        return
    pasta = PASTA
    if "--dir" in a:
        i = a.index("--dir")
        pasta = Path(a[i + 1])
        del a[i:i + 2]
    if not pasta.exists():
        sys.exit(f"sem provas resolvidas em {pasta} — nenhuma absorvida ainda.")
    rows = list(linhas_registro(pasta))
    if not rows:
        sys.exit("nenhuma questão com heading marcado nas provas resolvidas (ver docstring).")

    if a[:1] == ["--conferir"]:
        sys.exit(conferir(rows))
    if a[:1] == ["--heading"] and len(a) > 1:
        alvo = norm(a[1])
        for r in rows:
            if norm(chave(r)) == alvo:
                marca = "" if valida(r) else "  (não conta: sem gabarito A–E)"
                print(f"{r['prova']} · Q{r['q']} · gab {r['gab']} ({r['gab_fonte']}) — {r['regra']}{marca}")
        n = len(por_heading(rows).get(alvo, {"provas": ()})["provas"])
        print(f"[prova:: {n}]")
        return
    if a:
        termos = [norm(t) for t in a]
        for r in rows:
            alvo = norm(chave(r) + " " + r["regra"] + " " + r["angulo"])
            if all(t in alvo for t in termos):
                print(f"{r['prova']} · Q{r['q']} · gab {r['gab']} · {chave(r)} — {r['regra']}")
        return
    ordem = sorted(por_heading(rows).values(), key=lambda v: (-len(v["provas"]), v["rot"]))
    provas = {r["prova"] for r in rows}
    print(f"{len(provas)} prova(s) absorvida(s), {len(rows)} linha(s)\n")
    for v in ordem:
        print(f"{len(v['provas'])} prova(s) · {len(v['qs'])} questão(ões) · {v['rot']}")


if __name__ == "__main__":
    main()
