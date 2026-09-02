---
tipo: referencia
---

# Questões — depositório diário

## Como funciona

Cada **caderno resolvido** vira **uma nota própria** dentro de `Questoes/Diario`.
Os dados ficam nas propriedades (frontmatter) da nota — não em texto solto — então
o Obsidian mostra, no topo da nota, uma tabela real com o nome de cada campo e um
espaço para o valor, com o tipo certo (número, data, lista):

| Propriedade | O que colocar |
| --- | --- |
| `tipo` | sempre `caderno` (não mexa) |
| `data` | data em que você resolveu o caderno |
| `materia` | nome exato da matéria (tabela abaixo) |
| `bloco` | bloco de pontuação da matéria (copia da tabela abaixo) |
| `assuntos` | um ou mais assuntos cobrados (clique em "+" para adicionar mais de um) |
| `slot` | S2, S3, S4 ou S5 |
| `total` | quantas questões tinha o caderno |
| `acertos` | quantas você acertou |
| `tempo_min` | minutos gastos no caderno inteiro (o painel calcula o ritmo por questão) |
| `erro_tipo` | desconhecimento, desatenção ou exceção — a causa dominante do erro |
| `banca` | opcional: FCC, FGV, Cebraspe ou mista |
| `origem` | `caderno` (padrão), `simulado` ou `revisão` |
| `obs` | observação livre e curta, se sobrar algo que `erro_tipo` não capturou |

Abaixo do frontmatter fica a seção **Erros a revisar**, para anotar em texto livre
a regra ou pegadinha que causou o erro.

## Instalação

Já feita neste cofre:

1. Pasta `Questoes` na raiz, com `Diario/` (uma nota por caderno) e `Paineis/`.
2. Plugin **Dataview** ativo, com **Enable JavaScript Queries** ligado (usado
   pelo painel Ganho potencial).
3. Plugin interno **Modelos** apontando para a pasta `TEMPLATE`, onde está
   `Questões - Caderno.md`. Para criar um caderno novo: crie a nota em
   `Questoes/Diario`, abra a paleta de comandos (Cmd/Ctrl+P) → **Templates:
   Insert template** → escolha **Questões - Caderno**.
4. Tipos de propriedade registrados (`.obsidian/types.json`) para que `total`,
   `acertos` e `tempo_min` apareçam como campo numérico, `data` como data e
   `assuntos` como lista de chips.

## Uso diário

1. Crie uma nota em `Questoes/Diario`. Nomeie como `AAAA-MM-DD Slot Matéria`
   (ex.: `2026-09-07 S2 Contabilidade Avançada`). **O slot no nome não é
   estético — sem ele, dois cadernos da mesma matéria no mesmo dia (o do S2 e
   o de reforço no S4) disputam o mesmo nome de arquivo e o Obsidian recusa a
   criação do segundo.**
2. Insira o modelo **Questões - Caderno** e preencha as propriedades.
3. Repita: **um caderno = uma nota**. Caderno misto (duas ou três matérias)
   vira duas ou três notas — não dá mais para misturar, porque cada nota só
   tem um campo `materia`.

Veja [[_exemplo-caderno]] para um exemplo já preenchido.

## Regras que evitam dado inconsistente

- **Não digite percentual, nem qualquer outra agregação** ("total do mês",
  "média da semana"). Guarde `total` e `acertos` brutos; todo dado derivado
  mora em consulta, nunca em nota. Percentual digitado transforma média
  semanal em média de médias, e um caderno de 8 questões pesa igual a um
  de 60.
- **Use os nomes exatos** de `materia` e `bloco` desta tabela. "Cont. Avançada"
  e "Contabilidade Avançada" viram dois grupos distintos nos painéis.
- **Simulado ou revisão:** troque `origem`, para separar depois o desempenho
  sob pressão de tempo (simulado) e a repetição de erro antigo (revisão) do
  desempenho em caderno livre.

## Valores permitidos

`slot`: S2 · S3 · S4 · S5

`erro_tipo`: desconhecimento · desatenção · exceção

`origem`: caderno · simulado · revisão

`banca` (opcional): FCC · FGV · Cebraspe · mista

### matéria → bloco de pontuação

Os nomes abaixo são os mesmos das colunas B e C da aba Tópicos da planilha
`Cronograma_SEFAZ_CE_2027.xlsx`, para que os dois sistemas cruzem sem tradução.

| matéria | bloco | pontos |
| --- | --- | --- |
| Contabilidade Avançada | Cont. Avançada e de Custos | 40 |
| Contabilidade Custos | Cont. Avançada e de Custos | 40 |
| Direito Tributário | Direito Tributário | 40 |
| Legislação Tributária Estadual | Legislação Tributária | 40 |
| Finanças Públicas | Finanças Públicas | 20 |
| Ciências De Dados | Fluência de Dados | 20 |
| Segurança Da Informação E Proteção De Dados | Fluência de Dados | 20 |
| Matemática Financeira/Estatística E Raciocínio Lógico | Mat. Fin./Estat./RLM | 12 |
| Direito Constitucional | Const./Adm./Civil/Penal | 12 |
| Direito Administrativo | Const./Adm./Civil/Penal | 12 |
| Direito Civil | Const./Adm./Civil/Penal | 12 |
| Direito Penal | Const./Adm./Civil/Penal | 12 |
| Língua Portuguesa | Língua Portuguesa | 10 |
| Administração Pública E Governança Pública | Adm. e Governança | 10 |
| Microeconomia | Economia | 10 |
| Macroeconomia | Economia | 10 |
| Contabilidade Geral | Cont. Geral e Pública | 10 |
| Contabilidade Pública | Cont. Geral e Pública | 10 |
| Direito Financeiro | Direito Financeiro | 8 |
| Auditoria | Auditoria | 8 |

## Painéis

Em `Questoes/Paineis`:

**Visão de desempenho** — Hoje, Dia consolidado, Semana por matéria,
Mês por bloco, Evolução, Por slot.

**Visão de decisão** — Ganho potencial, Fila de reforço, Diagnóstico de erro
(este último só rende dado depois que `erro_tipo` começa a ser preenchido).

Abra qualquer um deles com o Dataview ativo.

## O ritual que fecha a alça

Painel que ninguém abre é enfeite. Reserve um horário fixo semanal (ex.: 1h no
domingo) e use nesta ordem:

1. **Ganho potencial** — ver se o topo da fila mudou.
2. **Fila de reforço** — decidir o que refazer.
3. **Diagnóstico de erro** — decidir se o problema da semana foi conteúdo ou
   leitura.

Se o topo do item 1 mudou, troque o conteúdo do slot S4 da semana seguinte.
