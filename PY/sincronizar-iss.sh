#!/bin/sh
# Alinha o cofre ISS SANTOS (AFTM Santos) com este vault. Só LÊ o vault-ba; só escreve no ISS,
# e só com --aplicar. Nunca commita.
#
# Grupo 1 (genéricos, idênticos nos dois cofres): copiados quando diferem.
# Grupo 2 (adaptados ao ISS — pesos, grade, banca): NUNCA copiados. O script só avisa quais mudaram
#   no vault-ba desde a última marca, para você portar à mão o trecho que interessa.
#
# Uso:  sh PY/sincronizar-iss.sh                # simulação: mostra o que faria
#       sh PY/sincronizar-iss.sh --aplicar      # copia o grupo 1 e grava a marca
#       sh PY/sincronizar-iss.sh --marcar       # só grava a marca (você conferiu o grupo 2)
#       sh PY/sincronizar-iss.sh -d "/outro/caminho/ISS"    # outro destino
#
# A marca é o commit do vault-ba na última sincronização, guardada em
# <ISS>/.vault-meta/sync-vault-ba. O grupo 2 é comparado contra ela (inclui alterações não commitadas).

set -eu

VAULT=$(cd "$(dirname "$0")/.." && pwd)
ISS="$VAULT/../ISS SANTOS "
APLICAR=0
MARCAR=0
while [ $# -gt 0 ]; do
  case "$1" in
    --aplicar) APLICAR=1 ;;
    --marcar) MARCAR=1 ;;
    -d) [ -n "${2:-}" ] || { echo "uso: $0 [-d DESTINO]" >&2; exit 2; }; ISS=$2; shift ;;
    *) echo "argumento desconhecido: $1" >&2; exit 2 ;;
  esac
  shift
done
[ -d "$ISS" ] || { echo "destino não existe: $ISS" >&2; exit 1; }
ISS=$(cd "$ISS" && pwd)

GRUPO1="PY/achar-heading.py PY/indice-materia.py PY/pdf-md.py PY/grifos.py PY/tec-caderno.py
PY/checar-markdown.py PY/validar-cadernos.py PY/backup-vault.sh PY/hooks/pre-commit"

GRUPO2="PY/plano-dia.py PY/tec-arvore.py PY/s1-ontem.py PY/s1-ontem.sh PY/diretorio-materias.py PY/fechamento-semana.py
.claude/commands/absorver-pdf.md .claude/commands/importar-tec.md .claude/commands/triar-inbox.md
.claude/commands/triar-inbox-plus.md .claude/skills/tirar-duvida/SKILL.md"

MARCA_ARQ="$ISS/.vault-meta/sync-vault-ba"
HEAD_ATUAL=$(git -C "$VAULT" rev-parse HEAD)

echo "origem:  $VAULT"
echo "destino: $ISS"
[ "$APLICAR" = 1 ] && echo "modo:    APLICAR" || echo "modo:    simulação (nada é escrito)"
echo

if [ "$MARCAR" = 0 ]; then
  echo "== Grupo 1 — genéricos =="
  MUDOU=0
  for f in $GRUPO1; do
    if [ ! -e "$VAULT/$f" ]; then echo "  ? $f (não existe no vault-ba)"; continue; fi
    if [ ! -e "$ISS/$f" ]; then ST="novo"; elif cmp -s "$VAULT/$f" "$ISS/$f"; then continue; else ST="difere"; fi
    MUDOU=1
    echo "  $ST: $f"
    if [ "$APLICAR" = 1 ]; then
      mkdir -p "$(dirname "$ISS/$f")"
      cp -p "$VAULT/$f" "$ISS/$f"
    fi
  done
  [ "$MUDOU" = 0 ] && echo "  tudo igual"
  # o hook do git não é versionado: mantém a cópia de .git/hooks em dia
  if [ "$APLICAR" = 1 ] && [ -d "$ISS/.git/hooks" ] && [ -e "$ISS/PY/hooks/pre-commit" ]; then
    cp "$ISS/PY/hooks/pre-commit" "$ISS/.git/hooks/pre-commit" && chmod +x "$ISS/.git/hooks/pre-commit"
  fi
  echo
fi

echo "== Grupo 2 — adaptados (não copiados) =="
if [ -f "$MARCA_ARQ" ]; then
  MARCA=$(cat "$MARCA_ARQ")
  echo "  marca: $(echo "$MARCA" | cut -c1-7) (última sincronização)"
  # shellcheck disable=SC2086
  LISTA=$(git -C "$VAULT" -c core.quotepath=false diff --name-only "$MARCA" -- $GRUPO2 2>/dev/null || true)
  if [ -z "$LISTA" ]; then
    echo "  nada mudou no vault-ba desde a marca"
  else
    echo "  mudaram no vault-ba — veja se algo vale portar para o ISS:"
    echo "$LISTA" | sed 's/^/    /'
    echo "  (ver o que mudou: git -C \"$VAULT\" diff $(echo "$MARCA" | cut -c1-7) -- <arquivo>)"
  fi
else
  echo "  sem marca ainda — não há como saber o que mudou. Arquivos deste grupo:"
  for f in $GRUPO2; do echo "    $f"; done
  echo "  Depois de conferir, grave a marca: sh PY/sincronizar-iss.sh --marcar"
fi
echo

if [ "$APLICAR" = 1 ] || [ "$MARCAR" = 1 ]; then
  mkdir -p "$ISS/.vault-meta"
  printf '%s\n' "$HEAD_ATUAL" > "$MARCA_ARQ"
  echo "marca gravada: $(echo "$HEAD_ATUAL" | cut -c1-7) → .vault-meta/sync-vault-ba"
else
  echo "Simulação. Para copiar o grupo 1: sh PY/sincronizar-iss.sh --aplicar"
fi
