Cruza o acerto dos últimos 30 dias com os pontos de cada bloco no edital e devolve quanto ponto cada bloco ainda tem a oferecer até a meta de 85%.

O topo da tabela é onde a próxima semana de estudo rende mais ponto — não onde houve mais erro, nem onde a sensação é pior.

Requer **Enable JavaScript Queries** ativado nas configurações do Dataview.

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
const corte = dv.luxon.DateTime.now().minus({ days: DIAS });

const agg = {};
for (const p of dv.pages('"Questoes/Diario"')) {
  if (!p.materia || !p.total || !p.data) continue;
  const d = dv.date(p.data);
  if (!d || d < corte) continue;
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

> [!warning]- Este código não foi executado contra um cofre real
> Dois pontos de atenção, ambos na comparação de datas. O corte usa `dv.luxon.DateTime.now()` em vez de `dv.date("today")`, porque não há garantia de que a string `"today"` seja interpretada pelo parser em todas as versões. E cada `p.data` passa por `dv.date()` antes da comparação, cobrindo o caso de a propriedade estar armazenada como texto.
>
> Se a tabela vier vazia, testar isoladamente `dv.span(dv.pages('"Questoes/Diario"').length)` numa nota nova para confirmar que o caminho da pasta está correto.
>
> Se um bloco aparecer com 0 em "Pontos", a grafia de `bloco` na nota diverge da chave no dicionário `PONTOS`. Conferir contra a aba **Pesos** do `Cronograma_SEFAZ_BA_2027.xlsx`.
