Diz **quando** reler cada resumo e **em que ordem**.

O intervalo vem do seu desempenho no bloco: quanto pior o acerto, mais cedo o material volta. A ordenação vem do ganho potencial: entre dois resumos igualmente vencidos, primeiro o que vale mais ponto.

Requer duas propriedades nos resumos:

```yaml
---
bloco: Legislação Tributária
revisado: 2026-08-20
---
```

`revisado` é a data da última releitura de verdade. Não atualize por correção de vírgula — o campo existe para medir esquecimento, não edição.

```dataviewjs
// ===== AJUSTAR =====
const RESUMOS = "MATERIAS";
const DIARIO  = "Questoes/Diario";
// ===================

const PONTOS = {
  "Cont. Avançada e de Custos": 40, "Direito Tributário": 40,
  "Legislação Tributária": 40, "Finanças Públicas": 20,
  "Fluência de Dados": 20, "Mat. Fin./Estat./RLM": 12,
  "Const./Adm./Civil/Penal": 12, "Língua Portuguesa": 10,
  "Adm. e Governança": 10, "Economia": 10,
  "Cont. Geral e Pública": 10, "Direito Financeiro": 8, "Auditoria": 8
};

// Escada de intervalo, em dias, por faixa de acerto
function intervalo(pct) {
  if (pct === null)   return 7;    // sem dados: revisita curta para gerar dado
  if (pct < 0.50)     return 2;
  if (pct < 0.65)     return 5;
  if (pct < 0.75)     return 10;
  if (pct < 0.85)     return 21;
  return 45;
}

const META = 0.85;
const DIAS = 30;
const hoje = dv.luxon.DateTime.now();
const corte = hoje.minus({ days: DIAS });

// 1. Desempenho por bloco
const agg = {};
for (const p of dv.pages(`"${DIARIO}"`)) {
  if (!p.materia || !p.total || !p.data) continue;
  const d = dv.date(p.data);
  if (!d || d < corte) continue;
  const b = String(p.bloco);
  agg[b] ??= { t: 0, a: 0 };
  agg[b].t += Number(p.total);
  agg[b].a += Number(p.acertos);
}

const info = {};
for (const [b, v] of Object.entries(agg)) {
  const pct = v.a / v.t;
  info[b] = { pct: pct, ganho: (PONTOS[b] ?? 0) * Math.max(0, META - pct) };
}

// 2. Agenda de releitura
const rows = [];
for (const p of dv.pages(`"${RESUMOS}"`)) {
  if (!p.bloco) continue;
  const b = String(p.bloco);
  const i = info[b] ?? { pct: null, ganho: 0 };
  const dias = intervalo(i.pct);

  const ultima = p.revisado ? dv.date(p.revisado) : null;
  const vence = ultima ? ultima.plus({ days: dias }) : null;
  const atraso = vence ? Math.floor(hoje.diff(vence, "days").days) : 9999;

  let situacao;
  if (!ultima)          situacao = "Nunca revisado";
  else if (atraso > 0)  situacao = `Vencido há ${atraso}d`;
  else if (atraso > -3) situacao = "Vence em breve";
  else                  situacao = "Em dia";

  rows.push([
    p.file.link,
    b,
    i.pct === null ? "sem dados" : (i.pct * 100).toFixed(0) + "%",
    dias + "d",
    ultima ? ultima.toFormat("dd/MM") : "—",
    situacao,
    i.ganho.toFixed(1),
    atraso, i.ganho
  ]);
}

// 3. Vencidos primeiro; entre vencidos, maior ganho primeiro
rows.sort((x, y) => {
  const xv = x[7] > 0, yv = y[7] > 0;
  if (xv !== yv) return yv - xv;
  if (xv) return y[8] - x[8] || y[7] - x[7];
  return y[7] - x[7];
});

dv.table(
  ["Resumo", "Bloco", "Acerto", "Intervalo", "Última", "Situação", "Ganho"],
  rows.map(r => r.slice(0, 7))
);
```

---

## A escada de intervalos

| Acerto no bloco | Reler em | Leitura |
| --- | --- | --- |
| abaixo de 50% | 2 dias | Não está aprendido; o material precisa voltar quase imediatamente |
| 50% a 64% | 5 dias | Frágil |
| 65% a 74% | 10 dias | Instável, mas em construção |
| 75% a 84% | 21 dias | Sólido, manutenção espaçada |
| 85% ou mais | 45 dias | Consolidado; só não deixar apagar |
| sem dados | 7 dias | Estudado e nunca testado — o mais perigoso da lista |

Os dias são convenção minha, calibrada para horizonte de concurso. A literatura do efeito de espaçamento sustenta o princípio — intervalos que se expandem conforme o domínio aumenta — mas os números exatos são julgamento, não schedule validado. Ajuste conforme observar o que funciona.

A propriedade útil desse desenho: nada é armazenado. O intervalo se recalcula sozinho a cada caderno novo. Se você piora num bloco, todos os resumos dele antecipam a data de vencimento automaticamente, sem você mexer em nada.

## Dicas de revisão que mudam o rendimento

**Releitura é o gesto mais fraco.** O painel diz quando o material precisa voltar, não que a forma de fazê-lo voltar seja ler. A sequência que rende: primeiro tente recuperar de memória o que a nota diz; só depois abra. Abrir direto é reconhecimento, não recuperação, e reconhecimento produz a sensação de saber sem o saber.

**Por isso o callout colapsável.** Estruture o resumo com a pergunta visível e a resposta escondida:

```markdown
> [!question]- Quais as hipóteses de diferimento?
> ...
```

Assim a própria nota força a tentativa antes da leitura.

**Bloco sem dados é prioridade escondida.** Material estudado e nunca testado aparece como "sem dados" e recebe intervalo curto de propósito. Você não sabe se domina — e não saber é pior que saber que não domina.

**Véspera não é releitura geral.** Perto da prova, a `#vespera` manda mais que a agenda: leia as folhas de uma tela, não o acervo. O painel serve para os meses anteriores; nos últimos dias, o critério é outro.

**Não atualize `revisado` por edição cosmética.** O campo mede esquecimento. Se ele virar carimbo de "mexi no arquivo", a agenda inteira passa a mentir.
