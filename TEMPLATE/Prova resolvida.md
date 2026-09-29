---
tipo: prova-antiga
banca:
ano:
orgao:
cargo:
questoes:
gabarito: oficial (tipo N) | não oficial (preliminar ou de terceiro) | ausente
fonte: caminho do PDF
absorvida: AAAA-MM-DD
---
> [!warning] Dois arquivos
> **Este template descreve dois arquivos.** A nota em `Questoes/Provas/` leva **só a seção "Resolução"** (as questões `### Q<n>`), sem frontmatter, título, Resumo, Mapa, Lacunas nem textos-base: uma nota grande com muitos links travou o Obsidian. Tudo o que vem antes de "## Resolução" abaixo vai para `.provas-mapa/<mesmo nome>.md` (pasta oculta do Obsidian, lida pelo `PY/provas-recorrencia.py`).

# <Banca> <Ano> - <Local> - <Cargo>

Duas ou três linhas: de onde veio o PDF, a situação do gabarito e o que muda na confiança do que está abaixo (gabarito preliminar, questão lida de imagem, questão anulada).

## Resumo

| Disciplina | Questões | Cobertas | Parciais | Lacunas | Resolução diverge do gabarito |
| --- | --- | --- | --- | --- | --- |
| … | … | … | … | … | … |

## Mapa

Uma linha por heading que a questão cobre (questão em dois headings = duas linhas). **A tabela é lida por posição pelo `PY/provas-recorrencia.py`: sete colunas, nesta ordem, com `Nota#Heading` em texto puro (sem `[[ ]]`: link ativo só na `## Resolução`).** Nenhuma outra tabela do arquivo pode começar a linha com `| <número> |` na margem.

| Q | Disciplina | Gab | Nota → heading | Regra cobrada | Ângulo | Cobertura |
| --- | --- | --- | --- | --- | --- | --- |
| 31 | Conhecimentos Específicos | A | P2 - Reforma Tributária#Split payment: procedimento simplificado e regras gerais (arts. 33 a 35) | sem identificar IBS/CBS implica opção pelo simplificado | troca de termo | coberto |

## Lacunas

- Q22 — princípios da Lei 14.133: a nota trata só de fases; candidata a `/absorver-pdf`.

## Resolução

Uma seção por questão da prova, **todas** (também as lacunas). O heading é só `### Q<n>` (sem zero à esquerda), porque os links `[[<prova>#Q31]]` das notas dependem dele. Abaixo dele, um callout recolhido no layout do `/tec-erros`: o externo guarda a questão; dentro, blocos coloridos irmãos separados por uma linha `>`. `Resposta` e `Na matéria` são obrigatórios; os demais só com conteúdo de verdade.

### Q31

> [!question]- Q31 · Conhecimentos Específicos · IBAM 2026 (Bragança Paulista, AFTM Jr.) — Split payment simplificado
> Enunciado limpo (sem número de página solto, sem quebra no meio de frase).
>
> (A) <mark style="background:#affad1">alternativa do gabarito</mark>
> (B) alternativa errada, com o trecho que a banca trocou em <span class="g-cond">solidários</span>
> (C) …
> (D) …
>
> **Gabarito:** 🟩 A (oficial) · **Minha resolução:** 🟩 A (concorda)
>
> > [!success] ✅ Resposta — A
> > Uma frase com o <mark style="background:#fff88f">núcleo da regra</mark> e o artigo em **negrito**. Depois, por que cada errada erra, uma por linha: **(B)** troca X por Y.
>
> > [!warning] ⚠️ Pegadinha da banca
> > O que a banca trocou e como costuma trocar. Só se der para dizer.
>
> > [!example]- 🧩 Quadro
> > | | Regra | Exceção |
> > | --- | --- | --- |
> > | … | … | … |
>
> > [!quote]- 📜 Texto literal — art. 33, § 2º-A, LC 214/2025
> > Lei seca do dispositivo: do cofre (`[!quote]-` da nota) ou de fonte oficial. Nunca de site ou doutrina.
>
> > [!warning] ⚠️ Gabarito × resolução
> > Só quando a resolução diverge: o que o gabarito manda, o que a fonte diz, e o que falta conferir (gabarito preliminar? tipo de caderno? redação da questão?).
>
> > [!info] 🔗 Na matéria
> > [[P2 - Reforma Tributária#Split payment: procedimento simplificado e regras gerais (arts. 33 a 35)]] — marcado (`[prova:: 1]`), trecho "§2º-A: originar a transação sem identificar…".
> > [[P2 - Reforma Tributária#Split payment (arts. 31 a 35)]] — vizinho: art. 32, consulta prévia (alternativa C).
> > **Fonte:** cofre `MATERIAS/P2 - Reforma Tributária.md:718` · internet <url> · resolução própria

## Regras do layout

- **Cores e grifos** são os do `/tirar-duvida` (seção "Layout"): gabarito em verde (`#affad1`), núcleo da regra em amarelo (`#fff88f`, uma vez por resposta), `g-prazo`/`g-cond`/`g-comp`/`g-num` nos dados que a banca troca. Não há alternativa "marcada" (o Pedro não fez esta prova); se ele a resolveu depois, acrescente `**Marquei:** 🟥 X`.
- **Um `Na matéria` por heading relacionado**: o principal (o que decide a resposta, o mesmo do Mapa) e os vizinhos que uma alternativa toca. Cada link é `[[Nota#Heading exato]]` confirmado com `PY/achar-heading.py`. Lacuna: `— lacuna` e diga o que falta.
- **Fonte** sempre presente, uma ou mais de: `cofre` (arquivo:linha), `internet` (URL oficial), `resolução própria` (Português, cálculo, raciocínio lógico). Fonte externa entra só aqui; nunca dentro de `MATERIAS/`.
- **Marcador de callout** é `[!tipo]` ou `[!tipo]-`, com o `-` colado ao `]`. Depois de gravar: `grep -n '\[!.*\]-\]' "<prova>.md"` tem que sair vazio.
- Questão lida de imagem ou com gabarito preliminar: diga no callout (`gab. preliminar`), não só no cabeçalho do arquivo.
