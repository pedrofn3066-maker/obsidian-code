---
name: tirar-duvida
description: Tira dúvidas sobre matérias e tópicos de estudo (Direito Tributário, Reforma Tributária, Auditoria, Contabilidade, Direito Administrativo etc.) buscando a explicação primeiro no cofre (MATERIAS, wiki, Erradas, Questoes) e, só se o cofre não cobrir, pesquisando na internet em fonte oficial. Use quando o Pedro perguntar "o que é X", "explica Y", "qual a diferença entre A e B", "como a banca cobra Z", "tira uma dúvida".
---

# Tirar dúvida (cofre primeiro, internet depois)

Paths relativos à raiz do cofre (`vault-ba/`). Responde a dúvida de estudo. **Não edita o cofre por conta própria** — só lê. As únicas escritas permitidas são: guardar a dúvida em `Questoes/Duvidas.md` quando o Pedro pedir (ver "Guardar a dúvida"), mover a entrada já respondida para o caderno de erros da matéria (ver "Arrumar o layout e mover para o caderno da matéria") e grifar, na nota de `MATERIAS/`, o dispositivo que a resposta usou (ver "Grifar o dispositivo na matéria") — só envolvendo texto que já existe, nunca acrescentando conteúdo.

## Modo padrão: esvaziar `## Dúvida`

Quando o Pedro chama `/tirar-duvida` **sem uma pergunta específica** (ou pede "responda o que está em Dúvida"), o trabalho é processar a caixa de entrada inteira, sem perguntar:

1. Ler `## Dúvida` de `Questoes/Duvidas.md` e separar as entradas (cada uma começa com `- <data>, <hh:mm> —`). Entrada que só continua a anterior (ex.: "sobre a questão anterior…") vira callout próprio, com o título indicando "continuação de …".
2. Para cada entrada: buscar no cofre (Passo 1); o que **não está no cofre** (súmula, artigo, item de norma que falta) completar na internet em fonte oficial (Passo 3). Na resposta, deixar claro o que é cofre e o que é novo.
3. Mover **todas** para `## 💭 Dúvidas respondidas` do caderno da matéria (seção "Arrumar o layout…"), inclusive as que ficarem sem fonte confirmada (marcadas `(sem fonte confirmada)` na linha **Fonte**). Linhas soltas de registro (`- … [Matéria] pergunta → resposta (fonte…)`) que repetem uma entrada entram no callout dela e saem da caixa.
4. **Ao final, `## Dúvida` fica vazio** (só o heading) e `Questoes/Duvidas.md` fica só com a introdução e a lista de links "Dúvidas respondidas, por matéria" — com link novo para cada caderno usado pela primeira vez.
5. No chat, uma tabela curta: entrada → caderno → o que era novo (não estava no cofre) → o que foi grifado em `MATERIAS/`. Não repita as respostas inteiras no chat; elas estão nos callouts.

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

Layout (callout recolhível, um por dúvida; **sem sub-headings** — o heading `## 💭 Dúvidas respondidas` é o único da seção). O callout externo guarda a questão; dentro dele, **blocos coloridos irmãos** (cada um é um callout de 2º nível, separados por uma linha `>`), na ordem abaixo. Só `[!success] Resposta` e `Fonte` são obrigatórios; os outros entram quando têm conteúdo de verdade.

