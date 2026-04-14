#!/usr/bin/env python3
import json
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from load_config import load_config

cfg = load_config()
url = cfg.get('chromeDebugUrl', 'http://127.0.0.1:9222').rstrip('/') + '/json/version'
try:
    with urllib.request.urlopen(url, timeout=3) as r:
        data = json.loads(r.read().decode('utf-8', errors='replace'))
    print(json.dumps({
        'ok': True,
        'url': url,
        'browser': data.get('Browser'),
        'ws': data.get('webSocketDebuggerUrl')
    }, indent=2))
except Exception as e:
    print(json.dumps({
        'ok': False,
        'url': url,
        'error': str(e),
        'hint': 'Launch Chrome with remote debugging and make sure the correct browser profile is open.'
    }, indent=2))
    sys.exit(1)
