---
description: Versão plus do triar-inbox para capturas de texto maiores (lei seca extensa) — distribui, limpa e aplica grifos semânticos (prazos/condições/competências/números)
---

Use este comando (e não o `/triar-inbox` normal) quando a captura for um texto maior — trechos longos de lei seca, artigos com muitos incisos/parágrafos — onde vale a pena marcar semanticamente o que a banca costuma trocar. Pra capturas curtas, use `/triar-inbox`.

Trie as capturas rápidas acumuladas em `Questoes/Capturas.md` e mova cada uma para onde ela pertence.

## Passo 0 — orientar-se sem ler tudo

Notas de `MATERIAS/` variam de 100 a 1400+ linhas. Não leia o arquivo inteiro pra achar onde uma captura entra:

- **Não sei em qual matéria a captura entra** → `python3 PY/diretorio-materias.py [palavra]` lista as 28 notas com bloco/peso/prioridade.
- **Sei a matéria, não sei o heading** → `python3 PY/indice-materia.py "MATERIAS/<nota>.md"` mostra a tabela VINTEUM (peso × dom) e a árvore de headings com linha exata, sem o corpo.
- **Vou editar perto de um heading específico** → `python3 PY/achar-heading.py "MATERIAS/<nota>.md" "<trecho>"` acha a linha tolerando espaço/NBSP. **Nunca confie em casamento de string exata** (`old_string`/`new_string`) em `MATERIAS/` — o vault tem `\xa0` escondido em vários headings que parecem normais no Obsidian; já quebrou a edição 3 vezes. Ache a linha com o script, leia e escreva por índice de linha em Python.

## Antes de mover

1. Leia `Questoes/Capturas.md` inteiro. Cada item começa com `- <data>, <hora> — <texto>`, mas o texto pode ocupar várias linhas até o próximo `- <data>`.
2. Agrupe as capturas por assunto antes de mexer em arquivo. Várias linhas seguidas costumam ser da mesma questão ou do mesmo tópico e devem ir juntas, num bloco só.
3. Descarte o que for lixo de captura: linha só com o nome da matéria, teste do Atalho, fragmento sem conteúdo (ex.: uma letra solta). Não crie nota para isso.

## Decidir o destino — e quando perguntar

- **`MATERIAS/<nota>.md`** — o caso normal. Ache o heading do tópico específico com `achar-heading.py`. Se não existir e o assunto for relevante, crie um heading com `- [ ] status [dom:: 0] [peso:: N]`, **N sempre igual ao `peso` do frontmatter da nota** — nunca o percentual da tabela VINTEUM. É o padrão usado em todo o vault (ex.: Bloco C de Custos, conferido em `97b7bb5`); o percentual VINTEUM só vive no `[peso::]` das linhas do `Checklist por importância`, nunca no tracker de um heading do corpo.
  - **Se o tópico exige mais de um heading pra fazer sentido** (ex.: um assunto com duas frentes bem distintas), prefira dois headings-irmãos no mesmo nível a um heading "guarda-chuva" vazio na frente deles — um heading que só existe pra agrupar, sem tracker próprio, é container legítimo (ver regra dos 38/57 em `9e2c629`). Só crie um heading-pai com conteúdo direto se você for escrever algo ali; caso contrário, o conteúdo real deve morar em headings **mais profundos** que o pai (nunca mais rasos — um `##` depois de um `###` não é filho, é seção nova desvinculada).
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

## Grifos semânticos (análise obrigatória antes de salvar)

Com o texto já no registro da nota (depois do `voz-autoral`), releia o trecho que vai entrar e marque quatro tipos de dado com `<span class="g-…">`. É o que a banca troca na alternativa errada. As cores vêm de `.obsidian/snippets/grifos.css`: fundo pastel + traço próprio por categoria, diferente do `<mark>` manual. O Pedro esconde cada categoria em *Style Settings → Grifos da triagem*.

| Classe | Categoria | Traço | O que grifar | Exemplo (LC 227/26, art. 16) |
| --- | --- | --- | --- | --- |
| `g-prazo` | prazos | contínuo | a duração ou o termo, com a unidade | `<span class="g-prazo">2 (dois) anos</span>`, `<span class="g-prazo">12 (doze) meses</span>` |
| `g-cond` | condições/ressalvas | tracejado | só a palavra-gatilho que proíbe, excepciona, restringe ou condiciona (vedado, ressalvado, somente, salvo, exceto, desde que) | `<span class="g-cond">É vedada</span>`, `<span class="g-cond">ressalvada</span>`, `<span class="g-cond">somente</span>` |
| `g-comp` | competências | pontilhado | ente, órgão ou colegiado, toda vez que aparece | `<span class="g-comp">Conselho Superior do CGIBS</span>`, `<span class="g-comp">Distrito Federal</span>` |
| `g-num` | números | duplo | valor que a banca pode trocar: alíquota, percentual, limite, valor, fração, quórum | `<span class="g-num">maioria absoluta</span>`, `<span class="g-num">18%</span>` |

