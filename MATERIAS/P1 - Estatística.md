---
disciplina: Estatística
bloco: Mat. Fin./Estat./RLM
revisado:
prova: I
peso: 2
pontos: 14
origem: BA 2019 · CE 2026 (com Mat. Financeira e RL)
prioridade: importante
---

# Estatística

## Percentual de cobrança (VINTEUM Fiscal 4.0)

*Fonte: Guia de Estudo Regular Fiscal 4.0 (VINTEUM) — bancas FCC, FGV e CEBRASPE. Mesma tabela em `P2 - Estatística Aplicada.md` (o guia trata como uma disciplina só).*

| Tópico | % |
| --- | --- |
| Probabilidades | 20,1% |
| Regressão | 14,0% |
| Medidas de Posição | 11,6% |
| Distribuições Contínuas | 9,9% |
| Testes de Hipóteses | 9,9% |
| Distribuições Discretas | 9,3% |
| Intervalos de Confiança | 7,6% |

## Checklist por importância (VINTEUM)

- [ ] Probabilidades [dom:: 0] [peso:: 20.1]
- [ ] Regressão [dom:: 3] [peso:: 14.0]
- [ ] Medidas de Posição [dom:: 3] [peso:: 11.6]
- [ ] Distribuições Contínuas [dom:: 0] [peso:: 9.9]
- [ ] Testes de Hipóteses [dom:: 0] [peso:: 9.9]
- [ ] Distribuições Discretas [dom:: 0] [peso:: 9.3]
- [ ] Intervalos de Confiança [dom:: 2] [peso:: 7.6]

> **7 questões · peso 2 · **14 pontos** · 4,3% da nota**
> Prioridade: **importante**

Matéria de **acúmulo lento** — a que mais se beneficia de tempo longo e a que o candidato mais adia por parecer menos urgente que a legislação.

---

> [!info]- Como preencher
> Cada `- [ ]` é um tópico. Ajuste `[dom:: N]` de 0 a 5 ao estudar; acrescente `[rev:: AAAA-MM-DD]` para
> o painel te cobrar. Escreva o conteúdo logo abaixo do cabeçalho do tópico, no formato que quiser.


# Bloco A: Estatística Descritiva

><font color="#00b050">A questão traz dois conceitos fundamentais referentes à amostras e populações:  </font>
- **estatística** é qualquer medida descritiva dos dados coletados de uma _amostra_. Por exemplo, média amostral, variância amostral e mediana amostral são estatísticas;
- **parâmetro** é uma medida de uma _população_: média populacional, variância populacional e mediana populacional são exemplos de parâmetros.

**Correto:** Visualiza a relação (por exemplo, correlação linear) entre dois atributos.

![[Pasted image 20260813143948.png|348]]

**Independentemente da assimetria**, a soma dos desvios quadrados é mínima quando feita com relação à **média aritmética da amostra**. Ou seja, o menor valor de ∑ni=1(xi−m)2 ocorre quando m=x¯.
Assim, independente se moda < mediana < média, a resposta continua sendo a média aritmética.
Vale notar duas outras importantes relações:
- a soma dos desvios **absolutos** é minimizada na **<font color="#f79646"><mark style="background:#fdbfff">mediana</mark></font>**: ∑ni=1|xi−md|
- a soma dos desvios com relação à **<mark style="background:#fff88f">média</mark>** é, por construção, sempre zero: ∑ni=1(xi−x¯)=0.

<center><p align="left"></p>BOX PLOT</center>

![[Pasted image 20260813151710.png|567]]![[Pasted image 20260813151730.png|605]]

***Desvio absoluto médio = basicamente iremos calcular a média e subtrair cada elemento do rol pela média. Como trata do desvio absoluto, iremos considerar os valores em módulo. Basta somá-los e dividir por ‘n’, que é o número de elementos do rol.**
**Média = (5 + 6 + 6 + 7 + 7 + 8 + 8 + 9 + 9 + 10)/10 = 7,5**
**DAM = |5-7,5| + |6-7,5|+ |6-7,5|+ |7-7,5|+ |7-7,5|+ |8-7,5|+ |8-7,5|+ |9-7,5| + |9-7,5| + |10-7,5| / 10 = 0,5 + 1,5 + 1,5 + 0,5 + 0,5 + 0,5 + 0,5 + 1,5 + 2,5 / 10 = 1,3**

