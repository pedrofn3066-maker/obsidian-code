---
tipo: painel
---

# S1 — Revisão de ontem

Painel do slot **S1** (30 min, todos os dias): recuperação de memória do que entrou no vault no dia anterior, **sem consultar a nota**.

S1 é o único slot que nunca aparece em `Questoes/Diario`, porque não é caderno de questões. O que ele revisa é o que você **escreveu** ontem — capturas do Atalho já triadas, anotações de aula, trechos de lei. Este painel reconstrói isso.

A ordem importa: primeiro os dois blocos abaixo dizem **onde** você mexeu; só então você tenta lembrar o conteúdo; só depois abre a nota. Abrir primeiro é reconhecimento, não recuperação — e reconhecimento produz a sensação de saber sem o saber.

## 1. Onde você mexeu ontem

```dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  bloco AS "Bloco",
  prioridade AS "Prioridade",
  dateformat(file.mtime, "HH:mm") AS "Última edição"
FROM ("MATERIAS" OR "Questoes" OR "Erradas") AND -"Questoes/Paineis"
WHERE file.mtime >= date(today) - dur(1 day) AND file.mtime < date(today)
SORT file.mtime ASC
```

> [!warning]- O que esta tabela erra — e o que ela acerta
> `file.mtime` guarda a **última** modificação, não todas. Nota editada ontem e reaberta hoje some daqui: conta como "hoje". Esse é o furo, e ele só tira linhas — nunca inventa uma.
>
> Em compensação, `mtime` é a **única** fonte do momento real da escrita. O git (bloco 3) registra o momento do *commit*, que é outra coisa: um commit de recuperação empacota dias de trabalho numa data só e atribui tudo ao dia em que você lembrou de commitar. Verificado em 2026-09-08 — o commit das 19:09 daquele dia carregava três notas escritas na véspera.
>
> Regra prática: **mtime diz quando você escreveu, git diz o que você escreveu.** Um não substitui o outro, e quando discordarem sobre a data, o mtime está certo.

## 2. Cadernos de ontem

```dataview
TABLE WITHOUT ID
  materia AS "Matéria", assuntos AS "Assuntos", slot AS "Slot",
  total AS "Q", acertos AS "Ac",
  round(100 * acertos / total, 1) AS "%", erro_tipo AS "Erro"
FROM "Questoes/Diario"
WHERE materia AND data = date(today) - dur(1 day)
SORT slot ASC
```

Se vier vazio, **não conclua que ontem não teve questões** — conclua que não teve registro. Confira no TEC antes: caderno resolvido e não lançado é o modo de falha mais comum aqui, e ele esconde justamente a informação mais valiosa do S1, que é o par erro → anotação. Só depois de confirmar que o dia foi mesmo de leitura vale a leitura de "recuperação de conteúdo novo, nunca testado".

## 3. O que você escreveu (não só onde)

Os blocos acima dizem em que arquivo você mexeu. Para ver o **texto** que entrou, é preciso git — o Dataview não lê histórico. Use o git pelo *conteúdo*, e o bloco 1 pela *data*: `--since` filtra por data de commit, então um commit de recuperação vai te mostrar, sob a data de ontem, coisa escrita dias antes. Cruze sempre com a tabela do bloco 1 antes de concluir que escreveu algo ontem.

No Terminal, na pasta do vault:

```
git log --since=yesterday.midnight --until=today.midnight --name-status --format=">>> %ad %s" --date=format:"%H:%M"
```

E para ler o conteúdo linha a linha, com contexto de onde caiu:

```
git log --since=yesterday.midnight --until=today.midnight -p -- MATERIAS/
```

Isso só funciona para o que já foi commitado. O que você escreveu ontem e ainda não commitou não aparece em nenhum dos dois — aparece em `git diff` puro, sem argumento de data.

## 4. Como rodar os 30 min

