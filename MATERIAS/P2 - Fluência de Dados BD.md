---
disciplina: Fluência de Dados BD
bloco: Fluência de Dados
revisado:
prova: II
peso: 3
pontos: 0
origem: CE 2026 (novidade FCC)
prioridade: importante
---

# Fluência de Dados

## Percentual de cobrança (VINTEUM Fiscal 4.0)

*Fonte: Guia de Estudo Regular Fiscal 4.0 (VINTEUM) — bancas FCC, FGV e CEBRASPE. Mesma tabela vale para as 4 notas "Fluência de Dados" (BD/CD/SGE/SGE-C) — o guia trata como uma disciplina só.*

| Tópico | % |
| --- | --- |
| Linguagem SQL | 14,2% |
| Aprendizado de Máquina (Machine Learning) | 9,9% |
| Big Data | 9,6% |
| Data Warehouse e Data Mart | 7,0% |
| Modelo Relacional | 4,8% |
| Conceitos Iniciais e Gerais de IA | 4,8% |
| Governança de Dados | 4,5% |
| Data Mining | 4,5% |
| LGPD | 4,2% |
| Processamento de Linguagem Natural (IA) | 4,0% |
| Python | 3,5% |
| Ferramentas de BI e Visualização de Dados | 3,2% |
| Fundamentos e Princípios da Ciência de Dados | 3,0% |

## Checklist por importância (VINTEUM)

- [ ] Linguagem SQL [dom:: 3] [peso:: 14.2]
- [ ] Aprendizado de Máquina (Machine Learning) [dom:: 0] [peso:: 9.9]
- [ ] Big Data [dom:: 4] [peso:: 9.6]
- [ ] Data Warehouse e Data Mart [dom:: 4] [peso:: 7.0]
- [ ] Modelo Relacional [dom:: 4] [peso:: 4.8]
- [ ] Conceitos Iniciais e Gerais de IA [dom:: 0] [peso:: 4.8]
- [ ] Governança de Dados [dom:: 0] [peso:: 4.5]
- [ ] Data Mining [dom:: 0] [peso:: 4.5]
- [ ] LGPD [dom:: 0] [peso:: 4.2]
- [ ] Processamento de Linguagem Natural (IA) [dom:: 4] [peso:: 4.0]
- [ ] Python [dom:: 2] [peso:: 3.5]
- [ ] Ferramentas de BI e Visualização de Dados [dom:: 0] [peso:: 3.2]
- [ ] Fundamentos e Princípios da Ciência de Dados [dom:: 4] [peso:: 3.0]

> **Zero na âncora BA 2019** — disciplina nova, introduzida pela FCC em CE 2026  Prioridade: **importante**

A grande novidade dos editais fiscais recentes. Substitui a antiga "Noções de Informática" por algo bem mais próximo do trabalho real de um auditor: análise de dados aplicada à seleção de contribuintes e ao cruzamento de informações fiscais.

Se aparecer no edital baiano, é bloco de vantagem quase total: material escasso, concorrência sem repertório, e conteúdo que dialoga direto com Estatística e Auditoria.#

---

> [!info]- Como preencher
> Cada `- [ ]` é um tópico. Ajuste `[dom:: N]` de 0 a 5 ao estudar; acrescente `[rev:: AAAA-MM-DD]` para
> o painel te cobrar. Escreva o conteúdo logo abaixo do cabeçalho do tópico, no formato que quiser.



# Bloco A:

## - Conceitos Iniciais de Banco de Dados
- [ ] status [dom:: 0] [peso:: 3]
## - Conceitos e Fases de Projeto e Modelagem de Dados
- [ ] status [dom:: 0] [peso:: 3]
## - Organização de Arquivos e Métodos de Acesso
- [ ] status [dom:: 0] [peso:: 3]
## - Recuperação de Dados em SGBDs
- [ ] status [dom:: 0] [peso:: 3]
## - Transações (Locks, ACID, etc.)
- [ ] status [dom:: 0] [peso:: 3]
## - Visão (View), Triggers, Índices
- [ ] status [dom:: 0] [peso:: 3]
## - Administração de Banco de Dados (DBA) e do Administrador de Dados (DA)
- [ ] status [dom:: 0] [peso:: 3]
## - Segurança em Banco de Dados
- [ ] status [dom:: 0] [peso:: 3]
## - Outros Tipos e Modelos de Bancos de Dados
- [ ] status [dom:: 0] [peso:: 3]
## - Catálogo e Dicionário de Dados
- [ ] status [dom:: 0] [peso:: 3]