```
> [!question]- 20/09 15:52 · Direito Tributário · IBAM (ISS Guarulhos) — Responsabilidade tributária
> Enunciado limpo (sem números de página soltos, quebras no meio de frase ou "Ill"/"l" no lugar de "III"/"I").
>
> I. …
> II. …
> (A) <mark style="background:#affad1">alternativa do gabarito</mark>
> (B) <mark style="background:rgba(163, 67, 31, 0.2)">alternativa que marquei</mark> — com o trecho trocado pela banca em <span class="g-cond">exceto</span>
>
> **Marquei:** 🟥 B · **Gabarito:** 🟩 A
> **Obs.:** anotação do Pedro, intacta.
>
> > [!success] ✅ Resposta — A
> > Uma frase com o <mark style="background:#fff88f">núcleo da regra</mark> e o artigo/súmula em **negrito**. Grifos semânticos nos dados que a banca troca: <span class="g-prazo">5 anos</span>, <span class="g-cond">salvo</span>, <span class="g-comp">lei complementar</span>, <span class="g-num">2/3</span>.
> >
> > Explicação curta (2–5 linhas), por que as outras erram, uma por linha: **(B)** troca X por Y.
>
> > [!example]- 🧩 Quadro
> > | | Regra | Exceção |
> > | --- | --- | --- |
> > | … | … | … |
>
> > [!warning] ⚠️ Pegadinha da banca
> > O que a banca trocou nesta questão e como ela costuma trocar.
>
> > [!tip] 💡 Macete
> > Gancho de memória em uma linha.
>
> > [!quote]- 📜 Texto literal — art. X, CTN
> > Lei seca do dispositivo, com os grifos semânticos.
>
> > [!info] 🔗 Na matéria
> > [[P2 - Direito Tributário#Heading exato|Heading]] — grifado agora / já estava grifado / não está no cofre (entrou pela internet).
> > **Fonte:** cofre `MATERIAS/P2 - Direito Tributário.md:759` · internet <url> · (sem fonte confirmada) se for o caso
```

Cores (mesmas do cofre, não invente outras):

| Uso | Marcação |
| --- | --- |
| alternativa do gabarito | `<mark style="background:#affad1">` (verde) e 🟩 |
| alternativa que o Pedro marcou errado | `<mark style="background:rgba(163, 67, 31, 0.2)">` (vermelho) e 🟥 |
| núcleo da regra, uma vez por resposta | `<mark style="background:#fff88f">` (amarelo, o mais usado nas notas) |
| prazo · condição/ressalva · competência · número | `<span class="g-prazo">` · `g-cond` · `g-comp` · `g-num` (`.obsidian/snippets/grifos.css`; regras de uso em `.claude/commands/triar-inbox-plus.md`, "Grifos semânticos") |

### Validar a sintaxe antes de encerrar

Cada `[!tipo]` acima é `[!tipo]` (fixo) ou `[!tipo]-` (recolhível, com o `-` colado no `]`, sem nada depois dele além do espaço e do título). Escrever esses marcadores à mão ou por concatenação de string em Python é onde nasce erro de colchete (ex.: `[!example]-]`, `[!quote]-]`) — o Obsidian não reconhece isso como callout e mostra o marcador cru na tela. Depois de gravar o(s) caderno(s), sempre rode:

```bash
grep -n '\[!.*\]-\]' "Erradas/ERRO <MATÉRIA>.md"
```

Tem que sair vazio. Se aparecer algo, é o bug do colchete: conserte para `[!tipo]-` e rode de novo. Vale também para qualquer callout novo que a resposta usar além dos listados aqui.

Quando usar cada bloco:
- **🧩 Quadro** (`[!example]-`, recolhido): tema complexo ou comparação — dois institutos parecidos (zona urbana × expansão urbana), vários incisos que a banca embaralha, momentos de uma operação, súmulas com sinal trocado. Tabela de 2 a 4 colunas; cada linha responde uma alternativa ou um caso. Pergunta simples não leva quadro.
- **⚠️ Pegadinha**: só se der para dizer o que foi trocado (verbo invertido, definição trocada entre pares, "exclusivamente", colagem de dois itens).
- **💡 Macete**: só se for um gancho real e curto (sigla, rima, "exportação Exonera, importação Incide").
- **📜 Texto literal** (recolhido): quando a banca cobra literalidade. Norma pode ir literal; site e doutrina, não.
- **🔗 Na matéria**: sempre que houver heading correspondente em `MATERIAS/`; wikilink para o heading exato (confira com `PY/achar-heading.py`).

Grifos: expressão mínima, nunca atravessando linha, nunca grifo dentro de grifo (dentro de `<mark>` pode). Se metade da resposta ficou colorida, corte: o grifo é para o olho achar o que decide a questão. O texto do Pedro (enunciado, Obs.) só recebe `<mark>`/`<span>` em volta do que já está escrito, sem trocar palavra.

### Grifar o dispositivo na matéria

Se a resposta se apoiou num **dispositivo importante que já está na nota de `MATERIAS/`** (artigo, súmula, item de norma na forma literal) e a banca cobrou justamente o dado que ela troca, grife esse trecho na própria nota:

