Referência dos slots (`S1`–`S5`) usados no campo `slot` de `Questoes/Diario`. Fonte: `Cronograma_SEFAZ_CE_2027.xlsx`, abas `Grade Semanal`, `Protocolo` e `Registro Diário`.

## O que cada slot significa

*(da aba Registro Diário)*

| Slot | Duração | Função |
| --- | --- | --- |
| S1 | 30 min | Revisão ativa — recuperação de memória sem consultar a nota. Nunca aparece no `Diario` porque não é caderno de questões. |
| S2 | 90 min | Leitura nova / matéria pesada do dia. |
| S3 | 90 min | Aprofundamento + questões. |
| S4 | 60 min | Bloco fixo de 60 min, matéria secundária do dia. |
| S5 | 90 min | Rodízio — matérias que revezam. |

Grade padrão: 6h/dia, 42h/semana.

## Grade semanal (matéria por dia × slot)

*Atualizada em 2026-09-07 — ver "Reconciliação com o Ciclo VINTEUM" mais abaixo.*

| Dia     | S2 · 90min                     | S3 · 90min                                  | S4 · 60min                         | S5 · 90min                                               |
| ------- | ------------------------------ | ------------------------------------------- | ---------------------------------- | -------------------------------------------------------- |
| Segunda | Contabilidade Avançada         | Direito Tributário                          | Língua Portuguesa                  | Ciências de Dados                                        |
| Terça   | Legislação Tributária Estadual | Contabilidade Avançada                      | Auditoria                          | Finanças Públicas                                        |
| Quarta  | Mat. Financeira/Estatística/RLM| Contabilidade de Custos                     | Direito Financeiro                 | Rodízio 4 (Constitucional, Administrativo, Civil, Penal) |
| Quinta  | Contabilidade Avançada         | Legislação Tributária Estadual              | Adm. Pública e Governança          | Ciências de Dados                                        |
| Sexta   | Direito Tributário             | Finanças Públicas                           | Segurança da Informação            | Mat. Financeira/Estatística/RLM                          |
| Sábado  | Ciências de Dados               | Cont. Geral (ímpares)/Cont. Pública (pares) | Micro (ímpares)/Macro (pares)      | Discursiva                                               |
| Domingo | Simulado                       | Simulado                                    | Correção com caderno de erros — 2h | Fechamento de ciclo — 1h                                 |

S1 (revisão ativa, todos os dias) e, no domingo, o simulado ocupa S1+S2+S3 (3h).

## Datas do protocolo

- **Início do ciclo formal**: 07/09/2026 (segunda-feira).
- **Fim**: 31/01/2027 — 21 semanas.
- **Fases**: semanas 1–13 construção (leitura nova conforme a aba `Tópicos`); 14–18 consolidação (só questões e revisão); 19–21 reta final (lei seca e simulados).
- Reforma Tributária não tem slot próprio — está dentro do item 28 de Direito Tributário e atravessa a Legislação Estadual.

**Nota**: os cadernos registrados em `Questoes/Diario` entre 01 e 04/09/2026 são anteriores ao início oficial do ciclo (07/09) — não seguem a grade acima de propósito, são aquecimento/diagnóstico pré-ciclo.

## Protocolo de revisão espaçada (por tópico, aba Tópicos)

| Intervalo | Critério |
| --- | --- |
| Mesmo dia | 20 questões sobre o que foi lido. Abaixo de 60%, releia antes de agendar. |
| 24 horas | Recuperação ativa: reconstrua o esquema sem consultar a nota. |
| 7 dias | 15 questões inéditas. 70% libera para 30 dias. |
| 30 dias | 10 questões e caderno de erros. 80% libera para 60 dias. |
| 60 dias | Bateria mista intercalada. Abaixo de 75%, retorna para a fila de 7 dias. |

Esse é um sistema de revisão espaçada **por tópico individual** (902 tópicos na aba `Tópicos`, com datas de revisão calculadas), diferente do `Agenda de releitura` do Obsidian, que opera por **resumo** (nota de `MATERIAS`) e por **% de acerto do bloco**. Os dois não são a mesma coisa e não se substituem — o Excel sequencia o que ler linha a linha; o Obsidian mede o que já foi lido.

## Ressalvas já documentadas na planilha (aba Protocolo)

