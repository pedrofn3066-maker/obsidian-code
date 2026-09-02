---
tipo: painel
---

# Evolução

## Por mês

```dataview
TABLE WITHOUT ID
  key AS "Mês",
  sum(rows.total) AS "Questões",
  round(100 * sum(rows.acertos) / sum(rows.total), 1) AS "%"
FROM "Questoes/Diario"
WHERE materia
GROUP BY dateformat(data, "yyyy-MM") AS key
SORT key DESC
```

## Por semana

```dataview
TABLE WITHOUT ID
  key AS "Semana",
  sum(rows.total) AS "Questões",
  round(100 * sum(rows.acertos) / sum(rows.total), 1) AS "%"
FROM "Questoes/Diario"
WHERE materia
GROUP BY dateformat(data, "kkkk-'W'WW") AS key
SORT key DESC
```

Se o rótulo da semana sair estranho na sua versão do Dataview, o problema está
nas aspas do token `'W'`. Troque por `dateformat(data, "yyyy-MM-dd")` de uma
segunda-feira ou me avise o que apareceu.
