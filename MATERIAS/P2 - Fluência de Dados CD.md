---
disciplina: Fluência de Dados CD
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
- [ ] Big Data [dom:: 3] [peso:: 9.6]
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

> ****Zero na âncora BA 2019** — disciplina nova, introduzida pela FCC em CE 2026**
> Prioridade: **importante**

A grande novidade dos editais fiscais recentes. Substitui a antiga "Noções de Informática" por algo bem mais próximo do trabalho real de um auditor: análise de dados aplicada à seleção de contribuintes e ao cruzamento de informações fiscais.

Se aparecer no edital baiano, é bloco de vantagem quase total: material escasso, concorrência sem repertório, e conteúdo que dialoga direto com Estatística e Auditoria.
[[ERRO P2 - Fluência de Dados CD]]

---

> [!info]- Como preencher
> Cada `- [ ]` é um tópico. Ajuste `[dom:: N]` de 0 a 5 ao estudar; acrescente `[rev:: AAAA-MM-DD]` para
> o painel te cobrar. Escreva o conteúdo logo abaixo do cabeçalho do tópico, no formato que quiser.



# Bloco A:  Teoria da Informação. Dados Abertos. Ciclo de Vida. Governança. Qualidade de Dados, DMBOK

## - 1 Teoria da Informação: entropia, redundância, ruído, comunicação e valor da informação.
- [ ] status [dom:: 0] [peso:: 3]

## - 2 Dados Abertos: princípios (abertos por padrão, acessíveis, reutilizáveis), transparência governamental e interoperabilidade.
- [x] status [dom:: 1] [peso:: 3] ✅ 2026-09-12

- Segundo a Open Knowledge Foundation - OKFn, “**dados são abertos** quando qualquer pessoa pode livremente usá-los, reutilizá-los e redistribuí-los, estando sujeito a, no máximo, a exigência de creditar a sua autoria e compartilhar pela mesma licença”. Quando os dados são produzidos, coletados ou custodiados por autoridades públicas e disponibilizados em formato aberto, diz-se que são dados abertos governamentais. Ainda segundo a OKFn, dados abertos também são pautados por três leis e oito princípios:

	Em 2007, um grupo de trabalho de 30 pessoas reuniu-se na Califórnia, Estados Unidos da América, para definir os princípios dos Dados Abertos Governamentais. Chegaram num consenso sobre os seguintes 8 princípios:
1. **Completos.** Todos os dados públicos são disponibilizados. Dados são informações eletronicamente gravadas, incluindo, mas não se limitando a, documentos, bancos de dados, transcrições e gravações audiovisuais. Dados públicos são dados que não estão sujeitos a limitações válidas de privacidade, segurança ou controle de acesso, reguladas por estatutos.
2. **Primários.** Os dados são publicados na forma coletada na fonte, **com a mais<span class="cloze-span"> fina granularidade</span> possível, e não de forma agregada ou transformada.**
3. **Atuais.** Os dados são disponibilizados o quão rapidamente seja necessário para preservar o seu valor.
4. **Acessíveis.** Os dados são disponibilizados para o público mais amplo possível e para os propósitos mais variados possíveis.
5. **Processáveis por máquina.** Os dados são **<span class="cloze-span">razoavelmente</span> estruturados para possibilitar o seu processamento automatizado.**
6. **Acesso não discriminatório.** Os dados estão disponíveis a todos, sem que seja necessária identificação ou registro.
7. **Formatos não proprietários.** Os dados estão disponíveis em um formato sobre o qual nenhum ente tenha controle <span class="cloze-span">exclusivo</span>.
8. **Licenças livres.** Os dados não estão sujeitos a restrições por regulações de direitos autorais, marcas, patentes ou segredo industrial. Restrições razoáveis de privacidade, segurança e controle de acesso <span class="cloze-span">podem</span> ser permitidas na forma regulada por estatutos.

	**Descreva as características de dados abertos:** 1)Reuso e redistribuição:; 2)isponibilidade e acesso; 3)articipação universal.
- **Reuso e Redistribuição**: Dados abertos são disponibilizados de forma a permitir seu uso e redistribuição sem restrições, desde que respeitados os direitos autorais e outras leis aplicáveis. Isso significa que qualquer pessoa pode utilizar, modificar e compartilhar os dados abertos sem precisar de autorização prévia ou pagar taxas adicionais.
- **Disponibilidade e Acesso:** Dados abertos devem estar disponíveis de forma <span class="cloze-span">acessível</span> e <span class="cloze-span">fácil</span>, <mark style="background:#fff88f">sem barreiras técnicas ou comerciais </mark>que impeçam o acesso. Isso inclui a disponibilidade de metadados, documentação e formatos de arquivo apropriados para seu uso e reutilização.
- **Participação Universal:** A ideia por trás dos dados abertos é fomentar a colaboração, a inovação e a participação universal na sociedade. Todos devem ter acesso e liberdade para utilizar, compartilhar e contribuir com os dados abertos, independentemente de sua localização, capacidade financeira ou outros fatores. Essa abertura e acessibilidade permitem que todos tenham a chance de aprender, colaborar e construir soluções juntos, independentemente das fronteiras.

>**accessURL → acesso direto ao dado**  
 **landingPage → página explicativa**  
 **contactPoint → contato**  
 **endpointURL → API/serviço**



## -  3 Ciclo de Vida dos Dados: coleta, armazenamento, processamento, compartilhamento, retenção e descarte.
- [x] status [dom:: 2] [peso:: 3] ✅ 2026-09-12

 **ILM (Information Lifecycle Management)**, ou **Gestão do Ciclo de Vida da Informação**, é um conjunto de políticas, processos e tecnologias usados para gerenciar as informações (dados) ao longo de todo o seu ciclo de vida – desde a criação até a destruição. O ILM busca garantir que os dados sejam armazenados, acessados e descartados de forma eficiente, segura e em conformidade com regulamentos e políticas organizacionais.

Aqui estão os principais **estágios do ciclo de vida da informação** no ILM:

1. **Criação/Captura:** Dados são criados ou coletados (por exemplo, e-mails, registros financeiros, relatórios).
    
2. **Armazenamento:** Os dados são armazenados de forma eficiente, considerando custo e performance (em armazenamento primário, secundário, nuvem, etc.).
    
3. **Uso/Distribuição:** Os dados são utilizados em operações, decisões, relatórios e análises.
    
4. **Retenção:** Os dados são mantidos conforme <mark style="background:rgba(3, 135, 102, 0.2)">requisitos legais, regulatórios e de negócios</mark>. Aqui entram políticas de compliance e auditoria.
    
5. **Arquivamento:** Dados que não são mais ativos, mas que precisam ser retidos <mark style="background:rgba(240, 200, 0, 0.2)">por motivos legais ou históricos,</mark> são movidos para armazenamento de longo prazo.
    
6. **Exclusão/Descarte:** Quando os dados atingem o fim de sua vida útil e não têm mais valor ou exigências legais, são eliminados de forma segura.
    
