#!/usr/bin/env python3
"""
Fechamento de domingo: congela, para a semana que começa na segunda, o que o
Ganho potencial, a Fila de reforço e o edital dizem — e grava em
Questoes/Paineis/Fechamento da semana.md. O PY/plano-dia.py lê essa nota.

O que o fechamento decide (a grade NÃO é reescrita — ela continua sendo o piso):
  1. Ranking de blocos por ganho potencial (pontos × quanto falta até 85%).
  2. Qual matéria entra em cada rodízio de S5 na semana.
  3. Quanto cada nota pesa na ordem dos tópicos de um slot (erro em questões +
     lacuna do edital) — nota sem caderno não some: o edital cobre.
  4. Quais blocos ganham +1 item de questões/revisão (os 3 primeiros do ranking).

    python3 PY/fechamento-semana.py              # grava a nota (rode no slot de fechamento do domingo)
    python3 PY/fechamento-semana.py --dry-run    # só imprime, não grava
    python3 PY/fechamento-semana.py --data 2026-09-20   # simula outro dia
"""
import argparse
import importlib.util
import json
import re
from datetime import date, timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("plano_dia", AQUI / "plano-dia.py")
pd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pd)

SAIDA = pd.VAULT / "Questoes" / "Paineis" / "Fechamento da semana.md"

# ---------------------------------------------------------------------------
# CONFIGURAÇÃO — mesmos números do painel Ganho potencial.md (Dataview). Se mudar
# um, mude o outro: o Dataview não consegue ser lido daqui.
# ---------------------------------------------------------------------------
PONTOS = {
    "Cont. Avançada e de Custos": 40, "Direito Tributário": 40,
    "Legislação Tributária": 40, "Finanças Públicas": 20,
    "Fluência de Dados": 20, "Mat. Fin./Estat./RLM": 12,
    "Const./Adm./Civil/Penal": 12, "Língua Portuguesa": 10,
    "Adm. e Governança": 10, "Economia": 10,
    "Cont. Geral e Pública": 10, "Direito Financeiro": 8, "Auditoria": 8,
}
META = 0.85
JANELA = 30            # dias de Diario que entram na conta
K_BLOCO = 60           # "questões fantasma" na média geral: amostra pequena puxa para a média
K_NOTA = 30            # idem, da nota para o acerto do seu bloco
AMOSTRA_Q, AMOSTRA_CAD = 60, 3
TOP = 3                # blocos que ganham cota extra no plano
PESO_ERRO, PESO_EDITAL = 0.7, 0.3   # mistura da ordem entre notas: erro em questões × lacuna do edital
FOME = 0.25            # rodízio: +25% no score por semana sem aparecer (máx. 4 semanas)
HISTORICO = 8

# nota (stem de MATERIAS) -> bloco do Ganho potencial
NOTA_BLOCO = {
    "P2 - Contabilidade Avançada e de Custos": "Cont. Avançada e de Custos",
    "P2 - Direito Tributário": "Direito Tributário",
    "P2 - Reforma Tributária": "Direito Tributário",
    "P2 - Legislação Tributária Estadual (BA)": "Legislação Tributária",
    "P2 - Finanças Públicas": "Finanças Públicas",
    "P2 - Fluência de Dados BD": "Fluência de Dados",
    "P2 - Fluência de Dados CD": "Fluência de Dados",
    "P2 - Fluência de Dados SGE": "Fluência de Dados",
    "P2 - Fluência de Dados SGE-C": "Fluência de Dados",
    "P2 - Tecnologia da Informação": "Fluência de Dados",
    "P2 - Matemática Financeira": "Mat. Fin./Estat./RLM",
    "P1 - Estatística": "Mat. Fin./Estat./RLM",
    "P2 - Estatística Aplicada": "Mat. Fin./Estat./RLM",
    "P1 - Raciocínio Lógico": "Mat. Fin./Estat./RLM",
    "P1 - Direito Constitucional": "Const./Adm./Civil/Penal",
    "P1 - Direito Administrativo": "Const./Adm./Civil/Penal",
    "P1 - Direito Civil": "Const./Adm./Civil/Penal",
    "P1 - Penal": "Const./Adm./Civil/Penal",
    "P1 - Língua Portuguesa": "Língua Portuguesa",
    "P1 - Administração e Governança Pública": "Adm. e Governança",
    "P1 - Administração Geral": "Adm. e Governança",
    "P1 - Macro Economia": "Economia",
    "P1 - Micro e Finanças Públicas": "Economia",
    "P1 - Contabilidade Geral": "Cont. Geral e Pública",
    "P2 - CASP": "Cont. Geral e Pública",
    "P1 - Direito Financeiro": "Direito Financeiro",
    "P1 - Auditoria": "Auditoria",
}


