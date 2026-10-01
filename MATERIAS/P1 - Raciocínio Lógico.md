---
disciplina: Raciocínio Lógico
bloco: Mat. Fin./Estat./RLM
revisado:
prova: I
peso: 2
pontos: 14
origem: BA 2019 · CE 2026 (com Mat. Financeira e RL)
prioridade: importante
---

# RACLOG

## Percentual de cobrança (VINTEUM Fiscal 4.0)

*Fonte: Guia de Estudo Regular Fiscal 4.0 (VINTEUM) — bancas FCC, FGV e CEBRASPE. Disciplina "Raciocínio Lógico-Matemático" no guia.*

| Tópico | % |
| --- | --- |
| Equivalências Lógicas | 15,0% |
| Associação de Informações | 8,2% |
| Raciocínio Crítico | 8,0% |
| Tabela Verdade das Proposições Compostas | 7,4% |
| Sequências de Números, Figuras, Letras e Palavras | 6,6% |
| Conjuntos e suas operações, diagramas | 6,5% |
| Argumentos — Métodos Decorrentes da Tabela Verdade | 6,0% |
| RL envolvendo problemas matemáticos | 6,0% |
| Orientação no Plano, no Espaço e no Tempo | 5,7% |
| Porcentagem | 5,2% |
| Proporções. Grandezas Proporcionais | 5,1% |

## Checklist por importância (VINTEUM)

- [ ] Equivalências Lógicas [dom:: 3] [peso:: 15.0]
- [ ] Associação de Informações [dom:: 3] [peso:: 8.2]
- [ ] Raciocínio Crítico [dom:: 4] [peso:: 8.0]
- [ ] Tabela Verdade das Proposições Compostas [dom:: 2] [peso:: 7.4]
- [ ] Sequências de Números, Figuras, Letras e Palavras [dom:: 3] [peso:: 6.6]
- [ ] Conjuntos e suas operações, diagramas [dom:: 0] [peso:: 6.5]
- [ ] Argumentos — Métodos Decorrentes da Tabela Verdade [dom:: 2] [peso:: 6.0]
- [ ] RL envolvendo problemas matemáticos [dom:: 0] [peso:: 6.0]
- [ ] Orientação no Plano, no Espaço e no Tempo [dom:: 0] [peso:: 5.7]
- [ ] Porcentagem [dom:: 0] [peso:: 5.2]
- [ ] Proporções. Grandezas Proporcionais [dom:: 0] [peso:: 5.1]


Matéria de **acúmulo lento** — a que mais se beneficia de tempo longo e a que o candidato mais adia por parecer menos urgente que a legislação.

---

> [!info]- Como preencher
> Cada `- [ ]` é um tópico. Ajuste `[dom:: N]` de 0 a 5 ao estudar; acrescente `[rev:: AAAA-MM-DD]` para
> o painel te cobrar. Escreva o conteúdo logo abaixo do cabeçalho do tópico, no formato que quiser.


**Bloco A**

### - Lógica de Proposição e Lógica de Argumentação.
- [ ] status [dom:: 0] [peso:: 2] [prova:: 3]

**1.4 Sentenças Abertas e Fechadas**

- **Sentença fechada** — já pode ser classificada como verdadeira ou falsa (ex.: 3 + 8 = 11 → falsa).
- **Sentença aberta** — contém incógnita; não pode ser julgada V/F até que o valor seja atribuído (ex.: x + 4 = 12).

**1.5** **Tabela Verdade**

|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|p|q|~p|p ^ q|p v q|p  ➜ q|p ⇿ q|p **v** q|
|V|V|F|V|V|V|V|F|
|V|F|F|F|V|F|F|V|
|F|V|V|F|V|V|F|V|
|F|F|V|F|F|V|V|F|

