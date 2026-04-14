# Troubleshooting

## Chrome debug session not found

Run:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-debug-xtractor
```

## Grok shows sign-in page

Make sure the debug Chrome profile is logged into X / Grok.

## Output is partial

Do not capture while Grok still shows states like:
- Analyzing
- Reading thread
- Thinking
- Quick Answer

Wait longer and capture only the stable final output.

## X thread does not load properly

Open the link manually in the debug Chrome profile first, then rerun extraction.

## Markdown output looks ugly

Switch prompt templates or post-process the result with `save_markdown.py`.