NOME_RODIZIO = {
    "rodizio 4 (constitucional, administrativo, civil, penal)": "Rodízio 4 (S5 de quarta)",
    "cont. geral (impares)/cont. publica (pares)": "Cont. Geral/Pública (S3 de sábado)",
    "micro (impares)/macro (pares)": "Micro/Macro (S4 de sábado)",
}


# Barra de botões dos painéis (estilo em .obsidian/snippets/painel.css)
BOTOES = '<div class="botoes-painel"><a class="botao" href="obsidian://shell-commands/?vault=vault-ba&amp;execute=planodia01">📅 Plano do dia</a> <a class="botao" href="obsidian://shell-commands/?vault=vault-ba&amp;execute=s1ontem01">🧠 S1 - Revisão de ontem</a> <a class="botao" href="obsidian://shell-commands/?vault=vault-ba&amp;execute=fechasemana01">📊 Fechamento da semana</a></div>'

def proxima_segunda(hoje):
    """Domingo -> amanhã. Segunda -> hoje (esqueceu no domingo). Terça a sábado -> a próxima."""
    return hoje if hoje.weekday() == 0 else hoje + timedelta(days=7 - hoje.weekday())


def blocos_do_diario():
    """stem do caderno -> valor do campo `bloco` (o Ganho potencial agrupa por ele)."""
    out = {}
    for f in pd.DIARIO.glob("*.md"):
        m = re.match(r"---\n(.*?)\n---", f.read_text(encoding="utf-8"), re.S)
        b = re.search(r"^bloco:\s*(.+)$", m.group(1), re.M) if m else None
        if b:
            out[f.stem] = pd.nfc(b.group(1).strip().strip("\"'"))
    return out


def nome_curto(stem):
    return re.sub(r"^P\d - ", "", stem)


