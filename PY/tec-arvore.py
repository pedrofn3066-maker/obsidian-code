#!/usr/bin/env python3
"""
Monta a árvore de assuntos do TecConcursos para as matérias do cofre.

As páginas públicas `tecconcursos.com.br/materias/<matéria>` embutem a árvore
inteira (hierarquia + total de questões por assunto) num `var jsonMateria`,
sem exigir login. Serve para escolher o nó certo em Filtros → Assunto ao
montar caderno.

    python3 PY/tec-arvore.py                imprime a nota no stdout
    python3 PY/tec-arvore.py --gravar       grava em "Questoes/TEC - Árvore de assuntos.md"
    python3 PY/tec-arvore.py --so direito-tributario   só essa matéria (stdout)

Usa `curl` (o urllib do Python falha na verificação de certificado atrás do
proxy do sandbox). No sandbox do Claude, o host www.tecconcursos.com.br
precisa estar liberado. A tabela MAPA abaixo é o casamento sugerido entre
matéria do TEC e nota do cofre: ajuste quando o vault mudar.
"""
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "Questoes" / "TEC - Árvore de assuntos.md"
URL = "https://www.tecconcursos.com.br/materias/{}"

MAPA = [  # (slug no TEC, notas do cofre)
    ("lingua-portuguesa-portugues", ["P1 - Língua Portuguesa"]),
    ("administracao-geral-e-publica", ["P1 - Administração Geral", "P1 - Administração e Governança Pública"]),
    ("direito-administrativo-doutrina-e-leis-federais", ["P1 - Direito Administrativo"]),
    ("direito-constitucional-cf1988-e-doutrina", ["P1 - Direito Constitucional"]),
    ("direito-civil", ["P1 - Direito Civil"]),
    ("direito-penal", ["P1 - Penal"]),
    ("afo-direito-financeiro-e-contabilidade-publica", ["P1 - Direito Financeiro", "P2 - CASP"]),
    ("contabilidade-geral", ["P1 - Contabilidade Geral", "P2 - Contabilidade Avançada e de Custos"]),
    ("contabilidade-de-custos", ["P2 - Contabilidade Avançada e de Custos"]),
    ("auditoria-governamental-e-controle", ["P1 - Auditoria"]),
    ("auditoria-privada", ["P1 - Auditoria"]),
    ("estatistica", ["P1 - Estatística", "P2 - Estatística Aplicada"]),
    ("raciocinio-logico", ["P1 - Raciocínio Lógico"]),
    ("matematica-financeira", ["P2 - Matemática Financeira"]),
    ("economia-e-financas-publicas", ["P1 - Macro Economia", "P1 - Micro e Finanças Públicas", "P2 - Finanças Públicas"]),
    ("direito-tributario", ["P2 - Direito Tributário", "P2 - Reforma Tributária"]),
    ("legislacao-tributaria-dos-estados-e-do-distrito-federal", ["P2 - Legislação Tributária Estadual (BA)"]),
    ("ti-banco-de-dados", ["P2 - Fluência de Dados BD"]),
    ("ti-ciencia-de-dados-e-inteligencia-artificial", ["P2 - Fluência de Dados CD"]),
    ("ti-gestao-e-governanca-de-ti", ["P2 - Tecnologia da Informação"]),
    ("informatica", ["P2 - Tecnologia da Informação"]),
]

# Matérias com árvore enorme (uma por estado): só estes prefixos de hierarquia.
SO_RAMOS = {"legislacao-tributaria-dos-estados-e-do-distrito-federal": ("01", "06")}  # Normas Gerais e Bahia


def baixa(slug):
    proc = subprocess.run(
        ["curl", "-sS", "-m", "40", "-A", "Mozilla/5.0", URL.format(slug)],
        capture_output=True, text=True,
    )
    html = proc.stdout
    i = html.find("var jsonMateria")
    if i < 0:
        sys.exit(f"{slug}: sem jsonMateria na página ({proc.stderr.strip() or 'HTTP ok, estrutura mudou?'})")
    obj, _ = json.JSONDecoder().raw_decode(html[html.index("{", i):])
    return obj


def conta(nos):
    return sum(1 + conta(n.get("filhos") or []) for n in nos)


def desce(nos, nivel, saida):
    for n in nos:
        hier = (n.get("hierarquia") or "") + " " if n.get("hierarquia") else ""
        saida.append("  " * nivel + f"- {hier}{n['nome']} ({n.get('totalQuestoes', '?')})")
        desce(n.get("filhos") or [], nivel + 1, saida)


def milhar(n):
    return f"{n:,}".replace(",", ".")


def secao(slug, notas):
    m = baixa(slug)
    assuntos = m["assuntos"]
    filtrado = slug in SO_RAMOS
    if filtrado:
        assuntos = [n for n in assuntos if (n.get("hierarquia") or "")[:2] in SO_RAMOS[slug]]
    linhas = [f"## {m['nome']}", ""]
    linhas.append(
        f"{milhar(m['totalQuestoes'])} questões no TEC, {conta(assuntos)} assuntos"
        + (" (só Normas Gerais e Bahia)" if filtrado else "")
        + ". Notas do cofre: " + ", ".join(f"[[{n}]]" for n in notas)
        + f". Página: {URL.format(slug)}"
    )
    linhas.append("")
    desce(assuntos, 0, linhas)
    linhas.append("")
    return linhas


def main():
    args = sys.argv[1:]
    gravar = "--gravar" in args
    mapa = MAPA
    if "--so" in args:
        alvo = args[args.index("--so") + 1]
        mapa = [(s, n) for s, n in MAPA if s == alvo]
        if not mapa:
            sys.exit(f"slug '{alvo}' não está no MAPA")
    cab = f"""---
tipo: tec-arvore
---

# TEC: árvore de assuntos das matérias do cofre

Árvore pública de assuntos do TecConcursos (`tecconcursos.com.br/materias/<matéria>`), extraída em {date.today().isoformat()}, com o total de questões de cada assunto entre parênteses (o pai soma os filhos). Serve para escolher o assunto certo ao montar caderno no TEC. O casamento entre matéria do TEC e nota do cofre é sugestão, ajuste se precisar. Regerar: `python3 PY/tec-arvore.py --gravar`.

Como usar: no TEC, em Filtros → Assunto, marque o nó exato da árvore abaixo. Assunto com poucas questões rende caderno curto; o pai é o guarda-chuva.

"""
    corpo = []
    for slug, notas in mapa:
        corpo += secao(slug, notas)
    texto = cab + "\n".join(corpo)
    if gravar:
        if "--so" in args:
            sys.exit("--gravar não combina com --so (gravaria a nota só com uma matéria)")
        DESTINO.write_text(texto, encoding="utf-8")
        print(f"gravado: {DESTINO.relative_to(RAIZ)} ({len(texto.splitlines())} linhas)")
    else:
        print(texto)


if __name__ == "__main__":
    main()