## Medidas de Dispersão
- [ ] status [dom:: 0] [peso:: 0]

*Fonte: Estratégia Concursos, "Resumo das Medidas de Dispersão" (ISS-BH) — complementa o Bloco A acima, que já tinha desvio em relação à média e desvio médio, mas não tinha variância, desvio padrão nem coeficiente de variação.*

As medidas de dispersão indicam **o quanto os dados se afastam** de uma medida de tendência central (geralmente a média). Dividem-se em duas famílias, e a diferença entre elas é justamente o que a banca testa com "somar/multiplicar uma constante":

| Dispersão | Medidas | Soma/subtrai constante | Multiplica/divide por k |
| --- | --- | --- | --- |
| **Absoluta** | amplitude, desvio médio, variância, desvio padrão | <mark style="background:#fff88f">não altera</mark> | altera (variância por k², desvio padrão por \|k\|) |
| **Relativa** | coeficiente de variação, variância relativa | altera | <mark style="background:#fff88f">não altera</mark> |

**Amplitude total: A = X_máx − X_mín.** Só usa os dois extremos — não olha o meio da distribuição, por isso é a mais sensível a outlier e a menos informativa das medidas de dispersão.

**Variância — populacional × amostral.** A variância mede a dispersão ao quadrado em torno da média; a pegadinha de prova é sempre o **denominador**:

| | Fórmula | Denominador |
| --- | --- | --- |
| Variância **populacional** (σ²) | σ² = Σ(xᵢ − x̄)² / N | <mark style="background:#fff88f">N</mark> (todo o conjunto) |
| Variância **amostral** (s²) | s² = Σ(xᵢ − x̄)² / (n − 1) | <mark style="background:#fff88f">n − 1</mark> (correção de Bessel) |

Fórmula alternativa (evita calcular cada desvio um a um): Var = [Σ(xᵢ²)/n] − x̄² (média dos quadrados menos quadrado da média). Como n−1 < N, a **variância amostral é sempre ≥ a variância populacional** para o mesmo conjunto de números.

**Desvio padrão** é a raiz quadrada da variância — devolve a dispersão à **mesma unidade dos dados** (a variância fica em unidade²): σ = √σ² (populacional), s = √s² (amostral). Sempre ≥ 0; quanto mais perto de 0, mais os dados se concentram na média.

**Coeficiente de Variação (CV) = (desvio padrão / média) × 100%.** É a medida de dispersão **relativa** — usada quando o enunciado pede para comparar a dispersão de **dois conjuntos com médias ou unidades diferentes**, porque variância e desvio padrão sozinhos não são comparáveis nesse caso (ex.: comparar a variabilidade de salários em reais com a de idades em anos). Leitura informal, mas cobrada como interpretação: CV < 15% = dispersão baixa · 15% a 30% = média · > 30% = alta (dados heterogêneos). Variância relativa = variância / x̄² = CV² (menos cobrada que o CV puro).

> [!tip]- Lupa: o mesmo conjunto de dados, respostas diferentes conforme população ou amostra
> **A ideia em uma frase:** trocar "população" por "amostra" no enunciado muda só o denominador (N vs n−1) — o resto da conta é igual.
>
> **Passo a passo** (conjunto {1, 2, 3, 5, 9}, exemplo ilustrativo Estratégia Concursos):
> 1. Média: x̄ = (1+2+3+5+9)/5 = 4.
> 2. Soma dos desvios ao quadrado: (1−4)² + (2−4)² + (3−4)² + (5−4)² + (9−4)² = 9+4+1+1+25 = 40.
> 3. Se {1,2,3,5,9} é a **população inteira** (N=5): variância = 40/5 = **8**; desvio padrão = √8 ≈ 2,83.
> 4. Se {1,2,3,5,9} é uma **amostra** (n=5, denominador n−1=4): variância = 40/4 = **10**; desvio padrão = √10 ≈ 3,16.
> 5. Coeficiente de variação (usando a versão amostral): CV = (3,16/4) × 100% ≈ 79% — dispersão bem alta para um conjunto tão pequeno e espalhado.
>
> **O erro clássico:** usar N no lugar de n−1 (ou o contrário) porque o enunciado não deixou claro se é população ou amostra. A IBAM costuma marcar isso de forma explícita ("foram coletados dados de uma amostra de..." × "todos os servidores do órgão") — leia essa palavra antes de bater a fórmula, e desconfie de tabelas/situações práticas que só fazem sentido lidas com atenção ao enunciado inteiro, não só aos números.

