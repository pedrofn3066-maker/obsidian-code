#!/usr/bin/env python3
"""
plano-dia.py — o que ler, o que praticar em questões e o que revisar em cada
slot do dia, por subtópico da matéria que a Grade Semanal marca para o slot.

    python3 PY/plano-dia.py                     # hoje; abre HTML no navegador
    python3 PY/plano-dia.py --data 2026-09-16   # outro dia
    python3 PY/plano-dia.py --texto             # saída no terminal
    python3 PY/plano-dia.py --diag Penal        # audita casamentos e métricas de uma matéria

Cada item traz também ONDE achar (link do TEC do assunto, material de apoio, caderno do
erro), COMO estudar (método que depende da ação e do tipo de erro) e um TEMPO sugerido; o
slot fecha com 5 min de registro. A página HTML tem checklist do dia (salvo no navegador).

Critérios, limitações e como ler: Questoes/Paineis/Plano do dia.md
"""
import argparse
import re
import subprocess
import tempfile
import unicodedata
import webbrowser
from datetime import date, datetime, timedelta
from html import escape
from pathlib import Path
from urllib.parse import quote

VAULT = Path(__file__).resolve().parent.parent
MATERIAS = VAULT / "MATERIAS"
DIARIO = VAULT / "Questoes" / "Diario"
GRADE = VAULT / "Questoes" / "Slots (Grade Semanal).md"

# ---------------------------------------------------------------------------
# CONFIGURAÇÃO
# ---------------------------------------------------------------------------

INICIO_CICLO = date(2026, 9, 7)
FASES = [(13, "construção"), (18, "consolidação"), (10**6, "reta final")]

FUNCAO_SLOT = {
    "S2": "leitura nova / matéria pesada",
    "S3": "aprofundamento + questões",
    "S4": "matéria secundária",
    "S5": "rodízio",
}
# Ordem das seções e quantos itens cada uma mostra, pela função do slot.
ENFASE = {
    "S2": [("ler", 3), ("questoes", 2), ("revisar", 2)],
    "S3": [("questoes", 3), ("revisar", 2), ("ler", 2)],
    "S4": [("revisar", 2), ("questoes", 2), ("ler", 1)],
    "S5": [("questoes", 2), ("revisar", 2), ("ler", 2)],
}
ROTULO_ACAO = {"ler": "Ler", "questoes": "Fazer questões", "revisar": "Revisar"}

# Roteiro do slot. São ESTIMATIVAS (ajuste ao seu ritmo): minutos por item e a reserva de
# registro no fim. Item que não cabe no orçamento do slot vira "se sobrar tempo".
MIN_ACAO = {"ler": 20, "questoes": 25, "revisar": 12}
MIN_REGISTRO = 5
QUESTOES_POR_ITEM = "10–15"

# Pastas de MATERIAL/ (cada uma com <pasta>/<pasta>.md de índice) que sustentam cada nota.
# Mapeamento manual: nota sem entrada aqui simplesmente não mostra "Material".
MATERIAL_POR_NOTA = {
    "P1 - Macro Economia": ["MACRO"],
    "P1 - Direito Financeiro": ["DIREITO FINANCEIRO"],
    "P2 - CASP": ["DIREITO FINANCEIRO"],  # MCASP/MIC/NBC TSP moram nessa pasta
    "P2 - Direito Tributário": ["DIREITO TRIBUTÁRIO", "JURISPRUDENCIAS"],
    "P2 - Reforma Tributária": ["Reforma Tributária", "BAT RESUMOS"],
    "P2 - Legislação Tributária Estadual (BA)": ["LTE"],
    "P1 - Direito Administrativo": ["JURISPRUDENCIAS"],
    "P1 - Direito Constitucional": ["JURISPRUDENCIAS"],
}

MIN_CONTEUDO = 3          # linhas de conteúdo real sob o heading para contar como "lido"
JANELA_ERRO = 30          # dias em que um erro de caderno ainda puxa revisão
CORTE_ERRO = 0.70         # acerto abaixo disso no tópico conta como erro (Fila de reforço)
CORTE_RELEITURA = 0.60    # abaixo disso o protocolo manda reler antes de refazer
INTERVALO_POR_DOM = {0: 7, 1: 7, 2: 7, 3: 15, 4: 30, 5: 60}
SCORE_HEADING = 0.40
SCORE_ASSUNTO = 0.45
HEADING_GENERICO = 3      # título repetido tantas vezes no grupo não serve de âncora

CUSTOS = "contabilidade de custos"
FLUENCIA = [(f"P2 - Fluência de Dados {s}", None) for s in ("BD", "CD", "SGE", "SGE-C")]
TI = [("P2 - Tecnologia da Informação", None)]

# Rótulo da Grade Semanal (normalizado) -> notas [(arquivo sem .md, segmento)].
GRADE_PARA_NOTAS = {
    "contabilidade avancada": [("P2 - Contabilidade Avançada e de Custos", None)],
    "contabilidade de custos": [("P2 - Contabilidade Avançada e de Custos", CUSTOS)],
    "direito tributario": [("P2 - Direito Tributário", None), ("P2 - Reforma Tributária", None)],
    "lingua portuguesa": [("P1 - Língua Portuguesa", None)],
    "ciencias de dados": FLUENCIA,
    "legislacao tributaria estadual": [("P2 - Legislação Tributária Estadual (BA)", None)],
    "auditoria": [("P1 - Auditoria", None)],
    "financas publicas": [("P2 - Finanças Públicas", None)],
    "mat. financeira/estatistica/rlm": [
        ("P2 - Matemática Financeira", None), ("P1 - Estatística", None),
        ("P2 - Estatística Aplicada", None), ("P1 - Raciocínio Lógico", None)],
    "direito financeiro": [("P1 - Direito Financeiro", None)],
    "adm. publica e governanca": [
        ("P1 - Administração e Governança Pública", None), ("P1 - Administração Geral", None)],
    "seguranca da informacao": TI,
}
# Rótulos que alternam por semana do ciclo: opção = (semana - 1) % len(opções).
# Com duas opções isso dá ímpares -> primeira, pares -> segunda.
RODIZIOS = {
    "rodizio 4 (constitucional, administrativo, civil, penal)": [
        [("P1 - Direito Constitucional", None)], [("P1 - Direito Administrativo", None)],
        [("P1 - Direito Civil", None)], [("P1 - Penal", None)]],
    "cont. geral (impares)/cont. publica (pares)": [
        [("P1 - Contabilidade Geral", None)], [("P2 - CASP", None)]],
    "micro (impares)/macro (pares)": [
        [("P1 - Micro e Finanças Públicas", None)], [("P1 - Macro Economia", None)]],
}
# `materia` do Diario (normalizada) -> notas, quando o nome não casa sozinho.
DIARIO_PARA_NOTAS = {
    "contabilidade publica": [("P2 - CASP", None)],
    "contabilidade geral": [("P1 - Contabilidade Geral", None), ("P2 - Contabilidade Avançada e de Custos", None)],
    "contabilidade avancada": [("P2 - Contabilidade Avançada e de Custos", None)],
    "contabilidade de custos": [("P2 - Contabilidade Avançada e de Custos", CUSTOS)],
    "ciencias de dados": FLUENCIA,
    "tecnologia da informacao": TI,
    "matematica financeira": [("P2 - Matemática Financeira", None)],
    "estatistica": [("P1 - Estatística", None), ("P2 - Estatística Aplicada", None)],
    "penal": [("P1 - Penal", None)],
}