Benefícios do ILM:
✅ Redução de custos com armazenamento e backup.  
✅ Maior segurança e conformidade com regulamentações (como LGPD, GDPR, HIPAA).  
✅ Melhor eficiência na gestão da informação.  
✅ Minimização de riscos de vazamento ou perda de dados.

> **O ciclo de vida dos dados é baseado no ciclo de vida do ==produto==. Não deve ser confundido com o ciclo de vida de desenvolvimento de sistemas**. Conceitualmente, o ciclo de vida dos dados é fácil de descrever. Inclui processos que criam ou obtêm dados, aqueles que os movem, transformam e armazenam e permitem que sejam mantidos e compartilhados, e aqueles que os usam ou aplicam, bem como aqueles que os descartam.

==1.4 Transformação dos Dados
A transformação de dados é um processo no qual os dados brutos são modificados ou manipulados de alguma forma para se adequar às necessidades específicas de análise. No contexto de data literacy, a transformação de dados é uma habilidade crucial para trabalhar eficientemente com grandes conjuntos de dados e extrair insights valiosos. Algumas tarefas comuns de transformação de dados incluem:==

| Tarefa                          | Descrição                                                                                                            | Quando Usar                                                                                                                             | Benefícios                                                                                      | Exemplo                                                                               |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Anonimização**                | Remoção ou substituição de informações identificáveis para proteger a privacidade.                                   | Usar ao trabalhar com dados <mark style="background:rgba(136, 49, 204, 0.2)">sensíveis</mark> para cumprir regulamentos de privacidade. | Protege a privacidade dos indivíduos, conforme GDPR ou outras leis de proteção de dados.        | Remoção de nomes e endereços de um conjunto de dados de pacientes.                    |
| **Discretização**               | Transformação de variáveis <mark style="background:rgba(240, 200, 0, 0.2)">contínuas</mark> em categorias discretas. | Usar quando variáveis contínuas precisam ser agrupadas em intervalos ou categorias.                                                     | Facilita a análise de dados categóricos e a construção de modelos de classificação.             | Transformação de idades em grupos etários (0-18, 19-35, 36-50, etc.).                 |
| **Normalização**                | Ajuste dos valores das variáveis para um intervalo comum.                                                            | <font color="#366092">Usar quando variáveis têm escalas diferentes e precisam ser comparáveis.</font>                                   | Melhora o desempenho de algoritmos de aprendizado de máquina.                                   | Escalonamento de dados de renda anual para um intervalo de 0 a 1.                     |
| **Padronização**                | <font color="#de7802">Transformação de dados para ter média zero e desvio padrão de um.</font>                       | Usar quando variáveis precisam ter distribuição normal.                                                                                 | Necessário para algoritmos que assumem normalidade dos dados, como PCA.                         | Ajuste de notas de teste para terem média zero e desvio padrão de um.                 |
| **Imputação**                   | Substituição de valores ausentes por estimativas.                                                                    | Usar quando há dados ausentes que precisam ser preenchidos.                                                                             | Mantém a integridade do conjunto de dados, evitando a perda de informações.                     | Preenchimento de valores ausentes de renda com a média da renda conhecida.            |
| **Agregação**                   | Combinação de múltiplas observações em resumos estatísticos.                                                         | Usar para simplificar grandes volumes de dados.                                                                                         | Facilita a visualização e a análise de grandes conjuntos de dados.                              | Cálculo da média mensal de vendas a partir de dados diários.                          |
| **Codificação**                 | Transformação de dados categóricos em formatos numéricos.                                                            | Usar quando variáveis categóricas precisam ser usadas em modelos matemáticos.                                                           | Permite a inclusão de dados categóricos em algoritmos de aprendizado de máquina.                | One-hot encoding de variáveis de gênero (masculino, feminino).                        |
| **Redução de Dimensionalidade** | Simplificação de conjuntos de dados reduzindo o número de variáveis.                                                 | Usar para melhorar a performance e a interpretabilidade de modelos.                                                                     | Reduz a complexidade do modelo, <mark style="background:#fff88f">prevenindo overfitting.</mark> | PCA (Análise de Componentes Principais) para reduzir variáveis de entrada.            |
| **Remoção de Outliers**         | Identificação e eliminação de valores anômalos que distorcem a análise.                                              | Usar quando outliers prejudicam a precisão do modelo ou análise.                                                                        | Melhora a precisão dos modelos e a qualidade da análise.                                        | Remoção de valores de temperatura extremamente altos/baixos que são erros de medição. |
**1.5 Tipos de Dados Ausentes**

|Tipo de Dados Ausentes|Características|Métodos Recomendados|Exemplos|
|---|---|---|---|
|**MCAR** _(Missing Completely at Random)_|Dados ausentes não dependem de nenhuma variável observada ou não observada; ausências são aleatórias.|Exclusão de casos, imputação simples.|Dados de sensores falhando **aleatoriamente** em diferentes momentos sem relação com as condições ambientais ou o funcionamento do sensor.|
|**MAR** _(Missing at Random)_|Dados ausentes podem ser explicados por outras variáveis observadas; a ausência não é completamente aleatória, mas pode ser prevista com base em outras informações disponíveis.|Imputação múltipla, modelagem estatística que aproveita as relações observadas.|Em um estudo médico, dados ausentes sobre a pressão arterial podem ser **previstos** com base em outras variáveis, como idade ou peso do paciente.|
|**MNAR** _(Missing Not at Random)_|Dados ausentes dependem da própria variável ausente ou de outras variáveis não observadas; as ausências têm um padrão específico.|Modelagem de equações estruturais, métodos bayesianos, modelagem direta do padrão de ausência.|Em um estudo de renda, pessoas com rendas muito altas ou muito baixas podem optar por não reportar seus rendimentos, e essa ausência está **relacionada diretamente ao valor da própria renda**.|

**1.6 Atributos dos Dados**

- **Relevância, Cobertura, Profundidade, Custo, História (duração), Frequência, Processamento, Custo de aquisição**: Estes atributos ajudam a avaliar a utilidade, aplicabilidade, custo e qualidade dos dados. São essenciais para entender o valor e as limitações dos dados em diferentes contextos.

| Atributo               | Definição                                                                                       |
| ---------------------- | ----------------------------------------------------------------------------------------------- |
| **Relevância**         | Utilidade de um conjunto de dados para propósitos específicos.                                  |
| **Cobertura**          | Área geográfica abrangida pelo conjunto de dados.                                               |
| **Profundidade**       | Variedade e número de diferentes pontos de dados no conjunto.                                   |
| **Custo de Dados**     | Custo de acesso e processamento do conjunto de dados.                                           |
| **História**           | Alcance histórico do conjunto de dados.                                                         |
| **Frequência**         | Intervalo de tempo entre pontos de dados e frequência de atualização.                           |
| **Processamento**      | <font color="#de7802">Quantidade de correção de erros e rotulagem antes da distribuição</font>. |
| **Custo de aquisição** | Custo de aquisição e verificação dos dados em sua forma original.                               |

