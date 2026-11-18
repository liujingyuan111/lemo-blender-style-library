"""Read source-backed art contracts. This module creates no Blender content."""
from pathlib import Path
import hashlib
import json
import re

PROFILE_ROOT = Path(__file__).resolve().parent / 'profiles'
UPSTREAM_COMMIT = '00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4'
CATEGORIES = {
    'palette':'配色', 'material':'材质', 'shape':'轮廓与造型',
    'composition':'构图', 'lighting':'光影', 'camera':'摄影机',
    'typography':'文字', 'consistency':'一致性',
}
LEVELS = {'required':'必须','forbidden':'禁止','recommended':'建议',
          'optional':'可选','example':'示例'}


def load_profile(style_id):
    if not isinstance(style_id, str) or not re.fullmatch(r'[a-z][a-z0-9-]{1,63}', style_id):
        raise ValueError('Invalid style identifier')
    path = PROFILE_ROOT / style_id / 'contract.json'
    if not path.is_file():
        raise ValueError('No Blender contract for style: ' + style_id)
    raw = path.read_bytes()
    data = json.loads(raw)
    validate_profile(data)
    return data, hashlib.sha256(raw).hexdigest()


def validate_profile(data):
    if data.get('schema_id') != 'lemo-blender-style/v1':
        raise ValueError('Unsupported style contract schema')
    if data.get('source', {}).get('commit') != UPSTREAM_COMMIT:
        raise ValueError('Unexpected upstream version')
    ids = set()
    for rule in data.get('rules', []):
        if not rule.get('id') or rule['id'] in ids:
            raise ValueError('Missing or duplicated rule id')
        ids.add(rule['id'])
        if rule.get('category') not in CATEGORIES or rule.get('level') not in LEVELS:
            raise ValueError('Unknown art rule category or level')
        if rule.get('review') != 'manual':
            raise ValueError('Art rules require explicit manual review')
        for field in ('rule_zh','source_section','source_quote','blender_translation'):
            if not rule.get(field):
                raise ValueError('Missing rule field: ' + field)
    if not ids:
        raise ValueError('Empty style contract')
    palette = data.get('palette', {})
    if palette.get('status') not in ('source_fixed','source_example','adapter_starting_point'):
        raise ValueError('Palette provenance is required')
    for color in palette.get('colors', []):
        if not re.fullmatch(r'#[0-9a-fA-F]{6}', color.get('hex', '')):
            raise ValueError('Invalid palette colour')
    return data


def list_profiles():
    return [load_profile(p.parent.name)[0]
            for p in sorted(PROFILE_ROOT.glob('*/contract.json'))]


def source_url(data):
    source = data['source']
    return source['repo'].removesuffix('.git').rstrip('/') + '/blob/' + source['commit'] + '/' + source['path']


def rule_card(data):
    out = ['# ' + data['title_zh'], '',
           '原始风格：' + data['title_original'],
           '原文：' + source_url(data),
           '固定提交：' + data['source']['commit'], '',
           '本页用于本场景的美术制作与逐条验收。原文要求与Blender转译建议分列。', '']
    for category, title in CATEGORIES.items():
        rules = [r for r in data['rules'] if r['category'] == category]
        if not rules:
            continue
        out += ['## ' + title, '']
        for rule in rules:
            out += ['### [' + LEVELS[rule['level']] + '] ' + rule['id'],
                    rule['rule_zh'], '',
                    '原文依据（' + rule['source_section'] + '）：',
                    '> ' + rule['source_quote'], '',
                    'Blender转译建议：' + rule['blender_translation'], '']
    out += ['## 配色来源', '', data['palette']['status'], str(data['palette'].get('notes','')), '',
            '## 仍需人工判断', '']
    out += ['- ' + s for s in data.get('not_automated', [])]
    a = data.get('attribution', {})
    out += ['', '## 出处与许可', '',
            a.get('original_author', 'Lemo-Opuscar by Lemomo (LemoLab)'),
            'CC BY-NC 4.0 — https://creativecommons.org/licenses/by-nc/4.0/',
            a.get('modifications', '中文整理与 Blender 转译建议。'),
            a.get('additional_film_permission', ''),
            '上游完整条款：' + a.get('upstream_terms_url', data['source']['repo'] + '/blob/' + data['source']['commit'] + '/LICENSE')]
    return '\n'.join(out) + '\n'


def srgb_channel_to_linear(value):
    return value / 12.92 if value <= .04045 else ((value + .055) / 1.055) ** 2.4


def hex_to_linear_rgba(hex_color):
    if not re.fullmatch(r'#[0-9a-fA-F]{6}', hex_color):
        raise ValueError('Expected #RRGGBB')
    return tuple(srgb_channel_to_linear(int(hex_color[i:i+2],16)/255)
                 for i in (1,3,5)) + (1.0,)
