---
tipo: metodo
---

# Como usar este cofre

Arquitetura leve: uma nota grande por matéria, tópicos marcados por campo inline, um único painel.

## Estrutura

| Onde | O quê |
|---|---|
| `MATERIAS/` | Dezenove notas grandes, uma por disciplina |
| `PAINEL` | Único painel. Gerado por consulta; você nunca o edita |
| `LTE - COMO ESTUDAR` | O método das três colunas para legislação estadual |
| `ESTRATEGIA` | Análise do certame e comparação com os editais FCC de CE e SP |
| `PROTOCOLO DE VIRADA DE EDITAL` | Leia agora, execute quando o edital sair |
| `DISCURSIVA` | Esqueleto de resposta e banco de temas |
| `DIARIO DE QUESTOES` | Uma linha por sessão |

## O ciclo

1. Estuda o tópico
2. Escreve o conteúdo **logo abaixo do cabeçalho daquele tópico** — prosa, tabela, print, lei colada
3. Ajusta `[dom:: N]` na linha do tópico
4. Faz as questões
5. Uma linha no diário
6. Fim

Passos 3 e 5 somados: menos de um minuto.

## As duas listas do painel, e por que são duas

**Seção 1 — projeção ancorada.** Só entram as matérias cuja pontuação é conhecida do edital baiano de
2019. Somam 285 pontos e produzem uma projeção que significa alguma coisa, porque tem denominador real.

**Seção 2 — cobertura preventiva.** Cinco disciplinas que a FCC cobra em Ceará ou São Paulo e que não
existiam na Bahia em 2019: Contabilidade Avançada e de Custos, Finanças Públicas, Fluência de Dados,
Direito Financeiro, Economia e Administração e Governança Pública. Mais a Reforma Tributária.

Elas entram com `pontos: 0` **de propósito**. Se eu chutasse uma pontuação para elas, a projeção da seção
1 viraria ficção — e a projeção é a única métrica do cofre que decide alguma coisa. Melhor ter uma
projeção honesta sobre 285 pontos reais e uma lista separada de cobertura, do que uma projeção inventada
sobre 400 pontos imaginários.

Isso **não significa estudar menos** essas matérias. Contabilidade Avançada e de Custos é candidata a 20
questões de peso 2 se a Bahia seguir o modelo FCC — o que a colocaria empatada com LTE em importância
relativa dentro da prova específica. Ela vale zero no painel e é crítica na realidade.

## Quando o edital sair

Passo 2 do [[PROTOCOLO DE VIRADA DE EDITAL]]: você atualiza o campo `pontos` nas dezenove notas, zera as
que não vierem, atribui valor às que vierem — e o painel inteiro se recalibra sozinho. É o momento em que
as duas listas viram uma só.

## Instalação

1. Instale o **Dataview** e ative *JavaScript Queries*
2. Abra o [[PAINEL]]
3. Nenhum outro plugin é necessário

## Se alguma consulta não renderizar

As seções 1, 2, 3, 4 e 7 dependem de o Dataview ler campos inline em linhas de tarefa. Se falhar,
coloque `dominio_medio:: 3.2` no topo de cada nota e ajuste uma vez por semana. Perde granularidade,
mantém a projeção. O conteúdo das notas não depende de plugin nenhum.

[[]]