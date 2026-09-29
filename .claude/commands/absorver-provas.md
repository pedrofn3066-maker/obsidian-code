---
description: Absorve uma prova antiga: resolve cada questão (cofre primeiro, fonte oficial se preciso), grava a prova resolvida em Questoes/Provas com link para os headings e, por último, marca as matérias e cruza as erradas
argument-hint: <prova.pdf> [gabarito.pdf] | --erradas [matéria] | --recorrencia
---

Absorva a prova `$ARGUMENTS`: extraia as questões, **resolva cada uma**, cruze com o que o cofre já ensina e **proponha** o que gravar. **Nada é escrito em `Questoes/Provas/`, `MATERIAS/`, `Erradas/` nem `LTM ISS SANTOS/` antes do Pedro aprovar a tabela do Passo 4.**

Os modos, pelo argumento:

- `<prova.pdf> [gabarito.pdf]` — Passos 1 a 6.
- `--erradas [matéria]` — só o Passo 5b, contra os registros já absorvidos (use depois de importar cadernos do TEC).
- `--recorrencia` — só relatório: `python3 PY/provas-recorrencia.py` cruzado com `dom::` e erros (Passo 6, item 6).

Tudo o que o comando escreve é de um de cinco tipos, e o tipo decide o que pode entrar:

- **Lastro de prova** — o que o PDF diz: nº da questão, página, gabarito, enunciado e alternativas literais. Intocável.
- **Resolução** — a resposta que *você* deu à questão, sempre com fonte: `cofre` (arquivo:linha), `internet` (URL oficial) ou `resolução própria` (Português, cálculo, lógica). Vive só na prova resolvida.
- **Ponte** — ligação com o que o cofre já sabe (`[[Nota#Heading]]`, súmula, erro de caderno). Só liga o que existe.
- **Lupa de prova** — explicação de *como a banca cobrou* aquele tópico, em callout recolhido. Interpretação: rotule (`padrão de 1 prova, não confirmado`). Nenhuma regra jurídica que a nota não tenha.
- **Marca** — o que aponta o trecho na matéria: `[prova:: N]`, grifo teal e callout `Prova anterior`. Não altera palavra da nota.

O cofre é a fonte da regra nas matérias: **este comando não cria conteúdo jurídico em `MATERIAS/`**. O que só a fonte externa trouxe fica na prova resolvida e vira sugestão de `/absorver-pdf` ou `/triar-inbox` no relatório.

## Passo 1 — extrair as questões

```
python3 PY/prova-questoes.py "<prova.pdf>" [--gabarito "<gabarito.pdf>"] [--tipo N] --esqueleto "<Banca Ano (Local, Cargo)>"
```

Grava em `.vault-meta/provas/` (ignorado pelo git): `<nome>.md` (um bloco `### Q07 · disciplina · p.N · gab: X` por questão) e `<nome>.resolvida.md` (o esqueleto da prova resolvida, no layout de `TEMPLATE/Prova resolvida.md`). Provas ficam em `LTM ISS SANTOS/PROVAS/PDF/` ou `inbox/`. Leia o diagnóstico antes de qualquer coisa:

- `SEM gabarito confiável` → procure o edital de gabaritos e passe com `--gabarito`. Sem gabarito você resolve, mas não compara: coluna Gab `?`, nada de lupa.
- `gabarito tem tipos [1, 2, 3]` → caderno embaralhado, um gabarito por tipo; o tipo vem da capa (`TIPO:3`). Se o script parar, pergunte qual caderno o Pedro tem. **Tipo errado inverte certo e errado**, e nada mais avisa.
- `questões fora de ordem no texto` → duas colunas embaralhadas: refaça por coluna com `pymupdf` no scratchpad (blocos por coluna, depois por `y`) ou leia o PDF (`Read` com `pages`).
- `nenhum marcador 'Questão N'` / `N pág(s) com pouco texto` → escaneada ou manuscrita: leia as páginas e monte a lista à mão. **Gabarito manuscrito, de terceiro ou preliminar é não oficial**: vai no frontmatter e em todo callout (`gab. preliminar`).
- **PDF que é impressão de página de site** (OCR embaralhado, alternativa certa numa caixa verde "GABARITO PRELIMINAR"): o script não serve, e a caixa verde por pixel erra (a borda encosta em duas alternativas). Renderize cada página em metades com `pymupdf` (`get_pixmap(matrix=Matrix(2.6, 2.6), clip=…)`, no scratchpad), leia as imagens e anote a letra da caixa. Logo e rodapé ("© IBAM") dão a banca quando o nome do arquivo diz "não confirmada".
- `sem 4+ alternativas separadas` → certo/errado, asserção-razão ou `**D)**` colado: confira essas questões no PDF antes de resolver.
- Questão anulada ou alterada por recurso → `ANULADA` no Mapa, sem marca na nota.
- Banca, ano, órgão ou cargo que o PDF não dá: pergunte uma vez com `AskUserQuestion`. Banca desconhecida entra como tal.

