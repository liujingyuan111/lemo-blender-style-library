#!/usr/bin/env python3
"""Verify that every translated art rule is anchored in the pinned original."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import sys

ROOT=Path(__file__).resolve().parent.parent
spec=importlib.util.spec_from_file_location('style_contract_data',ROOT/'blender/lemo_style_guard/contracts.py')
contracts=importlib.util.module_from_spec(spec)
spec.loader.exec_module(contracts)


def main():
    errors=[];profiles=[]
    for path in sorted((ROOT/'blender/lemo_style_guard/profiles').glob('*/contract.json')):
        d=json.loads(path.read_text(encoding='utf-8'))
        try:contracts.validate_profile(d)
        except ValueError as e:errors.append(str(path.relative_to(ROOT))+': '+str(e));continue
        if d['style_id']!=path.parent.name:errors.append('Style identifier differs from folder')
        source=(ROOT/'source/lemo-opuscar'/d['source']['path']).resolve()
        if not source.is_relative_to(ROOT/'source/lemo-opuscar') or not source.is_file():
            errors.append(d['style_id']+': missing source');continue
        raw=source.read_bytes();text=raw.decode('utf-8')
        if hashlib.sha256(raw).hexdigest()!=d['source']['sha256']:
            errors.append(d['style_id']+': source hash mismatch')
        for rule in d['rules']:
            if rule['source_quote'] not in text:
                errors.append(d['style_id']+'/'+rule['id']+': quote not a contiguous original substring')
        if d['palette']['status'] in ('source_fixed','source_example'):
            source_hexes={h.upper() for h in re.findall(r'#[0-9A-Fa-f]{6}\b',text)}
            for color in d['palette'].get('colors',[]):
                if color['hex'].upper() not in source_hexes:
                    errors.append(d['style_id']+': colour is not in original STYLE.md: '+color['hex'])
        if not (path.parent/'RULES.md').is_file():errors.append(d['style_id']+': missing Chinese rule card')
        profiles.append({'style_id':d['style_id'],'rules':len(d['rules']),
                         'quotes_verified':len(d['rules']),'palette_provenance':d['palette']['status'],
                         'source_sha256':d['source']['sha256']})
    if len(profiles)!=8:errors.append('Expected exactly eight reviewed Blender contracts')
    forbidden={'.blend','.mp4','.mov','.wav','.mp3','.svg','.png','.jpg','.webp'}
    extras=[str(p.relative_to(ROOT)) for p in ROOT.rglob('*')
            if p.is_file() and '.git' not in p.parts and p.suffix.lower() in forbidden]
    if extras:errors.append('Visual/film assets must not be in the style-only source package: '+str(extras))
    report={'schema_id':'lemo-contract-validation/v1','status':'passed' if not errors else 'failed',
            'contracts':len(profiles),'rule_count':sum(p['rules'] for p in profiles),
            'profiles':profiles,'errors':errors,
            'scope':'Checks source identity, exact quote anchors and palette provenance. Semantic review remains documented by the extractors.'}
    (ROOT/'validation').mkdir(exist_ok=True)
    (ROOT/'validation/contracts_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return int(bool(errors))


if __name__=='__main__':sys.exit(main())