DIAS = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]
NOME_DIA = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

STOP = {"de", "da", "do", "das", "dos", "e", "a", "o", "as", "os", "em", "com", "ao",
        "aos", "para", "por", "na", "no", "nas", "nos", "sem", "sobre", "entre", "um",
        "uma", "ou", "que", "se", "bloco", "art", "arts", "questoes", "mescladas",
        "parte", "capitulo", "etc"}

# ---------------------------------------------------------------------------

RE_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
RE_CHK_ITEM = re.compile(r"^- \[.\]\s+(.+?)\s*\[dom::\s*(\d+)\]\s*\[peso::\s*([\d.]+)\]")
RE_TRACKER = re.compile(r"^- \[.\] status \[dom::")
RE_TECLINK = re.compile(r"\(?https?://www\.tecconcursos\.com\.br/\S*\)?\.?")
RE_URL_TEC = re.compile(r"https?://www\.tecconcursos\.com\.br/\S+")
RE_PROX = re.compile(r"\[prox::\s*(\d{4}-\d{2}-\d{2})\s*\]")
RE_CONTA_BARRA = re.compile(r"—\s*(\d+)\s*/\s*(\d+)")
RE_CONTA_EXTENSO = re.compile(r"—\s*(\d+)\s+acertos?\s+em\s+(\d+)")


def nfc(s):
    return unicodedata.normalize("NFC", s)


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def chave(s):
    return re.sub(r"\s+", " ", sem_acento(s).lower()).strip()


def radical(w):
    if len(w) > 4:
        for fim, troca in (("oes", "ao"), ("aes", "ao"), ("ais", "al"), ("eis", "el"), ("ns", "m")):
            if w.endswith(fim):
                w = w[: -len(fim)] + troca
                break
        else:
            if w.endswith("s"):
                w = w[:-1]
    if len(w) > 5 and w[-1] in "ao":
        w = w[:-1]
    return w


def _ano(m):
    yy = int(m.group(2))
    return f"{m.group(1)}/{'19' if yy > 30 else '20'}{m.group(2)}"


_tokens = {}


def tokens(s, parenteses=False):
    k = (s, parenteses)
    if k not in _tokens:
        t = chave(s)
        t = re.sub(r"(\d)\.(\d)", r"\1\2", t)
        t = re.sub(r"\b(\d{1,5})/(\d{2})\b", _ano, t)
        if not parenteses:
            t = re.sub(r"\(.*?\)", " ", t)
        t = re.sub(r"[^a-z0-9 ]", " ", t)
        out = set()
        for w in t.split():
            if w in STOP:
                continue
            if w.isdigit():
                if len(w) >= 2:
                    out.add(w)
            elif len(w) > 2:
                out.add(radical(w))
        _tokens[k] = out
    return _tokens[k]


def iniciais(s):
    t = re.sub(r"\(.*?\)", " ", chave(s))
    return "".join(w[0] for w in re.findall(r"[a-z]+", t) if w not in STOP)


def distintos(textos):
    """Para cada texto, os tokens que não aparecem em nenhum outro texto do conjunto."""
    unicos = set(textos)
    out = {t: {} for t in unicos}
    for par in (False, True):
        cont = {}
        for t in unicos:
            for w in tokens(t, par):
                cont[w] = cont.get(w, 0) + 1
        for t in unicos:
            out[t][par] = {w for w in tokens(t, par) if cont[w] == 1}
    return out


def semelhanca(alvo, candidato, dist=None, estrito=True):
    """estrito=True para heading (âncora de navegação); False para assunto de caderno,
    que no TEC vem longo e específico e raramente repete dois tokens distintivos."""
    rotulo = chave(limpar_titulo(candidato))
    if re.fullmatch(r"[a-z]{2,6}", rotulo) and rotulo == iniciais(alvo):
        return 0.9
    siglas = {chave(w) for w in re.findall(r"\b[A-ZÀ-Ý]{2,6}\b", alvo)}
    partes = [p for p in re.split(r"\s+/\s+|\.\s+(?=[A-ZÀ-Ý])", alvo) if p.strip()]
    alternativas = [alvo] + (partes if len(partes) > 1 else [])
    melhor = 0.0
    for par in (False, True):
        c, cheio = tokens(candidato, par), tokens(alvo, par)
        if not c or not cheio:
            continue
        d = dist[par] if dist is not None else None
        for alt in alternativas:
            a = tokens(alt, par)
            inter = a & c
            if not inter:
                continue
            curto = c <= cheio
            sigla = len(inter) == 1 and next(iter(inter)) in siglas
            if len(inter) == 1 and len(a) > 1 and not (curto or sigla):
                continue
            if d:
                comuns_d = inter & d
                if not comuns_d:
                    continue
                if estrito and len(d) >= 2 and len(comuns_d) < 2 and not (curto or sigla):
                    continue
            s = max(len(inter) / len(a | c), 0.8 * len(inter) / len(a),
                    0.5 + 0.3 * len(inter) / len(cheio) if curto else 0.0,
                    0.55 if sigla else 0.0)
            if d is not None and not d and s < 0.8:
                continue
            melhor = max(melhor, s)
    return melhor


def limpar_titulo(txt):
    t = re.sub(r"^[-\s]+", "", txt)
    t = re.sub(r"^\d+(\.\d+)*\.?\s+", "", t)
    t = re.sub(r"[;.:]+$", "", t).strip()
    t = re.sub(r"\s+e$", "", t)
    return t.replace("_", "").replace("*", "").strip() or txt


def substantiva(linha):
    s = linha.strip()
    if not s or RE_HEADING.match(s) or RE_TRACKER.match(s):
        return False
    s = RE_TECLINK.sub("", s)
    s = re.sub(r"(?i)\b(resumo tec|tec resumo)\s*:?", "", s)
    s = re.sub(r"\[(cad|prox|dom|peso|rev)::[^\]]*\]", "", s)
    s = re.sub(r"(?<![\w\[])#[\w/À-ÿ-]+", "", s)
    s = re.sub(r"%%.*?%%", "", s)
    s = re.sub(r"^[-*>\s.:|`_]+", "", s).strip()
    return len(s) >= 3


def data_txt(d):
    return d.strftime("%d/%m") if d else "—"


def pct_txt(p):
    return "?" if p is None else f"{round(100 * p)}%"