##  4 Governança de Dados: papéis, políticas, accountability, stewardship e alinhamento estratégico.
- [x] status [dom:: 3] [peso:: 3] ✅ 2026-09-21

**De acordo com o DAMA DMBOK, a governança de dados tem como objetivo central habilitar a organização a gerenciar seus dados como ativos valiosos, exigindo _accountability_ (responsabilização), controle e regras bem definidas, de forma alinhada aos objetivos do negócio.**
Veja os erros das outras opções:
**A:** A governança não é um programa estritamente tecnológico ou de TI. As responsabilidades são compartilhadas entre a área de tecnologia e as áreas de negócio.  
**B:** A ética na manipulação de dados é um pilar estrutural do gerenciamento de dados que se aplica a todo o seu ciclo de vida, e não apenas a modelos de aprendizado de máquina.  
**C:** A governança exerce autoridade, supervisão e controle. A execução técnica e operacional (como realizar o processo de ETL) cabe a outras áreas de conhecimento, como a Integração de Dados.  
**D:** Os _data stewards_ (mordomos de dados) atuam e são responsáveis diretamente _dentro_ da área de negócios da organização, não sendo necessariamente especialistas externos independentes.

#### Governança colegiada

<mark style="background:#fff88f">Governança colegiada</mark>: composta por membros de **várias áreas distintas**, internas e externas à organização, que definem o processo de organização e gerenciamento de dados. Há definição de **diretrizes gerais**, e cada setor cuida das suas particularidades a partir do contexto geral.

Caso da questão: representantes da Coordenadoria de Fiscalização, da Subsecretaria de Arrecadação e da Diretoria de Tecnologia da Informação → governança colegiada.

#### Gestor de Dados (Data Steward)

<mark style="background:#fff88f">Gestor de Dados</mark> é o rótulo mais comum para a responsabilidade e a prestação de contas pelos dados e pelos processos que garantem o controle eficaz e o uso dos ativos de dados. Pode ser formalizado por cargos e descrições de trabalho, ou ser uma função menos formal, exercida por pessoas que ajudam a organização a obter valor dos dados. *Custodiante* e *fiduciário* costumam ser sinônimos de quem exerce funções semelhantes.

- Gerenciam ativos de dados **em nome de outros** e no melhor interesse da organização (McGilvray, 2008).
- Representam os interesses de **todas as partes interessadas** e adotam perspectiva empresarial, para que os dados sejam de alta qualidade e usados com eficácia.
- Os eficazes são responsáveis e prestam contas pelas atividades de governança de dados e dedicam parte do tempo a elas.

Na maioria dos casos, as atividades se concentram em alguns, senão todos, destes aspectos:

1. **Criar e gerenciar Metadados principais:** terminologia de negócios, valores de dados válidos e outros metadados críticos. Frequentemente respondem pelo **Glossário de Negócios**, que vira o sistema de registro dos termos de negócio relacionados aos dados.
2. **Documentar regras e padrões:** regras de negócio, padrões de dados e regras de qualidade de dados. As expectativas de dados de alta qualidade costumam ser formuladas como regras baseadas nos processos de negócio que criam ou consomem os dados. Ajudam a garantir consenso sobre elas e uso consistente.
3. **Gerenciar problemas de qualidade de dados:** identificação e resolução de questões relacionadas aos dados, ou facilitação do processo de resolução.
4. **Executar atividades operacionais de governança:** garantir, no dia a dia e projeto a projeto, que as políticas e iniciativas de governança sejam seguidas, e influenciar decisões para que os dados sejam gerenciados de modo a apoiar os objetivos gerais da organização.

#### Engenheiro de dados × cientista de dados

<mark style="background:#fff88f">Engenheiro de dados</mark>: projeta, implementa e mantém **pipelines de dados**, processos de integração, mecanismos de armazenamento e disponibilização de informações (item CORRETO). Desenvolve e otimiza pipelines que movem informações de múltiplas fontes para bancos de dados, data warehouses ou plataformas em nuvem, garantindo dados limpos, confiáveis e acessíveis. Gerencia o processamento em escala (fluxos em tempo real e em lote) para dar suporte a análise, BI e aprendizado de máquina, e cria a infraestrutura que torna possível a análise avançada.

⚠️ **Erro que cometi:** confundi com o cientista de dados. **Elaborar modelos estatísticos preditivos e construir algoritmos de aprendizado de máquina para identificar padrões automaticamente** é atribuição do cientista de dados, não do engenheiro.

#### Alfabetização de dados (data literacy)

<mark style="background:#fff88f">Alfabetização de dados</mark>: capacidade de ler, trabalhar, analisar, comunicar e raciocinar com dados de forma eficaz. É entender o que os dados significam, como são criados e como usá-los para fazer as perguntas certas, interpretá-los corretamente e tomar decisões informadas e baseadas em evidências. Traz uma abordagem de pensar criticamente sobre os dados e de explicar suas nuances com clareza.

⚠️ **Questão** (origem anotada: Cebraspe, SEFAZ-RN, Inovando RS): o enunciado pedia a técnica que avalia de forma **criteriosa** a fidedignidade das fontes, a integridade metodológica e a neutralidade dos dados → alfabetização de dados. "Criteriosa" remete a **questionamentos críticos**: ler e questionar criticamente os dados permite identificar distorções ou interpretações equivocadas **antes** da tomada de decisão.

#### Governança de dados não se resume à criptografia

⚠️ **Reducionismo do enunciado (item ERRADO):** dizer que a governança de dados é apenas um método com "criptografia segura para o armazenamento de dados" subestima sua amplitude.

- Governança de dados é um conjunto abrangente de práticas, processos, papéis, responsabilidades e métricas para garantir a **qualidade, a privacidade, a integridade e a proteção** dos dados, com atividades como gestão de dados mestres, qualidade de dados e gerenciamento do ciclo de vida.
- Lida com a maneira como os dados são coletados, armazenados, gerenciados, compartilhados e usados na organização.
- A criptografia é uma ferramenta vital contra o acesso não autorizado, mas é **apenas um componente** dessas práticas.

Erro que cometi: não percebi o reducionismo do enunciado.


## - 5 Qualidade de Dados: completude, consistência, acurácia, unicidade, atualidade e integridade.
- [ ] status [dom:: 0] [peso:: 3]

#### Dimensões de qualidade de dados

Item CORRETO: a qualidade de dados é tratada como <mark style="background:#fff88f">disciplina multidimensional</mark>, cujas dimensões (como acurácia, completude, consistência, tempestividade e unicidade) devem ser definidas e medidas com base nos **requisitos e na criticidade do negócio**. Uma dimensão serve para definir resultados da avaliação inicial da qualidade dos dados. São definidas **quatro categorias de dimensões**, e cada uma tem várias dimensões, entre elas as citadas.

#### Quality by Design (QbD)