**Propriedades das medidas de dispersão** (o que a banca testa com "somando/multiplicando uma constante" em todos os valores do conjunto):
- Somar ou subtrair uma constante k de todos os valores: variância e desvio padrão **não mudam** — a dispersão continua a mesma, só desloca a régua toda (a variância olha a distância entre os pontos, que não muda quando todo mundo anda junto).
- Multiplicar ou dividir todos os valores por uma constante k: a variância fica multiplicada por **k²**; o desvio padrão, por **|k|** (não k²) — porque o desvio padrão é a raiz da variância.
- Essas duas regras valem só para as medidas **absolutas**. O coeficiente de variação (relativa) faz o oposto: soma/subtração de constante **altera** o CV (muda a média sem mudar o desvio padrão), e multiplicação/divisão por constante **não altera** (desvio padrão e média mudam na mesma proporção — o k cancela na divisão).

# - Análise Bidimensional
    
### Análise Bidimensional: Introdução, Tabelas de Dupla Entrada, Diagrama de Dispersão
- [ ] status [dom:: 0] [peso:: 2]
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/5957?indice=1&materia=982)
        
### Coeficiente de Correlação Linear entre Dois Conjuntos de Dados
- [ ] status [dom:: 0] [peso:: 2]
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/870?indice=1&materia=982)

*Fonte: Estratégia Concursos, "Resumo sobre Correlação Linear e Regressão" (ISS-BH).*

O **coeficiente de correlação de Pearson (r)** mede a força e o sentido da relação **linear** entre duas variáveis X e Y: **r = Cov(X,Y) / (σ_X × σ_Y)** — a covariância entre as duas, dividida pelo produto dos desvios padrão de cada uma. Sempre entre <mark style="background:#fff88f">-1 e +1</mark>.

| Valor de r | Interpretação |
| --- | --- |
| r = 1 | correlação linear positiva perfeita |
| 0 < r < 1 | correlação positiva (X e Y crescem juntos) |
| r = 0 | sem correlação **linear** (não descarta relação não linear, ex.: parábola) |
| -1 < r < 0 | correlação negativa (um cresce, o outro cai) |
| r = -1 | correlação linear negativa perfeita |

**Propriedades:** somar/subtrair uma constante de X ou Y **não muda** r (desloca a nuvem de pontos, não a forma dela). Multiplicar X ou Y por uma constante positiva **não muda** r; por uma constante **negativa**, r **inverte o sinal** (a força continua a mesma, só o sentido troca).

### Coeficiente de Correlação Ordinal de Spearman
- [ ] status [dom:: 0] [peso:: 2]
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/1969?indice=1&materia=982)

### Regressão Linear Simples
- [ ] status [dom:: 0] [peso:: 14.0]

*Fonte: Estratégia Concursos, "Resumo sobre Correlação Linear e Regressão" (ISS-BH) — tópico "Regressão" do VINTEUM (14,0%, o maior peso individual da matéria) não tinha conteúdo no cofre até agora.*

A regressão linear simples estima **como Y varia em função de X**, ajustando uma reta: **Yᵢ = α + β·Xᵢ + εᵢ**, onde α é o coeficiente **linear** (intercepto, valor de Y quando X=0), β é o coeficiente **angular** (quanto Y varia para cada unidade de X) e εᵢ é o erro/resíduo de cada ponto em relação à reta.

**Método dos mínimos quadrados** — a reta "que melhor ajusta" é a que **minimiza a soma dos quadrados dos resíduos** (as distâncias verticais entre os pontos observados e a reta). Fórmulas dos coeficientes:
- β (angular) = Cov(X,Y) / Var(X) — covariância de X e Y dividida pela variância de X (repare a semelhança com o r de Pearson: aqui a razão não é normalizada pelos dois desvios padrão, só pelo de X).
- α (linear) = ȳ − β·x̄ — a reta sempre passa pelo ponto (x̄, ȳ), a média das duas variáveis.