# ---------------------------------------------------------------------------
# Notas de MATERIAS
# ---------------------------------------------------------------------------

class Nota:
    def __init__(self, stem):
        self.stem = stem
        self.path = MATERIAS / f"{stem}.md"
        self.rel = f"MATERIAS/{stem}"
        self.linhas = self.path.read_text(encoding="utf-8").split("\n")
        self.peso, self.prioridade = 2.0, ""
        self.headings, self.fence = [], set()
        self.meta, self.checklists, self.segmentos = [], [], []
        self._blame = None
        self._frontmatter()
        self._estrutura()

    def _frontmatter(self):
        if not self.linhas or self.linhas[0].strip() != "---":
            return
        for l in self.linhas[1:]:
            if l.strip() == "---":
                break
            m = re.match(r"^(peso|prioridade):\s*(.+)$", l)
            if m and m.group(1) == "peso":
                try:
                    self.peso = float(m.group(2))
                except ValueError:
                    pass
            elif m:
                self.prioridade = m.group(2).strip()

    def _estrutura(self):
        dentro = False
        for i, l in enumerate(self.linhas):
            if l.lstrip().startswith("```"):
                dentro = not dentro
                self.fence.add(i)
                continue
            if dentro:
                self.fence.add(i)
                continue
            m = RE_HEADING.match(l)
            if m:
                self.headings.append((i, len(m.group(1)), m.group(2).rstrip()))

        for k, (i, _, txt) in enumerate(self.headings):
            ck = chave(txt)
            if ck.startswith("percentual de cobranca") or ck.startswith("checklist por importancia"):
                fim = self.headings[k + 1][0] if k + 1 < len(self.headings) else len(self.linhas)
                self.meta.append((i, fim))
                if ck.startswith("checklist"):
                    itens = []
                    for l in self.linhas[i + 1:fim]:
                        m = RE_CHK_ITEM.match(l.strip())
                        if m:
                            itens.append((m.group(1).strip(), int(m.group(2)), float(m.group(3))))
                    self.checklists.append((i, fim, itens))

        h1s = [(i, txt) for i, n, txt in self.headings if n == 1]
        for ic, _, _ in self.checklists[1:]:
            antes = [h for h in h1s if h[0] < ic]
            if not antes:
                continue
            ini, rotulo = antes[-1]
            depois = [h[0] for h in h1s if h[0] > ic]
            self.segmentos.append((chave(rotulo), ini, depois[0] if depois else len(self.linhas)))
        self.fim_cabecalho = self.checklists[0][1] if self.checklists else 0
        self.inicios_segmento = {ini for _, ini, _ in self.segmentos}

    def segmento_de(self, i):
        for rot, ini, fim in self.segmentos:
            if ini <= i < fim:
                return rot
        return None

    def checklist_de(self, seg):
        for ic, _, itens in self.checklists:
            if self.segmento_de(ic) == seg:
                return itens
        return []

    def candidatos(self, seg):
        out = []
        for i, nivel, txt in self.headings:
            if i < self.fim_cabecalho or i in self.inicios_segmento:
                continue
            if any(a <= i < b for a, b in self.meta):
                continue
            if self.segmento_de(i) != seg:
                continue
            out.append((i, nivel, txt))
        return out

    def tem_tracker(self, i):
        return i + 1 < len(self.linhas) and bool(RE_TRACKER.match(self.linhas[i + 1].strip()))

    def tem_conteudo(self, i, nivel):
        return sum(1 for j in self.escopo(i, nivel) if substantiva(self.linhas[j])) >= MIN_CONTEUDO

    def escopo(self, i, nivel):
        j = i + 1
        while j < len(self.linhas):
            if j not in self.fence:
                m = RE_HEADING.match(self.linhas[j])
                if m and len(m.group(1)) <= nivel:
                    break
            j += 1
        return range(i + 1, j)

    def blame(self):
        if self._blame is None:
            self._blame = {}
            try:
                out = subprocess.run(
                    ["git", "blame", "--line-porcelain", "--", self.path.relative_to(VAULT).as_posix()],
                    cwd=VAULT, capture_output=True, check=True,
                ).stdout.decode("utf-8", errors="replace")
            except (subprocess.CalledProcessError, FileNotFoundError):
                return self._blame
            linha, t = None, None
            for l in out.split("\n"):
                m = re.match(r"^[0-9a-f]{40} \d+ (\d+)", l)
                if m:
                    linha = int(m.group(1)) - 1
                elif l.startswith("author-time "):
                    t = int(l.split()[1])
                elif l.startswith("\t") and linha is not None and t is not None:
                    self._blame[linha] = datetime.fromtimestamp(t).date()
        return self._blame


_notas = {}


def carregar(stem):
    stem = nfc(stem)
    if stem not in _notas:
        _notas[stem] = Nota(stem)
    return _notas[stem]


def stems_materias():
    return sorted(nfc(f.stem) for f in MATERIAS.glob("*.md") if not f.stem.startswith("MOC"))


# ---------------------------------------------------------------------------
# Cadernos do Diario
# ---------------------------------------------------------------------------

class Caderno:
    def __init__(self, nome, campos, erros):
        self.nome = nome
        self.data = date.fromisoformat(str(campos["data"])[:10])
        self.materia = nfc(str(campos.get("materia") or ""))
        # campo do Pedro: desconhecimento | desatencao | excecao | vazio
        self.erro_tipo = sem_acento(str(campos.get("erro_tipo") or "")).lower().strip()
        self.total = _int(campos.get("total"))
        self.acertos = _int(campos.get("acertos"))
        self.pares = pares_do_caderno(self.materia)
        assuntos = campos.get("assuntos") if isinstance(campos.get("assuntos"), list) else []
        erros_nao_listados = (not erros and self.total and self.acertos is not None
                              and self.acertos < self.total)
        self.itens, usados = [], set()
        for a in assuntos:
            melhor, ms = None, 0.0
            for k, (nome_erro, _) in enumerate(erros):
                s = 1.0 if chave(a) == chave(nome_erro) else semelhanca(a, nome_erro)
                if s > ms:
                    melhor, ms = k, s
            if melhor is not None and ms >= 0.7:
                usados.add(melhor)
                self.itens.append((a, True, erros[melhor][1]))
            elif erros_nao_listados:
                self.itens.append((a, None, self.acertos / self.total))
            else:
                self.itens.append((a, False, 1.0))
        for k, (nome_erro, pct) in enumerate(erros):
            if k not in usados:
                self.itens.append((nome_erro, True, pct))


def _int(v):
    try:
        return int(str(v).strip())
    except (TypeError, ValueError):
        return None