Concluído quando o diagnóstico não tem aviso sem resposta e o nº de questões extraídas é o do caderno.

## Passo 2 — resolver às cegas

Para **cada** questão (não só as que a nota cobre), antes de olhar o porquê do gabarito:

1. **Ache no cofre** o que decide a resposta. Nunca leia nota inteira (têm até 1400+ linhas):
   - qual nota: `python3 PY/diretorio-materias.py [palavra]`. Legislação **específica de Santos** vive em `LTM ISS SANTOS/` (fora do git; memória `iss-santos-prep`), a **da Bahia** só em `MATERIAS/`. Na dúvida, pergunte;
   - headings e `dom::`: `python3 PY/indice-materia.py "MATERIAS/<nota>.md"`; linha do heading (tolera NBSP): `python3 PY/achar-heading.py "<nota>" "<trecho>"` (o aviso `SEM tracker` pode ser falso; confira com `sed -n`);
   - o trecho: `grep -niE "termo.{1,2}outro" "<nota>"` (`.{1,2}` por causa do NBSP) e `Read` de ~40 linhas;
   - o resto do cofre: `Erradas/ERRO *.md`, `Questoes/Diario/`, `wiki/concepts/` (súmulas) e as provas já registradas (`python3 PY/provas-recorrencia.py <termo>`) mostram se a regra já foi cobrada e onde o Pedro erra; `python3 PY/plano-dia.py --diag "<matéria>"` dá `dom` e erros.
2. **Resolva.** O cofre decide → `cofre`. Português, matemática, lógica → `resolução própria` (confira conta em Python). Vá à **fonte oficial** quando (a) o cofre não decide (lacuna ou parcial), (b) a norma muda com frequência (Reforma Tributária: EC 132/2023, LC 214/2025, LC 227/2026), ou (c) sua resposta diverge do gabarito. Fontes, ferramentas e cuidados são os do `/tirar-duvida`, Passo 3 (`WebSearch`/`WebFetch` vêm deferidos: carregue com `ToolSearch`): oficial primeiro, cursinho só como apoio, lei seca pode ser citada literal, o resto se resume com URL.
3. **Compare com o gabarito.** Divergiu: releia o PDF e o tipo do caderno antes de afirmar; se persistir, é **conflito** — registre o que o gabarito manda, o que a fonte diz e a situação do gabarito (preliminar?). **Nunca corrija a nota nem o gabarito por conta própria.**

Concluído quando toda questão tem resposta, fonte e situação (`concorda` / `diverge`). Uma questão sem fonte é `resolução própria`, dita como tal; nunca deixe fonte em branco.

## Passo 3 — classificar

Para cada questão:

1. **Regra cobrada** em uma linha: o dispositivo que decide a resposta, não o enunciado.
2. **Nota → heading → trecho**: o heading da regra e a frase da nota que a resolve (linha exata), só se você leu esse trecho. Mais de um heading decisivo = uma linha do Mapa por heading; headings que só uma alternativa toca são "vizinhos", vão só no `Na matéria`.
3. **Cobertura**, lendo a nota: **coberto** (a nota tem a regra e o gabarito é coerente) · **parcial** (falta o dispositivo, o rol ou a pegadinha) · **lacuna** (a nota não trata; nada é marcado) · **conflito** (gabarito ou resolução contradiz a nota: `> [!warning]- Gabarito × nota`, sem reescrever).
4. **Ângulo**: `literalidade`, `troca de termo`, `exceção`, `rol/lista fechada`, `prazo/número`, `cálculo`, `competência`, `jurisprudência` ou `conceito`.
5. **Recorrência**: `python3 PY/provas-recorrencia.py --heading "<Nota>#<Heading>"` + esta prova.
6. **Lupa de prova** só se bater em um: (a) heading em ≥ 2 provas; (b) distrator sutil que dá para apontar na alternativa literal; (c) `ERRO` recente do Pedro; (d) `dom` ≤ 1 com peso alto. A marca já basta nos demais.
7. Se a nota já registra a pegadinha (`grep -n "Pegadinha de prova"`), a marca aponta para ela em vez de repetir o fato.

Concluído quando toda questão tem regra, cobertura e recurso.

## Passo 4 — o plano (o que o Pedro aprova)

Uma tabela, uma linha por questão, sem texto colado:

| Q | Disc. | Gab | Regra cobrada | Nota → heading (linha) | Trecho usado (início) | Cobertura | Fonte (cofre / externa / própria) | Recorrência | Recurso (marca / +lupa) | Erradas afetadas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Depois dela: (1) **lacunas** com sugestão de onde entrar, e **o que só a fonte externa trouxe**; (2) **conflitos** e questões em que a resolução diverge do gabarito; (3) anuladas, sem gabarito, gabarito não oficial e o que isso muda; (4) **erradas afetadas** com veredito provisório; (5) **sobreposições** entre notas (pergunte com `AskUserQuestion`); (6) **onde estudar primeiro**: recorrência × `dom::` baixo × erro do Pedro.

