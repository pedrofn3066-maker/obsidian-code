#!/usr/bin/env python3
"""
s1-ontem.py — versão legível do bloco 3 do painel "S1 - Revisão de ontem".

Mesma consulta do PY/s1-ontem.sh -p, mas em vez de despejar diff no
terminal, monta uma página HTML (markdown-lite renderizado) e abre no
navegador padrão. Resolve só a leitura — nenhuma fonte nova de dado.

QUAIS arquivos: por mtime (mesma regra do bloco 1 do painel) — é a única fonte
do momento real da escrita; a data de commit atribui tudo ao dia em que você
lembrou de commitar. Também entram os cadernos de Questoes/Diario com `data:` de ontem no frontmatter,
mesmo com mtime de hoje (importação/reescrita) — espelha o bloco 2 do painel.
QUAL texto: linhas acrescentadas nesses arquivos nos
commits desde ontem 00:00 (sem limite superior, pra pegar commit de recuperação
feito hoje) + o que ainda não foi commitado.

Duas seções: "Triagens de ontem" (um cartão por commit `Triagem…` — o que cada
/triar-inbox acrescentou às matérias, com o texto) e "Arquivos de ontem" (por mtime).
Commit de triagem feito no dia seguinte entra se o assunto trouxer "(dd/mm)" de ontem.

A página é feita pra RECUPERAR antes de reler (regra do painel): cada nota vem
fechada, só com hora e nome; o texto aparece ao clicar. Fórmulas $…$ e $$…$$ são
renderizadas com KaTeX (CDN) — sem internet, aparecem como LaTeX cru. Marcas
"lembrei / parcial / não lembrei" ficam no localStorage do navegador, por dia.
Atalhos: j/k navegam, 1/2/3 marcam, e abre/fecha tudo, c liga o modo cloze.

Uso:  python3 ~/…/vault-ba/PY/s1-ontem.py
"""

import re
import subprocess
import sys
import tempfile
import unicodedata
import webbrowser
from datetime import datetime, time, timedelta
from html import escape
from urllib.parse import quote
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
PASTAS = ["MATERIAS", "Questoes", "Erradas"]
IGNORAR = "Questoes/Paineis"  # espelha o -"Questoes/Paineis" do bloco 1
RS, FS = "\x1e", "\x1f"  # separadores que não aparecem em texto normal


def git(*args):
    return subprocess.run(
        ["git", "-c", "core.quotepath=false", *args],
        cwd=VAULT, capture_output=True, text=True, check=True,
    ).stdout


def arquivos_de_ontem():
    """[(hora, caminho_relativo)]: mtime de ontem em ordem de horário, depois os
    cadernos de ontem (data no frontmatter) que o mtime deixou de fora."""
    ontem = datetime.now().date() - timedelta(days=1)
    ini = datetime.combine(ontem, time.min)
    fim = ini + timedelta(days=1)
    achados, vistos = [], set()
    for pasta in PASTAS:
        for f in (VAULT / pasta).rglob("*.md"):
            rel = f.relative_to(VAULT).as_posix()
            if rel.startswith(IGNORAR + "/"):
                continue
            m = datetime.fromtimestamp(f.stat().st_mtime)
            if ini <= m < fim:
                achados.append((m, rel))
                vistos.add(rel)
    achados.sort()
    itens = [(m.strftime("%H:%M"), rel) for m, rel in achados]

    marca = re.compile(rf"^data:\s*{ontem.isoformat()}\s*$", re.M)
    extras = []
    for f in (VAULT / "Questoes" / "Diario").glob("*.md"):
        rel = f.relative_to(VAULT).as_posix()
        if rel in vistos:
            continue
        cabeca = f.read_text(encoding="utf-8").split("\n---", 2)[0]
        if marca.search(cabeca):
            m = datetime.fromtimestamp(f.stat().st_mtime)
            extras.append((rel, f"hoje {m:%H:%M}" if m >= fim else m.strftime("%d/%m %H:%M")))
    return itens + sorted((h, rel) for rel, h in extras)


def texto_acrescentado(rel):
    """Linhas acrescentadas em `rel` nos commits desde ontem 00:00 + não commitado."""
    if not git("ls-files", "--", rel).strip():  # não rastreado: o arquivo inteiro é novo
        return (VAULT / rel).read_text(encoding="utf-8")
    pedacos = []
    for out in (
        git("log", "--since=yesterday.midnight", "-p", "--format=", "--", rel),
        git("diff", "HEAD", "--no-color", "--", rel),
    ):
        pedacos += [t for _, t in parse_diff(out)]
    return "\n\n".join(pedacos)


