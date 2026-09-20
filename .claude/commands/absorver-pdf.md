---
description: Extrai um PDF pra Markdown de trabalho, lê por blocos e propõe (sem escrever) a distribuição nas notas de MATERIAS, com pontes pro resto do cofre, texto literal onde a banca cobra literalidade e lupa didática nos tópicos difíceis
argument-hint: <caminho do PDF> [matéria de destino]
---

Absorva o PDF `$ARGUMENTS`: extraia o texto, leia por blocos, cruze com o que o cofre já tem e **proponha** onde cada insight entra. **Não escreva em `MATERIAS/` antes do Pedro aprovar a tabela de distribuição.**

Tudo o que entra na nota é de um de três tipos. Cada um tem sua regra de origem, e o tipo decide o que pode ser escrito:

- **Lastro** — o que o PDF diz. Só fato, número, artigo ou exemplo que está no PDF, citado pela página. Intocável.
- **Ponte** — ligação com o que o cofre já sabe: outro heading (`[[Nota#Heading]]`), jurisprudência já registrada na nota, erro de caderno do tópico. Só liga o que existe; a ponte nunca traz fato novo.
- **Lupa** — explicação didática de um tópico difícil, escrita por você, em callout recolhido. Explica o lastro; não acrescenta regra. Todo número ou exemplo que não vier do PDF é rotulado `exemplo ilustrativo (sem lastro)`.

## Passo 1 — extrair

```
python3 PY/pdf-md.py "<pdf>"
```

Grava em `.vault-meta/pdf-md/<nome>.md` (ignorado pelo git). Leia a saída do script:

- `⚠️ N pág(s) com pouco texto` → são figuras, esquemas ou capa. Para essas páginas, leia o PDF direto (`Read` com `pages`) e anote no plano o que o esquema diz. Se o PDF inteiro for assim, é escaneado: pare e avise, não há OCR instalado.
- O `.md` é insumo, não conteúdo final. Nunca o copie inteiro pra uma nota de `MATERIAS/`.
- **PDF em duas colunas** (texto embaralhado, frases de colunas diferentes misturadas): refaça a extração por coluna com `pymupdf`, no scratchpad, ordenando os blocos por coluna e depois por `y`. Se o PDF tem lei seca e camada editorial (quadros, comentários, "Veja como foi cobrado"), separe pelo tamanho da fonte: a camada editorial costuma ser o que a nota ainda não tem.

## Passo 2 — orientar-se no destino sem ler tudo

Mesma regra do `/triar-inbox` (notas de `MATERIAS/` têm até 1400+ linhas):

- Qual nota? `python3 PY/diretorio-materias.py [palavra]`
- Quais headings, `dom::` e peso VINTEUM? `python3 PY/indice-materia.py "MATERIAS/<nota>.md"`
- Linha exata de um heading (tolera NBSP)? `python3 PY/achar-heading.py "MATERIAS/<nota>.md" "<trecho>"`
- Onde o Pedro erra hoje? `python3 PY/plano-dia.py --diag "<matéria>"` — guarde os tópicos com `ERRO`, `dom` baixo ou "nunca testado em caderno": são o mapa do que precisa de **lupa**.

**Nunca use `old_string` exato em `MATERIAS/`** (NBSP escondido). Escreva por índice de linha, em Python.

## Passo 3 — ler por blocos

Leia o `.md` extraído em blocos de ~10–15 páginas (pelos marcadores `<!-- p.N -->`), não de uma vez. Para cada bloco, anote: assunto, artigos/dispositivos, o que a banca costuma cobrar (nos resumos comerciais, `Bizú`, `Cuidado`, `IMPORTANTE` e `<mark>` são os sinais).

Em cada bloco, antes de propor, confira o que a nota de destino **já tem** naquele heading (leia só aquele trecho, pela linha do `achar-heading.py`). Classifique:

- **novo** — a nota não trata disso;
- **complementa** — a nota trata, mas falta um dispositivo, uma pegadinha ou um detalhe;
- **já existe** — não propor de novo.

Depois, para cada linha que vai à tabela, decida três coisas:

1. **Ponte.** Procure o que o cofre tem em volta: `python3 PY/diretorio-materias.py` e `grep` por dispositivo, termo ou súmula nas notas vizinhas. Registre só ligações que você achou (heading real, com linha), do tipo: mesmo instituto em outra matéria (ex.: norma pública × CPC privado), jurisprudência já na nota que testa a regra, tópico irmão com a regra oposta, erro de caderno do `--diag`.
2. **Texto literal.** Entra o dispositivo em bloco `>` quando a banca cobra a literalidade: prazo, rol taxativo, condição, percentual, quórum, competência. Copie do PDF sem alterar e cite a página. Trecho cortado → `> [!warning]-`.
3. **Lupa.** Um tópico é **difícil** se bater em pelo menos um: (a) `ERRO` recente no `--diag`; (b) peso VINTEUM ≥ 5% com `dom` ≤ 1; (c) quadro em que a banca troca termos entre categorias; (d) mecânica com passos (cálculo, lançamento, contagem de prazo, ordem de preferência). Fora desses critérios, não escreva lupa: uma nota carregada de callouts perde o núcleo.