Pare e peça aprovação. Concluído quando as onze colunas estão preenchidas em todas as linhas e a pergunta foi feita.

## Passo 5 — escrever (só após aprovação), nesta ordem

**Antes de editar qualquer nota** (`MATERIAS/`, `Erradas/`, `LTM ISS SANTOS/`), copie-a para `$TMPDIR/provas/<nome>.antes.md`: é a base do Passo 6. O `git show HEAD:` só serve se a nota não tinha mudança não commitada, e no cofre do Pedro quase sempre tem. Escreva por script Python que **localiza heading e trecho por texto** (não por nº de linha: cada inserção desloca as seguintes; nunca `old_string` exato, por causa do NBSP), recusa âncora que não ache exatamente uma vez e roda antes em modo simulação, imprimindo heading, linha e se há tracker.

### 5a. A prova resolvida e o Mapa — dois arquivos

**Prova resolvida** — `Questoes/Provas/<Banca> <Ano> - <Local> - <Cargo>.md`: **só as questões**, nada mais (sem frontmatter, título, resumo, mapa, lacunas nem textos-base; uma nota grande com muitos links e callouts travou o Obsidian). Parta do `.resolvida.md` do Passo 1 e siga `TEMPLATE/Prova resolvida.md` (leia-o antes; é o layout do `/tec-erros`): uma seção `### Q<n>` para **todas** as questões, com a **Resolução** do Passo 2 e um link `[[Nota#Heading]]` para cada heading relacionado (o do Mapa mais os vizinhos).

**Mapa** — `.provas-mapa/<mesmo nome>.md` (pasta oculta do Obsidian, versionada pelo git): frontmatter, introdução, Resumo por disciplina, Mapa de sete colunas, Lacunas e textos-base, tudo com `Nota#Heading` em texto puro (sem `[[ ]]`). É o que o `PY/provas-recorrencia.py` lê.

Se os arquivos já existem é reabsorção: atualize, não duplique. Concluído quando o nº de `### Q<n>` é o do caderno, toda `Fonte` está preenchida e todo link resolve (`achar-heading.py`).

### 5b. Cruzar as questões erradas

Para toda nota `Erradas/ERRO *.md` (e `LTM ISS SANTOS/ERRO *.md`) das matérias tocadas, ou a pedida em `--erradas`. Comece pelos títulos dos callouts (`grep -nE "^> \[!(bug|question)\]"`); a busca por palavra no corpo traz ruído. **Só as que o Pedro errou ou ficou em dúvida** (`(acertei)`/`(acertou)` sem `Obs.` de dúvida ficam de fora). Para cada uma:

1. Identifique a regra que ela testa (`A Regra`, `Onde caí`, o `[[Nota#Heading]]`).
2. Ache-a nos registros (`provas-recorrencia.py <termo>` ou `--heading`) e leia a linha do Mapa antes de concluir.
3. Veredito, com a evidência:
   - **✅ Condiz** — mesma regra/dispositivo cobrada em prova absorvida (prova · Q · gab). Se a alternativa que o Pedro marcou é o **mesmo distrator** da banca, diga: é o erro que se repete.
   - **🔶 Mesmo tópico, outro ângulo** — heading cobrado, regra outra; ou mesma norma em outro dispositivo (diga qual).
   - **⚪ Não aparece nas N provas absorvidas** — N real. Significa "nenhuma cobrou", nunca "a banca não cobra". Regra que só aparece como alternativa: diga ("só como alternativa (A) da Q20").
   - **🟰 É a própria questão da prova** (mesmo concurso, ano e nº): não é recorrência, só confirma que registro e gabarito batem.
   O veredito segue a **linha do Mapa** (heading e regra decisiva), não a menção no enunciado.
4. Uma linha no fim do callout. Os das Erradas costumam ter callouts aninhados: ponha antes uma linha só com `>`, senão o Obsidian a engole. O prefixo permite reabsorver (linha existente é substituída); ao mudar a contagem de provas, atualize as linhas já escritas:

   ```
   >
   > **Prova anterior (29/09 · 3 provas absorvidas):** ✅ Condiz — IBAM 2026 Bragança Q31 (gab. A) cobrou a mesma regra · [[IBAM 2026 - Bragança Paulista - AFTM Jr#Q31]]
   ```

Sem prova absorvida para a matéria, **não** escreva `⚪`: diga no relatório que não há base.

### 5c. Marcas nas matérias — o último passo

Por heading aprovado, só acrescentando:

