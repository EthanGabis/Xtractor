# Troubleshooting

## Chrome debug session not found

Run:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-debug-xtractor
```

Then verify:

```bash
python3 scripts/check_chrome_debug.py
```

## Grok shows sign-in page

Make sure the debug Chrome profile is logged into X / Grok.

## Output is partial

Do not trust partial states like:
- Analyzing
- Reading thread
- Thinking
- Quick Answer

Wait longer and capture only a stable final output.

## X thread does not load properly

Open the link manually in the debug Chrome profile first, then rerun extraction.

## The script opened or changed the wrong tab

It should not. Current behavior is to open a new dedicated tab. If that does not happen, treat it as a bug.

## The script closed my browser

It should not. Current behavior is to close only the dedicated Grok tab. If the full browser closes, treat it as a bug.

## Markdown output looks ugly

Try another prompt mode:

```bash
./scripts/extract_to_md.sh "<url>" verbatim
./scripts/extract_to_md.sh "<url>" article
```
