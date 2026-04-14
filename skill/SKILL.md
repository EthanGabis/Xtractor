---
name: xtractor
description: Extract X/Twitter threads and web articles into Markdown using a real logged-in Chrome session and Grok, without an API. Use when an agent needs to preserve social or web content as local Markdown files. Default flow: launch Chrome with remote debugging, attach safely without disturbing the user's existing tabs, open a dedicated Grok tab, send a prompt plus the source URL, wait for a stable final answer, and save the output to disk.
---

# Xtractor

Use this skill when the user wants to turn an X thread or article into a local Markdown file.

## Required workflow

1. Verify Chrome remote debugging is reachable on `http://127.0.0.1:9222`.
2. Use the user's logged-in browser session.
3. Open a **new dedicated tab** for Grok. Do not hijack the user's first tab.
4. Load a prompt template and inject the target URL safely.
5. Wait for a stable final answer, not a partial thinking state.
6. Save the output to Markdown with a clean filename.
7. Close only the dedicated Grok tab. Do not close the user's browser.

## Safety rules

- Never close the whole browser session.
- Never reuse or navigate the user's current tab by default.
- Prefer a new tab per extraction.
- If Grok is not logged in or not available, fail clearly.
- If the output looks partial or polluted with UI text, say so.

## Preferred prompts

- `prompts/value-extract.md` for high-value summary + takeaways
- `prompts/verbatim-extract.md` for near-verbatim archival output
- `prompts/article-extract.md` for normal web articles

## Setup docs

- `docs/setup.md`
- `docs/openclaw.md`
- `docs/claude.md`
- `docs/troubleshooting.md`
