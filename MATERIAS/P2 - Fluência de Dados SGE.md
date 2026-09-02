---
disciplina: Fluência de Dados SGE
prova: II
peso: 3
pontos: 0
origem: CE 2026 (novidade FCC)
prioridade: importante
---


> ****Zero na âncora BA 2019** — disciplina nova, introduzida pela FCC em CE 2026**
> Prioridade: **importante**

A grande novidade dos editais fiscais recentes. Substitui a antiga "Noções de Informática" por algo bem mais próximo do trabalho real de um auditor: análise de dados aplicada à seleção de contribuintes e ao cruzamento de informações fiscais.

Se aparecer no edital baiano, é bloco de vantagem quase total: material escasso, concorrência sem repertório, e conteúdo que dialoga direto com Estatística e Auditoria.

# - Bloco A: Seg. da Inf: Principios; Malwares; Antispyware; Backup

## 1. Resumo Teórico 

A Segurança da Informação (SI) é um conjunto de práticas, políticas, procedimentos e controles que visam proteger os ativos de informação de uma organização contra diversas ameaças. O objetivo é garantir a continuidade dos negócios, minimizar os riscos e maximizar o retorno sobre os investimentos e as oportunidades.

### Conceitos Fundamentais

- Ativo de Informação: Qualquer informação ou recurso que tenha valor para a organização (dados, hardware, software, pessoas, imagem da empresa, etc.).
- Ameaça: Qualquer evento ou ação potencial que possa causar dano aos ativos de informação (ex: malware, desastres naturais, erro humano, ataque intencional).
- Vulnerabilidade: Uma fraqueza em um ativo ou controle que pode ser explorada por uma ou mais ameaças.
- Risco: A probabilidade de uma ameaça explorar uma vulnerabilidade e o impacto resultante para a organização.
- Impacto: O prejuízo ou consequência resultante da materialização de um risco.

### Princípios Básicos (Pilares da Segurança da Informação)

Os pilares fundamentais da Segurança da Informação são frequentemente lembrados pelo mnemônico CID (ou CIDA, incluindo Autenticidade):

- **Confidencialidade:** Garante que a informação seja acessível somente por pessoas, entidades ou processos autorizados. É a proteção contra o acesso não autorizado. Pense em "segredo".
    - _Exemplo:_ Criptografar um e-mail para que apenas o destinatário possa lê-lo.
- **Integridade:** Garante a exatidão, completeza e a não modificação não autorizada da informação e dos métodos de processamento. A informação deve ser mantida em seu estado original e confiável. Pense em "originalidade" ou "exatidão".
    - _Exemplo:_ Usar uma função hash para verificar se um arquivo foi alterado durante o download.
- **Disponibilidade:** Garante que os usuários autorizados tenham acesso à informação e aos ativos associados sempre que necessário. A informação deve estar acessível quando solicitada. Pense em "acesso garantido".
    - _Exemplo:_ Ter servidores redundantes para que um sistema continue funcionando mesmo se um servidor falhar.

### Outros Atributos Essenciais

- Autenticidade: Garante que a identidade de um usuário, processo, sistema ou informação seja aquela que se alega ser. É a prova da origem ou da identidade.
    - _Exemplo:_ Um login e senha para acessar um sistema.
- Não Repúdio (Irretratabilidade): Garante que uma entidade não possa negar a autoria de uma ação ou transação que realizou. Oferece prova da origem e da entrega.
    - _Exemplo:_ Uma assinatura digital em um contrato eletrônico impede que o signatário negue ter assinado.
- Conformidade (Legalidade): Garante que as ações e os controles de segurança estejam de acordo com as leis, regulamentos, normas e obrigações contratuais.
- Responsabilização (Accountability): Garante que as ações de uma entidade possam ser rastreadas unicamente até essa entidade. Permite auditoria e identificação de responsáveis.

## 2. Principais Temas Cobrados em Concursos

Com base na análise de questões de diversas bancas, os seguintes tópicos são frequentemente abordados:

- A Tríade CID (Confidencialidade, Integridade, Disponibilidade): Definição, aplicação em cenários e diferenciação entre eles. É o tema mais central.
- **Identificação de Violações:** Questões que apresentam um incidente (ex: vazamento de dados, alteração de informações, sistema indisponível) e pedem para identificar qual(is) princípio(s) foi(ram) violado(s).
- **Autenticidade e Não Repúdio:** Conceitos, diferenças e mecanismos associados (ex: senhas, tokens, biometria para autenticidade; assinatura digital para não repúdio).
- **Mecanismos de Segurança e seus Princípios:**
    - Criptografia: Associada principalmente à Confidencialidade.
    - Funções Hash (Resumo): Associadas principalmente à Integridade.
    - Assinatura Digital: Garante Autenticidade, Integridade e Não Repúdio.
    - Certificados Digitais: Usados para Autenticidade.
    - Firewalls e IDS/IPS: Contribuem para Confidencialidade (controle de acesso) e Disponibilidade (proteção contra ataques).
    - Backups e Planos de Continuidade: Essenciais para a Disponibilidade e recuperação da Integridade.