<mark style="background:#fff88f">Quality by Design</mark> é uma abordagem **proativa**: incorpora a qualidade desde o início, na concepção e execução dos processos (entrada, captura e transformação dos dados). A ideia é evitar erros antes que aconteçam, em vez de corrigi-los depois.

→ qualidade embutida desde a origem: no projeto, na entrada e na transformação dos dados.

#### Qualidade em modelos de dados

⚠️ A definição de "secundário" **não** é componente principal dos processos de qualidade para modelos de dados. Os principais componentes geralmente incluem:

- **Definição de requisitos:** entender o que o modelo precisa representar e as necessidades dos usuários.
- **Modelagem conceitual:** modelo de alto nível com os conceitos e relacionamentos importantes do domínio de negócio.
- **Modelagem lógica:** transforma o conceitual em modelo mais detalhado, independente de qualquer tecnologia específica de banco de dados.
- **Modelagem física:** mapeia o lógico para um esquema de banco de dados específico, considerando o SGBD utilizado.
- **Normalização:** técnicas para garantir a integridade dos dados e minimizar a redundância.
- **Revisão por pares:** outros especialistas revisam o modelo para identificar erros, inconsistências ou melhorias.
- **Testes:** validar o modelo com dados reais ou simulados para garantir que atenda aos requisitos e funcione como esperado.
- **Documentação:** documentação clara e completa, com diagramas, descrições de entidades e atributos e regras de negócio.

#### Data profiling

<mark style="background:#fff88f">Data profiling</mark> é o processo de criação de perfis de dados para descobrir, entender e classificar os dados, identificando suas características e avaliando a qualidade. Revela se os dados são completos ou exclusivos, detecta erros e padrões atípicos e determina a usabilidade. Com isso, a empresa obtém análises precisas, decisões mais eficazes e economia de recursos.

## - 6 DMBOK: áreas de conhecimento, governança, arquitetura de dados, metadados, qualidade, segurança e master data.
- [ ] status [dom:: 0] [peso:: 3]

As **áreas de conhecimento** descrevem o escopo e o contexto de conjuntos de atividades de gerenciamento de dados; nelas estão embutidos os objetivos e princípios fundamentais do gerenciamento de dados. Como os dados se movem horizontalmente nas organizações, as atividades das áreas **se cruzam entre si** e com outras funções organizacionais.

| Cap. | Área | Escopo |
| --- | --- | --- |
| 3 | **Governança de Dados** | fornece direção e supervisão para o gerenciamento de dados, estabelecendo um sistema de **direitos de decisão** sobre os dados que considera as necessidades da empresa. |
| 4 | **Arquitetura de Dados** | define o modelo para gerenciar ativos de dados, alinhando-se com a estratégia organizacional para estabelecer requisitos de dados estratégicos e designs para atendê-los. |
| 5 | **Modelagem e Projeto de Dados** | processo de descobrir, analisar, representar e comunicar requisitos de dados numa forma precisa chamada modelo de dados. |
| 6 | **Armazenamento de Dados e Operações** | design, implementação e suporte de dados armazenados para maximizar seu valor. As operações dão suporte durante todo o **ciclo de vida dos dados, do planejamento ao descarte**. |
| 7 | **Segurança de Dados** | garante que a privacidade e a confidencialidade sejam mantidas, que os dados não sejam violados e que sejam acessados de forma adequada. |
| 8 | **Integração e Interoperabilidade** | processos de movimentação e consolidação de dados dentro e entre armazenamentos, aplicativos e organizações. |
| 9 | **Gerenciamento de Conteúdo e Documento** | planejamento, implementação e controle do ciclo de vida de dados e informações em mídias não estruturadas, especialmente documentos necessários a requisitos de conformidade legal e regulatória. |
| 10 | **Dados Mestres e de Referência** | reconciliação e manutenção contínuas de dados compartilhados essenciais, para permitir o uso consistente em todos os sistemas da versão mais precisa, oportuna e relevante da verdade sobre entidades comerciais essenciais. |
| 11 | **Data Warehousing e Business Intelligence** | planejamento, implementação e controle para gerenciar dados de suporte à decisão e permitir que os trabalhadores do conhecimento obtenham valor dos dados por análise e relatórios. |
| 12 | **Metadados** | planejamento, implementação e controle para permitir acesso a metadados integrados de alta qualidade (definições, modelos, fluxos de dados e outras informações críticas para entender os dados e os sistemas que os criam, mantêm e acessam). |
| 13 | **Qualidade dos Dados** | planejamento e implementação de técnicas de gerenciamento de qualidade para medir, avaliar e melhorar a adequação dos dados para uso na organização. |

⚠️ **Erro que cometi:** não sabia que o *Armazenamento de Dados e Operações* responde pelo suporte ao ciclo de vida dos dados; eu associava isso à governança de dados.


# Bloco B: Data mining, CSV, XML, JSON, CRISP-DM
 **Ténicas de Pré-Processamento:**

**Limpeza dos Dados –** Preenche valores faltantes, suaviza dados ruidosos, identifica ou remove “outliers” e resolve inconsistências.
**Integração –** Dados de origens diferentes devem ser integrados. <mark style="background:rgba(240, 200, 0, 0.2)">Resolver conflitos e redundância</mark>
**Transformação –** Normalização e agregação dos dados.
**Redução -** Tenta reduzir o volume de dados sem provocar grandes alterações no resultado. Compressão de atributos e redução do número de dados.
<mark style="background:rgba(240, 200, 0, 0.2)">Discretização</mark> – Faz parte do processo de redução, mas tem papel importante, especialmente com dados numéricos. <font color="#ff0000">Visa estabelecer valores discretos para variáveis contínuas.</font>
## Data Mining: fases do KDD (Knowledge Discovery in Databases)
- [ ] status [dom:: 0] [peso:: 3]

Processo de descoberta de conhecimento em bancos de dados (Navathe), em seis fases:

1. Seleção de dados — escolha de itens ou categorias específicas.
2. Limpeza de dados — correção de dados e tratamento de valores nulos.
3. Enriquecimento — adição de novas informações a partir de fontes externas, integração de dados de origens diferentes ou aplicação de regras de negócio, para melhorar qualidade e relevância dos dados.
4. Transformação/codificação de dados — agregação, discretização ou redução de dimensionalidade.
5. Mineração de dados — identificação de padrões e relacionamentos (agrupamento, regressão, classificação, associação etc.).
6. Relatório e exibição da informação descoberta — resultados apresentados em listas, gráficos, tabelas etc.

As quatro primeiras fases compõem o pré-processamento.

⚠️ Não confundir enriquecimento com fases vizinhas: seleção de amostras pertence à fase de seleção; deduplicação de registros pertence à limpeza; integração de bases diferentes é combinar dados de fontes distintas numa única base; tratamento de valores nulos é técnica de limpeza — nenhuma dessas é enriquecimento.

