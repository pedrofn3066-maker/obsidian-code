---
description: Lê Questoes/Inbox.md, distribui cada captura para a nota certa e limpa o Inbox
---

Trie as capturas rápidas acumuladas em `Questoes/Inbox.md` e mova cada uma para onde ela pertence.

## Passo 0 — orientar-se sem ler tudo

Notas de `MATERIAS/` variam de 100 a 1400+ linhas. Não leia o arquivo inteiro pra achar onde uma captura entra:

- **Não sei em qual matéria a captura entra** → `python3 PY/diretorio-materias.py [palavra]` lista as 28 notas com bloco/peso/prioridade.
- **Sei a matéria, não sei o heading** → `python3 PY/indice-materia.py "MATERIAS/<nota>.md"` mostra a tabela VINTEUM (peso × dom) e a árvore de headings com linha exata, sem o corpo.
- **Vou editar perto de um heading específico** → `python3 PY/achar-heading.py "MATERIAS/<nota>.md" "<trecho>"` acha a linha tolerando espaço/NBSP. **Nunca confie em casamento de string exata** (`old_string`/`new_string`) em `MATERIAS/` — o vault tem `\xa0` escondido em vários headings que parecem normais no Obsidian; já quebrou a edição 3 vezes. Ache a linha com o script, leia e escreva por índice de linha em Python.

## Antes de mover

1. Leia `Questoes/Inbox.md` inteiro. Cada item começa com `- <data>, <hora> — <texto>`, mas o texto pode ocupar várias linhas até o próximo `- <data>`.
2. Agrupe as capturas por assunto antes de mexer em arquivo. Várias linhas seguidas costumam ser da mesma questão ou do mesmo tópico e devem ir juntas, num bloco só.
3. Descarte o que for lixo de captura: linha só com o nome da matéria, teste do Atalho, fragmento sem conteúdo (ex.: uma letra solta). Não crie nota para isso.

## Decidir o destino — e quando perguntar

- **`MATERIAS/<nota>.md`** — o caso normal. Ache o heading do tópico específico com `achar-heading.py`. Se não existir e o assunto for relevante, crie um `###` com `- [ ] status [dom:: 0] [peso:: N]`, N igual ao `peso` do frontmatter da nota. Se a matéria também tiver tabela VINTEUM e o tópico corresponder a uma linha dela, o `peso` do tracker deve refletir aquele percentual, não o peso genérico da nota — como fizemos no Bloco C de Custos.
- **`Questoes/Diario/<data> <materia>.md`** — só se a captura for resultado de caderno (total, acertos, assuntos). Preencha `materia`, `bloco`, `assuntos`, `total`, `acertos`; deixe `slot`, `erro_tipo`, `tempo_min` e `tec` vazios — são campos que o Pedro preenche.
- **`Erradas/`** — questão errada com comentário, e já existe caderno de erros da matéria.

**Sobreposições conhecidas — pare e pergunte (`AskUserQuestion`) em vez de decidir sozinho:**

| Assunto | Destinos possíveis | Critério |
| --- | --- | --- |
| Orçamento público, princípios orçamentários, LDO/PPA/LOA | `Direito Financeiro`, `Finanças Públicas`, `CASP` | A própria nota de Direito Financeiro avisa: "sobreposição forte com Finanças Públicas, estudar as duas juntas". Sem pista clara do ângulo (jurídico × econômico × contábil), perguntar. |
| Inflação, juros reais/aparentes | `Macro Economia`, `Matemática Financeira` | Se vier com cálculo/fórmula → Matemática Financeira. Se for conceito/efeito econômico → Macro Economia. |
| Simples Nacional | `Direito Tributário` (regra geral, LC 123), `Legislação Tributária Estadual` (ótica estadual do ICMS) | Se a captura for sobre o regime em si → Direito Tributário. Se for sobre como o Simples afeta o ICMS estadual → LTE. |

Essa tabela não é exaustiva — se `achar-heading.py` ou `indice-materia.py` mostrar o mesmo assunto plausível em duas notas fora dessa lista, trate como sobreposição nova: pergunte, não escolha.

## Ao escrever na nota de matéria

**Invoque a skill `voz-autoral` (modo AUDITAR)** antes de colar o texto de uma captura que veio com voz de professor, de outro assistente ("Galera, aqui a banca foi direto...", "Sua observação é excelente!") ou qualquer narrativa didática longa. Ela tem o catálogo de 15 assinaturas e o critério de corte — não reinvente os critérios a cada triagem. Regra dela que vale reforçar aqui: **o lastro é intocável** — nunca acrescente fato, número, artigo de lei ou exemplo que não estava na captura; se faltar algo (ex.: fórmula cortada no meio), registre como pendência de autoria (`> [!warning]-`) em vez de completar.

Respeite o registro da nota de destino: denso, direto, `<mark>` para o núcleo da regra, ⚠️ para pegadinha de banca.

## Depois de mover

1. Apague do Inbox as linhas movidas. Deixe a seção `## Capturas` vazia se tudo saiu — não apague o cabeçalho nem o texto explicativo da nota.
2. Para cada matéria tocada, cruze os assuntos das capturas com a tabela `Percentual de cobrança (VINTEUM Fiscal 4.0)` daquela nota (via `indice-materia.py`) e diga ao Pedro **qual tópico específico** merece o próximo bloco de estudo — considerando o peso do edital e o `dom::` atual, não só o volume que ele capturou.
3. **Verifique antes de reportar como feito.** Depois de cada edição em `MATERIAS/`, rode:
   ```
   git diff -U0 -- "<nota>" | grep "^-" | grep -v "^---" | sed 's/^-//' | sort > /tmp/r.txt
   git diff -U0 -- "<nota>" | grep "^+" | grep -v "^+++" | sed 's/^+//' | sort > /tmp/a.txt
   comm -23 /tmp/r.txt /tmp/a.txt
   ```
   Isso deve mostrar só linha vazia, ou só o que você removeu de propósito (ex.: uma linha normalizada por NBSP). Qualquer outra coisa ali é conteúdo perdido — pare e investigue antes de seguir.
4. Relate em tabela: o que era a captura, para que nota e heading foi, e qual o peso VINTEUM do tópico.

Não commite sem o Pedro pedir.
