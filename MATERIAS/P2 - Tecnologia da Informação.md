---
disciplina: Tecnologia da Informação
bloco: Fluência de Dados
revisado:
prova: II
peso: 3
pontos: 30
origem: BA 2019
prioridade: importante
---

# Tecnologia da Informação

> **10 questões · peso 3 · **30 pontos** · 9,1% da nota**
> Prioridade: **importante**

Trinta pontos que a maioria trata como periférico — valia o mesmo que Matemática e RL e mais que Auditoria e Estatística Aplicada somadas.

**Atenção:** nos editais FCC recentes, este bloco foi substituído por Fluência de Dados, bem mais exigente. Se a Bahia seguir o modelo, migre o esforço para lá.

## Percentual de cobrança (VINTEUM Fiscal 4.0)

*Fonte: Guia de Estudo Regular Fiscal 4.0 (VINTEUM) — bancas FCC, FGV e CEBRASPE. Disciplina "Tecnologia da Informação" no guia atual.*

> [!warning]- O checklist abaixo não é essa disciplina
> Os tópicos marcados com `- [ ]` mais abaixo (Hardware, Pacote de escritório, Internet, NF-e/SPED...) são o conteúdo antigo de "Noções de Informática" (âncora BA 2019). A tabela abaixo é o currículo atual de "Tecnologia da Informação" na VINTEUM 4.0 (governança de TI, metodologias, ITIL, PMBOK, COBIT, segurança) — praticamente não se sobrepõe ao checklist antigo. Os dois convivem nesta nota só porque você pediu para renomear a disciplina; avaliar se vale separar o checklist de tópicos fica pra depois.

| Tópico | % |
| --- | --- |
| Metodologias de Desenvolvimento Ágeis | 13,9% |
| Gestão de Projetos (PMBOK) | 13,7% |
| ITIL | 10,2% |
| Gerenciamento de Processos de Negócio (BPM/BPMN) | 9,4% |
| COBIT | 9,0% |
| Criptografia (Segurança da Informação) | 8,8% |
| Gestão da Segurança da Informação | 7,8% |
| Gestão por Processos (PETI, SWOT, PDCA e BSC) | 7,6% |
| Planejamento Estratégico de TI | 3,9% |
| Conceitos de Governança de TI | 3,5% |

## Checklist por importância (VINTEUM)

- [ ] Metodologias de Desenvolvimento Ágeis [dom:: 0] [peso:: 13.9]
- [ ] Gestão de Projetos (PMBOK) [dom:: 0] [peso:: 13.7]
- [ ] ITIL [dom:: 2] [peso:: 10.2]
- [ ] Gerenciamento de Processos de Negócio (BPM/BPMN) [dom:: 3] [peso:: 9.4]
- [ ] COBIT [dom:: 3] [peso:: 9.0]
- [ ] Criptografia (Segurança da Informação) [dom:: 0] [peso:: 8.8]
- [ ] Gestão da Segurança da Informação [dom:: 4] [peso:: 7.8]
- [ ] Gestão por Processos (PETI, SWOT, PDCA e BSC) [dom:: 0] [peso:: 7.6]
- [ ] Planejamento Estratégico de TI [dom:: 4] [peso:: 3.9]
- [ ] Conceitos de Governança de TI [dom:: 4] [peso:: 3.5]

---

> [!info]- Como preencher
> Cada `- [ ]` é um tópico. Ajuste `[dom:: N]` de 0 a 5 ao estudar; acrescente `[rev:: AAAA-MM-DD]` para
> o painel te cobrar. Escreva o conteúdo logo abaixo do cabeçalho do tópico, no formato que quiser.

### Hardware, software e sistemas operacionais
- [ ] status [dom:: 0] [peso:: 3]

### Pacote de escritório; planilhas e fórmulas
- [ ] status [dom:: 0] [peso:: 3]

### Internet, navegadores e correio eletrônico
- [ ] status [dom:: 0] [peso:: 3]

### Segurança da informação; malwares; backup
- [x] status [dom:: 2] [peso:: 3] [prova:: 1] ✅ 2026-09-18

#### 1. Resumo Teórico 
- [x] status [dom:: 2] [peso:: 3] ✅ 2026-09-18

A Segurança da Informação (SI) é um conjunto de práticas, políticas, procedimentos e controles que visam proteger os ativos de informação de uma organização contra diversas ameaças. O objetivo é garantir a continuidade dos negócios, minimizar os riscos e maximizar o retorno sobre os investimentos e as oportunidades.

##### Conceitos Fundamentais
- [x] status [dom:: 2] [peso:: 3] ✅ 2026-09-18

- Ativo de Informação: Qualquer informação ou recurso que tenha valor para a organização (dados, hardware, software, pessoas, imagem da empresa, etc.).
- Ameaça: Qualquer evento ou ação potencial que possa causar dano aos ativos de informação (ex: malware, desastres naturais, erro humano, ataque intencional).
- Vulnerabilidade: Uma fraqueza em um ativo ou controle que pode ser explorada por uma ou mais ameaças.
- Risco: A probabilidade de uma ameaça explorar uma vulnerabilidade e o impacto resultante para a organização.
- Impacto: O prejuízo ou consequência resultante da materialização de um risco.

