> [!warning] Só questões
> A nota em `Questoes/Provas/` leva **apenas** as seções `### Q<n>` abaixo, uma por questão, na ordem do caderno. Sem frontmatter, título, resumo, mapa, lacunas, textos-base nem arquivo auxiliar: uma nota grande com muitos links travou o Obsidian. A recorrência por heading vem daqui mesmo (`PY/provas-recorrencia.py` lê o gabarito e os rótulos do bloco "Na matéria").

Uma seção por questão da prova, **todas** (também as lacunas e as anuladas). O heading é só `### Q<n>` (sem zero à esquerda), porque os links `[[<prova>#Q31]]` das notas dependem dele. Abaixo dele, um callout recolhido no layout do `/tec-erros`: o externo guarda a questão; dentro, blocos coloridos irmãos separados por uma linha `>`. `Resposta` e `Na matéria` são obrigatórios; os demais só com conteúdo de verdade.

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
> > Só quando a resolução diverge: o que o gabarito manda, o que a fonte diz e o que falta conferir (gabarito preliminar? tipo de caderno? redação da questão?).
>
> > [!info] 🔗 Na matéria
> > [[P2 - Reforma Tributária#Split payment: procedimento simplificado e regras gerais (arts. 33 a 35)]] — marcado (callout `Prova anterior`)
> > [[P2 - Reforma Tributária#Split payment (arts. 31 a 35)]] — vizinho · art. 32, consulta prévia (alternativa C)
> > — lacuna: só quando a nota não trata (diga o que falta)
> > **Fonte:** cofre `MATERIAS/P2 - Reforma Tributária.md:718` · internet <url> · resolução própria

## Regras do layout

- **Gabarito** numa linha fixa, que o script lê: `**Gabarito:** 🟩 D (oficial)`, `🟩 D (preliminar)`, `🟩 D (oficial, definitivo; alterado após recurso)` ou `⬛ ANULADA (oficial, definitivo)`. O texto entre parênteses diz a situação; para anulada, nenhuma alternativa fica em verde.
- **Rótulos do bloco "Na matéria"** (o script conta só o que começa por `> > [[Nota#Heading]] — `): `marcado (callout `Prova anterior`)` = heading decisivo, vai receber marca; `mapeado (questão anulada, sem marca)`; `aviso `Gabarito × nota``; `vizinho` = só uma alternativa toca, não conta.
- **Cores e grifos** são os do `/tirar-duvida` (seção "Layout"): gabarito em verde (`#affad1`), núcleo da regra em amarelo (`#fff88f`, uma vez por resposta), `g-prazo`/`g-cond`/`g-comp`/`g-num` nos dados que a banca troca. Não há alternativa "marcada" (o Pedro não fez esta prova); se ele a resolveu depois, acrescente `**Marquei:** 🟥 X`.
- **Um link por heading relacionado**: o principal (o que decide a resposta) e os vizinhos. Cada link é `[[Nota#Heading exato]]` confirmado com `PY/achar-heading.py`. Lacuna: `— lacuna` e diga o que falta.
- **Fonte** sempre presente, uma ou mais de: `cofre` (arquivo:linha), `internet` (URL oficial) ou `resolução própria` (Português, cálculo, lógica). Fonte externa entra só aqui; nunca dentro de `MATERIAS/`.
- **Marcador de callout** é `[!tipo]` ou `[!tipo]-`, com o `-` colado ao `]`. Depois de gravar: `grep -n '\[!.*\]-\]' "<prova>.md"` tem que sair vazio.
- **Nada solto entre os callouts**: título de disciplina do PDF, linha em branco com espaço ou texto sem `>` dentro do bloco de uma questão quebra o callout.
- Questão lida de imagem ou com gabarito preliminar: diga no callout (`gab. preliminar`), não só na linha `Gabarito`.