1. **Tracker:** ` [prova:: N]` depois de `[peso:: P]` e **antes** de `✅ data`. N = valor de `provas-recorrencia.py --heading` (recalcule, não incremente). Heading sem tracker fica sem `[prova::]` (só o callout aponta); nunca crie tracker (o `plano-dia.py` passaria a tratar o heading como tópico).
2. **Grifo:** `<mark class="prova" style="background:rgba(0,170,170,0.28)">…</mark>` (teal, cor sem uso no cofre) na frase que a questão testou; mesma linha, sem atravessar. **Não** grife dentro de `<mark>` ou `<span class="g-…">`, nem em heading, tracker, tabela, wikilink ou callout: então basta o callout.
3. **Callout `Prova anterior`**, recolhido, logo depois do bloco do trecho (e do `[!quote]-` literal dele, se houver). Mesma frase em mais de uma prova = um callout, uma linha por prova, mais recente primeiro:

   ```
   > [!example]- Prova anterior: IBAM 2026 · Bragança Paulista · Q31 (gab. A · oficial)
   > **Trecho usado:** "<até ~25 palavras copiadas da nota>"
   > **Como cobrou:** <ângulo> — <o que a certa diz / o termo que a errada trocou, literal do PDF>
   > **Lastro:** PDF p. 15 · [[IBAM 2026 - Bragança Paulista - AFTM Jr#Q31]]
   ```
4. **Lupa de prova** (só onde o Passo 3 mandou), depois do callout, em três partes: **o padrão** → **a armadilha** (alternativa errada literal, termo trocado) → **como resolver** (só regra que a nota já tem). Rotule inferência.

   ```
   > [!tip]- Lupa de prova: <tema>
   > **O padrão:** …
   > **A armadilha:** …
   > **Como resolver:** …
   ```
5. **Conflito** aprovado pelo Pedro: `> [!warning]- Gabarito × nota` (gabarito, frase da nota, pendência), no heading da regra.

Regras: nunca altere o texto de um heading (quebra `[[Nota#Heading]]`) nem uma palavra do lastro da nota. Tabela na margem, com linha em branco antes e depois. Callout só de fato que esteja no PDF ou na nota. Ordem no bloco: lastro → texto literal → lupa → ponte → **Prova anterior** → **Lupa de prova**, sem reordenar o que já existe.

## Passo 6 — verificar e reportar

1. **Texto original intacto**, por nota tocada contra a cópia `.antes.md`:
   ```
   python3 PY/provas-recorrencia.py --limpo "$TMPDIR/provas/<nome>.antes.md" > $TMPDIR/A.txt
   python3 PY/provas-recorrencia.py --limpo "<nota>" > $TMPDIR/D.txt
   cmp $TMPDIR/A.txt $TMPDIR/D.txt
   ```
   O `--limpo` remove grifo teal, `[prova:: N]`, callouts de prova, a linha das Erradas e os brancos que os separam: o `cmp` sai **sem diferença**, byte a byte. Se diferir, o `diff` mostra o que se perdeu: pare. Use arquivos: `diff <(…)` e `cmp <(…)` são bloqueados no sandbox e dão erro que parece divergência.
2. **Contagem das marcas:** `python3 PY/provas-recorrencia.py --conferir` termina em `OK` (`!` = N que não bate; `?` = heading com prova sem marca, válido só sem tracker).
3. **Renderização:** `python3 PY/checar-markdown.py "<nota>"` (`--tudo` em `LTM ISS SANTOS/` e na prova resolvida) e `python3 PY/grifos.py "<nota>"` sem linha `!`. Na prova resolvida: `grep -n '\[!.*\]-\]' "<prova>.md"` vazio.
4. **Links, nos dois sentidos:** todo `[[Nota#Heading]]` da prova resolvida resolve e todo `Nota#Heading` do Mapa (em `.provas-mapa/`) aparece como link na questão dele; todo `[[<prova>#Qn]]` das matérias e das Erradas aponta para um `### Qn` que existe; todo heading marcado aparece em alguma questão da prova resolvida.
5. **Auditoria de lastro:** releia cada callout e confira com o PDF (nº, página, gabarito, alternativa). O que falhar sai ou vira `> [!warning]-`.
6. **Relatório** em tabela (o que foi marcado e onde, lacunas, conflitos, erradas com veredito) e depois: **prioridade de estudo** (cobrado em prova × erro recente × `dom` baixo, via `plano-dia.py --diag`); **perfil da banca** (só com ≥ 2 provas da mesma banca; rotule o de 1 prova); marcas `[prova:: N]` altas sem lupa nem texto literal na nota, onde vale `/absorver-pdf` ou `/triar-inbox`.

O PDF **fica onde está**. Não commite sem o Pedro pedir. `LTM ISS SANTOS/` é gitignorado: as marcas nele só existem no disco.
