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
- [ ] status [dom:: 0] [peso:: 3]

- Segundo a Open Knowledge Foundation - OKFn, “**dados são abertos** quando qualquer pessoa pode livremente usá-los, reutilizá-los e redistribuí-los, estando sujeito a, no máximo, a exigência de creditar a sua autoria e compartilhar pela mesma licença”. Quando os dados são produzidos, coletados ou custodiados por autoridades públicas e disponibilizados em formato aberto, diz-se que são dados abertos governamentais. Ainda segundo a OKFn, dados abertos também são pautados por três leis e oito princípios:

	Em 2007, um grupo de trabalho de 30 pessoas reuniu-se na Califórnia, Estados Unidos da América, para definir os princípios dos Dados Abertos Governamentais. Chegaram num consenso sobre os seguintes 8 princípios:
1. **Completos.** Todos os dados públicos são disponibilizados. Dados são informações eletronicamente gravadas, incluindo, mas não se limitando a, documentos, bancos de dados, transcrições e gravações audiovisuais. Dados públicos são dados que não estão sujeitos a limitações válidas de privacidade, segurança ou controle de acesso, reguladas por estatutos.
2. **Primários.** Os dados são publicados na forma coletada na fonte, **com a mais fina granularidade possível, e não de forma agregada ou transformada.**
3. **Atuais.** Os dados são disponibilizados o quão rapidamente seja necessário para preservar o seu valor.
4. **Acessíveis.** Os dados são disponibilizados para o público mais amplo possível e para os propósitos mais variados possíveis.
5. **Processáveis por máquina.** Os dados são **razoavelmente estruturados para possibilitar o seu processamento automatizado.**
6. **Acesso não discriminatório.** Os dados estão disponíveis a todos, sem que seja necessária identificação ou registro.
7. **Formatos não proprietários.** Os dados estão disponíveis em um formato sobre o qual nenhum ente tenha controle exclusivo.
8. **Licenças livres.** Os dados não estão sujeitos a restrições por regulações de direitos autorais, marcas, patentes ou segredo industrial. Restrições razoáveis de privacidade, segurança e controle de acesso podem ser permitidas na forma regulada por estatutos.

	**Descreva as características de dados abertos:** 1)Reuso e redistribuição:; 2)isponibilidade e acesso; 3)articipação universal.
- **Reuso e Redistribuição**: Dados abertos são disponibilizados de forma a permitir seu uso e redistribuição sem restrições, desde que respeitados os direitos autorais e outras leis aplicáveis. Isso significa que qualquer pessoa pode utilizar, modificar e compartilhar os dados abertos sem precisar de autorização prévia ou pagar taxas adicionais.
- **Disponibilidade e Acesso:** Dados abertos devem estar disponíveis de forma acessível e fácil, sem barreiras técnicas ou comerciais que impeçam o acesso. Isso inclui a disponibilidade de metadados, documentação e formatos de arquivo apropriados para seu uso e reutilização.
- **Participação Universal:** A ideia por trás dos dados abertos é fomentar a colaboração, a inovação e a participação universal na sociedade. Todos devem ter acesso e liberdade para utilizar, compartilhar e contribuir com os dados abertos, independentemente de sua localização, capacidade financeira ou outros fatores. Essa abertura e acessibilidade permitem que todos tenham a chance de aprender, colaborar e construir soluções juntos, independentemente das fronteiras.

>**accessURL → acesso direto ao dado**  
**landingPage → página explicativa**  
**contactPoint → contato**  
**endpointURL → API/serviço**



## -  3 Ciclo de Vida dos Dados: coleta, armazenamento, processamento, compartilhamento, retenção e descarte.
- [ ] status [dom:: 0] [peso:: 3]

 **ILM (Information Lifecycle Management)**, ou **Gestão do Ciclo de Vida da Informação**, é um conjunto de políticas, processos e tecnologias usados para gerenciar as informações (dados) ao longo de todo o seu ciclo de vida – desde a criação até a destruição. O ILM busca garantir que os dados sejam armazenados, acessados e descartados de forma eficiente, segura e em conformidade com regulamentos e políticas organizacionais.

Aqui estão os principais **estágios do ciclo de vida da informação** no ILM:

1. **Criação/Captura:** Dados são criados ou coletados (por exemplo, e-mails, registros financeiros, relatórios).
    
2. **Armazenamento:** Os dados são armazenados de forma eficiente, considerando custo e performance (em armazenamento primário, secundário, nuvem, etc.).
    