# Bloco B:

## - Conceitos e Fundamentos de Modelo Relacional;
- [ ] status [dom:: 0] [peso:: 3]

- A principal diferença entre as restrições **PRIMARY KEY** e **UNIQUE** está no tratamento de valores NULL. Ambas impõem unicidade aos valores armazenados, impedindo a ocorrência de duplicidades. Entretanto, a chave primária também exige que todos os seus atributos sejam obrigatoriamente preenchidos, ou seja, não admite valores NULL.

-- A Forma Normal Boyce-Codd **(FNBC)** é uma forma de normalização em bancos relacionais que busca eliminar problemas de atualização e garantir a integridade dos dados. É mais rigorosa do que a 3NF e se baseia nas dependências não triviais. Conforme a regra, uma tabela está na **FNBC** se, e somente se, para cada uma de suas dependências não triviais X → Y, X é uma superchave. **Segundo Silberschatz, Korth e Sudarshan:**

> Uma relação de esquema R está na forma normal de Boyce-Codd (BCNF) se, e somente se, para cada uma de suas dependências X → Y que são não triviais (ou seja, Y ∉ X), X é uma superchave para R.
> 
> Uma superchave para uma relação é um conjunto de atributos tal que a relação não contém duas tuplas (ou linhas) com o mesmo valor para esses atributos. Ou seja, um conjunto de atributos X é uma superchave para uma relação R se a dependência funcional X → R é satisfeita pela relação R.
> 
> A condição BCNF é mais forte que a condição 3NF. Em outras palavras, toda relação que está na BCNF também está na 3NF. No entanto, uma relação pode estar na 3NF, mas não na BCNF.
- Dessa forma, considerando o comando SQL para criação da tabela, podemos identificar os seguintes atributos:  
>**A int not null UNIQUE,** 
   **B int not null UNIQUE,** 
  **C int**

Onde,
**A → B**  (B é determinado por A)
**B → A**  (A é determinado por B)
**A → C**  (C é determinado por A)
**B → C**  (C é determinado por B)
Assim, cada uma dessas dependências é "não trivial" pois não é uma repetição da mesma informação. Além disso, tanto **A** quanto **B** são superchaves, porque são únicos e não nulos. Logo, todas as quatro dependências atendem à condição da **FNBC**.

### 1.6 AS REGRAS DE CODD
- [ ] status [dom:: 0] [peso:: 3]
Foram criadas para definir o que é necessário para que um SGBD seja considerado relacional:

- #1: as regras para informações
    - _"Todas as informações em um banco de dados relacional são representadas explicitamente no nível lógico e exatamente de uma maneira - por valores em tabelas"._
- #2: a regra de acesso garantido
    - _"Cada e todos os dados (valor atômico) em um banco de dados relacional têm a garantia de serem logicamente acessíveis pela reclassificação de uma combinação de nomes de tabelas, valor de chave primária e nome de coluna"._
- #3: tratamento sistemático de valores nulos
    - _"Valores nulos (distintos da string de caracteres vazia ou de uma string de caracteres em branco ou de qualquer outro número) são suportados completamente em um SGBD relacional para representar de maneira sistemática as informações ausentes, independentemente do tipo de dados"._
- #4: Catálogo online dinâmico baseado no modelo relacional
    - "A descrição da base de dados é representada no nível lógico da mesma maneira que os dados comuns, de modo que os usuários autorizados podem aplicar a sua interrogação a mesma linguagem relacional que se aplicam aos dados regulares."
- #5: A regra da sublinguagem de dados abrangentes
    - "Um sistema relacional pode suportar vários idiomas e vários modos de uso do terminal (por exemplo, o modo de preencher as lacunas). No entanto, deve haver pelo menos uma linguagem cujas declarações sejam expressas, por alguma sintaxe bem definida, como cadeias de caracteres e que seja abrangente no suporte de todos os seguintes itens:
        - Definição de dados.
        - Definição da visualização.
        - Manipulação de dados (interativa e por programa).
        - Restrições de integridade.
        - Autorização.
        - Limites da transação (início, confirmação e reversão)."
- #6: A regra da visualização atualização
    - _"Todas as visualizações que são teoricamente atualizáveis também são atualizáveis pelo sistema."_
- #7: Inserção, atualização e exclusão de alto nível
    - _"A capacidade de lidar com uma relação de base ou uma relação derivada como um único operando se aplica não apenas à recuperação de dados, mas também à inserção, atualização e exclusão de dados."_
