---
materia: estatística
tipo: caderno-de-erros
tags:
---
# 📉 Caderno de Erros: [[P1 - Estatística]]

> [!info] Regra de Ouro
> Copie apenas o estritamente necessário. O objetivo não é reescrever a aula, é registrar a "pegadinha" da banca e a lacuna do seu conhecimento.

---

## 🎯 Mapeamento de Pontos Cegos
*(Liste aqui os subtópicos dessa matéria que você percebeu que são o seu "calcanhar de Aquiles" nas baterias do TEC)*
- **Matéria inteiramente nova** — primeiro caderno de Estatística (C02, 25/09/2026): 6 erros em 5 assuntos diferentes, todos dentro de Medidas de Dispersão (desvio em relação à média, desvio médio, variância/desvio padrão, coeficiente de variação, propriedades). Faz tempo que não revisa Estatística — o bloco inteiro precisa de reforço, não só um ponto isolado.
- **Propriedades das Medidas de Dispersão — 2 erros no caderno C02 (25/09/2026):** não aplicou corretamente que somar/subtrair constante não altera variância nem desvio padrão (grupos deslocados) e errou o sistema para achar `a` e `b` de uma transformação linear `Y = aX + b`. Padrão: sabe a regra de cor, mas trava ao aplicá-la num problema com números.

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

### 25/09

