#!/usr/bin/env python3
from pathlib import Path
import argparse

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--full',action='store_true',help='Also append large source texts.')
args=parser.parse_args()

order=[]
for line in (ROOT/'context/CONTEXT_ORDER.txt').read_text(encoding='utf-8').splitlines():
    s=line.strip()
    if s and not s.startswith('#'): order.append(s)
if args.full:
    order += [
      'source/aru-vaen/the_troth_v3_draft.md',
      'source/aru-vaen/Aru_vaen_pdf_extracted.txt',
      'source/doctrine/The Doctrine of Unclaimed Virtue.md',
      'source/liturgy/The Liturgy of the Troth.md',
      'source/liturgy/The Greeting of the Troth.md',
      'source/sermons/The Troth Remains - John 10.md',
      'source/institutional/Constitution of the Order of the Troth.md',
      'source/institutional/The Rule of the Troth.md',
      'source/institutional/The Short Rule of the Troth.md',
      'source/institutional/The Mark of the Troth.md',
      'source/book-of-the-troth/The Letter of Little Vey to the Vaerun.md'
    ]

parts=['# CODEX CONTEXT BUNDLE\n']
for rel in order:
    p=ROOT/rel
    if not p.exists():
        parts.append(f'\n## MISSING: {rel}\n')
        continue
    parts.append(f'\n\n---\n\n# FILE: {rel}\n\n')
    parts.append(p.read_text(encoding='utf-8',errors='replace'))
out=ROOT/'build/CODEX_CONTEXT_FULL.md' if args.full else ROOT/'build/CODEX_CONTEXT.md'
out.write_text(''.join(parts),encoding='utf-8')
print(out)
