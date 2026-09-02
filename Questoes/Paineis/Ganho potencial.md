---
tipo: painel
---

# Ganho potencial

Cruza a lacuna (100% − % de acerto) com o peso do bloco no edital. O topo da
tabela é onde a próxima semana de estudo rende mais ponto — não onde você
errou mais nem onde se sente pior.

Requer **Enable JavaScript Queries** ligado nas configurações do Dataview
(já está ligado neste cofre).

```dataviewjs
const PONTOS = {
  "Cont. Avançada e de Custos": 40, "Direito Tributário": 40,
  "Legislação Tributária": 40, "Finanças Públicas": 20,
  "Fluência de Dados": 20, "Mat. Fin./Estat./RLM": 12,
  "Const./Adm./Civil/Penal": 12, "Língua Portuguesa": 10,
  "Adm. e Governança": 10, "Economia": 10,
  "Cont. Geral e Pública": 10, "Direito Financeiro": 8, "Auditoria": 8
};
const META = 0.85, DIAS = 30;
const corte = dv.date("today").minus({ days: DIAS });
const agg = {};
for (const p of dv.pages('"Questoes/Diario"')) {
  if (!p.materia || !p.total || !p.data || p.data < corte) continue;
  const b = String(p.bloco);
  agg[b] ??= { t: 0, a: 0 };
  agg[b].t += Number(p.total);
  agg[b].a += Number(p.acertos);
}
const rows = Object.entries(agg).map(([b, v]) => {
  const pct = v.a / v.t, pts = PONTOS[b] ?? 0;
  return [b, pts, v.t, (pct * 100).toFixed(1) + "%",
          (pts * Math.max(0, META - pct)).toFixed(1)];
}).sort((x, y) => Number(y[4]) - Number(x[4]));
dv.table(["Bloco", "Pontos", "Questões", "% acerto", "Ganho potencial"], rows);
```
