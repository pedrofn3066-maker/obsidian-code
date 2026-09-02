---
tipo: painel
---

# Dia consolidado

Recupera a visão de dia inteiro que a nota única dava, sem depender dela — soma
os cadernos que caem na mesma data.

```dataview
TABLE WITHOUT ID
  data AS "Data",
  sum(rows.total) AS "Q",
  sum(rows.acertos) AS "Ac",
  round(100 * sum(rows.acertos) / sum(rows.total), 1) AS "%",
  length(rows) AS "Cadernos",
  join(rows.materia, " · ") AS "Matérias"
FROM "Questoes/Diario"
WHERE materia AND data >= date(today) - dur(14 days)
GROUP BY data
SORT data DESC
```