## XML
- [x] status [dom:: 2] [peso:: 3] ✅ 2026-09-12
(https://www.w3schools.com/xml/schema_facets.asp).

XML é uma linguagem de <mark style="background:rgba(240, 200, 0, 0.2)">marcação</mark>, ou seja, utilizarmos para organizar a estrutura de uma página. Quando falamos em estilos em uma página a primeira linguagem que vem à mente é CSS. Também temos uma conhecida como XSLT para estilar o XML.

<font color="#1f497d">Pattern Value = "valor padrão"</font>  
Define que só aceitará letras minúsculas do alfabeto entre a e z  
<xs:pattern value="[a-z]"/>  
Define que só aceitará 2 letras maiúsculas do alfabeto entre a e z  
<xs:pattern value="[A-Z][A-Z]"/>  
Define que só aceitará 3 letras minúsculas do alfabeto entre a e z  
<xs:pattern value="[a-z][a-z][a-z]"/>

## JSON
- [x] status [dom:: 2] [peso:: 3] ✅ 2026-09-12
**JSON**
```
{
   "id":1,
   "nome":"Alexandre Gama",
   "endereco":"R. Qualquer"
}
```
![[Pasted image 20260823151332.png]]

--A alternativa correta é a **C**.
JSON é leve, com sintaxe simples (pares chave-valor), fácil de gerar e interpretar por linguagens de programação (parsing nativo em JavaScript, por exemplo), o que o tornou o formato dominante para APIs REST no transporte de dados entre cliente e servidor.

- Em JSON, quando há múltiplos valores para uma mesma chave, eles devem ser representados como um array >>>entre colchetes [ ] "telefones": [  "(71) 98765-8976","(71) 98756-4678"  ]}}

-**b)**  o XML _Schema_ é adequado para validar tanto a estrulura quanto os valores dos elementos em um documento XML.
**Correta**. O XML Schema é realmente adequado para validar tanto a estrutura quanto os valores dos elementos em um documento XML. Isso porque é possível definir regras de negócio específicas.



# Bloco C: ML e algoritmos

**e)  redução de dimensionalidade**
**ERRADO.** A redução de dimensionalidade visa diminuir o número de variáveis independentes ou características nos dados, sem perder informações importantes. Técnicas como PCA (Principal Component Analysis) ou t-SNE (t-distributed Stochastic Neighbor Embedding) são usadas para transformar dados de alta dimensionalidade em um espaço de dimensões mais baixas. Logo, não resolve diretamente o problema de classificação de imagens de animais, que exige a previsão de um rótulo categórico.

**Gabarito: Certo**
O item está correto e faz uma interpretação perfeita dos coeficientes da equação da reta de regressão linear simples Y=β0​+β1​X.
**Análise da Equação:** Y=30+0,8X
1. **O Coeficiente Linear (Intercepto): 30**
    - Representa o valor de Y quando X=0.
    - No contexto do problema: Se a quantidade de fertilizante (X) for zero, a produção esperada (Y) é de **30 sacas/ha**. A afirmação do item está correta quanto a este ponto.
        
2. **O Coeficiente Angular (Inclinação): 0,8**
    - Representa a taxa de variação de Y em relação a uma unidade de X. Ou seja, para cada 1 kg de fertilizante, a produção aumenta em 0,8 saca.
    - O item propõe um aumento de **10 kg** de fertilizante. Para calcular o impacto, multiplicamos a variação de X pelo coeficiente angular:
        10 kg×0,8 saca/kg=8 sacas
    - Portanto, espera-se um aumento de **8 sacas** na produção. A afirmação também está correta neste ponto


## Detecção de Anomalias: tipos e classificação
- [x] status [dom:: 2] [peso:: 3] ✅ 2026-09-12

Duas categorias de anomalias, por origem: <mark style="background:#fff88f">não intencionais</mark> (desvio da norma por erro ou ruído na coleta — sensor defeituoso, erro humano) e <mark style="background:#fff88f">intencionais</mark> (desvio por ação ou evento real, ex.: pico de vendas em época festiva).

Três subtipos, por escopo (podem ser intencionais ou não intencionais):
- **Pontuais** (outliers globais) — ponto individual muito fora do restante do conjunto. Ex.: saque bancário muito acima do padrão do usuário.
- **Contextuais** — não são outliers isolados, mas destoam dentro de um contexto específico (hora do dia, local). Ex.: pico de consumo de energia ao meio-dia, quando a casa costuma estar vazia.
- **Coletivas** — um conjunto de instâncias que, juntas, destoam da norma, mesmo com cada instância parecendo normal isoladamente. Ex.: aumento simultâneo de tráfego de rede vindo de vários IPs.

## Espaço Latente
- [x] status [dom:: 3] [peso:: 3] ✅ 2026-09-12

Representação abstrata e compactada dos dados, usada por algoritmos de aprendizado de máquina em vez das informações brutas e de alta dimensionalidade (ex.: cada pixel de uma imagem) — foca nas características essenciais, descobrindo padrões e relações ocultas.

## LSTM (Long Short-Term Memory)
- [x] status [dom:: 3] [peso:: 3] ✅ 2026-09-12

Arquitetura de rede neural recorrente (RNN) que retém valores por intervalos arbitrários — adequada para classificar, processar e prever séries temporais com gaps de duração desconhecida. A insensibilidade ao comprimento do gap dá vantagem à LSTM sobre RNNs tradicionais ("vanilla"), Modelos Ocultos de Markov (MOM) e outros métodos de aprendizado de sequências.

# Bloco D: PLN, IA e LLMs

## Conceitos Iniciais e Gerais de IA
- [x] status [dom:: 2] [peso:: 3] ✅ 2026-09-12

<mark style="background:#fff88f">IA Fraca (Estreita)</mark>: modela a inteligência humana para tarefas específicas, sem habilidades cognitivas completas — opera só dentro de um conjunto de funções predefinidas, sem desviar do caminho programado. Ex.: assistentes de voz (Siri, Alexa) classificam dados e respondem consultas rapidamente, mas não realizam tarefas fora do escopo treinado.
> [!warning]- Pendência de autoria
> A captura original citava "8 exemplos práticos de IA fraca/estreita" mas só trouxe o primeiro (assistentes de voz). Completar com os outros 7 se for revisar o material de origem.

<mark style="background:#fff88f">IA deve seguir as leis de proteção de dados do país onde for utilizada e comercializada</mark>, independentemente de onde foi desenvolvida ou fabricada — a legislação aplicável é a do local de uso, não a de origem.

#### Discriminação algorítmica e viés

<mark style="background:#fff88f">Discriminação algorítmica</mark>: o sistema de IA usa, numa tomada de decisão e sem justificativa válida, a informação de que alguém pertence a um grupo social (ou características que funcionam como **proxies**), gerando desvantagens sistemáticas para esse grupo em contextos em que esse critério não deveria influenciar a decisão.

**Viés (Algorithmic Bias):** o sistema reflete, reproduz ou **amplifica** preconceitos históricos ou sociais, tratando indivíduos de forma injusta com base em características inerentes a eles. Costuma ocorrer porque os **dados de treinamento** (o histórico do passado) já contêm essas injustiças humanas. A máquina não tem bússola moral nem analisa o contexto real das situações para filtrar as nuances que dados históricos podem carregar.

