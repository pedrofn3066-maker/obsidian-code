---
tipo: painel
---

# Leitura de provas anteriores

Registro das provas de fazenda estadual já prestadas, com o que cada resultado revela sobre a preparação para a Bahia. O valor desta nota está na **comparação entre provas** — uma prova mostra oscilação, duas mostram padrão, três permitem descartar o que era coincidência.

Os resultados são **estáticos de propósito**: as provas aconteceram, os números não mudam. Só o bloco de peso da Bahia é vivo, lido do frontmatter de `MATERIAS/`.

> [!tip]- Como acrescentar uma prova nova
> Mande o PDF de resultado da FCC. O que precisa entrar: sistema de pontuação, acertos por sub-prova, peso de cada bloco, classificação e situação. Depois de acrescentar a seção da prova, **revise a tabela "O que se repete"** — é ela que carrega a conclusão, e cada prova nova pode derrubar uma leitura anterior. Já aconteceu: o SP derrubou a leitura de que Fluência de Dados era força consistente.

## Provas registradas

| Prova | Cargo | Sistema | Estrutura | Nota | Mínimo | Classificação | Situação |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SEFAZ-CE 2026 | Auditor-Fiscal 1ª Classe | Escore padronizado | 2 provas · 160 q | 182,83 | 150 | 1515º | Não classificado para a discursiva |
| SEFAZ-MT 2025 | Fiscal de Tributos Estaduais | Bruto ponderado | 2 provas · 160 q | 173,00 | 112 | 378º | Habilitado |
| SEFAZ-SP 2025 | Auditor Fiscal da Receita Estadual | Bruto ponderado | 3 provas · 260 q | 210,00 | 204 | 2375º | Habilitado, por 6 pontos |

## O patamar medido

| Prova | Questões | Acertos | Taxa bruta |
| --- | --- | --- | --- |
| SEFAZ-CE 2026 | 160 | **116** | 72,5% |
| SEFAZ-MT 2025 | 160 | **116** | 72,5% |
| SEFAZ-SP 2025 | 260 | 165 | 63,5% |

<mark style="background:#fff88f">CE e MT: exatamente 116 acertos em 160, exatamente 44 erros, nas duas.</mark> Estados, editais e cargos diferentes, mesmo número. Isso mede o patamar: 72,5% não é sorte, é o nível real numa prova com o formato do CE.

O SP quebra o padrão para baixo — 63,5%, nove pontos percentuais abaixo. Aquela prova tinha 100 questões a mais e escopo bem mais largo: Inglês, Direito Empresarial, Raciocínio Crítico, e separação entre básico e avançado em Tributário e Legislação. **Amplitude expõe buraco.** Quanto mais largo o edital, mais o patamar cai — o que importa saber ao apostar que a BA se parece com o CE.

A consequência das três juntas é dura: entre "não classificado em 1515º" (CE), "habilitado em 378º" (MT) e "habilitado por 6 pontos em 2375º" (SP), o que mudou foi o sistema de pontuação, o tamanho do campo e a amplitude do edital — **não o seu desempenho**, que ficou estável. Não dá para contar com o edital ser favorável.

## Os sistemas que a FCC usa

Três provas, três desenhos:

| | CE 2026 | MT 2025 | SP 2025 |
| --- | --- | --- | --- |
| Modelo | `NP = ((acertos − média)/DP) × 10 + 50` | `Nota = acertos × peso` | `Nota = acertos × peso` |
| Nota relativa ao grupo | Sim | Não | Não |
| Blocos | 2 | 2 | 3 |
| Peso do bloco específico | 2× | 2× | 2× |

<mark style="background:#fff88f">A única regra constante nas três: o bloco de Conhecimentos Específicos vale o dobro.</mark> É a única coisa da FCC com que dá para contar, e é o que deve guiar a alocação de tempo.

## O que se repete nas três provas

