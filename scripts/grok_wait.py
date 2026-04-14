#!/usr/bin/env python3
import json
import subprocess
import sys
import textwrap
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: grok_wait.py '<prompt>'", file=sys.stderr)
    sys.exit(2)

prompt = sys.argv[1]
root = Path(__file__).resolve().parents[1]
tmp_dir = root / "tmp"
tmp_dir.mkdir(parents=True, exist_ok=True)
script_path = tmp_dir / "grok_runner.js"

script_path.write_text(textwrap.dedent(f"""
const {{ chromium }} = require('playwright');
(async() => {{
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context = browser.contexts()[0];
  if (!context) throw new Error('No Chrome context available. Make sure a debug Chrome profile is open.');

  const page = await context.newPage();
  let finalText = '';
  try {{
    await page.goto('https://grok.com/', {{ waitUntil: 'domcontentloaded', timeout: 30000 }}).catch(async()=>{{
      await page.goto('https://x.com/i/grok', {{ waitUntil: 'domcontentloaded', timeout: 30000 }});
    }});
    await page.waitForTimeout(5000);

    const bodyBefore = await page.locator('body').innerText().catch(()=> '');
    if (/sign in|sign up/i.test(bodyBefore) && !/grok/i.test(bodyBefore)) {{
      throw new Error('Grok/X appears to be signed out in the debug Chrome session.');
    }}

    const textbox = page.locator('textarea, div[contenteditable="true"], input[type="text"]').first();
    await textbox.click({{ timeout: 10000 }});
    await textbox.fill({json.dumps(prompt)}).catch(async()=>{{
      await page.keyboard.insertText({json.dumps(prompt)});
    }});
    await page.keyboard.press('Enter');

    const partialMarkers = ['Analyzing', 'Reading thread', 'Extracting thread', 'Quick Answer', 'Thinking', 'Get notified when Grok finishes answering'];
    let stable = 0;
    let last = '';
    for (let i = 0; i < 150; i++) {{
      await page.waitForTimeout(2000);
      const body = await page.locator('body').innerText().catch(()=> '');
      const hasPartial = partialMarkers.some(m => body.includes(m));
      const signedOut = /sign in|sign up/i.test(body) && !/grok/i.test(body);
      if (signedOut) throw new Error('Lost Grok/X login state while waiting for answer.');
      if (!hasPartial && body === last && body.length > 200) stable += 1; else stable = 0;
      last = body;
      if (!hasPartial && stable >= 2) break;
    }}

    finalText = last.slice(0, 50000);
    console.log(finalText);
  }} finally {{
    await page.close().catch(() => {{}});
    await browser.close().catch(() => {{}});
  }}
}})().catch(err => {{ console.error(String(err && err.stack || err)); process.exit(1); }});
"""), encoding="utf-8")

res = subprocess.run(["node", str(script_path)], cwd=str(root), capture_output=True, text=True)
print(res.stdout)
if res.returncode != 0:
    print(res.stderr, file=sys.stderr)
    sys.exit(res.returncode)
