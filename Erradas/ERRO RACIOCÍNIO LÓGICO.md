---
materia: raciocínio lógico
tipo: caderno-de-erros
tags:
---
# 📉 Caderno de Erros: [[P1 - Raciocínio Lógico]]

> [!info] Regra de Ouro
> Copie apenas o estritamente necessário. O objetivo não é reescrever a aula, é registrar a "pegadinha" da banca e a lacuna do seu conhecimento.

---

## 🎯 Mapeamento de Pontos Cegos
*(Liste aqui os subtópicos dessa matéria que você percebeu que são o seu "calcanhar de Aquiles" nas baterias do TEC)*
- **Análise combinatória — 2 erros no caderno C02 RLOG (01/10/2026):** #3912759 (comitê de 4 entre 11: combinação, ordem não importa) e #3732047 (senha com grupos juntos: arranjo nas letras e símbolos, 3! entre os blocos). Os dois são decidir se a ordem conta. Não há heading de combinatória em `P1 - Raciocínio Lógico`: falta absorver.
- **Probabilidade — 2 erros no mesmo caderno (01/10/2026):** #3178505 (sem reposição, "não vermelha" como soma de dois caminhos) e #3732048 (probabilidade total como média ponderada). Em `P1 - Estatística`, a Intersecção está escrita (linha 238) e o Teorema da Probabilidade Total está só como heading (linha 266).

---

## ❌ Registro de Erros (TEC Concursos)

*(Copie e cole o modelo abaixo para cada nova questão errada)*

> [!bug] TEC: Q[Número] - [Banca]
> **Onde caí:** *(Descreva rapidamente por que errou)*
> **A Regra:** *(A explicação direta para não errar mais)* `#tec/erro`
> **Revisão Ativa:** [Pegadinha/Conceito da Questão] :: [A Regra Certa] 


---

# CEBRASPE
- #banca/cebraspe 

# FCC
- #banca/fcc 

# FGV
- #banca/fgv 

# OUTRAS BANCAS 
- #banca/outras

---

## 💭 Dúvidas respondidas

*(Dúvidas tiradas com `/tirar-duvida`, com a questão e o apontamento. Uma por callout, a mais nova no fim.)*

### 01/10

