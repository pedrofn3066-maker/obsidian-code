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

Uso:  python3 ~/…/vault-ba/PY/s1-ontem.py
"""

import re
import subprocess
import sys
import tempfile
import webbrowser
from datetime import datetime, time, timedelta
from html import escape
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
PASTAS = ["MATERIAS", "Questoes", "Erradas"]
IGNORAR = "Questoes/Paineis"  # espelha o -"Questoes/Paineis" do bloco 1


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


def inline(txt):
    txt = escape(txt)
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


def render_markdown(texto):
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
    return "\n".join(out)


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
.arquivo .hora { font-weight: 400; }
.arquivo { margin: 1.6rem 0 0; }
.arquivo h3 {
  font-size: .8rem; text-transform: uppercase; letter-spacing: .03em;
  opacity: .55; margin: 0 0 .5rem; font-weight: 600;
}
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


def montar_pagina(itens):
    ontem = (datetime.now().date() - timedelta(days=1)).isoformat()
    partes = [f"<!doctype html><meta charset=utf-8><title>S1 — ontem</title><style>{CSS}</style>",
              "<h1>S1 — o que entrou ontem</h1>",
              f'<div class="sub">bloco 3 · arquivos com mtime de {ontem} + cadernos com data {ontem} · gerado por s1-ontem.py</div>']

    if not itens:
        partes.append(
            f'<div class="vazio">Nenhum arquivo com mtime de {ontem} em MATERIAS, Questoes ou Erradas. '
            "Nota editada ontem e reaberta hoje conta como hoje — ver aviso do bloco 1.</div>"
        )

    for hora, caminho, texto in itens:
        partes.append('<div class="arquivo">')
        partes.append(f'<h3><span class="hora">{escape(hora)}</span> · {escape(caminho)}</h3>')
        if texto.strip():
            partes.append(render_markdown(texto))
        else:
            partes.append('<div class="vazio">Sem texto novo no git desde ontem 00:00 '
                          "(commitado antes, ou só reformatado).</div>")
        partes.append("</div>")

    return "\n".join(partes)


def main():
    itens = [(h, rel, texto_acrescentado(rel)) for h, rel in arquivos_de_ontem()]
    html = montar_pagina(itens)

    destino = Path(tempfile.gettempdir()) / "s1-ontem.html"
    destino.write_text(html, encoding="utf-8")
    webbrowser.open(destino.as_uri())
    print(f"Aberto: {destino}")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        sys.exit(f"git falhou: {e.stderr}")
