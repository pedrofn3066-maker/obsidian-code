---
description: Importa um export .xlsx de Desempenho do TecConcursos e cria as notas de caderno do dia em Questoes/Diario
---

Transforme um export "Desempenho" do TecConcursos numa nota por matéria em `Questoes/Diario/`.

## Passo 0 — ler a planilha pelo script, nunca a olho

```
python3 PY/tec-caderno.py <caminho do .xlsx>
```

Ele devolve, por disciplina: total e percentual, a árvore de **tópicos-folha** com os erros marcados, o casamento sugerido de `materia`/`bloco` contra o vocabulário que o `Diario` já usa, e a conferência da soma. Não despeje as 40+ linhas da planilha no contexto — o script existe pra isso.

## Antes de escrever qualquer nota

1. **A data não está no arquivo.** O export não carrega data nenhuma. Se o Pedro não disser de que dia é, **pergunte** — não deduza pela data de modificação do arquivo nem pelo "hoje".
2. **Confira se já existe nota pra essa data + matéria.** `ls "Questoes/Diario/<data>"*` — se existir, pare e pergunte: pode ser reexport do mesmo caderno (duplicaria a contagem) ou uma segunda sessão do dia (aí é outro arquivo, com slot diferente).
3. **Volume.** O script avisa acima de 120 questões. O mesmo export do TEC serve como acumulado de período/vida inteira — um de 2054 linhas já foi usado neste vault pra derivar o `dom` dos checklists VINTEUM (commit `f29c76a`). Se vier acumulado e for tratado como "o dia", polui o `Diario` inteiro.

## Mapear disciplina → matéria

O vocabulário vem do próprio `Diario` (o script já cruza). Casamentos que não são óbvios e o script resolve:

| No export do TEC | No vault |
| --- | --- |
| Auditoria Privada | `Auditoria` |
| Legislação Tributária dos Estados e do Distrito Federal | `Legislação Tributária Estadual` |

Quando o script marcar `?? sem casamento confiável — PERGUNTAR`, use `AskUserQuestion` com as matérias plausíveis (`python3 PY/diretorio-materias.py` lista as 28). **Não invente uma matéria nova** sem confirmar — matéria nova no `Diario` que não existe em `MATERIAS/` fica órfã nos painéis.

**`bloco` é obrigatório.** Duas notas do vault (`2026-09-07 S5 TI - *`) estão com `bloco:` vazio e, por isso, não contam em `Ganho potencial` nem em `Agenda de releitura`, que agrupam por bloco. Se o script mostrar `(VAZIO no Diario — preencher)`, resolva o bloco antes de escrever.

## Formato da nota

Uma nota por matéria: `Questoes/Diario/<AAAA-MM-DD> <materia>.md`. Acrescente o slot ao nome (`<data> S3 <materia>.md`) **só se o Pedro informar** — slot é campo dele.

```yaml
---
tipo: caderno
data: 2026-09-08
materia: Auditoria
bloco: Auditoria
assuntos:
  - <um item por tópico-FOLHA da árvore>
slot:
total: 11
acertos: 9
tempo_min:
erro_tipo:
banca:
origem: TEC (importado)
tec:
obs: <análise curta — ver abaixo>
---

## Erros a revisar

- <tópico-folha com erro> — <acertos>/<total>. <o que revisar>
```

Regras que não são óbvias:

- **`assuntos` recebe só as folhas.** As linhas-pai da hierarquia (`01`, `01.01`) são agregados dos filhos; incluí-las inflaria a lista com o mesmo assunto em dois níveis. O script já separa.
- **Campos do Pedro ficam vazios:** `slot`, `erro_tipo`, `tempo_min`, `banca`, `tec`. Não preencha por inferência.
- **Caderno sem erro fica com `erro_tipo` vazio, obrigatoriamente.** O painel `Diagnóstico de erro` filtra por `WHERE materia AND erro_tipo` — preencher o campo num caderno 100% faz a matéria aparecer na coluna "Onde" como lacuna de conhecimento, sem nenhum erro pra contabilizar. Se o Pedro preencher mesmo assim, respeite a escolha dele mas avise uma vez.
- **`obs` é análise, não resumo do número.** O percentual já está em `total`/`acertos`. Use a `obs` pro que os números não mostram: onde o erro se concentra dentro da matéria, se a amostra é grande o bastante pra concluir algo (1-2 questões não é), e contraste de peso quando ele saltar aos olhos.

## Cruzamento que dá o valor real

Depois de criar as notas, faça a análise que os números sozinhos não dão:

1. **Erro × o que ele escreveu naquele dia.** Rode `sh PY/s1-ontem.sh -p` (ou `git log --since=<data> --until=<data+1> -p -- MATERIAS/`) e veja se os tópicos errados batem com o que ele anotou no mesmo dia. Em 2026-09-08 os dois erros de Auditoria eram exatamente os dois tópicos anotados naquela tarde — isso mudou a leitura do dia inteiro de "leitura solta" para "correção de erro".
2. **Erro sem anotação nenhuma.** Para cada tópico errado, procure com `python3 PY/achar-heading.py "MATERIAS/<nota>.md" "<trecho>"`. O erro que **não** virou nota em lugar nenhum é o mais perigoso do dia — foi assim que "Obrigações Alternativas" apareceu.
3. **Peso VINTEUM × desempenho.** `python3 PY/indice-materia.py "MATERIAS/<nota>.md"` mostra o percentual de cobrança e o `dom`. Diga qual tópico específico merece o próximo bloco de estudo — tópico errado **e** de peso alto vem primeiro; tópico de peso baixo com 1 questão de amostra não vira prioridade.
4. **Contraste de alocação.** Compare o volume de questões por matéria contra o peso dela. Em 2026-09-08, Auditoria (15 pontos) levou 11 questões e LTE (75 pontos, `crítico`) levou 1 — esse tipo de descompasso é o achado mais acionável do dia.

## Antes de reportar como feito

1. **Concilie o total.** A soma de `total`/`acertos` das notas criadas tem que bater com o `TOTAL A CONCILIAR` do script. Se não bater, alguma folha foi contada duas vezes ou ficou de fora.
2. Se o dia importado for anterior a hoje, o registro daquele dia no painel [[S1 - Revisão de ontem]] pode estar errado — ele pode ter concluído "dia sem questões" quando na verdade era "dia sem registro". Corrija o registro se existir.
3. Relate em tabela: matéria, acertos/total, %, erros e onde cada erro cai no peso VINTEUM.

Não commite sem o Pedro pedir.