**Coeficiente de determinação (R²)** — mede **quanto da variação de Y o modelo explica**, de 0 a 1 (ou 0% a 100%): **R² = SQM/SQT**, soma dos quadrados do modelo dividida pela soma dos quadrados totais (SQT = SQM + SQR, sendo SQR a soma dos quadrados dos resíduos — o que o modelo **não** explica). R² = 1 → ajuste perfeito, todos os pontos na reta; R² = 0 → o modelo não explica nada da variação de Y. Numa regressão **simples** (uma só variável X), R² = r² (o quadrado do coeficiente de correlação de Pearson).

> [!tip]- Lupa: β não é o mesmo r — cuidado ao trocar as fórmulas
> **A ideia em uma frase:** r (correlação) é **simétrico** entre X e Y e sempre fica entre -1 e 1; β (coeficiente angular da regressão) **não é simétrico** (depende de qual variável é X e qual é Y) e pode assumir qualquer valor.
>
> **O erro clássico:** usar a fórmula de β (Cov/Var(X)) achando que é r, ou vice-versa — r divide pelos dois desvios padrão (σ_X e σ_Y), β divide só pela variância de X. Também é comum trocar o sinal: se r é negativo, β também é negativo (mesmo sinal sempre, mas magnitudes diferentes).

### Análise Bidimensional: Outros Temas
- [ ] status [dom:: 0] [peso:: 2]
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/5956?indice=1&materia=982)
        
## Medidas de Desigualdade e Concentração
- [ ] status [dom:: 0] [peso:: 2]
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/3337?indice=1&materia=982)
    
## Números Índices
- [ ] status [dom:: 0] [peso:: 2]
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/871?indice=1&materia=982)




____

Tanto o índice de Paasche quanto o de Laspeyres são dados justamente pela divisão do preço da cesta em X2 (ano de interesse) pelo preço da cesta em X0 (ano base).

Para uma comparação adequada, a cesta tem que ser exatamente a mesma. Ou seja, só podemos comparar preços se as cestas tiverem as mesmas quantidades dos mesmos produtos. Só podemos comparar uma cesta com duas maçãs e cinco bananas com outra cesta que também contenha duas maçãs e cinco bananas.
O problema é que as quantidades comercializadas, de cada uma das mercadorias (A, B e C), foram se alterando ao longo dos anos. O que fazer?

**No índice de Laspeyres, adotam-se as quantidades do período base.** *No índice de Paasche adotam-se as quantidades do período de interesse.*

![](https://cdn.tecconcursos.com.br/img/teoria/tome-nota.png)
Índice de Laspeyres: usar as quantidades do período base.

Índice de Paasche: usar as quantidades do período de interesse.

<mark style="background:rgba(163, 67, 31, 0.2)">Nenhum destes dois índices apresenta a propriedade circular.</mark>


![[Captura de Tela 2026-09-02 às 11.07.27.png|752]]



![[Captura de Tela 2026-09-02 às 11.08.37.png|814]]

**ÍNDICE DE PREÇOS DE FISHER**
É desejável que, multiplicando-se um índice de preços pelo correspondente índice de quantidades, obtenhamos o índice relativo de valor.

Já vimos que essa igualdade ocorre quando multiplicamos o relativo de preços pelo relativo de quantidades.
Contudo, essa mesma igualdade não ocorre quando multiplicamos o índice de preços de Paasche pelo índice de quantidade de Paasche.

Também não ocorre quando multiplicamos o índice de preços de Laspeyres pelo índice de quantidade de Laspeyres.

Desse modo, foi criado o índice de Fischer, que é a média geométrica entre os índices de Laspeyres e Paasche. O índice de Fischer supre esta lacuna, deixada pelos índices de Laspeyres e Paasche.

O índice de **preços** de Fischer fica:
![[Captura de Tela 2026-09-02 às 11.10.02.png]]



# Probabilidade
- [ ] status [dom:: 4] [peso:: 20.1]
## Eventos e Espaço Amostral
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/883?indice=1&materia=882)
    
## Problemas Introdutórios de Probabilidade: Eventos Equiprováveis e Abordagem Frequentista
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/885?indice=1&materia=882)
    
## Probabilidade Condicional
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/886?indice=1&materia=882)
    
## Probabilidade da Intersecção
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/887?indice=1&materia=882)

**P(A∩B) = P(A) × P(B|A)** — fórmula geral da interseção para eventos dependentes.

