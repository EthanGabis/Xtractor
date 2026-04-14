# OpenClaw wiring

OpenClaw needs a browser automation path to make this flow work.

Recommended setup:
- Chrome launched with remote debugging on port `9222`
- Playwright available locally
- Grok available in the logged-in browser profile
- local file write permissions for saving Markdown

## Safe agent flow

1. Verify `http://127.0.0.1:9222/json/version` is reachable
2. Open a **new dedicated Grok tab** in the attached browser session
3. Load the selected prompt template
4. Inject the target URL safely
5. Send the prompt to Grok
6. Wait until the answer is stable (not still thinking/analyzing)
7. Save the visible final answer to Markdown
8. Close only the dedicated tab

## Important agent rules

- Do not close the user's browser session
- Do not reuse the first open tab by default
- Do not claim success if Grok is signed out or the output is partial
- Prefer value mode by default; use verbatim mode only when the user wants near-verbatim output

## Why this is better than API-first

- no X API needed
- uses the user's real authenticated session
- easier to preserve full thread/article meaning
- saves directly into local agent-readable files