- #8: Independência de dados físicos
    - _"Atividades de programas e atividades de terminais permanecem logicamente intactos sempre que alguma alteração ocorrer na representação de armazenamento ou métodos de acesso."_
- #9: Independência lógica de dados
    - "Programas de aplicações e as atividades de terminais permanecem logicamente intactos quando são feitas alterações de qualquer tipo as tabelas básicas que preservam informações que teoricamente permitem a estabilização dos dados."
- #10: Independência de integridade
    - _"Restrições de integridade específicas para um banco de dados relacional em particular devem ser definidas na sublinguagem de dados relacionais passíveis de serem armazenadas no catálogo, não nos programas de aplicação."_
- #11: Independência de distribuição
    - "Um SGBD relacional tem independência de distribuição"
- #12: A regra de não subversão

## - Modelo Entidade-Relacionamento (MER)
- [ ] status [dom:: 0] [peso:: 3]
- #tec/resumo 
(https://www.tecconcursos.com.br/aulas/materias/141/assuntos/4953). 

![[Pasted image 20260820150332.png|724]]



## - Modelagem e Mapeamento ER-relacional
- [ ] status [dom:: 0] [peso:: 3]
## - Álgebra Relacional
- [ ] status [dom:: 0] [peso:: 3]
## - Normalização
- [ ] status [dom:: 0] [peso:: 3]
- #tec/resumo 
(https://www.tecconcursos.com.br/aulas/materias/141/assuntos/2380).







# Bloco C:

## - Modelagem Dimensional
- [ ] status [dom:: 0] [peso:: 3]

**A tabela de fatos armazena os fatos ocorridos e as chave para as características correspondentes, nas tabelas dimensionais**.
As **chaves primárias** das tabelas <font color="#548dd4">Dimensão</font> são **chaves estrangeiras** na tabela <font color="#9bbb59">Fato</font>.


## - OLAP e suas diferenças com OLTP
- [ ] status [dom:: 0] [peso:: 3]

_O OLAP (On-Line Analytical Processing) é uma ferramenta de análise de dados usada para examinar grandes volumes de informações armazenadas em Data Warehouses → seu foco é permitir análises multidimensionais baseadas em **cubos de dados** → cada cubo contém **dimensões** (como tempo, produto, região) e **medidas** (como vendas ou lucro)._

→ Enquanto o **OLTP (On-Line Transaction Processing)** é voltado para **transações rotineiras** e rápidas, como inserir, atualizar ou excluir registros, o **OLAP** é voltado para **consultas e análises estratégicas**, sem alterar os dados originais.  
→ Assim, OLTP = operação do dia a dia; OLAP = tomada de decisão._

O OLAP se divide em três principais tipos quanto ao **armazenamento**:  
→ **MOLAP:** usa bancos multidimensionais → desempenho alto, mas pouca escalabilidade.  
→ **ROLAP:** usa bancos relacionais → desempenho mais lento, mas grande volume de dados.  
→ **HOLAP:** modelo híbrido → combina desempenho (MOLAP) e escalabilidade (ROLAP)._

Quanto à **origem da consulta**, há duas variações:  
→ **DOLAP:** acesso local via desktop → reduz o tráfego de rede.  
→ **WOLAP:** acesso via navegador web → permite análise remota._

As **operações OLAP** permitem explorar o cubo de dados de diferentes formas:  
→ **Slice:** fixa um valor em uma dimensão → cria uma fatia (ex.: vendas de carros em todas as regiões).  
→ **Dice:** seleciona múltiplos valores → forma um subcubo (ex.: vendas de motos e bicicletas no Sul e Norte entre 2018 e 2019).  
→ **Pivot (Rotate):** gira o cubo → altera a forma de visualização (ex.: trocar linhas por colunas).  
→ **Drill Down (Roll Down):** aumenta o detalhamento → reduz a granularidade (ex.: de ano → mês).  
→ **Drill Up (Roll Up):** reduz o detalhamento → aumenta a granularidade (ex.: de mês → ano).  
→ **Drill Across:** navega entre níveis da mesma dimensão (ex.: de região → município, sem passar por estado).  
→ **Drill Through:** muda de dimensão na análise (ex.: sair da dimensão região e analisar tempo)._

Em resumo → **OLAP = análise estratégica, modelo multidimensional e foco gerencial** → **OLTP = execução operacional, modelo relacional e foco transacional.

A pergunta pede que se identifique, entre as opções, o tipo de aplicação que geralmente opera de forma predominante em _lote_ (batch). Em linhas gerais, processamento em lote se caracteriza por executar grandes quantidades de dados de forma programada, <mark style="background:#fff88f">sem a necessidade de interação imediata do usuário e sem exigir respostas em tempo real.</mark>


## - Otimização (Tuning) em Banco de Dados
- [ ] status [dom:: 0] [peso:: 3]

**Resumo para concurso:** B-tree = consultas gerais e `LIKE 'prefixo%'`; Full-text = busca textual por palavras; Hash = igualdade exata; Bitmap = baixa cardinalidade e BI/Data Warehouse; Espacial = dados geográficos.



## - Cloud Computing (Computação em Nuvem)
- [ ] status [dom:: 0] [peso:: 3]
O termo **computação em nuvem** _**(cloud computing)**_ define um tipo de serviço disponibilizado por organizações a fim de entregar tipos específicos de recursos de computação conforme demanda do cliente através da internet, podendo haver definição de preço, tempo de uso, quantidade de dados trafegados, capacidade computacional, armazenamento de dados, limitação de tipos ou características em determinados serviços, etc. conforme contratado pelo cliente. Ou seja, é possível comprar a disponibilização de serviços como _datacenters_, servidores, máquinas virtuais, etc., de forma remota, aumentando e diminuindo os recursos disponíveis rapidamente, conforme acordo entre as partes ou conforme disponibilizado pelo locador do serviço.

De forma geral, existem muitas formas de classificar os modelos de abordagens em nuvem, embora as mais comuns são as que se referem ao modelo de serviços e são classificadas em 3 tipos:

- **IaaS (Infraestrutura como Serviço) -** Usualmente é o modelo usado por gestores de sistemas para a criação de máquinas virtuais, sistemas operacionais, memórias virtuais, etc. É considerada como a camada mais profunda da nuvem e tem como principal objetivo esboçar um ambiente conforme a demanda e necessidade, que seja de fácil compreensão para o usuário final e disponibilize seus múltiplos recursos. De forma geral, um IaaS oferece infraestrutura e recursos necessários para o modelo PaaS e o SaaS. Ou seja, resumidamente, o modelo permite dimensionar servidores, armazenamento, processamento e demais itens de acordo com sua demanda, tendo o usuário autonomia total e flexibilidade para aumentar e diminuir os recursos, realizar configurações de infraestrutura, gerenciamento da rede e diversas outras configurações. Algumas soluções de IaaS são: AWS, Microsoft Azure, Google Cloud, etc.

- **PaaS (Plataforma como Serviço) -** A plataforma como serviço é considerada a camada intermediária entre os modelos de serviços de computação em nuvem. A camada é composta por hardwares virtuais oferecidos como serviço, que são virtualizados e oferecidos na internet por um fornecedor especializado de recursos. Através desse modelo, é possível obter o desenvolvimento de aplicações sem a necessidade de comportar capacidade com servidores, realização de testes e análises de massa de dados, integração com bancos de dados, etc. Através da PaaS é possível realizar a integração de aplicações, experimentações e inserção de _frameworks_. Basicamente, um PaaS oferece infraestrutura e recursos necessários para o modelo SaaS. Ou seja, resumidamente, nesse modelo são disponibilizadas plataformas para que possam ser desenvolvidas e implantadas soluções de tecnologia para a nuvem, como aplicações para disponibilizar sites, bancos de dados e diversas aplicações na internet.

- **SaaS (Software como Serviço) -** Por último, a camada de software é considerada a camada mais externa dos modelos de serviços em nuvem. O modelo de SaaS é formado por um grupo de aplicações que são executadas diretamente no ambiente virtual, através de um interface disponibilizada via web (browser, aplicativo, software, etc). Geralmente, são serviços disponibilizados e utilizados por usuários finais, permitindo acesso a serviços como e-mails, conteúdo on demand, serviços por assinatura, etc.
**Exemplo:**

![[Pasted image 20260902140859.png|778]]

![[Pasted image 20260902140845.png|714]]

<mark style="background:#b1ffff">Uma Zona de Disponibilidade (AZ - Availability Zone)</mark> é projetada para ser uma unidade isolada e independente dentro de uma região de um provedor de nuvem. Cada AZ possui:
- **Datacenters próprios:** Um ou mais datacenters fisicamente separados.
- **Infraestrutura independente:** Energia, refrigeração, rede e segurança próprios, para evitar que falhas em uma AZ afetem outras.
- **Baixa latência entre AZs dentro da mesma região:** Embora isoladas, as AZs dentro de uma mesma região são conectadas por redes de alta velocidade e baixa latência, permitindo a replicação de dados e a criação de aplicações altamente disponíveis.
- **Isolamento de falhas:** O objetivo principal é que, se uma AZ falhar (devido a desastres naturais, falhas de energia, etc.), as outras AZs na mesma região continuem operando, garantindo a resiliência das aplicações.

Portanto, a afirmação de que uma zona de disponibilidade é composta por um conjunto de datacenters que <font color="#9bbb59">não são compartilhados com outras zonas de disponibilidade</font> está **correta**. O não compartilhamento é fundamental para o isolamento e a alta disponibilidade.

# Bloco D:

## - Big Data
- [ ] status [dom:: 0] [peso:: 3]
## - Business Intelligence e Analytics
- [ ] status [dom:: 0] [peso:: 3]
## - Definições e Funções de Data Warehouse e Data Mart
- [ ] status [dom:: 0] [peso:: 3]
## - ETL (Extração, Transformação e Carga)
- [ ] status [dom:: 0] [peso:: 3]

# Bloco E:

## - Consultas e Comandos em SQL
- [ ] status [dom:: 0] [peso:: 3]
## - Sublinguagens SQL (DDL, DML, DQL, DCL e DTL)
- [ ] status [dom:: 0] [peso:: 3]
## - Procedimentos Armazenados (Stored Procedures)
- [ ] status [dom:: 0] [peso:: 3]

### SGBD
- [ ] status [dom:: 0] [peso:: 3]


#### RECUPERAÇÃO DE DADOS 
- [ ] status [dom:: 0] [peso:: 3]

A **paginação de sombra** é uma técnica utilizada em sistemas de banco de dados para recuperação de transações, que evita a necessidade de logs complexos, garantindo a integridade e consistência dos dados em caso de falhas. Essa técnica é baseada na manutenção de uma cópia "sombra" da página de dados antes de qualquer modificação, permitindo uma recuperação confiável caso a transação não seja concluída com sucesso.


## modelagem de um banco de dados
- [ ] status [dom:: 0] [peso:: 3]

1. **Levantamento de requisitos:** Essa etapa é fundamental para compreender as necessidades e expectativas dos usuários e stakeholders em relação ao sistema de banco de dados que será desenvolvido. Durante essa fase, são coletadas informações essenciais que guiarão o restante do projeto.
    
2. **Modelagem conceitual:** Baseando-se nas informações coletadas durante o levantamento de requisitos, esta etapa visa criar um **esquema conceitual que define os objetos e seus relacionamentos relevantes para o sistema de banco de dados.** O modelo entidade-relacionamento (MER) é utilizado para representar essas estruturas em alto nível e de forma abstrata, ou seja, não existem detalhes de implementação especificados nessa etapa.
    
3. **Projeto lógico:** Nesta fase, o esquema conceitual é transformado em um esquema lógico, utilizando um modelo de dados específico, como o Modelo Relacional. Essa transformação organiza o banco de dados em conjuntos de relações, detalhando tabelas, domínios, tipos de dados, colunas, chaves primárias e estrangeiras. Embora seja importante a definição do modelo de dados, nessa etapa ainda não existe a obrigatoriedade de definição de um SGBD específico.
    
4. **Projeto físico:** A etapa de projeto físico abrange a escolha do Sistema de Gerenciamento de Banco de Dados (SGBD) que será utilizado, bem como questões relacionadas ao controle de acesso, estratégias de armazenamento e otimização de desempenho. Esse estágio foca em aspectos técnicos específicos que asseguram a implementação eficiente e segura do banco de dados.Além disso, é nesse momento que questões pendentes das etapas anteriores geralmente são resolvidas. Por exemplo, se a escolha de um SGBD específico não foi definida na fase de projeto lógico, a definição completa de certos tipos de dados pode ficar prejudicada. Isso ocorre porque o suporte a tipos de dados, como `bigint` ou `smallint`, entre outros, pode variar dependendo da tecnologia selecionada. Essa integração entre o projeto lógico e físico é essencial para garantir a coerência e a funcionalidade do banco de dados em produção.





## Banco de dados relacional; modelo entidade-relacionamento; normalização
- [ ] status [dom:: 0] [peso:: 3]


>O **modelo relacional** representa um banco de dados como uma **coleção de tabelas** **bidimensionais**(linhas x colunas), onde cada tabela pode ser armazenada como um arquivo separado. As tabelas (relações) representam tanto os dados como os relacionamentos entre esses dados.
 
 >O **modelo de rede** é um modelo legado (mais antigo) que representa os dados como tipos de registro e também representa um tipo limitado de relacionamento **1:N**, chamado de tipo de conjunto. Um relacionamento 1:N (um-para-muitos) relaciona uma instância de um registro a muitas instâncias de registros usando algum mecanismo de ligação com ponteiros nesses modelos.
 O **modelo hierárquico** representa os dados como estruturas de árvore hierárquicas. Cada hierarquia simboliza uma série de registros relacionados em uma estrutura de **“pais” e “filhos”**. O registro principal é chamado de raiz (root). Cada registro tem um único “pai”, mas pode ter vários “filhos”. Um registro que não seja “pai” em nenhum relacionamento é denominado “folha” (leaf). Não existe uma linguagem padrão para o modelo hierárquico, mas uma linguagem hierárquica popular é a DL/1, que foi um padrão de fato na indústria por muito tempo.

>**A)** **Trigger**: um gatilho é um procedimento que é executado automaticamente em resposta a determinados eventos em um banco de dados, como inserções, atualizações ou exclusões. Portanto, não é usado para controlar acessos concorrentes ou evitar dirty reads.
 **B)** **Shared lock**: um bloqueio compartilhado permite que vários usuários leiam (mas não modifiquem) um mesmo recurso simultaneamente. Assim, **<span style="color:rgb(216, 0, 219)">não evita dirty reads</span>, pois permite que outras transações leiam dados que podem estar em processo de alteração.