- **Pontuação**: pontos por disciplina vêm de análise de banca fornecida pelo usuário (160 questões, Gerais peso 1, Específicos peso 2) — não conferida contra o edital de abertura.
- **Avançada x Custos**: a divisão dos 40 pontos do bloco entre os dois assuntos não consta do edital — é arbitragem (3 partes Avançada, 1 parte Custos), não dado. Ver seção "Avançada x Custos" abaixo para o que a VINTEUM permite refinar aqui.
- **Legislação Estadual**: o verticalizado lista só as cinco normas; foram acrescentados 30 subtópicos de estrutura do ICMS vindos do cofre (origem "cofre" na coluna I da aba Tópicos).
- **LC nº 227/2026**: norma posterior ao conhecimento confiável de quem montou a planilha — ler no texto primário.
- **Discursivas**: peso 2, corrigidas só para quem soma 150 nas objetivas. Ocupam o slot S5 de sábado.

## Reordenação por domínio real (TecConcursos), 2026-09-06

Depois de calcular `dom::` (0-5) nos checklists VINTEUM das notas de `MATERIAS` a partir do histórico de questões do TecConcursos, tentei casar esses tópicos com a coluna `Tópico` da aba `Tópicos` da planilha. Cobertura baixa: só **43 de 173** itens com `dom:: > 0` batem exatamente com o texto do edital usado na planilha — a maioria diverge porque o VINTEUM agrupa temas de um jeito e o edital descreve linha a linha de outro (ex.: VINTEUM "Sintaxe" não tem equivalente 1:1 nas linhas "Morfossintaxe." / "Pronomes." / "Concordância nominal e concordância verbal." do edital). Não forcei correspondência nos outros 130 — ficaram como estavam.

Para os **35 tópicos únicos que bateram com certeza** (deduplicando as 4 notas de Fluência de Dados, que apontam para as mesmas linhas de "Ciências De Dados"), apliquei uma **troca dentro de cada disciplina**: peguei as datas/semanas/slots que essas linhas já ocupavam, e realoquei — tópico com `dom::` mais baixo (menos praticado no TEC) recebe a data mais cedo disponível entre elas; `dom::` mais alto (já domina) vai para a mais tarde. Nenhuma data nova foi criada e nenhuma outra linha da planilha foi tocada; é só uma permutação entre as linhas confirmadas de cada disciplina. Backup pré-troca: `Cronograma_SEFAZ_CE_2027 (backup pre-swap-slots-dom 2026-09-06).xlsx`.

Disciplinas com mudança real (dom variava entre os tópicos confirmados): Direito Constitucional, Contabilidade Geral, Contabilidade Avançada, Auditoria, Matemática Financeira/Estatística/RLM. Nas demais (Direito Administrativo, Direito Tributário, Ciências De Dados) os tópicos confirmados tinham todos o mesmo `dom::`, então nada mudou. `P2 - Tecnologia da Informação.md` não tem disciplina correspondente na planilha (o bucket mais próximo, "Segurança Da Informação E Proteção De Dados", é só LGPD/criptografia) — ficou de fora.

**Isso cobre só ~4% das 902 linhas.** Se quiser mais cobertura, as opções são: (a) reescrever os nomes dos tópicos do checklist VINTEUM para casar com a redação do edital, ou (b) reordenar por média de `dom::` da disciplina inteira em vez de tópico a tópico (tabela abaixo).

## Média de `dom::` por disciplina (nota de MATERIAS), 2026-09-07

Média só sobre os itens com `dom:: > 0` (correspondência confirmada no TEC) — os que ficaram em `dom:: 0` por falta de match são excluídos da média, não contam como "zero domínio". Ordenado do mais fraco pro mais forte.

| Disciplina (nota) | Itens medidos / total | Média `dom::` |
| --- | --- | --- |
| P2 - CASP | 12/12 | 2.33 |
| P1 - Raciocínio Lógico | 6/11 | 2.83 |
| P1 - Estatística | 3/7 | 2.67 |
| P2 - Estatística Aplicada | 3/7 | 2.67 |
| P1 - Macro Economia | 11/12 | 3.00 |
| P1 - Contabilidade Geral | 21/26 | 3.38 |
| P2 - Contabilidade Avançada e de Custos | 21/26 | 3.38 |
| P1 - Direito Constitucional | 8/14 | 3.38 |
| P2 - Tecnologia da Informação | 6/10 | 3.33 |
| P2 - Fluência de Dados (BD/CD/SGE/SGE-C) | 7/13 | 3.57 |
| P2 - Matemática Financeira | 11/11 | 3.64 |
| P1 - Penal | 3/7 | 3.67 |
| P1 - Direito Administrativo | 9/13 | 3.78 |
| P1 - Língua Portuguesa | 8/9 | 3.75 |
| P1 - Direito Civil | 8/9 | 3.50 |
| P2 - Direito Tributário | 11/14 | 3.91 |
| P1 - Auditoria | 7/9 | 3.86 |
| P1 - Direito Financeiro | 3/8 | 4.00 |
| P2 - Legislação Tributária Estadual (BA) | 0/9 | n/a — nenhum item bateu com o TEC |
| P2 - Reforma Tributária | 0/11 | n/a — tema novo, sem histórico no TEC |

