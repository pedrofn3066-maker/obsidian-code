---
description: Absorve uma prova antiga (PDF + gabarito): separa as questões, liga cada uma ao heading e ao trecho exato da nota que a resolve, marca o heading com [prova:: N], aponta o trecho no texto (grifo + callout "Prova anterior"), escreve lupa de prova nos tópicos que a banca cobra com armadilha e diz, em cada questão errada do caderno de erros, se ela condiz com o que outras provas já cobraram
argument-hint: <prova.pdf> [gabarito.pdf] | --erradas [matéria] | --recorrencia
---

Absorva a prova `$ARGUMENTS`: extraia as questões, cruze cada uma com o que o cofre **já** ensina e **proponha** onde marcar. **Não escreva em `MATERIAS/`, `LTM ISS SANTOS/` nem `Erradas/` antes do Pedro aprovar a tabela do Passo 4.**

Este comando **não cria conteúdo jurídico**: a nota é a fonte da regra, a prova só diz *onde a banca bateu*. Questão que a nota não trata vira **lacuna** no relatório (e sugestão de `/absorver-pdf` ou `/triar-inbox`), nunca texto novo na nota.

Três modos, pelo argumento:

- `<prova.pdf> [gabarito.pdf]` — fluxo completo (Passos 1 a 6).
- `--erradas [matéria]` — sem prova nova: só refaz o cruzamento (Passo 5) das questões erradas contra os registros já absorvidos. Use depois de importar cadernos novos do TEC.
- `--recorrencia` — só relatório: `python3 PY/provas-recorrencia.py` e cruzamento com `dom::` e erros (Passo 6, itens 5 e 6).

Tudo o que este comando escreve é de um de quatro tipos. O tipo decide o que pode ser escrito:

- **Lastro de prova** — o que a prova diz: número da questão, página, gabarito, enunciado e alternativa literais. Só o que está no PDF; intocável.
- **Ponte** — ligação com o que o cofre já sabe (`[[Nota#Heading]]`, súmula da nota, erro de caderno). Só liga o que existe; não traz fato novo.
- **Lupa de prova** — explicação sua de *como a banca cobrou* aquele tópico, em callout recolhido. Interpretação: **rotule** (`padrão de 1 prova, não confirmado`). Nenhuma regra jurídica na lupa que não esteja na nota.
- **Marca** — o que aponta o trecho: `[prova:: N]` no tracker, grifo teal na frase e callout `Prova anterior`. Só marca; não altera palavra da nota.

## Passo 1 — extrair as questões

```
python3 PY/prova-questoes.py "<prova.pdf>" [--gabarito "<gabarito.pdf>"] [--tipo N]
```

Grava em `.vault-meta/provas/<nome>.md` (ignorado pelo git): um bloco `### Q07 · <disciplina> · p.N · gab: X` por questão, com enunciado e alternativas. Provas ficam em `LTM ISS SANTOS/PROVAS/PDF/` ou `inbox/`. Leia o diagnóstico antes de qualquer coisa:

- `SEM gabarito confiável` → o caderno não traz. Procure o edital de gabaritos da banca (PDF separado) e passe com `--gabarito`. Sem gabarito você mapeia o **tópico**, mas não diz o que a banca considerou correto: nada de lupa, e a coluna Gab fica `?`.
- `gabarito tem tipos [1, 2, 3]` → caderno embaralhado, um gabarito por tipo. O tipo vem da capa (`TIPO:3`); se o script parar, pergunte ao Pedro qual caderno ele tem. **Tipo errado inverte certo e errado**, e nada mais avisa.
- `questões fora de ordem no texto` → duas colunas embaralhadas. Refaça a extração por coluna com `pymupdf` no scratchpad (blocos por coluna, depois por `y`) ou leia o PDF direto (`Read` com `pages`).
- `nenhum marcador 'Questão N'` / `N pág(s) com pouco texto` → escaneada ou manuscrita (as provas "resolvidas" costumam ser). Leia as páginas com `Read`+`pages` e monte a lista à mão. **Gabarito manuscrito ou de terceiro é não oficial**: vai no frontmatter do registro e em todo callout (`gab. não oficial`).
- `sem 4+ alternativas separadas` → certo/errado, asserção-razão ou `**D)**` colado ao enunciado seguinte. Confira essas questões no PDF antes de classificar; não classifique de memória.
- Questão **anulada** ou com gabarito alterado por recurso → registre como `ANULADA`, sem marca na nota.
- Metadados que o PDF não dá (banca, ano, órgão, cargo) e prova de "banca não confirmada": pergunte com `AskUserQuestion`, uma vez. Banca desconhecida entra como tal; não chute.

