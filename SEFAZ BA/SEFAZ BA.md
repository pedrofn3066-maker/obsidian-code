# 🎯 Painel Tático - SEFAZ BA

> [!info] Foco Total
> "O que não é medido, não é gerenciado." Mantenha este painel aberto durante a sua sessão de estudos.

---

## 🚨 1. Pendências e Dúvidas (Resolver Hoje)
*Aqui aparecem todas as caixinhas de seleção (checkboxes) que você deixou em branco nas suas notas. Ideal para limpar dúvidas acumuladas antes de avançar para o próximo bloco.* 

___


# DOMÍNIO/BAIXO

```dataview
TABLE WITHOUT ID 
  L.section AS "📍 Local Exato", 
  replace(L.text, "#dominio/baixo", "") AS "🩸 Ponto a Melhorar"
FROM #dominio/baixo
FLATTEN file.lists AS L
WHERE contains(L.tags, "#dominio/baixo")
```
```dataview
TABLE WITHOUT ID 
  L.section AS "📍 Local Exato", 
  replace(L.text, "#tec/resumo", "") AS "🌂 pontos importantes"
FROM #tec/resumo 
FLATTEN file.lists AS L
WHERE contains(L.tags, "#tec/resumo")
```



___


# 🗂️ Gavetas de Revisão Rápida

> [!danger]- 🕵️‍♂️ Pegadinhas de Banca
> ```dataview
> LIST WITHOUT ID L.section + " ➡️ " + replace(L.text, "#pegadinha", "")
> FROM #pegadinha
> FLATTEN file.lists AS L
> WHERE contains(L.tags, "#pegadinha")
> ```

> [!question]- ❓ Dúvidas e Pesquisas Pendentes
> ```dataview
> LIST WITHOUT ID L.section + " ➡️ " + replace(L.text, "#acao/pesquisar", "")
> FROM #acao/pesquisar
> FLATTEN file.lists AS L
> WHERE contains(L.tags, "#acao/pesquisar")
> ```

> [!abstract]- ⚖️ Súmulas e Jurisprudência
> ```dataview
> LIST WITHOUT ID L.section + " ➡️ " + replace(L.text, "#jurisprudencia", "")
> FROM #jurisprudencia
> FLATTEN file.lists AS L
> WHERE contains(L.tags, "#jurisprudencia")
> ```

> [!warning]- 🚨 Foco em Exceções
> ```dataview
> LIST WITHOUT ID L.section + " ➡️ " + replace(L.text, "#excecao", "")
> FROM #excecao
> FLATTEN file.lists AS L
> WHERE contains(L.tags, "#excecao")
> ```

> [!ler]- 📖 REVISAR
> ```dataview
> LIST WITHOUT ID L.section + " ➡️ " + replace(L.text, "#revisar", "")
> FROM #revisar 
> FLATTEN file.lists AS L
> WHERE contains(L.tags, "#revisar")
> ```

> [!worng]- 😥 tec/erro
> ```dataview
> LIST WITHOUT ID L.section + " ➡️ " + replace(L.text, "#tec/erro", "")
> FROM #tec/erro  
> FLATTEN file.lists AS L
> WHERE contains(L.tags, "#tec/erro")
> ```

> [!worng]- 😥 banca
> ```dataview
> LIST WITHOUT ID L.section + " ➡️ " + replace(L.text, "banca", "")
> FROM #banca   
> FLATTEN file.lists AS L
> WHERE contains(L.tags, "#banca")
> ```
