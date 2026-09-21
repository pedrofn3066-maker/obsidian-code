---
name: tirar-duvida
description: Tira dúvidas sobre matérias e tópicos de estudo (Direito Tributário, Reforma Tributária, Auditoria, Contabilidade, Direito Administrativo etc.) buscando a explicação primeiro no cofre (MATERIAS, wiki, Erradas, Questoes) e, só se o cofre não cobrir, pesquisando na internet em fonte oficial. Use quando o Pedro perguntar "o que é X", "explica Y", "qual a diferença entre A e B", "como a banca cobra Z", "tira uma dúvida".
---

# Tirar dúvida (cofre primeiro, internet depois)

Paths relativos à raiz do cofre (`vault-ba/`). Responde a dúvida de estudo. **Não edita o cofre por conta própria** — só lê. As únicas escritas permitidas são: guardar a dúvida em `Questoes/Duvidas.md` quando o Pedro pedir (ver "Guardar a dúvida") e mover a entrada já respondida para o caderno de erros da matéria (ver "Arrumar o layout e mover para o caderno da matéria").

## Passo 1 — buscar no cofre

Ordem de busca (pare quando tiver base suficiente, mas confira 2 fontes se for tema cobrado por literalidade):

1. **Descobrir a matéria:** `python3 PY/diretorio-materias.py <palavra>` lista as notas de `MATERIAS/` com bloco/peso/prioridade.
2. **Achar o tópico em headings:** `python3 PY/achar-heading.py "MATERIAS/<nota>.md" "<trecho>"` devolve a linha exata (tolera NBSP escondido). Para ver a árvore da nota: `python3 PY/indice-materia.py "MATERIAS/<nota>.md"`.
3. **Busca no corpo (todas as notas):**
   ```bash
   grep -rniE --include='*.md' 'sujeito.{1,2}passivo' MATERIAS wiki Erradas Questoes | cut -c1-160
   ```
   - Sempre com aspas em `--include='*.md'` (zsh quebra sem aspas).
   - Use `.{1,2}` entre palavras em vez de espaço: o cofre tem `\xa0` (NBSP) que casa com `.` mas não com espaço comum.
   - Tente também sem acento/termos vizinhos (ex.: `ICMS` e `substitui.{1,3}o tribut`).
4. **Ler o trecho:** `Read` com `offset`/`limit` na linha achada (~40 linhas). Nunca leia a nota inteira — têm 100 a 1400+ linhas.
5. **Onde o Pedro erra:** `Erradas/ERRO <MATÉRIA>.md` e `Questoes/Diario/` mostram questões erradas e assuntos testados; cite se ajudar ("você errou isso em 14/09").
6. **Pontos de atenção/súmulas:** `wiki/concepts/` (súmulas vinculantes, pontos de atenção da Reforma Tributária).
7. **Material bruto (PDF de lei/aula):** `MATERIAL/` — só cite o caminho; extrair PDF é trabalho do `/absorver-pdf`.

## Passo 2 — decidir se o cofre basta

- **Basta:** achou o tópico com explicação/literal suficiente para responder → responda só com isso.
- **Parcial:** achou o assunto, mas falta um ponto (prazo, exceção, jurisprudência, artigo) → responda com o que tem e complete com a internet, separando claramente as duas origens.
- **Não tem:** nenhum resultado relevante → vá direto para a internet e avise "não encontrei no cofre".

## Passo 3 — internet (fallback)

`WebSearch` e `WebFetch` são ferramentas deferidas: carregue antes com `ToolSearch` (`select:WebSearch,WebFetch`).

- Priorize fonte oficial: planalto.gov.br (leis, CTN, LCs), stf.jus.br / stj.jus.br (jurisprudência, súmulas), sefaz.ba.gov.br e legislação estadual, gov.br/fazenda, cgibs/Receita para IBS/CBS, portais dos tribunais. Doutrina e cursinhos só como apoio.
- Confira data/vigência: hoje a legislação de Reforma Tributária (EC 132/2023, LC 214/2025, LC 227/2026) muda com frequência.
- Não copie trecho longo de site; resuma e cite a URL. Lei seca (texto de norma) pode ser citada literalmente.

## Formato da resposta

Direta e de estudo, em português, do jeito que cai na prova (banca FCC/fiscal):

1. **Resposta curta** (1–3 linhas).
2. **Explicação** com o essencial: regra, exceção, prazo/percentual/número, artigo.
3. **Como a banca cobra** (pegadinha comum), se souber pelo cofre ou pela prova.
4. **Fontes**, separadas:
   - `Cofre:` `[[nota]]` com linha (ex.: `MATERIAS/P2 - Direito Tributário.md:731`) — use link de arquivo.
   - `Internet:` URL + o que foi tirado dela. Se nada veio da internet, omita.
