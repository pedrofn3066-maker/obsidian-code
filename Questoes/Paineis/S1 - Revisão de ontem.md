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

**[▶ Ver o que entrou ontem](obsidian://shell-commands/?vault=vault-ba&execute=s1ontem01)** — ou `Cmd+P` → *Execute: S1 - Revisão de ontem*. Roda `PY/s1-ontem.py` pelo plugin Shell commands e abre a página no navegador; erro do script aparece como notificação no Obsidian. Só funciona no Mac (o iPhone não roda Python).

Os blocos acima dizem em que arquivo você mexeu. Para ver o **texto** que entrou, é preciso git — o Dataview não lê histórico. Use o git pelo *conteúdo*, e o bloco 1 pela *data*: `--since` filtra por data de commit, então um commit de recuperação vai te mostrar, sob a data de ontem, coisa escrita dias antes. Cruze sempre com a tabela do bloco 1 antes de concluir que escreveu algo ontem.

Está empacotado em `PY/s1-ontem.sh`. No Terminal — a aba ao lado da conversa no Claude Code, ou o Terminal.app — cole:

```
sh "$HOME/Documents/vault-ba/PY/s1-ontem.sh"
```

Funciona de qualquer diretório; o script se localiza sozinho. Acrescente `-p` no fim para ver o **texto** que entrou em vez de só a lista de arquivos:

```
sh "$HOME/Documents/vault-ba/PY/s1-ontem.sh" -p
```

Terminal é ruim pra ler prosa longa — monoespaçado, sem quebra de linha decente. Pra leitura de verdade (não só checagem rápida), use `PY/s1-ontem.py`: mesma consulta do `-p` acima, mas monta uma página HTML formatada (parágrafos, listas, tabelas, `[[wikilinks]]`) e abre sozinha no navegador:

```
python3 "$HOME/Documents/vault-ba/PY/s1-ontem.py"
```

Sem argumento — não tem modo lista-só, porque essa versão existe só pra ler o texto. Pra checagem rápida "onde eu mexi" sem sair do terminal, o `.sh` sem `-p` continua sendo o mais rápido.

O script `.sh` já resolve quatro coisas que o comando cru erra: mostra acentos em vez de `L\303\255ngua` (precisa de `core.quotepath=false`), corta o ruído de `.obsidian/` e `Z IMG/`, no modo `-p` tira o plumbing do diff (`diff --git`, `index`, `@@`, linhas removidas) e mostra só o caminho do arquivo + o texto que entrou, e lista no fim o que você escreveu mas **ainda não commitou** — que não aparece em nenhum `git log`, por definição.

> [!note]- Por que não dá pra pedir lista de arquivos e conteúdo de uma vez
> `--name-status` e `-p` são ambos formato de diff, e o `--name-status` vence seja qual for a ordem em que você escreva. Por isso o script escolhe um ou outro em vez de empilhar os dois.
	
## 4. Como rodar os 30 min

1. **Leia só a coluna "Nota"** dos blocos 1 e 2. Não abra nada ainda.
2. Para cada nota, escreva ou fale: *o que eu acrescentei ali ontem?* Falhar em lembrar já é o dado — é o item que precisa voltar.
3. Só então abra e confira.
4. **O passo que quase todo mundo pula:** abra o `Checklist por importância (VINTEUM)` da matéria só pra **conferir o peso** — veja se o que você acrescentou cai num tópico de **peso alto**. Escrever muito num tópico de 4% enquanto um de 21% está com `dom:: 3` é o erro mais caro e mais invisível do sistema — o volume de anotação dá sensação de produtividade sem mover pontuação. **Não edite o `dom` daqui**: esse é o do checklist, calculado uma vez a partir do seu histórico real no TEC — é fato retroativo, não recall de hoje (ver [[Cobertura VINTEUM]]).
5. No corpo da nota, sob o heading que você mexeu, atualize o `[dom:: N]` da linha `- [ ] status [dom:: N] [peso:: N]` se a recuperação mostrou que mudou — esse é o tracker manual, o que é seu de fato. Se a caixa ainda estava desmarcada, marque: ela só indica "esse tópico já foi aberto pra estudo alguma vez", não domínio — marcar aqui não exige ter lembrado tudo.

Não atualize `revisado` da nota por causa do S1 — aquele campo alimenta a [[Agenda de releitura]] e mede esquecimento de resumo inteiro, não de um trecho novo.

## 5. O que o S1 não faz

Ele não substitui a [[Fila de revisão]] nem a [[Agenda de releitura]]. Aquelas duas trabalham em escala de semanas e são movidas por desempenho em questões. O S1 trabalha em escala de 24h e é movido pelo que você **escreveu**. Um conteúdo bem recuperado no S1 ainda vai voltar pela agenda no intervalo dela — recuperar hoje não quita a revisão de daqui a 10 dias.

---

# Registro

Anotação manual dos S1 em que apareceu algum padrão que valha lembrar. Não precisa registrar todo dia — só quando o dia revelou alguma coisa sobre **como** você está estudando, não sobre o conteúdo.

## 2026-09-08 (terça)

**Entrou de fato na terça** (confirmado por `mtime`, não por data de commit): definição de mercadoria (§2º) → LTE-BA · drawback não se aplica a IBS/CBS → Reforma Tributária · Art. 399 CC, mora do devedor → Direito Civil · NBC TA 230 §8 (documentação), A7 (amostragem), NBC TA 540 (estimativas), A9 (especialista) e o bloco SPED — NF-e com cancelamento em 24h, inutilização até o 10º dia, limites da CC-e, mais ECD/ECF → Auditoria.

**Não conta como terça:** Língua Portuguesa (formas nominais, "tão… que"), Cont. Avançada (classificação no BP por intenção) e Direito Tributário (imagem da CF) foram escritos na **segunda (07/09)** e só entraram no commit de recuperação das 19:09 de terça.

**Cadernos da terça** (importados do TEC só em 09/09, por isso o bloco 2 aparecia vazio): 24 questões, 20 acertos, 83%.

| Slot | Matéria | Resultado | `erro_tipo` |
| --- | --- | --- | --- |
| S5 | Auditoria | 9/11 · 82% | desatencao |
| S5 | Direito Civil | 8/10 · 80% | desatencao |
| S2 | Contabilidade Geral | 2/2 | — |
| S2 | Legislação Tributária Estadual | 1/1 | — |

**Três padrões:**

- **O erro foi de desatenção, e anotar conteúdo não é o remédio para isso.** A escrita da terça pareou com os erros topico a tópico — NBC TA 540 e A9 para os dois erros de Auditoria, art. 399 para o erro em "Da Mora". Parece o ciclo virtuoso errar → anotar, mas os dois cadernos estão marcados como `desatencao`, não `desconhecimento`. Se o conteúdo já estava sabido e a questão caiu por leitura apressada, escrever o conteúdo de novo trata o sintoma errado: o remédio é procedimental — reler o enunciado, marcar negativas, desacelerar — não mais anotação. O S1 de hoje reforça: NBC TA 540 voltou de memória, limpo.
- **A grade foi cumprida no papel, não na prática.** S2 é LTE, 90 min, a matéria `crítico` de 75 pontos: recebeu **3 questões** no dia todo (1 de LTE, 2 de Cont. Geral). S5, que era Finanças Públicas, foi ocupado inteiro por Auditoria e Direito Civil — 21 das 24 questões do dia. S3 (Cont. Avançada, 90 min) e S4 (Auditoria, 60 min) não registraram nada. A segunda, em contraste, seguiu a grade à risca.
- **Um erro não virou nota.** "Das Obrigações Alternativas (arts. 252 a 256)", 0/1, é o único erro da terça sem correção escrita em lugar nenhum. Os outros três geraram anotação no mesmo dia.

**Limite do schema, notado aqui:** `erro_tipo` é um campo por **caderno**, mas os dois erros de Auditoria não são do mesmo tipo. No S1 de hoje, NBC TA 540 voltou limpo (compatível com desatenção) e A9 voltou parcial (mais parecido com desconhecimento). O frontmatter não comporta essa distinção; quando ela importar, o lugar dela é a lista "Erros a revisar" da própria nota de caderno.

**Lição de método:** este registro nasceu errado duas vezes. Primeiro atribuiu à terça três notas da segunda, porque foi montado com `git log --since`, que filtra por data de commit — o bloco 1 pegou. Depois concluiu que a terça não teve questões, quando na verdade os cadernos existiam e só não tinham sido lançados. **Bloco 2 vazio não significa "dia sem questões", significa "dia sem registro"** — confira no TEC antes de tirar conclusão sobre o dia.

**Resolvido em 2026-09-09:** o bloco SPED estava solto no fim de `MATERIAS/P1 - Auditoria.md`, fora do tópico "Auditoria Fiscal" a que pertence — o checklist não o contabilizava como progresso. Reaninhado sob `## - Auditoria Fiscal;` (commit `9609869`).