- **Autenticação Multifator (MFA):** Conceito e importância como camada adicional de segurança para a Autenticidade.
- **Outros Atributos:** Embora menos frequentes que a tríade CID, conceitos como Legalidade/Conformidade e Responsabilização podem aparecer.

**Dica de Ouro: Dominando a Tríade!**

A maioria das questões gira em torno da Tríade CID. Entender profundamente cada pilar e como eles se manifestam em situações práticas é crucial. Por exemplo, se um CPF é alterado indevidamente em um cadastro, houve falha na Integridade. Se dados sigilosos de um processo são acessados por alguém não autorizado, a Confidencialidade foi comprometida. Se um sistema fica fora do ar devido a um ataque, a Disponibilidade foi afetada.

## 3. Pontos de Atenção e Dificuldades Comuns

Candidatos frequentemente encontram dificuldades em:

- **Diferenciar sutilmente os pilares da Tríade CID em cenários complexos.**
    - _Exemplo:_ Um dado pode estar disponível, mas corrompido (falha na Integridade, não necessariamente na Disponibilidade de acesso ao dado corrompido).
- **Confundir Autenticidade com Não Repúdio.**
    - Autenticidade prova quem você é. Não Repúdio prova que você fez algo e não pode negar.
- **Associar corretamente mecanismos de segurança aos princípios que eles garantem.**
    - _Exemplo:_ Criptografia assimétrica (chaves pública/privada) é fundamental para assinaturas digitais, que por sua vez garantem Autenticidade, Integridade e Não Repúdio.
- **Interpretar termos sinônimos:** Irretratabilidade é o mesmo que Não Repúdio.

**Dica de Ouro: Mnemônico CIDA + NR!**

Para memorizar os principais atributos, pense em CIDA + NR:

- **C**onfidencialidade: Só acessa quem pode (segredo).
- **I**ntegridade: Informação correta e completa (exatidão).
- **D**isponibilidade: Acesso garantido quando necessário (sempre ligado).
- **A**utenticidade: É quem diz ser (identidade verdadeira).
- **NR**(Não Repúdio): Não pode negar que fez (prova da ação).

**Dica de Ouro: Integridade vs. Confidencialidade na Prática!**

Imagine um arquivo confidencial. Se alguém não autorizado o acessa, a Confidencialidade é quebrada. Se alguém altera o conteúdo desse arquivo (autorizado ou não, mas sem que a alteração seja legítima/esperada), a Integridade é afetada. Se o arquivo é deletado e não há backup, a Disponibilidade é comprometida.

**Dica de Ouro: O que NÃO é um atributo básico?**

Algumas questões tentam confundir com termos que parecem relacionados, mas não são atributos fundamentais da SI. Por exemplo, "Presteza" ou "Flexibilidade" não são usualmente reconhecidos como atributos básicos da SI no mesmo nível de CIDANR.

**VULNERABILIDADE, AMEAÇA E RISCO**
- Vulnerabilidade: é uma falha ou fraqueza que pode ser explorada por uma ameaça.
- Ameaça: é um evento ou ação que pode causar danos, explorando uma vulnerabilidade.
- Risco: é a probabilidade de uma ameaça se concretizar e causas danos.


## 4. Estratégias de Resolução de Questões

- **Identifique Palavras-Chave:**
    - "Acesso não autorizado", "vazamento", "sigilo", "privacidade": Confidencialidade.
    - "Alteração", "modificação", "corrupção", "exatidão", "consistência": Integridade.
    - "Indisponível", "fora do ar", "acesso negado (quando deveria ser permitido)", "continuidade": Disponibilidade.
    - "Identidade", "verificar quem é", "origem": Autenticidade.
    - "Não poder negar", "prova de autoria", "assinatura": Não Repúdio.
- **Analise o Cenário Completo:** Em questões situacionais, leia atentamente a descrição do incidente. Pergunte-se: "Qual foi o principal problema ou falha de segurança ocorrido?"
    - Se a informação foi lida por quem não devia: Confidencialidade.
    - Se a informação foi alterada indevidamente: Integridade.
    - Se a informação/sistema não pôde ser acessado: Disponibilidade.
- **Processo de Eliminação:** Em questões de múltipla escolha, descarte as alternativas que claramente não se aplicam.
- **Cuidado com Generalizações:** Uma medida de segurança pode contribuir para múltiplos princípios, mas as questões geralmente focam no principal objetivo do mecanismo. Por exemplo, um backup (Disponibilidade) também ajuda a restaurar a Integridade após um incidente.
- **Lembre-se das Ferramentas:**
    - Criptografia é a rainha da Confidencialidade.
    - Hash é o guardião da Integridade.
    - Assinatura Digital é o trio Autenticidade + Integridade + Não Repúdio.

- #pegadinha 

