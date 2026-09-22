---
materia: P2 - Fluência de Dados CD
tipo: caderno-de-erros
tags:
---
# 📉 Caderno de Erros: [[MATERIAS/P2 - Fluência de Dados CD]]

> [!info] Regra de Ouro
> Copie apenas o estritamente necessário. O objetivo não é reescrever a aula, é registrar a "pegadinha" da banca e a lacuna do seu conhecimento.

---

## 🎯 Mapeamento de Pontos Cegos
*(Liste aqui os subtópicos dessa matéria que você percebeu que são o seu "calcanhar de Aquiles" nas baterias do TEC)*
- 
- 

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

- A <font color="#ff0000">regressão</font> tem como objetivos a CESP:
<mark style="background:rgba(240, 200, 0, 0.2)">Controle</mark>
<mark style="background:rgba(240, 200, 0, 0.2)">Estimação</mark>
<mark style="background:rgba(240, 200, 0, 0.2)">Sumarização</mark>
<mark style="background:rgba(240, 200, 0, 0.2)">Predição</mark>

- Os <font color="#ff0000">comentários</font> que adicionamos em nosso arquivo JSON <mark style="background:rgba(240, 200, 0, 0.2)">são incluídos no objeto JSON.</mark> Em outras palavras, os comentários **são tratados como dados.**



# FCC
- #banca/fcc 

# FGV
- #banca/fgv 

- <font color="#ff0000">Errado</font>. A questão inverteu os conceitos nos itens I e II
I. ~~Reuso e redistribuição~~ (Disponibilidade e acesso): os dados precisam estar disponíveis integralmente, devendo estar em um formato conveniente e modificável e sob custo não maior que um custo razoável de reprodução.
II. ~~Disponibilidade e acesso~~ (Reuso e redistribuição): os dados precisam ser fornecidos em condições de reuso e redistribuição, podendo ser recombinados com outros dados.



# OUTRAS BANCAS 
- #banca/outras

---

## 💭 Dúvidas respondidas

*(Dúvidas tiradas com `/tirar-duvida`, com a questão e o apontamento. Uma por callout, a mais nova no fim.)*

> [!question]- 21/09 22:12 · Fluência de Dados (Ferramentas de BI e Visualização de Dados) · FCC (Auditor Fiscal Tributário, Pref J Guararapes) — Ferramenta de BI para análise em tempo real
> #3116008 FCC - 2024 - Auditor Fiscal Tributário (Pref J Guararapes)
> Uma prefeitura, que possui grandes volumes de dados provenientes de várias fontes, busca otimizar a gestão de dados relacionados a serviços públicos, como saúde, educação e transporte. Para realizar análises em tempo real desses dados provenientes de várias fontes essa prefeitura deve usar a ferramenta de Business Intelligence (BI)
> (A) Data Warehouse.
> (B) OLAP (Online Analytical Processing).
> (C) ETL (Extract, Transform, Load).
> (D) Microsoft Access.
> (E) QlikView.
>
> **Marquei:** B · **Gabarito:** E
> **Obs.:** resposta de colegas do TEC — QlikView é BI conhecida por análise associativa, em memória, com dashboards interativos e conexão a diversas fontes; consegue lidar com grandes volumes e se integrar a tecnologias de Big Data.
>
> > [!success] Resposta
> > A pergunta pede uma **ferramenta** de BI, ou seja, um produto pronto para análise em tempo real de várias fontes — é o que o QlikView é. As outras alternativas são conceitos/componentes, não produtos: OLAP é o modelo de análise multidimensional (o "como"), Data Warehouse é o repositório dos dados, ETL é o processo de extração/transformação/carga — nenhum deles é, sozinho, "a ferramenta" que a prefeitura contrataria. Access (D) é SGBD de uso pessoal, não ferramenta de BI para grande volume.
> >
> > **Pegadinha:** a banca troca o componente técnico (OLAP, DW, ETL) pelo produto final (QlikView, Power BI, Tableau).
> >
> > **Fonte:** cofre `MATERIAS/P2 - Fluência de Dados BD.md:297` (Business Intelligence e Analytics) e `:180` (OLAP). O nome "QlikView" como exemplo de ferramenta não está no cofre; a distinção conceito × ferramenta é do professor/análise, não do cofre.
