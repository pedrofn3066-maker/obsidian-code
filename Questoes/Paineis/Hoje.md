---
tipo: painel
---

# Hoje

```dataview
TABLE WITHOUT ID
  materia AS "Matéria", assuntos AS "Assuntos", slot AS "Slot",
  total AS "Q", acertos AS "Ac",
  round(100 * acertos / total, 1) AS "%", obs AS "Observação"
FROM "Questoes/Diario"
WHERE materia AND data = date(today)
SORT slot ASC
```

## Total do dia

```dataview
TABLE WITHOUT ID
  sum(rows.total) AS "Questões",
  sum(rows.acertos) AS "Acertos",
  round(100 * sum(rows.acertos) / sum(rows.total), 1) AS "% acerto"
FROM "Questoes/Diario"
WHERE materia AND data = date(today)
GROUP BY true
```