C)** **Exclusive lock**: um bloqueio exclusivo previne outros usuários de acessar o recurso bloqueado para qualquer operação, seja de leitura ou escrita. Isso garante o isolamento - nenhuma outra transação pode ler ou modificar os dados até que a transação atual seja concluída (commit) ou revertida (rollback), consequentemente previne dirty reads.
**D)** **Two-phase commit**: é um protocolo de controle de transação distribuída que garante que todas as partes envolvidas em uma transação concordem com a sua conclusão antes de ser efetivamente concluída. Não é um mecanismo direto para evitar dirty reads, pois serve para garantir a atomicidade em transações distribuídas.
**E)** **Three-phase commit**: é uma extensão do two-phase commit que visa reduzir o risco de bloqueio em caso de falhas. Assim como o two-phase commit, não é especificamente um mecanismo para evitar dirty reads, mas para gerenciar transações distribuídas.



## SQL: consulta, agregação, junção
- [ ] status [dom:: 0] [peso:: 3]


## NoSQL
- [ ] status [dom:: 0] [peso:: 3]

|Tipo de banco NoSQL|Estrutura|Melhor uso|
|---|---|---|
|**Chave/Valor**|Chave → Valor|Cache, sessões, alta velocidade|
|**Documentos**|JSON/BSON/XML|Aplicações web, APIs, dados semiestruturados|
|**Colunas (Column Family)**|Famílias de colunas|Big Data, analytics|
|**Grafos**|Nós + arestas + propriedades|Redes sociais, fraude, recomendações|

Como é possível notar nos exemplos acima, os dados em documentos podem conter **atributos aninhados e arrays**.  O **atributo aninhado** presente nesse exemplo é o campo:
"preferencias": {
"idioma": "pt-BR",
"tema": "escuro"
Mais especificamente, '`preferencias'` é um **atributo composto** (ou documento embutido). Dentro dele existem outros atributos: '`idioma'` e '`tema'`. Esses campos **não estão no mesmo nível** do atributo '`usuario'`, por isso são chamados de **aninhados** (_nested attributes_).

> A afirmativa está **CORRETA**, pois o armazenamentos **key–value** (pares chave-valor) são extremamente rápidos e escaláveis, mas oferecem apenas acesso simples, através da **recuperação direta pela chave**.
Isso significa que não oferecem consultas complexas. Essas consultas simples não permitem junções complexas em diferentes locais de armazenamento contendo referências, como nos modelos relacionais, por exemplo. Além disso, não há filtragens por atributos internos (além da chave) e não há padronização entre diferentes bancos key–value.
**Os armazenamentos de pares chave-valor são os menos adequados para uso em sistemas que precisam consultar dados em diferentes armazenamentos de pares chave-valor.**
---