def ler_caderno(path):
    t = path.read_text(encoding="utf-8")
    if not t.startswith("---"):
        return None
    fim = t.find("\n---", 3)
    if fim < 0:
        return None
    fm, corpo = t[3:fim], t[fim + 4:]
    campos, lista = {}, None
    for l in fm.split("\n"):
        m = re.match(r"^(\w+):\s*(.*)$", l)
        if m:
            k, v = m.group(1), m.group(2).strip()
            campos[k] = [] if v == "" else v.strip("\"'")
            lista = k if v == "" else None
        elif lista and re.match(r"^\s*-\s+", l):
            campos[lista].append(re.sub(r"^\s*-\s+", "", l).strip().strip("\"'"))
    if not campos.get("materia") or not campos.get("data") or isinstance(campos.get("data"), list):
        return None

    erros = []
    m = re.search(r"^## Erros a revisar\s*$(.*?)(?=^## |\Z)", corpo, re.S | re.M)
    if m:
        for l in m.group(1).split("\n"):
            s = re.sub(r"^\s*[-*]\s*", "", l).strip() if re.match(r"^\s*[-*]", l) else ""
            if not s or chave(s).rstrip(".") in {"nenhum", "nenhuma"}:
                continue
            nome = s.split(" — ")[0].strip().rstrip(";.")
            c = RE_CONTA_BARRA.search(s) or RE_CONTA_EXTENSO.search(s)
            pct = int(c.group(1)) / int(c.group(2)) if c and int(c.group(2)) else None
            erros.append((nome, pct))
    try:
        return Caderno(path.stem, campos, erros)
    except ValueError:
        return None


def ler_cadernos():
    out = []
    for f in sorted(DIARIO.glob("*.md")):
        c = ler_caderno(f)
        if c:
            out.append(c)
    return out


def pares_do_caderno(materia):
    k = chave(materia)
    if k in DIARIO_PARA_NOTAS:
        return DIARIO_PARA_NOTAS[k]
    if k.startswith("fluencia de dados"):
        return FLUENCIA
    if k.startswith("ti - "):
        return TI
    stems = stems_materias()
    for stem in stems:
        if chave(re.sub(r"^P\d - ", "", stem)) == k:
            return [(stem, None)]
    tm = tokens(materia)
    for stem in stems:
        if tm and tm <= tokens(re.sub(r"^P\d - ", "", stem)):
            return [(stem, None)]
    return []


# ---------------------------------------------------------------------------
# Unidades de estudo (subtópicos) e classificação
# ---------------------------------------------------------------------------

class Unidade:
    def __init__(self, topico, peso, dom, nota, fonte):
        self.topico, self.peso, self.dom, self.nota, self.fonte = topico, peso, dom, nota, fonte
        self.dist = None
        self.heading, self.score = None, 0.0
        self.ocorrencias = []
        self.conteudo, self.escrito_ult, self.prox_vencido = 0, None, None
        self.tec_link = None  # 1º link do TEC sob o heading ("Resumo tec: (…)")

    def medir(self, hoje):
        if not self.heading:
            return
        n, i, nivel, _ = self.heading
        blame = n.blame()
        datas, proxs = [], []
        for j in n.escopo(i, nivel):
            l = n.linhas[j]
            if self.tec_link is None:
                m = RE_URL_TEC.search(l)
                if m:
                    self.tec_link = m.group(0).rstrip(").,;")
            for p in RE_PROX.findall(l):
                proxs.append(date.fromisoformat(p))
            if substantiva(l):
                self.conteudo += 1
                if j in blame:
                    datas.append(blame[j])
        self.escrito_ult = max(datas) if datas else None
        vencidas = [p for p in proxs if p <= hoje]
        self.prox_vencido = min(vencidas) if vencidas else None

    def ultimo_teste(self):
        return max((d for d, *_ in self.ocorrencias), default=None)

    def erro_recente(self, hoje):
        ult = self.ultimo_teste()
        if not ult or (hoje - ult).days > JANELA_ERRO:
            return None
        ruins = [pct for d, erro, pct, _ in self.ocorrencias
                 if d == ult and erro and (pct is None or pct < CORTE_ERRO)]
        if not ruins:
            return None
        conhecidos = [p for p in ruins if p is not None]
        return ult, (min(conhecidos) if conhecidos else None)

    def caderno_do_erro(self, data):
        """Caderno em que o tópico errou naquela data (para ler o erro_tipo e linkar)."""
        return next((c for d, erro, _, c in self.ocorrencias if d == data and erro), None)

    def nota_exibida(self):
        return self.heading[0] if self.heading else self.nota

    def heading_txt(self):
        return limpar_titulo(self.heading[3]) if self.heading else None


def montar_unidades(pares):
    notas = [(carregar(stem), seg) for stem, seg in pares]
    peso_max = max(n.peso for n, _ in notas)
    # Heading só serve de âncora para tópicos do próprio checklist (ou de um checklist
    # idêntico, caso das 4 notas de Fluência) — senão "Disposições Preliminares" da
    # Reforma cai no heading homônimo do Simples Nacional em Direito Tributário.
    assinatura = {(n.stem, seg): frozenset(chave(t) for t, _, _ in n.checklist_de(seg))
                  for n, seg in notas}
    candidatos = [(n, assinatura[(n.stem, seg)], i, nivel, txt)
                  for n, seg in notas for i, nivel, txt in n.candidatos(seg)]
    repeticoes = {}
    for *_, txt in candidatos:
        k = chave(limpar_titulo(txt))
        repeticoes[k] = repeticoes.get(k, 0) + 1
    candidatos = [c for c in candidatos if repeticoes[chave(limpar_titulo(c[4]))] < HEADING_GENERICO]

    unidades, vistos = [], set()
    for n, seg in notas:
        fator = n.peso / peso_max
        itens = n.checklist_de(seg)
        if itens:
            dist = distintos([t for t, _, _ in itens])
            for topico, dom, p in itens:
                if chave(topico) in vistos:
                    continue
                vistos.add(chave(topico))
                u = Unidade(topico, p * fator, dom, n, "checklist")
                u.dist = dist[topico]
                melhor = None
                for cn, sig, i, nivel, txt in candidatos:
                    if sig != assinatura[(n.stem, seg)]:
                        continue
                    s = semelhanca(topico, txt, u.dist)
                    if s < SCORE_HEADING:
                        continue
                    # scores próximos (mesma casa decimal): vence o heading que tem conteúdo
                    ordem = (round(s, 1), cn.tem_conteudo(i, nivel), round(s, 3), cn.tem_tracker(i), -nivel)
                    if melhor is None or ordem > melhor[0]:
                        melhor = (ordem, (cn, i, nivel, txt))
                if melhor:
                    u.heading, u.score = melhor[1], melhor[0][2]
                unidades.append(u)
        else:
            hs = [(i, nivel, txt) for i, nivel, txt in n.candidatos(seg) if n.tem_tracker(i)]
            dist = distintos([limpar_titulo(txt) for _, _, txt in hs])
            for i, nivel, txt in hs:
                u = Unidade(limpar_titulo(txt), 100 / len(hs) * fator, None, n, "heading")
                u.dist = dist[limpar_titulo(txt)]
                u.heading, u.score = (n, i, nivel, txt), 1.0
                unidades.append(u)
    return unidades