| Área | CE 2026 | MT 2025 | SP 2025 | Leitura |
| --- | --- | --- | --- | --- |
| **Legislação Tributária Estadual** | 12/20 · 60% | 6/15 · 40% | básica 6/15 · 40%<br>avançada 16/25 · 64% | <mark style="background:#ffb8b8">Maior perda ponderada nas três provas. Nenhuma outra área aparece em 1º mais de uma vez</mark> |
| **Contabilidade Avançada e de Custos** | 11/20 · 55% | — | 10/20 · 50% | Fraqueza confirmada duas vezes, sempre em torno de metade |
| Contabilidade Geral | 7/10 · 70% *(com Pública)* | 8/10 · 80% *(com Custos)* | 15/15 · **100%** | O SP separou e provou: Geral está resolvida. O buraco é a parte **Avançada** |
| Direito Tributário | 14/20 · 70% | 11/15 · 73% | básico 67%<br>avançado 60% | Estável em ~60-73%. Teto baixo que não se move sozinho |
| **Fluência de Dados / TI** | 8/10 · 80% | 38/45 · 84% | 4/10 · **40%** | <mark style="background:#ffb8b8">Volátil, não força. Ver a revisão abaixo</mark> |
| **Auditoria** | 8/8 · 100% | 9/10 · 90% | 9/10 · 90% | Única força confirmada nas três. Teto atingido |
| Direito (Const./Adm./Civil/Penal…) | 10/12 · 83% | 6/8 · 75% | 11/25 · **44%** | Desaba quando o escopo inclui Empresarial e Financeiro |
| Economia e Finanças Públicas | Econ 60% · Fin.Púb 90% | 0/5 · **0%** | 7/15 · 47% | Quando vêm juntas, afunda. Ver hipótese abaixo |
| Língua Portuguesa | 6/10 · 60% | 10/10 · 100% | 24/30 · 80% | Volátil nas amostras pequenas; 80% em 30 questões é o número confiável |
| Mat. Financeira / Estatística | 10/12 · 83% *(com RLM)* | MF 50% · Est 71% | 10/15 · 67% | ~65%. O 83% do CE era composto e enganava |
| Adm. Geral e Pública | 9/10 · 90% | — | 12/15 · 80% | Sólido |

### Conclusões que sobrevivem às três provas

**1. LTE é o gargalo, definitivamente.** Maior perda ponderada no CE (22,7%), no MT (26,9%) e no SP (20,8%, somando básica e avançada). Três provas, três primeiros lugares. Nenhuma outra área chega perto dessa consistência — e é a disciplina que nenhum material comercial cobre bem.

**2. O problema em contabilidade é a Avançada, e agora está provado.** O SP separou Contabilidade Geral (15/15, **100%**) de Contabilidade Avançada e de Custos (10/20, 50%). O CE já apontava 55% na Avançada. O MT, que juntava Geral com Custos, mostrava 80% e mascarava tudo.

**3. Sub-prova composta esconde fraqueza — dois exemplos comprovados.** O CE mostrou "Matem. Financ./Estatística e Rac. Lógico" em 83%; o MT separou e revelou Matemática Financeira em 50%. O MT mostrou "Contabilidade Geral e de Custos" em 80%; o SP separou e revelou Avançada em 50%. <mark style="background:#fff88f">Quando uma sub-prova agrupa matérias, o número de cima não serve para decidir estudo.</mark>

> [!warning]- Revisão: Fluência de Dados não é força consistente
> A versão anterior desta nota, escrita com apenas CE e MT, dizia que TI/Fluência de Dados era "força consistente" — 80% e 84%. **O SP derruba isso: 4/10, 40%.** Com três pontos (80%, 84%, 40%) o quadro é de volatilidade, não de domínio.
>
> A amostra do SP é pequena (10 questões) e a do MT é grande (45), então o peso da evidência ainda favorece "razoavelmente bom". Mas não dá mais para tratar como área resolvida — e você registrou que TI e Fluência de Dados caem sempre, o que a torna obrigatória. No MT, mesmo com 84%, os 7 erros em 45 questões de peso 2 custaram 14 pontos: a segunda maior perda daquela prova. **Percentual alto em volume alto perde mais que percentual baixo em volume baixo.**