def triagens_de_ontem():
    """[(rotulo_hora, assunto, hash, [(caminho, texto), ...])] em ordem cronológica.
    Commits `Triagem…` feitos ontem, ou feitos depois mas com "(dd/mm)" de ontem no assunto
    (o /triar-inbox nem sempre commita no mesmo dia)."""
    ontem = datetime.now().date() - timedelta(days=1)
    tag = f"({ontem:%d/%m})"
    out = git(
        "log", "--since=yesterday.midnight", "--grep=^Triagem", "-p",
        f"--format={RS}%h{FS}%ad{FS}%s", "--date=format:%Y-%m-%d %H:%M",
        "--", *PASTAS, f":!{IGNORAR}",
    )
    achados = []
    for chunk in out.split(RS)[1:]:
        header, _, body = chunk.partition("\n")
        h, quando, assunto = header.split(FS, 2)
        dia, hora = quando.split(" ")
        if dia != ontem.isoformat() and tag not in assunto:
            continue
        arquivos = parse_diff(body)
        if arquivos:
            rotulo = hora if dia == ontem.isoformat() else f"commit de {dia[8:]}/{dia[5:7]} {hora}"
            achados.append((quando, rotulo, assunto, h, arquivos))
    return [(r, a, h, f) for _, r, a, h, f in sorted(achados)]


def parse_diff(body):
    """[(caminho, texto_acrescentado), ...] — descarta plumbing e linhas removidas."""
    arquivos = []
    caminho, linhas = None, []
    SKIP = ("index ", "new file mode", "deleted file mode", "old mode",
            "new mode", "similarity index", "rename from", "rename to",
            "--- ", "+++ ", "@@ ")
    for linha in body.splitlines():
        if linha.startswith("diff --git a/"):
            if caminho is not None:
                arquivos.append((caminho, "\n".join(linhas)))
            resto = linha[len("diff --git a/"):]
            i = resto.find(" b/")
            caminho = resto[:i] if i != -1 else resto
            linhas = []
        elif linha.startswith(SKIP):
            continue
        elif linha.startswith("+") and not linha.startswith("+++"):
            linhas.append(linha[1:])
        # linhas removidas e de contexto: bloco 3 é "o que entrou", não diff de leitura
    if caminho is not None:
        arquivos.append((caminho, "\n".join(linhas)))
    return [(c, t) for c, t in arquivos if t.strip()]


# --------------------------------------------------------------------------
# markdown-lite -> HTML (sem dependências externas)
# --------------------------------------------------------------------------

def _wikilink(m):
    # [[Nota#Heading|Apelido]] (ou com \| escapado, sintaxe de dentro de
    # tabela) — mostra só o apelido, título completo no hover.
    alvo, _, apelido = m.group(1).partition("|")
    alvo = alvo.replace("\\", "").strip()
    texto = (apelido or alvo).replace("\\", "").strip()
    return f'<span class="wikilink" title="{alvo}">{texto}</span>'


# Marcação visual do Obsidian (grifo, cor, sublinhado): HTML embutido no markdown.
# O escape() abaixo mostraria a tag como texto; então as tags conhecidas viram
# marcadores antes do escape e voltam depois, com a cor validada. Qualquer outra
# tag continua sendo escapada.
_COR_OK = re.compile(r"^(#[0-9a-fA-F]{3,8}|rgba?\([\d\s.,%]+\)|[a-zA-Z]+)$")
_GRIFOS = {"g-prazo", "g-cond", "g-comp", "g-num"}
_RE_TAG = re.compile(
    r'<mark(?:\s+style="background:\s*([^";]+);?")?\s*>'
    r'|<span\s+style="color:\s*([^";]+);?"\s*>'
    r'|<font\s+color="([^"]+)"\s*>'
    r'|<span(?:\s+class="([\w\- ]+)")?\s*>'
    r'|</(mark|span|font|u)>|<(u)>|<br\s*/?>',
    re.I)


def _cor_opaca(cor):
    """True para fundo sem transparência (#hex): precisa de texto escuro no tema escuro."""
    return cor.startswith("#") and len(cor) in (4, 7)