def associar(unidades, pares, cadernos, hoje):
    alvo = set(pares)
    for c in cadernos:
        if c.data > hoje or not alvo & set(c.pares):
            continue
        for texto, erro, pct in c.itens:
            melhor, ms = None, 0.0
            for u in unidades:
                s = semelhanca(u.topico, texto, u.dist, estrito=False)
                if s > ms:
                    melhor, ms = u, s
            if melhor and ms >= SCORE_ASSUNTO:
                melhor.ocorrencias.append((c.data, erro, pct, c))


def classificar(u, hoje):
    lacuna = 1.0 if not u.dom else (5 - u.dom) / 5
    erro = u.erro_recente(hoje)

    if u.conteudo < MIN_CONTEUDO:
        ult = u.ultimo_teste()
        testado_ok = ult is not None and (hoje - ult).days <= JANELA_ERRO
        if not erro and ((u.dom is not None and u.dom >= 4) or testado_ok):
            return None
        razoes = ["nenhum heading correspondente na nota" if not u.heading
                  else "heading ainda sem conteúdo escrito"]
        fator = 1.0
        if erro:
            razoes.insert(0, f"errou em {data_txt(erro[0])} ({pct_txt(erro[1])}) e nada foi escrito sobre isso")
            fator = 2.0
        return "ler", u.peso * lacuna * fator, razoes

    if erro:
        d, pct = erro
        p = pct if pct is not None else 0.5
        c = u.caderno_do_erro(d)
        tipo = c.erro_tipo if c else ""
        if u.escrito_ult and u.escrito_ult >= d:
            instrucao = f"correção já escrita em {data_txt(u.escrito_ult)} — refaça questões do tópico"
        elif tipo == "desatencao":
            instrucao = "erro de desatenção — não releia o conteúdo, refaça as questões"
        elif p < CORTE_RELEITURA or tipo == "desconhecimento":
            instrucao = "releia o heading antes de refazer questões"
        else:
            instrucao = "refaça uma bateria curta (~15 questões)"
        return "revisar", u.peso * (1 - p) * 2 + 0.01, [f"errou em {data_txt(d)} ({pct_txt(pct)})", instrucao]

    if u.prox_vencido:
        return "revisar", u.peso * lacuna, [f"revisão agendada vencida desde {data_txt(u.prox_vencido)}"]

    ult = u.ultimo_teste()
    if ult is None:
        return "questoes", u.peso * lacuna * 1.5, [
            f"lido (escrito até {data_txt(u.escrito_ult)}) e nunca testado em caderno"]
    if u.escrito_ult and ult < u.escrito_ult:
        return "questoes", u.peso * lacuna * 1.5, [
            f"conteúdo novo ({data_txt(u.escrito_ult)}) depois do último caderno ({data_txt(ult)})"]

    contato = max(ult, u.escrito_ult or ult)
    intervalo = INTERVALO_POR_DOM.get(u.dom, 7) if u.dom is not None else 7
    dias = (hoje - contato).days
    if dias >= intervalo:
        return "revisar", u.peso * lacuna * min(2.0, dias / intervalo), [
            f"último contato {data_txt(contato)} ({dias} dias) · intervalo de {intervalo}d "
            f"para dom {u.dom if u.dom is not None else '—'}"]
    return None


# ---------------------------------------------------------------------------
# Onde achar, como fazer, quanto tempo
# ---------------------------------------------------------------------------

def abrir(rel):
    """obsidian://open para um arquivo do vault (caminho relativo, sem .md)."""
    return f"obsidian://open?vault={quote(VAULT.name)}&file={quote(rel, safe='')}"


def material_de(stem):
    achados = []
    for pasta in MATERIAL_POR_NOTA.get(stem, []):
        if (VAULT / "MATERIAL" / pasta / f"{pasta}.md").exists():
            achados.append((f"Material · {pasta}", abrir(f"MATERIAL/{pasta}/{pasta}")))
    return achados


def dicas(acao, u, razoes, hoje):
    """{'onde': [(rótulo, href|None)], 'como': str} — o que o item não diz sozinho."""
    onde = []
    erro = u.erro_recente(hoje)
    c = u.caderno_do_erro(erro[0]) if erro else None
    tipo = c.erro_tipo if c else ""

    if not u.heading:
        onde.append((f"Criar heading em {u.nota.stem}", uri(u.nota)))
    if u.tec_link:
        onde.append(("TEC · assunto", u.tec_link))
    elif acao != "revisar":
        onde.append((f"TEC: filtre por “{u.topico}”", None))
    if acao != "revisar" or not c:
        onde += material_de(u.nota_exibida().stem)
    if c:
        onde.append((f"Caderno {c.data:%d/%m}", abrir(f"Questoes/Diario/{c.nome}")))

    if acao == "ler":
        como = "Leia a fonte uma vez, feche e escreva de memória o que fixou; só então complete no heading."
        if erro:
            como = "Comece pela questão que você errou — ela diz o que faltava. " + como
    elif acao == "questoes":
        como = (f"~{QUESTOES_POR_ITEM} questões do assunto. Ao errar, anote na hora se foi leitura, "
                "lacuna ou exceção e corrija no heading no mesmo dia.")
        if u.escrito_ult and u.ultimo_teste() and u.ultimo_teste() < u.escrito_ult:
            como = "Teste o que você acabou de escrever, sem consultar a nota. " + como
    elif razoes and razoes[0].startswith("errou"):
        como = {
            "desatencao": "Refaça as questões marcando o comando e as negativas antes de olhar as "
                          "alternativas. Não releia o conteúdo: o erro foi de leitura.",
            "desconhecimento": "Releia o heading, escreva a regra de memória e só então refaça as "
                               "questões que errou.",
            "excecao": "Liste as exceções da regra em 3 linhas e treine só os casos-limite.",
        }.get(tipo, "Antes de estudar, classifique o erro (leitura, lacuna ou exceção) e preencha "
                    "o erro_tipo do caderno — o remédio muda.")
    else:
        como = ("Recuperação ativa: escreva de memória o que lembra do heading (3 min) e só então "
                "abra. O que faltar volta para a próxima revisão.")
    return {"onde": onde, "como": como}


def alocar(minutos, secoes):
    """Encaixa os itens no tempo do slot, na ordem das seções. Cada extra ganha ini/fim (min)
    e `cabe`; o que não cabe vira 'se sobrar tempo'. Devolve (usado, orçamento)."""
    orcamento, t = max(minutos - MIN_REGISTRO, 0), 0
    for acao, itens in secoes:
        for _, _, extra in itens:
            d = MIN_ACAO[acao]
            extra["min"] = d
            extra["cabe"] = t + d <= orcamento
            if extra["cabe"]:
                extra["ini"], extra["fim"], t = t, t + d, t + d
    return t, orcamento


