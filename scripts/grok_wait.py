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
sys.path.insert(0, str(root / 'scripts'))
from load_config import load_config
cfg = load_config()
chrome_debug_url = cfg.get('chromeDebugUrl', 'http://127.0.0.1:9222')
grok_urls = cfg.get('grokUrls', ['https://grok.com/', 'https://x.com/i/grok'])
poll_ms = int(cfg.get('pollIntervalMs', 2000))
max_polls = int(cfg.get('maxPolls', 150))

tmp_dir = root / 'tmp'
tmp_dir.mkdir(parents=True, exist_ok=True)
script_path = tmp_dir / 'grok_runner.js'

script_path.write_text(textwrap.dedent(f"""
const {{ chromium }} = require('playwright');
(async() => {{
  const browser = await chromium.connectOverCDP({json.dumps(chrome_debug_url)});
  const context = browser.contexts()[0];
  if (!context) throw new Error('No Chrome context available. Make sure a debug Chrome profile is open.');

  const page = await context.newPage();
  let last = '';
  try {{
    const grokUrls = {json.dumps(grok_urls)};
    let opened = false;
    for (const url of grokUrls) {{
      try {{
        await page.goto(url, {{ waitUntil: 'domcontentloaded', timeout: 30000 }});
        opened = true;
        break;
      }} catch (e) {{}}
    }}
    if (!opened) throw new Error('Could not open Grok in the current browser session.');

    await page.waitForTimeout(6000);
    const bodyBefore = (await page.locator('body').innerText().catch(()=> '')).trim();
    if ((/sign in|sign up/i.test(bodyBefore) && !/grok/i.test(bodyBefore)) || /create your account|log in to x/i.test(bodyBefore)) {{
      throw new Error('Grok/X appears to be signed out in the debug Chrome session before prompt submission.');
    }}

    const textbox = page.locator('textarea, div[contenteditable="true"], input[type="text"]').first();
    await textbox.click({{ timeout: 15000 }});
    await textbox.fill({json.dumps(prompt)}).catch(async()=>{{
      await page.keyboard.insertText({json.dumps(prompt)});
    }});
    await page.keyboard.press('Enter');

    const partialMarkers = ['Analyzing', 'Reading thread', 'Extracting thread', 'Quick Answer', 'Thinking', 'Get notified when Grok finishes answering'];
    const likelyAnswerMarkers = ['## ', '# ', 'Key Takeaways', 'Why It Matters', 'Action Items', 'Source'];
    let stable = 0;
    let signedOutHits = 0;
    let seenSubstantiveOutput = false;

    for (let i = 0; i < {max_polls}; i++) {{
      await page.waitForTimeout({poll_ms});
      const body = (await page.locator('body').innerText().catch(()=> '')).trim();
      const articles = await page.locator('article').allInnerTexts().catch(() => []);
      const hasPartial = partialMarkers.some(m => body.includes(m));
      const maybeSignedOut = ((/sign in|sign up/i.test(body) && !/grok/i.test(body)) || /create your account|log in to x/i.test(body));

      let candidate = articles && articles.length ? articles[articles.length - 1] : body;
      candidate = (candidate || '').trim();
      if (!candidate || candidate.length < 80) candidate = body;

      if (candidate.length > 300 || likelyAnswerMarkers.some(m => candidate.includes(m))) {{
        seenSubstantiveOutput = true;
      }}

      if (maybeSignedOut && !seenSubstantiveOutput) signedOutHits += 1;
      else signedOutHits = 0;

      if (signedOutHits >= 3) {{
        throw new Error('Grok/X appears to be signed out while waiting for answer.');
      }}

      if (!hasPartial && candidate === last && candidate.length > 200) stable += 1; else stable = 0;
      last = candidate;

      if (seenSubstantiveOutput && !hasPartial && stable >= 3) break;
    }}

    if (!last || last.length < 80) throw new Error('Did not capture a usable answer from Grok.');
    console.log(last.slice(0, 50000));
  }} finally {{
    await page.close().catch(() => {{}});
  }}
}})().catch(err => {{ console.error(String(err && err.stack || err)); process.exit(1); }});
"""), encoding='utf-8')

res = subprocess.run(['node', str(script_path)], cwd=str(root), capture_output=True, text=True)
print(res.stdout)
if res.returncode != 0:
    print(res.stderr, file=sys.stderr)
    sys.exit(res.returncode)
