# OpenClaw wiring

OpenClaw needs some browser automation path to make this flow work.

Recommended setup:
- Chrome launched with remote debugging on port `9222`
- agent script that can attach to the real browser session
- Grok available in the logged-in browser profile
- local file write permissions for saving Markdown

## Agent flow

1. Verify `http://127.0.0.1:9222/json/version` is reachable
2. Open Grok in the attached browser session
3. Load the selected prompt template
4. Inject the target URL into the prompt
5. Send the prompt to Grok
6. Wait until the answer is stable (not still thinking/analyzing)
7. Save the visible final answer to Markdown

## Why this is better than API-first

- no X API needed
- uses the user's real authenticated session
- easier to preserve full thread/article meaning
- saves directly into local agent-readable files