Exemplo (sorteio sem reposição): urna com 2 bolas vermelhas e 3 pretas, duas sorteadas sem reposição. P(1ª vermelha e 2ª preta)?
- P(A) = 2/5 (vermelha na 1ª extração)
- P(B|A) = 3/4 (preta na 2ª, restando 1 vermelha e 3 pretas de 4)
- P(A∩B) = 2/5 × 3/4 = 6/20 = 3/10

⚠️ Sem reposição, a probabilidade da 2ª extração muda conforme o resultado da 1ª — eventos dependentes exigem condicionar (P(B|A)), não multiplicar P(A) por P(B) isolados.

Generalização para n eventos, mesma lógica encadeada:
- três eventos: P(A∩B∩C) = P(A) × P(B|A) × P(C|A,B)
- quatro eventos: P(A∩B∩C∩D) = P(A) × P(B|A) × P(C|A,B) × P(D|A,B,C)

Exemplo (3 eventos): Jorge viaja a trabalho. P(avião) = 0,6 (A); dado que vai de avião, P(escala) = 0,4 (B|A); dado que faz escala, P(escala em JK) = 0,3 (C|A,B).
P(A∩B∩C) = 0,6 × 0,4 × 0,3 = 0,072 = 7,2%
    
## Probabilidade da União
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/889?indice=1&materia=882)
    
## Eventos Independentes e Eventos Mutuamente Excludentes
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/888?indice=1&materia=882)
    
## Probabilidade do Evento Complementar
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/890?indice=1&materia=882)
    
## Teorema da Probabilidade Total
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/892?indice=1&materia=882)
    
## Teorema de Bayes
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/891?indice=1&materia=882)
    
## Cálculo de Probabilidades Usando Análise Combinatória
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/893?indice=1&materia=882)
    
## Cálculo de Probabilidade a Partir de Áreas
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/9328?indice=1&materia=882)

---

# Distribuições Discretas
- [ ] status [dom:: 0] [peso:: 9.3]

*Fonte: Estratégia Concursos, "Resumo das Distribuições Discretas" (ISS-BH) — seção nova; o cofre não tinha nada sobre distribuições de probabilidade além do que está em Probabilidade (acima).*

Variável aleatória **discreta** assume valores **enumeráveis** (contagem: 0, 1, 2, 3…). O que a banca testa, além das fórmulas, é **reconhecer no enunciado qual distribuição se aplica** — a palavra-chave que aparece no texto é a pista.

| Distribuição | Quando usar (palavra-chave do enunciado) | P(X=k) | E(X) | V(X) |
| --- | --- | --- | --- | --- |
| **Bernoulli** | um único ensaio, sucesso/fracasso | P(1)=p, P(0)=q | p | p·q |
| **Binomial** | n ensaios **independentes**, **com reposição**, mesma probabilidade p | C(n,k)·pᵏ·q^(n-k) | n·p | n·p·q |
| **Geométrica** | nº de ensaios **até o 1º sucesso** | q^(k-1)·p | 1/p | q/p² |
| **Hipergeométrica** | seleção **sem reposição** de população **finita** (N itens, S "sucessos") | [C(S,k)·C(N-S,n-k)] / C(N,n) | n·S/N | — |
| **Poisson** | nº de eventos **num intervalo fixo** (tempo/espaço), taxa média λ conhecida, sem n definido | e^(-λ)·λᵏ/k! | λ | λ |
| **Uniforme discreta** | todos os valores de a a b **igualmente prováveis** | 1/(b-a+1) | (a+b)/2 | [(b-a+1)²-1]/12 |

(q = 1-p em todas as linhas que usam q.)

**Poisson como limite da Binomial:** quando n é muito grande e p é muito pequeno (evento raro), mantendo n·p = λ constante, a Binomial se aproxima da Poisson — é por isso que Poisson não tem "número de tentativas" explícito, só a taxa média λ.