def calcular(hoje):
    cads = [c for c in pd.ler_cadernos()
            if c.total and c.acertos is not None and hoje - timedelta(days=JANELA) <= c.data <= hoje]
    do_bloco = blocos_do_diario()
    avisos = []

    agg = {b: [0, 0, 0] for b in PONTOS}          # bloco -> [questões, acertos, cadernos]
    alvo = {}                                     # caderno -> notas que recebem o crédito dele
    for c in cads:
        b = do_bloco.get(c.nome)
        if b not in PONTOS:
            avisos.append(f"caderno {c.nome!r}: bloco {b!r} fora de PONTOS — ignorado")
            continue
        agg[b][0] += c.total
        agg[b][1] += c.acertos
        agg[b][2] += 1
        stems = {s for s, _ in c.pares}
        # o caderno "Contabilidade Geral" também mapeia para a nota Avançada (plano-dia.py); aqui só
        # recebe crédito a nota do mesmo bloco do caderno. Sem nenhuma do bloco, vale o mapeamento inteiro.
        alvo[c.nome] = {s for s in stems if NOTA_BLOCO.get(s) == b} or stems
        for s in alvo[c.nome] - {s for s in stems if NOTA_BLOCO.get(s) == b}:
            avisos.append(f"{c.materia}: cadernos com bloco {b!r}, mas a nota {s!r} está fixa em "
                          f"{NOTA_BLOCO.get(s)!r} — crédito dado à nota mesmo assim (confira NOTA_BLOCO ou o `bloco` do caderno)")

    tot_q = sum(v[0] for v in agg.values())
    media = sum(v[1] for v in agg.values()) / tot_q if tot_q else 0.6

    blocos = []
    for b, (t, a, n) in agg.items():
        suav = (a + K_BLOCO * media) / (t + K_BLOCO)
        amostra = "sem dado" if t == 0 else ("baixa" if t < AMOSTRA_Q or n < AMOSTRA_CAD else "ok")
        blocos.append({"bloco": b, "pontos": PONTOS[b], "questoes": t, "cadernos": n,
                       "acerto_bruto": round(a / t, 4) if t else None, "acerto": round(suav, 4),
                       "ganho": round(PONTOS[b] * max(0.0, META - suav), 2), "amostra": amostra})
    blocos.sort(key=lambda x: -x["ganho"])
    for i, b in enumerate(blocos, 1):
        b["posicao"] = i
    por_bloco = {b["bloco"]: b for b in blocos}

    # ---- por nota: erro em questões (30d) + lacuna do edital (dom do checklist VINTEUM)
    notas = {}
    for stem, bloco in NOTA_BLOCO.items():
        t = a = 0
        for c in cads:
            if stem in alvo.get(c.nome, ()):
                t += c.total
                a += c.acertos
        suav = (a + K_NOTA * por_bloco[bloco]["acerto"]) / (t + K_NOTA)
        lac = None
        if (pd.MATERIAS / f"{stem}.md").exists():
            itens = [(d, p) for _, _, its in pd.carregar(stem).checklists for _, d, p in its]
            soma = sum(p for _, p in itens)
            lac = sum(p * (5 - d) / 5 for d, p in itens) / soma if soma else None
        notas[stem] = {"bloco": bloco, "questoes": t, "acerto": round(suav, 4),
                       "necessidade": round(max(0.0, META - suav), 4),
                       "lacuna_edital": round(lac, 4) if lac is not None else None}
    max_nec = max((n["necessidade"] for n in notas.values()), default=0) or 1
    lacs = [n["lacuna_edital"] for n in notas.values() if n["lacuna_edital"] is not None]
    max_lac = max(lacs, default=0) or 1
    lac_med = (sum(lacs) / len(lacs) / max_lac) if lacs else 0.5
    for n in notas.values():
        lac_rel = n["lacuna_edital"] / max_lac if n["lacuna_edital"] is not None else lac_med
        n["peso_ordem"] = round(PESO_ERRO * n["necessidade"] / max_nec + PESO_EDITAL * lac_rel, 4)

    reforco = sorted(
        [c for c in cads if c.acertos / c.total < pd.CORTE_ERRO],
        key=lambda c: c.acertos / c.total)
    return cads, blocos, por_bloco, notas, reforco, avisos, media


def texto_ausencia(h, stem):
    if stem not in h:
        return "sem escolha recente"
    i = h.index(stem)
    return "escolhida na semana passada" if i == 0 else f"escolhida há {i + 1} semanas"


def escolher_rodizios(seg, notas, antigo):
    """Um rodízio por rótulo de S5. Score = ordem da nota × (1 + FOME × semanas sem aparecer)."""
    semana = (seg - pd.INICIO_CICLO).days // 7 + 1
    hist_antigo = (antigo or {}).get("historico_rodizios", {})
    mesma = (antigo or {}).get("semana_inicio") == seg.isoformat()
    rodizios, historico = {}, {}
    for rot, opcoes in pd.RODIZIOS.items():
        h = list(hist_antigo.get(rot) or [])
        if mesma and h:
            h = h[1:]                       # refazendo a mesma semana: descarta a escolha anterior
        if not h:                           # sem histórico: assume que as semanas passadas seguiram o padrão
            for k in range(1, len(opcoes) + 1):
                if semana - k >= 1:
                    h.append(opcoes[(semana - k - 1) % len(opcoes)][0][0])
        melhor = None
        for op in opcoes:
            stem = op[0][0]
            ausente = min(h.index(stem), 4) if stem in h else 4
            score = notas[stem]["peso_ordem"] * (1 + FOME * ausente)
            if melhor is None or score > melhor[0]:
                melhor = (score, op, stem, ausente)
        _, op, stem, ausente = melhor
        n = notas[stem]
        rodizios[rot] = {
            "escolha": [[s, g] for s, g in op],
            "motivo": (f"{nome_curto(stem)} — acerto {n['acerto']:.0%} ({n['questoes']} questões em {JANELA}d), "
                       f"lacuna do edital {pct(n['lacuna_edital'])}, "
                       f"{texto_ausencia(h, stem)} · fechamento de domingo"),
        }
        historico[rot] = ([stem] + h)[:HISTORICO]
    return rodizios, historico


