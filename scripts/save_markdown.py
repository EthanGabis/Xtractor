#!/usr/bin/env python3
import re
import sys
from pathlib import Path


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r'[^a-z0-9\u0590-\u05ff]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text or 'xtractor-output'


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: save_markdown.py <title> <output_dir>', file=sys.stderr)
        sys.exit(2)
    title = sys.argv[1]
    outdir = Path(sys.argv[2]).expanduser()
    outdir.mkdir(parents=True, exist_ok=True)
    content = sys.stdin.read()
    path = outdir / f'{slugify(title)}.md'
    path.write_text(content, encoding='utf-8')
    print(str(path))