**Atributos protegidos:** características sensíveis que, por lei ou ética, não devem ser usadas para negar oportunidades (ex.: raça, gênero, religião, orientação sexual, origem nacional).

⚠️ **Variável proxy:** remover a coluna "Raça" não neutraliza o modelo. Se ele mantiver "CEP" ou "Histórico Escolar" com forte correlação histórica com grupos raciais marginalizados, a IA usa o CEP como <mark style="background:#fff88f">substituto disfarçado da raça</mark> e discrimina da mesma forma.

**Viés de automação:** tendência de confiar nas decisões automatizadas da IA como sempre precisas ou imparciais, mesmo quando estão incorretas.

> [!warning]- Pendência de autoria
> A captura trazia a dúvida "discriminação algorítmica é a mesma coisa que viés algorítmico?" sem resposta. O material de origem escreve "Discriminação Algorítmica (Viés/Bias)", tratando os termos lado a lado. Confirmar se a banca os distingue.

⚠️ **Pegadinha CEBRASPE (item ERRADO):** um auditor usa IA generativa (IAG) na análise de informações de diferentes fontes e na redação dos achados de uma auditoria operacional em programa social para comunidades quilombolas. O item afirma que a IAG contribui para a imparcialidade porque, **desde que treinadas com grandes volumes de dados**, as ferramentas **não reproduzem** tendências humanas discriminatórias, como o racismo.

- A IA **pode** contribuir com a imparcialidade, mas reflete os dados com que foi treinada. Não está imune a reproduzir tendências discriminatórias, mesmo programada com essa diretriz.
- A IAG **herda** os vieses dos dados de treinamento, não os elimina.
- A imparcialidade em auditoria exige **julgamento humano crítico**, sobretudo em contextos sensíveis como políticas sociais.

O erro veio de tomar o enunciado por genérico demais e supor que a banca o aceitaria. O item é categórico ("não reproduzem").

#### Agentes de IA

- **Agente reativo simples (de reflexo simples):** realiza tarefas que **não exigem aprendizado**, previamente projetadas. Exemplos: redefinição de senhas; acionar o ar condicionado quando a temperatura ultrapassa a pré-programada.
- **Agente baseado em aprendizado:** o agente de IA que utiliza dados anteriores.

## IA Generativa: modelos de difusão
- [x] status [dom:: 2] [peso:: 3] ✅ 2026-09-12

Modelos generativos profundos: adicionam ruído gaussiano aos dados de treinamento (difusão direta) e depois invertem o processo, removendo o ruído (difusão reversa), para recuperar/gerar dados. O modelo aprende gradualmente a remover ruído, gerando novas imagens de alta qualidade a partir de sementes aleatórias.
⚠️ Modelos de difusão não fazem classificação (tarefa tradicional de ML que atribui uma classe a um conjunto de dados) — pertencem ao âmbito da <mark style="background:#fff88f">IA generativa</mark>, focada em gerar dados novos a partir de ruído.
> [!warning]- Pendência de autoria
> A captura original termina cortada em "É um processo mais complexo, portanto" — sem concluir a frase.

## Processamento de Linguagem Natural e LLMs
- [x] status [dom:: 2] [peso:: 3] ✅ 2026-09-12

LLMs avançaram o PLN e se tornaram acessíveis via interfaces como ChatGPT (GPT-3/GPT-4). Outros exemplos: <u>Llama, e os codificadores bidirecionais BERT e RoBERTa</u>.
GPT-3 (OpenAI, 2020): 175 bilhões de parâmetros — ficou famoso por gerar texto preciso a partir de entradas no ChatGPT.
Aplicações: responder perguntas, redigir textos, traduzir, resumir documentos, gerar código, chatbots e assistentes digitais — qualquer tarefa de geração ou compreensão de texto.

**Incorporações de palavras (word embeddings):** os LLMs representam as palavras por <mark style="background:#fff88f">vetores multidimensionais</mark>, de modo que palavras com significados contextuais semelhantes ou com outras relações fiquem **próximas entre si no espaço vetorial**. Com isso, os transformadores pré-processam o texto como representações numéricas por meio do **codificador** e entendem o contexto de palavras e frases de significado semelhante, bem como outras relações entre palavras, como partes do discurso. Os LLMs aplicam esse conhecimento da linguagem por meio do **decodificador** para produzir um resultado exclusivo. Item que descreve isso foi dado como CORRETO.

# Bloco E: Power BI, AED, Ferramentas de BI e Visualização de Dados, Ferramentas de análise de dados e observabilidade

## - Análise Exploratória de Dados (AED) — variáveis qualitativas e quantitativas
- [x] status [dom:: 2] [peso:: 3] ✅ 2026-09-12

Na classificação de variáveis em AED, os valores não numéricos são **qualitativos**, subdivididos em:

- **nominais** — categorias sem ordem (ex.: raça, cor);
- **ordinais** — categorias com ordem (ex.: tamanho de roupa, classe social).

⚠️ **Discreta não é subtipo de qualitativa** — é classificação de variável **quantitativa** (valores inteiros e contáveis). O erro clássico de banca troca "nominal" por "discreta" dentro da árvore de variáveis qualitativas.

## - Integração de Sistemas
- [ ] status [dom:: 0] [peso:: 3]

Integração de sistemas permite que aplicações distintas troquem dados e utilizem funcionalidades de maneira coordenada. Na administração tributária é fundamental porque as informações fiscais normalmente estão distribuídas entre diferentes sistemas internos, órgãos públicos e fontes externas.

```
SISTEMA A ↔ API / SERVIÇO / MENSAGERIA ↔ SISTEMA B
                    ↓
            TROCA DE INFORMAÇÕES
```

#### APIs

Uma <mark style="background:#fff88f">API (Application Programming Interface)</mark> estabelece regras e interfaces para que sistemas se comuniquem. Permite integração sem que uma aplicação precise ter acesso direto à implementação interna da outra.

| Benefício | Resultado |
| --- | --- |
| **Interoperabilidade** | Sistemas diferentes conseguem trocar informações. |
| **Automação** | Redução de tarefas manuais de transferência e redigitação. |
| **Atualização** | Possibilidade de fluxos de dados mais tempestivos. |
| **Reutilização** | Serviços podem ser consumidos por diferentes aplicações autorizadas. |

⚠️ **Pegadinha:** integração **não** significa simplesmente colocar todos os dados em um único banco. Sistemas podem permanecer independentes e interoperar por APIs, serviços, eventos ou outros mecanismos.

#### ETL × API

| ETL | API |
| --- | --- |
| Extrai, transforma e carrega dados; muito associado à integração de dados e a ambientes analíticos. | Define uma interface de comunicação entre aplicações e serviços. |
| Foco no fluxo e na preparação dos dados. | Foco na interação entre sistemas. |

## - Inteligência Fiscal
- [ ] status [dom:: 0] [peso:: 3]

