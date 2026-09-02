# Cofre SEFAZ-BA (Obsidian)

Cofre de estudo para concurso fiscal. Notas em Markdown com campos inline do
Dataview. **Não é um projeto de software** — não há build, testes ou dependências.

## Regras que não devem ser quebradas

- **Nunca reescreva o conteúdo de estudo.** Texto de matéria, resumos, tabelas e
  anotações são autorais. Alterações se limitam a campos de controle
  (`dom`, `peso`, `cad`, `prox`) e tags.
- **Nunca edite** `SEFAZ BA/SEFAZ BA.md`, `SEFAZ BA/PAINEL.md`, `TAGs/TAGs.md`,
  `SEFAZ BA/COMO USAR.md` sem pedido explícito. São painéis e documentação da
  taxonomia; contêm nomes de tags dentro de consultas Dataview e quebram fácil.
- **Nunca toque em** `.obsidian/`, `.smart-env/`, `.trash/`.
- Antes de qualquer edição em lote, rode em modo simulação e mostre o resultado.
- Tags dentro de crases (`` `#tec/erro` ``) ou aspas retas (`"#tec/erro"`) são
  exemplos em template, não marcações. Ignore-as.

## Estrutura

```
SEFAZ BA/
  SEFAZ BA.md          painel de gavetas por tag
  PAINEL.md            painel de projeção de pontos
  COMO USAR.md         instruções de uso
  MATERIAS/            27 notas, uma por disciplina
MATERIAL/              notas de erro por disciplina (ERRO *.md)
TAGs/TAGs.md           taxonomia documentada
```

## Formato das notas de disciplina

Frontmatter:

```yaml
---
disciplina: Direito Financeiro
prova: I                    # I ou II
peso: 2
pontos: 0
origem: "CE 2026"
prioridade: importante      # crítico | importante | complementar
---
```

Tópicos:

```markdown
### Nome do tópico
- [ ] status [dom:: 0] [peso:: 2]
```

`dom` vai de 0 (nunca estudado) a 5 (domínio total). 12 das 27 notas ainda não
têm checklist de tópicos.

## Tags

Só três naturezas importam:

| Natureza | Tags | Dirige agendamento |
|---|---|---|
| Estado | `#revisar`, `#revisar/Nd`, `#dominio/baixo`, `#status/*`, `#acao/*` | sim |
| Procedência | `#tec/resumo` (link para aula do TecConcursos) | não |
| Classificação | `#banca/*`, `#pegadinha`, `#jurisprudencia`, `#excecao` | não |

`#banca/cebraspe`, `#banca/fcc`, `#banca/fgv` e `#banca/outras` são **cabeçalhos
fixos** de todas as notas `ERRO *.md`. Aparecem 18 vezes cada porque toda nota tem
as quatro seções, marcadas ou não. Não são sinal de nada.

## Motor de revisão

`revisoes.py` na raiz do cofre. Três comandos:

```bash
python3 revisoes.py agendar   --vault .          # simula
python3 revisoes.py agendar   --vault . --apply  # grava
python3 revisoes.py escalonar --vault . [--apply] [--limite N]
python3 revisoes.py cobertura --vault .          # somente leitura
```

- `agendar` lê tags de estado e escreve `[cad:: Nd] [prox:: AAAA-MM-DD]` no fim
  da linha. Idempotente: se a cadência não mudou, `prox` não é tocado.
- `escalonar` rebaixa um degrau da escada (3d → 7d → 15d → 30d) quando `prox`
  está atrasado além do limite, e torna a cadência explícita na tag.
- `cobertura` relata tópicos com `dom 0` agrupados por disciplina e prioridade.

Ciclo: revisou, promove a tag (`/3d` → `/7d` → `/15d` → `/30d`); errou muito,
rebaixa. Rodar `agendar` ajusta as datas.

## Pendências conhecidas

- `MATERIAL/ERRO DIREITO ADMINISTRATIVO.md` linha 26 usa aspas retas
  (`"#tec/erro"`) onde as outras 17 notas usam crases. Padronizar para crases.
- Três linhas marcadas com tag não são itens de lista, e as consultas do painel
  usam `FLATTEN file.lists`, que só enxerga itens de lista. Acrescentar `- `.
- Tags órfãs, provavelmente resíduo de colagem: `#page`, `#search`, `#tag-name`,
  `#questão`, `#definicao`, `#flashcard`, `#Crédito`.
- `#estrategia/*` e `#tipo/*` estão documentadas em `TAGs.md` mas têm zero uso.
