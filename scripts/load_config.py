#!/usr/bin/env python3
import json
from pathlib import Path

DEFAULTS = {
    'chromeDebugUrl': 'http://127.0.0.1:9222',
    'defaultMode': 'value',
    'defaultOutputDir': '~/Desktop',
    'grokUrls': ['https://grok.com/', 'https://x.com/i/grok'],
    'pollIntervalMs': 2000,
    'maxPolls': 150,
}


def load_config():
    root = Path(__file__).resolve().parents[1]
    user_path = root / 'xtractor.config.json'
    if user_path.exists():
        data = json.loads(user_path.read_text(encoding='utf-8'))
        cfg = DEFAULTS.copy()
        cfg.update(data)
        return cfg
    return DEFAULTS.copy()


if __name__ == '__main__':
    print(json.dumps(load_config()))
