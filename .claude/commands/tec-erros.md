---
description: Lê o JSON de questões erradas do TEC (extraído pelo bookmarklet ou por PY/tec-erradas.py) e registra cada erro em Erradas/ERRO <matéria>.md, no mesmo formato rico que o /tirar-duvida usa em "💭 Dúvidas respondidas"
---

Transforma o JSON de questões erradas (enunciado, alternativas, gabarito, comentário) em entradas na seção `## 💭 Dúvidas respondidas` de `Erradas/ERRO <matéria>.md` — **mesmo layout, formatação e regras do `/tirar-duvida`** (veja `.claude/skills/tirar-duvida/SKILL.md`, seção "Layout"). Não é um formato novo: é o mesmo, alimentado por um JSON em vez de dúvida colada.

## Passo 0 — achar o JSON

Se o Pedro não apontar o arquivo, pegue o mais recente:

```
ls -t ~/Downloads/tec-erradas-*.json | head -1
```

Leia com o Read normal (é pequeno, é JSON já compacto). Cada bloco tem `caderno` (nome), `data` (do caderno, sem hora por questão) e `questoesErradas[]` — cada questão com `idQuestao`, `materia`, `assunto`, `banca`, `concurso` (`orgao`/`cargo`/`ano`), `enunciado`, `alternativas[]` (`letra`/`texto`/`marcada`/`correta`) e `comentario` (texto corrido, ausente se o TEC não publicou).

## Passo 1 — decidir a matéria de cada caderno

**O nome do caderno (`caderno`) manda mais que o campo `materia` da questão.** O Pedro nomeia os cadernos pela matéria de estudo dele (ex: caderno "C01. RETRI LC 227/26" = Reforma Tributária, mesmo que a questão traga `materia: "Legislação Tributária Federal"`). `materia`/`assunto` da questão servem de contexto/desempate.

`ls Erradas/` lista as notas existentes. Ache a que casa (comparando palavras-chave, ignorando "ERRO " e ".md"). Sem casamento confiável, pergunte com `AskUserQuestion` (opções = notas existentes + "criar nova") — **não crie nota nova sem confirmar**.

## Passo 2 — não duplicar

Cada questão processada fica identificável pelo `idQuestao` dentro do `#` da linha de título (ex: `Inéditas (AFRFB 2026, #3876770)`) ou, se a banca for real, no corpo. Antes de escrever, `grep` a nota alvo por esse `idQuestao` — se já existe, pule.

## Passo 3 — escrever cada entrada nova, no layout do `/tirar-duvida`

Siga **exatamente** a seção "Layout" de `.claude/skills/tirar-duvida/SKILL.md`: título `dd/mm hh:mm · matéria · banca (prova) — tema`, alternativas com `<mark>` verde no gabarito e vermelho na marcada, linha `**Marquei:** 🟥 X · **Gabarito:** 🟩 Y`, `[!success]` com núcleo em amarelo e grifos semânticos (`g-prazo`/`g-cond`/`g-comp`/`g-num`), e os blocos opcionais (`🧩 Quadro`, `⚠️ Pegadinha`, `💡 Macete`, `📜 Texto literal`, `🔗 Na matéria`) **só quando têm conteúdo de verdade** — não force todos em toda questão.

Adaptações específicas pra essa origem (JSON, não dúvida colada):

- **Sem hora por questão** (o bookmarklet não captura isso) — use `<data do caderno> (mesma captura, sem hora registrada)`, igual já aparece em entradas anteriores desta nota.
- **Banca/prova:** se `banca` for uma banca real (CEBRASPE, FGV, FCC, IBAM etc.), formate `<banca> (<cargo ou órgão abreviado>, <ano>)`. Se `banca` vier `"Tec Concursos"` (questão inédita do TEC), use o padrão já usado nesta nota: `Inéditas (<cargo abreviado> <ano>, #<idQuestao>)`.
- **Fonte do "Resposta":** use o `comentario` do JSON (já vem com o texto legal citado) — **não pesquise de novo** no cofre ou na internet por questão, isso é trabalho do `/tirar-duvida` interativo. Aqui é distilar o que o TEC já trouxe.
- **"Na matéria":** rode `python3 PY/achar-heading.py "MATERIAS/<nota>.md" "<termo do assunto>"` pra achar o heading — é rápido e vale a pena, mas não é uma investigação: se não achar de primeira, marque "não está no cofre" e siga, sem insistir.
- **Grifar a matéria:** só se o trecho relevante **ainda não estiver grifado** lá (confira antes) — se já estiver, diga "já estava grifado" em vez de reprocessar. Não é obrigatório fazer isso pra toda questão; faça quando for rápido de achar.
- Questão sem `comentario`: registre mesmo assim, com `[!success]` deduzindo pela alternativa `correta` vs a `marcada`; sem `📜 Texto literal` nem `⚠️ Pegadinha` (não force um "por quê" que você não tem fonte).

## Passo 4 — padrão comportamental (não confundir com pontos cegos de conteúdo)

Se várias questões do mesmo lote erram por um **padrão de comportamento** (ex: marcar Errado em item literal por desconfiança, não por falta de conteúdo) em vez de lacuna de matéria, registre isso **uma vez** em "🎯 Mapeamento de Pontos Cegos" — não repita a observação em cada callout individual. Pontos cegos de **conteúdo de verdade** (2+ erros no mesmo `assunto` por não saber a matéria) também entram ali, à parte.

## Passo 5 — heading de dia

Igual o `/tirar-duvida` faz: antes da primeira entrada de hoje em `## 💭 Dúvidas respondidas`, insira `### dd/mm` (sem hora) se ainda não existir um heading pra esse dia nessa nota — linha em branco antes e depois. Não repita o heading se já tiver entrada de hoje ali (é só a primeira do dia que abre o heading).

## Antes de reportar como feito

1. **Rode a validação de colchete** (regra do `/tirar-duvida`, mesma classe de bug):
   ```bash
   grep -n '\[!.*\]-\]' "Erradas/ERRO <MATÉRIA>.md"
   ```
   Tem que sair vazio.
2. Confira `Questoes/Duvidas.md`: se o caderno usado ainda não tem link em "Dúvidas respondidas, por matéria", acrescente `- [[ERRO <MATÉRIA>#💭 Dúvidas respondidas|<Matéria>]]`.
3. Relate em tabela: matéria/nota alvo, quantas entradas novas, quantas já existiam (puladas), padrão comportamental ou ponto cego de conteúdo encontrado.
4. Avise que `python3 PY/agendar_revisoes.py --vault "$(pwd)" --apply` agenda a revisão das entradas novas pela tag `#tec/erro`, quando o Pedro quiser — não rode por conta própria.
5. Não commite sem o Pedro pedir.