**Inteligência fiscal** é o uso organizado de dados, técnicas analíticas e conhecimento especializado para produzir informação útil à gestão do risco tributário, à seleção de casos, à fiscalização e à promoção da conformidade.

```
COLETA
  ↓
INTEGRAÇÃO
  ↓
TRATAMENTO E QUALIDADE
  ↓
ANÁLISE / CRUZAMENTO / IA
  ↓
IDENTIFICAÇÃO DE RISCOS
  ↓
PRODUÇÃO DE INTELIGÊNCIA
  ↓
DECISÃO / AÇÃO
```

É mais ampla que uma tecnologia específica: pode usar BI, mineração de dados, inteligência artificial, geoprocessamento, cruzamentos, indicadores e conhecimento de especialistas.

⚠️ Inteligência fiscal ≠ simples acúmulo de dados. Os dados precisam ser tratados, contextualizados e analisados para virar informação útil à decisão.

| Nível | Conceito |
| --- | --- |
| **Dado** | Registro bruto de um fato. |
| **Informação** | Dado tratado e contextualizado. |
| **Conhecimento / Inteligência** | Interpretação capaz de apoiar decisões e ações. |

⭐ Pense como um ciclo: coletar → integrar → analisar → identificar riscos → priorizar → agir → avaliar resultados.

## - Business Intelligence e Analytics
- [ ] status [dom:: 0] [peso:: 3]

**Business Intelligence (BI)** é o conjunto de tecnologias, processos e práticas que transforma dados brutos em informações organizadas e visualmente compreensíveis, para apoiar a tomada de decisão. Segundo Turban, a arquitetura de BI tem quatro componentes:

| Componente | Função |
| --- | --- |
| **Data Warehouse** | repositório com os dados-fonte, já integrados e tratados |
| **Análise de Negócios** | ferramentas para manipular e analisar os dados do DW (inclui Data Mining) |
| **Business Performance Management (BPM)** | monitora e otimiza o desempenho, conectando metas estratégicas a indicadores (ex.: Balanced Scorecard) |
| **Interface de Usuário** | dashboards, portais e painéis que apresentam a informação de forma visual e interativa |

O **processo de BI** segue esse fluxo: **Data Sources** (ERP, CRM, planilhas, APIs — lógica OLTP) → **ETL** → **Data Warehouse** (ou EDW) → ferramentas de consulta, relatório e visualização.

⚠️ **BI clássico só faz análise descritiva e diagnóstica** ("o que aconteceu" e "por que aconteceu") — análise preditiva e prescritiva pertencem, a rigor, a Business Analytics, Data Science ou Analytics Avançado. Na prática, porém, ferramentas de BI (Power BI, Tableau, Qlik Sense) já embarcam funções preditivas simples.

**BI 3.0** é a fase que incorpora inteligência artificial para automatizar a tomada de decisão em tempo real.

O **dashboard** organiza a informação em três camadas: **monitoramento** (visão em tempo real), **análise** (exploração para gerar insight) e **gerenciamento** (apoio à decisão).

Em BI, vale a tríade: **dado** (registro bruto) → **informação** (dado organizado) → **conhecimento** (valor gerado a partir da informação, para apoiar a decisão).

