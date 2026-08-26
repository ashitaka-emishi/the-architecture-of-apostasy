#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, re, sys

from build_aru_vaen_reviews import check_packets

ROOT = Path(__file__).resolve().parents[1]
required = [
    'AGENTS.md','context/CURRENT_DECISIONS.md','context/ACCEPTED_ARTIFACTS.md','context/CORE_CONTEXT.md',
    'source/aru-vaen/Aru vaen-A Keeping of the Troth.pdf',
    'source/aru-vaen/the_troth_v3_draft.md',
    'aru-vaen/ARU_VAEN.md',
    'doctrine/Doctrine_of_Unclaimed_Virtue.md',
    'registers/proposition-register.json','registers/artifact-register.json',
    'registers/glossary.json','registers/workstreams.json'
]
errors=[]; warnings=[]
for r in required:
    if not (ROOT/r).exists(): errors.append(f'Missing required path: {r}')

valid_status={'source','user_established','working_synthesis','proposed','research','deprecated'}

for jf in ROOT.rglob('*.json'):
    try:
        json.loads(jf.read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'Invalid JSON {jf.relative_to(ROOT)}: {e}')

try:
    pr=json.loads((ROOT/'registers/proposition-register.json').read_text())['propositions']
    ids=[x['id'] for x in pr]
    if len(ids)!=len(set(ids)): errors.append('Duplicate proposition IDs')
    for x in pr:
        if x.get('status') not in valid_status: errors.append(f"Invalid proposition status {x.get('status')} on {x.get('id')}")
except Exception as e:
    errors.append(f'Cannot validate proposition register: {e}')

try:
    ar=json.loads((ROOT/'registers/artifact-register.json').read_text())['artifacts']
    ids=[x['id'] for x in ar]
    if len(ids)!=len(set(ids)): errors.append('Duplicate artifact IDs')
    for x in ar:
        p=ROOT/x['path']
        if not p.exists(): errors.append(f"Artifact path missing: {x['path']}")
        if x.get('status') not in valid_status: errors.append(f"Invalid artifact status {x.get('status')} on {x.get('id')}")
        if p.exists() and x.get('sha256'):
            h=hashlib.sha256(p.read_bytes()).hexdigest()
            if h != x['sha256']: warnings.append(f"Hash changed since scaffold creation: {x['path']}")
except Exception as e:
    errors.append(f'Cannot validate artifact register: {e}')

try:
    errors.extend(check_packets())
except Exception as e:
    errors.append(f'Cannot validate Aru Va\'en review packets: {e}')

# Warn about accidental resurrection of Order of the Troth outside explanatory/context files.
allowed_order_files={
    'context/CURRENT_DECISIONS.md',
    'context/DO_NOT_ASSUME.md',
    'AGENTS.md',
    'registers/glossary.json',
    'institutional/README.md',
    'institutional/CONSTITUTION_DRAFT.md',
    'institutional/RULE_DRAFT.md',
    'institutional/SHORT_RULE_DRAFT.md',
    'institutional/SIGIL_DRAFT.md',
}
for md in ROOT.rglob('*.md'):
    rel=str(md.relative_to(ROOT))
    if rel.startswith('source/') or rel.startswith('build/') or rel in allowed_order_files: continue
    txt=md.read_text(encoding='utf-8',errors='ignore')
    if re.search(r'\bOrder of the Troth\b',txt): warnings.append(f"'Order of the Troth' found in working file: {rel}")

print('The Keeping Between Workbench validation')
for w in warnings: print('WARN:',w)
for e in errors: print('ERROR:',e)
if errors:
    print(f'FAILED with {len(errors)} error(s), {len(warnings)} warning(s).')
    sys.exit(1)
print(f'PASS with {len(warnings)} warning(s).')
