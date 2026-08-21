---
tipo: painel
cssclasses:
  - painel
---
****
# Painel — Auditor Fiscal · SEFAZ-BA

> [!warning] Duas hipóteses embutidas
> **Formato:** modelado no Edital SAEB/01/2019 (BA) cruzado com os editais FCC de SEFAZ-CE 2026 e
> SEFAZ-SP 2026. **Banca:** FCC é um chute — não há contratação. Ver [[ESTRATEGIA]], seção 1.


## 1. Projeção de pontos — âncora BA 2019

Só entram aqui as matérias com pontuação conhecida do edital de 2019. Total de referência: **285 pontos**
nas objetivas.

```dataviewjs
const pages = dv.pages('"MATERIAS"').where(p => Number(p.pontos ?? 0) > 0).sort(p => -Number(p.pontos));
let tot = 0, esp = 0; const rows = [];
for (const p of pages) {
  const ts = p.file.tasks.where(t => t.dom !== undefined);
  const n = ts.length;
  const dom = n ? ts.map(t => Number(t.dom)).array().reduce((a,c)=>a+c,0)/n : 0;
  const pts = Number(p.pontos);
  esp += pts*dom/5; tot += pts;
  rows.push([p.file.link, p.prova ?? "", pts, n, dom.toFixed(1)+"/5", (pts*dom/5).toFixed(1)]);
}
rows.push(["**TOTAL**", "", tot, "", "", "**"+esp.toFixed(0)+"**"]);
dv.table(["Matéria","Prova","Pontos","Tópicos","Domínio","Pontos esperados"], rows);
dv.paragraph(`Pisos de 2019: **60 na Prova I** (de 120) e **99 na Prova II** (de 165). Projeção: **${esp.toFixed(0)}** de ${tot}.`);
```

## 2. Cobertura preventiva — matérias sem pontuação conhecida

Disciplinas que a FCC cobra em CE ou SP e que **não existiam** no edital baiano de 2019. Entram com zero
para não distorcer a projeção, mas são exatamente onde mora a vantagem se aparecerem em 2026.

```dataviewjs
const pages = dv.pages('"MATERIAS"').where(p => Number(p.pontos ?? 0) === 0);
const rows = [];
for (const p of pages) {
  const ts = p.file.tasks.where(t => t.dom !== undefined);
  const n = ts.length;
  const dom = n ? ts.map(t => Number(t.dom)).array().reduce((a,c)=>a+c,0)/n : 0;
  rows.push([p.file.link, p.origem ?? "", n, dom.toFixed(1)+"/5"]);
}
dv.table(["Matéria","Onde é cobrada hoje","Tópicos","Domínio"], rows);
```

## 3. Buracos de peso 3

```dataview
TASK
FROM "MATERIAS"
WHERE peso = 3 AND dom != null AND dom <= 2
GROUP BY file.link
```

## 4. Revisão vencida

```dataview
TASK
FROM "MATERIAS"
WHERE rev != null AND rev <= date(today)
GROUP BY file.link
```

## 5. Desempenho em questões, por tema

```dataview
TABLE WITHOUT ID
  Tema,
  sum(rows.L.acertos) AS "Acertos",
  sum(rows.L.total) AS "Questões",
  round(100 * sum(rows.L.acertos) / sum(rows.L.total)) + "%" AS "Taxa"
FROM "DIARIO DE QUESTOES"
FLATTEN file.lists AS L
WHERE L.tema
GROUP BY L.tema AS Tema
SORT round(100 * sum(rows.L.acertos) / sum(rows.L.total)) ASC
```

## 6. Causa dominante dos erros

```dataview
TABLE WITHOUT ID Causa, length(rows) AS "Sessões"
FROM "DIARIO DE QUESTOES"
FLATTEN file.lists AS L
WHERE L.causa
GROUP BY L.causa AS Causa
SORT length(rows) DESC
```

> Se **leitura** e **atenção** dominarem, o problema é protocolo de prova, não conteúdo.

## 7. Cobertura geral

```dataviewjs
let f = 0, t = 0;
for (const p of dv.pages('"MATERIAS"')) { const ts = p.file.tasks; t += ts.length; f += ts.where(x=>x.completed).length; }
dv.paragraph(`**${f} / ${t}** tópicos fechados (${t ? Math.round(f/t*100) : 0}%).`);
```

---

[[ESTRATEGIA]] · [[LTE - COMO ESTUDAR]] · [[PROTOCOLO DE VIRADA DE EDITAL]] · [[DISCURSIVA]] · [[DIARIO DE QUESTOES]] · [[COMO USAR]] 