- **Um trecho, uma categoria; nunca grifo dentro de grifo.** Número que mede tempo é `g-prazo` ("2 (dois) anos"), não `g-num`.
- **Grife a expressão mínima**: `ressalvada`, não "ressalvada a hipótese de a eleição anterior…". O olho bate no gatilho e lê o resto da frase.
- **Não é número:** numeração de artigo, inciso, parágrafo ou lei (`art. 9º`, `incisos I e II do § 2º`, `Lei 7.014/96`).
- **Não é competência:** remissão a norma (`desta Lei Complementar`) nem cargo interno do órgão (`o Presidente e os Vice-Presidentes`). Espécie normativa só entra quando é reserva: `mediante <span class="g-comp">lei complementar</span>`.
- **Nunca atravesse linha** (o `grifos.py` recusa) e nunca grife heading, tracker `- [ ] status`, frontmatter, wikilink `[[…]]` ou bloco de código.
- **Dentro de `<mark>` e de negrito pode**: o span vai por dentro, `**<span class="g-num">18%</span>**`. Dentro do `<mark>` o grifo perde o fundo e fica só com o sublinhado.
- **Grifo não mexe no lastro**: só envolve texto que já está lá, sem reescrever nem acrescentar.
- **Escopo: só o texto que esta triagem está colando.** Não grife conteúdo antigo da nota. Isso altera linhas existentes, e a checagem do `comm` abaixo vai acusar.
- Se metade do parágrafo ficou colorida, o grifo parou de apontar. Corte até sobrar o que distingue a alternativa certa da errada.

## Depois de mover

1. Apague de `Capturas.md` as linhas movidas. Deixe a seção `## Capturas` vazia se tudo saiu — não apague o cabeçalho nem o texto explicativo da nota.
2. Para cada matéria tocada, cruze os assuntos das capturas com a tabela `Percentual de cobrança (VINTEUM Fiscal 4.0)` daquela nota (via `indice-materia.py`) e diga ao Pedro **qual tópico específico** merece o próximo bloco de estudo — considerando o peso do edital e o `dom::` atual, não só o volume que ele capturou.
3. **Verifique antes de reportar como feito.** Depois de cada edição em `MATERIAS/`, rode:
   ```
   git diff -U0 -- "<nota>" | grep "^-" | grep -v "^---" | sed 's/^-//' | sort > /tmp/r.txt
   git diff -U0 -- "<nota>" | grep "^+" | grep -v "^+++" | sed 's/^+//' | sort > /tmp/a.txt
   comm -23 /tmp/r.txt /tmp/a.txt
   ```
   Isso deve mostrar só linha vazia, ou só o que você removeu de propósito (ex.: uma linha normalizada por NBSP). Qualquer outra coisa ali é conteúdo perdido — pare e investigue antes de seguir.
4. **Valide os grifos** de cada nota tocada:
   ```
   python3 PY/grifos.py "MATERIAS/<nota>.md"
   ```
   Tem que sair sem nenhuma linha `!` (código 0). Os `!` apontam classe errada (`g-prazos`), span não fechado na mesma linha, grifo dentro de grifo ou grifo vazio. Pra reler o texto que entrou sem os spans e conferir que é palavra por palavra o da captura:
   ```
   git show HEAD:"MATERIAS/<nota>.md" | python3 PY/grifos.py --limpo - > "$TMPDIR/antes.md"
   python3 PY/grifos.py --limpo "MATERIAS/<nota>.md" > "$TMPDIR/depois.md"
   diff "$TMPDIR/antes.md" "$TMPDIR/depois.md"
   ```
   O `diff` só pode ter linhas `>` (o que entrou). Linha `<` é texto antigo alterado.
5. Relate em tabela: o que era a captura, para que nota e heading foi, qual o peso VINTEUM do tópico e a contagem de grifos por categoria que o `grifos.py` mostrou.

Não commite sem o Pedro pedir.
