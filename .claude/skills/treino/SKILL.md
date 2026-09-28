---
name: treino
description: Gera questões de treino (Certo/Errado e múltipla escolha) e flashcards (frente/verso) a partir do que já está escrito em MATERIAS/ e Erradas/, questões saem como página HTML interativa (Artifact) sem escrever no cofre; FLASHCARDS vão SEMPRE pro Anki por padrão (blocos ```flashcard escritos direto na nota, pro plugin Flashcards sincronizar com o Anki, perfil vault-ba). Só publica flashcards como Artifact (sem Anki) se o Pedro pedir isso explicitamente. Aciona com /treino, ou organicamente sempre que o Pedro pedir pra "treinar", "praticar", "testar o que eu escrevi", "reforçar [matéria]", "fazer uns flashcards de X", "revisar rápido Y" — mesmo sem citar a palavra "treino".
---

# Treino (questões e flashcards gerados do cofre)

Paths relativos à raiz do cofre (`vault-ba/`). Gera **questões** e/ou **flashcards** a partir do que já está em `MATERIAS/` e `Erradas/`, **Regra de saída (definida pelo Pedro em 28/09/2026):** **flashcards vão sempre pro Anki** (Passo 6: blocos ```` ```flashcard ```` escritos na nota de origem) — ele não precisa pedir. O caminho não padrão, que exige pedido explícito, é o contrário: "só me mostra", "sem Anki", "só no artifact" → aí publica o HTML de flashcards (Passos 4–5) sem escrever no cofre. **Questões** continuam só em Artifact, sem escrever no cofre; não substituem o TEC, não contam pro `dom`, não entram no Diario.

## Passo 0 — escopo: tema e tipo de saída

**Tema:**
- **Explícito** ("questões de Imposto Seletivo", "flashcards de Split Payment", "treina Responsabilidade Tributária comigo"): usa isso direto.
- **Sem tema (default):** rode `python3 PY/plano-dia.py --texto` e use os itens das seções **Fazer questões** / **Ler** / **Revisar** do slot atual (ou do dia inteiro, se não houver slot óbvio no momento). Essa lista já vem ordenada por peso do edital × lacuna de domínio — não precisa recalcular pontos cegos à parte, o plano do dia já reflete a pivotagem atual do edital (hoje, ISS Santos).
- **"Reforça meus pontos fracos"** (pedido explícito, sem filtro de dia): use [[Ganho potencial]] / [[Fila de reforço]] em vez do plano do dia — são os painéis que rankeiam peso × lacuna sem o filtro de slot/data de hoje. Se estiverem vazios ou visivelmente desatualizados, avise e caia de volta pro plano do dia.

**Tipo de saída:** "questões" → só quiz; "flashcards"/"cards" → só cards; pedido genérico de "treino" sem especificar → decida pelo contexto (pedido de revisão rápida antes de dormir tende a flashcard; pedido de "praticar"/"testar" tende a questão) ou pergunte em uma linha se não for óbvio.

## Passo 1 — escolher a fonte de conteúdo

Duas fontes, com risco de invenção bem diferente:

- **`MATERIAS/<nota>.md`** — conteúdo de estudo puro. Aqui **você escreve pergunta e resposta do zero**: ancore cada item num trecho específico (linha) e nunca invente artigo, número, prazo ou exceção que não esteja literalmente no texto lido. Se o tema pedido não tiver conteúdo suficiente na nota, diga isso — não complete com o que "provavelmente" é a lei. Ofereça `/absorver-pdf` ou `/tirar-duvida` primeiro.
- **`Erradas/ERRO <MATÉRIA>.md`** — erros já registrados, com comentário do TEC (já vetado por banca real). Reaproveite esse comentário como base da resposta — risco de invenção bem menor que criar do zero. **Não repita a questão original literalmente** (ela já existe lá, refazer o idêntico não ensina nada novo); gere uma variação/ângulo diferente sobre o mesmo dispositivo, ou vire flashcard do núcleo que o erro ensinou.

