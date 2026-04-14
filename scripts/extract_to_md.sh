#!/usr/bin/env bash
set -euo pipefail

URL="${1:-}"
MODE="${2:-}"
OUTDIR="${3:-}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CFG_JSON="$(python3 "$ROOT/scripts/load_config.py")"

DEFAULT_MODE="$(python3 - <<'PY' "$CFG_JSON"
import json, sys
print(json.loads(sys.argv[1]).get('defaultMode','value'))
PY
)"
DEFAULT_OUTDIR="$(python3 - <<'PY' "$CFG_JSON"
import json, sys, os
print(os.path.expanduser(json.loads(sys.argv[1]).get('defaultOutputDir','~/Desktop')))
PY
)"

MODE="${MODE:-$DEFAULT_MODE}"
OUTDIR="${OUTDIR:-$DEFAULT_OUTDIR}"

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
if ! RAW_OUTPUT="$(python3 "$ROOT/scripts/grok_wait.py" "$PROMPT")"; then
  echo "Extraction failed. Check Chrome login state, Grok availability, and troubleshooting docs." >&2
  exit 1
fi
TITLE="$(printf '%s\n' "$RAW_OUTPUT" | head -n 1 | sed 's/^# *//')"
if [[ -z "$TITLE" ]]; then
  TITLE="xtractor-output"
fi
SAVED_PATH="$(printf '%s\n' "$RAW_OUTPUT" | python3 "$ROOT/scripts/save_markdown.py" "$TITLE" "$OUTDIR")"
echo "$SAVED_PATH"
