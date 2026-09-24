#!/usr/bin/env python3
"""
Busca, via a API interna do TecConcursos (a mesma que o app usa — achada
pela aba Network do navegador), as questões erradas de um ou mais cadernos
e devolve um JSON compacto: enunciado, alternativa marcada, alternativa
correta, e só o trecho da resolução comentada que explica essas duas (não
as 4) — pra manter baixo o custo de quem for ler o resultado.

Precisa de PY/.tec-cookie, com você logado no TEC. Aceita dois formatos:
  (a) a linha crua do header Cookie: "nome1=valor1; nome2=valor2; ..."
      (DevTools → Network → clique numa chamada /api/... → Cabeçalhos →
      Cabeçalhos da Requisição → "Cookie").
  (b) a tabela Nome/Valor da aba "Cookies" do inspetor (Safari): selecione
      as linhas da tabela e copie — o script reconhece "nome<tab>valor"
      por linha e monta o header sozinho.
Em qualquer caso: copie e rode `pbpaste > PY/.tec-cookie` no terminal, sem
colar o valor em chat — é equivalente a estar logado.
Esse arquivo é sensível (git-ignorado) e expira com a sessão — se o script
começar a devolver 401/403, repita os passos acima.

Uso:
    python3 PY/tec-erradas.py <idCaderno> [<idCaderno> ...]

O que o script NÃO faz de propósito: não escreve nota nenhuma no vault, não
decide matéria/bloco, e não manda atualizarCronometro=true (pra não sujar
o tempo/estatística registrados no caderno). Só lê e devolve JSON.
"""
import html
import json
import re
import sys
import time
from pathlib import Path

import requests

COOKIE_FILE = Path(__file__).parent / ".tec-cookie"
BASE = "https://www.tecconcursos.com.br/api"
LETRAS = "abcde"
PAUSA = 0.2  # segundos entre chamadas, por educação com o servidor deles


def normalizar_cookie(bruto):
    """Aceita a linha crua 'nome=valor; nome=valor' OU uma tabela colada
    (uma linha por cookie, nome e valor separados por tab/2+ espaços/':').
    Devolve sempre no formato de header: 'nome=valor; nome=valor'."""
    bruto = bruto.strip()
    linhas = [l for l in bruto.splitlines() if l.strip()]

    # já é a linha crua do header (uma linha só, com '=' e '; ')
    if len(linhas) == 1 and "=" in linhas[0] and ";" in linhas[0]:
        return linhas[0].strip()

    # tabela colada: uma linha por par nome/valor
    pares = []
    for linha in linhas:
        partes = re.split(r"\t+|:\s+| {2,}", linha.strip(), maxsplit=1)
        if len(partes) != 2:
            continue
        nome, valor = partes[0].strip(), partes[1].strip()
        if nome.lower() in ("nome", "name", "valor", "value"):
            continue  # cabeçalho da tabela
        if nome and valor:
            pares.append(f"{nome}={valor}")
    if pares:
        return "; ".join(pares)

    # única linha mas sem múltiplos pares — tenta como header mesmo assim
    return bruto


def carregar_cookie():
    if not COOKIE_FILE.exists():
        sys.exit(
            f"falta {COOKIE_FILE} — veja o cabeçalho do script pra saber "
            "como pegar o cookie no DevTools"
        )
    bruto = COOKIE_FILE.read_text(encoding="utf-8")
    if not bruto.strip():
        sys.exit(f"{COOKIE_FILE} está vazio")
    return normalizar_cookie(bruto)


def sessao(cookie):
    s = requests.Session()
    s.headers.update({
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
    })
    return s


def limpar_html(texto):
    if not texto:
        return ""
    texto = html.unescape(texto)
    texto = re.sub(r"<strong>", "**", texto)
    texto = re.sub(r"</strong>", "**", texto)
    texto = re.sub(r"<s>", "~~", texto)
    texto = re.sub(r"</s>", "~~", texto)
    texto = re.sub(r"</p>|<br\s*/?>", "\n", texto)
    texto = re.sub(r"<[^>]+>", "", texto)
    texto = re.sub(r"[ \t]+", " ", texto)
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto.strip()


