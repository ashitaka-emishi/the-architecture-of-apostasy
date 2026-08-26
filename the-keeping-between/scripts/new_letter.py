#!/usr/bin/env python3
from pathlib import Path
import argparse, re

ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('recipient')
p.add_argument('--theme',default='[issue]')
args=p.parse_args()
slug=re.sub(r'[^a-z0-9]+','-',args.recipient.lower()).strip('-')
out=ROOT/f'book-of-wolves/letters/{slug}.md'
if out.exists(): raise SystemExit(f'Exists: {out}')
tpl=(ROOT/'book-of-wolves/letters/LETTER_TEMPLATE.md').read_text(encoding='utf-8')
tpl=tpl.replace('[Recipient]',args.recipient).replace('[issue]',args.theme)
out.write_text(tpl,encoding='utf-8')
print(out)