##### Princípios Básicos (Pilares da Segurança da Informação)
- [x] status [dom:: 2] [peso:: 3] [prova:: 1] ✅ 2026-09-18

Os pilares fundamentais da Segurança da Informação são frequentemente lembrados pelo mnemônico CID (ou CIDA, incluindo Autenticidade):

- **Confidencialidade:** Garante que a informação seja <mark class="prova" style="background:rgba(0,170,170,0.28)">acessível somente por pessoas, entidades ou processos autorizados</mark>. É a proteção contra o acesso não autorizado. Pense em "segredo".
    - _Exemplo:_ Criptografar um e-mail para que apenas o destinatário possa lê-lo.
- **Integridade:** Garante a exatidão, completeza e a não modificação não autorizada da informação e dos métodos de processamento. A informação deve ser mantida em seu estado original e confiável. Pense em "originalidade" ou "exatidão".
    - _Exemplo:_ Usar uma função hash para verificar se um arquivo foi alterado durante o download.
- **Disponibilidade:** Garante que os <mark class="prova" style="background:rgba(0,170,170,0.28)">usuários autorizados tenham acesso à informação e aos ativos associados sempre que necessário</mark>. A informação deve estar acessível quando solicitada. Pense em "acesso garantido".
    - _Exemplo:_ Ter servidores redundantes para que um sistema continue funcionando mesmo se um servidor falhar.

