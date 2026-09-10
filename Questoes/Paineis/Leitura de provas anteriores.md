---
tipo: painel
---

# Leitura de provas anteriores

Registro das provas de fazenda estadual já prestadas, com o que cada resultado revela sobre a preparação para a Bahia. O valor desta nota está na **comparação entre provas** — uma prova isolada mostra oscilação, duas mostram padrão.

Os resultados são **estáticos de propósito**: as provas aconteceram, os números não mudam. Só o bloco de peso da Bahia é vivo, lido do frontmatter de `MATERIAS/`.

> [!tip]- Como acrescentar uma prova nova
> Mande o PDF de resultado da FCC. O que precisa entrar: sistema de pontuação (padronizado ou bruto ponderado), acertos por sub-prova, peso de cada bloco, classificação e situação. Depois de acrescentar a seção da prova, **reveja a tabela "O que se repete"** — é ela que carrega a conclusão, não as seções individuais.

## Provas registradas

| Prova | Cargo | Sistema de pontuação | Nota | Mínimo | Classificação | Situação |
| --- | --- | --- | --- | --- | --- | --- |
| SEFAZ-CE 2026 | Auditor-Fiscal 1ª Classe | Escore padronizado | 182,83 | 150 | 1515º | Não classificado para a discursiva |
| SEFAZ-MT 2025 | Fiscal de Tributos Estaduais | Bruto ponderado | 173,00 | 112 | 378º | **Habilitado** |

## O número que não muda

| Prova | C. Gerais | C. Específicos | Total | Aproveitamento | Erros |
| --- | --- | --- | --- | --- | --- |
| SEFAZ-CE 2026 | 62/80 | 54/80 | **116/160** | 72,5% | 44 |
| SEFAZ-MT 2025 | 59/80 | 57/80 | **116/160** | 72,5% | 44 |

<mark style="background:#fff88f">Duas provas diferentes, de estados diferentes, com editais diferentes: exatamente 116 acertos em 160 nas duas. Exatamente 44 erros.</mark>

Isso diz duas coisas. A primeira é que o nível está **estável e medido** — 72,5% não é sorte nem oscilação, é o patamar real. A segunda é mais dura: a diferença entre "habilitado em 378º" e "não classificado em 1515º" **não veio de você**. Veio do sistema de pontuação e da força do campo. Não dá para contar com o edital ser favorável; o que muda o resultado é mover o patamar — e mover onde pesa.

## Os dois sistemas que a FCC usa

A banca alterna entre dois modelos, e a estratégia muda com eles:

| | SEFAZ-CE 2026 | SEFAZ-MT 2025 |
| --- | --- | --- |
| Modelo | `NP = ((acertos − média)/DP) × 10 + 50` | `Nota = acertos × peso` |
| Nota é relativa ao grupo | Sim | Não |
| Peso de Específicos | 2× | 2× |
| Consequência | Questão difícil que o pelotão erra vale mais na classificação | Cada acerto vale igual; só o volume importa |

**O que é constante nos dois: Específicos vale o dobro de Gerais.** No CE isso deu 1,96× por acerto; no MT, exatos 2×. É a única regra da FCC que se manteve entre os dois editais, e é a que deve guiar a alocação.

## O que se repete nas duas provas

Esta é a tabela que importa. Uma prova mostra ruído; duas mostram sinal.