# ---------------------------------------------------------------------------
# Plano
# ---------------------------------------------------------------------------

def celulas(l):
    s = l.strip()
    if not s.startswith("|"):
        return None
    return [c.strip() for c in s.strip("|").split("|")]


def ler_grade():
    linhas = nfc(GRADE.read_text(encoding="utf-8")).split("\n")
    for i, l in enumerate(linhas):
        cab = celulas(l)
        if not cab or chave(cab[0]) != "dia":
            continue
        colunas = []
        for c in cab:
            s, m = re.search(r"\b(S\d)\b", c), re.search(r"(\d+)\s*min", c)
            colunas.append((s.group(1) if s else None, int(m.group(1)) if m else None))
        grade = {}
        for l2 in linhas[i + 2:]:
            c2 = celulas(l2)
            if not c2:
                break
            grade[chave(c2[0])] = [(colunas[k][0], colunas[k][1], c2[k])
                                   for k in range(1, min(len(c2), len(colunas))) if colunas[k][0]]
        return grade
    return {}


def resolver(rotulo, semana):
    k = chave(rotulo)
    if k in GRADE_PARA_NOTAS:
        return GRADE_PARA_NOTAS[k], None
    if k in RODIZIOS:
        opcoes = RODIZIOS[k]
        escolha = opcoes[(max(semana, 1) - 1) % len(opcoes)]
        return escolha, f"semana {semana} do ciclo → {', '.join(s for s, _ in escolha)}"
    return None, None


def especial(rotulo):
    k = chave(rotulo)
    for prefixo, tipo in (("simulado", "simulado"), ("discursiva", "discursiva"),
                          ("correcao", "correcao"), ("fechamento", "fechamento")):
        if k.startswith(prefixo):
            return tipo
    return None


def analisar(pares, cadernos, hoje):
    unidades = montar_unidades(pares)
    associar(unidades, pares, cadernos, hoje)
    for u in unidades:
        u.medir(hoje)
    return unidades


def plano(hoje):
    semana = (hoje - INICIO_CICLO).days // 7 + 1
    fase = "pré-ciclo" if semana < 1 else next(nome for lim, nome in FASES if semana <= lim)
    cadernos = ler_cadernos()
    dia = DIAS[hoje.weekday()]
    grade = ler_grade()

    slots = []
    for slot, minutos, rotulo in grade.get(dia, []):
        s = {"slot": slot, "min": minutos, "rotulo": rotulo, "funcao": FUNCAO_SLOT.get(slot, ""),
             "rodizio": None, "notas": [], "secoes": [], "especial": None, "erros": [], "aviso": None,
             "usado": 0, "orcamento": 0}
        tipo = especial(rotulo)
        if tipo == "correcao":
            for c in cadernos:
                if hoje - timedelta(days=6) <= c.data <= hoje:
                    for texto, erro, pct in c.itens:
                        if erro:
                            s["erros"].append((c.data, c.materia, texto, pct))
            s["erros"].sort(key=lambda e: (e[0], e[1]))
            s["especial"] = ("Erros dos cadernos dos últimos 7 dias — refaça cada um sem consultar a nota:"
                             if s["erros"] else "Nenhum erro registrado nos cadernos dos últimos 7 dias.")
        elif tipo == "fechamento":
            s["especial"] = "Ritual de domingo (LEIA-ME): Ganho potencial → Fila de reforço → Diagnóstico de erro."
        elif tipo:
            s["especial"] = "Sem recomendação por subtópico para este slot."
        else:
            pares, s["rodizio"] = resolver(rotulo, semana)
            if not pares:
                s["aviso"] = "Rótulo da grade sem mapeamento em PY/plano-dia.py (GRADE_PARA_NOTAS)."
            else:
                try:
                    unidades = analisar(pares, cadernos, hoje)
                except FileNotFoundError as e:
                    s["aviso"] = f"Nota não encontrada: {e.filename}"
                    unidades = []
                s["notas"] = [carregar(stem) for stem, _ in pares if (MATERIAS / f"{stem}.md").exists()]
                por_acao = {"ler": [], "questoes": [], "revisar": []}
                for u in unidades:
                    r = classificar(u, hoje)
                    if r:
                        por_acao[r[0]].append((r[1], u, r[2]))
                for acao, n in ENFASE.get(slot, [("ler", 2), ("questoes", 2), ("revisar", 2)]):
                    if acao == "ler" and fase in ("consolidação", "reta final"):
                        continue
                    itens = sorted(por_acao[acao], key=lambda x: -x[0])[:n]
                    s["secoes"].append((acao, [(u, razoes, dicas(acao, u, razoes, hoje))
                                               for _, u, razoes in itens]))
                s["usado"], s["orcamento"] = alocar(minutos, s["secoes"])
        slots.append(s)

    s1 = ("S1 · ocupado pelo simulado" if dia == "domingo"
          else "S1 · 30 min · revisão ativa — use o painel S1 - Revisão de ontem")
    return {"data": hoje, "dia": NOME_DIA[hoje.weekday()], "semana": semana, "fase": fase,
            "s1": s1, "slots": slots, "tem_grade": bool(grade)}


# ---------------------------------------------------------------------------
# Saída
# ---------------------------------------------------------------------------

def meta_item(u):
    partes = [f"peso {u.peso:g}%" if u.fonte == "checklist" else "sem peso VINTEUM (nota sem checklist)"]
    if u.dom == 0:
        partes.append("sem dado TEC (dom 0)")
    elif u.dom is not None:
        partes.append(f"dom TEC {u.dom}")
    return " · ".join(partes)


def varias_notas(s):
    return len({n.stem for n in s["notas"]}) > 1


def uri(nota, heading=None):
    base = f"obsidian://adv-uri?vault={quote(VAULT.name)}&filepath={quote(nota.rel)}"
    return base + (f"&heading={quote(heading)}" if heading else "")


def seta(u):
    alvo = u.heading_txt()
    return alvo if alvo and chave(alvo) != chave(u.topico) else None


REGISTRO = ("Registro · 5 min — anote os erros do slot (foi leitura, lacuna ou exceção? vira o "
            "erro_tipo no /importar-tec) e mande o que sobrou pelo Atalho → /triar-inbox.")


def faixa(extra):
    return f"{extra['ini']}–{extra['fim']} min" if extra["cabe"] else "se sobrar tempo"