def _tag_html(m):
    bg, cor_span, cor_font, classe, fecha, abre_u = m.groups()
    t = m.group(0).lower()
    if t.startswith("<mark"):
        if bg and _COR_OK.match(bg.strip()):
            bg = bg.strip()
            extra = ";color:#1c1c1e" if _cor_opaca(bg) else ""
            return f'<mark style="background:{bg}{extra}">'
        return "<mark>"
    if cor_span or cor_font:
        cor = (cor_span or cor_font).strip()
        # preto some no tema escuro: herda a cor do texto
        if not _COR_OK.match(cor) or cor.lower() in ("#000", "#000000", "black"):
            return "<span>"
        return f'<span style="color:{cor}">'
    if t.startswith("<span"):
        cls = [c for c in (classe or "").split() if c in _GRIFOS]
        return f'<span class="{cls[0]}">' if cls else "<span>"
    if fecha:
        return "</span>" if fecha.lower() == "font" else f"</{fecha.lower()}>"
    if abre_u:
        return "<u>"
    return "<br>"


def inline(txt):
    guardadas = []

    def _guardar(m):
        guardadas.append(_tag_html(m))
        return f"\x00{len(guardadas) - 1}\x00"

    # trechos em `crase` são literais: a tag dentro deles continua visível como texto
    def _codigo(m):
        guardadas.append(f"<code>{escape(m.group(1))}</code>")
        return f"\x00{len(guardadas) - 1}\x00"

    txt = re.sub(r"`([^`]+)`", _codigo, txt)
    txt = _RE_TAG.sub(_guardar, txt)
    txt = re.sub(r"==([^=\n]+?)==", lambda m: _guardar_html("<mark>" + m.group(1) + "</mark>", guardadas), txt)
    txt = _inline_base(txt)
    return re.sub(r"\x00(\d+)\x00", lambda m: guardadas[int(m.group(1))], txt)


def _guardar_html(html, guardadas):
    # ==x== e ~~x~~: o conteúdo interno ainda passa pelo escape (não vira HTML cru)
    partes = re.match(r"(<\w+>)(.*)(</\w+>)$", html, re.S)
    guardadas.append(partes.group(1))
    guardadas.append(partes.group(3))
    return f"\x00{len(guardadas) - 2}\x00{partes.group(2)}\x00{len(guardadas) - 1}\x00"


def _inline_base(txt):
    txt = re.sub(r"~~([^~\n]+?)~~", lambda m: "\x01" + m.group(1) + "\x02", txt)
    txt = escape(txt)
    txt = txt.replace("\x01", "<del>").replace("\x02", "</del>")
    txt = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", txt)
    txt = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", txt)
    txt = re.sub(r"`([^`]+)`", r"<code>\1</code>", txt)
    txt = re.sub(r"\[\[([^\]]+)\]\]", _wikilink, txt)
    return txt


CALLOUT_COR = {
    "warning": "#c9a227", "danger": "#c0392b", "bug": "#c0392b",
    "info": "#3a7ebf", "question": "#3a7ebf", "note": "#6b7280",
    "tip": "#2f9e58", "success": "#2f9e58", "example": "#6b7280",
}


def celulas_da_linha(l):
    """Split de linha de tabela markdown respeitando \\| escapado (sintaxe
    do Obsidian pra usar [[Nota\\|Apelido]] dentro de uma célula)."""
    l = l.strip()
    if l.startswith("|"):
        l = l[1:]
    if l.endswith("|"):
        l = l[:-1]
    partes = re.split(r"(?<!\\)\|", l)
    return [p.replace("\\|", "|").strip() for p in partes]


def render_frontmatter(linhas):
    # [chave, valor_simples, [itens_de_lista]] — monta a estrutura antes de
    # gerar HTML, em vez de emendar string fechada (frágil e sem chave certa
    # do tamanho do "</dd>" a cortar).
    entradas = []
    for l in linhas:
        m = re.match(r"^(\w[\w-]*):\s*(.*)$", l)
        if m:
            entradas.append([m.group(1), m.group(2).strip(), []])
        elif l.strip().startswith("- ") and entradas:
            entradas[-1][2].append(l.strip()[2:])
        elif l.strip() and entradas:
            entradas[-1][1] = (entradas[-1][1] + " " + l.strip()).strip()

    html = ['<dl class="frontmatter">']
    for chave, valor, itens in entradas:
        conteudo = inline(valor) if valor else ""
        conteudo += "".join(f"<br>· {inline(item)}" for item in itens)
        html.append(f"<dt>{escape(chave)}</dt><dd>{conteudo}</dd>")
    html.append("</dl>")
    return "\n".join(html)


# --------------------------------------------------------------------------
# matemática: protegida antes do markdown-lite, renderizada no navegador
# --------------------------------------------------------------------------