## Passo 2 — orientar-se nas notas sem ler tudo

Mesma regra do `/absorver-pdf` (notas têm até 1400+ linhas; nunca leia inteira):

- Qual nota? `python3 PY/diretorio-materias.py [palavra]`. Legislação **específica de Santos** vive em `LTM ISS SANTOS/` (fora do git, ver a memória `iss-santos-prep`); legislação **específica da Bahia** só em `MATERIAS/`. Matéria comum (Constitucional, Administrativo, Auditoria, Contabilidade…) fica em `MATERIAS/`. Na dúvida sobre onde uma questão cai, pergunte.
- Headings e `dom::`: `python3 PY/indice-materia.py "MATERIAS/<nota>.md"`.
- Linha exata de um heading (tolera NBSP): `python3 PY/achar-heading.py "MATERIAS/<nota>.md" "<trecho>"`. O aviso `SEM tracker` dessa saída pode ser falso (o tracker pode estar no bloco, não colado ao heading): confira com `sed -n`.
- O trecho da regra: `grep -niE "termo.{1,2}outro" "<nota>"` (`.{1,2}` no lugar de espaço, por causa do NBSP) e depois `Read` com `offset`/`limit` de ~40 linhas.
- Onde o Pedro erra: `python3 PY/plano-dia.py --diag "<matéria>"` — tópicos com `ERRO`, `dom` baixo ou "nunca testado" pedem **lupa de prova**.
- Já existe algo sobre essa questão na nota? `grep -n "Pegadinha de prova"` e `grep -n "Prova anterior"` na nota. Se a nota já registra a pegadinha (`⚠️ Pegadinha de prova (captura…, Q…)`), a marca aponta para ela em vez de repetir o fato.

**Nunca use `old_string` exato em `MATERIAS/` ou `LTM ISS SANTOS/`** (NBSP escondido). Escreva por índice de linha, em Python.

## Passo 3 — classificar cada questão

Para cada questão do `.vault-meta/provas/<nome>.md` (leia em blocos de ~10):

1. **Regra cobrada** em uma linha: o dispositivo/conceito que decide a resposta (não o enunciado).
2. **Nota → heading → trecho.** O heading que trata da regra e a **frase da nota** que a resolve (linha exata). Só vale se você leu esse trecho.
3. **Cobertura**, lendo a nota, não presumindo:
   - **coberto** — a nota tem a regra e o gabarito é coerente com ela;
   - **parcial** — a nota tem o tópico, mas falta o dispositivo, o rol ou a pegadinha que a questão usa;
   - **lacuna** — a nota não trata; não marque nada, vai pro relatório;
   - **conflito** — o gabarito contradiz a nota. **Não corrija a nota.** Vai como `> [!warning]- Gabarito × nota` e pergunta ao Pedro (a nota pode estar errada, o gabarito pode ser de terceiro ou ter sido alterado).
4. **Ângulo** da cobrança, em uma palavra: `literalidade`, `troca de termo`, `exceção`, `rol/lista fechada`, `prazo/número`, `cálculo`, `competência`, `jurisprudência`, `conceito`.
5. **Recorrência.** `python3 PY/provas-recorrencia.py --heading "<Nota>#<Heading>"` (vazio se for a primeira prova absorvida). Some esta prova ao que já existe.
6. **Recurso.** Só a **marca** já basta. Escreva **lupa de prova** só se bater em pelo menos um: (a) o heading foi cobrado em ≥ 2 provas; (b) a questão tem distrator sutil (troca de termo, prazo, rol) que você consegue apontar na alternativa literal; (c) `ERRO` recente do Pedro nesse tópico; (d) `dom` ≤ 1 com peso alto. Fora disso, uma nota carregada de callouts perde o núcleo.