def render_texto(p):
    out = [f"PLANO DO DIA — {p['dia']}, {p['data'].strftime('%d/%m/%Y')} · "
           f"semana {p['semana']} do ciclo · fase {p['fase']}", "", p["s1"]]
    if not p["tem_grade"]:
        out.append("\n(tabela da Grade Semanal não encontrada)")
    for s in p["slots"]:
        out += ["", f"{s['slot']} · {s['min']} min · {s['rotulo']} — {s['funcao']}"]
        if s["rodizio"]:
            out.append(f"  rodízio: {s['rodizio']}")
        for aviso in filter(None, [s["aviso"], s["especial"]]):
            out.append(f"  {aviso}")
        for d, materia, texto, pct in s["erros"]:
            out.append(f"    - {data_txt(d)} · {materia} · {texto} ({pct_txt(pct)})")
        if s["secoes"]:
            out.append(f"  roteiro: {s['usado']} min de {s['orcamento']} + {MIN_REGISTRO} de registro")
        for acao, itens in s["secoes"]:
            out.append(f"  {ROTULO_ACAO[acao]}")
            if not itens:
                out.append("    —")
            for k, (u, razoes, extra) in enumerate(itens, 1):
                prefixo = f"[{u.nota_exibida().stem}] " if varias_notas(s) else ""
                alvo = seta(u)
                out.append(f"    {k}. {prefixo}{u.topico}{'  → ' + alvo if alvo else ''}")
                out.append(f"       {meta_item(u)}")
                out.append(f"       {' · '.join(razoes)}")
                out.append(f"       ⏱ {faixa(extra)}")
                out.append(f"       onde: {' · '.join(r for r, _ in extra['onde']) or '—'}")
                out.append(f"       como: {extra['como']}")
        if s["secoes"]:
            out += ["", f"  {REGISTRO}"]
    return "\n".join(out)


CSS = """
:root { color-scheme: light dark; }
body { max-width: 50rem; margin: 2.5rem auto; padding: 0 1.5rem 5rem;
  font: 16px/1.55 -apple-system, "SF Pro Text", "Helvetica Neue", sans-serif;
  color: #1c1c1e; background: #fdfdfb; }
@media (prefers-color-scheme: dark) { body { color: #e7e7e5; background: #16161a; } }
h1 { font-size: 1.45rem; margin: 0 0 .2rem; }
.sub { opacity: .6; margin-bottom: 1rem; }
.s1 { opacity: .8; margin-bottom: 1rem; }
.barra { position: sticky; top: 0; z-index: 5; display: flex; flex-wrap: wrap; gap: .5rem .8rem;
  align-items: center; padding: .55rem 0; background: inherit;
  border-bottom: 1px solid rgba(128,128,128,.25); font-size: .9rem; margin-bottom: .6rem; }
.barra .sp { flex: 1; }
button, a.chip { font: inherit; font-size: .78rem; padding: .18rem .6rem; border-radius: 999px; cursor: pointer;
  border: 1px solid rgba(128,128,128,.4); background: transparent; color: inherit; text-decoration: none; }
button:hover, a.chip:hover { background: rgba(128,128,128,.15); }
button.on { background: rgba(74,125,187,.25); border-color: #4a7dbb; }
.slot { margin-top: 2.2rem; padding-top: 1.2rem; border-top: 1px solid rgba(128,128,128,.25); }
.slot h2 { font-size: 1.1rem; margin: 0; }
.slot h2 .cod { opacity: .55; font-weight: 500; }
.slot h2 .prog { float: right; font-size: .8rem; font-weight: 500; opacity: .6; }
.funcao, .rodizio, .notas, .roteiro { font-size: .85rem; opacity: .6; }
.aviso { color: #c0392b; font-size: .9rem; }
h3 { font-size: .78rem; text-transform: uppercase; letter-spacing: .04em; margin: 1.1rem 0 .3rem; }
h3.ler { color: #3a7ebf; } h3.questoes { color: #2f9e58; } h3.revisar { color: #c9822a; }
ul.itens { list-style: none; margin: 0; padding: 0; }
li.item { display: flex; gap: .7rem; margin: .7rem 0; align-items: flex-start; }
li.item .chk { display: flex; flex-direction: column; align-items: center; gap: .15rem; min-width: 4.6rem; }
li.item .chk input { width: 1.15rem; height: 1.15rem; cursor: pointer; }
.tempo { font-size: .7rem; opacity: .6; text-align: center; line-height: 1.15; }
li.item .corpo { flex: 1; min-width: 0; }
li.item.sobra { opacity: .55; }
li.item.feito .topico, li.item.feito .razao { text-decoration: line-through; opacity: .5; }
.ocultar-feitos li.item.feito { display: none; }
a.topico { color: inherit; text-decoration: none; border-bottom: 1px solid rgba(74,125,187,.5); font-weight: 600; }
.nota { font-size: .75rem; opacity: .55; margin-right: .3rem; }
.alvo { font-size: .85rem; opacity: .6; }
.meta { display: block; font-size: .8rem; opacity: .55; }
.razao { display: block; font-size: .88rem; }
.onde { display: flex; flex-wrap: wrap; gap: .3rem; margin: .3rem 0 .1rem; }
.onde .txt { font-size: .75rem; opacity: .6; padding: .18rem 0; }
.como { display: block; font-size: .85rem; opacity: .8; }
.como::before { content: "como: "; opacity: .55; }
.registro { margin-top: 1.2rem; font-size: .85rem; opacity: .7; padding: .5rem .8rem;
  border-left: 3px solid rgba(128,128,128,.4); }
.vazio { opacity: .45; font-style: italic; font-size: .9rem; }
.rodape { margin-top: 3rem; font-size: .8rem; opacity: .55; }
"""

JS = r"""
(function () {
  var DIA = "__DIA__";
  function ler(k) { try { return localStorage.getItem("plano:" + DIA + ":" + k) === "1"; } catch (e) { return false; } }
  function gravar(k, v) {
    try { if (v) localStorage.setItem("plano:" + DIA + ":" + k, "1"); else localStorage.removeItem("plano:" + DIA + ":" + k); }
    catch (e) {}
  }
  function contar() {
    var tot = 0, ok = 0;
    [].forEach.call(document.querySelectorAll(".slot"), function (sl) {
      var t = 0, o = 0;
      [].forEach.call(sl.querySelectorAll("li.item:not(.sobra)"), function (li) {
        t++; if (li.querySelector("input").checked) o++;
      });
      var pr = sl.querySelector(".prog"); if (pr) pr.textContent = t ? o + "/" + t : "";
      tot += t; ok += o;
    });
    document.getElementById("cont").textContent = ok + "/" + tot + " feitos hoje";
  }
  [].forEach.call(document.querySelectorAll("li.item"), function (li) {
    var cb = li.querySelector("input");
    cb.checked = ler(li.dataset.k); li.classList.toggle("feito", cb.checked);
    cb.addEventListener("change", function () {
      gravar(li.dataset.k, cb.checked); li.classList.toggle("feito", cb.checked); contar();
    });
  });
  var bf = document.getElementById("b-feitos");
  bf.addEventListener("click", function () {
    bf.classList.toggle("on", document.body.classList.toggle("ocultar-feitos"));
  });
  contar();
})();
"""


