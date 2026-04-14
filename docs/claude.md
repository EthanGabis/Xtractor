# Claude / browser wiring

If Claude or another assistant is orchestrating the browser rather than OpenClaw, the same setup still works.

You need:
- a real Chrome window with remote debugging enabled
- a logged-in Grok session
- Playwright available locally
- permission to save files on disk

## Safe flow

1. Launch Chrome with remote debugging
2. Log into X / Grok in that Chrome session
3. Run the extraction script
4. Let it open a dedicated Grok tab
5. Wait for the stable final answer
6. Save the Markdown file locally

The important thing is not the exact assistant — it is the wiring:
- real browser
- logged-in Grok
- prompt + link
- stable final answer
- save to Markdown