5. Se o cofre estiver **desatualizado ou contradizer** a fonte oficial, diga explicitamente — não corrija o cofre sozinho; ofereça guardar a dúvida em `Questoes/Duvidas.md`.

## Guardar a dúvida

Só quando o Pedro pedir ("guarda essa dúvida", "anota isso"). Nunca por conta própria. Acrescente ao final da seção certa de `Questoes/Duvidas.md` (sem reescrever o resto), uma linha por dúvida:

- **Respondida** → vai direto para `## 💭 Dúvidas respondidas` do caderno da matéria (`Erradas/ERRO <MATÉRIA>.md`), em callout (ver abaixo), não para `Duvidas.md`.
- **Sem fonte confirmada** → fim de `## Dúvida`, a caixa de entrada: heading que o atalho do Pedro usa como alvo, não renomeie.


```
- 20 de set. de 2026, 15:41 — [Direito Tributário] pergunta → resposta curta (fonte: cofre MATERIAS/P2 - Direito Tributário.md:731 / internet <url>)
```

Não use `Capturas.md`: o `/triar-inbox` distribui tudo que está lá. Dúvida sem resposta confirmada também pode ser guardada, marcada com `(sem fonte confirmada)`.

## Arrumar o layout e mover para o caderno da matéria

`## Dúvida` é a caixa de entrada do atalho: só deve ter o que ainda não foi respondido. Quando a dúvida respondida é uma entrada que já está lá (o atalho manda texto cru: enunciado colado, alternativas quebradas, nota do Pedro no fim), **depois de responder no chat, reformate a entrada e mova-a para o heading `## 💭 Dúvidas respondidas` do caderno de erros da matéria**, no fim desse heading. Só a entrada respondida, sem tocar nas outras.

Caderno da matéria: `Erradas/ERRO <MATÉRIA>.md` (ex.: `ERRO DIREITO TRIBUTÁRIO.md`, `ERRO REFORMA TRIBUTÁRIA.md`; LGPD vai em `ERRO DIREITO ADMINISTRATIVO.md`). `## 💭 Dúvidas respondidas` fica no fim da nota (depois de `# OUTRAS BANCAS`). Se o heading não existir, crie-o no fim (`---`, linha em branco, heading, linha em branco, callout). Se não houver caderno para a matéria, pergunte ao Pedro antes de criar. Assim `## Dúvida` em `Questoes/Duvidas.md` fica livre para o atalho continuar acrescentando.

Layout (callout recolhível, um por dúvida; **sem sub-headings** — o heading `## 💭 Dúvidas respondidas` é o único da seção):

```
> [!question]- 20/09 15:52 · Direito Tributário · IBAM (ISS Guarulhos) — Responsabilidade tributária
> Enunciado limpo (sem números de página soltos, quebras no meio de frase ou "Ill"/"l" no lugar de "III"/"I").
>
> I. …
> II. …
> (A) …
> (B) …
>
> **Marquei:** B · **Gabarito:** A
>
> > [!success] Resposta
> > Resposta curta em 1–3 linhas, com regra/exceção/artigo/súmula.
> >
> > **Fonte:** cofre `MATERIAS/P2 - Direito Tributário.md:759` · internet <url> · (sem fonte confirmada) se for o caso
```

Regras do reformat:
- **Título:** `dd/mm hh:mm · matéria · banca (prova) — tema em poucas palavras`. Data/hora vêm da linha original do atalho; banca/prova, do que o Pedro escreveu.
- **Preserve o conteúdo do Pedro:** corrija só OCR/quebra de linha óbvia. Não reescreva enunciado nem apague a anotação dele ("errei porque…", "fiquei na dúvida…"); ela vira a linha **Marquei/Gabarito** ou uma linha **Obs.:**.
- Dúvida sem enunciado (pergunta solta): callout só com a pergunta e a resposta.
- Mover = tirar o bloco de `## Dúvida` (do `> [!question]-` até a última linha `>` do callout, mais a linha em branco que o separava) e inserir no fim de `## 💭 Dúvidas respondidas` do caderno. Nunca deixe a entrada duplicada.
- Edite por índice de linha em Python (o vault tem NBSP; não confie em `old_string` exato) e confira depois: `grep -c '\[!question\]' Questoes/Duvidas.md` cai em 1 por dúvida movida e o do caderno sobe em 1.
- Nunca mova nem reformate entrada que ainda não foi respondida, e nunca apague dúvida.

## Regras

- Nunca afirme que "está no cofre" sem ter lido o trecho. Nunca invente artigo, número de súmula ou percentual: se não achou, diga que não achou.
- Dúvida ambígua (ex.: "ICMS" existe em Tributário e em Legislação Estadual BA): responda pela matéria mais provável e mencione a outra em uma linha, sem interrogatório.
- Pedido de *editar* nota, absorver PDF ou triar capturas não é desta skill → `/absorver-pdf`, `/triar-inbox`.
