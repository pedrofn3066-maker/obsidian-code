---
description: Versão plus do triar-inbox para capturas de texto maiores (lei seca extensa) — distribui complementando o que a nota já tem, com pontes, texto literal e lupa nos tópicos difíceis, limpa e aplica grifos semânticos (prazos/condições/competências/números)
---

Use este comando (e não o `/triar-inbox` normal) quando a captura for um texto maior — trechos longos de lei seca, artigos com muitos incisos/parágrafos — onde vale a pena marcar semanticamente o que a banca costuma trocar. Pra capturas curtas, use `/triar-inbox`.

Trie as capturas rápidas acumuladas em `Questoes/Capturas.md` e mova cada uma para onde ela pertence.

## Passo 0 — orientar-se sem ler tudo

Notas de `MATERIAS/` variam de 100 a 1400+ linhas. Não leia o arquivo inteiro pra achar onde uma captura entra:

- **Não sei em qual matéria a captura entra** → `python3 PY/diretorio-materias.py [palavra]` lista as 28 notas com bloco/peso/prioridade.
- **Sei a matéria, não sei o heading** → `python3 PY/indice-materia.py "MATERIAS/<nota>.md"` mostra a tabela VINTEUM (peso × dom) e a árvore de headings com linha exata, sem o corpo.
- **Vou editar perto de um heading específico** → `python3 PY/achar-heading.py "MATERIAS/<nota>.md" "<trecho>"` acha a linha tolerando espaço/NBSP. **Nunca confie em casamento de string exata** (`old_string`/`new_string`) em `MATERIAS/` — o vault tem `\xa0` escondido em vários headings que parecem normais no Obsidian; já quebrou a edição 3 vezes. Ache a linha com o script, leia e escreva por índice de linha em Python.
- **Quero saber onde o Pedro erra hoje** → `python3 PY/plano-dia.py --diag "<matéria>"`. Guarde os tópicos com `ERRO`, `dom` baixo ou "nunca testado em caderno": são o mapa de onde uma **lupa** (abaixo) faz falta e o que serve de **ponte**.

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

## Cruzar com o que o cofre já tem

A triagem não é só mover: a captura tem de entrar **somando** ao que a nota já sabe. Três tipos de conteúdo, cada um com sua regra de origem — o tipo decide o que pode ser escrito:

- **Lastro** — o que a captura diz. Só fato, número, artigo ou exemplo que está na captura. Intocável.
- **Ponte** — ligação com o que o cofre já sabe: outro heading (`[[Nota#Heading]]`), jurisprudência já registrada na nota, erro de caderno do tópico. Só liga o que existe; a ponte nunca traz fato novo.
- **Lupa** — explicação didática de um tópico difícil, escrita por você, em callout recolhido. Explica o lastro; não acrescenta regra. Todo número ou exemplo que não vier da captura é rotulado `exemplo ilustrativo (sem lastro)`.

Para cada grupo de capturas, depois de achar o heading de destino, faça três coisas:

1. **Leia o que o heading já tem** (só aquele trecho, pela linha do `achar-heading.py`) e classifique:
   - **novo** — a nota não trata disso: escreva o lastro;
   - **complementa** — a nota trata, mas falta um dispositivo, uma pegadinha, um prazo ou um detalhe: **integre no ponto do texto a que o insight pertence** (junto do parágrafo ou item relacionado, não largado no fim) e escreva só o que falta;
   - **já existe** — não duplique: não escreva nada, e no relatório diga em que linha já estava. Se a captura **contradiz** o que a nota diz, pare e pergunte (`AskUserQuestion`); não sobrescreva nenhum dos dois.
