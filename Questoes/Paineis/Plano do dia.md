---
tipo: painel
---

# Plano do dia

A [[Slots (Grade Semanal)]] diz **qual matéria** cai em cada slot. Não diz o que fazer dentro dela — e numa matéria de 26 tópicos, abrir a nota e escolher na hora é onde o slot se perde: o olho vai para o que está mais à mão, não para o que vale mais ponto.

Este painel responde, para cada slot do dia, **quais subtópicos ler, quais praticar em questões e quais revisar**, cruzando quatro coisas que o vault já tem mas que nenhum outro painel junta no nível do tópico:

- **peso do edital** — o `[peso::]` do `Checklist por importância (VINTEUM)` da nota;
- **domínio em questões** — o `[dom::]` do mesmo checklist (histórico real do TEC, calculado em 06/09);
- **o que já está escrito** — se o heading do tópico tem conteúdo e **quando** ele entrou (git blame);
- **o que você errou** — as linhas de `## Erros a revisar` dos cadernos de `Questoes/Diario`.

## Como rodar

O Dataview não lê histórico do git, então o cálculo mora em `PY/plano-dia.py` — mesmo arranjo do bloco 3 de [[S1 - Revisão de ontem]]. No Terminal (a aba ao lado da conversa no Claude Code, ou o Terminal.app):

```
python3 "$HOME/Library/Mobile Documents/com~apple~CloudDocs/vault-ba/PY/plano-dia.py"
```

Abre uma página no navegador com o plano de hoje. Cada tópico é um link que abre a nota **direto no heading** (via Advanced URI). Variações:

```
python3 "$HOME/Library/Mobile Documents/com~apple~CloudDocs/vault-ba/PY/plano-dia.py" --data 2026-09-16
python3 "$HOME/Library/Mobile Documents/com~apple~CloudDocs/vault-ba/PY/plano-dia.py" --texto
python3 "$HOME/Library/Mobile Documents/com~apple~CloudDocs/vault-ba/PY/plano-dia.py" --diag Penal
```

`--data` planeja outro dia (útil no domingo, para ver a semana). `--texto` imprime no terminal. `--diag` mostra, para uma matéria, cada tópico com o heading que o script escolheu, o conteúdo contado, os cadernos casados e a ação resultante — é o comando para desconfiar de uma recomendação.

Nada é armazenado: cada execução lê o estado atual das notas, do Diario e da grade.

## Como ler

Cada item traz o tópico (nome do checklist VINTEUM), `→` o heading da nota onde ele mora quando o nome difere, o peso, o `dom` e **o motivo**. O motivo é a parte que importa — se ele não bate com o que você sabe do tópico, a recomendação está errada e o `--diag` mostra por quê.

**Ler** — o heading não tem conteúdo escrito (menos de 3 linhas reais, sem contar tracker, link do TEC e tag), ou nem existe heading correspondente. Ordena por peso × lacuna, onde lacuna = (5 − dom) ÷ 5 e `dom 0` conta como lacuna cheia. Erro recente num tópico sem nada escrito **dobra** a prioridade: é o erro que não virou nota. Fica fora da lista o tópico com `dom ≥ 4` ou testado nos últimos 30 dias sem erro — ali o que falta é transcrição, não leitura (isso é [[Cobertura VINTEUM]]).

**Fazer questões** — tem conteúdo escrito e **nenhum caderno desde que foi escrito**: estudado e nunca testado, ou reescrito depois do último teste. Ordena por peso × lacuna × 1,5.

**Revisar** — três gatilhos, nesta ordem:

| Gatilho | Critério | Instrução |
| --- | --- | --- |
| Erro recente | último caderno do tópico, nos últimos 30 dias, com acerto abaixo de 70% | correção escrita depois do erro → refaça questões; acerto abaixo de 60% → releia antes; senão, bateria curta |
| Agenda vencida | `[prox::]` com data passada sob o heading | revisão que o `PY/revisoes.py` agendou |
| Esquecimento | dias desde o último contato (último caderno ou última escrita, o mais recente) ≥ intervalo do `dom` | 7 dias para dom 0–2 · 15 para dom 3 · 30 para dom 4 · 60 para dom 5 |

Os cortes de 60% e 70% são os da [[Fila de reforço]] e do protocolo da grade; a escada 7/15/30/60 segue o protocolo de revisão espaçada da mesma nota.

**Quantos itens por slot** segue a função do slot: S2 (leitura nova) mostra 3 de Ler primeiro; S3 (aprofundamento) mostra 3 de Questões primeiro; S4 (60 min) começa por Revisar e mostra menos itens; S5 equilibra. A partir da semana 14 do ciclo (consolidação) a seção Ler some.