MI, MF = "\ue000", "\ue001"  # delimitam o marcador de uma fórmula guardada
RE_MATH_BLOCO = re.compile(r"\$\$(.+?)\$\$", re.S)
# $…$ em linha, regra do pandoc: sem espaço logo após o $ de abertura nem antes do de
# fechamento, e o de fechamento não vem seguido de dígito/letra. Isso deixa "R$ 100 e
# R$ 200" em paz. O (?<![\w\\$]) impede abrir depois de letra (R$) ou de \$.
RE_MATH_LINHA = re.compile(r"(?<![\w\\$])\$(?=[^\s$])((?:[^$\n\\]|\\.)*?(?:[^\s$\\]|\\\S))\$(?![\w$])")
RE_CODIGO_INLINE = re.compile(r"(`[^`\n]*`)")
RE_MARCADOR = re.compile(rf"{MI}([di])(\d+){MF}")


def proteger_matematica(texto):
    """Troca cada fórmula por um marcador que o markdown-lite não sabe mexer.
    Devolve (texto_com_marcadores, [latex, ...]). Fórmula dentro de `crase` não conta."""
    guardadas = []

    def guardar(tipo, tabela=False):
        def _sub(m):
            tex = m.group(1).strip()
            if tabela:  # em célula de tabela o Obsidian lê \| como um | literal
                tex = tex.replace("\\|", "|")
            guardadas.append(tex)
            return f"{MI}{tipo}{len(guardadas) - 1}{MF}"
        return _sub

    texto = RE_MATH_BLOCO.sub(guardar("d"), texto)
    linhas = []
    for linha in texto.split("\n"):
        sub = guardar("i", tabela=linha.lstrip().startswith("|"))
        partes = RE_CODIGO_INLINE.split(linha)  # índices ímpares são os trechos em `crase`
        linhas.append("".join(
            p if i % 2 else RE_MATH_LINHA.sub(sub, p) for i, p in enumerate(partes)
        ))
    return "\n".join(linhas), guardadas


def restaurar_matematica(html, guardadas):
    """Marcador -> <span class="m" data-tex=…> com o LaTeX cru dentro. Se o KaTeX não
    carregar (sem internet) o leitor ainda vê a fórmula, só não formatada."""
    def _sub(m):
        display = m.group(1) == "d"
        tex = guardadas[int(m.group(2))]
        delim = "$$" if display else "$"
        return (f'<span class="m{" d" if display else ""}" data-tex="{escape(tex)}">'
                f'{escape(delim + tex + delim)}</span>')
    return RE_MARCADOR.sub(_sub, html)


def render_markdown(texto):
    texto, formulas = proteger_matematica(texto)
    linhas = texto.split("\n")
    out = []

    # frontmatter só quando o bloco acrescentado começa mesmo em "---"
    if linhas and linhas[0].strip() == "---":
        try:
            fim = linhas.index("---", 1)
            out.append(render_frontmatter(linhas[1:fim]))
            linhas = linhas[fim + 1:]
        except ValueError:
            pass

    buf, modo = [], None  # modo: None | "p" | "ul" | "ol" | "bq" | "table"

    def flush():
        nonlocal buf, modo
        if not buf:
            modo = None
            return
        if modo == "p":
            out.append(f"<p>{inline(' '.join(buf))}</p>")
        elif modo == "ul":
            out.append("<ul>" + "".join(f"<li>{inline(b)}</li>" for b in buf) + "</ul>")
        elif modo == "ol":
            out.append("<ol>" + "".join(f"<li>{inline(b)}</li>" for b in buf) + "</ol>")
        elif modo == "bq":
            texto = " ".join(buf)
            m = re.match(r"^\[!(\w+)\][+-]?\s*(.*)$", texto)
            if m:
                tipo, resto = m.group(1), m.group(2)
                cor = CALLOUT_COR.get(tipo.lower(), "#6b7280")
                out.append(
                    f'<blockquote class="callout" style="border-left-color:{cor}">'
                    f'<span class="callout-tipo" style="color:{cor}">{escape(tipo.capitalize())}</span> '
                    f'{inline(resto)}</blockquote>'
                )
            else:
                out.append(f"<blockquote>{inline(texto)}</blockquote>")
        elif modo == "table":
            linhas_tbl = [l for l in buf if not re.match(r"^\|?[\s:|-]+\|?$", l)]
            if linhas_tbl:
                head, *corpo = [celulas_da_linha(l) for l in linhas_tbl]
                th = "".join(f"<th>{inline(c)}</th>" for c in head)
                trs = "".join(
                    "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
                    for r in corpo
                )
                out.append(f"<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>")
        buf, modo = [], None

    for linha in linhas:
        s = linha.strip()
        h = re.match(r"^(#{1,6})\s+(.+)$", s)
        cb = re.match(r"^>\s?(.*)$", s)
        li = re.match(r"^[-*]\s+(.+)$", s)
        ol = re.match(r"^\d+[.)]\s+(.+)$", s)
        tbl = s.startswith("|")

        if not s:
            flush()
        elif re.fullmatch(rf"{MI}d\d+{MF}", s):  # $$…$$ sozinho: bloco próprio
            flush()
            out.append(s)
        elif h:
            flush()
            nivel = min(6, len(h.group(1)) + 2)
            out.append(f"<h{nivel}>{inline(h.group(2))}</h{nivel}>")
        elif s == "---":
            flush()
            out.append("<hr>")
        elif cb:
            if modo != "bq":
                flush()
                modo = "bq"
            buf.append(cb.group(1))
        elif li:
            if modo != "ul":
                flush()
                modo = "ul"
            buf.append(li.group(1))
        elif ol:
            if modo != "ol":
                flush()
                modo = "ol"
            buf.append(ol.group(1))
        elif tbl:
            if modo != "table":
                flush()
                modo = "table"
            buf.append(s)
        else:
            if modo != "p":
                flush()
                modo = "p"
            buf.append(s)
    flush()
    return restaurar_matematica("\n".join(out), formulas)


