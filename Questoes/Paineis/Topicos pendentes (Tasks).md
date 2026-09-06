Lista todo checkbox `- [ ] status [dom:: N] [peso:: N]` ainda não marcado dentro de `MATERIAS/` — ou seja, todo tópico que ainda não foi sequer aberto pra estudo, agrupado por matéria e por tópico.

```tasks
not done
path includes MATERIAS
group by path
group by heading
```

> [!warning]- Isso não substitui o Ganho Potencial
> O Tasks não entende `[dom:: N]` nem `[peso:: N]` como campos próprios — são sintaxe do Dataview, não dele. Essa lista mostra **o que falta abrir**, não **o que vale mais ponto**. Pra priorizar por peso do edital, use `Ganho potencial`/`Fila de reforço`. Pra ver o que ainda está zerado (nunca estudado) matéria por matéria, use esta lista.

> [!tip]- Marcar como concluído
> Clique na caixa do checkbox na própria nota de `MATERIAS` (não aqui no painel) — o Tasks reflete o estado real da nota, não guarda status à parte.
