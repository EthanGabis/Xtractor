#!/usr/bin/env python3
import json
import sys
import urllib.request

url = 'http://127.0.0.1:9222/json/version'
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
    print(json.dumps({'ok': False, 'url': url, 'error': str(e)}, indent=2))
    sys.exit(1)
