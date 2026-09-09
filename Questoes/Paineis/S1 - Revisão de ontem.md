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

> [!warning]- Esta tabela subestima o dia
> `file.mtime` é a **última** modificação, não todas. Uma nota que você editou ontem e voltou a editar hoje some daqui — ela conta como "hoje". Para o dia fechado, a tabela é fiel; para o dia corrente, ela vaza. O bloco 3 (git) não tem esse problema.

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

Se vier vazio, ontem foi dia de leitura e anotação, não de questões. Muda o S1: não há erro recente para atacar, então a recuperação é de conteúdo novo — mais frágil, porque nunca foi testado.

## 3. O que você escreveu (não só onde)

Os blocos acima dizem em que arquivo você mexeu. Para ver o **texto** que entrou, é preciso git — o Dataview não lê histórico. No Terminal, na pasta do vault:

```
git log --since=yesterday.midnight --until=today.midnight --name-status --format=">>> %ad %s" --date=format:"%H:%M"
```

E para ler o conteúdo linha a linha, com contexto de onde caiu:

```
git diff @{yesterday} -- MATERIAS/
```

Isso só funciona para o que já foi commitado. Captura de ontem ainda não commitada aparece em `git diff` sem argumento de data.

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

**Entrou:** definição de mercadoria (§2º) → LTE-BA · drawback não se aplica a IBS/CBS → Reforma Tributária · A7 amostragem e NBC TA 230 §8 → Auditoria · NBC TA 540 estimativas e A9 especialista → Auditoria · NF-e (cancelamento 24h, inutilização até o 10º dia, limites da CC-e) e ECD/ECF → bloco SPED da Auditoria · Art. 399 CC (mora) → Direito Civil · formas nominais mantêm transitividade e "tão… que" com vírgula facultativa → Português.

**Três padrões:**

- **O dia inverteu a grade.** Terça é S2 LTE · S3 Cont. Avançada · S4 Auditoria (60 min, o menor slot) · S5 Finanças Públicas. Na prática Auditoria levou 5 blocos, LTE levou 1 linha, Finanças Públicas levou zero. Auditoria vale 15 pontos (`importante`); LTE vale 75 (`crítico`).
- **A pesquisa longa caiu no tópico mais barato.** As ~3h de SPED/NF-e alimentam "Tópicos de Auditoria Fiscal (NF-e e EFD)" — **4,3%**, o último da tabela VINTEUM da matéria. "Testes em Áreas Específicas" (**21,7%**, `dom:: 3`) e "Auditoria Interna e Controle Interno" (**6,6%**, `dom:: 0`) não foram tocados: são, respectivamente, o maior ganho potencial e o maior buraco da disciplina.
- **A anotação mais valiosa do dia custou uma linha.** A definição de mercadoria (ICMS, 15,5%, `dom:: 0`) veio da captura rápida pelo Atalho, não da pesquisa longa. Vale como calibragem: tempo investido e ponto ganho não andam juntos.

**Pendência estrutural:** o bloco SPED em `MATERIAS/P1 - Auditoria.md` está solto no fim da nota, depois de "Utilização do Trabalho de Outros Profissionais", em vez de aninhado sob "## - Auditoria Fiscal;". Como está, o checklist não contabiliza esse conteúdo como progresso no tópico a que ele pertence.
