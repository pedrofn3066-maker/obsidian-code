---
tipo: painel
---

# Hoje

<div class="botoes-painel"><a class="botao" href="obsidian://shell-commands/?vault=vault-ba&amp;execute=planodia01">📅 Plano do dia</a> <a class="botao" href="obsidian://shell-commands/?vault=vault-ba&amp;execute=s1ontem01">🧠 S1 - Revisão de ontem</a> <a class="botao" href="obsidian://shell-commands/?vault=vault-ba&amp;execute=fechasemana01">📊 Fechamento da semana</a></div>

```dataview
TABLE WITHOUT ID
  materia AS "Matéria", assuntos AS "Assuntos", slot AS "Slot",
  total AS "Q", acertos AS "Ac",
  round(100 * acertos / total, 1) AS "%", tec AS "Observação"
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
