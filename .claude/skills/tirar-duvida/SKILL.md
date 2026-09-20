---
name: tirar-duvida
description: Tira dúvidas sobre matérias e tópicos de estudo (Direito Tributário, Reforma Tributária, Auditoria, Contabilidade, Direito Administrativo etc.) buscando a explicação primeiro no cofre (MATERIAS, wiki, Erradas, Questoes) e, só se o cofre não cobrir, pesquisando na internet em fonte oficial. Use quando o Pedro perguntar "o que é X", "explica Y", "qual a diferença entre A e B", "como a banca cobra Z", "tira uma dúvida".
---

# Tirar dúvida (cofre primeiro, internet depois)

Paths relativos à raiz do cofre (`vault-ba/`). Responde a dúvida de estudo. **Não edita o cofre por conta própria** — só lê. A única escrita permitida é guardar a dúvida em `Questoes/Duvidas.md` quando o Pedro pedir (ver "Guardar a dúvida").

## Passo 1 — buscar no cofre

Ordem de busca (pare quando tiver base suficiente, mas confira 2 fontes se for tema cobrado por literalidade):

1. **Descobrir a matéria:** `python3 PY/diretorio-materias.py <palavra>` lista as notas de `MATERIAS/` com bloco/peso/prioridade.
2. **Achar o tópico em headings:** `python3 PY/achar-heading.py "MATERIAS/<nota>.md" "<trecho>"` devolve a linha exata (tolera NBSP escondido). Para ver a árvore da nota: `python3 PY/indice-materia.py "MATERIAS/<nota>.md"`.
3. **Busca no corpo (todas as notas):**
   ```bash
   grep -rniE --include='*.md' 'sujeito.{1,2}passivo' MATERIAS wiki Erradas Questoes | cut -c1-160
   ```
   - Sempre com aspas em `--include='*.md'` (zsh quebra sem aspas).
   - Use `.{1,2}` entre palavras em vez de espaço: o cofre tem `\xa0` (NBSP) que casa com `.` mas não com espaço comum.
   - Tente também sem acento/termos vizinhos (ex.: `ICMS` e `substitui.{1,3}o tribut`).
4. **Ler o trecho:** `Read` com `offset`/`limit` na linha achada (~40 linhas). Nunca leia a nota inteira — têm 100 a 1400+ linhas.
5. **Onde o Pedro erra:** `Erradas/ERRO <MATÉRIA>.md` e `Questoes/Diario/` mostram questões erradas e assuntos testados; cite se ajudar ("você errou isso em 14/09").
6. **Pontos de atenção/súmulas:** `wiki/concepts/` (súmulas vinculantes, pontos de atenção da Reforma Tributária).
7. **Material bruto (PDF de lei/aula):** `MATERIAL/` — só cite o caminho; extrair PDF é trabalho do `/absorver-pdf`.

## Passo 2 — decidir se o cofre basta

- **Basta:** achou o tópico com explicação/literal suficiente para responder → responda só com isso.
- **Parcial:** achou o assunto, mas falta um ponto (prazo, exceção, jurisprudência, artigo) → responda com o que tem e complete com a internet, separando claramente as duas origens.
- **Não tem:** nenhum resultado relevante → vá direto para a internet e avise "não encontrei no cofre".

## Passo 3 — internet (fallback)

`WebSearch` e `WebFetch` são ferramentas deferidas: carregue antes com `ToolSearch` (`select:WebSearch,WebFetch`).

- Priorize fonte oficial: planalto.gov.br (leis, CTN, LCs), stf.jus.br / stj.jus.br (jurisprudência, súmulas), sefaz.ba.gov.br e legislação estadual, gov.br/fazenda, cgibs/Receita para IBS/CBS, portais dos tribunais. Doutrina e cursinhos só como apoio.
- Confira data/vigência: hoje a legislação de Reforma Tributária (EC 132/2023, LC 214/2025, LC 227/2026) muda com frequência.
- Não copie trecho longo de site; resuma e cite a URL. Lei seca (texto de norma) pode ser citada literalmente.

## Formato da resposta

Direta e de estudo, em português, do jeito que cai na prova (banca FCC/fiscal):

1. **Resposta curta** (1–3 linhas).
2. **Explicação** com o essencial: regra, exceção, prazo/percentual/número, artigo.
3. **Como a banca cobra** (pegadinha comum), se souber pelo cofre ou pela prova.
4. **Fontes**, separadas:
   - `Cofre:` `[[nota]]` com linha (ex.: `MATERIAS/P2 - Direito Tributário.md:731`) — use link de arquivo.
   - `Internet:` URL + o que foi tirado dela. Se nada veio da internet, omita.
5. Se o cofre estiver **desatualizado ou contradizer** a fonte oficial, diga explicitamente — não corrija o cofre sozinho; ofereça guardar a dúvida em `Questoes/Duvidas.md`.

## Guardar a dúvida

Só quando o Pedro pedir ("guarda essa dúvida", "anota isso"). Nunca por conta própria. Acrescente ao final de `Questoes/Duvidas.md` (abaixo de `## Dúvidas`, sem reescrever o resto), uma linha por dúvida:

```
- 20 de set. de 2026, 15:41 — [Direito Tributário] pergunta → resposta curta (fonte: cofre MATERIAS/P2 - Direito Tributário.md:731 / internet <url>)
```

Não use `Capturas.md`: o `/triar-inbox` distribui tudo que está lá. Dúvida sem resposta confirmada também pode ser guardada, marcada com `(sem fonte confirmada)`.

## Regras

- Nunca afirme que "está no cofre" sem ter lido o trecho. Nunca invente artigo, número de súmula ou percentual: se não achou, diga que não achou.
- Dúvida ambígua (ex.: "ICMS" existe em Tributário e em Legislação Estadual BA): responda pela matéria mais provável e mencione a outra em uma linha, sem interrogatório.
- Pedido de *editar* nota, absorver PDF ou triar capturas não é desta skill → `/absorver-pdf`, `/triar-inbox`.