def ler_antigo():
    if not SAIDA.exists():
        return None
    m = re.search(r"```json\n(.*?)\n```", SAIDA.read_text(encoding="utf-8"), re.S)
    try:
        return json.loads(m.group(1)) if m else None
    except json.JSONDecodeError:
        return None


def pct(x):
    return "—" if x is None else f"{x * 100:.1f}%".replace(".", ",")


def num(x):
    return f"{x:.2f}".replace(".", ",")


def md(s):
    return str(s).replace("|", "/").replace("\n", " ")


def tabela_slots(seg, rodizios, por_bloco, notas):
    semana = (seg - pd.INICIO_CICLO).days // 7 + 1
    grade = pd.ler_grade()
    linhas = ["| Dia | S2 | S3 | S4 | S5 |", "| --- | --- | --- | --- | --- |"]
    for k, dia in enumerate(pd.DIAS[:6]):
        cel = {}
        for slot, _, rot in grade.get(dia, []):
            if pd.especial(rot):
                cel[slot] = md(rot)
                continue
            pares, _ = pd.resolver(rot, semana)
            escolha = rodizios.get(pd.chave(rot))
            if escolha:
                pares = [tuple(x) for x in escolha["escolha"]]
                rot = f"{NOME_RODIZIO.get(pd.chave(rot), rot).split(' (')[0]} → **{nome_curto(pares[0][0])}**"
            b = NOTA_BLOCO.get(pares[0][0]) if pares else None
            cel[slot] = md(rot) + (f" · #{por_bloco[b]['posicao']}" if b else "")
        linhas.append(f"| {pd.NOME_DIA[k].capitalize()} | " +
                      " | ".join(cel.get(s, "—") for s in ("S2", "S3", "S4", "S5")) + " |")
    return "\n".join(linhas)


