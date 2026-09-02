---
tipo: painel
---

# Por slot e por tipo de erro

Se o acerto cair no S5, o problema é fadiga e não conteúdo — a solução é trocar
a ordem dos slots, não estudar mais.

```dataview
TABLE WITHOUT ID
  slot AS "Slot",
  sum(total) AS "Questões",
  round(100 * sum(acertos) / sum(total), 1) AS "%"
FROM "Questoes/Diario"
WHERE materia AND data >= date(today) - dur(30 days)
GROUP BY slot
SORT slot ASC
```

## Assunto específico

Troque o termo entre aspas pelo assunto que quiser investigar.

```dataview
TABLE WITHOUT ID
  data AS "Data", materia AS "Matéria", assuntos AS "Assuntos",
  total AS "Q", round(100 * acertos / total, 1) AS "%"
FROM "Questoes/Diario"
WHERE materia AND contains(assuntos, "MEP")
SORT data DESC
```
