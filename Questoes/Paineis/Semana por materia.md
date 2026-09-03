---
tipo: painel
---

# Semana por matéria

Ordenado por erro absoluto, não por percentual: 68% em 500 questões custa mais
ponto do que 45% em 12. O topo desta tabela é a fila de reforço da semana seguinte.

```dataview
TABLE WITHOUT ID
  key AS "Matéria",
  sum(rows.total) AS "Questões",
  sum(rows.acertos) AS "Acertos",
  round(100 * sum(rows.acertos) / sum(rows.total), 1) AS "%",
  sum(rows.total) - sum(rows.acertos) AS "Erros"
FROM "Questoes/Diario"
WHERE materia AND data >= date(today) - dur(7 days)
GROUP BY materia
SORT sum(rows.total) - sum(rows.acertos) DESC
```

## Últimos 30 dias

```dataview
TABLE WITHOUT ID
  key AS "Matéria",
  sum(rows.total) AS "Questões",
  round(100 * sum(rows.acertos) / sum(rows.total), 1) AS "%",
  sum(rows.total) - sum(rows.acertos) AS "Erros"
FROM "Questoes/Diario"
WHERE materia AND data >= date(today) - dur(30 days)
GROUP BY materia
SORT sum(rows.total) - sum(rows.acertos) DESC
```
