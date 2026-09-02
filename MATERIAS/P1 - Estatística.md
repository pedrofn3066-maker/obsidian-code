---
disciplina: Estatística
prova: I
peso: 2
pontos: 14
origem: "BA 2019 · CE 2026 (com Mat. Financeira e RL)"
prioridade: importante
---

# Estatística

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

# - Análise Bidimensional
    
### Análise Bidimensional: Introdução, Tabelas de Dupla Entrada, Diagrama de Dispersão
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/5957?indice=1&materia=982)
        
### Coeficiente de Correlação Linear entre Dois Conjuntos de Dados
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/870?indice=1&materia=982)
        
### Coeficiente de Correlação Ordinal de Spearman
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/1969?indice=1&materia=982)
        
### Análise Bidimensional: Outros Temas
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/5956?indice=1&materia=982)
        
## Medidas de Desigualdade e Concentração
(https://www.tecconcursos.com.br/aulas/materias/61/assuntos/3337?indice=1&materia=982)
    
## Números Índices
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