> [!tip]- Lupa: qual distribuição usar — o teste da "reposição" e do "intervalo"
> **A ideia em uma frase:** primeiro pergunte "tem número fixo de tentativas ou é uma taxa por intervalo?"; se tem tentativas fixas, pergunte "é com ou sem reposição".
>
> **Passo a passo de decisão:**
> 1. O enunciado fala em **taxa média por intervalo de tempo/espaço** ("em média 3 clientes por hora", "2 defeitos por metro") sem número máximo de ocorrências? → **Poisson**.
> 2. Tem um número fixo de tentativas (n) e cada uma é sucesso/fracasso? Vá para o passo 3.
> 3. As tentativas são **independentes** (com reposição, ou população tão grande que reposição não importa)? → **Binomial**. São **sem reposição** de um grupo pequeno e finito? → **Hipergeométrica**.
> 4. A pergunta é "quantas tentativas até o primeiro sucesso"? → **Geométrica**.
>
> **O erro clássico:** aplicar Binomial num sorteio **sem reposição** de uma amostra pequena (é Hipergeométrica) — quando N é muito maior que n, a diferença entre repor ou não é desprezível e a banca pode aceitar a aproximação binomial, mas se N e n forem próximos, o erro é grosseiro. Outro erro: esquecer que **Poisson tem sempre E(X) = V(X) = λ** — se a questão der médias e variâncias diferentes chamando de Poisson, ou o enunciado está mal formulado ou a resposta é "não é Poisson".

---

# Distribuições Contínuas
- [ ] status [dom:: 0] [peso:: 9.9]

*Fonte: Estratégia Concursos, "Resumo das Variáveis Aleatórias Contínuas" (ISS-BH).*

Variável aleatória **contínua** assume qualquer valor dentro de um intervalo (não dá pra enumerar). Usa **função densidade de probabilidade (f.d.p.)** em vez da função de probabilidade discreta — a f.d.p. nunca é negativa e a **área total sob a curva vale 1 (100%)**. Consequência importante: **P(X = um valor exato) = 0** sempre; só faz sentido calcular P(a < X < b), a área entre dois pontos.

**Uniforme contínua:** f(x) = 1/(b-a) para a≤x≤b (densidade constante — mesma "altura" em todo o intervalo). E(X) = (a+b)/2, V(X) = (b-a)²/12. Probabilidade de um sub-intervalo = proporção do comprimento (ex.: X uniforme em [0,50], P(X>20) = 30/50 = 0,6).

**Exponencial:** f(x) = λ·e^(-λx), x≥0; F(x) = 1 - e^(-λx) (função acumulada). E(X) = 1/λ, V(X) = 1/λ². Modela **tempo até o próximo evento** (fila, falha de equipamento). Liga direto com a Poisson: se o número de eventos por intervalo segue Poisson(λ), o **tempo entre eventos** segue Exponencial(λ) — mesma taxa λ, duas perguntas diferentes (quantos eventos × quanto tempo até o próximo).

**Normal (Gaussiana):** a distribuição contínua mais cobrada em prova. Simétrica em torno da média μ, parametrizada por μ e σ² (ou σ).

**Padronização:** Z = (X - μ) / σ transforma qualquer normal em **normal padrão** N(0,1), a única que está tabelada (é assim que se calcula qualquer probabilidade normal na prova — sempre padroniza primeiro, depois consulta a tabela ou usa o Z dado pelo enunciado).

**Regra empírica (68-95-99,7):** aproximadamente 68% dos dados caem em μ±1σ; 95% em μ±2σ; 99,7% em μ±3σ.

> [!tip]- Lupa: padronizar e ler o resultado (exemplo ilustrativo)
> **A ideia em uma frase:** toda questão de normal se resolve em dois passos — padronizar (achar Z) e depois olhar a tabela (ou usar o Z que a própria questão fornece).
>
> **Passo a passo** (nota média μ=6,5, variância=4; aprovam os 10% com melhor nota):
> 1. Desvio padrão: σ = √variância = √4 = 2 (⚠️ a banca costuma dar **variância**, não desvio padrão — tirar a raiz antes de usar Z).
> 2. Os 10% melhores correspondem ao percentil 90; a tabela normal padrão dá z ≈ 1,28 (arredondado a 1,3 em bancas que só tabelam 1 casa).
> 3. Despadronizar: nota mínima = μ + z·σ = 6,5 + 1,3×2 = **9,1**.
>
> **O erro clássico:** usar variância (σ²) no lugar de desvio padrão (σ) direto na fórmula de Z — Z = (X-μ)/σ, nunca /σ². Outro erro: esquecer que a tabela normal padrão geralmente só dá a área de 0 até Z (metade da curva) — para P(X>valor) ou P(a<X<b) é preciso somar/subtrair 0,5 (metade da curva) conforme o caso, olhando o desenho antes de decidir a conta.

