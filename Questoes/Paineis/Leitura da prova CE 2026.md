---
tipo: painel
---

# Leitura da prova — SEFAZ-CE 2026

Registro do resultado real da última prova prestada (FCC, Auditor-Fiscal SEFAZ-CE, resultado preliminar de 09/09/2026) e o que ele diz sobre a preparação para a Bahia.

**Nota objetiva 182,83 · mínimo 150 · classificação 1515º · não classificado para correção da discursiva.** A nota passou o mínimo com folga de 32,8 pontos. O que barrou foi a posição relativa, não a nota.

Este painel é **estático de propósito** na parte do resultado — a prova aconteceu, os números não mudam. Só a coluna de peso da Bahia é viva, lida do frontmatter das notas de `MATERIAS/`, para continuar correta quando o edital de 2027 sair e os pesos forem atualizados.

## Como a FCC calcula, e por que isso decide a estratégia

A banca não soma acertos. Converte em escore padronizado e multiplica pelo peso da prova:

```
NP = ((acertos − média_do_grupo) / DP_do_grupo) × 10 + 50
```

| Bloco | Acertos | Média do grupo | DP | Distância | NP | Peso | Pontos |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C. Gerais | 62/80 | 44,49 | 14,75 | +1,19 DP | 61,87 | 1 | 61,87 |
| C. Específicos | 54/80 | 38,19 | 15,08 | +1,05 DP | 60,48 | 2 | 120,96 |
| **Objetiva** | | | | | | | **182,83** |

<mark style="background:#fff88f">Um acerto em Conhecimentos Específicos vale 1,96× um acerto em Conhecimentos Gerais</mark> — 1,326 ponto contra 0,678. Não é nuance, é praticamente o dobro.

Em cenário concreto, medido sobre esta prova:

| Cenário | Ganho na nota |
| --- | --- |
| Acertar 9 questões a mais em Custos + LTE | +11,95 |
| Acertar **todas** as 18 que errou em Conhecimentos Gerais | +12,21 |

Nove questões nas duas matérias certas equivalem a uma prova perfeita de Gerais.

⚠️ A média do grupo em Específicos foi 38,19/80 (47,7%), contra 55,6% em Gerais. **O pelotão desiste justamente do bloco que vale dobrado** — é onde a diferenciação é mais barata.

## Onde os pontos foram embora

Perda ponderada = erros × valor marginal do bloco (0,678 em Gerais, 1,326 em Específicos).

| Disciplina | Resultado | Erros | Perda | % da perda |
| --- | --- | --- | --- | --- |
| **Contabilidade Avançada e de Custos** | 11/20 · 55% | 9 | −11,94 | 25,6% |
| **Legislação Tributária Estadual** | 12/20 · 60% | 8 | −10,61 | 22,7% |
| **Direito Tributário** | 14/20 · 70% | 6 | −7,96 | 17,0% |
| Língua Portuguesa | 6/10 · 60% | 4 | −2,71 | 5,8% |
| Economia | 6/10 · 60% | 4 | −2,71 | 5,8% |
| Fluência de Dados | 8/10 · 80% | 2 | −2,65 | 5,7% |
| Contabilidade Geral e Pública | 7/10 · 70% | 3 | −2,03 | 4,4% |
| Direito Financeiro | 6/8 · 75% | 2 | −1,36 | 2,9% |
| Mat. Fin./Estatística/RLM | 10/12 · 83% | 2 | −1,36 | 2,9% |
| Const./Admin./Civil/Penal | 10/12 · 83% | 2 | −1,36 | 2,9% |
| Finanças Públicas | 9/10 · 90% | 1 | −1,33 | 2,8% |
| Administração e Governança | 9/10 · 90% | 1 | −0,68 | 1,5% |
| Auditoria | 8/8 · 100% | 0 | 0 | 0% |
| | | **44** | **−46,69** | |

Três disciplinas concentram **65,3%** de tudo que foi perdido.

## Desempenho no CE × peso na Bahia

