Visão consolidada do dia inteiro, somando todos os cadernos resolvidos em cada data dos últimos 14 dias. Serve para conferir, ao fechar o dia, se todos os cadernos foram registrados.

```dataview
TABLE WITHOUT ID
  key AS "Data",
  sum(rows.total) AS "Q",
  sum(rows.acertos) AS "Ac",
  round(100 * sum(rows.acertos) / sum(rows.total), 1) AS "%",
  length(rows) AS "Cadernos",
  join(rows.materia, " · ") AS "Matérias"
FROM "Questoes/Diario"
WHERE materia AND data >= date(today) - dur(14 days)
GROUP BY data
SORT key DESC
```

> [!note]- Se a coluna Data vier vazia
> Depois de `GROUP BY data`, o campo agrupador passa a se chamar `key` — `data` deixa de existir como campo simples. Por isso a primeira coluna e o `SORT` usam `key`. Se ainda assim vier vazio, confirmar que a propriedade `data` nas notas de `Diario` está tipada como data, e não como texto.