> [!note]- Hipótese sobre Economia e Finanças Públicas
> Os três resultados: no CE vieram **separadas** (Economia 6/10 = 60%, Finanças Públicas 9/10 = 90%); no MT e no SP vieram **juntas** e afundaram (0/5 e 7/15 = 47%).
>
> A hipótese que os dados sustentam é que **Economia é a metade fraca e Finanças Públicas a metade forte** — somadas, a primeira arrasta a segunda. Isso encaminha a pendência aberta sobre o 0/5 do MT, mas não fecha: você ia conferir o recorte daquelas 5 questões. Se confirmar que eram de Economia, a conclusão está fechada e o alvo de estudo é Economia, não Finanças Públicas.

## Peso na Bahia — premissa de trabalho

Premissa definida por você em 2026-09-09: **o edital BA 2027 deve se parecer com o do CE 2026, e TI/Fluência de Dados caem sempre.** Isso substitui a leitura baseada na âncora BA 2019, que tratava Fluência de Dados e Contabilidade Avançada como peso zero. Quando o edital sair, revisar esta seção primeiro.

O bloco abaixo lê a âncora **BA 2019** do frontmatter das notas, cruzada com o resultado do CE. Serve como referência histórica — a âncora de 2019 não conhecia Fluência de Dados nem Contabilidade Avançada como blocos próprios.

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

`*` marca sub-prova composta — o valor soma os `pontos` de várias notas e infla quando elas se sobrepõem. As linhas sem `*` têm mapeamento exato.

## Ordem de ataque

Revisada em 2026-09-09 com as três provas.

| # | Bloco | Lógica |
| --- | --- | --- |
| 1 | **LTE — ICMS estadual, Lei Kandir, Simples Nacional** | Maior perda ponderada nas três provas: 60%, 40% e 40/64%. Nenhuma outra área repete isso |
| 2 | **Contabilidade Avançada** | 55% no CE, 50% no SP. O SP provou que Geral está em 100%: o buraco é inteiro na Avançada. Armadilhas numéricas da FCC — taxa contratual × efetiva, dividendo proposto, VJORA no resultado |
| 3 | **Custos — Ponto de Equilíbrio** | 20,1% da disciplina, 4/9 no caderno de 09/09. Anda junto com o item 2 no mesmo bloco de prova |
| 4 | **Direito Tributário** | ~60-73% nas três, e no SP a versão avançada foi a maior perda isolada da prova específica (20 pontos). Estável demais para melhorar sozinho |
| 5 | **Fluência de Dados / TI** | Volátil (40-84%) e obrigatória pela sua premissa. Volume alto multiplica erro: 14 pontos perdidos no MT mesmo com 84% |
| 6 | **Matemática Financeira** | 50% no MT, 67% no SP. O 83% do CE era composto e escondia isso |
| 7 | Direito Empresarial e Financeiro | Só entra porque o SP mostrou 44% quando o escopo os inclui. Se a BA seguir o CE, sai da lista |
| 8 | Economia | Metade fraca da dupla com Finanças Públicas. Confirmar a hipótese antes de investir |
| — | Auditoria, Contabilidade Geral, Português, Adm. Geral | Manutenção apenas. 80-100% de forma consistente |

## Aberto

- **O recorte das 5 questões de Economia e Finanças Públicas no MT.** Você ia conferir. Se eram de Economia, a hipótese acima fecha e o alvo passa a ser Economia.
- **A discursiva.** No CE não foi corrigida. Enquanto a objetiva não estabilizar bem acima do corte, o bloco de sábado (S5 em [[Slots (Grade Semanal)]]) compete por tempo com LTE.
- **A margem do SP.** Habilitado por 6 pontos em 340. Qualquer uma das fraquezas acima resolvida teria mudado a classificação de forma relevante.