**Dica de Ouro: Questões de "Certo ou Errado" (CESPE/Cebraspe)**
Nesse tipo de questão, cada detalhe importa. Se uma afirmativa diz que "A disponibilidade garante o acesso por terceiros interessados, independentemente de autorização", está ERRADO, pois disponibilidade é para usuários AUTORIZADOS. A falta da palavra "autorizado" ou a inclusão de "independentemente de autorização" muda tudo.

**Dica de Ouro: Múltiplas Violações**
Um único incidente pode violar múltiplos princípios. Por exemplo, um invasor acessa dados confidenciais (Confidencialidade), altera esses dados (Integridade) e depois apaga os logs para esconder seus rastros (afetando a Responsabilização e dificultando a análise da Autenticidade das ações).



## BACKUP

A questão cobra o **tema backups.** Existem três tipos de backup, a saber: **completo, diferencial e incremental.** No backup completo, todos os dados são salvos, independente de quaisquer condições. No backup incremental, adiciona-se um pequeno incremento ao backup completo ou ao backup incremental anterior. Por fim  , **no backup diferencial, não são marcadas as "flags"**  de registro dos dados. Dessa maneira, ele não consegue reconhecer outros backups diferenciais e por esse motivo pega todos os dados após o último backup completo, mesmo que tenha sido executado um backup diferencial anterior.

**Ransomware** é um tipo de software malicioso (malware) que "sequestra" o computador ou os dados da vítima. Ele bloqueia o acesso ao sistema ou criptografa os arquivos importantes e, em seguida, exige o pagamento de um resgate (em inglês, _ransom_) para que o acesso seja restabelecido.
> Como devo me proteger de **_ransomware_**?
> Entendido! Quer que eu organize esses itens ou ajude a lembrar de mais alguma coisa?

   Para se proteger de _ransomware_ você deve tomar os mesmos cuidados que toma para evitar os outros códigos maliciosos, como:
- manter o sistema operacional e os programas instalados com todas as atualizações aplicadas;
- ter um antivírus instalado;
- ser cuidadoso ao clicar em _links_ ou abrir arquivos.
Fazer _backups_ regularmente também é essencial para proteger os seus dados pois, **se seu equipamento for infectado, a única garantia de que você conseguirá acessá-los novamente é possuir _backups_ atualizados**. **O pagamento do resgate não garante que você conseguirá restabelecer o acesso aos dados.**

> **Como funciona a deduplicação?**
> 
> Quando ela é ativada, ao executar um “job”, a ferramenta analisa os arquivos que estão em processo de backup através de identificadores únicos e, se determinado arquivo for encontrado no disco, é criado apenas um ponteiro para este arquivo, eliminando duplicatas e economizando espaço.
![[Pasted image 20260824090933.png]]


# - Bloco B: PMBOK; COBIT 2019

Os seguintes atores são comumente mencionados em frameworks de governança de TI e segurança da informação, como o COBIT ou a ISO/IEC 27001:

|**Ator**|**Papel**|
|---|---|
|**Gestor da Informação**|Responsável por definir e gerenciar as autorizações de acesso lógico, garantindo que as permissões estejam alinhadas com as políticas de segurança da informação.|
|**Gestor de Processo**|Supervisiona a execução de processos específicos, mas não gerencia diretamente as autorizações de acesso.|
|**Usuário**|Utiliza os sistemas e recursos de informação com base nas permissões concedidas. Não gerencia autorizações.|
|**Gestor do Usuário**|Supervisiona as atividades dos usuários e pode solicitar alterações de permissões, mas não decide sobre as autorizações de acesso.|
|**Custodiante do Recurso**|Responsável pela proteção física e integridade dos recursos de informação (ex.: servidores, bancos de dados). Não gerencia acesso lógico.|
|**Administrador de Sistemas**|Configura e mantém os sistemas, incluindo a implementação das autorizações de acesso definidas pelo gestor da informação.|
|**Auditor de Segurança**|Verifica se as autorizações de acesso estão em conformidade com as políticas de segurança e regulamentações.|
|**Proprietário do Ativo**|Define a classificação e a criticidade dos ativos de informação, influenciando as políticas de acesso.|
|**Comitê de Segurança**|Define as políticas e diretrizes gerais de segurança da informação, incluindo o gerenciamento de acesso.|
|**Analista de Segurança**|Implementa controles de segurança e monitora o acesso aos sistemas para detectar violações ou irregularidades.|
|**Dono do Processo**|Responsável por garantir que os processos sob sua responsabilidade estejam alinhados com as políticas de segurança, incluindo o acesso lógico.|




# - Bloco C: ITIL; Governança em TI (PETI, SWOT, BSC)
# - Bloco D: Engenharia de Software - Modelos; Metodologias Ágeis
# - Bloco E: Scrum, XP, Kanban



---



> [!info]- Como preencher
> Cada `- [ ]` é um tópico. Ajuste `[dom:: N]` de 0 a 5 ao estudar; acrescente `[rev:: AAAA-MM-DD]` para
> o painel te cobrar. Escreva o conteúdo logo abaixo do cabeçalho do tópico, no formato que quiser.






---



