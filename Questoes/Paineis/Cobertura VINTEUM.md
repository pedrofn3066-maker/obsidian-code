---
tipo: painel
---

# Cobertura VINTEUM

Cruza os dois trackers de `dom` que o vault carrega para cada tópico — e que **não medem a mesma coisa**:

- **`dom` do `Checklist por importância (VINTEUM)`** — calculado uma vez, em 2026-09-06, a partir do seu histórico real de desempenho no TecConcursos (export de 2054 linhas). É desempenho **em questões**, retroativo.
- **`dom` do heading no corpo da nota** — tracker manual, por tópico escrito. Antes de 2026-09-09 só 139 dos ~970 headings do vault tinham essa linha; o resto ganhou `dom:: 0` num passe único naquele dia, como valor neutro de partida — não como avaliação.

Os dois divergirem **não é bug**. Um tópico pode ter `dom:: 4` no checklist (você manda bem nas questões do TEC sobre ele) e não ter uma linha sequer escrita no corpo — porque o corpo mede se a *nota* foi estudada, não se o *assunto* foi.

O que este painel isola é o cruzamento que interessa: **tópicos com desempenho real conhecido (dom do checklist > 0) e nenhum conteúdo no corpo da nota.** É a lista "você já tem sinal sobre isso vindo de questões, mas o vault não tem nada escrito" — prioridade de transcrição, não de estudo.

```dataviewjs
const MATERIAS = "MATERIAS";
const PULAR = new Set(["MOC - Direito Tributário"]);
const STOP = new Set(["de","da","do","das","dos","e","a","o","as","os","em","com","ao","à","às","aos","para","por","na","no","nas","nos","sem","sobre","entre","num","numa"]);

function tokens(s) {
  s = s.toLowerCase().replace(/\(.*?\)/g, " ").replace(/[^a-zà-ú0-9 ]/g, " ");
  return new Set(s.split(/\s+/).filter(w => w.length > 2 && !STOP.has(w)));
}
function normaliza(s) { return s.replace(/\s+/g, " ").trim(); }

function parseChecklist(txt) {
  const linhas = txt.split("\n");
  const rows = [];
  const re = /^- \[.\]\s+(.+?)\s*\[dom::\s*(\d+)\]\s*\[peso::\s*([\d.]+)\]/;
  let dentro = false;
  for (const l of linhas) {
    if (/^## Checklist por importância/.test(l)) { dentro = true; continue; }
    if (dentro && /^#{1,6}\s/.test(l)) break;
    if (!dentro) continue;
    const m = l.match(re);
    if (m) rows.push([m[1], parseInt(m[2]), parseFloat(m[3])]);
  }
  return rows;
}

function parseBody(txt) {
  const linhas = txt.split("\n");
  let skipUntil = -1;
  for (let i = 0; i < linhas.length; i++) {
    if (/^## Checklist por importância/.test(linhas[i])) {
      skipUntil = i;
      for (let j = i + 1; j < linhas.length; j++) {
        if (/^#{1,6}\s/.test(linhas[j])) break;
        skipUntil = j;
      }
      break;
    }
  }
  const out = [];
  for (let i = 0; i < linhas.length; i++) {
    if (i <= skipUntil) continue;
    const hm = linhas[i].match(/^(#{1,6})\s+(.+)$/);
    if (!hm) continue;
    const titulo = normaliza(hm[2]);
    const prox = (linhas[i + 1] || "").trim();
    const dm = prox.match(/^- \[.\] status \[dom::\s*(\d+)\]/);
    const nivelAtual = hm[1].length;
    let j = i + (dm ? 2 : 1);
    let temConteudo = false;
    while (j < linhas.length) {
      const hm2 = linhas[j].match(/^(#{1,6})\s+(.+)$/);
      if (hm2 && hm2[1].length <= nivelAtual) break; // heading do mesmo nível ou mais raso: fim do escopo
      if (linhas[j].trim()) { temConteudo = true; break; } // linha real OU heading mais fundo (que também conta como conteúdo)
      j++;
    }
    out.push([titulo, dm ? parseInt(dm[1]) : null, temConteudo]);
  }
  return out;
}

function melhorMatch(topico, headings) {
  const tt = tokens(topico);
  if (tt.size === 0) return [null, 0];
  let melhor = null, score = 0;
  for (const [titulo, dom, temConteudo] of headings) {
    const ht = tokens(titulo);
    if (ht.size === 0) continue;
    let inter = 0;
    for (const w of tt) if (ht.has(w)) inter++;
    const uniao = new Set([...tt, ...ht]).size;
    const j = uniao ? inter / uniao : 0;
    const cobertura = inter / tt.size;
    const s = Math.max(j, cobertura * 0.8);
    if (s > score) { melhor = [titulo, dom, temConteudo]; score = s; }
  }
  return [melhor, score];
}

const linhas = [];
for (const page of dv.pages(`"${MATERIAS}" or "LTM ISS SANTOS"`)) {  // TEMP ISS Santos — voltar para `"${MATERIAS}"` depois da prova
  if (PULAR.has(page.file.name)) continue;
  const txt = await dv.io.load(page.file.path);
  const checklist = parseChecklist(txt);
  if (checklist.length === 0) continue;
  const body = parseBody(txt);
  for (const [topico, domChk, peso] of checklist) {
    if (domChk === 0) continue;
    const [match, score] = melhorMatch(topico, body);
    let gap = false;
    if (!match || score < 0.25) gap = true;
    else {
      const [, domBody, temConteudo] = match;
      if (!temConteudo && (domBody === null || domBody === 0)) gap = true;
    }
    if (gap) linhas.push([page.file.link, topico, domChk, peso]);
  }
}

linhas.sort((a, b) => b[3] - a[3]);

dv.header(3, `${linhas.length} lacunas encontradas`);
dv.table(
  ["Matéria", "Tópico (do checklist VINTEUM)", "dom TEC", "Peso VINTEUM"],
  linhas.map(r => [r[0], r[1], r[2], r[3].toFixed(1) + "%"])
);

const porMateria = {};
for (const [materia, , , peso] of linhas) {
  const k = materia.toString();
  porMateria[k] = porMateria[k] || { n: 0, peso: 0 };
  porMateria[k].n += 1;
  porMateria[k].peso += peso;
}
const resumo = Object.entries(porMateria)
  .map(([m, v]) => [m, v.n, v.peso])
  .sort((a, b) => b[2] - a[2]);

dv.header(3, "Resumo por matéria");
dv.table(
  ["Matéria", "Lacunas", "Peso VINTEUM somado"],
  resumo.map(r => [r[0], r[1], r[2].toFixed(1) + "%"])
);
```