---

# Amostragem e Intervalos de Confiança
- [ ] status [dom:: 0] [peso:: 7.6]

*Fonte: Estratégia Concursos, "Resumo sobre Distribuição Amostral" (ISS-BH), mais fórmulas-padrão de intervalo de confiança.*

**Distribuição amostral da média:** se tiramos várias amostras de tamanho n de uma população com média μ e variância σ², a média de cada amostra (x̄) também é uma variável aleatória, com **E(X̄) = μ** e **Var(X̄) = σ²/n** (população infinita, ou amostragem com reposição) — o **erro padrão** da média é √(σ²/n) = σ/√n. Quanto maior n, menor a dispersão de x̄ em torno de μ.

**Teorema Central do Limite (TCL):** para n **suficientemente grande** (regra prática: n≥30), a distribuição amostral da média se aproxima de uma **Normal**, mesmo que a população original não seja normal. É o TCL que autoriza usar Z (em vez de outra distribuição) em praticamente qualquer teste/IC com amostra grande.

**Distribuição amostral da proporção:** E(p̂) = p, Var(p̂) = p(1-p)/n — mesma lógica da média, aplicada a uma proporção amostral.

**Intervalo de Confiança (IC) para a média:**
- σ **conhecido** (ou n≥30, usando s no lugar de σ pelo TCL): **IC = x̄ ± z_(α/2) · (σ/√n)**
- σ **desconhecido** e n<30 (população normal): **IC = x̄ ± t_(α/2, n-1) · (s/√n)**, com n-1 graus de liberdade

**Margem de erro** = a metade do intervalo = z_(α/2)·(σ/√n) (ou o termo equivalente com t).

**IC para proporção:** p̂ ± z_(α/2) · √[p̂(1-p̂)/n]

**Valores de z tabelados (decorar, caem direto em prova):**

| Nível de confiança | α | z_(α/2) |
| --- | --- | --- |
| 90% | 0,10 | 1,645 |
| 95% | 0,05 | 1,96 |
| 99% | 0,01 | 2,576 |

> [!tip]- Lupa: mais confiança não é de graça — a troca entre confiança e precisão
> **A ideia em uma frase:** aumentar n **encolhe** o intervalo (mais preciso); aumentar o nível de confiança (95%→99%) **alarga** o intervalo (menos preciso) — são efeitos opostos, e a banca gosta de misturar os dois numa mesma questão.
>
> **O erro clássico:** achar que 95% de confiança significa "95% de chance de o parâmetro estar dentro **deste** intervalo calculado". Tecnicamente errado: o parâmetro populacional é **fixo** (não é aleatório); o que varia é o intervalo, que muda a cada amostra nova. A leitura correta (frequentista): se o processo de amostragem fosse repetido muitas vezes, **95% dos intervalos construídos** conteriam o verdadeiro parâmetro. É sutil, mas é exatamente esse tipo de frase que a banca usa para testar (V/F) se o candidato decorou a fórmula sem entender o conceito.

---

# Testes de Hipóteses
- [ ] status [dom:: 0] [peso:: 9.9]

*Fonte: Estratégia Concursos, "Resumo sobre Teste de Hipóteses" (ISS-BH) — seção nova, era o principal ponto de dificuldade relatado.*

**A ideia central:** parte de uma afirmação sobre um parâmetro populacional (**H0**) e usa os dados de uma amostra para decidir se há evidência estatística suficiente para **rejeitá-la**.

**H0 (hipótese nula):** a afirmação testada, assumida verdadeira até prova em contrário — geralmente vem com "=", "≤" ou "≥".
**H1 (hipótese alternativa):** o que se aceita **se** H0 for rejeitada — é a negação de H0, com "≠", "<" ou ">".

**Tipos de teste, conforme H1** (a palavra do enunciado que define o tipo):

| Tipo | H1 | Região crítica |
| --- | --- | --- |
| Bilateral | parâmetro **≠** valor | nas duas pontas da distribuição |
| Unilateral à direita | parâmetro **>** valor | só na cauda direita |
| Unilateral à esquerda | parâmetro **<** valor | só na cauda esquerda |

**Tabela dos dois erros possíveis:**

| | H0 verdadeira | H0 falsa |
| --- | --- | --- |
| **Rejeitar H0** | Erro Tipo I (α) | decisão correta |
| **Não rejeitar H0** | decisão correta | Erro Tipo II (β) |

