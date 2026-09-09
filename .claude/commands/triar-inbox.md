---
description: Lê Questoes/Inbox.md, distribui cada captura para a nota certa e limpa o Inbox
---

Trie as capturas rápidas acumuladas em `Questoes/Inbox.md` e mova cada uma para onde ela pertence.

## Antes de mover

1. Leia `Questoes/Inbox.md` inteiro. Cada item começa com `- <data>, <hora> — <texto>`, mas o texto pode ocupar várias linhas até o próximo `- <data>`.
2. Agrupe as capturas por assunto antes de mexer em arquivo. Várias linhas seguidas costumam ser da mesma questão ou do mesmo tópico e devem ir juntas, num bloco só.
3. Descarte o que for lixo de captura: linha só com o nome da matéria, teste do Atalho, fragmento sem conteúdo. Não crie nota para isso.

## Destinos

- **`MATERIAS/<nota>.md`** — o caso normal. Ache o heading do tópico específico e escreva logo abaixo dele. Se o assunto não tiver heading próprio e for relevante, crie um `###` e dê a ele a linha `- [ ] status [dom:: 0] [peso:: N]`, com N igual ao `peso` do frontmatter da nota.
- **`Questoes/Diario/<data> <materia>.md`** — só se a captura for resultado de caderno (total, acertos, assuntos). Preencha `materia`, `bloco`, `assuntos`, `total`, `acertos`; deixe `slot`, `erro_tipo`, `tempo_min` e `tec` vazios, que são campos do Pedro.
- **`Erradas/`** — se for questão errada com comentário, e já existir caderno de erros da matéria.

## Ao escrever na nota de matéria

Condense. Captura costuma vir com voz de professor ou colada de outro assistente ("Galera, aqui a banca foi direto em...", "Sua observação é excelente!"). Corte a bajulação, o metacomentário e a repetição; preserve **todo** o lastro — regra, artigo de lei, número, exemplo, nome de autor, pegadinha de banca. Nunca acrescente fato que não estava na captura.

Respeite o registro da nota de destino: denso, direto, `<mark>` para o núcleo da regra, ⚠️ para pegadinha de banca.

## Depois de mover

1. Apague do Inbox as linhas movidas. Deixe a seção `## Capturas` vazia se tudo saiu — não apague o cabeçalho nem o texto explicativo da nota.
2. Para cada matéria tocada, cruze os assuntos das capturas com a tabela `Percentual de cobrança (VINTEUM Fiscal 4.0)` daquela nota e diga ao Pedro **qual tópico específico** merece o próximo bloco de estudo — considerando o peso do edital e o `dom::` atual, não só o volume que ele capturou.
3. Relate em tabela: o que era a captura, para que nota e heading foi, e qual o peso VINTEUM do tópico.

Não commite sem o Pedro pedir.
