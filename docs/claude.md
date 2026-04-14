# Claude / assistant wiring

If Claude or another browser-aware assistant is orchestrating the flow, the same setup still works.

You need:
- a real Chrome window with remote debugging enabled
- a logged-in Grok session
- Playwright installed locally
- permission to save files on disk

## Safe flow

1. Launch Chrome with remote debugging
2. Log into X / Grok in that Chrome session
3. Run the extraction script
4. Let it open a dedicated Grok tab
5. Wait for the stable final answer
6. Save the Markdown file locally

The important part is not the exact assistant.
The important part is the wiring:
- real browser
- logged-in Grok
- prompt + link
- stable final answer
- save to Markdown