# --------------------------------------------------------------------------
# página
# --------------------------------------------------------------------------

CSS = """
:root { color-scheme: light dark; }
body {
  max-width: 46rem; margin: 3rem auto; padding: 0 1.5rem 6rem;
  font: 17px/1.65 -apple-system, "SF Pro Text", "Helvetica Neue", sans-serif;
  color: #1c1c1e; background: #fdfdfb;
}
@media (prefers-color-scheme: dark) { body { color: #e7e7e5; background: #16161a; } }
h1 { font-size: 1.5rem; margin-bottom: .2rem; }
.sub { opacity: .6; margin-bottom: 2.5rem; }
.barra {
  position: sticky; top: 0; z-index: 5; display: flex; flex-wrap: wrap; gap: .5rem .8rem;
  align-items: center; padding: .6rem 0; margin-bottom: .4rem;
  background: inherit; border-bottom: 1px solid rgba(128,128,128,.25); font-size: .9rem;
}
.barra .sp { flex: 1; }
button, .acoes a {
  font: inherit; font-size: .82rem; padding: .25rem .7rem; border-radius: 6px; cursor: pointer;
  border: 1px solid rgba(128,128,128,.4); background: transparent; color: inherit; text-decoration: none;
}
button:hover, .acoes a:hover { background: rgba(128,128,128,.15); }
button.on { background: rgba(74,125,187,.25); border-color: #4a7dbb; }
.ajuda { font-size: .78rem; opacity: .55; margin: .3rem 0 1.4rem; }
details.nota { border-bottom: 1px solid rgba(128,128,128,.2); }
details.nota > summary {
  list-style: none; cursor: pointer; padding: .7rem .2rem; display: flex; flex-wrap: wrap;
  gap: .2rem .7rem; align-items: baseline; border-radius: 6px;
}
details.nota > summary::-webkit-details-marker { display: none; }
details.nota > summary::before { content: "▸"; opacity: .5; }
details.nota[open] > summary::before { content: "▾"; }
details.nota > summary:focus-visible { outline: 2px solid #4a7dbb; }
.hora { opacity: .55; font-size: .85rem; white-space: nowrap; }
.nome { font-weight: 600; flex: 1 1 14rem; min-width: 0; overflow-wrap: anywhere; }
.badge { font-size: .78rem; opacity: .65; }
.marca { margin-left: auto; font-size: .78rem; white-space: nowrap; }
details.nota[data-m="l"] .marca { color: #2f9e58; }
details.nota[data-m="p"] .marca { color: #c9a227; }
details.nota[data-m="n"] .marca { color: #c0392b; }
details.nota[data-m="l"] > summary .nome { opacity: .55; }
.conteudo { padding: .2rem .4rem .6rem 1.4rem; }
.acoes { display: flex; flex-wrap: wrap; gap: .5rem; padding: .3rem 0 1.1rem 1.6rem; }
.sec { font-size: 1rem; margin: 1.8rem 0 .2rem; opacity: .75; }
.arq { display: flex; gap: .7rem; align-items: baseline; font-size: .8rem; opacity: .65; margin: 1rem 0 .2rem; }
.arq a { color: inherit; }
.m.d { display: block; text-align: center; margin: .8rem 0; overflow-x: auto; }
.conteudo { overflow-wrap: anywhere; }
.conteudo table { display: block; max-width: 100%; overflow-x: auto; }
body.cloze .conteudo strong:not(.aberto) {
  filter: blur(.4em); cursor: pointer; user-select: none; transition: filter .15s;
}
body.cloze .conteudo strong.aberto { background: rgba(201,162,39,.25); border-radius: 3px; }
h4, h5, h6 { margin: 1.2rem 0 .4rem; }
h4 { font-size: 1.05rem; } h5 { font-size: .95rem; } h6 { font-size: .9rem; opacity: .8; }
p { margin: .6rem 0; }
ul, ol { margin: .5rem 0; padding-left: 1.4rem; }
li { margin: .25rem 0; }
blockquote {
  margin: .8rem 0; padding: .3rem 1rem; border-left: 3px solid rgba(128,128,128,.4);
  opacity: .85; font-size: .95rem;
}
blockquote.callout { opacity: 1; }
.callout-tipo { font-weight: 700; text-transform: uppercase; font-size: .75rem; letter-spacing: .03em; }
mark { background: rgba(255,225,0,.35); color: inherit; border-radius: 3px; padding: 0 .12em; }
del { opacity: .6; }
:root {
  --g-prazo-bg: #d8e9cf; --g-prazo-bd: #6f9a5e; --g-cond-bg: #d3deec; --g-cond-bd: #5b7fa8;
  --g-comp-bg: #f7e2a4; --g-comp-bd: #c4961a; --g-num-bg: #e8d7ec; --g-num-bd: #9a6aa8;
}
@media (prefers-color-scheme: dark) { :root {
  --g-prazo-bg: rgba(125,175,105,.24); --g-prazo-bd: #8fbf7c; --g-cond-bg: rgba(100,145,200,.24); --g-cond-bd: #82a8d6;
  --g-comp-bg: rgba(220,175,50,.22); --g-comp-bd: #dcb44a; --g-num-bg: rgba(175,125,190,.26); --g-num-bd: #bf93cc;
} }
.g-prazo { --g-bg: var(--g-prazo-bg); --g-bd: var(--g-prazo-bd); --g-traco: solid; }
.g-cond { --g-bg: var(--g-cond-bg); --g-bd: var(--g-cond-bd); --g-traco: dashed; }
.g-comp { --g-bg: var(--g-comp-bg); --g-bd: var(--g-comp-bd); --g-traco: dotted; }
.g-num { --g-bg: var(--g-num-bg); --g-bd: var(--g-num-bd); --g-traco: double; --g-esp: 3px; }
.g-prazo, .g-cond, .g-comp, .g-num {
  background: var(--g-bg); border-bottom: var(--g-esp, 2px) var(--g-traco) var(--g-bd);
  border-radius: 3px 3px 0 0; padding: 0 .12em; -webkit-box-decoration-break: clone; box-decoration-break: clone;
}
mark .g-prazo, mark .g-cond, mark .g-comp, mark .g-num { background: transparent; }
code { background: rgba(128,128,128,.15); padding: .1em .35em; border-radius: 4px; font-size: .9em; }
.wikilink { color: #4a7dbb; }
table { border-collapse: collapse; margin: .8rem 0; font-size: .9rem; }
th, td { border: 1px solid rgba(128,128,128,.3); padding: .3rem .6rem; text-align: left; }
dl.frontmatter {
  font-size: .85rem; opacity: .75; display: grid; grid-template-columns: auto 1fr;
  gap: .15rem .8rem; margin: 0 0 1rem;
}
dl.frontmatter dt { font-weight: 600; }
dl.frontmatter dd { margin: 0; }
.vazio { opacity: .5; font-style: italic; margin-top: 3rem; }
"""