Questões de disciplina sem nota no cofre (ex.: Inglês) → lacuna de matéria inteira, uma linha no relatório.

## Passo 4 — o plano (o que o Pedro vê e aprova)

Uma tabela, uma linha por questão, sem texto colado:

| Q | Disc. | Gab | Regra cobrada | Nota → heading (linha) | Trecho usado (início) | Cobertura | Recorrência (nº provas) | Recurso (marca / +lupa) | Erradas afetadas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Depois da tabela:

1. **Lacunas** (nota não trata) com sugestão de onde entrar, e **conflitos** gabarito × nota.
2. **Anuladas / sem gabarito / gabarito não oficial**, e o que isso muda na marca.
3. **Erradas afetadas** (prévia do Passo 5): quais callouts de `Erradas/` ganham a linha `Prova anterior`, com o veredito provisório.
4. **Sobreposições** entre notas (mesma regra em duas notas): pergunte com `AskUserQuestion` em vez de escolher.
5. **Onde estudar primeiro**: heading cobrado em mais provas × `dom::` baixo × erro do Pedro.

Pare aqui e peça aprovação. Está concluído quando a tabela tem as dez colunas preenchidas em todas as linhas e a pergunta de aprovação foi feita.

## Passo 5 — escrever (só após aprovação)

**Antes de editar qualquer nota** (`MATERIAS/`, `Erradas/` ou `LTM ISS SANTOS/`), copie-a: `cp "<nota>" "$TMPDIR/provas/<nome>.antes.md"`. É a base da conferência do Passo 6. O `git show HEAD:` só serve se a nota não tinha mudança não commitada, e no cofre do Pedro quase sempre tem; `LTM ISS SANTOS/` nem versionada é.

Escreva por script Python que **localiza heading e trecho por texto** (não por nº de linha: cada inserção desloca as seguintes), recusa âncora que não ache exatamente uma vez e roda primeiro em modo simulação, imprimindo o heading, a linha e se há tracker.

### 5a. Registro da prova — `Questoes/Provas/<Banca> <Ano> - <Local> - <Cargo>.md`

Frontmatter: `tipo: prova-antiga`, `banca`, `ano`, `orgao`, `cargo`, `questoes`, `gabarito: oficial (tipo N) | não oficial | ausente`, `fonte` (caminho do PDF), `absorvida` (data). Depois, **uma tabela** com exatamente estas colunas (o `PY/provas-recorrencia.py` lê por posição):

| Q | Disciplina | Gab | Nota → heading | Regra cobrada | Ângulo | Cobertura |
| --- | --- | --- | --- | --- | --- | --- |

`Nota → heading` é `[[Nota#Heading]]` (confira com `achar-heading.py`). Lacunas e anuladas vão numa segunda seção `## Lacunas`, fora da tabela acima. Se o arquivo já existe, é reabsorção: atualize as linhas, não duplique. O registro é a base do Passo 5c e das próximas provas.

### 5b. Nas notas — por heading aprovado

1. **Tracker:** no `- [ ] status [dom:: D] [peso:: P]` do heading, acrescente ` [prova:: N]` logo depois de `[peso:: P]` e **antes** de `✅ data` se houver. **N = valor de `python3 PY/provas-recorrencia.py --heading "<Nota>#<Heading>"`** (recalcule, não incremente). Heading sem tracker (contêiner) fica sem `[prova::]`; só o callout aponta. Nunca crie tracker novo (o `plano-dia.py` passaria a tratar o heading como tópico).
2. **Grifo no trecho:** envolva a frase da nota que a questão testou com `<mark class="prova" style="background:rgba(0,170,170,0.28)">…</mark>` (teal, cor que nenhum outro grifo do cofre usa). Só a frase que decide a resposta, na mesma linha, sem atravessar linha. **Não** grife dentro de `<mark>` ou `<span class="g-…">` existente, nem em heading, tracker, tabela, wikilink ou callout de texto literal: nesses casos o callout do item 3 basta.
3. **Callout `Prova anterior`**, recolhido, logo depois do bloco que tem o trecho (e depois do `[!quote]-` de texto literal desse trecho, se houver):

   ```
   > [!example]- Prova anterior: IBAM 2026 · Bragança Paulista · Q31 (gab. A · oficial)
   > **Trecho usado:** "<até ~25 palavras copiadas da nota>"
   > **Como cobrou:** <ângulo> — <o que a alternativa certa diz / qual termo a errada trocou, literal do PDF>
   > **Lastro:** Caderno tipo 3, p. 15 · [[IBAM 2026 - Bragança Paulista - AFTM Jr#Q31]]
   ```
   Mais de uma prova no mesmo trecho: **um** callout, uma linha por prova, mais recente primeiro. Repetir a mesma frase em vários callouts é ruído.