| Área | CE 2026 | MT 2025 | Leitura |
| --- | --- | --- | --- |
| **Legislação Tributária Estadual** | 12/20 · 60% | 6/15 · **40%** | <mark style="background:#ffb8b8">Fraqueza confirmada e piorando. Foi a maior perda ponderada nas **duas** provas</mark> |
| **Matemática Financeira** | *(oculta em composto: 83%)* | 5/10 · **50%** | Fraqueza que só apareceu quando o MT separou a sub-prova |
| Direito Tributário | 14/20 · 70% | 11/15 · 73% | Estável em ~70%. Nem força nem buraco — teto baixo |
| Contabilidade | 11/20 · 55% *(Avançada+Custos)* | 8/10 · 80% *(Geral+Custos)* | O problema é a parte **Avançada**, não Geral nem Custos |
| **TI / Fluência de Dados** | 8/10 · 80% | 38/45 · 84% | Força consistente — mas ver a ressalva de volume abaixo |
| **Auditoria** | 8/8 · 100% | 9/10 · 90% | Força confirmada. Teto atingido, sem ganho disponível |
| Const./Adm./Civil/Penal | 10/12 · 83% | 6/8 · 75% | Sólido |
| Língua Portuguesa | 6/10 · 60% | 10/10 · 100% | Volátil — a amostra de 10 não sustenta conclusão |
| Economia / Finanças Públicas | 6/10 e 9/10 | **0/5** | Volátil, com um zero absoluto no MT. Investigar |
| Estatística / RLM | *(em composto)* | 5/7 e 7/10 · ~70% | Medianos quando medidos separados |

### Três conclusões que sobrevivem às duas provas

**1. LTE é o gargalo, sem margem para dúvida.** Foi a maior perda ponderada no CE (22,7% de tudo que perdeu) e no MT (26,9%). Os percentuais foram 60% e 40% — e o MT é o mais recente. É a disciplina que decide concurso de fazenda estadual e a única que nenhum material comercial cobre bem.

**2. Sub-prova composta esconde fraqueza.** No CE, "Matem. Financ./Estatística e Rac. Lógico" veio 10/12 (83%) e parecia área resolvida. O MT separou os três: Matemática Financeira 50%, Estatística 71%, RLM 70%. A média ponderada real dos três no MT é 63%, não 83%. <mark style="background:#fff88f">Quando uma sub-prova agrupa matérias, o número de cima não serve para decidir estudo.</mark>

**3. Força com volume alto ainda sangra pontos.** TI foi 84% no MT — leitura de força. Mas eram **45 questões de peso 2**, mais da metade de todo o bloco Específicos. Os 7 erros custaram 14 pontos: a **segunda maior perda da prova inteira**, atrás só de LTE. Percentual alto em volume alto perde mais que percentual baixo em volume baixo.

## Peso na Bahia — premissa de trabalho

Premissa atual, definida por você em 2026-09-09: **o edital BA 2027 deve se parecer com o do CE 2026, e TI/Fluência de Dados caem sempre.** Isso substitui a leitura anterior baseada na âncora BA 2019, que tratava Fluência de Dados como peso zero. Quando o edital sair, revisar esta seção primeiro.

O bloco abaixo ainda lê a âncora **BA 2019** do frontmatter das notas. Serve como referência histórica, não como prioridade — a âncora de 2019 não conhecia Fluência de Dados nem Contabilidade Avançada como blocos próprios.