RE_TOTAL = re.compile(r"^total:\s*(\d+)", re.M)
RE_ACERTOS = re.compile(r"^acertos:\s*(\d+)", re.M)

KATEX = """<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>"""
JS = r"""
(function () {
  var DIA = "__DIA__";
  var ROT = { l: "✓ lembrei", p: "~ parcial", n: "✗ não lembrei" };
  var notas = [].slice.call(document.querySelectorAll("details.nota"));

  function ler(k) { try { return localStorage.getItem("s1:" + DIA + ":" + k); } catch (e) { return null; } }
  function gravar(k, v) {
    try { if (v) localStorage.setItem("s1:" + DIA + ":" + k, v); else localStorage.removeItem("s1:" + DIA + ":" + k); }
    catch (e) {}
  }

  function pintar(d) {
    var m = ler(d.dataset.k) || "";
    d.dataset.m = m;
    d.querySelector(".marca").textContent = m ? ROT[m] : "";
  }
  function contar() {
    var c = { l: 0, p: 0, n: 0 };
    notas.forEach(function (d) { if (d.dataset.m) c[d.dataset.m]++; });
    document.getElementById("cont").textContent =
      (c.l + c.p + c.n) + "/" + notas.length + " revisadas · ✓ " + c.l + " · ~ " + c.p + " · ✗ " + c.n;
  }

  function foco(d) {
    var s = d.querySelector("summary");
    s.focus();
    s.scrollIntoView({ block: "center", behavior: "smooth" });
  }
  function atual() {
    var a = document.activeElement, d = a && a.closest ? a.closest("details.nota") : null;
    return d || notas.filter(function (x) { return x.open; })[0] || notas[0];
  }
  // Depois de marcar: fecha a nota e leva o foco pra próxima SEM marca — sem abrir, pra
  // manter recuperar-antes-de-reler.
  function marcar(d, m) {
    gravar(d.dataset.k, d.dataset.m === m ? "" : m);
    pintar(d); contar(); d.open = false;
    var i = notas.indexOf(d), prox = null;
    for (var j = 1; j <= notas.length; j++) {
      var x = notas[(i + j) % notas.length];
      if (!x.dataset.m) { prox = x; break; }
    }
    foco(prox || d);
  }

  function tudo() {
    var abrir = notas.some(function (d) { return !d.open; });
    notas.forEach(function (d) { d.open = abrir; });
    document.getElementById("b-tudo").textContent = abrir ? "Recolher tudo" : "Expandir tudo";
  }
  function cloze() {
    document.getElementById("b-cloze").classList.toggle("on", document.body.classList.toggle("cloze"));
  }

  notas.forEach(function (d) {
    pintar(d);
    [].forEach.call(d.querySelectorAll(".acoes button"), function (b) {
      b.addEventListener("click", function () { marcar(d, b.dataset.m); });
    });
  });
  contar();
  document.getElementById("b-tudo").addEventListener("click", tudo);
  document.getElementById("b-cloze").addEventListener("click", cloze);
  document.getElementById("b-limpar").addEventListener("click", function () {
    if (!confirm("Limpar as marcas de hoje?")) return;
    notas.forEach(function (d) { gravar(d.dataset.k, ""); pintar(d); });
    contar();
  });
  document.addEventListener("click", function (e) {
    var t = e.target;
    if (document.body.classList.contains("cloze") && t.tagName === "STRONG" && t.closest(".conteudo"))
      t.classList.toggle("aberto");
  });
  document.addEventListener("keydown", function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey || !notas.length) return;
    var k = e.key;
    if (k === "j" || k === "k") {
      e.preventDefault();
      var i = notas.indexOf(atual());
      foco(notas[k === "j" ? Math.min(notas.length - 1, i + 1) : Math.max(0, i - 1)]);
    } else if (k === "1" || k === "2" || k === "3") {
      marcar(atual(), { "1": "l", "2": "p", "3": "n" }[k]);
    } else if (k === "e") { tudo(); }
    else if (k === "c") { cloze(); }
  });

  // KaTeX: renderiza cada .m pelo LaTeX guardado (não varre o texto atrás de $, então
  // "R$ 100" nunca vira fórmula). Se o KaTeX não carregar, o LaTeX cru continua legível.
  window.addEventListener("load", function () {
    if (!window.katex) return;
    [].forEach.call(document.querySelectorAll(".m"), function (el) {
      try {
        katex.render(el.dataset.tex, el, { displayMode: el.classList.contains("d"), throwOnError: false });
      } catch (e) {}
    });
  });
})();
"""


