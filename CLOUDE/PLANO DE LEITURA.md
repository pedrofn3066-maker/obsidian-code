---
tipo: painel
---

# Plano de Leitura — resumos TecConcursos

> [!info]- Como funciona
> Os tópicos vivem nas notas de `SEFAZ BA/MATERIAS/`. O script `revisoes.py leitura`
> grava `[ordem:: N]` e `[leitura:: AAAA-MM-DD]` em cada linha de tópico.
> Este painel só lê esses campos.
>
> Para regerar com outra data ou outro ritmo:
> `python3 revisoes.py leitura --vault . --inicio 2026-09-14 --por-dia 3 --apply`
>
> Ao terminar de ler um tópico, ajuste o `[dom:: N]` da linha. A coluna "Domínio"
> abaixo mostra o progresso.

---

## Hoje

```dataview
TABLE WITHOUT ID
  L.section AS "Tópico",
  L.dom AS "Domínio",
  L.ordem AS "#"
FROM "SEFAZ BA/MATERIAS"
FLATTEN file.lists AS L
WHERE L.leitura = date(today)
SORT L.ordem ASC
```

## Atrasado

Tópicos cuja data já passou e que continuam com domínio zero.

```dataview
TABLE WITHOUT ID
  L.section AS "Tópico",
  L.leitura AS "Era para",
  L.ordem AS "#"
FROM "SEFAZ BA/MATERIAS"
FLATTEN file.lists AS L
WHERE L.leitura < date(today) AND L.dom = 0
SORT L.leitura ASC
LIMIT 30
```

## Próximos

```dataview
TABLE WITHOUT ID
  L.section AS "Tópico",
  L.leitura AS "Data",
  L.ordem AS "#"
FROM "SEFAZ BA/MATERIAS"
FLATTEN file.lists AS L
WHERE L.leitura > date(today)
SORT L.ordem ASC
LIMIT 15
```

---

## Progresso por disciplina

```dataview
TABLE WITHOUT ID
  disciplina AS "Disciplina",
  prioridade AS "Prioridade",
  length(filter(file.lists, (x) => x.dom)) AS "Tópicos",
  length(filter(file.lists, (x) => x.dom > 0)) AS "Iniciados"
FROM "SEFAZ BA/MATERIAS"
WHERE disciplina
SORT prioridade ASC, disciplina ASC
```

---

## Disciplinas fora do plano

Estas notas têm frontmatter mas nenhuma linha de tópico, então não entram no
cronograma. Mapear os tópicos delas é o que falta para o plano ficar completo.

```dataview
LIST WITHOUT ID
  disciplina + " — " + prioridade + ", prova " + prova
FROM "SEFAZ BA/MATERIAS"
WHERE disciplina AND length(filter(file.lists, (x) => x.dom)) = 0
SORT prioridade ASC
```
