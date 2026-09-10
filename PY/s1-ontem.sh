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
git -c core.quotepath=false log \
  --since=yesterday.midnight --until=today.midnight \
  "$FORMATO" --format="%n>>> %ad · %s" --date=format:"%H:%M" \
  -- MATERIAS Questoes Erradas ':!Questoes/Paineis'

echo
echo "--- ainda não commitado (não aparece acima) ---"
git -c core.quotepath=false status --short -- MATERIAS Questoes Erradas ':!Questoes/Paineis'