Leitura: CASP, RLM e Estatística são as disciplinas com pior domínio medido — priorize aí. Legislação Tributária Estadual e Reforma Tributária não têm nenhum dado do TEC (a primeira por citar artigos de lei específicos que o TEC não categoriza por nome; a segunda por ser tema novo pós-reforma) — tratar como prioridade alta por padrão, já que "sem dado" aqui não é o mesmo que "domina".

## Reconciliação com o Ciclo VINTEUM, 2026-09-07

`Questoes/Ciclos de estudo (VINTEUM).md` tinha sua própria grade semanal ("Cronograma personalizado — Fase Avançada"), calculada a partir do Ganho Potencial em 2026-09-05, com estrutura de dia diferente desta aqui — ex.: segunda-feira lá incluía Direito Administrativo e Legislação Tributária Estadual, que não apareciam na Grade Semanal desta nota. Duas grades vivas para a mesma semana, sem se comunicar.

Resolvi mantendo esta nota (que alimenta o `slot` real do `Diario` e a planilha) como única fonte, e usando a lógica de priorização por Ganho Potencial do Ciclo VINTEUM pra corrigir esta grade em vez de manter as duas. Ganho Potencial recalculado agora (nenhum caderno novo desde 04/09, os números batem com os de 05/09):

| Bloco | Ganho potencial | % acerto (30d) |
| --- | --- | --- |
| Cont. Avançada e de Custos | 8,86 | 62,9% |
| Mat. Fin./Estat./RLM | 5,70 | 37,5% |
| Fluência de Dados | 4,08 | 64,6% |
| Direito Tributário | 3,60 | 76,0% |
| Cont. Geral e Pública | 2,41 | 60,9% |
| Const./Adm./Civil/Penal | 1,95 | 68,8% |
| Auditoria | 1,57 | 65,4% |

Comparando com a Grade Semanal antiga: Direito Tributário e Legislação Tributária Estadual tinham 3x/semana cada mesmo com Direito Tributário já em 76% de acerto e Legislação Tributária Estadual sem nenhum dado recente; Mat. Fin./Estat./RLM tinha só 1x/semana apesar do 2º maior Ganho Potencial (5,70) — e a tabela de `dom::` por disciplina acima reforça isso, com RLM/Estatística entre as mais fracas medidas. Fluência de Dados também estava abaixo do seu Ganho Potencial (2x/semana, ganho 4,08, 3º lugar).

**Duas trocas feitas** na Grade Semanal (nota + planilha, aba `Grade Semanal`):

- **Quarta, S2**: Direito Tributário → Mat. Financeira/Estatística/RLM. Direito Tributário cai de 3x para 2x/semana (ainda com peso alto, mas já domina bem); RLM/Estatística sobe de 1x para 2x.
- **Sábado, S2**: Legislação Tributária Estadual → Ciências de Dados. Legislação Tributária Estadual cai de 3x para 2x (mantém cobertura, sem dado de desempenho ainda pra justificar 3x); Fluência de Dados sobe de 2x para 3x, alinhado ao seu Ganho Potencial.

Não mexi no resto: Contabilidade Avançada (3x, já bate com o maior Ganho Potencial), Auditoria (1x, bate com o menor ganho da lista), e o "Rodízio 4" de quarta (Constitucional/Administrativo/Civil/Penal) — esse último cobre 4 matérias num slot só por semana, mais lento que o ideal, mas mudar isso trocaria a mecânica de rodízio em si, não só a prioridade; fica como ponto em aberto.

CASP em particular (média `dom::` 2,33, a mais fraca medida) ainda alterna com Contabilidade Geral no sábado (S3, ímpares/pares) — se quiser priorizar CASP de propósito, dá pra parar de alternar e fixar CASP toda semana, mas isso muda a cadência em vez de só a prioridade, então não fiz sem confirmar.

A seção "Cronograma personalizado — Fase Avançada" do Ciclo VINTEUM foi marcada como histórica (ver nota lá) — a grade ativa agora é só esta.
