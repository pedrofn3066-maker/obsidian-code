---
tipo: painel
---

# Mês por bloco de pontuação

Agrupado pelos blocos do edital. Cruze o percentual com os pontos de cada bloco
(aba Pesos da planilha) para recalcular o ganho potencial sem depender de novo
export do TEC.

```dataview
TABLE WITHOUT ID
  bloco AS "Bloco",
  sum(total) AS "Questões",
  sum(acertos) AS "Acertos",
  round(100 * sum(acertos) / sum(total), 1) AS "%"
FROM "Questoes/Diario"
WHERE materia AND data >= date(today) - dur(30 days)
GROUP BY bloco
SORT round(100 * sum(acertos) / sum(total), 1) ASC
```