1. **Leia só a coluna "Nota"** dos blocos 1 e 2. Não abra nada ainda.
2. Para cada nota, escreva ou fale: *o que eu acrescentei ali ontem?* Falhar em lembrar já é o dado — é o item que precisa voltar.
3. Só então abra e confira.
4. **O passo que quase todo mundo pula:** abra o `Checklist por importância (VINTEUM)` da matéria e veja se o que você acrescentou cai num tópico de **peso alto**. Escrever muito num tópico de 4% enquanto um de 21% está com `dom:: 3` é o erro mais caro e mais invisível do sistema — o volume de anotação dá sensação de produtividade sem mover pontuação.
5. Atualize o `[dom:: N]` do tópico se a recuperação mostrou que mudou.

Não atualize `revisado` da nota por causa do S1 — aquele campo alimenta a [[Agenda de releitura]] e mede esquecimento de resumo inteiro, não de um trecho novo.

## 5. O que o S1 não faz

Ele não substitui a [[Fila de revisão]] nem a [[Agenda de releitura]]. Aquelas duas trabalham em escala de semanas e são movidas por desempenho em questões. O S1 trabalha em escala de 24h e é movido pelo que você **escreveu**. Um conteúdo bem recuperado no S1 ainda vai voltar pela agenda no intervalo dela — recuperar hoje não quita a revisão de daqui a 10 dias.

---

# Registro

Anotação manual dos S1 em que apareceu algum padrão que valha lembrar. Não precisa registrar todo dia — só quando o dia revelou alguma coisa sobre **como** você está estudando, não sobre o conteúdo.

## 2026-09-08 (terça)

**Entrou de fato na terça** (confirmado por `mtime`, não por data de commit): definição de mercadoria (§2º) → LTE-BA · drawback não se aplica a IBS/CBS → Reforma Tributária · Art. 399 CC, mora do devedor → Direito Civil · NBC TA 230 §8 (documentação), A7 (amostragem), NBC TA 540 (estimativas), A9 (especialista) e o bloco SPED — NF-e com cancelamento em 24h, inutilização até o 10º dia, limites da CC-e, mais ECD/ECF → Auditoria.

**Não conta como terça:** Língua Portuguesa (formas nominais, "tão… que"), Cont. Avançada (classificação no BP por intenção) e Direito Tributário (imagem da CF) foram escritos na **segunda (07/09)** e só entraram no commit de recuperação das 19:09 de terça.

**Cadernos da terça** (importados do TEC só em 09/09, por isso o bloco 2 aparecia vazio): 24 questões, 20 acertos, 83% — Auditoria 9/11 · Direito Civil 8/10 · Cont. Geral 2/2 · LTE 1/1.

**Três padrões:**

- **A escrita da terça foi correção de erro, não leitura solta.** Os dois erros de Auditoria — Contingências e Estimativas Contábeis, e Utilização do Trabalho de Outros Profissionais — são exatamente os dois tópicos anotados no mesmo dia (NBC TA 540 e A9). O erro de Direito Civil foi em "Da Mora", e a anotação do dia foi o art. 399. O ciclo errar → anotar funcionou; não é preciso corrigi-lo.
- **O problema está a montante, na escolha do caderno.** Num dia de 24 questões, Auditoria levou 11 e LTE levou 1. Auditoria vale 15 pontos (`importante`); LTE vale 75 (`crítico`) e é o primeiro critério de desempate da área. A terça também deixou Cont. Avançada (S3, 90 min) e Finanças Públicas (S5) com zero. A segunda, em contraste, seguiu a grade à risca.
- **Um erro não virou nota.** "Das Obrigações Alternativas (arts. 252 a 256)", 0/1, é o único erro da terça sem correção escrita em lugar nenhum. Os outros três geraram anotação no mesmo dia.

**Lição de método:** este registro nasceu errado duas vezes. Primeiro atribuiu à terça três notas da segunda, porque foi montado com `git log --since`, que filtra por data de commit — o bloco 1 pegou. Depois concluiu que a terça não teve questões, quando na verdade os cadernos existiam e só não tinham sido lançados. **Bloco 2 vazio não significa "dia sem questões", significa "dia sem registro"** — confira no TEC antes de tirar conclusão sobre o dia.

**Resolvido em 2026-09-09:** o bloco SPED estava solto no fim de `MATERIAS/P1 - Auditoria.md`, fora do tópico "Auditoria Fiscal" a que pertence — o checklist não o contabilizava como progresso. Reaninhado sob `## - Auditoria Fiscal;` (commit `9609869`).
