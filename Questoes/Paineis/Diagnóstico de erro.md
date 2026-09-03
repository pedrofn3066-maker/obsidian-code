Separa falha de conteúdo de falha de leitura de enunciado. Se a maior parte dos erros for do tipo `excecao`, o problema não é falta de conteúdo — é a armadilha plantada entre as alternativas, e o remédio muda completamente.

Só produz resultado depois que a propriedade `erro_tipo` estiver em uso nos cadernos.

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

Valores permitidos em `erro_tipo`: `desconhecimento` · `desatencao` · `excecao`.