3. **Uso/Distribuição:** Os dados são utilizados em operações, decisões, relatórios e análises.
    
4. **Retenção:** Os dados são mantidos conforme requisitos legais, regulatórios e de negócios. Aqui entram políticas de compliance e auditoria.
    
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

| Tarefa                          | Descrição                                                                          | Quando Usar                                                                         | Benefícios                                                                               | Exemplo                                                                               |
| ------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Anonimização**                | Remoção ou substituição de informações identificáveis para proteger a privacidade. | Usar ao trabalhar com dados sensíveis para cumprir regulamentos de privacidade.     | Protege a privacidade dos indivíduos, conforme GDPR ou outras leis de proteção de dados. | Remoção de nomes e endereços de um conjunto de dados de pacientes.                    |
| **Discretização**               | Transformação de variáveis contínuas em categorias discretas.                      | Usar quando variáveis contínuas precisam ser agrupadas em intervalos ou categorias. | Facilita a análise de dados categóricos e a construção de modelos de classificação.      | Transformação de idades em grupos etários (0-18, 19-35, 36-50, etc.).                 |
| **Normalização**                | Ajuste dos valores das variáveis para um intervalo comum.                          | Usar quando variáveis têm escalas diferentes e precisam ser comparáveis.            | Melhora o desempenho de algoritmos de aprendizado de máquina.                            | Escalonamento de dados de renda anual para um intervalo de 0 a 1.                     |
| **Padronização**                | Transformação de dados para ter média zero e desvio padrão de um.                  | Usar quando variáveis precisam ter distribuição normal.                             | Necessário para algoritmos que assumem normalidade dos dados, como PCA.                  | Ajuste de notas de teste para terem média zero e desvio padrão de um.                 |
| **Imputação**                   | Substituição de valores ausentes por estimativas.                                  | Usar quando há dados ausentes que precisam ser preenchidos.                         | Mantém a integridade do conjunto de dados, evitando a perda de informações.              | Preenchimento de valores ausentes de renda com a média da renda conhecida.            |
| **Agregação**                   | Combinação de múltiplas observações em resumos estatísticos.                       | Usar para simplificar grandes volumes de dados.                                     | Facilita a visualização e a análise de grandes conjuntos de dados.                       | Cálculo da média mensal de vendas a partir de dados diários.                          |
| **Codificação**                 | Transformação de dados categóricos em formatos numéricos.                          | Usar quando variáveis categóricas precisam ser usadas em modelos matemáticos.       | Permite a inclusão de dados categóricos em algoritmos de aprendizado de máquina.         | One-hot encoding de variáveis de gênero (masculino, feminino).                        |
| **Redução de Dimensionalidade** | Simplificação de conjuntos de dados reduzindo o número de variáveis.               | Usar para melhorar a performance e a interpretabilidade de modelos.                 | Reduz a complexidade do modelo, prevenindo overfitting.                                  | PCA (Análise de Componentes Principais) para reduzir variáveis de entrada.            |
| **Remoção de Outliers**         | Identificação e eliminação de valores anômalos que distorcem a análise.            | Usar quando outliers prejudicam a precisão do modelo ou análise.                    | Melhora a precisão dos modelos e a qualidade da análise.                                 | Remoção de valores de temperatura extremamente altos/baixos que são erros de medição. |
**1.5 Tipos de Dados Ausentes**

|Tipo de Dados Ausentes|Características|Métodos Recomendados|Exemplos|
|---|---|---|---|
|**MCAR** _(Missing Completely at Random)_|Dados ausentes não dependem de nenhuma variável observada ou não observada; ausências são aleatórias.|Exclusão de casos, imputação simples.|Dados de sensores falhando **aleatoriamente** em diferentes momentos sem relação com as condições ambientais ou o funcionamento do sensor.|
|**MAR** _(Missing at Random)_|Dados ausentes podem ser explicados por outras variáveis observadas; a ausência não é completamente aleatória, mas pode ser prevista com base em outras informações disponíveis.|Imputação múltipla, modelagem estatística que aproveita as relações observadas.|Em um estudo médico, dados ausentes sobre a pressão arterial podem ser **previstos** com base em outras variáveis, como idade ou peso do paciente.|
|**MNAR** _(Missing Not at Random)_|Dados ausentes dependem da própria variável ausente ou de outras variáveis não observadas; as ausências têm um padrão específico.|Modelagem de equações estruturais, métodos bayesianos, modelagem direta do padrão de ausência.|Em um estudo de renda, pessoas com rendas muito altas ou muito baixas podem optar por não reportar seus rendimentos, e essa ausência está **relacionada diretamente ao valor da própria renda**.|

