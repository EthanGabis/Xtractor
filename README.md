# Xtractor

Turn X/Twitter threads and web articles into clean Markdown using a real logged-in browser session and Grok — no API required.

## What this is

Xtractor solves a simple problem:

you find high-signal stuff on X or random articles every day, but that knowledge stays trapped in the feed or browser.

This repo gives you a reproducible flow to:
- open a real Chrome session with automation enabled
- use Grok inside that session to read a thread/article
- send an exact prompt plus the source link
- wait for the final answer
- save the result as a clean `.md` file on your Mac

## Why this exists

Every developer, founder, operator, and AI builder finds useful stuff on Twitter/X constantly.

The hard part is not discovery.
The hard part is capture.

Bookmarks rot. Threads disappear. Copy-paste is annoying. Agents cannot use information you never preserve.

Xtractor turns social content into local Markdown files so OpenClaw, Claude, or your own note system can actually use it.

## Two supported scenarios

### 1. Claude in Chrome
Use this when you already work inside Claude / Grok / browser tabs manually and want a repeatable way to export threads or articles.

### 2. OpenClaw + browser automation
Use this when OpenClaw is driving the browser for you and you want the extraction flow to be reproducible by an agent.

In both cases the core idea is the same:
- the user launches Chrome with automation enabled
- the browser is logged into X / Grok
- the tool opens Grok
- sends a prompt + the URL
- waits for the final answer
- writes Markdown to disk

## Quick start

### Step 1: launch Chrome with remote debugging

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-debug-xtractor
```

Log into X / Grok in that Chrome window.

### Step 2: run extraction

```bash
./scripts/extract_to_md.sh "https://x.com/irabukht/status/2043666224358556159?s=46"
```

That will:
1. verify the Chrome debug session exists
2. open Grok in your logged-in session
3. send the default prompt plus the URL
4. wait for the final answer
5. save the result as Markdown

## Repo layout

```text
Xtractor/
├── README.md
├── prompts/
│   ├── value-extract.md
│   ├── verbatim-extract.md
│   └── article-extract.md
├── scripts/
│   ├── check_chrome_debug.py
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

## Exact default prompt

See `prompts/value-extract.md`.

This is the default high-value prompt:
- extract content
- preserve meaning
- produce clean Markdown
- add takeaways and action items
- keep the source link

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
```

## Important notes

- this is **not** using the X API
- this is **not** scraping anonymously
- this depends on your real logged-in browser session
- if Grok cannot read the source fully, the output should say so explicitly

## For OpenClaw users

If OpenClaw is driving the browser, it needs a browser automation path (for example Chrome remote debugging plus a script like the ones in this repo). The agent should:
- attach to Chrome
- open Grok
- send the prompt
- wait for a stable answer
- save the answer into `.md`

See `docs/openclaw.md`.

## For Claude/browser users

If you are running the browser yourself and using Claude or another assistant to orchestrate it, the same remote-debugging setup works. The important part is that the browser session is real, logged in, and accessible.

See `docs/claude.md`.

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