- Só o trecho usado na resposta (a linha citada na **Fonte**), só texto literal/lastro — nunca lupa, ponte, heading, tracker, frontmatter, wikilink ou bloco de código.
- Mesmas classes `g-prazo`/`g-cond`/`g-comp`/`g-num`, mais `<mark style="background:#fff88f">` no núcleo que a questão testou. Linha que já tem grifo nesse trecho fica como está.
- Envolver sem reescrever: o texto sem os spans tem de ser o mesmo de antes. Valide:
  ```bash
  python3 PY/grifos.py "MATERIAS/<nota>.md"
  git show HEAD:"MATERIAS/<nota>.md" | python3 PY/grifos.py --limpo - > "$TMPDIR/antes.md"
  python3 PY/grifos.py --limpo "MATERIAS/<nota>.md" > "$TMPDIR/depois.md"
  diff "$TMPDIR/antes.md" "$TMPDIR/depois.md" | grep -v '<mark' | head   # só pode mudar <mark>
  ```
- Registre no bloco **🔗 Na matéria** ("grifado agora: art. 79, I, b") e liste no resumo do chat.
- Dispositivo que **não está** na nota: não acrescente (isso é `/triar-inbox`); diga "não está no cofre" no bloco 🔗 e no chat.

Regras do reformat:
- **Título:** `dd/mm hh:mm · matéria · banca (prova) — tema em poucas palavras`. Data/hora vêm da linha original do atalho; banca/prova, do que o Pedro escreveu.
- **Preserve o conteúdo do Pedro:** corrija só OCR/quebra de linha óbvia. Não reescreva enunciado nem apague a anotação dele ("errei porque…", "fiquei na dúvida…"); ela vira a linha **Marquei/Gabarito** ou uma linha **Obs.:**.
- Dúvida sem enunciado (pergunta solta): callout só com a pergunta e a resposta.
- Mover = tirar o bloco de `## Dúvida` (do `> [!question]-` até a última linha `>` do callout, mais a linha em branco que o separava) e inserir no fim de `## 💭 Dúvidas respondidas` do caderno. Nunca deixe a entrada duplicada.
- Depois de mover, confira o topo de `Questoes/Duvidas.md` (lista "Dúvidas respondidas, por matéria"): se o caderno usado ainda não tem link lá, acrescente uma linha `- [[ERRO <MATÉRIA>#💭 Dúvidas respondidas|<Matéria>]]`, sem tocar nas outras.
- Edite por índice de linha em Python (o vault tem NBSP; não confie em `old_string` exato) e confira depois: `grep -c '\[!question\]' Questoes/Duvidas.md` cai em 1 por dúvida movida e o do caderno sobe em 1.
- Nunca apague dúvida: toda entrada sai de `## Dúvida` **para dentro de um callout** do caderno. No modo padrão (esvaziar a caixa), a que não tiver resposta confirmada também é movida, com `(sem fonte confirmada)` na linha **Fonte** — `## Dúvida` não deve ficar com sobra.
- Texto colado pelo Pedro (resposta do professor, ementa) fica no callout, em `> **Resposta do professor (colada):**` antes do `[!success]`; a resposta da skill resume e aponta o artigo/item, sem copiar de novo.
- Caderno sem `## 💭 Dúvidas respondidas`: crie o heading no fim da nota e acrescente o link em `Questoes/Duvidas.md` sem perguntar (só pergunte se não existir o arquivo `Erradas/ERRO <MATÉRIA>.md`).

## Regras

- Nunca afirme que "está no cofre" sem ter lido o trecho. Nunca invente artigo, número de súmula ou percentual: se não achou, diga que não achou.
- Dúvida ambígua (ex.: "ICMS" existe em Tributário e em Legislação Estadual BA): responda pela matéria mais provável e mencione a outra em uma linha, sem interrogatório.
- Pedido de *editar* nota, absorver PDF ou triar capturas não é desta skill → `/absorver-pdf`, `/triar-inbox`.
- **Nunca encerre a tarefa sem rodar** `grep -n '\[!.*\]-\]' "Erradas/ERRO <MATÉRIA>.md"` em todo caderno tocado (ver "Validar a sintaxe antes de encerrar"). É a mesma classe de erro que já vazou uma vez (colchete sobrando no `[!example]-]`) — checar sempre, não só quando desconfiar.
