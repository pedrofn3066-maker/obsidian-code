---
description: Extrai um PDF pra Markdown de trabalho, lê por blocos e propõe (sem escrever) a distribuição dos insights nas notas de MATERIAS
argument-hint: <caminho do PDF> [matéria de destino]
---

Absorva o PDF `$ARGUMENTS`: extraia o texto, leia por blocos, cruze com o que o cofre já tem e **proponha** onde cada insight entra. **Não escreva em `MATERIAS/` antes do Pedro aprovar a tabela de distribuição.**

## Passo 1 — extrair

```
python3 PY/pdf-md.py "<pdf>"
```

Grava em `.vault-meta/pdf-md/<nome>.md` (ignorado pelo git). Leia a saída do script:

- `⚠️ N pág(s) com pouco texto` → são figuras, esquemas ou capa. Para essas páginas, leia o PDF direto (`Read` com `pages`) e anote no plano o que o esquema diz. Se o PDF inteiro for assim, é escaneado: pare e avise, não há OCR instalado.
- O `.md` é insumo, não conteúdo final. Nunca o copie inteiro pra uma nota de `MATERIAS/`.

## Passo 2 — orientar-se no destino sem ler tudo

Mesma regra do `/triar-inbox` (notas de `MATERIAS/` têm até 1400+ linhas):

- Qual nota? `python3 PY/diretorio-materias.py [palavra]`
- Quais headings, `dom::` e peso VINTEUM? `python3 PY/indice-materia.py "MATERIAS/<nota>.md"`
- Linha exata de um heading (tolera NBSP)? `python3 PY/achar-heading.py "MATERIAS/<nota>.md" "<trecho>"`

**Nunca use `old_string` exato em `MATERIAS/`** (NBSP escondido). Escreva por índice de linha, em Python.

## Passo 3 — ler por blocos

Leia o `.md` extraído em blocos de ~10–15 páginas (pelos marcadores `<!-- p.N -->`), não de uma vez. Para cada bloco, anote: assunto, artigos/dispositivos, o que a banca costuma cobrar (nos resumos comerciais, `Bizú`, `Cuidado`, `IMPORTANTE` e `<mark>` são os sinais).

Em cada bloco, antes de propor, confira o que a nota de destino **já tem** naquele heading (leia só aquele trecho, pela linha do `achar-heading.py`). Classifique:

- **novo** — a nota não trata disso;
- **complementa** — a nota trata, mas falta um dispositivo, uma pegadinha ou um detalhe;
- **já existe** — não propor de novo.

## Passo 4 — o plano (o que o Pedro vê e aprova)

Tabela, uma linha por insight, sem texto colado:

| Págs | Assunto / dispositivo | Nota → heading | Peso VINTEUM · dom | Ação (novo / complementa) | Resumo em 1 linha |
| --- | --- | --- | --- | --- | --- |

Depois da tabela:

1. **Não distribuído**, com o motivo (já existe, fora do edital, esquema em imagem que precisa de decisão).
2. **Sobreposições** entre notas (mesma regra do `/triar-inbox`: perguntar com `AskUserQuestion` em vez de escolher).
3. **Onde estudar primeiro**, cruzando peso do edital com `dom::` atual.

Pare aqui e peça aprovação. Só siga se o Pedro aprovar (total ou parcial).

## Passo 5 — escrever (só após aprovação)

- Registro da nota de destino: denso, direto, `<mark>` no núcleo da regra, ⚠️ na pegadinha de banca.
- **O lastro é intocável**: nunca acrescente fato, número, artigo ou exemplo que não esteja no PDF. Trecho cortado ou fórmula incompleta → `> [!warning]-` com a pendência, não complete.
- Cite a origem pela página: `(Resumo EC 132, p. 12)`.
- Texto com voz de professor/apostila ("Galera, atenção...") → passe pela skill `voz-autoral` (AUDITAR) antes de colar.
- Heading novo: `- [ ] status [dom:: 0] [peso:: N]`, **N = `peso` do frontmatter da nota**, nunca o percentual VINTEUM.
- Se o assunto exige dois headings, faça irmãos no mesmo nível; heading-pai só se tiver conteúdo direto.

## Passo 6 — verificar e reportar

1. Depois de cada edição em `MATERIAS/`:
   ```
   git diff -U0 -- "<nota>" | grep "^-" | grep -v "^---" | sed 's/^-//' | sort > $TMPDIR/r.txt
   git diff -U0 -- "<nota>" | grep "^+" | grep -v "^+++" | sed 's/^+//' | sort > $TMPDIR/a.txt
   comm -23 $TMPDIR/r.txt $TMPDIR/a.txt
   ```
   Só linha vazia ou o que você removeu de propósito. Qualquer outra coisa é conteúdo perdido: pare e investigue.
2. Relate em tabela o que entrou e onde, e qual tópico merece o próximo bloco de estudo.
3. `python3 PY/plano-dia.py --diag "<matéria>"` e diga em que seção os tópicos tocados caíram.

O PDF em `inbox/` **fica onde está** (nunca apague). Não commite sem o Pedro pedir.
