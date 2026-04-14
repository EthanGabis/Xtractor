# OpenClaw wiring

OpenClaw needs a browser automation path to make this flow work.

Recommended setup:
- Chrome launched with remote debugging on port `9222`
- Playwright installed locally
- Grok available in the logged-in browser profile
- local file write permissions for saving Markdown

## Safe agent flow

1. Verify the Chrome debug endpoint is reachable
2. Open a **new dedicated Grok tab**
3. Load the selected prompt template
4. Inject the target URL safely
5. Send the prompt to Grok
6. Wait until the answer is stable (not still thinking/analyzing)
7. Save the final answer to Markdown
8. Close only the dedicated tab

## Agent rules

- do not close the user's browser session
- do not reuse the first open tab by default
- do not claim success if Grok is signed out
- do not pretend partial output is complete
- prefer value mode by default unless the user wants verbatim output

## Why this fits OpenClaw

The output becomes a local Markdown file that can be reused in later agent workflows:
- research
- note-taking
- knowledge capture
- memory building

That is the real value.