## Passo 4 — o plano (o que o Pedro vê e aprova)

Tabela, uma linha por insight, sem texto colado:

| Págs | Assunto — resumo em 1 linha | Nota → heading | Peso VINTEUM · dom | Ação (novo / complementa) | Recurso (texto literal / lupa / —) | Ponte (heading real) |
| --- | --- | --- | --- | --- | --- | --- |

Depois da tabela:

1. **Não distribuído**, com o motivo (já existe, fora do edital, esquema em imagem que precisa de decisão).
2. **Sobreposições** entre notas (mesma regra do `/triar-inbox`: perguntar com `AskUserQuestion` em vez de escolher).
3. **Onde estudar primeiro**, cruzando peso do edital com `dom::` atual e com os erros de caderno.

Pare aqui e peça aprovação. Só siga se o Pedro aprovar (total ou parcial). Está concluído quando a tabela tem as sete colunas preenchidas em todas as linhas e a pergunta de aprovação foi feita.

## Passo 5 — escrever (só após aprovação)

Cada linha aprovada entra na nota nesta ordem, e só com os recursos que a tabela marcou:

1. **Lastro:** registro denso e direto, `<mark>` no núcleo da regra, ⚠️ na pegadinha de banca, origem pela página `(Resumo EC 132, p. 12)`. Quadro do PDF vira tabela markdown.
2. **Texto literal:** bloco `>` com o dispositivo, na página citada.
3. **Lupa:** callout recolhido `> [!tip]- Lupa: <tema>` com três partes, nesta ordem: **a ideia em uma frase** (o que a regra protege ou resolve) → **o passo a passo** com um exemplo (do PDF; se for seu, `exemplo ilustrativo (sem lastro)`) → **o erro clássico** (como a banca troca o termo ou inverte a regra). Linguagem de quem explica a um colega: direta, sem "Galera, atenção...".
4. **Ponte:** uma linha `> [!info]- Ponte` com os `[[links]]` e o que cada um acrescenta ("mesma regra no CPC 27 privado", "a Súm. X da nota testa isto", "errou em 17/09"). Confira cada link com `achar-heading.py` antes de gravar.

Regras da escrita:

- **Tabela sempre na margem** (coluna 0), com linha em branco antes e depois. Nunca recuada dentro de item de lista: o Obsidian não renderiza. O título da tabela vai em parágrafo próprio, não em bullet.
- **O lastro é intocável:** nunca acrescente fato, número, artigo ou exemplo que não esteja no PDF, fora da lupa e da ponte. Trecho cortado ou fórmula incompleta → `> [!warning]-` com a pendência, não complete.
- Texto do PDF com voz de professor/apostila → passe pela skill `voz-autoral` (AUDITAR) antes de colar. A lupa, por ser sua, já sai neutra.
- Heading novo: `- [ ] status [dom:: 0] [peso:: N]`, **N = `peso` do frontmatter da nota**, nunca o percentual VINTEUM.
- Se o assunto exige dois headings, faça irmãos no mesmo nível; heading-pai só se tiver conteúdo direto.

Está concluído quando cada linha da tabela aprovada tem o que marcou (lastro, mais texto literal, lupa e ponte quando previstos) e todo `[[link]]` resolve.

## Passo 6 — verificar e reportar

1. Depois de cada edição em `MATERIAS/`:
   ```
   git diff -U0 -- "<nota>" | grep "^-" | grep -v "^---" | sed 's/^-//' | sort > $TMPDIR/r.txt
   git diff -U0 -- "<nota>" | grep "^+" | grep -v "^+++" | sed 's/^+//' | sort > $TMPDIR/a.txt
   comm -23 $TMPDIR/r.txt $TMPDIR/a.txt
   ```
   Só linha vazia ou o que você removeu de propósito. Qualquer outra coisa é conteúdo perdido: pare e investigue.
2. **Renderização:** `python3 PY/checar-markdown.py "<nota>"` (só as linhas alteradas). Tabela recuada, sem linha em branco antes ou com nº de colunas errado → corrija antes de reportar. Deve terminar em `OK`.
3. **Auditoria de lastro:** releia o que você escreveu e confira que todo fato fora de lupa e ponte está no PDF, na página citada. O que falhar sai ou vira `> [!warning]-`.
4. Relate em tabela o que entrou e onde, com as colunas Recurso e Ponte, e qual tópico merece o próximo bloco de estudo.
5. `python3 PY/plano-dia.py --diag "<matéria>"` e diga em que seção os tópicos tocados caíram, cruzando com os erros de caderno que motivaram cada lupa.

O PDF em `inbox/` **fica onde está** (nunca apague). Não commite sem o Pedro pedir.