4. **Lupa de prova** (só onde o Passo 3 item 6 mandou), recolhido, depois do callout `Prova anterior`, com três partes nesta ordem: **o padrão** (o que a banca pergunta nesse tópico e como) → **a armadilha** (a alternativa errada literal, o termo trocado, por que atrai) → **como resolver** (o passo da nota que decide; regra só a que a nota já tem). Rotule o que é inferência: `padrão de 1 prova, não confirmado`. Linguagem de quem explica a um colega.

   ```
   > [!tip]- Lupa de prova: <tema>
   > **O padrão:** …
   > **A armadilha:** …
   > **Como resolver:** …
   ```
5. **Conflito** gabarito × nota que o Pedro mandou registrar: `> [!warning]- Gabarito × nota` com o gabarito, a frase da nota e a pendência. **Não** reescreva a nota.

Regras da escrita:

- **Nunca altere o texto do heading** (quebra os `[[Nota#Heading]]` que já apontam para ele) nem uma palavra do lastro da nota; grifo e callout só **acrescentam**.
- Tabela sempre na margem, com linha em branco antes e depois.
- Callout de prova só de fato que esteja no PDF (número, página, alternativa) ou na nota (o trecho). Nada de "a banca costuma…" sem o rótulo de 1 prova ou a contagem do `provas-recorrencia.py`.
- Ordem no bloco do heading: lastro → texto literal → lupa → ponte → **Prova anterior** → **Lupa de prova**. Acrescente sem reordenar o que já existe.

### 5c. Cruzar as questões erradas

Vale para toda nota de `Erradas/ERRO *.md` (e `LTM ISS SANTOS/ERRO *.md`) das matérias tocadas — ou da matéria pedida em `--erradas`. Cada callout `> [!bug]` ou `> [!question]-` com uma questão real (ignore o modelo `Q[Número]` e as linhas de "Ponto cego") é uma **questão errada**. Para cada uma:

0. **Só as que o Pedro errou ou ficou em dúvida.** Callout com `(acertei)`, `(acertou)` e sem `Obs.` de dúvida fica de fora. Comece por uma varredura dos títulos dos callouts de cada `ERRO *.md` (`grep -nE "^> \[!(bug|question)\]"`), porque a busca por palavra no corpo traz muito ruído (ex.: "Imposto Seletivo" aparece de passagem em dezenas).
1. Identifique a regra que ela testa (leia o callout: `A Regra`, `Onde caí`, o link `[[Nota#Heading]]` se houver).
2. Ache candidatas nos registros: `python3 PY/provas-recorrencia.py <termo> [<termo>…]` e/ou `--heading "<Nota>#<Heading>"`. Leia a linha do registro (e a questão em `.vault-meta/provas/`, se precisar) antes de concluir.
3. Dê um veredito, com a evidência:
   - **✅ Condiz** — a mesma regra/dispositivo foi cobrada em prova absorvida. Diga quais (prova · Q · gab). Se a alternativa que o Pedro marcou é o **mesmo distrator** que a banca usou lá, escreva isso: é o erro que se repete.
   - **🔶 Mesmo tópico, outro ângulo** — o heading foi cobrado, mas a regra/dispositivo é outra. Diga o ângulo da prova e o da questão.
   - **⚪ Não aparece nas N provas absorvidas** — N é o número **real** de registros. Significa "nenhuma das N cobrou", nunca "a banca não cobra". Se a regra só aparece como **alternativa** de uma questão (não é o que decide a resposta), diga isso na linha: "só aparece como alternativa (A) da Q20".

   O veredito segue a **linha do registro** (heading e regra decisiva), não a simples menção no enunciado. Use 🔶 também para a mesma norma em outro dispositivo (ex.: split payment, art. 32 × art. 33), dizendo qual.
   - **Própria questão:** se o callout já é a questão da prova que você está absorvendo (mesmo concurso, ano e nº — os callouts trazem "IBAM (…, Pref. X, 2026)"), o veredito é `🟰 É a própria questão da prova (Q19)`. Não é recorrência: só confirma que o registro e o gabarito batem com o que o Pedro anotou.