2. **Ponte.** Procure o que o cofre tem em volta: `python3 PY/diretorio-materias.py` e `grep` por dispositivo, termo ou súmula nas notas vizinhas. Registre só ligações que você achou (heading real, com linha): mesmo instituto em outra matéria (norma pública × CPC privado), jurisprudência já na nota que testa a regra, tópico irmão com a regra oposta, erro de caderno do `--diag`.
3. **Texto literal e lupa.**
   - **Literal:** o dispositivo entra em bloco `>` quando a banca cobra a literalidade (prazo, rol taxativo, condição, percentual, quórum, competência). Copie da captura sem alterar. Trecho cortado → `> [!warning]-`.
   - **Lupa:** só se o tópico for **difícil**, isto é, bater em pelo menos um: (a) `ERRO` recente no `--diag`; (b) peso VINTEUM ≥ 5% com `dom` ≤ 1; (c) quadro em que a banca troca termos entre categorias; (d) mecânica com passos (cálculo, lançamento, contagem de prazo, ordem de preferência). Fora disso, não escreva lupa: nota carregada de callouts perde o núcleo. Capturas curtas (uma frase, um número) quase nunca pedem lupa.

## Ao escrever na nota de matéria

**Invoque a skill `voz-autoral` (modo AUDITAR)** antes de colar o texto de uma captura que veio com voz de professor, de outro assistente ("Galera, aqui a banca foi direto...", "Sua observação é excelente!") ou qualquer narrativa didática longa. Ela tem o catálogo de 15 assinaturas e o critério de corte — não reinvente os critérios a cada triagem. Regra dela que vale reforçar aqui: **o lastro é intocável** — nunca acrescente fato, número, artigo de lei ou exemplo que não estava na captura; se faltar algo (ex.: fórmula cortada no meio), registre como pendência de autoria (`> [!warning]-`) em vez de completar.

Respeite o registro da nota de destino: denso, direto, `<mark>` para o núcleo da regra, ⚠️ para pegadinha de banca.

Cada grupo entra na nota nesta ordem, e só com os recursos que a etapa anterior marcou:

1. **Lastro:** registro denso e direto; origem pela data da captura `(captura 19/09)`.
2. **Texto literal:** bloco `>` com o dispositivo, quando previsto.
3. **Lupa:** callout recolhido `> [!tip]- Lupa: <tema>` com três partes, nesta ordem: **a ideia em uma frase** (o que a regra protege ou resolve) → **o passo a passo** com um exemplo (da captura; se for seu, `exemplo ilustrativo (sem lastro)`) → **o erro clássico** (como a banca troca o termo ou inverte a regra). Linguagem de quem explica a um colega: direta, sem "Galera, atenção...".
4. **Ponte:** uma linha `> [!info]- Ponte` com os `[[links]]` e o que cada um acrescenta ("mesma regra no CPC 27 privado", "a Súm. X da nota testa isto", "errou em 17/09"). Confira cada link com `achar-heading.py` antes de gravar.

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
- **Grifo só no lastro e no texto literal.** Lupa e ponte são suas, não têm o que a banca troque: sem span.
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
5. **Auditoria de lastro e pontes.** Releia o que você escreveu: todo fato fora de lupa e ponte tem de estar na captura; o que falhar sai ou vira `> [!warning]-`. Todo `[[link]]` de ponte tem de resolver (`achar-heading.py`).
6. Relate em tabela: o que era a captura, nota e heading, peso VINTEUM · `dom`, **ação (novo / complementa / já existe)**, **recurso (texto literal / lupa / —)**, **ponte** (heading real) e a contagem de grifos por categoria que o `grifos.py` mostrou. As lupas ficam em coluna própria para o Pedro poder vetar.
7. **Plano do dia atualizado.** Rode `python3 PY/plano-dia.py --texto` e mostre ao Pedro só os slots de hoje, apontando os tópicos que esta triagem mudou de seção (ex.: saiu de Ler e foi para Fazer questões). Se a matéria tocada não está na grade de hoje, rode `python3 PY/plano-dia.py --diag "<matéria>"` e diga em uma linha em que seção os tópicos triados caíram. Critérios em `Questoes/Paineis/Plano do dia.md`.

Não commite sem o Pedro pedir.