def dividir_comentario_por_alternativa(html_bruto):
    """Divide o HTML bruto do comentário em blocos por marcador 'a)'..'e)'."""
    marcadores = list(re.finditer(
        r"<strong>\s*([a-e])\)\s*(?:&nbsp;)?\s*</strong>", html_bruto
    ))
    if not marcadores:
        return {}
    blocos = {}
    for i, m in enumerate(marcadores):
        letra = m.group(1)
        ini = m.end()
        fim = marcadores[i + 1].start() if i + 1 < len(marcadores) else len(html_bruto)
        blocos[letra] = limpar_html(html_bruto[ini:fim])
    return blocos


def buscar_resumo(s, id_caderno):
    r = s.get(f"{BASE}/cadernos/{id_caderno}/resumo")
    r.raise_for_status()
    return r.json()["caderno"]


def buscar_questao(s, id_caderno, n):
    r = s.get(f"{BASE}/cadernos/{id_caderno}/questoes/{n}")
    r.raise_for_status()
    return r.json()["questao"]


def buscar_comentario(s, id_questao):
    r = s.get(
        f"{BASE}/questoes/{id_questao}/comentario",
        params={"tokenPreVisualizacao": ""},
    )
    if r.status_code != 200:
        return None
    return r.json().get("comentario", {}).get("textoComentario")


def processar_caderno(s, id_caderno):
    resumo = buscar_resumo(s, id_caderno)
    total = resumo["numeroTotalQuestoes"]
    erradas = []
    for n in range(1, total + 1):
        q = buscar_questao(s, id_caderno, n)
        time.sleep(PAUSA)
        if q.get("anulada") or q.get("correcaoQuestao") or not q.get("alternativaSelecionada"):
            continue  # anulada, acertou, ou em branco/não respondida
        marcada_n = q["alternativaSelecionada"]
        correta_n = q["numeroAlternativaCorreta"]
        if marcada_n > len(LETRAS) or correta_n > len(LETRAS):
            continue  # formato inesperado (ex: questão discursiva) — pula
        letra_marcada = LETRAS[marcada_n - 1]
        letra_correta = LETRAS[correta_n - 1]
        alternativas = q.get("alternativas", [])

        item = {
            "idQuestao": q["idQuestao"],
            "materia": q.get("nomeMateria"),
            "assunto": q.get("nomeAssunto"),
            "banca": q.get("bancaSigla"),
            "orgao": q.get("orgaoNome"),
            "ano": q.get("concursoAno"),
            "enunciado": limpar_html(q.get("enunciado")),
            "marcada": {
                "letra": letra_marcada.upper(),
                "texto": limpar_html(alternativas[marcada_n - 1])
                if marcada_n - 1 < len(alternativas) else None,
            },
            "correta": {
                "letra": letra_correta.upper(),
                "texto": limpar_html(alternativas[correta_n - 1])
                if correta_n - 1 < len(alternativas) else None,
            },
        }

        html_comentario = buscar_comentario(s, q["idQuestao"])
        time.sleep(PAUSA)
        if html_comentario:
            blocos = dividir_comentario_por_alternativa(html_comentario)
            item["explicacao_marcada"] = blocos.get(letra_marcada)
            item["explicacao_correta"] = blocos.get(letra_correta)

        erradas.append(item)

    return {
        "idCaderno": id_caderno,
        "nome": resumo.get("nomeCaderno"),
        "data": resumo.get("dataCaderno"),
        "total": total,
        "acertos": resumo.get("numeroAcertos"),
        "erros": resumo.get("numeroErros"),
        "questoesErradas": erradas,
    }


def main():
    if len(sys.argv) < 2:
        sys.exit("uso: python3 PY/tec-erradas.py <idCaderno> [<idCaderno> ...]")
    cookie = carregar_cookie()
    s = sessao(cookie)
    resultado = []
    for cid in sys.argv[1:]:
        try:
            resultado.append(processar_caderno(s, cid))
        except requests.HTTPError as e:
            sys.exit(f"caderno {cid}: {e} — cookie expirado? renove PY/.tec-cookie")
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