## Passo 2 — ler o trecho e ancorar

Mesmo fluxo de busca do `/tirar-duvida` (Passo 1):

```bash
python3 PY/achar-heading.py "MATERIAS/<nota>.md" "<termo>"     # linha exata do heading
python3 PY/indice-materia.py "MATERIAS/<nota>.md"              # árvore do bloco/matéria
```

Leia o trecho com `Read` (offset/limit) — nunca a nota inteira, elas têm de 100 a 1400+ linhas. Cada item do treino carrega, no fim, uma linha **Fonte:** `arquivo.md:linha` — o mesmo espírito do bloco "🔗 Na matéria" do `/tirar-duvida`: se você não consegue apontar a linha, não escreva o item.

## Passo 3 — gerar os itens

**Questões** — misture Certo/Errado (padrão TEC) e múltipla escolha A–E (inclua de vez em quando "assinale a INCORRETA/EXCETO", que treina leitura mais fina). A pegadinha de cada item deve trocar **um dado real** do texto — número, sujeito, prazo, exceção — nunca inventar um dado novo que não está na nota. 5–8 questões por lote é o tamanho que já se mostrou bom; ajuste se o Pedro pedir mais ou menos.

**Flashcards** — frente = pergunta ou conceito curto; verso = resposta com o núcleo em destaque (`<mark class="core">`) + **Fonte**. Depois de virar o card, o Pedro marca 🟢 fácil / 🟡 médio / 🔴 difícil: fácil tira o card da fila da sessão; médio e difícil reinserem mais adiante na fila (difícil mais perto, pra repetir antes do fim) — a reordenação só dura a sessão, não precisa persistir entre sessões. 10–15 cards é um bom tamanho de lote.

## Passo 4 — montar o HTML (questões, ou flashcards só quando o Pedro pedir "sem Anki"/"só ver")

Use os templates prontos em `.claude/skills/treino/assets/` como ponto de partida — já têm a paleta, a tipografia (IBM Plex Sans/Serif/Mono sobre fundo parchment) e toda a interação em JS validados em testes anteriores. Copie o template pra um arquivo no scratchpad e só troque:

- `assets/template-questoes.html` — o array `QUESTOES` (`tema`, `bloco`, `artigo`, `tipoLabel`, `enunciado`, `gabarito`, `opcoes[]`, `explicacao`, `pegadinha`, `fonte`) e os textos do topo (`<title>`, eyebrow, bloco "Puxado de").
- `assets/template-flashcards.html` — o array `FLASHCARDS` (`tema`, `artigo`, `frente`, `verso`, `fonte`) e os mesmos textos do topo.

Preencha o bloco **"Puxado de"** dizendo de onde veio o tema (plano do dia de tal dia/slot, Fila de reforço, ou pedido explícito do Pedro) — isso é o que deixa claro que a skill não inventou o assunto, só o conteúdo dos itens. **Nunca remova o disclaimer fixo**: é treino feito por Claude, não conta pro `dom` nem entra no Diario/TEC.

## Passo 5 — publicar

Publique o HTML preenchido com a ferramenta Artifact (ícone `quiz` para questões, `cards` para flashcards). Siga a orientação padrão do `artifact-design`: uma olhada visual antes de publicar, não um loop de screenshots.

## Passo 6 — Anki (padrão para flashcards)

Questões publicam Artifact e não tocam no cofre. **Flashcards passam por este passo sempre**, sem o Pedro precisar pedir (ele só precisa pedir para NÃO mandar). Gere os cards (Passo 3), ancore (Passo 2) e escreva os cards na sintaxe do plugin **Flashcards** (já instalado, perfil Anki `vault-ba`), direto na nota de origem.