> [!example]- Prova anterior: IBAM 2026 · Guarulhos · Q19 (gab. A · preliminar) e IBAM 2025 · Mauá · Q13 (gab. A · preliminar)
> **Trecho usado:** "Tabela Verdade: p, q, ~p, p ^ q, p v q, p ➜ q, p ⇿ q"
> **Q19 (Guarulhos, 2026) — como cobrou:** conceito — com P verdadeira e Q falsa, pede o valor de "(P ^ ¬Q) v (¬P ^ Q)". A certa é "(A) O valor lógico é verdadeiro, pois a primeira conjunção é verdadeira"; a "(B)" diz "falso, pois P e Q possuem valores lógicos diferentes" e a "(C)", "falso, pois a disjunção exige que as duas conjunções sejam verdadeiras".
> **Q13 (Mauá, 2025) — como cobrou:** conceito — quatro afirmações sobre quando cada proposição composta é falsa ou verdadeira, com p = "O sistema foi atualizado" e q = "O relatório foi validado". Gab. A: V, F, V, V. Por exemplo, "A proposição p → q é falsa quando p é verdadeira e q é falsa" (V).
> **Lastro:** Q19: PDF p. 10 · [[IBAM 2026 - Guarulhos - Auditor Fiscal VI Manhã#Q19]] · Q13: PDF p. 3 · [[IBAM 2025 - Mauá - AFTM#Q13]]

> [!tip]- Lupa de prova: (P ^ ¬Q) v (¬P ^ Q) é o ou exclusivo
> **O padrão:** dá P e Q com valores diferentes (P verdadeira, Q falsa) e pede o valor de (P ^ ¬Q) v (¬P ^ Q); a composta só vale quando P e Q diferem, ou seja, é a disjunção exclusiva (a coluna p v q em negrito da tabela). (padrão de 1 prova, não confirmado)
> **A armadilha:** "(B) O valor lógico é falso, pois P e Q possuem valores lógicos diferentes" tem premissa verdadeira (P e Q de fato diferem) e conclusão trocada; "(C) O valor lógico é falso, pois a disjunção exige que as duas conjunções sejam verdadeiras" trata a disjunção como se fosse conjunção.
> **Como resolver:** monte a linha da tabela com P = V e Q = F: ¬Q = V, então P ^ ¬Q = V; ¬P = F, então ¬P ^ Q = F. Pela tabela, a disjunção p v q é V se ao menos uma das duas for V (a conjunção p ^ q é que exige as duas), logo V v F = V.

<mark>Número de linhas da tabela verdade = 2ⁿ</mark>, onde n é a quantidade de proposições simples **diferentes** (não importa se se repetem na fórmula).

**Negação da Condicional**:

 >**~(P→Q)** **=** **P ^~Q** 
  Mantém a primeira **E**negue a segunda (regra do MANÉ)
 ”se tenho febre então não vou trabalhar”.
 B: tenho febre e vou trabalhar

**Condição necessária e Suficiente**
**❗****Atenção**, você deve identificar qual proposição simples é a suficiente e qual é a necessária: ⚠️ **Bancas já fizeram essa cobrança.**
**Se** **eu for à festa,** **então** **ficarei solteiro” (p****→→****q)**
- **p** é condição **suficiente** para **q;**
- **q** é condição **necessária** para **p.**
**⚠️ Quando houver o "Se...então..." fica fácil identificar a proposição suficiente:**
**S**uficiente: **S**e eu for à festa...

>O quantificador **TODOS** se relaciona a uma condição suficiente e o quantificador **NENHUM** se relaciona a uma condição suficiente para a negação
- Todo A é B : _A → B_
- Nenhum A é B: _A → ~ B_

**Negação de Quantificadores**
- <mark class="prova" style="background:rgba(0,170,170,0.28)">**Todo** se nega por **Algum / Existe um / Pelo menos um** (nunca por "nenhum")</mark> — nega-se o quantificador **e** o predicado.

> [!example]- Prova anterior: IBAM 2026 · Bragança Paulista · Q11 (gab. D · oficial)
> **Trecho usado:** "Todo se nega por Algum / Existe um / Pelo menos um (nunca por "nenhum")"
> **Como cobrou:** conceito — pede a negação de "Todos os contratos analisados apresentaram conformidade documental". A certa é "(D) Ao menos um contrato analisado não apresentou conformidade documental"; "(A) Nenhum dos contratos analisados apresentou conformidade documental" é a troca clássica.
> **Lastro:** Caderno tipo 3, p. 7 · [[IBAM 2026 - Bragança Paulista - AFTM Jr#Q11]]

Ex.: "Todo funcionário daquela loja é atencioso" → "Existe pelo menos um funcionário daquela loja que não é atencioso."

Ex. (quantificador + disjunção exclusiva): "Todas as empresas têm filiais no Brasil ou no exterior" (universal afirmativa, disjunção exclusiva) → negação: "Existe empresa que tem filial no exterior se, e somente se, tem filial no Brasil" (particular negativa; a negação da disjunção exclusiva vira bicondicional).

**1.6 Equivalências Lógicas  Fundamentais**
- <mark class="prova" style="background:rgba(0,170,170,0.28)">_p → q_ _≡_ _~q →_ _~__p_ (Contrapositiva)</mark>
- <mark class="prova" style="background:rgba(0,170,170,0.28)">_p → q_ _≡_ _~__p ∨ q_ (Transformação da condicional em disjunção inclusiva)</mark>
- _p ∨ q_ _≡_ _~__p → q_ (Transformação da disjunção inclusiva em condicional)
- _p ↔ q_ _≡_ _(p → q) ∧ (q → p)_ (Transformação da bicondicional em condicional/conjunção)

> [!example]- Prova anterior: IBAM 2026 · Guarulhos · Q20 (gab. C · preliminar)
> **Trecho usado:** "p → q ≡ ~q → ~p (Contrapositiva); p → q ≡ ~p ∨ q (Transformação da condicional em disjunção inclusiva)"
> **Como cobrou:** troca de termo — cinco afirmações sobre P → Q: I "é equivalente a ¬P v Q" e II "é equivalente a ¬Q → ¬P" (certas); III "A proposição ¬P → ¬Q é equivalente a P → Q" e IV "P → Q é equivalente a Q → P" (erradas: trocam a contrapositiva por inversa e recíproca); V "A negação de P → Q é equivalente a P ^ ¬Q" (certa, ver 1.7 "Negação da condicional"). A certa é "(C) I, II e V, apenas".
> **Lastro:** PDF p. 10 · [[IBAM 2026 - Guarulhos - Auditor Fiscal VI Manhã#Q20]]

> [!tip]- Lupa de prova: contrapositiva não é inversa nem recíproca
> **O padrão:** a prova lista formas de P → Q e pede quais são equivalentes: valem a disjunção (¬P v Q), a contrapositiva (¬Q → ¬P) e a negação (P ^ ¬Q). (padrão de 1 prova, não confirmado)
> **A armadilha:** "¬P → ¬Q é equivalente a P → Q" (inversa) e "P → Q é equivalente a Q → P" (recíproca) trocam a contrapositiva por formas que só negam ou só invertem a ordem.
> **Como resolver:** confira cada afirmação com a lista de 1.6: só valem ~q → ~p (nega e inverte os dois lados) e ~p ∨ q; ¬P → ¬Q mantém a ordem e Q → P não nega nada, então nenhuma das duas aparece ali. A nota ainda não diz em palavras que inversa e recíproca não são equivalentes à condicional (lacuna registrada na prova resolvida).

**Aplicação:** "Se todas as bancas estão no lugar correto, então não há motivo para reclamação" (todo B → ¬M) ≡ M → algum B ≡ algum ¬B ∨ ¬M → "Pelo menos uma banca não está no lugar correto ou não há motivo para reclamação."

> [!warning]- Pendência de autoria
> A captura original tem "M → ALGUM B" no passo intermediário (sem negar B), o que não bate com o resultado final "ALGUM ¬B v ¬M". Conferir a derivação.

**1.7** **Negação de proposições**
- _~(~p)_ _≡_ _p_ (Dupla negação da proposição simples)
- _~ (__p ^ q)_ _≡_ _~__p ∨ ~q_ (Negação da conjunção)
- _~ (__p ∨ q)_ _≡_ _~__p ^ ~q_ (Negação da disjunção inclusiva)
- <mark class="prova" style="background:rgba(0,170,170,0.28)">_~(p → q)_ _≡_ _p ^ ~q_ (Negação da condicional)</mark>
- _~(p ↔ q)_ _≡_ _p v q_ (Negação da bicondicional)
- _~(p v q)_ _≡_ _p ↔ q_ (Negação da disjunção exclusiva)



**Bloco B**

### - Sequência de Números, Figuras, Letras;
- [ ] status [dom:: 0] [peso:: 2]
### - Orientação no Plano/Espaço/Tempo;
- [ ] status [dom:: 0] [peso:: 2]
### - Datas e Calendários;
- [ ] status [dom:: 0] [peso:: 2]
### - Problemas diversos de lógica;
- [ ] status [dom:: 0] [peso:: 2]
### - Progressão Aritmética e Progressão Geométrica.
- [ ] status [dom:: 0] [peso:: 2]

**Bloco C**

### - Problemas Aritméticos;
- [ ] status [dom:: 0] [peso:: 2]
### - Teoria dos Conjuntos;
- [ ] status [dom:: 0] [peso:: 2]
### - Porcentagem;
- [ ] status [dom:: 0] [peso:: 2]
### - Regra de 3;
- [ ] status [dom:: 0] [peso:: 2]
### - Proporcionalidade.
- [ ] status [dom:: 0] [peso:: 2]

**Bloco D**

### - Equações e Sistemas Lineares;
- [ ] status [dom:: 0] [peso:: 2]
### - Geometria Plana e Espacial;
- [ ] status [dom:: 0] [peso:: 2]
### - Matrizes;
- [ ] status [dom:: 0] [peso:: 2]
### - Plano Cartesiano.
- [ ] status [dom:: 0] [peso:: 2]
