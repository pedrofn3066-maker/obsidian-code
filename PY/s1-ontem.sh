#!/bin/zsh
# Mostra o que entrou no vault ontem — bloco 3 do painel "S1 - Revisão de ontem".
# Uso:  sh ~/…/vault-ba/PY/s1-ontem.sh          (só os arquivos)
#       sh ~/…/vault-ba/PY/s1-ontem.sh -p       (com o texto que entrou)

cd "$(dirname "$0")/.." || exit 1

# --name-status vence sobre -p no git seja qual for a ordem, então é um OU outro.
if [ -n "$1" ]; then FORMATO="-p"; else FORMATO="--name-status"; fi

# core.quotepath=false: sem isso o git mostra "L\303\255ngua" no lugar de "Língua".
# Os pathspecs no fim cortam o ruído de .obsidian/, Z IMG/ e Questoes/Paineis —
# este último espelha o -"Questoes/Paineis" do bloco 1 (Dataview), que já não
# conta painel como "onde você mexeu".
LOG=$(git -c core.quotepath=false log \
  --since=yesterday.midnight --until=today.midnight \
  "$FORMATO" --format="%n>>> %ad · %s" --date=format:"%H:%M" \
  -- MATERIAS Questoes Erradas ':!Questoes/Paineis')

if [ "$FORMATO" = "-p" ]; then
  # Modo -p é pra recall de texto, não pra ler diff: aqui só interessa "o que entrou",
  # então tira o plumbing do git (diff --git, index, mode, ---/+++, @@) e as linhas
  # removidas, e mostra o caminho do arquivo + só as linhas acrescentadas.
  echo "$LOG" | awk '
    /^>>> / { print; next }
    /^diff --git a\// {
      s = $0
      sub(/^diff --git a\//, "", s)
      n = index(s, " b/")
      path = (n > 0) ? substr(s, 1, n - 1) : s
      print "  · " path
      next
    }
    /^(index |new file mode|deleted file mode|old mode|new mode|similarity index|rename from|rename to|--- |\+\+\+ |@@ )/ { next }
    /^\+/ { sub(/^\+/, "    "); print; next }
    /^-/  { next }
    /^$/  { print; next }
    { next }
  '
else
  echo "$LOG"
fi

echo
echo "--- ainda não commitado (não aparece acima) ---"
git -c core.quotepath=false status --short -- MATERIAS Questoes Erradas ':!Questoes/Paineis'
