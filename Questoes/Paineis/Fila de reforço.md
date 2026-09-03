Aplica automaticamente os critérios de saída do protocolo de revisão: abaixo de 60% o tópico volta para leitura; entre 60% e 70%, nova bateria em uma semana.

```dataview
TABLE WITHOUT ID
  data AS "Data", materia AS "Matéria", assuntos AS "Assuntos",
  round(100 * acertos / total, 1) AS "%",
  choice(acertos / total < 0.6, "Releitura",
    choice(acertos / total < 0.7, "Refazer em 7d", "Revisão normal")) AS "Ação"
FROM "Questoes/Diario"
WHERE materia AND total > 0 AND acertos / total < 0.7 AND data >= date(today) - dur(30 days)
SORT acertos / total ASC
```

> [!note]- Sobre o `total > 0`
> Acrescentado ao filtro original para evitar divisão por zero num caderno registrado sem questões — caso raro, mas que quebra a consulta inteira quando acontece.