> [!question]- 01/10 (mesma captura, sem hora registrada) · Raciocínio Lógico · IBAM (Fiscal de Tributos, Pref. Cachoeiras de Macacu, 2024) — Probabilidade sem reposição: 1ª não vermelha e 2ª preta
> Em uma caixa foram colocadas cinco bolas vermelhas, três bolas brancas e duas bolas pretas.
>
> Rodolfo retira dessa caixa, de forma consecutiva e sem reposição, duas bolas. A probabilidade de que a primeira não seja vermelha e de que a segunda seja preta está mais próxima de:
>
> (A) 5%
> <mark style="background:#affad1">(B) 7%</mark>
> <mark style="background:rgba(163, 67, 31, 0.2)">(C) 11%</mark>
> (D) 15%
>
> **Marquei:** 🟥 C · **Gabarito:** 🟩 B
>
> > [!success] ✅ Resposta — B: 4/45 ≈ 8,9%, o mais próximo é 7%
> > "1ª **não vermelha**" abre dois caminhos: <mark style="background:#fff88f">1ª branca e 2ª preta</mark>, ou 1ª preta e 2ª preta. Sem reposição, o total cai de 10 para 9 bolas.
> >
> > **Caso 1:** 3/10 × 2/9 = <span class="g-num">6/90</span> = 1/15. **Caso 2:** 2/10 × <span class="g-num">1/9</span> = 2/90 = 1/45 (a 1ª preta tira uma das duas pretas, sobra 1). Soma: 6/90 + 2/90 = 8/90 = **4/45 ≈ 8,9%**.
> >
> > **(C)** 11% é 10/90: sai se, no caso 2, você mantém 2 pretas para a 2ª retirada (2/10 × 2/9 = 4/90), o que é um erro provável, mas o TEC não mostra a sua conta.
>
> > [!warning] ⚠️ Pegadinha da banca
> > "Não vermelha" não é uma cor: junta branca e preta, e a preta da 1ª retirada **sai da urna** antes da 2ª. A alternativa pede "mais próxima de", então a resposta (8,9%) não aparece exata.
>
> > [!info] 🔗 Na matéria
> > [[P1 - Estatística#Probabilidade da Intersecção]] — P(A∩B) = P(A) × P(B|A) e o aviso de que, sem reposição, a 2ª extração depende da 1ª (linha 238). Já estava escrito; o caso de "1ª não vermelha" como soma de dois caminhos não está. Nada grifado.
> > **Fonte:** cofre `MATERIAS/P1 - Estatística.md:238` · comentário do TEC · TEC #3178505

> [!question]- 01/10 (mesma captura, sem hora registrada) · Raciocínio Lógico · VUNESP (Analista Técnico Científico, MPE SP, 2025) — Teorema da Probabilidade Total
> Considere que A e B são eventos de um determinado espaço amostral. A probabilidade de ocorrer o evento A é de 1/3. A probabilidade de ocorrer o evento B, dado que o evento A ocorreu, é de 2/5. A probabilidade de ocorrer o evento B, dado que o evento A não ocorreu, é de 3/4. A probabilidade de ocorrer o evento B é um valor entre:
>
> <mark style="background:#affad1">(A) 60% e 70%</mark>
> (B) 30% e 40%
> (C) 40% e 50%
> (D) 50% e 60%
> <mark style="background:rgba(163, 67, 31, 0.2)">(E) 70% e 80%</mark>
>
> **Marquei:** 🟥 E · **Gabarito:** 🟩 A
>
> > [!success] ✅ Resposta — A: P(B) ≈ 63%
> > <mark style="background:#fff88f">P(B) = P(B|A)·P(A) + P(B|Ā)·P(Ā)</mark>, com P(Ā) = 1 − 1/3 = <span class="g-num">2/3</span>.
> >
> > P(B) = 2/5 × 1/3 + 3/4 × 2/3 = 2/15 + 1/2 = 4/30 + 15/30 = **19/30 ≈ 63,3%**.
> >
> > **(E)** 70–80% não sai de um erro que o TEC mostre; o ponto é pesar cada condicional pela probabilidade do evento que a condiciona (1/3 e 2/3), em vez de usar uma delas pura (3/4 = 75% cai em E).
>
> > [!tip] 💡 Macete
> > Probabilidade total = **média ponderada** das condicionais; os pesos (P(A) e P(Ā)) somam 1, e o resultado fica entre 2/5 e 3/4 (40% e 75%), mais perto de 3/4 porque Ā pesa 2/3.
>
> > [!info] 🔗 Na matéria
> > [[P1 - Estatística#Teorema da Probabilidade Total]] — heading existe na linha 266, mas só traz o link do TEC; **não está no cofre**.
> > **Fonte:** comentário do TEC (lei da probabilidade total) · (sem fonte no cofre) · TEC #3732048

> [!question]- 01/10 (mesma captura, sem hora registrada) · Raciocínio Lógico · IBAM (Auditor Fiscal de Tributos Municipais, Pref. Mauá, 2026) — Combinação: comitê de 4 entre 11, ordem não importa
> Um comitê acadêmico precisa ser formado escolhendo exatamente 4 professores entre um grupo de 11 docentes qualificados, todos com a mesma probabilidade de seleção. O regulamento estabelece que a ordem dos escolhidos nao influencia o resultado final da composição. Quantos comitês distintos podem ser formados nessas condições?
>
> <mark style="background:rgba(163, 67, 31, 0.2)">(A) 286</mark>
> (B) 220
> <mark style="background:#affad1">(C) 330</mark>
> (D) 462
>
> **Marquei:** 🟥 A · **Gabarito:** 🟩 C
>
> > [!success] ✅ Resposta — C: 330
> > "A ordem **não** influencia" = <mark style="background:#fff88f">combinação</mark>: C(11,4) = 11! / (4! × 7!) = (11 × 10 × 9 × 8) / (4 × 3 × 2 × 1) = 7.920 / 24 = <span class="g-num">330</span>.
> >
> > **(A)** 286 não é C(11,4); conferir o cancelamento do 7! e a divisão por 4! = 24. **(B)** 220 e **(D)** 462 também não correspondem ao enunciado.
>
> > [!tip] 💡 Macete
> > Ordem **não** importa → combinação (divide por k!). Ordem importa → arranjo (não divide). Todos os elementos, só trocando de lugar → permutação.
>
> > [!info] 🔗 Na matéria
> > Análise combinatória **não está no cofre**: `P1 - Raciocínio Lógico` não tem heading de combinatória ou contagem, e `P1 - Estatística` só traz "Cálculo de Probabilidades Usando Análise Combinatória" (linha 272), vazio.
> > **Fonte:** comentário do TEC (C(n,p)) · (sem fonte no cofre) · TEC #3912759

> [!question]- 01/10 (mesma captura, sem hora registrada) · Raciocínio Lógico · VUNESP (Analista Técnico Científico, MPE SP, 2025) — Princípio da contagem: senha com grupos juntos
> A senha para abertura de um cofre deve ser formada por 7 caracteres. Desses caracteres, 2 devem ser letras distintas do alfabeto, escolhidas de A a E, 2 devem ser símbolos distintos, dentre quatro disponíveis, e 3 devem ser algarismos escolhidos de 1 a 5, podendo ou não ser repetidos. Os caracteres de cada um desses grupos (de letras, de símbolos e de algarismos) devem estar juntos, mas os grupos podem ocorrer em qualquer ordem. Com essas condições, o número de senhas diferentes que podem ser formadas está no intervalo
>
> <mark style="background:rgba(163, 67, 31, 0.2)">(A) 61.000 e 121.000.</mark>
> (B) 181.000 e 241.000.
> (C) 241.000 e 301.000.
> <mark style="background:#affad1">(D) 121.000 e 181.000.</mark>
> (E) 31.000 e 61.000.
>
> **Marquei:** 🟥 A · **Gabarito:** 🟩 D
>
> > [!success] ✅ Resposta — D: 180.000 senhas
> > Multiplique as escolhas de cada grupo e a ordem dos três grupos: letras 5 × 4 = <span class="g-num">20</span> · símbolos 4 × 3 = <span class="g-num">12</span> · algarismos 5 × 5 × 5 = <span class="g-num">125</span> · ordem dos grupos 3! = <span class="g-num">6</span>. Total: 20 × 12 × 125 × 6 = **180.000**.
> >
> > **(A)** 61.000 a 121.000: um valor desse intervalo sai, por exemplo, se um grupo for tratado como combinação (C(5,2) = 10 no lugar de 5 × 4 = 20 dá 90.000), mas o TEC não mostra a sua conta. Numa senha, a **posição** de cada caractere conta; então as letras e os símbolos distintos usam arranjo (ordem importa), e só os algarismos admitem repetição.
>
> > [!example]- 🧩 Quadro — cada grupo da senha
> > | Grupo | Regra | Contagem |
> > | --- | --- | --- |
> > | 2 letras (A a E) | distintas, ordem importa | 5 × 4 = 20 |
> > | 2 símbolos (4 disponíveis) | distintos, ordem importa | 4 × 3 = 12 |
> > | 3 algarismos (1 a 5) | podem repetir | 5 × 5 × 5 = 125 |
> > | ordem dos 3 grupos | blocos juntos, em qualquer ordem | 3! = 6 |
>
> > [!warning] ⚠️ Pegadinha da banca
> > "Devem estar juntos" transforma cada grupo em um bloco, e os **blocos** é que se permutam (3!), em vez dos 7 caracteres (7!). Quem ignora a ordem dos grupos (×6) ou usa combinação nos grupos cai bem abaixo de 180.000.
>
> > [!info] 🔗 Na matéria
> > Análise combinatória **não está no cofre** (ver a entrada de #3912759, no mesmo caderno).
> > **Fonte:** comentário do TEC (princípio multiplicativo e permutação simples) · (sem fonte no cofre) · TEC #3732047