## Mapeamentos que o script assume

- **Direito Tributário** inclui `P2 - Reforma Tributária` (a grade não dá slot próprio à Reforma). **Ciências de Dados** são as quatro notas de Fluência de Dados (mesmo checklist). **Segurança da Informação** é `P2 - Tecnologia da Informação` inteira. **Contabilidade de Custos** é só a seção `# CONTABILIDADE DE CUSTOS` da nota de Avançada, com o checklist próprio dela.
- **Rodízios alternam pela semana do ciclo** (semana 1 começou em 07/09): "ímpares/pares" = semana ímpar/par; o "Rodízio 4" gira Constitucional → Administrativo → Civil → Penal, um por semana. **Essa regra foi deduzida do rótulo, não conferida na planilha** (`Cronograma_SEFAZ_BA_2027.xlsx` não está no vault). Se a regra real for outra, ajuste `RODIZIOS` e `INICIO_CICLO` no topo do script.
- Rótulo novo na grade que o script não conhece aparece com aviso em vermelho no slot — acrescente em `GRADE_PARA_NOTAS`.

## O que este painel erra

> [!warning]- Casamento por palavras, não por significado
> O checklist VINTEUM e os headings das notas foram escritos com vocabulários diferentes, e não há ligação explícita entre eles. O script casa por palavras distintivas do tópico (as que não aparecem em nenhum outro tópico do mesmo checklist), trata singular/plural e masculino/feminino como iguais, reconhece siglas (`DFC`, `BP`, `ITCMD`) e normaliza números de lei (`8.137/90` = `8137/1990`). Mesmo assim erra. Casos conhecidos em 14/09: **"Competências da União"** cai em "Competências para Fiscalização e Tribunal de Contas da União"; **"Definições — diferença entre gastos, despesas, custos e perdas"** não acha "Terminologia Aplicada à Contabilidade de Custos", onde o conteúdo de fato está; **"Jurisprudência em Matéria Constitucional"** cai no `# Jurisprudência` do fim da nota, não nos julgados espalhados sob cada tema. A seta `→` existe para você ver o casamento sem precisar do `--diag`.

> [!warning]- Acerto por tópico só existe quando o caderno lista o erro com contagem
> O Diario guarda `total`/`acertos` por **caderno**, não por assunto. O acerto por tópico vem da linha `- <assunto> — a/t` em `## Erros a revisar` (formato do `/importar-tec`). Assunto listado sem linha de erro conta como 100%. Erro em texto livre, dos cadernos de antes do import, entra como erro sem percentual (`?`). E assunto específico do TEC ("Peculato Mediante Erro de Outrem") só cai num tópico VINTEUM genérico ("Crimes Praticados por Funcionário Público…") quando os nomes compartilham termos — quase nunca.

> [!warning]- "Quando foi escrito" é a data do commit
> O git blame dá a data do commit que trouxe a linha, não o momento em que você escreveu. Commit de recuperação atrasa a data (o mesmo furo documentado no [[S1 - Revisão de ontem]]); conteúdo ainda não commitado conta como hoje. Isso só desloca a fronteira entre "Fazer questões" e "Revisar" em um ou dois dias.

> [!note]- Qual `dom` entra, e por que não o do heading
> Entra o `dom` do checklist (desempenho no TEC). O `[dom::]` da linha `status` de cada heading ficou em 0 como valor neutro em quase todo o vault (ver [[Cobertura VINTEUM]]) e não diferencia nada; o que o script usa do corpo é a **existência de conteúdo**. Em notas sem checklist VINTEUM — Administração e Governança Pública, Administração Geral, Micro e Finanças Públicas, P2 Finanças Públicas — cada heading com tracker vale o mesmo, e a ordem sai só do estado (erro, escrito, testado).

> [!note]- Tags de revisão antigas
> Quase todas as linhas com `[prox::]` estão vencidas desde o fim de agosto. Enquanto `PY/revisoes.py agendar` não voltar a ser usado, esses tópicos aparecem como "revisão agendada vencida" (ex.: Teoria do Crime em Penal). É dado real, só velho.

## O que ele não substitui

Ele decide **dentro** do slot que a grade já decidiu. Qual bloco merece mais slots continua sendo [[Ganho potencial]]; o recall de 24h continua sendo o [[S1 - Revisão de ontem]]; a releitura do resumo inteiro continua sendo a [[Agenda de releitura]].