> [!example]- Prova anterior: IBAM 2026 · Guarulhos · Q26 (gab. B · preliminar)
> **Trecho usado:** "acessível somente por pessoas, entidades ou processos autorizados … usuários autorizados tenham acesso à informação e aos ativos associados sempre que necessário"
> **Como cobrou:** troca de termo — sequência de quatro itens V/F (gab. B: V, V, F, F). O item 1 (V) é a confidencialidade: "restringir o acesso à informação às pessoas devidamente autorizadas a conhecê-la". O item 3 (F) põe na integridade a definição da disponibilidade: "A integridade tem por objetivo garantir que a informação esteja disponível aos usuários no exato momento em que for requisitada". O item 2 (rastreabilidade) cai em Outros Atributos Essenciais; o item 4 (controle de acesso × criptografia) a nota não trata.
> **Lastro:** PDF p. 11 · [[IBAM 2026 - Guarulhos - Auditor Fiscal VI Manhã#Q26]]

##### Outros Atributos Essenciais
- [x] status [dom:: 2] [peso:: 3] [prova:: 1] ✅ 2026-09-18

- Autenticidade: Garante que a identidade de um usuário, processo, sistema ou informação seja aquela que se alega ser. É a prova da origem ou da identidade.
    - _Exemplo:_ Um login e senha para acessar um sistema.
- Não Repúdio (Irretratabilidade): Garante que uma entidade não possa negar a autoria de uma ação ou transação que realizou. Oferece prova da origem e da entrega.
    - _Exemplo:_ Uma assinatura digital em um contrato eletrônico impede que o signatário negue ter assinado.
- Conformidade (Legalidade): Garante que as ações e os controles de segurança estejam de acordo com as leis, regulamentos, normas e obrigações contratuais.
- Responsabilização (Accountability): <mark class="prova" style="background:rgba(0,170,170,0.28)">Garante que as ações de uma entidade possam ser rastreadas unicamente até essa entidade. Permite auditoria e identificação de responsáveis.</mark>

> [!example]- Prova anterior: IBAM 2026 · Guarulhos · Q26 (gab. B · preliminar)
> **Trecho usado:** "Responsabilização (Accountability): Garante que as ações de uma entidade possam ser rastreadas unicamente até essa entidade. Permite auditoria e identificação de responsáveis."
> **Como cobrou:** troca de termo — o item 2 (V) chama de rastreabilidade o que a nota chama de Responsabilização: "A rastreabilidade permite reconstituir a sequência de eventos e identificar os responsáveis pelas ações realizadas sobre a informação". Gab. B: V, V, F, F. A nota traz o nome Responsabilização, mas não o termo "rastreabilidade".
> **Lastro:** PDF p. 11 · [[IBAM 2026 - Guarulhos - Auditor Fiscal VI Manhã#Q26]]

#### 2. Principais Temas Cobrados em Concursos
- [x] status [dom:: 2] [peso:: 3] ✅ 2026-09-18

Com base na análise de questões de diversas bancas, os seguintes tópicos são frequentemente abordados:

- A Tríade CID (Confidencialidade, Integridade, Disponibilidade): Definição, aplicação em cenários e diferenciação entre eles. É o tema mais central.
- **Identificação de Violações:** Questões que apresentam um incidente (ex: vazamento de dados, alteração de informações, sistema indisponível) e pedem para identificar qual(is) princípio(s) foi(ram) violado(s).
- **Autenticidade e Não Repúdio:** Conceitos, diferenças e mecanismos associados (ex: senhas, tokens, biometria para autenticidade; assinatura digital para não repúdio).
- **Mecanismos de Segurança e seus Princípios:**
    - Criptografia: Associada principalmente à Confidencialidade.
    - Funções Hash (Resumo): Associadas principalmente à Integridade.
    - Assinatura Digital: Garante Autenticidade, Integridade e Não Repúdio.
    - Certificados Digitais: Usados para Autenticidade.
    - Firewalls e IDS/IPS: Contribuem para Confidencialidade (controle de acesso) e Disponibilidade (proteção contra ataques).
    - Backups e Planos de Continuidade: Essenciais para a Disponibilidade e recuperação da Integridade.
- **Autenticação Multifator (MFA):** Conceito e importância como camada adicional de segurança para a Autenticidade.
- **Outros Atributos:** Embora menos frequentes que a tríade CID, conceitos como Legalidade/Conformidade e Responsabilização podem aparecer.

**Dica de Ouro: Dominando a Tríade!**

A maioria das questões gira em torno da Tríade CID. Entender profundamente cada pilar e como eles se manifestam em situações práticas é crucial. Por exemplo, se um CPF é alterado indevidamente em um cadastro, houve falha na Integridade. Se dados sigilosos de um processo são acessados por alguém não autorizado, a Confidencialidade foi comprometida. Se um sistema fica fora do ar devido a um ataque, a Disponibilidade foi afetada.

#### 3. Pontos de Atenção e Dificuldades Comuns
- [x] status [dom::2] [peso:: 3] ✅ 2026-09-18

Candidatos frequentemente encontram dificuldades em:

- **Diferenciar sutilmente os pilares da Tríade CID em cenários complexos.**
    - _Exemplo:_ Um dado pode estar disponível, mas corrompido (falha na Integridade, não necessariamente na Disponibilidade de acesso ao dado corrompido).
- **Confundir Autenticidade com Não Repúdio.**
    - Autenticidade prova quem você é. Não Repúdio prova que você fez algo e não pode negar.
- **Associar corretamente mecanismos de segurança aos princípios que eles garantem.**
    - _Exemplo:_ Criptografia assimétrica (chaves pública/privada) é fundamental para assinaturas digitais, que por sua vez garantem Autenticidade, Integridade e Não Repúdio.
- **Interpretar termos sinônimos:** Irretratabilidade é o mesmo que Não Repúdio.

**Dica de Ouro: Mnemônico CIDA + NR!**

Para memorizar os principais atributos, pense em CIDA + NR:

- **C**onfidencialidade: Só acessa quem pode (segredo).
- **I**ntegridade: Informação correta e completa (exatidão).
- **D**isponibilidade: Acesso garantido quando necessário (sempre ligado).
- **A**utenticidade: É quem diz ser (identidade verdadeira).
- **NR**(Não Repúdio): Não pode negar que fez (prova da ação).

**Dica de Ouro: Integridade vs. Confidencialidade na Prática!**

Imagine um arquivo confidencial. Se alguém não autorizado o acessa, a Confidencialidade é quebrada. Se alguém altera o conteúdo desse arquivo (autorizado ou não, mas sem que a alteração seja legítima/esperada), a Integridade é afetada. Se o arquivo é deletado e não há backup, a Disponibilidade é comprometida.

**Dica de Ouro: O que NÃO é um atributo básico?**

Algumas questões tentam confundir com termos que parecem relacionados, mas não são atributos fundamentais da SI. Por exemplo, "Presteza" ou "Flexibilidade" não são usualmente reconhecidos como atributos básicos da SI no mesmo nível de CIDANR.

**VULNERABILIDADE, AMEAÇA E RISCO**
- Vulnerabilidade: é uma falha ou fraqueza que pode ser explorada por uma ameaça.
- Ameaça: é um <font color="#e36c09">evento</font> ou <font color="#e36c09">ação</font> que pode causar danos, explorando uma vulnerabilidade.
- Risco: é a <font color="#0070c0">probabilidade</font> de uma ameaça se concretizar e causas danos.

##### Controles de Segurança: Físicos × Lógicos
- [x] status [dom:: 2] [peso:: 3] [prova:: 1] ✅ 2026-09-27

| Tipo | Exemplos |
| --- | --- |
| **Físicos** | Portas, trancas, paredes, vigilantes, alarmes, catracas, cercas etc. |
| **Lógicos** | Senhas, autenticação, antivírus, firewall, criptografia, biometria, IDS/IPS etc. |

> [!example]- Prova anterior: IBAM 2026 · Guarulhos · Q31 (gab. B · preliminar) e IBAM 2025 · Mauá · Q17 (gab. C · preliminar)
> **Trecho usado:** "Lógicos | Senhas, autenticação, antivírus, firewall, criptografia, biometria, IDS/IPS etc."
> **Q31 (Guarulhos, 2026) — como cobrou:** conceito — questão de asserção com PORQUE; a II diz que "O firewall atua no controle do tráfego de rede, filtrando os pacotes de dados conforme regras de segurança previamente definidas" (V) e não justifica a I, sobre criptografia simétrica. Gab. B. A nota só lista o firewall entre os controles lógicos; a função de filtrar tráfego por regras não está nela.
> **Q17 (Mauá, 2025) — como cobrou:** conceito — seis itens V/F (gab. C: V, V, V, F, V, V). Dois se ligam ao que a nota tem: "Firewalls atuam no controle do tráfego de dados entre redes…" (V) e "A simples instalação de um antivírus atualizado elimina a necessidade de outras medidas de segurança" (F). Vírus com arquivo hospedeiro, malware como categoria e phishing como engenharia social não têm regra na nota.
> **Lastro:** Q31: PDF p. 12 · [[IBAM 2026 - Guarulhos - Auditor Fiscal VI Manhã#Q31]] · Q17: PDF p. 3 · [[IBAM 2025 - Mauá - AFTM#Q17]]

⚠️ **Atenção!** A classificação depende do **recurso protegido** e da **forma de uso** — não é uma etiqueta fixa por tecnologia. Biometria para entrar numa sala atua como controle **físico**; a mesma biometria para acessar um sistema atua como controle **lógico**.

*(Guruja, aba Bizu — Segurança da Informação)*

##### Autenticação: os 3 Fatores e MFA
- [x] status [dom:: 2] [peso:: 3] [prova:: 1] ✅ 2026-09-27

| Fator | Exemplos |
| --- | --- |
| **O que você sabe** | Senha, PIN, perguntas de segurança, código. |
| **O que você tem** | Token, smartcard, celular, certificado, aplicativo autenticador. |
| **O que você é** | Biometria: digital, face, íris, voz etc. |

Boas práticas de senha: comprimento e complexidade, <mark class="prova" style="background:rgba(0,170,170,0.28)">não reutilizar, evitar dados pessoais, usar gerenciador de senhas e MFA</mark>. **TOTP** é baseado em **tempo**; **HOTP**, em **contador**.

> [!example]- Prova anterior: IBAM 2026 · Bragança Paulista · Q17 (gab. C · oficial)
> **Trecho usado:** "não reutilizar, evitar dados pessoais, usar gerenciador de senhas e MFA"
> **Como cobrou:** conceito — sequência de nove itens V/F (gab. C: V, V, F, V, F, V, V, V, F). Dois cobrem o que a nota tem: "A utilização de senhas distintas para diferentes serviços reduz o impacto caso uma delas venha a ser comprometida" (V) e "O uso de autenticação em dois fatores pode acrescentar uma camada de proteção… além da senha" (V). Extensão .pdf, nuvem, phishing e sessão em computador compartilhado não estão na nota.
> **Lastro:** Caderno tipo 3, p. 9 · [[IBAM 2026 - Bragança Paulista - AFTM Jr#Q17]]

**Autenticação forte (MFA):** usa **dois ou mais fatores distintos** — não basta somar credenciais do mesmo fator.

> [!example]- 🧩 Pegadinha clássica de prova
> SENHA + PIN = **mesmo fator** ❌ (os dois são "o que você sabe")
> SENHA + TOKEN = **fatores distintos** ✅
> CARTÃO + BIOMETRIA = **fatores distintos** ✅

*(Guruja, aba Bizu — Segurança da Informação)*


#### 4. Estratégias de Resolução de Questões
- [x] status [dom:: 2] [peso:: 3] ✅ 2026-09-18

- **Identifique Palavras-Chave:**
    - "Acesso não autorizado", "vazamento", "sigilo", "privacidade": Confidencialidade.
    - "Alteração", "modificação", "corrupção", "exatidão", "consistência": Integridade.
    - "Indisponível", "fora do ar", "acesso negado (quando deveria ser permitido)", "continuidade": Disponibilidade.
    - "Identidade", "verificar quem é", "origem": Autenticidade.
    - "Não poder negar", "prova de autoria", "assinatura": Não Repúdio.
- **Analise o Cenário Completo:** Em questões situacionais, leia atentamente a descrição do incidente. Pergunte-se: "Qual foi o principal problema ou falha de segurança ocorrido?"
    - Se a informação foi lida por quem não devia: Confidencialidade.
    - Se a informação foi alterada indevidamente: Integridade.
    - Se a informação/sistema não pôde ser acessado: Disponibilidade.
- **Processo de Eliminação:** Em questões de múltipla escolha, descarte as alternativas que claramente não se aplicam.
- **Cuidado com Generalizações:** Uma medida de segurança pode contribuir para múltiplos princípios, mas as questões geralmente focam no principal objetivo do mecanismo. Por exemplo, um backup (Disponibilidade) também ajuda a restaurar a Integridade após um incidente.
- **Lembre-se das Ferramentas:**
    - Criptografia é a rainha da Confidencialidade.
    - Hash é o guardião da Integridade.
    - <u>Assinatura Digital</u> é o trio <mark style="background:rgba(5, 117, 197, 0.2)">Autenticidade + Integridade + Não Repúdio</mark>.

- #pegadinha 

**Dica de Ouro: Questões de "Certo ou Errado" (CESPE/Cebraspe)**
Nesse tipo de questão, cada detalhe importa. Se uma afirmativa diz que "A disponibilidade garante o acesso por terceiros interessados, independentemente de autorização", está ERRADO, pois disponibilidade é para usuários AUTORIZADOS. A falta da palavra "autorizado" ou a inclusão de "independentemente de autorização" muda tudo.

**Dica de Ouro: Múltiplas Violações**
Um único incidente pode violar múltiplos princípios. Por exemplo, um invasor acessa dados confidenciais (Confidencialidade), altera esses dados (Integridade) e depois apaga os logs para esconder seus rastros (afetando a Responsabilização e dificultando a análise da Autenticidade das ações).



#### BACKUP
- [ ] status [dom:: 2] [peso:: 3]

A questão cobra o **tema backups.** Existem três tipos de backup, a saber: **completo, diferencial e incremental.** No backup completo, todos os dados são salvos, independente de quaisquer condições. No backup incremental, adiciona-se um pequeno incremento ao backup completo ou ao backup incremental anterior. Por fim  , **no backup diferencial, não são marcadas as "flags"**  de registro dos dados. Dessa maneira, ele não consegue reconhecer outros backups diferenciais e por esse motivo pega todos os dados após o último backup completo, mesmo que tenha sido executado um backup diferencial anterior.

**Ransomware** é um tipo de software malicioso (malware) que "sequestra" o computador ou os dados da vítima. Ele bloqueia o acesso ao sistema ou criptografa os arquivos importantes e, em seguida, exige o pagamento de um resgate (em inglês, _ransom_) para que o acesso seja restabelecido.
> Como devo me proteger de **_ransomware_**?

   Para se proteger de _ransomware_ você deve tomar os mesmos cuidados que toma para evitar os outros códigos maliciosos, como:
- manter o sistema operacional e os programas instalados com todas as atualizações aplicadas;
- ter um antivírus instalado;
- ser cuidadoso ao clicar em _links_ ou abrir arquivos.
Fazer _backups_ regularmente também é essencial para proteger os seus dados pois, **se seu equipamento for infectado, a única garantia de que você conseguirá acessá-los novamente é possuir _backups_ atualizados**. **O pagamento do resgate não garante que você conseguirá restabelecer o acesso aos dados.**

> **Como funciona a deduplicação?**
> 
> Quando ela é ativada, ao executar um “job”, a ferramenta analisa os arquivos que estão em processo de backup através de identificadores únicos e, se determinado arquivo for encontrado no disco, é criado apenas um ponteiro para este arquivo, eliminando duplicatas e economizando espaço.
![[Pasted image 20260824090933.png]]


### Certificação digital e assinatura eletrônica
- [x] status [dom:: 2] [peso:: 3] [prova:: 1] ✅ 2026-09-27

**Criptografia Simétrica, Assimétrica e Híbrida**

| Tipo | Características |
| --- | --- |
| **Simétrica** | Mesma chave para cifrar/decifrar; rápida; problema de distribuição da chave. Exemplos: DES, 3DES, AES, IDEA, RC4 e Blowfish. |
| **Assimétrica** | Par chave pública + privada; facilita troca segura e assinatura. Exemplos: RSA, DSA, ECDSA e ElGamal. |
| **Híbrida** | Assimétrica protege a troca da chave de sessão; simétrica protege os dados (é o modelo usado na prática — TLS/HTTPS, por exemplo). |

> [!example]- Prova anterior: IBAM 2026 · Guarulhos · Q31 (gab. B · preliminar)
> **Trecho usado:** "Simétrica | Mesma chave para cifrar/decifrar; rápida; problema de distribuição da chave"
> **Como cobrou:** conceito — questão de asserção com PORQUE. A I diz que "A criptografia simétrica utiliza uma única chave secreta, compartilhada entre as partes, para cifrar e decifrar as mensagens trocadas" (V); a II, sobre o firewall (V), não a justifica. Gab. B: "As asserções I e II são verdadeiras, mas a II não é uma justificativa correta da I." A nota cobre só o lado da I; a função do firewall não está aqui.
> **Lastro:** PDF p. 12 · [[IBAM 2026 - Guarulhos - Auditor Fiscal VI Manhã#Q31]]

> [!info] Princípio de Kerckhoff
> A segurança deve depender do **sigilo da chave**, não do segredo do algoritmo — o algoritmo pode (e deve) ser público e auditável.

**Funções Hash**

Hash transforma entrada de tamanho variável em resumo de tamanho fixo; deve ser **unidirecional** e **resistente a colisões**.

| Algoritmo | Característica |
| --- | --- |
| **MD5** | 128 bits; inseguro para aplicações que exigem segurança. |
| **SHA-1** | 160 bits; obsoleto/inseguro devido a colisões. |
| **SHA-256** | (família SHA-2) 256 bits; seguro no contexto atual. |

⚠️ **Hash não criptografa.** Produz um resumo; não se "descriptografa" o hash para recuperar a entrada original.

**Assinatura Digital**

Garante **integridade**, **autenticidade** e **irretratabilidade/não repúdio** — <mark style="background:#fff88f">nunca confidencialidade</mark> (isso é papel da criptografia, não da assinatura). Utiliza função hash + criptografia assimétrica: o emissor assina com sua **chave privada**; a verificação usa sua **chave pública**.

**Certificado Digital e ICP-Brasil**

Documento eletrônico que associa uma **identidade a uma chave pública**, emitido por uma Autoridade Certificadora (AC).

⚠️ A **chave privada não fica dentro do certificado** — permanece protegida com o titular; o certificado contém apenas a **chave pública**.

Hierarquia da ICP-Brasil: <mark class="prova" style="background:rgba(0,170,170,0.28)">**AC-Raiz** (topo da cadeia; define políticas, audita/fiscaliza as subordinadas) → **AC** (emite, distribui, renova, revoga e gerencia certificados) → **AR** (identifica o solicitante, registra e encaminha o pedido à AC)</mark> → **Titular**.

> [!example]- Prova anterior: IBAM 2026 · Guarulhos · Q38 (gab. D · preliminar)
> **Trecho usado:** "AC-Raiz (topo da cadeia; define políticas, audita/fiscaliza as subordinadas) → AC (emite … certificados) → AR (identifica o solicitante, registra e encaminha o pedido à AC)"
> **Como cobrou:** troca de termo — o item II diz que "a autoridade de registro ocupa o topo da hierarquia e responde pelo credenciamento das demais autoridades certificadoras do país" (F); na nota o topo é a AC-Raiz e a AR só identifica, registra e encaminha o pedido à AC. Gab. D: I e III verdadeiras (certificado liga a chave pública à identidade do titular; assinatura assimétrica dá autoria e integridade).
> **Lastro:** PDF p. 14 · [[IBAM 2026 - Guarulhos - Auditor Fiscal VI Manhã#Q38]]

> [!tip]- Lupa de prova: AC-Raiz × AR na ICP-Brasil
> **O padrão:** a afirmativa troca o papel de dois elos da cadeia, dando à AR o topo da hierarquia. Padrão de 1 prova, não confirmado (só a Guarulhos Manhã cobrou este heading).
> **A armadilha:** o item II — "a autoridade de registro ocupa o topo da hierarquia e responde pelo credenciamento das demais autoridades certificadoras do país" — vem entre dois itens verdadeiros (I e III); quem não confere a hierarquia cai em "(B) I, II e III." ou em "(E) I e II, apenas."
> **Como resolver:** pela nota, o topo é a AC-Raiz; a AC emite e gerencia certificados; a AR só identifica o solicitante, registra e encaminha o pedido à AC. Item que põe a AR no topo é falso (Mapa de Fixação: AC → emite | AR → identifica e encaminha).

Certificados seguem o padrão **X.509** (versão, número de série, algoritmo, emissor, validade, titular, chave pública, assinatura da AC), validados por uma **cadeia de certificação** até uma raiz confiável (existe também o **Web of Trust**, modelo alternativo descentralizado, sem AC central).

**Tipos de certificado:** **A** (Assinatura digital — autenticidade/integridade de documentos) × **S** (Sigilo — criptografia de documentos/dados). Cada tipo tem categorias A1/S1 a A4/S4, conforme geração das chaves, armazenamento e validade.

> [!warning] ⚠️ Pegadinha clássica de prova (IBAM, Pref. Santos 2020)
> **Assinatura eletrônica** é a expressão mais ampla — inclui clique, assinatura manuscrita em tela, geolocalização, biometria etc. **Nem toda assinatura eletrônica é uma assinatura digital**: a assinatura digital é a modalidade específica baseada em criptografia assimétrica **e certificado digital**.

> [!example]- 🧩 Mapa de Fixação (Super Bizu Final da Guruja)
> CID → Confidencialidade + Integridade + Disponibilidade
> Simétrica → mesma chave | Assimétrica → par de chaves
> Hash → resumo, não criptografia
> Assinatura → Integridade + Autenticidade + Não Repúdio
> MFA → fatores distintos
> Certificado → identidade + chave pública
> AC → emite | AR → identifica e encaminha

*(Guruja, aba Bizu — Segurança da Informação, bloco C)*

### Banco de dados e noções de SQL
- [ ] status [dom:: 2.5] [peso:: 3]

### NF-e, CT-e, MDF-e, SPED e EFD
- [ ] status [dom:: 2] [peso:: 3]



### Gerenciamento de Processos de Negócio (BPM/BPMN)
- [ ] status [dom:: 3] [peso:: 3]


#### - Business Process Management — BPM

##### 1. Gerenciamento de Processos de Negócio (BPM)
- [x] status [dom:: 3] [peso:: 3] ✅ 2026-09-18

> _“Gerenciamento de processo de negócio (BPM- Business Process Management) representa uma nova forma de visualizar as operações de negocio que vai além das estruturas funcionais tradicionais.”_ (PBM CBOK, 2013, p.33)

Segundo o Wikipédia, BPM é um conceito que une **gestão de negócios** e **tecnologia da informação** com foco na **otimização dos resultados** das organizações **por meio da melhoria dos** **processos de negócio**.

A banca CESPE/CEBRASPE já definiu o BPM da seguinte maneira:

> O **BPM** trata de como os processos são executados para que melhorias possam ser realizadas e os processos possam ser gerenciados, o que possibilita uma melhor tomada de decisões e uma visão do negócio como um todo

**1.1 Propósito do CBOK:**

O propósito primário do guia é **identificar** e **fornecer** uma visão geral de áreas do conhecimento reconhecidas e aceitas como boas práticas no gerenciamento de processos.

É organizado em **9 áreas de conhecimento**
![[Captura de Tela 2026-08-19 às 12.16.15.png|360]]

**1.2 Processo**

> Processo é uma agregação de atividades e comportamentos executados por humanos ou máquinas para alcançar um ou mais resultados.

**1.3 Processo de Negócio**

O Guia BPM CBOK define **“processo de negócio”** como um trabalho que **entrega valor** para os **clientes** ou **apoia/gerencia** **outros processos**. Sendo assim, podemos classificar os processos de negócios em três tipos: primário, de suporte e de gerenciamento.

**1.3.1 Processo Primário**

É um processo tipicamente **interfuncional** ponta a ponta (e até interorganizacional ponta a ponta) que **agrega valor diretamente para o cliente**.

 **1.3.2 Processo de suporte**

Existe para prover **suporte a processos primários,** mas também pode prover suporte a outros processos de suporte (processos de suporte de segundo nível, terceiro nível e sucessivos) ou processos de gerenciamento. A diferença principal entre os processos primários e os de suporte é que processos de suporte entregam valor para outros processos e não diretamente para os clientes.

**1.3.3 Processo de gerenciamento**

Tem o propósito de para **medir, monitorar, controlar** atividades e administrar o presente e o futuro do negócio. Processos de gerenciamento, assim como os processos de suporte, não agregam valor diretamente para os clientes, mas são necessários para assegurar que a organização opere de acordo com seus objetivos e metas de desempenho.

![[Captura de Tela 2026-08-19 às 12.17.49.png|950]]

##### 2. Modelagem de processos de negócio
- [x] status [dom:: 3] [peso:: 3] ✅ 2026-09-18

Modelagem de processos de negócio é o conjunto de atividades envolvidas na **criação de representações de processos de negócio** existentes ou propostos.

O propósito da modelagem é **criar uma representação do processo** de maneira completa e precisa sobre seu funcionamento.

**2.1 Diagrama, mapa ou modelo de processos**

- **DIAGRAMA:** Retrata os principais elementos de um fluxo de processo;
- **MAPA:** Fornece uma **visão abrangente** dos principais componentes de um processo;
- **MODELO**: Implica a representação de um determinado estado do negócio (atual/futuro) e dos respectivos recursos envolvidos;

![[Captura de Tela 2026-08-19 às 12.18.38.png|780]]

**2.2 Notações de modelagem de processos** 

Das notações de modelagem de processos, a mais cobrada em prova é a BPMN, que será estudada em mais detalhes em outro momento.

O BPM**N** é a **N**otação da modelagem de processo.

**Referência Biliográfica:**

BPM CBOK: Guia para o Gerenciamento de Processos de Negócio. Corpo Comum do Conhecimento – ABPMP BPM CBOK, Association of Business Process Management Professionals.

##### 3. Análise de Processos
- [x] status [dom:: 3] [peso:: 3] ✅ 2026-09-18

O primeiro passo para **definir um novo processo** ou **atualizar** um que já exista é criar um entendimento comum do estado atual ("**AS-IS**") do processo e como ele cumpre seus objetivos. 

A análise de processos é essencial para avaliar **como** os processos de negócio **estão operando**.

**Quando efetuar a análise?** 

pode ser realizada:

- em resposta a desvios em desempenho de processos ou
- acionada por eventos externos ou temporais (análise programada).

**Análise SWOT**

SWOT = **_S_**_trenghts, Weakness,_ **_O_**_pportunities,_ **_T_**_hreats_

ou FOFA ( **F**orças, **O**portunidades, **F**raquezas e **A**meaças)

![[Captura de Tela 2026-08-19 às 12.19.36.png|767]]


Responsabilidades de alguns papéis


#### - Business Process Model and Notation — BPMN

##### 1. Business Process Model and Notation (BPMN)
- [x] status [dom:: 2] [peso:: 3] ✅ 2026-09-18

> Notação padrão para o desenho de fluxogramas em Processos de Negócios que refere-se um conjunto de regras e convenções, determinando como os fluxogramas devem ser desenhados (WHITE, 2006)

- O BPMN é um conjunto de convenções gráficas para descrever processos de negócios, **especificamente projetada** para coordenar a **sequência de processos** e a **troca de mensagens** existente **entre processos**.

De acordo com Chinosi e Trombetta (2012), o BPMN pode modelar três tipos diferentes de Processos de Negócios usando três sub-modelos:

1. **Processos de negócio privados (internos):**
2. focalizam geralmente o ponto de vista de uma única organização do negócio e definem as atividades internas da organização.
3. O fluxo da sequência do processo está contido dentro de um único pool e não pode cruzar os seus limites.
4. **Processos de negócio abstratos (públicos):** 
5. representam as interações entre um processo empresarial privado e outro processo ou participante externo.
6. Somente as atividades que são usadas para comunicação para fora do processo de negócio privado e os mecanismos de controle de fluxo apropriados são incluídos no processo abstrato.
7. **Processos de negócio colaborativos de B2B (Business-to-Business):**
8. descrevem as interações entre duas ou mais entidades de negócio.
9. Os diagramas de processos são geralmente de um ponto de vista global. As interações são descritas como as sequências de atividades e as trocas de mensagens entre os participantes.

**1.1 Diagrama de Orquestração**

- **Propósito Principal:** Representar um processo de negócio padrão.
![[Captura de Tela 2026-08-19 às 12.24.24.png|815]]

**1.2 Diagrama de Coreografia**

- Focaliza a forma como os participantes trocam mensagens, demonstrando a comunicação entre os eles;
- É a representação dos processos e suas interações;
- Demonstra o comportamento esperado entre os participantes;
- É o contrato de negócio de interação entre os participantes.

![[Captura de Tela 2026-08-19 às 12.25.00.png|766]]

![[Captura de Tela 2026-08-19 às 12.25.22.png|687]]

![[Captura de Tela 2026-08-19 às 12.25.47.png|705]]
![[Captura de Tela 2026-08-19 às 12.26.10.png|715]]

**Na imagem acima, o primeiro gateway da esquerda para direita é o "Garfo" ou "Fork" e o segundo (mais a direita) é o Join, ou seja, a convergência do fluxo, aonde temos as duas entradas que devem ser concluídas para que a única saída aconteça.**

![[Pasted image 20260821153917.png]]


###### Materiais Complementares de Consulta
- [ ] status [dom:: 1] [peso:: 3]

- [**Guia Simplificado de Boas Práticas em Modelagem de Processos com BPMN**](https://www.ufmg.br/dti/wp-content/uploads/2019/01/POP-0001-ANEXO-A-Guia-simplificado-de-boas-praticas-em-modelagem.pdf) do departamento de TI da UFMG
- **blog da iprocess** (Algumas postagens desse blog já foram cobradas em provas da área fiscal):

- [Um guia para iniciar estudos em BPMN (I)](https://blog.iprocess.com.br/2012/11/um-guia-para-iniciar-estudos-em-bpmn-i-atividades-e-sequencia/)
- [Um guia para iniciar estudos em BPMN (II): Gateways](https://blog.iprocess.com.br/2012/11/um-guia-para-iniciar-estudos-em-bpmn-ii-gateways/)
- [Um guia para iniciar estudos em BPMN (III): Eventos de Início e Fim](https://blog.iprocess.com.br/2012/12/um-guia-para-iniciar-estudos-em-bpmn-iii-eventos-de-inicio-e-fim/)
- [Um guia para iniciar estudos em BPMN (IV): Eventos Intermediários](https://blog.iprocess.com.br/2012/12/um-guia-para-iniciar-estudos-em-bpmn-iv-eventos-intermediarios/)
- [Um guia para iniciar estudos em BPMN (V): Subprocessos](https://blog.iprocess.com.br/2012/12/um-guia-para-iniciar-estudos-em-bpmn-v-subprocessos/)
- [Um guia para iniciar estudos em BPMN (VI): Swimlanes e Artefatos](https://blog.iprocess.com.br/2013/01/um-guia-para-iniciar-estudos-em-bpmn-vi-swimlanes-e-artefatos/)

- Para os diversos tipos de Gateways (muuuuuuito cobrados em provas), há um post com animações do meso blog da iprocess, vale a pena conferir:
- [https://blog.iprocess.com.br/2021/05/diferencas-entre-os-gateways-de-bpmn-com-animacoes/](https://blog.iprocess.com.br/2021/05/diferencas-entre-os-gateways-de-bpmn-com-animacoes/)

- Indo mais além, sobre diagramas de conversação e coreografia:
- [https://blog.iprocess.com.br/2013/08/bpmn-2-0-novos-diagramas-e-elementos-introducao-a-coreografia/](https://blog.iprocess.com.br/2013/08/bpmn-2-0-novos-diagramas-e-elementos-introducao-a-coreografia/)
- [https://blog.iprocess.com.br/2014/06/novos-diagramas-e-elementos-introducao-a-conversacao/](https://blog.iprocess.com.br/2014/06/novos-diagramas-e-elementos-introducao-a-conversacao/)
- [Poster-Resumo “BPMN 2.0 - Notação e Modelo de Processo de Negócio”](http://www.bpmb.de/images/BPMN2_0_Poster_PT.pdf)


### Conceitos de Governança de TI
- [ ] status [dom:: 0] [peso:: 3]


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

#### - ISO/IEC 27002 — Controles de Segurança da Informação
- [ ] status [dom:: 0] [peso:: 3]

-- Na verdade, são 4 tipos de controles apontados na Norma ISO 27002/2022. **São eles: 1. Controles Organizacionais, 2. Controles de Pessoal, 3. Controles Físicos e 4. Controles Tecnológicos. Vejamos abaixo uma descrição sobre isso:**
> Os controles da ISO 27002 são referenciados no Anexo da ISO 27001, para apoio à implementação de um Sistema de Gestão de Segurança da Informação (SGSI).

<font color="#548dd4">Tipos de Controles:  </font>
**Preventivos:** controles que são projetados para **IMPEDIR** uma ameaça  
**Detectivos:** controle que são projetados para **DETECTAR** uma ameaça  
**Corretivos:** controles que são projetados para **CORRIGIR** uma ameaça  
  
<font color="#76923c">Propriedades de Segurança da Informação  </font>
Confidencialidade  
Integridade  
Disponibilidade  

<font color="#31859b">Conceitos de Segurança Cibernética</font>  
Identificar  
Proteger  
Detectar  
Responder

![[Pasted image 20260829185258.png]]

- **Broken Access Control** → **2. Permitir ações que necessitem de login sem que o login tenha sido feito.**  
    Falhas de controle de acesso permitem que usuários executem ações sem a devida autorização.
    
- **Injection** → **4. Utilizar dados inseridos pelo usuário sem validação.**  
    Caracteriza ataques como SQL Injection e Command Injection.
    
- **Cryptographic Failures** → **3. Transmitir senhas em claro.**  
    Indica uso inadequado ou ausência de criptografia para proteger dados sensíveis.
    
- **Identification and Authentication Failures** → **1. Permitir ataques por força bruta ou outros ataques automatizados.**  
    Relaciona-se a falhas nos mecanismos de autenticação.

#### - Open Worldwide Application Security Project — OWASP
- [ ] status [dom:: 0] [peso:: 3]