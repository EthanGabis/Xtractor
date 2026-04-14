# Setup

## 1. Launch Chrome with automation enabled

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-debug-xtractor
```

## 2. Log into X / Grok

Use that Chrome window and make sure Grok is available in the session.

## 3. Run extraction

```bash
./scripts/extract_to_md.sh "https://x.com/..."
```

## 4. Check the output path

The script prints the final `.md` file path after saving.
