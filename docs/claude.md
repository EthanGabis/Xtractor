# Claude / browser wiring

If Claude or another assistant is orchestrating the browser rather than OpenClaw, the same setup still works.

You need:
- a real Chrome window with remote debugging enabled
- a logged-in Grok session
- a script or helper that can open Grok, send the prompt, wait, and save the answer

The important thing is not the exact assistant — it is the flow:
- real browser
- logged-in Grok
- prompt + link
- stable final answer
- save to Markdown
