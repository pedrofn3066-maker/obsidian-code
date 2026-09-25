Ordena os resumos pelo ganho potencial do bloco a que pertencem. Responde à pergunta "o que eu releio primeiro" cruzando onde você erra com quanto vale.

Serve para os dois momentos: queda de percentual num bloco, e revisão de véspera.

Requer que cada resumo tenha `bloco` no frontmatter, com a mesma grafia usada nos cadernos.

```dataviewjs
// ===== AJUSTAR ESTES DOIS CAMINHOS =====
const RESUMOS = "MATERIAS";             // pasta onde ficam os resumos
const DIARIO  = "Questoes/Diario";      // pasta dos cadernos
// =======================================

const PONTOS = {
  "Cont. Avançada e de Custos": 40, "Direito Tributário": 40,
  "Legislação Tributária": 40, "Finanças Públicas": 20,
  "Fluência de Dados": 20, "Mat. Fin./Estat./RLM": 12,
  "Const./Adm./Civil/Penal": 12, "Língua Portuguesa": 10,
  "Adm. e Governança": 10, "Economia": 10,
  "Cont. Geral e Pública": 10, "Direito Financeiro": 8, "Auditoria": 8,
  // TEMP ISS Santos — remover esta linha depois da prova
  "Legislação Tributária Municipal de Santos, PAF e Dívida Ativa": 16
};

const META = 0.85;
const DIAS = 30;   // para revisão de véspera, aumentar para 9999

const corte = dv.luxon.DateTime.now().minus({ days: DIAS });

// 1. Desempenho por bloco, a partir dos cadernos
const agg = {};
for (const p of dv.pages(`"${DIARIO}"`)) {
  if (!p.materia || !p.total || !p.data) continue;
  const d = dv.date(p.data);
  if (!d || d < corte) continue;
  const b = String(p.bloco);
  agg[b] ??= { t: 0, a: 0 };
  agg[b].t += Number(p.total);
  agg[b].a += Number(p.acertos);
}

// 2. Ganho potencial de cada bloco
const ganho = {};
for (const [b, v] of Object.entries(agg)) {
  const pct = v.a / v.t;
  ganho[b] = { g: (PONTOS[b] ?? 0) * Math.max(0, META - pct), pct: pct };
}

// 3. Resumos, ordenados pelo ganho do seu bloco
const rows = [];
for (const p of dv.pages(`"${RESUMOS}" or "LTM ISS SANTOS"`)) {  // TEMP ISS Santos — voltar para `"${RESUMOS}"` depois da prova
  if (!p.bloco) continue;
  const b = String(p.bloco);
  const info = ganho[b];
  rows.push([
    p.file.link,
    b,
    info ? info.g.toFixed(1) : "—",
    info ? (info.pct * 100).toFixed(1) + "%" : "sem dados",
    p.file.mtime.toFormat("yyyy-MM-dd"),
    info ? info.g : -1
  ]);
}

rows.sort((x, y) => y[5] - x[5]);
const saida = rows.map(r => r.slice(0, 5));

dv.table(
  ["Resumo", "Bloco", "Ganho do bloco", "% acerto", "Modificado"],
  saida
);
```

> [!warning]- Não testado contra cofre real
> Ajuste `RESUMOS` e `DIARIO` antes do primeiro uso. Se a tabela vier vazia, o motivo mais provável é caminho de pasta errado — teste com `dv.span(dv.pages('"Resumos"').length)` numa nota nova.
>
> Resumo que aparece com "sem dados" na coluna de percentual pertence a um bloco sem caderno resolvido na janela. Não é erro: é bloco que você não treinou.
>
> Resumo que não aparece de jeito nenhum está sem a propriedade `bloco`, ou com a grafia divergente da usada nos cadernos.

> [!tip]- Modo véspera
> Trocar `DIAS = 30` por `DIAS = 9999` faz a ordenação usar todo o histórico em vez da janela recente. Para revisão de véspera é o que você quer — o desempenho do semestre inteiro, não o das últimas quatro semanas.
