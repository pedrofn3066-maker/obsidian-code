---
tipo: painel
---

# Diagnóstico de erro

Separa falha de conteúdo (desconhecimento) de falha de leitura (desatenção,
exceção) — o remédio é diferente para cada uma. Só funciona nos cadernos em
que `erro_tipo` foi preenchido.

```dataview
TABLE WITHOUT ID
  key AS "Tipo de erro",
  length(rows) AS "Cadernos",
  sum(rows.total) - sum(rows.acertos) AS "Questões erradas",
  join(rows.materia, " · ") AS "Onde"
FROM "Questoes/Diario"
WHERE materia AND erro_tipo
GROUP BY erro_tipo
SORT sum(rows.total) - sum(rows.acertos) DESC
```
