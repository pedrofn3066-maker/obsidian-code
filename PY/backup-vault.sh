#!/bin/sh
# Backup local do vault: copia a pasta inteira (com .git e os arquivos que o git ignora,
# como inbox/*.pdf e .smart-env) para <destino>/<vault>-AAAA-MM-DD_HHMMSS. Não envia nada
# ao GitHub e nunca sobrescreve um backup existente.
#
# Uso:  sh PY/backup-vault.sh                 (destino padrão: ~/Backups)
#       sh PY/backup-vault.sh -d /Volumes/HD  (outro destino, p. ex. disco externo)
#       BACKUP_DIR=/Volumes/HD sh PY/backup-vault.sh
#
# O 1º backup é uma cópia completa (~1 GB). Os seguintes usam hardlinks contra o backup
# mais recente (rsync --link-dest): arquivo que não mudou não ocupa espaço de novo, então
# cada snapshot custa só o que mudou — e continua sendo uma pasta inteira, restaurável
# sozinha. Nada é apagado: para liberar espaço, apague pastas antigas à mão (cada uma é
# independente).
#
# Restaurar: abra a pasta do backup como vault no Obsidian, ou copie de volta com rsync -a.

set -eu

VAULT=$(cd "$(dirname "$0")/.." && pwd)
DESTINO=${BACKUP_DIR:-$HOME/Backups}
if [ "${1:-}" = "-d" ]; then
  [ -n "${2:-}" ] || { echo "uso: $0 [-d DESTINO]" >&2; exit 2; }
  DESTINO=$2
fi

NOME="$(basename "$VAULT")-$(date +%Y-%m-%d_%H%M%S)"
NOVO="$DESTINO/$NOME"

mkdir -p "$DESTINO"
[ -e "$NOVO" ] && { echo "já existe: $NOVO" >&2; exit 1; }

# Backup mais recente = último por nome (a data está no nome, então ordem alfabética = cronológica).
ANTERIOR=$(ls -d "$DESTINO/$(basename "$VAULT")"-* 2>/dev/null | sort | tail -1 || true)

echo "origem:  $VAULT"
echo "destino: $NOVO"
[ -n "$ANTERIOR" ] && echo "base:    $ANTERIOR (hardlinks)"

if [ -n "$ANTERIOR" ]; then
  rsync -a --exclude .DS_Store --link-dest="$ANTERIOR" "$VAULT/" "$NOVO/"
else
  rsync -a --exclude .DS_Store "$VAULT/" "$NOVO/"
fi

# Conferência: mesmo número de arquivos, mesmo commit, e o git da cópia sem erro real
# (objetos "dangling" são lixo normal de commits antigos, não erro).
N_ORIGEM=$(find "$VAULT" -type f ! -name .DS_Store | wc -l | tr -d ' ')
N_COPIA=$(find "$NOVO" -type f | wc -l | tr -d ' ')
HEAD_ORIGEM=$(git -C "$VAULT" rev-parse --short HEAD 2>/dev/null || echo "-")
HEAD_COPIA=$(git -C "$NOVO" rev-parse --short HEAD 2>/dev/null || echo "-")
ERROS=$(git -C "$NOVO" fsck --no-progress 2>&1 | grep -ciE 'error|missing|corrupt|broken' || true)

echo
echo "arquivos: origem $N_ORIGEM · cópia $N_COPIA"
echo "HEAD:     origem $HEAD_ORIGEM · cópia $HEAD_COPIA"
echo "fsck:     $ERROS erro(s)"
if [ -n "$ANTERIOR" ]; then
  echo "espaço:   $(du -sh "$ANTERIOR" "$NOVO" | tail -1 | cut -f1) a mais que o backup anterior"
else
  echo "espaço:   $(du -sh "$NOVO" | cut -f1)"
fi

if [ "$N_ORIGEM" != "$N_COPIA" ] || [ "$HEAD_ORIGEM" != "$HEAD_COPIA" ] || [ "$ERROS" != "0" ]; then
  echo "ATENÇÃO: a conferência falhou — não confie nesta cópia: $NOVO" >&2
  exit 1
fi
echo "OK — backup conferido."