def resumo_caderno(texto):
    """'20/23 · 87%' para nota de caderno (frontmatter acrescentado com total/acertos)."""
    t, a = RE_TOTAL.search(texto), RE_ACERTOS.search(texto)
    if not (t and a) or int(t.group(1)) == 0:
        return ""
    total, acertos = int(t.group(1)), int(a.group(1))
    return f"{acertos}/{total} · {round(100 * acertos / total)}%"


def _obsidian(caminho):
    nome = caminho[:-3] if caminho.endswith(".md") else caminho
    return f"obsidian://open?vault={quote(VAULT.name)}&file={quote(nome, safe='')}"


def _cartao(chave, hora, nome, badge, corpo, acoes_extra=""):
    return (
        f'<details class="nota" data-k="{escape(chave)}">'
        f'<summary><span class="hora">{escape(hora)}</span><span class="nome">{escape(nome)}</span>'
        + (f'<span class="badge">{escape(badge)}</span>' if badge else "")
        + '<span class="marca"></span></summary>'
        f'<div class="conteudo">{corpo}</div>'
        '<div class="acoes"><button data-m="l">1 · Lembrei</button>'
        '<button data-m="p">2 · Parcial</button><button data-m="n">3 · Não lembrei</button>'
        f"{acoes_extra}</div></details>"
    )


