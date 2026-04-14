#!/usr/bin/env bash
set -euo pipefail

URL="${1:-}"
MODE="${2:-value}"
OUTDIR="${3:-$HOME/Desktop}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

if [[ -z "$URL" ]]; then
  echo "Usage: ./scripts/extract_to_md.sh <url> [value|verbatim|article] [output_dir]" >&2
  exit 2
fi

python3 "$ROOT/scripts/check_chrome_debug.py" >/dev/null

case "$MODE" in
  value) TEMPLATE="$ROOT/prompts/value-extract.md" ;;
  verbatim) TEMPLATE="$ROOT/prompts/verbatim-extract.md" ;;
  article) TEMPLATE="$ROOT/prompts/article-extract.md" ;;
  *) echo "Unknown mode: $MODE" >&2; exit 2 ;;
esac

PROMPT="$(python3 "$ROOT/scripts/template_prompt.py" "$TEMPLATE" "$URL")"
RAW_OUTPUT="$(python3 "$ROOT/scripts/grok_wait.py" "$PROMPT")"
TITLE="$(printf '%s\n' "$RAW_OUTPUT" | head -n 1 | sed 's/^# *//')"
if [[ -z "$TITLE" ]]; then
  TITLE="xtractor-output"
fi
SAVED_PATH="$(printf '%s\n' "$RAW_OUTPUT" | python3 "$ROOT/scripts/save_markdown.py" "$TITLE" "$OUTDIR")"
echo "$SAVED_PATH"