**1.6 Atributos dos Dados**

- **Relevância, Cobertura, Profundidade, Custo, História (duração), Frequência, Processamento, Custo de aquisição**: Estes atributos ajudam a avaliar a utilidade, aplicabilidade, custo e qualidade dos dados. São essenciais para entender o valor e as limitações dos dados em diferentes contextos.

|Atributo|Definição|
|---|---|
|**Relevância**|Utilidade de um conjunto de dados para propósitos específicos.|
|**Cobertura**|Área geográfica abrangida pelo conjunto de dados.|
|**Profundidade**|Variedade e número de diferentes pontos de dados no conjunto.|
|**Custo de Dados**|Custo de acesso e processamento do conjunto de dados.|
|**História**|Alcance histórico do conjunto de dados.|
|**Frequência**|Intervalo de tempo entre pontos de dados e frequência de atualização.|
|**Processamento**|Quantidade de correção de erros e rotulagem antes da distribuição.|
|**Custo de aquisição**|Custo de aquisição e verificação dos dados em sua forma original.|

## -  4 Governança de Dados: papéis, políticas, accountability, stewardship e alinhamento estratégico.
- [ ] status [dom:: 0] [peso:: 3]

**De acordo com o DAMA DMBOK, a governança de dados tem como objetivo central habilitar a organização a gerenciar seus dados como ativos valiosos, exigindo _accountability_ (responsabilização), controle e regras bem definidas, de forma alinhada aos objetivos do negócio.**
Veja os erros das outras opções:
**A:** A governança não é um programa estritamente tecnológico ou de TI. As responsabilidades são compartilhadas entre a área de tecnologia e as áreas de negócio.  
**B:** A ética na manipulação de dados é um pilar estrutural do gerenciamento de dados que se aplica a todo o seu ciclo de vida, e não apenas a modelos de aprendizado de máquina.  
**C:** A governança exerce autoridade, supervisão e controle. A execução técnica e operacional (como realizar o processo de ETL) cabe a outras áreas de conhecimento, como a Integração de Dados.  
**D:** Os _data stewards_ (mordomos de dados) atuam e são responsáveis diretamente _dentro_ da área de negócios da organização, não sendo necessariamente especialistas externos independentes.


## - 5 Qualidade de Dados: completude, consistência, acurácia, unicidade, atualidade e integridade.
- [ ] status [dom:: 0] [peso:: 3]

## - 6 DMBOK: áreas de conhecimento, governança, arquitetura de dados, metadados, qualidade, segurança e master data.
- [ ] status [dom:: 0] [peso:: 3]


# Bloco B: Data mining, CSV, XML, JSON, CRISP-DM
 **Ténicas de Pré-Processamento:**

**Limpeza dos Dados –** Preenche valores faltantes, suaviza dados ruidosos, identifica ou remove “outliers” e resolve inconsistências.
**Integração –** Dados de origens diferentes devem ser integrados. Resolver conflitos e redundância
**Transformação –** Normalização e agregação dos dados.
**Redução -** Tenta reduzir o volume de dados sem provocar grandes alterações no resultado. Compressão de atributos e redução do número de dados.
<mark style="background:rgba(240, 200, 0, 0.2)">Discretização</mark> – Faz parte do processo de redução, mas tem papel importante, especialmente com dados numéricos. <font color="#ff0000">Visa estabelecer valores discretos para variáveis contínuas.</font>
## XML
- [ ] status [dom:: 0] [peso:: 3]
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
- [ ] status [dom:: 0] [peso:: 3]
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

--**b)**  o XML _Schema_ é adequado para validar tanto a estrulura quanlo os valores dos elementos em um documento XML.
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
- [ ] status [dom:: 0] [peso:: 3]

Duas categorias de anomalias, por origem: <mark style="background:#fff88f">não intencionais</mark> (desvio da norma por erro ou ruído na coleta — sensor defeituoso, erro humano) e <mark style="background:#fff88f">intencionais</mark> (desvio por ação ou evento real, ex.: pico de vendas em época festiva).