## Como ler

- **A tabela não prova que o assunto falta no vault** — prova que este heurístico não achou um heading correspondente com conteúdo. Correspondência é por sobreposição de palavras entre o nome do tópico no checklist e os títulos dos headings do corpo; nomenclatura muito diferente entre a tabela VINTEUM e a nota (ex.: "Tributos" vs. "Espécies de Tributos") pode ou não casar. Confira a nota antes de tratar como lacuna real, principalmente em matérias com heading espalhado por sinônimos.
- **"Peso VINTEUM somado" no resumo não é peso da matéria** — é a soma dos pesos só dos tópicos que aparecem como lacuna. Uma matéria pequena com poucas lacunas de peso alto pode superar uma matéria grande com muitas lacunas de peso baixo.
- **Isso não é fila de estudo.** É fila de **transcrição** — mover o que você já sabe (ou já errou) no TEC para dentro da nota, pra que o corpo passe a refletir o que o checklist já mede. A fila de estudo de verdade continua sendo [[Ganho potencial]] e [[Fila de reforço]].

## Por que os dois `dom` divergem — e por que não sincronizar

Forçar os dois a bater destruiria informação: o `dom` do checklist é fato histórico (quantas questões você acertou), o `dom` do corpo é estado do seu processo de escrita (quanto da nota você já revisou). São perguntas diferentes. O objetivo deste painel não é igualar os dois — é achar onde o primeiro existe e o segundo nunca foi alimentado.