4. Escreva **uma linha**, no fim do callout, sem tocar no resto dele. Os callouts das Erradas costumam ter callouts aninhados (`> > [!success]`, `> > [!info]`): coloque antes uma linha só com `>` e depois a linha nova, senão o Obsidian a engole como continuação do aninhado. O prefixo fixo permite reabsorver sem duplicar (se a linha já existe, substitua-a):

   ```
   > **Prova anterior (29/09 · 3 provas absorvidas):** ✅ Condiz — IBAM 2026 Bragança Q31 (gab. A) cobrou a mesma regra; você marcou o distrator "bloqueia a liquidação", igual ao da prova · [[IBAM 2026 - Bragança Paulista - AFTM Jr#Q31]]
   ```

   Sem prova nenhuma absorvida ainda para a matéria, **não** escreva `⚪`: diga no relatório que não há base para o cruzamento.

## Passo 6 — verificar e reportar

1. **O texto original ficou intacto** — por nota tocada (`MATERIAS/`, `Erradas/` e `LTM ISS SANTOS/`), contra a cópia `.antes.md` do Passo 5:
   ```
   python3 PY/provas-recorrencia.py --limpo "$TMPDIR/provas/<nome>.antes.md" > $TMPDIR/A.txt
   python3 PY/provas-recorrencia.py --limpo "<nota>" > $TMPDIR/D.txt
   cmp $TMPDIR/A.txt $TMPDIR/D.txt
   ```
   O `--limpo` remove grifo teal, `[prova:: N]`, callouts de prova, a linha das Erradas e os brancos que os separam; então o `cmp` tem que sair **sem diferença**, byte a byte. Se diferir, o `diff` dos dois mostra o conteúdo perdido ou alterado: pare e investigue. Use arquivos, não `diff <(…)` nem `cmp <(…)`: a substituição de processo é bloqueada no sandbox e devolve erro que parece divergência.
2. **Contagem das marcas:** `python3 PY/provas-recorrencia.py --conferir` — termina em `OK`. Linha `!` é `[prova:: N]` que não bate com os registros; linha `?` é heading com prova mas sem marca (só vale se ele não tem tracker).
3. **Renderização:** `python3 PY/checar-markdown.py "<nota>"` (só linhas alteradas; não vale para `LTM ISS SANTOS/`, que não tem git — nela use `--tudo`). E `python3 PY/grifos.py "<nota>"` sem linha `!`.
4. **Links:** todo `[[Nota#Heading]]` e todo `[[<registro>#Q31]]` resolve (`achar-heading.py`).
5. **Auditoria de lastro:** releia cada callout que escreveu e confira com o PDF: número, página, gabarito e alternativa citada. O que falhar sai ou vira `> [!warning]-`.
6. **Relatório** em tabela: o que foi marcado e onde (Q → heading → recurso), lacunas, conflitos e erradas com veredito (✅/🔶/⚪). Depois:
   - **Prioridade de estudo:** headings cobrados em prova **e** com erro recente **e** `dom` baixo — `python3 PY/plano-dia.py --diag "<matéria>"`.
   - **Perfil da banca** (só com ≥ 2 provas da mesma banca): os ângulos que mais aparecem, no registro; rotule quando for 1 prova.
   - Se uma marca `[prova:: N]` alta ainda não tem lupa nem texto literal na nota, aponte: é onde vale um `/absorver-pdf` ou `/triar-inbox`.

O PDF da prova **fica onde está** (nunca apague). Não commite sem o Pedro pedir. `LTM ISS SANTOS/` é gitignorado: as marcas nele só existem no disco.
