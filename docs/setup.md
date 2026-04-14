# Setup

## Goal

Create a real browser session that Xtractor can attach to safely.

## 1. Launch Chrome with remote debugging

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-debug-xtractor
```

Why this matters:
- it gives the tool a browser automation endpoint
- it keeps this workflow separate from your normal Chrome profile if you want that
- it lets the tool attach to the exact browser session you logged into

## 2. Log into X / Grok

Use that Chrome window and make sure Grok is available.

## 3. Install dependencies

```bash
npm install
npx playwright install chromium
chmod +x scripts/*.py scripts/*.sh
```

## 4. Verify the browser session

```bash
python3 scripts/check_chrome_debug.py
```

## 5. Run extraction

```bash
./scripts/extract_to_md.sh "https://x.com/..."
```

## Output

The script prints the saved Markdown file path.