> [!info]- Ponte
> A mesma tríade dado → informação → conhecimento aparece em [[#- Inteligência Fiscal|Inteligência Fiscal]] (linha 493), aplicada ao contexto fiscal. Ferramentas de mercado citadas aqui (Power BI, Tableau, Qlik Sense) reaparecem em [[#- Ferramentas de BI e Visualização de Dados|Ferramentas de BI e Visualização de Dados]], logo abaixo, e na dúvida sobre QlikView em `Erradas/ERRO P2 - Fluência de Dados CD.md` (heading Dúvidas respondidas).

## - Data Warehouse e Data Mart
- [ ] status [dom:: 0] [peso:: 3]

**Definições formais** — palavras-chave mais cobradas em prova:

| Autor | Definição |
| --- | --- |
| **Ralph Kimball** | conjunto de ferramentas e técnicas de projeto que, aplicadas às necessidades dos usuários e aos bancos de dados específicos, permitem planejar e construir um Data Warehouse |
| **Bill Inmon** | coleção de dados orientada por assunto, integrada, variável com o tempo e **não volátil**, para dar suporte à tomada de decisão |
| **Arun Sen** | banco de dados para suporte à decisão de negócios, com dados históricos sumarizados e consolidados a partir de bancos de dados operacionais |
| **Kenneth Laudon** | banco de dados — com ferramentas de consulta e relatório — que armazena dados atuais e históricos extraídos de vários sistemas, consolidados para análise e relatórios administrativos |

<mark style="background:rgba(240, 200, 0, 0.2)">Orientado por assunto</mark>: organizado por tema de negócio (Vendas, Clientes, Finanças), não por sistema. <mark style="background:rgba(240, 200, 0, 0.2)">Integrado</mark>: dados de várias fontes são padronizados e consolidados. <mark style="background:rgba(240, 200, 0, 0.2)">Variável no tempo</mark>: guarda a perspectiva histórica (ano, mês, dia). <mark style="background:rgba(240, 200, 0, 0.2)">Não volátil</mark>: depois de carregado via ETL, o dado não é alterado ou apagado individualmente — sem UPDATE/DELETE linha a linha, só atualização em ciclos.

**Tipos de repositório no ecossistema do DW:**

| Tipo | O que é |
| --- | --- |
| **Enterprise Data Warehouse (EDW)** | repositório corporativo centralizado, com dados de todas as áreas — a "fonte única da verdade" da empresa |
| **Operational Data Store (ODS)** | intermediário entre OLTP e o DW; atualização quase em tempo real, sem grande histórico, e pode permitir atualização direta (insert/update/delete) |
| **Data Mart (DM)** | subconjunto do DW dedicado a uma área (Vendas, RH, Finanças); mais simples e rápido que o EDW completo |

> [!tip]- Lupa: Data Mart dependente × independente (Inmon × Kimball)
> **A ideia em uma frase:** a banca cobra quem defende cada abordagem e a direção do fluxo de dados.
> 
> **O passo a passo:** no modelo **dependente** (Top-Down, Bill Inmon), o Data Mart nasce **depois** do EDW — puxa dados já integrados e limpos dele, o que dá mais governança mas exige que o EDW já exista. No modelo **independente** (Bottom-Up, Ralph Kimball), o Data Mart é construído **direto dos sistemas transacionais**, sem depender de um DW central — implantação mais rápida, mas com risco de inconsistência entre Data Marts e de "ilhas de informação" (data silos). O modelo **híbrido** combina os dois: recebe dados do DW e de fontes operacionais.
> 
> **O erro clássico:** trocar a autoria (dizer que Kimball defende o Top-Down ou Inmon o Bottom-Up) ou afirmar que o modelo independente sempre é pior — ele só troca governança por velocidade de implantação.

#### Data Lake

O Data Lake adota **schema-on-read**: os dados entram brutos e só são estruturados quando alguém precisa usá-los. O Data Warehouse, ao contrário, exige **schema-on-write**: a modelagem vem antes do armazenamento.

⚠️ Sem governança, catalogação, controle de acesso e versionamento, o Data Lake vira um **Data Swamp** (pântano de dados): arquivos duplicados, dados desatualizados, sem metadados e sem utilidade prática.

| Critério | Data Warehouse | Data Lake |
| --- | --- | --- |
| Tratamento dos dados | extraídos, transformados e só então carregados (ETL) | carregados brutos, transformados depois (ELT) |
| Tipo de dados | principalmente estruturados | estruturados, semiestruturados (JSON, XML) e não estruturados (imagem, áudio, vídeo, log) |
| Usuários | analistas de BI, gestores | cientistas e engenheiros de dados, IA/ML |
| Esquema | schema-on-write | schema-on-read |
| Objetivo | relatórios, dashboards, indicadores (KPI) | exploração, Machine Learning, Big Data |

> [!info]- Ponte
> A dúvida #3116008 (QlikView) em `Erradas/ERRO P2 - Fluência de Dados CD.md` troca justamente ferramenta de BI por componente técnico (OLAP, DW, ETL) — o mesmo cuidado vale aqui: Data Lake e Data Warehouse são repositórios, não ferramentas.

## - OLAP × OLTP
- [ ] status [dom:: 0] [peso:: 3]

| Característica | OLTP (dados operacionais) | OLAP (dados informacionais) |
| --- | --- | --- |
| Finalidade | suporte a operações do dia a dia (transações) | suporte à análise, decisão e relatórios |
| Conteúdo dos dados | valores atuais/detalhados, registro a registro | dados sumarizados, históricos, integrados de várias fontes |
| Organização | por aplicação/processo (sistema de vendas, RH) | por assunto/tema de negócio (Vendas, Clientes, Finanças) |
| Natureza | dinâmica (muda constantemente) | estática ou historizada (só muda em ciclos de carga) |
| Modelo de dados | relacional, normalizado (3FN) | dimensional (fatos e dimensões), desnormalizado |
| Atualização | CRUD frequente (INSERT/UPDATE/DELETE) | carregamento em lote (ETL/ELT), sem UPDATE direto na maior parte dos casos |
| Tempo de resposta | milissegundos a menos de 1 segundo | segundos a minutos, conforme a complexidade |
| Usuários típicos | operadores, sistemas de cadastro | gestores, analistas, BI, cientistas de dados |

> [!info]- Ponte
> O detalhamento dos tipos de armazenamento OLAP (MOLAP/ROLAP/HOLAP), das variações de acesso (DOLAP/WOLAP) e das operações sobre o cubo (slice, dice, pivot, drill down/up/across/through) está em [[P2 - Fluência de Dados BD#- OLAP e suas diferenças com OLTP|P2 - Fluência de Dados BD]] — não repito aqui para não duplicar.

## - ETL (Extração, Transformação e Carga)
- [ ] status [dom:: 0] [peso:: 3]

O ETL é considerado uma das etapas mais críticas e demoradas de um projeto de Data Warehouse: estima-se que **70% a 80%** do esforço total do projeto esteja no ETL, e que cerca de **60%** do esforço do próprio ETL esteja só na **extração** — os dados vêm espalhados em sistemas, planilhas, APIs e bancos legados, cada um exigindo captura e conversão diferentes.

Entre a extração e a carga, os dados passam pela **Staging Area** (ou ODS/Staging): uma zona técnica e temporária, não acessível a usuários finais, onde ocorrem limpeza, padronização de formatos (ex.: "SP", "São Paulo", "S. Paulo" viram um só padrão), remoção de duplicidades e verificação de integridade, antes da carga no DW.

Depois da carga inicial (todo o histórico disponível), o mais comum é a **carga incremental**: carregar só o que é novo ou mudou desde a última atualização, usando técnicas como *timestamp*, logs de transação ou **Change Data Capture (CDC)**.

> [!tip]- Lupa: ETL × ELT
> **A ideia em uma frase:** as duas siglas levam dados de sistemas transacionais a um ambiente analítico — a diferença é **onde** a transformação acontece.
> 
> **O passo a passo:** no **ETL**, a ordem é Extrair → **Transformar** → Carregar: os dados só entram no destino (DW) depois de tratados. No **ELT**, a ordem é Extrair → Carregar → **Transformar**: os dados brutos vão primeiro para o repositório (DW, Data Lake ou Lakehouse) e são transformados **dentro** dele, sob demanda, geralmente com processamento paralelo em nuvem (MPP). O ELT virou tendência porque armazenamento e processamento em nuvem ficaram baratos e rápidos, permitindo guardar tudo bruto (schema-on-read) e deixar analistas transformarem via SQL/BI, sem depender só de engenheiros de dados.
> 
> **O erro clássico:** achar que ELT substitui ETL — na prática convivem em arquiteturas híbridas (ETL para dados críticos/legados, ELT para Big Data em nuvem); e esquecer que o ELT também tem risco, o de virar Data Swamp se faltar governança.

> [!info]- Ponte
> A distinção **ETL × API** (fluxo de dados × interface de comunicação entre sistemas) está em [[#- Integração de Sistemas|Integração de Sistemas]] (linha 459) — é outro corte, não confundir com ETL × ELT acima.

## - Ferramentas de BI e Visualização de Dados
- [ ] status [dom:: 0] [peso:: 3]

Ferramentas de mercado citadas como exemplo de BI: **Power BI**, **Tableau**, **Qlik Sense** e **Excel avançado**.

> [!warning]- Pendência de autoria
> O material-fonte só cita esses nomes, sem comparar recursos, licenciamento ou arquitetura entre eles. Para um heading mais completo (o que cada ferramenta faz de diferente), falta capturar material específico sobre BI de mercado.

> [!info]- Ponte
> A dúvida #3116008, em `Erradas/ERRO P2 - Fluência de Dados CD.md` (heading Dúvidas respondidas), erra justamente ao confundir OLAP (componente técnico) com QlikView (ferramenta) — a pegadinha central deste heading. Ver também [[#- Business Intelligence e Analytics|Business Intelligence e Analytics]], que já cita as mesmas ferramentas.

## - Mapa de Fixação
- [ ] status [dom:: 0] [peso:: 3]

| Se a questão falar em... | Pense em... |
| --- | --- |
| Aprender padrões, classificar ou prever | IA / Machine Learning |
| Comparar informações de fontes distintas | Cruzamento de Dados |
| Gráficos, KPIs, filtros e acompanhamento visual | Painel Gerencial |
| Medir desempenho, arrecadação, conformidade ou risco | Indicador Fiscal |
| Coordenadas, parcelas, mapas e análise espacial | Georreferenciamento / SIG |
| Comunicação e troca de dados entre aplicações | Integração de Sistemas / APIs |
| Transformar dados e análises em apoio à ação fiscal | Inteligência Fiscal |
| Regras automáticas que identificam divergências | Automação de Malhas Fiscais |





---



