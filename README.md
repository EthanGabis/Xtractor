# Xtractor

Turn X/Twitter threads and web articles into clean Markdown using your real logged-in browser session and Grok — no API required.

## Why this matters

Every developer finds useful stuff on X all day:
- threads with killer prompts
- growth tactics
- infra/debugging explanations
- niche articles you absolutely want later

The problem is not discovery.
The problem is capture.

Bookmarks rot. Threads disappear. Agents cannot use information you never preserve.

**Xtractor converts feed knowledge into local Markdown files your agents can actually use later.**

That is the whole point.

## What it actually does

Xtractor uses a real browser session, not an API.

The flow:
1. launch Chrome with remote debugging enabled
2. log into X / Grok in that Chrome profile
3. attach safely to the live browser session
4. open a dedicated Grok tab
5. send Grok a prompt plus the source URL
6. wait for a stable final answer
7. save the result as a `.md` file on disk

So instead of bookmarking a thread and losing it forever, you get a real Markdown artifact you can search, store, feed into OpenClaw, or reuse later.

## Good fit

Use Xtractor when you want to:
- export X threads to Markdown
- preserve useful articles locally
- build a personal knowledge base from content you discover online
- feed saved content into OpenClaw, Claude, or future agent workflows

## Supported scenarios

### 1. Claude / assistant + browser
Use this when you already work manually in a browser and want a repeatable export flow.

### 2. OpenClaw + browser automation
Use this when OpenClaw is orchestrating the browser and needs a documented extraction workflow.

## Safety behavior

Xtractor tries to avoid messing up the user’s live browser session:
- opens a **new dedicated tab** instead of hijacking the first tab
- closes only that tab when finished
- does **not intentionally close the whole browser session**
- fails clearly if the browser session is missing or Grok is signed out

## Requirements

- macOS or Linux with Chrome/Chromium
- Python 3
- Node.js
- a logged-in Grok-capable browser session
- browser automation access via Chrome remote debugging

## Install

```bash
npm install
npx playwright install chromium
chmod +x scripts/*.py scripts/*.sh
cp xtractor.config.example.json xtractor.config.json
```

## Quick start

### 1. Launch Chrome with remote debugging

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-debug-xtractor
```

Use that Chrome window to log into X / Grok.

### 2. Verify the session

```bash
python3 scripts/check_chrome_debug.py
```

### 3. Run extraction

```bash
./scripts/extract_to_md.sh "https://x.com/irabukht/status/2043666224358556159?s=46"
```

That will:
1. verify the debug session exists
2. load the chosen prompt template
3. open Grok in a dedicated tab
4. send the prompt plus the URL
5. wait for the final answer
6. save the Markdown file and print its path

### Optional modes

```bash
./scripts/extract_to_md.sh "https://x.com/..." value
./scripts/extract_to_md.sh "https://x.com/..." verbatim
./scripts/extract_to_md.sh "https://example.com/article" article
```

## Config

Edit `xtractor.config.json` if you want to change:
- Chrome debug URL
- default mode
- default output directory
- Grok URL order
- polling interval
- max polls

Keep it simple. The example config is enough for most users.

## Repo layout

```text
Xtractor/
├── README.md
├── LICENSE
├── xtractor.config.example.json
├── skill/
│   └── SKILL.md
├── prompts/
│   ├── value-extract.md
│   ├── verbatim-extract.md
│   └── article-extract.md
├── scripts/
│   ├── check_chrome_debug.py
│   ├── load_config.py
│   ├── template_prompt.py
│   ├── grok_wait.py
│   ├── save_markdown.py
│   └── extract_to_md.sh
├── examples/
│   ├── sample-thread-output.md
│   ├── sample-article-output.md
│   ├── real-thread-example.md
│   └── real-article-example.md
└── docs/
    ├── setup.md
    ├── openclaw.md
    ├── claude.md
    └── troubleshooting.md
```

## Prompt templates

- `prompts/value-extract.md` → default useful Markdown with takeaways and action items
- `prompts/verbatim-extract.md` → near-verbatim archival extraction
- `prompts/article-extract.md` → normal web articles

## OpenClaw

If OpenClaw is driving the browser, use the skill in `skill/SKILL.md` and the docs in `docs/openclaw.md`.

The agent should:
- verify the Chrome debug session
- attach safely
- open a new Grok tab
- send prompt + URL
- wait for stable output
- save to Markdown

## Limitations

This is practical and useful, but not magic.

It still depends on:
- a real logged-in browser session
- Grok availability
- page/UI stability
- Grok actually reading the source correctly

When that fails, Xtractor should fail clearly rather than pretend success.

## Why Markdown

Markdown is the right destination because it is:
- local
- searchable
- portable
- agent-readable
- git-friendly
- easy to reuse later

## Call to action

If your bookmarks are full of threads you never revisit, this is for you.
If you use Claude or OpenClaw and want your best discoveries to become reusable knowledge, this is for you.

Stop losing high-signal content to the feed.
Turn it into Markdown and make it part of your agent workflow.