Três subtipos, por escopo (podem ser intencionais ou não intencionais):
- **Pontuais** (outliers globais) — ponto individual muito fora do restante do conjunto. Ex.: saque bancário muito acima do padrão do usuário.
- **Contextuais** — não são outliers isolados, mas destoam dentro de um contexto específico (hora do dia, local). Ex.: pico de consumo de energia ao meio-dia, quando a casa costuma estar vazia.
- **Coletivas** — um conjunto de instâncias que, juntas, destoam da norma, mesmo com cada instância parecendo normal isoladamente. Ex.: aumento simultâneo de tráfego de rede vindo de vários IPs.

## Espaço Latente
- [ ] status [dom:: 0] [peso:: 3]

Representação abstrata e compactada dos dados, usada por algoritmos de aprendizado de máquina em vez das informações brutas e de alta dimensionalidade (ex.: cada pixel de uma imagem) — foca nas características essenciais, descobrindo padrões e relações ocultas.

## LSTM (Long Short-Term Memory)
- [ ] status [dom:: 0] [peso:: 3]

Arquitetura de rede neural recorrente (RNN) que retém valores por intervalos arbitrários — adequada para classificar, processar e prever séries temporais com gaps de duração desconhecida. A insensibilidade ao comprimento do gap dá vantagem à LSTM sobre RNNs tradicionais ("vanilla"), Modelos Ocultos de Markov (MOM) e outros métodos de aprendizado de sequências.

# Bloco D: PLN, IA e LLMs

## Conceitos Iniciais e Gerais de IA
- [ ] status [dom:: 0] [peso:: 3]

<mark style="background:#fff88f">IA Fraca (Estreita)</mark>: modela a inteligência humana para tarefas específicas, sem habilidades cognitivas completas — opera só dentro de um conjunto de funções predefinidas, sem desviar do caminho programado. Ex.: assistentes de voz (Siri, Alexa) classificam dados e respondem consultas rapidamente, mas não realizam tarefas fora do escopo treinado.
> [!warning]- Pendência de autoria
> A captura original citava "8 exemplos práticos de IA fraca/estreita" mas só trouxe o primeiro (assistentes de voz). Completar com os outros 7 se for revisar o material de origem.

<mark style="background:#fff88f">IA deve seguir as leis de proteção de dados do país onde for utilizada e comercializada</mark>, independentemente de onde foi desenvolvida ou fabricada — a legislação aplicável é a do local de uso, não a de origem.

## IA Generativa: modelos de difusão
- [ ] status [dom:: 0] [peso:: 3]

Modelos generativos profundos: adicionam ruído gaussiano aos dados de treinamento (difusão direta) e depois invertem o processo, removendo o ruído (difusão reversa), para recuperar/gerar dados. O modelo aprende gradualmente a remover ruído, gerando novas imagens de alta qualidade a partir de sementes aleatórias.
⚠️ Modelos de difusão não fazem classificação (tarefa tradicional de ML que atribui uma classe a um conjunto de dados) — pertencem ao âmbito da <mark style="background:#fff88f">IA generativa</mark>, focada em gerar dados novos a partir de ruído.
> [!warning]- Pendência de autoria
> A captura original termina cortada em "É um processo mais complexo, portanto" — sem concluir a frase.

## Processamento de Linguagem Natural e LLMs
- [ ] status [dom:: 0] [peso:: 3]

LLMs avançaram o PLN e se tornaram acessíveis via interfaces como ChatGPT (GPT-3/GPT-4). Outros exemplos: Llama, e os codificadores bidirecionais BERT e RoBERTa.
GPT-3 (OpenAI, 2020): 175 bilhões de parâmetros — ficou famoso por gerar texto preciso a partir de entradas no ChatGPT.
Aplicações: responder perguntas, redigir textos, traduzir, resumir documentos, gerar código, chatbots e assistentes digitais — qualquer tarefa de geração ou compreensão de texto.

# Bloco E: Power BI, AED, Ferramentas de BI e Visualização de Dados, Ferramentas de análise de dados e observabilidade

## - Análise Exploratória de Dados (AED) — variáveis qualitativas e quantitativas
- [ ] status [dom:: 0] [peso:: 3]

Na classificação de variáveis em AED, os valores não numéricos são **qualitativos**, subdivididos em:

- **nominais** — categorias sem ordem (ex.: raça, cor);
- **ordinais** — categorias com ordem (ex.: tamanho de roupa, classe social).

⚠️ **Discreta não é subtipo de qualitativa** — é classificação de variável **quantitativa** (valores inteiros e contáveis). O erro clássico de banca troca "nominal" por "discreta" dentro da árvore de variáveis qualitativas.





---



