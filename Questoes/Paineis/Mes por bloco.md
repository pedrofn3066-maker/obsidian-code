---
tipo: painel
---

# Mês por bloco de pontuação

Agrupado pelos blocos do edital. Cruze o percentual com os pontos de cada bloco
(aba Pesos da planilha) para recalcular o ganho potencial sem depender de novo
export do TEC.

```dataview
TABLE WITHOUT ID
  key AS "Bloco",
  sum(rows.total) AS "Questões",
  sum(rows.acertos) AS "Acertos",
  round(100 * sum(rows.acertos) / sum(rows.total), 1) AS "%",
  sum(rows.total) - sum(rows.acertos) AS "Erros"
FROM "Questoes/Diario"
WHERE materia AND data >= date(today) - dur(30 days)
GROUP BY bloco
SORT sum(rows.total) - sum(rows.acertos) DESC
```