def render_html(p):
    dia = p["data"].isoformat()
    h = [f'<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">'
         f"<title>Plano do dia — {p['data'].strftime('%d/%m')}</title>",
         f"<style>{CSS}</style>",
         f"<h1>Plano do dia — {escape(p['dia'])}, {p['data'].strftime('%d/%m/%Y')}</h1>",
         f'<div class="sub">semana {p["semana"]} do ciclo · fase {escape(p["fase"])}</div>',
         f'<div class="s1">{escape(p["s1"])}</div>']
    if not p["tem_grade"]:
        h.append('<div class="aviso">Tabela da Grade Semanal não encontrada.</div>')

    tem_itens = any(s["secoes"] for s in p["slots"])
    if tem_itens:
        s1 = f"obsidian://shell-commands/?vault={quote(VAULT.name)}&execute=s1ontem01"
        h.append(
            '<div class="barra"><strong id="cont"></strong><span class="sp"></span>'
            f'<a class="chip" href="{s1}">S1 · revisão de ontem</a>'
            f'<a class="chip" href="{abrir("Questoes/Capturas")}">Capturas</a>'
            '<button id="b-feitos">Ocultar feitos</button></div>')

    for s in p["slots"]:
        h.append('<div class="slot">')
        h.append(f'<h2><span class="cod">{escape(s["slot"])} · {s["min"]} min ·</span> {escape(s["rotulo"])}'
                 '<span class="prog"></span></h2>')
        h.append(f'<div class="funcao">{escape(s["funcao"])}</div>')
        if s["rodizio"]:
            h.append(f'<div class="rodizio">rodízio: {escape(s["rodizio"])}</div>')
        if s["notas"]:
            links = " · ".join(f'<a href="{uri(n)}">{escape(n.stem)}</a>' for n in s["notas"])
            h.append(f'<div class="notas">{links}</div>')
        if s["secoes"]:
            h.append(f'<div class="roteiro">roteiro: {s["usado"]} min de {s["orcamento"]} '
                     f"+ {MIN_REGISTRO} de registro</div>")
        if s["aviso"]:
            h.append(f'<div class="aviso">{escape(s["aviso"])}</div>')
        if s["especial"]:
            h.append(f"<p>{escape(s['especial'])}</p>")
        if s["erros"]:
            h.append("<ul>" + "".join(
                f"<li>{data_txt(d)} · {escape(m)} · {escape(t)} ({pct_txt(pc)})</li>"
                for d, m, t, pc in s["erros"]) + "</ul>")
        for acao, itens in s["secoes"]:
            h.append(f'<h3 class="{acao}">{ROTULO_ACAO[acao]}</h3>')
            if not itens:
                h.append('<div class="vazio">nada nesta categoria</div>')
                continue
            h.append('<ul class="itens">')
            for u, razoes, extra in itens:
                nota = (f'<span class="nota">{escape(u.nota_exibida().stem)}</span>'
                        if varias_notas(s) else "")
                href = uri(u.heading[0], u.heading[3]) if u.heading else uri(u.nota)
                alvo = seta(u)
                alvo_html = f' <span class="alvo">→ {escape(alvo)}</span>' if alvo else ""
                chips = "".join(
                    f'<a class="chip" href="{escape(hr)}">{escape(r)}</a>' if hr
                    else f'<span class="txt">{escape(r)}</span>'
                    for r, hr in extra["onde"])
                chave_item = escape(f"{s['slot']}:{u.topico}")
                h.append(
                    f'<li class="item{"" if extra["cabe"] else " sobra"}" data-k="{chave_item}">'
                    f'<label class="chk"><input type="checkbox"><span class="tempo">{escape(faixa(extra))}</span></label>'
                    f'<div class="corpo">{nota}<a class="topico" href="{href}">{escape(u.topico)}</a>{alvo_html}'
                    f'<span class="meta">{escape(meta_item(u))}</span>'
                    f'<span class="razao">{escape(" · ".join(razoes))}</span>'
                    f'<span class="onde">{chips}</span>'
                    f'<span class="como">{escape(extra["como"])}</span></div></li>')
            h.append("</ul>")
        if s["secoes"]:
            h.append(f'<div class="registro">{escape(REGISTRO)}</div>')
        h.append("</div>")
    h.append('<div class="rodape">gerado por PY/plano-dia.py com o estado atual do vault · '
             'critérios em Questoes/Paineis/Plano do dia.md · tempos são estimativas (MIN_ACAO)</div>')
    if tem_itens:
        h.append(f"<script>{JS.replace('__DIA__', dia)}</script>")
    return "\n".join(h)


def diagnostico(texto, hoje):
    k = chave(texto)
    pares = next((v for rot, v in GRADE_PARA_NOTAS.items() if k in rot), None)
    if pares is None:
        pares = [(stem, None) for stem in stems_materias() if k in chave(stem)]
    if not pares:
        print(f"Nada casou com {texto!r}.")
        return
    unidades = analisar(pares, ler_cadernos(), hoje)
    print(f"DIAGNÓSTICO — {', '.join(s + (f' [{g}]' if g else '') for s, g in pares)} · {hoje}\n")
    for u in sorted(unidades, key=lambda x: -x.peso):
        r = classificar(u, hoje)
        acao = f"{ROTULO_ACAO[r[0]]} ({r[1]:.1f})" if r else "em dia / fora"
        print(f"{u.peso:5.1f}%  dom {u.dom if u.dom is not None else '—'}  {u.topico}")
        if u.heading:
            n, i, nivel, txt = u.heading
            print(f"        heading: {'#' * nivel} {txt}  (linha {i + 1}, score {u.score:.2f}, {n.stem})")
        else:
            print("        heading: —")
        print(f"        conteúdo {u.conteudo} linhas · escrito até {data_txt(u.escrito_ult)}"
              f" · prox vencido {data_txt(u.prox_vencido)}")
        for d, erro, pct, c in sorted(u.ocorrencias, key=lambda o: o[0]):
            marca = {True: "ERRO", False: "ok", None: "sem detalhe"}[erro]
            print(f"        caderno {data_txt(d)} {marca} {pct_txt(pct)}  ({c.nome})")
        print(f"        → {acao}{' · ' + ' · '.join(r[2]) if r else ''}\n")


def main():
    ap = argparse.ArgumentParser(description="Plano do dia por subtópico.")
    ap.add_argument("--data", help="AAAA-MM-DD (padrão: hoje)")
    ap.add_argument("--texto", action="store_true", help="imprime no terminal em vez de abrir HTML")
    ap.add_argument("--diag", metavar="MATÉRIA", help="audita casamentos e métricas de uma matéria")
    a = ap.parse_args()
    hoje = date.fromisoformat(a.data) if a.data else date.today()

    if a.diag:
        diagnostico(a.diag, hoje)
        return
    p = plano(hoje)
    if a.texto:
        print(render_texto(p))
        return
    destino = Path(tempfile.gettempdir()) / "plano-dia.html"
    destino.write_text(render_html(p), encoding="utf-8")
    webbrowser.open(destino.as_uri())
    print(f"Aberto: {destino}")


if __name__ == "__main__":
    main()
