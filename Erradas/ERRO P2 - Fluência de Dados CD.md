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
- **DAMA-DMBOK (governança e qualidade de dados): 6 erros em 29/09, todos de conteúdo.** Misturei itens da mesma família: categoria × dimensão (intrínseca/contextual/representacional/acessibilidade × acurácia/completude), MAR × MNAR, governança centralizada × compartilhada × colegiada, disponibilidade × performance, Integração × Dados Mestres, accuracy × consistency. Estudar por **quadro comparativo** e por pergunta-chave de cada item.
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

### 21/09

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

### 29/09

> [!question]- 29/09 (mesma captura, sem hora registrada) · Fluência de Dados (Governança e Qualidade de Dados) · FGV (Analista Legislativo, ALEGO, 2026) — Categorias da qualidade de dados
> #3822377 FGV - 2026 - Analista Legislativo (ALEGO)
> A importância da qualidade dos dados é um dos fundamentos da Ciência da Dados, é essencial nos projetos desenvolvidos na ALEGO. Tais características são bem delineadas e classificadas na literatura e, em essência, servem de indicadores para avaliar quais conjuntos de dados são importantes ou não para um determinado estudo.
>
> A classificação das características básicas da qualidade de dados são, respectivamente,
>
> (A) <mark style="background:#affad1">intrínseca, contextual, representacional e acessibilidade, apenas.</mark>
> (B) encontrável, acessível, interpolável e reusável, apenas.
> (C) contextualização, completude e acurácia, apenas.
> (D) consistência, singularidade e relevância, apenas.
> (E) <mark style="background:rgba(163, 67, 31, 0.2)">completude, acurácia e acessibilidade, apenas.</mark>
>
> **Marquei:** 🟥 E · **Gabarito:** 🟩 A
>
> > [!success] ✅ Resposta — A
> > A qualidade de dados se classifica em **quatro categorias**: <mark style="background:#fff88f">intrínseca, contextual, representacional e acessibilidade</mark> (Wang & Strong; DAMA-DMBOK). **Acurácia** e **completude** são **dimensões** que ficam dentro das categorias, não categorias.
> > 
> > **(B)** são os princípios FAIR (Findable, Accessible, Interoperable, Reusable), e ainda troca "interoperável" por "interpolável". **(C)** e **(D)** listam só dimensões soltas. **(E)** mistura duas dimensões (completude, acurácia) com uma categoria (acessibilidade).
>
> > [!example]- 🧩 Quadro
> > | Categoria | Avalia | Dimensões |
> > | --- | --- | --- |
> > | Intrínseca | o dado em si | acurácia, objetividade, credibilidade, reputação |
> > | Contextual | adequação à tarefa | relevância, valor agregado, tempestividade, completude |
> > | Representacional | formato e sentido | interpretabilidade, facilidade de entendimento, consistência de representação |
> > | Acessibilidade | chegar ao dado | acessibilidade, segurança de acesso |
>
> > [!warning] ⚠️ Pegadinha da banca
> > Trocar o **nível**: lista dimensões (acurácia, completude, consistência) onde a pergunta pede as categorias. Outro distrator é o FAIR, que é de dados científicos/abertos e não é a classificação de qualidade.
>
> > [!tip] 💡 Macete
> > Quatro grupos = I-C-R-A (Intrínseca, Contextual, Representacional, Acessibilidade); o que tiver nome de métrica (acurácia, completude, unicidade) é dimensão, não grupo.
>
> > [!info] 🔗 Na matéria
> > [[P2 - Fluência de Dados CD#Dimensões de qualidade de dados]] — o cofre só diz "quatro categorias de dimensões" e não as nomeia; **não está no cofre** (entrou pelo comentário do TEC), então nada foi grifado.
> > **Fonte:** comentário do TEC (DAMA-DMBOK 2; Wang & Strong, 1996) · cofre `MATERIAS/P2 - Fluência de Dados CD.md:221`

> [!question]- 29/09 (mesma captura, sem hora registrada) · Fluência de Dados (Governança e Qualidade de Dados) · FGV (CNU, 2025) — Dados ausentes: MCAR × MAR × MNAR
> #3645035 FGV - 2025 - Servidor Público Federal (CNU)
> A tipologia sobre mecanismos de dados faltantes, estabelecida por Rubin (1976), define diferentes tratamentos estatísticos adequados no tratamento de tais dados.
>
> Uma equipe de analistas do governo federal está tratando os dados de uma pesquisa aplicada a jornalistas, comunicadores institucionais e profissionais da imprensa. O objetivo do estudo é entender como a cobertura de temas sociais evoluiu nos veículos de comunicação entre 2022 e 2024.
>
> Durante o tratamento da base, dois padrões de ausência chamaram atenção:
>
> • parte dos respondentes deixou em branco a variável “tempo de leitura semanal de portais de notícia”, o que ocorreu com mais frequência entre comunicadores de áreas como cultura, entretenimento e arte;
> • parte dos respondentes deixou em branco a variável “data de início da carreira”, o que ocorreu com mais frequência nos respondentes com menor tempo de atuação profissional.
>
> Considerando essa pesquisa, os analistas podem concluir que tais dados ausentes:
>
> (A) são do tipo omissos completamente ao acaso (missing completely at random – MCAR), pois os respondentes omitiram espontaneamente suas respostas e, portanto, devem ser excluídos da base de dados sem impacto estatístico;
> (B) irão enviesar os resultados da pesquisa, a despeito de serem classificados como MCAR, MNAR ou MAR, e, portanto, devem ser excluídos da base de dados, bem como as demais informações fornecidas pelos respectivos respondentes;
> (C) são do tipo omissos completamente ao acaso (missing completely at random – MCAR), pois não dependem de qualquer variável observável ou não observável e, portanto, podem ser estimados conforme as técnicas de imputação apropriadas;
> (D) <mark style="background:rgba(163, 67, 31, 0.2)">são do tipo omissos não aleatoriamente (missing not at random – MNAR), pois a ausência depende do próprio valor faltante, e, portanto, devem ser excluídos da base de dados, bem como as demais informações fornecidas pelos respectivos respondentes;</mark>
> (E) <mark style="background:#affad1">são do tipo dados omissos aleatoriamente (missing at random – MAR), pois a ausência está relacionada a outras variáveis observadas, como área de atuação e tempo de carreira, e, portanto, podem ser estimados conforme as técnicas de imputação apropriadas.</mark>
>
> **Marquei:** 🟥 D · **Gabarito:** 🟩 E
>
> > [!success] ✅ Resposta — E
> > Nos dois casos a ausência pode ser explicada por **outra variável que a base tem** (área de atuação; tempo de carreira) → <mark style="background:#fff88f">MAR</mark>. MAR é <span class="g-cond">ignorável</span> e admite <span class="g-comp">imputação</span> (múltipla, modelagem), não exclusão.
> > 
> > **(D)** define o MNAR certo, mas o caso não é esse: nenhuma ausência depende do **próprio valor** que faltou, e ainda manda excluir os respondentes. **(A)** e **(C)** dizem MCAR, mas a ausência tem padrão (área, tempo de carreira). **(B)** generaliza que qualquer mecanismo enviesa e manda excluir.
>
> > [!example]- 🧩 Quadro
> > | Mecanismo | A ausência depende de… | Ignorável? | Tratamento |
> > | --- | --- | --- | --- |
> > | MCAR | de nada | sim | exclusão, imputação simples |
> > | MAR | **outra variável observada** | sim | imputação múltipla, modelagem |
> > | MNAR | do **próprio valor** faltante (ou de variável não observada) | não | modelar o padrão de ausência |
>
> > [!warning] ⚠️ Pegadinha da banca
> > Alternativas com **definição correta aplicada ao caso errado**: (D) descreve MNAR direito, mas o enunciado dá exemplos de MAR. Toda vez que o enunciado citar "mais frequente entre [grupo]", a ausência tem relação com uma variável observada.
>
> > [!tip] 💡 Macete
> > Pergunte: "outra coluna que eu tenho prevê a falta?" Sim → MAR; não, é sorte → MCAR; só o próprio valor explica → MNAR.
>
> > [!info] 🔗 Na matéria
> > [[P2 - Fluência de Dados CD]] — seção 1.5 Tipos de Dados Ausentes (tabela MCAR/MAR/MNAR, `:142-145`, sem heading próprio) — já cobre a definição; grifei agora o núcleo do MAR.
> > **Fonte:** comentário do TEC · cofre `MATERIAS/P2 - Fluência de Dados CD.md:144`

> [!question]- 29/09 (mesma captura, sem hora registrada) · Fluência de Dados (Governança e Qualidade de Dados) · FGV (Auditor do Estado, CAGE RS, 2025) — Governança de dados centralizada
> #3227972 FGV - 2025 - Auditor do Estado (CAGE RS)
> Em uma estrutura de governança de dados centralizada, é comum que
>
> (A) <mark style="background:#affad1">um único departamento, geralmente TI, seja responsável pela gestão e pelo controle dos dados da organização.</mark>
> (B) a responsabilidade pela governança de dados seja dividida igualmente entre todas as equipes.
> (C) <mark style="background:rgba(163, 67, 31, 0.2)">as decisões de dados sejam tomadas de maneira colaborativa entre diferentes departamentos.</mark>
> (D) as tomadas de decisões relacionadas aos dados sejam totalmente distribuídas e autônomas.
> (E) não haja uma política formal para a gestão de dados.
>
> **Marquei:** 🟥 C · **Gabarito:** 🟩 A
>
> > [!success] ✅ Resposta — A
> > Na governança **centralizada** <mark style="background:#fff88f">uma única unidade (geralmente a TI)</mark> define e controla a organização e o gerenciamento dos dados. Decisão colaborativa entre departamentos é a governança <span class="g-comp">compartilhada</span> (só áreas internas); com participantes também <span class="g-comp">externos</span>, é a <span class="g-comp">colegiada</span>.
> > 
> > **(B)**, **(C)** e **(D)** descrevem modelos compartilhados/distribuídos. **(E)** está errada em qualquer modelo: todos têm política formal.
>
> > [!example]- 🧩 Quadro
> > | Modelo | Quem decide | Composição |
> > | --- | --- | --- |
> > | Centralizada | uma unidade central (em geral TI) | um só departamento |
> > | Compartilhada | equipe de vários departamentos | só internos |
> > | Colegiada | vários departamentos, com diretrizes gerais e cada setor cuida do seu | internos **e externos** |
>
> > [!warning] ⚠️ Pegadinha da banca
> > A banca descreve a compartilhada ("colaborativa entre departamentos") e chama de centralizada. A palavra que decide é **"único"** departamento.
>
> > [!tip] 💡 Macete
> > Centralizada = **um** manda; compartilhada = **vários internos** decidem juntos; colegiada = vários, **com gente de fora**.
>
> > [!info] 🔗 Na matéria
> > [[P2 - Fluência de Dados CD#Governança colegiada]] — a colegiada está no cofre; **centralizada e compartilhada não estão** (entraram pelo comentário do TEC), nada foi grifado.
> > **Fonte:** comentário do TEC (DAMA-DMBOK 2) · cofre `MATERIAS/P2 - Fluência de Dados CD.md:172`

> [!question]- 29/09 (mesma captura, sem hora registrada) · Fluência de Dados (Governança e Qualidade de Dados) · FGV (Analista Administrativo, TCE-RR, 2025) — Dimensão de qualidade: tempo de resposta e acesso
> #3251573 FGV - 2025 - Analista Administrativo (TCE-RR)
> O guia DAMA-DMBOK® prevê onze dimensões de Qualidade de Dados que devem ser atingidas para considerar um dado de qualidade. As dimensões recomendadas pelo guia são: acuracidade, completude, consistência, valor corrente, precisão, privacidade, razoabilidade, integridade referencial, em tempo adequado, unicidade e validade.
>
> A dimensão que indica se o tempo de resposta e acesso aos dados é satisfatório para os requisitos de uso é a
>
> (A) <mark style="background:#affad1">performance.</mark>
> (B) manutenibilidade.
> (C) unicidade.
> (D) <mark style="background:rgba(163, 67, 31, 0.2)">disponibilidade.</mark>
> (E) confiabilidade.
>
> **Marquei:** 🟥 D · **Gabarito:** 🟩 A
>
> > [!success] ✅ Resposta — A
> > <mark style="background:#fff88f">Performance</mark> mede o <span class="g-cond">tempo de resposta e de acesso</span> aos dados nos sistemas e se as métricas são razoáveis para o uso. **(D)** disponibilidade diz respeito ao sistema estar no ar quando necessário, não à velocidade do acesso. **(B)** é manutenção de sistemas; **(C)** é dado duplicado; **(E)** é dado íntegro e adequado ao contexto.
>
> > [!warning] ⚠️ Pegadinha da banca
> > A banca dá o gabarito por "performance" com base no comentário do TEC, mas a lista de onze dimensões do próprio enunciado **não traz** "performance": a questão pede pelo conceito ("tempo de resposta"), não pela lista. Aqui prevalece a leitura do enunciado: velocidade de acesso = performance; sistema no ar = disponibilidade.
>
> > [!info] 🔗 Na matéria
> > [[P2 - Fluência de Dados CD#Dimensões de qualidade de dados]] — a dimensão performance **não está no cofre** (entrou pelo comentário do TEC), nada foi grifado.
> > **Fonte:** comentário do TEC · cofre `MATERIAS/P2 - Fluência de Dados CD.md:221`

> [!question]- 29/09 (mesma captura, sem hora registrada) · Fluência de Dados (Governança e Qualidade de Dados) · FGV (Auditor de Controle Externo, TCE-PA, 2024) — Área do DMBOK: dados mestres
> #3046640 FGV - 2024 - Auditor de Controle Externo (TCE-PA)
> O DMBOK é estruturado em torno de onze (11) áreas de conhecimento do Framework de Gerenciamento de Dados DAMA-DMBOK. Essas áreas descrevem o escopo e o contexto de diversos conjuntos de atividades de gerenciamento de dados, e nelas estão incorporados os objetivos e princípios fundamentais do gerenciamento de dados.
>
> A área do conhecimento que inclui a reconciliação e a manutenção contínuas dos dados críticos, compartilhados e essenciais para permitir o uso consistente entre sistemas da versão mais precisa, oportuna e relevante da verdade sobre entidades empresariais essenciais é a
>
> (A) Governança de Dados.
> (B) Segurança de Dados.
> (C) <mark style="background:#affad1">Referência e Dados Mestres.</mark>
> (D) <mark style="background:rgba(163, 67, 31, 0.2)">Integração e Interoperabilidade de Dados.</mark>
> (E) Data Warehouse e Business Intelligence.
>
> **Marquei:** 🟥 D · **Gabarito:** 🟩 C
>
> > [!success] ✅ Resposta — C
> > <mark style="background:#fff88f">Referência e Dados Mestres</mark>: <span class="g-cond">reconciliação e manutenção contínuas</span> de dados críticos compartilhados, para que todos os sistemas usem a <span class="g-cond">versão mais precisa, oportuna e relevante da verdade</span> sobre as entidades essenciais.
> > 
> > **(D)** Integração e Interoperabilidade trata de **movimentação e consolidação** de dados entre bases, sistemas e organizações, não da versão única e confiável. **(A)** dá direção e direitos de decisão; **(B)** privacidade e confidencialidade; **(E)** dados de apoio à decisão, análise e relatórios.
>
> > [!example]- 🧩 Quadro
> > | Área | O que faz |
> > | --- | --- |
> > | Dados Mestres e de Referência | mantém a **versão única da verdade** das entidades essenciais |
> > | Integração e Interoperabilidade | **move e consolida** dados entre sistemas |
> > | Governança | direitos de decisão sobre os dados |
> > | Segurança | privacidade, confidencialidade, acesso adequado |
> > | DW e BI | dados para decisão, análise e relatórios |
>
> > [!warning] ⚠️ Pegadinha da banca
> > "Uso consistente entre sistemas" lembra integração, mas o núcleo é **reconciliar e manter a versão mais precisa** ("verdade") das entidades: isso é dado mestre.
>
> > [!tip] 💡 Macete
> > Integração = **transporta**; dado mestre = **decide qual versão vale**.
>
> > [!info] 🔗 Na matéria
> > [[P2 - Fluência de Dados CD#- 6 DMBOK: áreas de conhecimento, governança, arquitetura de dados, metadados, qualidade, segurança e master data.]] — tabela das áreas (linha 10, `:260`); grifado agora.
> > **Fonte:** comentário do TEC · cofre `MATERIAS/P2 - Fluência de Dados CD.md:260`

> [!question]- 29/09 (mesma captura, sem hora registrada) · Fluência de Dados (Governança e Qualidade de Dados) · FGV (Analista em Gestão Municipal, Pref SJC, 2024) — Dimensão: dados representam a vida real
> #2773076 FGV - 2024 - Analista em Gestão Municipal (Pref SJC)
> As dimensões de qualidade de dados discutidas no DAMA- DMBOK2 descrevem características mensuráveis dos dados que ajudam a definir seus requisitos de qualidade.
>
> A dimensão que se refere ao grau em que os dados representam corretamente entidades da “vida real” é denominada
>
> (A) validity.
> (B) <mark style="background:#affad1">accuracy.</mark>
> (C) <mark style="background:rgba(163, 67, 31, 0.2)">consistency.</mark>
> (D) uniqueness.
> (E) completeness.
>
> **Marquei:** 🟥 C · **Gabarito:** 🟩 B
>
> > [!success] ✅ Resposta — B
> > <mark style="background:#fff88f">Accuracy (precisão/acurácia)</mark>: grau em que os dados descrevem corretamente o objeto ou evento do <span class="g-cond">mundo real</span>. Difícil de medir sem uma fonte verificada como correta (sistema de registro, fonte confiável).
> > 
> > **(C)** consistency é a ausência de diferença entre duas ou mais representações da mesma coisa, sem olhar o mundo real. **(A)** validity é conformidade com sintaxe, formato, tipo, intervalo. **(D)** uniqueness: nenhuma instância registrada mais de uma vez. **(E)** completeness: proporção de dados presentes em relação ao potencial de 100%.
>
> > [!example]- 🧩 Quadro
> > | Dimensão | Pergunta que responde |
> > | --- | --- |
> > | Accuracy | reflete o mundo real? |
> > | Validity | obedece a sintaxe/formato/intervalo? |
> > | Consistency | duas representações da mesma coisa batem? |
> > | Uniqueness | está registrada só uma vez? |
> > | Completeness | está tudo que devia estar? |
>
> > [!warning] ⚠️ Pegadinha da banca
> > Consistência e acurácia se confundem: consistência compara **dados com dados** (ou com a definição); acurácia compara **dado com a realidade**. O dado pode ser consistente nos dois sistemas e errado nos dois.
>
> > [!info] 🔗 Na matéria
> > [[P2 - Fluência de Dados CD#Dimensões de qualidade de dados]] — cita acurácia, completude, consistência, tempestividade e unicidade só de nome; as **definições de cada dimensão não estão no cofre** (entraram pelo comentário do TEC), nada foi grifado.
> > **Fonte:** comentário do TEC (DAMA-DMBOK 2, cap. 13) · cofre `MATERIAS/P2 - Fluência de Dados CD.md:221`