> [!question]- 25/09 (mesma captura, sem hora registrada) · Estatística · VUNESP (Pref Campinas 2019, #1028374) — Desvio em relação à média: quadro de frequência
> Considere a tabela-1 e o enunciado seguintes para responder a questão.
>
> A tabela-1 de distribuição de frequência mostra a organização e síntese de 18 dados xᵢ colhidos como amostra para um estudo estatístico, onde a coluna fᵢ é a que registra os valores das frequências, enquanto a coluna (xᵢ − x̄)² contém os valores dos quadrados dos desvios.
>
> Os valores substituídos pelas letras A, B e C na tabela são, respectivamente:
>
> <mark style="background:rgba(163, 67, 31, 0.2)">(A) 0, 16, 0.</mark>
> (B) 4, 4, 4.
> <mark style="background:#affad1">(C) 16, 0, 16.</mark>
> (D) 0, 4, 0.
> (E) 16, 4, 16.
>
> **Marquei:** 🟥 A · **Gabarito:** 🟩 C
>
> > [!success] ✅ Resposta — C (16, 0, 16)
> > Média: x̄ = (1·2 + 3·4 + 5·6 + 7·4 + 9·2) / 18 = 90/18 = <mark style="background:#fff88f">5</mark>. Desvio quadrático de cada linha: A = (1−5)² = 16, B = (5−5)² = 0, C = (9−5)² = 16.
>
> > [!example]- 🧩 Quadro — tabela reconstituída a partir do comentário
> > A tabela-1 original é uma imagem e não veio em texto; estes valores foram reconstituídos a partir da conta do comentário.
> >
> > | xᵢ | fᵢ | (xᵢ−x̄)² |
> > | --- | --- | --- |
> > | 1 | 2 | **A = 16** |
> > | 3 | 4 | 4 |
> > | 5 | 6 | **B = 0** |
> > | 7 | 4 | 4 |
> > | 9 | 2 | **C = 16** |
>
> > [!info] 🔗 Na matéria
> > [[P1 - Estatística#Bloco A: Estatística Descritiva|Bloco A]] — a propriedade da soma dos desvios² em relação à média já está no cofre; não achei trecho literal específico pra grifar (é um cálculo numérico da questão, não texto de lei/norma).
> > **Fonte:** TEC (comentário da questão)

> [!question]- 25/09 (mesma captura, sem hora registrada) · Estatística · VUNESP (Pref Peruíbe 2023, #2430569) — Desvio médio do último trimestre
> A tabela a seguir mostra o comportamento sazonal da receita do Imposto Territorial Rural (ITR), em out/nov/dez de 20X1, 20X2 e 20X3. Em 20X3: outubro R$ 32.700,00 · novembro R$ 25.600,00 · dezembro R$ 22.500,00.
>
> O desvio-médio do último trimestre de 20X3 é de, aproximadamente:
>
> (A) 3.688,89.
> <mark style="background:#affad1">(B) 3.844,44.</mark>
> (C) 3.888,89.
> <mark style="background:rgba(163, 67, 31, 0.2)">(D) 4.269,53.</mark>
> (E) 4.392,67.
>
> **Marquei:** 🟥 D · **Gabarito:** 🟩 B
>
> > [!success] ✅ Resposta — B (R$ 3.844,44)
> > Média do trimestre: (32.700 + 25.600 + 22.500) / 3 = <mark style="background:#fff88f">26.933,33</mark>. Desvio médio = média dos módulos das diferenças de cada mês em relação a essa média: (|32.700−26.933,33| + |25.600−26.933,33| + |22.500−26.933,33|) / 3 = **3.844,44**.
>
> > [!info] 🔗 Na matéria
> > [[P1 - Estatística#Bloco A: Estatística Descritiva|Bloco A]] — a fórmula do desvio absoluto médio (DAM) já está no cofre; não grifado (fórmula genérica, não os valores desta questão).
> > **Fonte:** TEC (comentário da questão)

> [!question]- 25/09 (mesma captura, sem hora registrada) · Estatística · VUNESP (ARSESP 2025, #3768696) — Variância populacional por tabela de frequência
> Uma pesquisa com 100 funcionários de uma empresa investigou o número de dias da semana trabalhados em regime de home office: 1 dia (5 funcionários), 2 dias (5), 3 dias (20), 4 dias (25), 5 dias (45).
>
> Com base nesses dados, o valor da variância populacional do número de dias da semana trabalhados em regime de home office é:
>
> (A) 1,1.
> <mark style="background:#affad1">(B) 1,3.</mark>
> (C) 1,2.
> <mark style="background:rgba(163, 67, 31, 0.2)">(D) 1,4.</mark>
> (E) 1,5.
>
> **Marquei:** 🟥 D · **Gabarito:** 🟩 B
>
> > [!success] ✅ Resposta — B (1,3)
> > Média: x̄ = (1·5 + 2·5 + 3·20 + 4·25 + 5·45) / 100 = 400/100 = 4. Variância populacional = <mark style="background:#fff88f">soma dos desvios² ponderada pelas frequências, dividida por N</mark> = (5·9 + 5·4 + 20·1 + 25·0 + 45·1) / 100 = 130/100 = **1,3**.
>
> > [!info] 🔗 Na matéria
> > [[P1 - Estatística#Medidas de Dispersão|Medidas de Dispersão]] — fórmula σ² = Σ(xᵢ−x̄)²/N, já grifada (N em amarelo, linha do denominador populacional); já estava grifado.
> > **Fonte:** TEC (comentário da questão)

> [!question]- 25/09 (mesma captura, sem hora registrada) · Estatística · VUNESP (Pref Ilhabela 2020, #1620663) — Coeficiente de Variação: o que ele indica
> O Coeficiente de variação (CV) indica:
>
> <mark style="background:#affad1">(A) uma medida de dispersão relativa que é útil ao se comparar o risco de ativos com retornos distintos esperados.</mark>
> <mark style="background:rgba(163, 67, 31, 0.2)">(B) o indicador estatístico mais comum do risco de um ativo que mostra a dispersão em torno do valor esperado.</mark>
> (C) o indicador estatístico mais comum do risco de um ativo que sinaliza a dispersão em torno do retorno esperado.
> (D) o retorno mais provável de um dado ativo.
> (E) um modelo que relaciona probabilidades com os resultados associados.
>
> **Marquei:** 🟥 B · **Gabarito:** 🟩 A
>
> > [!success] ✅ Resposta — A
> > CV = <mark style="background:#fff88f">desvio padrão / média</mark>, expresso em %. É a medida de dispersão **relativa**, usada para comparar a variabilidade de conjuntos com médias ou unidades diferentes (ex.: risco de ativos com retornos esperados distintos) — variância e desvio padrão sozinhos não servem para essa comparação.
> >
> > As opções B e C erram ao chamar o CV de "o indicador mais comum do risco" tout court, sem a ideia de comparação relativa; D e E descrevem outra coisa (retorno esperado e distribuição de probabilidade).
>
> > [!info] 🔗 Na matéria
> > [[P1 - Estatística#Medidas de Dispersão|Medidas de Dispersão]] — definição do CV como medida de dispersão relativa já no cofre, com "relativa" em negrito; já estava com destaque, não precisei regrifar.
> > **Fonte:** TEC (comentário da questão)

> [!question]- 25/09 (mesma captura, sem hora registrada) · Estatística · VUNESP (EsFCEx 2025, #3641655) — Propriedades das medidas de dispersão: grupo deslocado
> Sejam os dados do grupo A = {2, 3, 4, 5, 6} e do grupo B = {5, 6, 7, 8, 9}. É correto afirmar que a variância:
>
> (A) amostral do grupo A é igual à variância amostral do grupo B, e o desvio padrão amostral do grupo A é menor do que o desvio padrão populacional do grupo B.
> <mark style="background:#affad1">(B) amostral do grupo A é igual à variância amostral do grupo B, e o desvio padrão amostral do grupo A é maior do que o desvio padrão populacional do grupo B.</mark>
> (C) populacional do grupo A é maior do que a variância amostral do grupo B, e o desvio padrão amostral do grupo A é igual ao desvio padrão amostral do grupo B.
> (D) populacional do grupo A é menor do que a variância populacional do grupo B, e o desvio padrão amostral do grupo A é igual ao desvio padrão amostral do grupo B.
> <mark style="background:rgba(163, 67, 31, 0.2)">(E) amostral do grupo A é igual à variância populacional do grupo B, e o desvio padrão amostral do grupo A é igual ao desvio padrão amostral do grupo B.</mark>
>
> **Marquei:** 🟥 E · **Gabarito:** 🟩 B
>
> > [!success] ✅ Resposta — B
> > B = A + 3 (grupo B é o A "deslocado" em 3 unidades). Somar uma constante a todos os elementos <mark style="background:#fff88f">não altera a variância nem o desvio padrão</mark>, logo var(B) = var(A) e os desvios padrão são iguais entre si. Além disso, o desvio padrão **amostral** é sempre **maior** que o **populacional** do mesmo conjunto (fator de correção n/(n−1) > 1) — por isso o desvio padrão amostral do grupo A é maior que o desvio padrão populacional do grupo B.
>
> > [!info] 🔗 Na matéria
> > [[P1 - Estatística#Medidas de Dispersão|Medidas de Dispersão]] — as duas regras usadas ("somar constante não altera variância" e "variância/desvio padrão amostral ≥ populacional") já estão no cofre, ambas em negrito; não precisei regrifar.
> > **Fonte:** TEC (comentário da questão)

> [!question]- 25/09 (mesma captura, sem hora registrada) · Estatística · VUNESP (TJ SP 2025, #3751628) — Propriedades das medidas de dispersão: transformação linear de série
> Um algoritmo funciona para séries com média 75 e variância 180. Uma série de teste tem média 84 e variância 245. Para alterar linearmente a série e torná-la apta ao teste, é necessário que cada observação seja:
>
> (A) multiplicada por 13/14 e diminuída de 3.
> <mark style="background:#affad1">(B) multiplicada por 6/7 e adicionada de 3.</mark>
> (C) multiplicada por 6/7 e adicionada de 6.
> (D) multiplicada por 13/14 e diminuída de 5.
> <mark style="background:rgba(163, 67, 31, 0.2)">(E) multiplicada por 11/14 e adicionada de 9.</mark>
>
> **Marquei:** 🟥 E · **Gabarito:** 🟩 B
>
> > [!success] ✅ Resposta — B (×6/7, +3)
> > Transformação Y = aX + b, com X de média 84 e variância 245, buscando Var(Y) = 180 e E[Y] = 75. Pela propriedade da variância, <mark style="background:#fff88f">Var(aX+b) = a²·Var(X)</mark>: 180 = a²·245 → a² = 36/49 → a = 6/7. Pela propriedade da média, E[aX+b] = a·E[X] + b: 75 = 84·(6/7) + b = 72 + b → b = 3.
>
> > [!info] 🔗 Na matéria
> > [[P1 - Estatística#Medidas de Dispersão|Medidas de Dispersão]] — a propriedade "multiplicar por k multiplica a variância por k²" já está no cofre, em negrito; não precisei regrifar.
> > **Fonte:** TEC (comentário da questão)