```dataviewjs
// Resultado do CE 2026: fato histórico, fixo. Peso da BA: lido ao vivo do frontmatter.
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
  const composta = notas.length > 1 ? "*" : "";
  const aviso = faltando.length ? ` ⚠️ nota não encontrada: ${faltando.join(", ")}` : "";
  return {
    nome, total, acertos,
    pct: Math.round((100 * acertos) / total),
    pontos, composta,
    prio: [...prios].sort().join(" / ") + aviso,
  };
});

linhas.sort((a, b) => b.pct - a.pct);

dv.table(
  ["Sub-prova do CE", "Resultado", "%", "Pontos na BA 2019", "Prioridade no vault"],
  linhas.map(r => [
    r.nome,
    `${r.acertos}/${r.total}`,
    r.pct + "%",
    r.pontos + r.composta,
    r.prio,
  ])
);

const semPeso = linhas.filter(r => r.pontos === 0 && r.pct >= 75);
dv.paragraph(`**${semPeso.length} das suas melhores matérias valem zero na âncora BA 2019:** ` +
  semPeso.map(r => `${r.nome} (${r.pct}%)`).join(" · "));
```

`*` marca sub-prova composta: o CE agrupa numa prova só o que o vault trata em várias notas, então o valor é a soma dos `pontos` delas. Some com cuidado — em Mat. Fin./Estatística/RLM as quatro notas provavelmente se sobrepõem na estrutura da BA 2019, e o total infla. As linhas sem `*` têm mapeamento exato e é nelas que o argumento se apoia.

## A leitura

**Seu desempenho está inversamente correlacionado com o peso na Bahia.** A matéria de maior peso isolado do edital baiano — LTE, 75 pontos, 22,8% da prova pela âncora de 2019 — é onde você teve o segundo pior resultado (60%). E quatro das suas cinco melhores valem zero naquela âncora.

Auditoria é o caso extremo: 8/8, teto absoluto, 15 pontos na Bahia. Não existe ganho de classificação disponível ali.

> [!warning]- Ressalva sobre a âncora
> O campo `pontos` das notas é a âncora **BA 2019**, e o edital BA 2027 não existe ainda. Contabilidade Avançada e de Custos aparece com zero porque em 2019 a Bahia consolidava contabilidade num bloco único; CE 2026 e SP 2026 separaram num bloco pesado. Tratar Custos como `crítico` é aposta na tendência recente da FCC, não fato confirmado.
>
> LTE é a exceção: é certeza. Todo edital de SEFAZ estadual carrega pesado, e a própria nota de LTE registra que é "o bloco que decide o concurso" e a única disciplina que nenhum material comercial cobre bem.

## Ordem de ataque

Derivada em 2026-09-09. Recalcular quando sair o edital BA 2027 ou quando houver caderno novo que mude o diagnóstico.

| # | Bloco | Lógica |
| --- | --- | --- |
| 1 | **LTE — ICMS estadual, Lei Kandir, Simples Nacional** | 75 pontos, 22,8% da prova, você em 60%. Maior retorno absoluto, sem concorrência preparada |
| 2 | **Custos — Ponto de Equilíbrio e Custo Padrão** | 20,1% da disciplina, 55% na prova real e 50% no caderno de 09/09. Fraqueza confirmada em dois pontos no tempo |
| 3 | **Contabilidade Avançada — catálogo de armadilhas FCC** | O erro é numérico, não conceitual: taxa contratual × efetiva, dividendo proposto na equivalência, VJORA no resultado |
| 4 | **Direito Tributário — fechar os 30% restantes** | 17,0% da perda, 30 pontos na BA, e já vem melhorando |
| 5 | Contabilidade Geral e Pública | 20 pontos na BA, 70% no CE. Ponte direta com o item 3 |
| 6 | Mat. Financeira e Estatística | Peso alto na BA, já em 83%. Manutenção barata |
| 7 | Língua Portuguesa | 20 pontos na BA, 60% no CE. Retorno pequeno, mas ganho fácil |
| 8 | Auditoria, Administração, Finanças Públicas, Fluência de Dados | Só manutenção — teto atingido e peso baixo ou zero na Bahia |

## Decisão de alocação em aberto

A discursiva não foi corrigida (classificação 1515º). Enquanto a objetiva não colocar você dentro do corte, o bloco de discursiva do sábado (S5 em [[Slots (Grade Semanal)]]) tem retorno condicional — só rende depois que a objetiva melhorar. Hoje ele compete por tempo com LTE, que é o gargalo real.