```dataviewjs
const CE = [
  ["Auditoria", 8, 8, ["P1 - Auditoria"]],
  ["Administração e Governança Pública", 10, 9, ["P1 - Administração Geral", "P1 - Administração e Governança Pública"]],
  ["Finanças Públicas", 10, 9, ["P2 - Finanças Públicas"]],
  ["Matem. Financ./Estatística e Rac. Lógico", 12, 10, ["P2 - Matemática Financeira", "P2 - Estatística Aplicada", "P1 - Estatística", "P1 - Raciocínio Lógico"]],
  ["Dir. Const., Admin., Civil e Penal", 12, 10, ["P1 - Direito Constitucional", "P1 - Direito Administrativo", "P1 - Direito Civil", "P1 - Penal"]],
  ["Fluência de Dados", 10, 8, ["P2 - Fluência de Dados BD"]],
  ["Direito Financeiro", 8, 6, ["P1 - Direito Financeiro"]],
  ["Contabilidade Geral e Pública", 10, 7, ["P1 - Contabilidade Geral", "P2 - CASP"]],
  ["Direito Tributário", 20, 14, ["P2 - Direito Tributário"]],
  ["Legislação Tributária Estadual", 20, 12, ["P2 - Legislação Tributária Estadual (BA)"]],
  ["Língua Portuguesa", 10, 6, ["P1 - Língua Portuguesa"]],
  ["Economia", 10, 6, ["P1 - Macro Economia", "P1 - Micro e Finanças Públicas"]],
  ["Contabilidade Avançada e de Custos", 20, 11, ["P2 - Contabilidade Avançada e de Custos"]],
];

const porNome = {};
for (const p of dv.pages('"MATERIAS"')) porNome[p.file.name] = p;

const linhas = CE.map(([nome, total, acertos, notas]) => {
  let pontos = 0, prios = new Set(), faltando = [];
  for (const n of notas) {
    const p = porNome[n];
    if (!p) { faltando.push(n); continue; }
    pontos += Number(p.pontos ?? 0);
    if (p.prioridade) prios.add(String(p.prioridade));
  }
  return {
    nome, total, acertos,
    pct: Math.round((100 * acertos) / total),
    pontos, composta: notas.length > 1 ? "*" : "",
    prio: [...prios].sort().join(" / ") + (faltando.length ? ` ⚠️ não encontrada: ${faltando.join(", ")}` : ""),
  };
});

linhas.sort((a, b) => b.pct - a.pct);

dv.table(
  ["Sub-prova do CE 2026", "Resultado", "%", "Pontos na âncora BA 2019", "Prioridade no vault"],
  linhas.map(r => [r.nome, `${r.acertos}/${r.total}`, r.pct + "%", r.pontos + r.composta, r.prio])
);
```

`*` marca sub-prova composta — o valor é a soma dos `pontos` de várias notas e infla quando elas se sobrepõem (o caso de Mat. Fin./Estatística/RLM). As linhas sem `*` têm mapeamento exato.

## Ordem de ataque

Revisada em 2026-09-09 com as duas provas e a premissa de que a BA se parece com o CE.

| # | Bloco | Lógica |
| --- | --- | --- |
| 1 | **LTE — ICMS estadual, Lei Kandir, Simples Nacional** | Maior perda ponderada nas duas provas (60% e 40%). Nenhuma outra disciplina aparece em primeiro lugar duas vezes |
| 2 | **Matemática Financeira** | 50% no MT, escondida atrás de um composto no CE. Peso alto e fraqueza recém-revelada |
| 3 | **Contabilidade Avançada — armadilhas numéricas da FCC** | 55% no CE. O MT mostrou que Geral e Custos estão em 80%: o buraco é a parte Avançada. Taxa contratual × efetiva, dividendo proposto, VJORA no resultado |
| 4 | **Custos — Ponto de Equilíbrio** | 20,1% da disciplina, 4/9 no caderno de 09/09. Fraqueza medida no vault, ainda não isolada em prova |
| 5 | **TI / Fluência de Dados — fechar os 16%** | 80-84% nas duas. Só entra alto na lista porque você confirmou que cai sempre e porque volume alto multiplica erro: no MT custou 14 pontos |
| 6 | Direito Tributário | ~70% estável nas duas. Teto baixo que não se move sozinho |
| 7 | Economia e Finanças Públicas | 0/5 no MT contra 90% no CE. Antes de estudar, investigar o que aconteceu — pode ser recorte de conteúdo, não desconhecimento |
| 8 | Auditoria, Português, Const./Adm./Civil/Penal | Manutenção. 90-100% ou volátil por amostra pequena |

## Aberto

- **O zero em Economia e Finanças Públicas (MT).** 0/5 é resultado improvável para quem fez 90% em Finanças Públicas no CE. Vale abrir a prova do MT e ver se o recorte era outro (finanças públicas estaduais? contas do MT?) antes de tratar como lacuna de conteúdo.
- **A discursiva.** No CE não foi corrigida (não classificado). No MT houve habilitação. Enquanto a objetiva não estabilizar acima do corte, o bloco de discursiva do sábado (S5 em [[Slots (Grade Semanal)]]) compete por tempo com LTE.