def montar_pagina(itens, triagens=()):
    ontem = (datetime.now().date() - timedelta(days=1)).isoformat()
    partes = [f'<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">'
              f"<title>S1 — ontem</title>{KATEX}<style>{CSS}</style>",
              "<h1>S1 — o que entrou ontem</h1>",
              f'<div class="sub">{ontem} · gerado por s1-ontem.py</div>']

    if not itens and not triagens:
        partes.append(
            f'<div class="vazio">Nenhuma triagem e nenhum arquivo com mtime de {ontem} em MATERIAS, '
            "Questoes ou Erradas. Nota editada ontem e reaberta hoje conta como hoje — ver aviso do bloco 1.</div>"
        )
        return "\n".join(partes)

    partes.append(
        '<div class="barra"><strong id="cont"></strong><span class="sp"></span>'
        '<button id="b-tudo">Expandir tudo</button><button id="b-cloze">Cloze</button>'
        '<button id="b-limpar">Limpar marcas</button></div>'
        '<div class="ajuda">Leia só os nomes e tente lembrar o que você acrescentou; abra depois. '
        "j/k navegam · Enter abre · 1 lembrei · 2 parcial · 3 não lembrei · e abre/fecha tudo · "
        "c cloze (borra os termos em negrito; clique para revelar)</div>"
    )

    # O macOS guarda alguns nomes com acento decomposto e o git devolve composto: sem
    # normalizar, "Finanças" do disco != "Finanças" do git e o selo some.
    nfc = lambda c: unicodedata.normalize("NFC", c)
    em_triagem = {nfc(c) for _, _, _, arqs in triagens for c, _ in arqs}

    partes.append(f'<h2 class="sec">Triagens de ontem ({len(triagens)})</h2>')
    if not triagens:
        partes.append('<div class="vazio">Nenhum commit "Triagem…" de ontem (nem com a data de ontem no assunto).</div>')
    for rotulo, assunto, h, arquivos in triagens:
        corpo = "".join(
            f'<div class="arq"><span>{escape(c)}</span><a href="{escape(_obsidian(c))}">Abrir no Obsidian ↗</a></div>'
            + render_markdown(t)
            for c, t in arquivos
        )
        partes.append(_cartao(f"t:{h}", rotulo, assunto, f"{len(arquivos)} nota(s)", corpo))

    partes.append(f'<h2 class="sec">Arquivos de ontem ({len(itens)}) · por mtime + cadernos com data {ontem}</h2>')
    for hora, caminho, texto in itens:
        nome = caminho[:-3] if caminho.endswith(".md") else caminho
        badge = " · ".join(b for b in (resumo_caderno(texto), "via triagem" if nfc(caminho) in em_triagem else "") if b)
        corpo = (render_markdown(texto) if texto.strip() else
                 "Sem texto novo no git desde ontem 00:00 (commitado antes, ou só reformatado).")
        if not texto.strip():
            corpo = f'<span class="vazio">{corpo}</span>'
        partes.append(_cartao(caminho, hora, nome, badge, corpo,
                              f'<a href="{escape(_obsidian(caminho))}">Abrir no Obsidian ↗</a>'))

    partes.append(f"<script>{JS.replace('__DIA__', ontem)}</script>")
    return "\n".join(partes)


def main():
    itens = [(h, rel, texto_acrescentado(rel)) for h, rel in arquivos_de_ontem()]
    html = montar_pagina(itens, triagens_de_ontem())

    destino = Path(tempfile.gettempdir()) / "s1-ontem.html"
    destino.write_text(html, encoding="utf-8")
    webbrowser.open(destino.as_uri())
    print(f"Aberto: {destino}")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        sys.exit(f"git falhou: {e.stderr}")
