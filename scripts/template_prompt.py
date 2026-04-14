#!/usr/bin/env python3
import sys
from pathlib import Path

if len(sys.argv) < 3:
    print('Usage: template_prompt.py <template_path> <url>', file=sys.stderr)
    sys.exit(2)

path = Path(sys.argv[1])
url = sys.argv[2]
text = path.read_text(encoding='utf-8')
print(text.replace('{{URL}}', url))