def montar(hoje, seg):
    cads, blocos, por_bloco, notas, reforco, avisos, media = calcular(hoje)
    antigo = ler_antigo()
    rodizios, historico = escolher_rodizios(seg, notas, antigo)
    top = [b["bloco"] for b in blocos[:TOP]]
    dados = {"versao": 1, "semana_inicio": seg.isoformat(), "gerado_em": hoje.isoformat(),
             "janela_dias": JANELA, "meta": META, "top": top, "blocos": blocos, "notas": notas,
             "rodizios": rodizios, "historico_rodizios": historico}

    L = ["---", "tipo: fechamento", f"semana_inicio: {seg.isoformat()}", f"gerado_em: {hoje.isoformat()}", "---",
         "# Fechamento da semana", "", BOTOES, "",
         f"Semana de **{seg.strftime('%d/%m/%Y')}** · fechado em {hoje.strftime('%d/%m/%Y')} · janela de {JANELA} dias "
         f"({len(cads)} cadernos) · meta {META:.0%}.", "",
         "Gerado por `PY/fechamento-semana.py` — não edite à mão, "
         "[▶ rode de novo](obsidian://shell-commands/?vault=vault-ba&execute=fechasemana01). O [[Plano do dia]] lê o bloco "
         "`json` no fim desta nota e só o aplica nos dias da semana acima.", "",
         "A grade continua sendo o piso: o fechamento só decide o rodízio de S5, a ordem dos tópicos dentro do slot "
         f"e o item extra de questões/revisão dos {TOP} primeiros blocos.", "",
         "## Ganho potencial", "",
         f"`pontos × máx(0, {META:.0%} − acerto)`. O acerto é **suavizado** com {K_BLOCO} questões fantasma na média "
         f"geral ({pct(media)}): bloco com poucas questões não sobe nem some por acaso, e bloco sem caderno usa a média.", "",
         "| # | Bloco | Pontos | Questões | Cadernos | Acerto (bruto) | Acerto (usado) | Ganho | Amostra |",
         "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for b in blocos:
        L.append(f"| {b['posicao']} | {b['bloco']} | {b['pontos']} | {b['questoes']} | {b['cadernos']} | "
                 f"{pct(b['acerto_bruto'])} | {pct(b['acerto'])} | {num(b['ganho'])} | {b['amostra']} |")
    L += ["", f"**Prioridade da semana:** {', '.join(f'{i}. {b}' for i, b in enumerate(top, 1))}.", "",
          "## Slots da semana", "",
          "`#` é a posição do bloco no ranking. Rodízios de S5 mostram a matéria escolhida.", "",
          tabela_slots(seg, rodizios, por_bloco, notas), "", "### Rodízios", ""]
    for rot, r in rodizios.items():
        L.append(f"- **{NOME_RODIZIO.get(rot, rot)}**: {r['motivo']}")
    L += ["", "## Fila de reforço", "",
          f"Cadernos dos últimos {JANELA} dias abaixo de {pd.CORTE_ERRO:.0%}: abaixo de {pd.CORTE_RELEITURA:.0%} volta para "
          "releitura; entre os dois, nova bateria em 7 dias. O plano do dia já puxa isso **por tópico**, ao vivo "
          "(seção *Revisar*, mesmo corte) — esta tabela é o mapa da semana.", ""]
    if reforco:
        L += ["| Data | Matéria | Assuntos | % | Ação |", "| --- | --- | --- | --- | --- |"]
        for c in reforco:
            assuntos = [t for t, e, _ in c.itens if e is not False] or [t for t, _, _ in c.itens]
            p = c.acertos / c.total
            resumo = "; ".join(assuntos[:3])
            resumo = resumo if len(resumo) <= 140 else resumo[:137] + "…"
            L.append(f"| {pd.data_txt(c.data)} | {md(c.materia)} | {md(resumo)} | {pct(p)} | "
                     f"{'Releitura' if p < pd.CORTE_RELEITURA else 'Refazer em 7d'} |")
    else:
        L.append("Nenhum caderno abaixo de 70% na janela.")
    L += ["", "## Ordem das notas dentro do slot", "",
          f"`peso_ordem = {PESO_ERRO:g} × necessidade (erro em questões, suavizado) + {PESO_EDITAL:g} × lacuna do edital` "
          "(ambos relativos ao maior). Vale só quando o slot tem mais de uma nota; multiplica o score dos tópicos por "
          f"1 + 0,5 × peso_ordem. Lacuna do edital = média de (5 − dom)/5 ponderada pelo peso VINTEUM do checklist.", "",
          "| Nota | Bloco | Questões (30d) | Acerto usado | Lacuna do edital | peso_ordem |",
          "| --- | --- | --- | --- | --- | --- |"]
    for stem, n in sorted(notas.items(), key=lambda kv: -kv[1]["peso_ordem"]):
        L.append(f"| {nome_curto(stem)} | {n['bloco']} | {n['questoes']} | {pct(n['acerto'])} | "
                 f"{pct(n['lacuna_edital'])} | {num(n['peso_ordem'])} |")
    if avisos:
        L += ["", "## Avisos", ""] + [f"- {a}" for a in sorted(set(avisos))]
    L += ["", "## Dados (lidos pelo plano-dia.py)", "", "```json",
          json.dumps(dados, ensure_ascii=False, indent=1), "```", ""]
    return "\n".join(L), blocos, top, rodizios, avisos


def main():
    ap = argparse.ArgumentParser(description="Fechamento de domingo: ganho potencial + fila de reforço + edital.")
    ap.add_argument("--data", help="AAAA-MM-DD (padrão: hoje)")
    ap.add_argument("--dry-run", action="store_true", help="imprime a nota sem gravar")
    a = ap.parse_args()
    hoje = date.fromisoformat(a.data) if a.data else date.today()
    seg = proxima_segunda(hoje)
    texto, blocos, top, rodizios, avisos = montar(hoje, seg)
    if hoje.weekday() != 6:
        print(f"⚠ hoje é {pd.NOME_DIA[hoje.weekday()]}, não domingo — o fechamento vale para a semana de {seg:%d/%m}. "
              "Simulado e correção de domingo só entram se rodar depois deles.")
    if a.dry_run:
        print(texto)
        return
    SAIDA.write_text(texto, encoding="utf-8")
    print(f"Gravado: {SAIDA.relative_to(pd.VAULT)} · semana de {seg:%d/%m/%Y}")
    print("Prioridade:", "; ".join(f"{i}. {b}" for i, b in enumerate(top, 1)))
    for rot, r in rodizios.items():
        print(f"{NOME_RODIZIO.get(rot, rot)}: {r['motivo']}")
    for av in sorted(set(avisos)):
        print("⚠", av)


if __name__ == "__main__":
    main()