**Onde escrever:** logo depois do parágrafo/heading que originou o card, dentro da própria nota (`MATERIAS/<nota>.md` ou `Erradas/ERRO <MATÉRIA>.md`) — perto do contexto, não numa seção separada. Antes de inserir, `grep` a nota pelo trecho da frente do card (ou por `` ```flashcard ``) pra não duplicar um card que já existe.

**Sintaxe exata** (extraída do código do plugin instalado, `flashcards-obsidian/main.js` — a regex que ele usa pra parsear o bloco só reconhece as chaves `front`, `back`, `content` e `type`, então não invente outras chaves tipo `deck:` ou `tags:` dentro do bloco):

```
​```flashcard
front: <pergunta ou conceito curto>
back: <resposta, com o núcleo em **negrito** ou ==highlight==>
​```
```

- `type:` é opcional — omitido = `basic`. Use `type: reversed` quando o card também vale ser treinado ao contrário (ex.: "o que é X" e "como se chama Y" viram duas perguntas úteis). Não use `type: cloze` nesta skill por enquanto (o modo escolhido foi frente/verso, não lacuna).
- **Fonte** vai como texto normal **fora** do bloco (linha `**Fonte:** arquivo.md:linha` logo abaixo), nunca como campo dentro do fence — o parser não reconhece esse campo e um erro aqui faz o card não sincronizar.
- **Deck é automático pela pasta**: card em `MATERIAS/*.md` cai no deck `MATERIAS`; em `Erradas/*.md`, no deck `Erradas` (config `folderBasedDecks`). Não precisa (e não dá pra) especificar deck por card.
- Depois de escrever os blocos, avise o Pedro que ele ainda precisa rodar a sincronização do plugin (comando "Update Anki from current note", ou "Update Anki from vault" pra tudo de uma vez) — isso é dentro do Obsidian, você não consegue disparar.
- ⚠️ **O modo "inline" do plugin colide com o cofre.** As configurações do plugin têm "Inline cards" ligado por padrão, que varre qualquer `Frente::Verso` solto no texto — e o cofre usa `[dom:: N]`, `[peso:: N]`, `[cad:: N]`, `[prox:: N]` em quase todo heading. Isso já gerou cards fantasma tipo "[x] status [dom" numa sincronização real (28/09/2026). Antes do primeiro lote, confirme que "Inline cards" está **desligado** nas configurações do plugin; se não estiver e aparecerem mais cards do que blocos `` ```flashcard `` que você escreveu, ache os extras via AnkiConnect (`findNotes`/`notesInfo` no deck) e apague com `deleteNotes` — não precisa refazer o lote inteiro.
- Cards que entram aqui têm a mesma régua de fonte do resto da skill (Passo 2) — mas agora o erro persiste numa fila de repetição espaçada de verdade, por semanas. Seja mais conservador: se a ancoragem for frágil (parafraseando demais, ou juntando dois trechos distantes), prefira deixar de fora e avisar, em vez de arriscar.

## Regras

- **Só flashcards (Anki) escrevem no cofre; questões e o modo "sem Anki" nunca.** Isto não é `/triar-inbox` nem `/tec-erros` — não move nada pra `Erradas/`, não mexe no Diario, não grifa `MATERIAS/`. Se o Pedro quiser registrar um erro de verdade (questão real do TEC), isso é `/tec-erros`/`/importar-tec`, não esta skill.
- **Nunca inventa fato.** Regra igual ao `/tirar-duvida`: nunca afirme algo sem ter lido o trecho; se não achou, diga que não achou. Vale em dobro no modo Anki, por causa da persistência.
- **O disclaimer é obrigatório** em toda página publicada (Artifact) — quem olha precisa saber, sem precisar perguntar, que aquilo é treino sintético e não entra nas métricas oficiais.
- Reforma Tributária muda de redação com frequência (LC 227/2026 já revogou parágrafos da LC 214/2025 mais de uma vez) — ao ancorar um item, confira se o trecho da nota já está marcado como redação vigente; se a nota tiver uma nota de "redação anterior"/"revogado", não vire pergunta (nem card) com base no texto revogado.
