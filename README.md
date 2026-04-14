# Xtractor

Turn X/Twitter threads and web articles into clean Markdown using a real logged-in browser session and Grok — no API required.

## What this does

Xtractor gives agents and humans a reproducible way to preserve useful content from X and the web as local Markdown files.

The core flow is simple:
1. launch Chrome with remote debugging enabled
2. log into X / Grok in that Chrome profile
3. attach safely to the live browser session
4. open a **dedicated Grok tab**
5. send a prompt plus the source URL
6. wait for a stable final answer
7. save the result as a `.md` file on disk

This is meant to be practical, not magical. It uses your real browser session, not the X API.

## Why this exists

Every developer, founder, operator, and AI builder finds useful stuff on X constantly.

The hard part is not discovery.
The hard part is capture.

Bookmarks rot. Threads disappear. Copy-paste is annoying. Agents cannot use information you never preserve.

Xtractor turns social content into local Markdown files so OpenClaw, Claude, and other assistants can actually use it later.

## Supported scenarios

### 1. Claude / assistant + browser
Use this when you are already working manually in a browser and want a repeatable export flow.

### 2. OpenClaw + browser automation
Use this when OpenClaw is orchestrating the browser and needs a documented, safe extraction workflow.

In both cases the same wiring matters:
- Chrome launched with remote debugging
- logged-in X / Grok session
- safe browser attachment
- dedicated Grok tab
- prompt + URL
- stable answer capture
- Markdown save

## Safety guarantees

Xtractor is designed to be safer for real user sessions:
- it opens a **new dedicated tab** instead of hijacking your first tab
- it closes only that tab when finished
- it does **not** intentionally close your whole browser session
- it fails clearly if the debug browser is missing or Grok is signed out

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

## Repo layout

```text
Xtractor/
├── README.md
├── LICENSE
├── skill/
│   └── SKILL.md
├── prompts/
│   ├── value-extract.md
│   ├── verbatim-extract.md
│   └── article-extract.md
├── scripts/
│   ├── check_chrome_debug.py
│   ├── template_prompt.py
│   ├── grok_wait.py
│   ├── save_markdown.py
│   └── extract_to_md.sh
├── examples/
│   ├── sample-thread-output.md
│   └── sample-article-output.md
└── docs/
    ├── setup.md
    ├── openclaw.md
    ├── claude.md
    └── troubleshooting.md
```

## Prompt templates

- `prompts/value-extract.md` → best default for useful Markdown with takeaways and action items
- `prompts/verbatim-extract.md` → best for archival / near-verbatim extraction
- `prompts/article-extract.md` → best for normal web articles

## OpenClaw

If OpenClaw is driving the browser, use the skill in `skill/SKILL.md` and the docs in `docs/openclaw.md`.

The agent should:
- verify the Chrome debug session
- attach safely
- open a new Grok tab
- send prompt + URL
- wait for stable output
- save to Markdown

## Claude / assistant users

If a browser-aware assistant is orchestrating the flow, the same setup still works.

See `docs/claude.md`.

## Limitations

- depends on a real logged-in browser session
- depends on Grok availability and page structure
- the final output quality still depends on Grok reading the source correctly
- some pages may still be partial or blocked, and the output should say so when that happens

## Why Markdown

Markdown is the right output because it is:
- local
- searchable
- portable
- agent-readable
- git-friendly
- easy to reuse in notes, repos, and future analysis

## Call to action

If your bookmarks are full of threads you never revisit, this is for you.
If you use Claude or OpenClaw and want your best discoveries to become reusable knowledge, this is for you.

Stop losing high-signal content to the feed.
Turn it into Markdown and make it part of your agent workflow.