**α (nível de significância)** = P(erro tipo I) = probabilidade de rejeitar H0 sendo ela verdadeira. Fixado **antes** de olhar a amostra (valores usuais: 5% e 1%).
**β** = P(erro tipo II) = probabilidade de não rejeitar H0 sendo ela falsa. **Potência do teste = 1-β** = probabilidade de rejeitar H0 corretamente quando ela é de fato falsa.

⚠️ α e β **não** têm relação direta simples (não somam 1) — para n fixo, reduzir um tende a aumentar o outro; a forma de reduzir os dois ao mesmo tempo é **aumentar o tamanho da amostra**.

**Estatística de teste para a média** (mesma lógica do IC, "de trás para frente"):
- σ conhecido (ou n≥30, usa s): **Z = (x̄ - μ) / (σ/√n)**
- σ desconhecido e n<30: **t = (x̄ - μ) / (s/√n)**, com n-1 graus de liberdade

**Estatística de teste para proporção:** Z = (p̂ - p) / √[p(1-p)/n]

**p-valor:** probabilidade de obter uma estatística de teste **igual ou mais extrema** que a observada, assumindo H0 verdadeira. Regra de decisão equivalente à comparação com o valor crítico: **p-valor < α → rejeita H0**; **p-valor ≥ α → não rejeita H0**.

**Passo a passo padrão de resolução:**
1. Escrever H0 e H1 a partir do enunciado (a palavra-chave — "igual", "maior", "diferente" — define o tipo de teste).
2. Fixar α (o nível de significância, normalmente dado na questão).
3. Calcular a estatística de teste (Z ou t) com os dados da amostra.
4. Comparar com o valor crítico tabelado (de acordo com α e o tipo de teste) **ou** comparar o p-valor com α.
5. Decidir: estatística dentro da região crítica (ou p-valor < α) → **rejeita H0**. Fora (ou p-valor ≥ α) → **não rejeita H0** — nunca "aceita H0"; é só "não há evidência suficiente para rejeitar".

> [!tip]- Lupa: um teste de hipóteses inteiro, do enunciado à decisão
> **A ideia em uma frase:** o teste é sempre a mesma sequência de 5 passos — só muda se usa Z ou t, e se a região crítica é de um lado só ou dos dois.
>
> **Passo a passo** (exemplo ilustrativo): um órgão afirma que o tempo médio de atendimento é de 10 minutos. Um auditor suspeita que na prática é **maior** que isso. Colhe uma amostra de n=36 atendimentos: x̄=10,8 min, desvio padrão amostral s=2,4 min. Usa α=5%.
> 1. **H0:** μ = 10 · **H1:** μ > 10 → teste **unilateral à direita** (a suspeita é "maior que").
> 2. n=36 ≥ 30 → pelo TCL, usa **Z** mesmo sem conhecer o σ populacional (usa s no lugar de σ).
> 3. Z = (10,8 − 10) / (2,4/√36) = 0,8 / (2,4/6) = 0,8 / 0,4 = **2,0**.
> 4. Valor crítico para α=5%, unilateral à direita: **z_crítico = 1,645** (tabelado — decorar junto com os valores do IC). Z calculado (2,0) > z crítico (1,645) → está dentro da região crítica.
> 5. **Rejeita H0** — há evidência estatística, a 5% de significância, de que o tempo médio de atendimento é maior que 10 minutos.
>
> **O erro clássico:** montar teste bilateral quando o enunciado pede unilateral, ou o contrário — quem decide é a palavra em H1 ("diferente de" → bilateral; "maior/menor que" → unilateral). Segundo erro comum: no teste bilateral, usar z_(α) em vez de **z_(α/2)** no valor crítico (o α se divide entre as duas caudas). Terceiro erro: trocar Z por t (ou o contrário) — decida **antes** de calcular, olhando se σ é conhecido e se n≥30.
>
> **Ponte com IC:** o intervalo de confiança (1-α) em torno do parâmetro corresponde à região de **não rejeição** de um teste **bilateral** com o mesmo α — se o valor de H0 cai **fora** do IC, o teste bilateral equivalente rejeitaria H0. É um atalho útil quando a questão já deu o IC pronto e só pergunta se "rejeitaria H0" para um valor específico.