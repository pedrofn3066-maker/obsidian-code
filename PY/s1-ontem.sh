#!/bin/sh
# Mostra o que entrou no vault ontem — bloco 3 do painel "S1 - Revisão de ontem".
# Uso:  sh ~/…/vault-ba/PY/s1-ontem.sh          (só os arquivos)
#       sh ~/…/vault-ba/PY/s1-ontem.sh -p       (com o texto que entrou)
#
# QUAIS arquivos: por mtime (mesma regra do bloco 1 do painel). O mtime é a única
# fonte do momento real da escrita; a data de commit atribui tudo ao dia em que
# você lembrou de commitar.
# Além disso entram os cadernos de Questoes/Diario com `data:` de ontem no frontmatter,
# mesmo que o mtime seja de hoje (importação/reescrita) — espelha o bloco 2 do painel.
# Antes dos arquivos vem a seção de triagens (commits "Triagem…" do dia).
# QUAL texto (-p): git não guarda o texto por mtime, então o -p mostra as linhas
# acrescentadas nesses arquivos nos commits desde ontem 00:00 (sem limite superior,
# pra pegar commit de recuperação feito hoje) + o que ainda não foi commitado.

cd "$(dirname "$0")/.." || exit 1

ONTEM=$(date -v-1d +%Y-%m-%d)
HOJE=$(date +%Y-%m-%d)

# -newermt é por instante: >= ontem 00:00 e não >= hoje 00:00. Exclui Questoes/Paineis,
# espelhando o -"Questoes/Paineis" do bloco 1.
LISTA=$(find MATERIAS Questoes Erradas -type f -name '*.md' \
  -not -path 'Questoes/Paineis/*' \
  -newermt "$ONTEM 00:00:00" ! -newermt "$HOJE 00:00:00" \
  -exec stat -f '%m %N' {} + 2>/dev/null | sort -n | cut -d' ' -f2-)

# Cadernos de ontem pela data do frontmatter, ainda fora da lista (mtime de hoje).
# Ficam depois dos de mtime, marcados com "hoje HH:MM".
EXTRAS=""
for c in Questoes/Diario/*.md; do
  [ -f "$c" ] || continue
  grep -q "^data: $ONTEM\$" "$c" || continue
  printf '%s\n' "$LISTA" | grep -Fxq -- "$c" && continue
  EXTRAS="$EXTRAS$c
"
done
LISTA=$(printf '%s\n%s' "$LISTA" "$EXTRAS" | sed '/^$/d')

# Só acrescentadas, sem o plumbing do git.
so_acrescentado() {
  awk '
    /^>>> / { print; next }
    /^diff --git a\// { next }
    /^(index |new file mode|deleted file mode|old mode|new mode|similarity index|rename from|rename to|--- |\+\+\+ |@@ )/ { next }
    /^\+/ { sub(/^\+/, "    "); print; next }
  '
}

# Triagens: um cartão por commit "Triagem…" de ontem, ou feito depois mas com "(dd/mm)" de
# ontem no assunto (o /triar-inbox nem sempre commita no mesmo dia). Com -p mostra o texto.
DDMM=$(date -v-1d +%d/%m)
PATHSPEC="MATERIAS Questoes Erradas :!Questoes/Paineis"
echo "Triagens de ontem (commits 'Triagem…' de $ONTEM ou com ($DDMM) no assunto):"
echo
# --reverse: ordem cronológica. read com IFS='|': o assunto fica com o resto da linha.
# shellcheck disable=SC2086
git -c core.quotepath=false log --since=yesterday.midnight --grep='^Triagem' --reverse \
    --format='%h|%ad|%s' --date=format:'%Y-%m-%d %H:%M' -- $PATHSPEC |
while IFS='|' read -r h quando assunto; do
  case "$quando" in
    "$ONTEM "*) rotulo="${quando#* }" ;;
    *) case "$assunto" in
         *"($DDMM)"*) d=${quando%% *}; md=${d#*-}; rotulo="commit de ${md#*-}/${md%-*} ${quando#* }" ;;
         *) continue ;;
       esac ;;
  esac
  echo ">>> $rotulo · $assunto ($h)"
  if [ -n "$1" ]; then
    git -c core.quotepath=false show --format= -p "$h" -- $PATHSPEC | awk '
      /^diff --git a\// { s=$0; sub(/^diff --git a\//,"",s); n=index(s," b/"); print "  · " (n>0 ? substr(s,1,n-1) : s); next }
      /^(index |new file mode|deleted file mode|old mode|new mode|similarity index|rename from|rename to|--- |\+\+\+ |@@ )/ { next }
      /^\+/ { sub(/^\+/, "    "); print }'
  else
    git -c core.quotepath=false show --format= --name-only "$h" -- $PATHSPEC | sed 's/^/  · /'
  fi
  echo
done
# O while roda em subshell (pipe), então o aviso de "nenhuma" vem de uma segunda consulta.
if ! git log --since=yesterday.midnight --grep='^Triagem' --format='%ad|%s' --date=format:'%Y-%m-%d' \
     -- $PATHSPEC | grep -Eq "^$ONTEM\||\($DDMM\)"; then
  echo "(nenhum commit 'Triagem…' de ontem)"
  echo
fi

if [ -z "$LISTA" ]; then
  echo "Nenhum arquivo com mtime de $ONTEM em MATERIAS, Questoes ou Erradas."
  echo "(Nota editada ontem e reaberta hoje conta como hoje — ver aviso do bloco 1.)"
  exit 0
fi

echo "Arquivos com mtime de $ONTEM + cadernos com data $ONTEM:"
echo
printf '%s\n' "$LISTA" | while IFS= read -r f; do
  hora=$(stat -f '%Sm' -t '%H:%M' "$f")
  [ "$(stat -f '%Sm' -t '%Y-%m-%d' "$f")" = "$ONTEM" ] || hora="hoje $hora"
  if [ -z "$1" ]; then
    echo "$hora  $f"
    continue
  fi
  echo ">>> $hora · $f"
  # core.quotepath=false: sem isso o git mostra "L\303\255ngua" no lugar de "Língua".
  # Commits desde ontem 00:00 (inclui commit de recuperação de hoje) e depois o não commitado.
  {
    git -c core.quotepath=false log --since=yesterday.midnight -p --format='' -- "$f"
    git -c core.quotepath=false diff HEAD --no-color -- "$f"
  } | so_acrescentado
  echo
done
