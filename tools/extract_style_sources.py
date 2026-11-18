#!/usr/bin/env python3
"""Build the style-only reference layer without importing films or demo code.

Initial import:
  python tools/extract_style_sources.py --upstream /path/to/pinned/lemo-opuscar
      --reference-catalog /path/to/upstream_styles.json
      --reference-inventory /path/to/code_inventory.json

After import, rerun without arguments to regenerate the art excerpts and catalog
from the byte-preserved source/ tree. This script never executes upstream code.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
REPOSITORY = 'https://github.com/lemomo-ai/lemo-opuscar'
COMMIT = '00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4'
EXPECTED_STYLE_COUNT = 99
FIRST_CONTRACTS = {
    'spy-titles', 'shadow-puppet', 'paper-lantern', 'paper-popup',
    'silhouette-rhythm', 'backrooms', 'white-model', 'lowpoly-island',
}
HEADING = re.compile(r'^## (\d+)\. ([^\r\n]+)\r?$', re.MULTILINE)
STANDARD_HEADINGS = [
    'Essence, and what it is not', 'Materials & rendering', 'Colour logic',
    'Type & subtitles', 'Motion quality', 'Camera grammar', 'Sound palette',
    'Native moves', 'Pitfalls of the medium', 'Engine', 'Variation space',
]
# Title-based selection is necessary: in several documentary styles section 9
# is asset procurement or footage, and in Bauhaus section 9 is a move menu.
ART_TITLE_PREFIXES = (
    'Essence,', 'Materials & rendering', 'Colour', 'Type', 'Camera',
    'Frame and layout', 'Caption card', 'Graphics', 'Grade and image quality',
    'Picture layer and grade', 'Shot & layout grammar', 'Pitfalls',
    'Consistency checks',
)
EXTRACTION_POLICY = {
    'selected': 'Whole numbered source sections whose headings name visual identity, rendering/material, colour, type, framing/camera, visual pitfalls or consistency.',
    'excluded': 'Sound palette, native-move/story menus, variation plots, engine/code instructions, character/image-generation workflows, footage/source procurement, and editing/motion sections are not independently selected.',
    'preservation': 'Selected section text is copied verbatim. Mixed reminders inside a selected source section remain source text, not Blender rules.',
    'blender': 'Art excerpts are source references only. Only separately reviewed contract.json files enter the Blender adapter.',
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def preserve_file(source: Path, destination: Path, expected: dict, upstream_path: str) -> dict:
    if not source.is_file() or source.is_symlink():
        raise ValueError('Expected a regular source file: ' + str(source))
    payload = source.read_bytes()
    actual_sha = digest(payload)
    actual_blob = hashlib.sha1(b'blob ' + str(len(payload)).encode('ascii') + b'\0' + payload).hexdigest()
    if actual_sha != expected['sha256'] or actual_blob != expected['git_blob']:
        raise ValueError('Source differs from pinned file identity: ' + upstream_path)
    if destination.exists() and destination.read_bytes() != payload:
        raise ValueError('Refusing to overwrite changed source bytes: ' + str(destination))
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.resolve() != destination.resolve():
        destination.write_bytes(payload)
    if destination.read_bytes() != payload:
        raise ValueError('Copied source bytes differ: ' + str(destination))
    return {'path': str(destination.relative_to(ROOT)), 'upstream_path': upstream_path,
            'sha256': actual_sha, 'git_blob': actual_blob, 'bytes': len(payload)}


def section_records(payload: bytes) -> tuple[list[dict], bool]:
    text = payload.decode('utf-8')
    matches = list(HEADING.finditer(text))
    if not matches:
        return [], False
    records = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        section = text[match.start():end]
        title = match.group(2)
        selected = title.startswith(ART_TITLE_PREFIXES)
        records.append({
            'number': int(match.group(1)), 'title': title,
            'source_line_start': text.count('\n', 0, match.start()) + 1,
            'source_line_end': text.count('\n', 0, end),
            'selected': selected,
            'selection_reason': 'art_heading_match' if selected else 'outside_visual_reference_scope',
            'sha256': digest(section.encode('utf-8')),
            'text': section,
            'contains_fenced_source_formula': '```' in section,
        })
    standard = [r['title'] for r in records] == STANDARD_HEADINGS
    return records, standard


def source_credit(slug: str) -> str:
    if slug == 'memphis-diorama':
        return 'Memphis Diorama by EianLu, in Lemo-Opuscar by Lemomo (LemoLab)'
    if slug == 'crayon-world':
        return 'Crayon World 3D by 2nd1st, in Lemo-Opuscar by Lemomo (LemoLab)'
    return 'Lemo-Opuscar by Lemomo (LemoLab)'


def build(upstream: Path, reference_catalog: Path | None, reference_inventory: Path | None, contracts_ready: bool | None) -> dict:
    source_root = ROOT / 'source/lemo-opuscar'
    origin_path = ROOT / 'source/ORIGIN.json'
    if contracts_ready is None:
        existing_catalog = ROOT / 'catalog/styles.json'
        if existing_catalog.is_file():
            prior = json.loads(existing_catalog.read_text(encoding='utf-8'))
            statuses = {s['style_id']: s.get('blender_status') for s in prior['styles']}
            contracts_ready = all(statuses.get(slug) == 'contract_available' for slug in FIRST_CONTRACTS)
        else:
            contracts_ready = False
    if reference_inventory:
        identity = json.loads(reference_inventory.read_text(encoding='utf-8'))
        if identity.get('upstream_commit') != COMMIT:
            raise ValueError('Reference inventory is from a different commit')
        expected_files = {f['upstream_path']: f for f in identity['files']}
    elif upstream.resolve() == source_root.resolve() and origin_path.is_file():
        identity = json.loads(origin_path.read_text(encoding='utf-8'))
        if identity.get('commit') != COMMIT:
            raise ValueError('Source archive is from a different commit')
        expected_files = {f['upstream_path']: f for f in identity['source_files']}
    else:
        raise ValueError('Initial import requires the pinned --reference-inventory; later reruns use source/ORIGIN.json')
    metadata_paths = sorted((upstream / 'styles').glob('*/style.json'))
    metadata = {}
    for path in metadata_paths:
        slug = path.parent.name
        if slug == '_template':
            continue
        if not re.fullmatch(r'[a-z][a-z0-9-]*', slug):
            raise ValueError('Unexpected style directory: ' + slug)
        record = json.loads(path.read_text(encoding='utf-8'))
        if record.get('slug') != slug:
            raise ValueError('Directory / metadata slug mismatch: ' + slug)
        metadata[slug] = record
    if len(metadata) != EXPECTED_STYLE_COUNT:
        raise ValueError(f'Expected 99 distinct styles, found {len(metadata)}')
    if reference_catalog:
        source_catalog = json.loads(reference_catalog.read_text(encoding='utf-8'))
        if source_catalog.get('upstream_commit') != COMMIT:
            raise ValueError('Reference catalog is from a different commit')
        source_items = source_catalog['styles']
        if set(metadata) != {s['slug'] for s in source_items}:
            raise ValueError('Style set differs from the pinned 99-style catalog')
        slugs = [s['slug'] for s in source_items]
    else:
        slugs = sorted(metadata, key=lambda slug: (int(metadata[slug].get('num', 9999)), slug))

    source_files = []
    for relative in [Path('LICENSE'), Path('REUSE.toml')] + [p.relative_to(upstream) for p in sorted((upstream / 'LICENSES').glob('*.txt'))]:
        source_files.append(preserve_file(upstream / relative, source_root / relative, expected_files[relative.as_posix()], relative.as_posix()))

    styles, extracted, unusual = [], [], []
    for slug in slugs:
        item = metadata[slug]
        original_path = Path('styles') / slug / 'STYLE.md'
        meta_path = Path('styles') / slug / 'style.json'
        original = preserve_file(upstream / original_path, source_root / original_path, expected_files[original_path.as_posix()], original_path.as_posix())
        meta_copy = preserve_file(upstream / meta_path, source_root / meta_path, expected_files[meta_path.as_posix()], meta_path.as_posix())
        source_files += [original, meta_copy]
        payload = (source_root / original_path).read_bytes()
        sections, standard = section_records(payload)
        selected = [section for section in sections if section['selected']]
        status = 'extracted' if selected else 'not_extracted'
        if not standard:
            unusual.append(slug)
        excerpt_path = ROOT / 'art_rules' / (slug + '.md')
        original_url = f'{REPOSITORY}/blob/{COMMIT}/{original_path.as_posix()}'
        header = (
            f"# {item['cn']} · 原文美术章节\n\n"
            f"来源：{source_credit(slug)}。原文：[STYLE.md]({original_url})。\n\n"
            f"固定提交：`{COMMIT}`。原文 SHA-256：`{original['sha256']}`。\n\n"
            "本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。"
            "原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。"
            "某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。\n\n"
            "文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。"
            "改动：只增加此说明并选择章节，所选原文未改写。\n\n"
            "保留章节：" + ('、'.join(str(s['number']) for s in selected) if selected else '无；结构待人工处理') + "。\n\n---\n\n"
        )
        body = ''.join(section['text'] for section in selected)
        excerpt_path.parent.mkdir(parents=True, exist_ok=True)
        excerpt_path.write_text(header + body, encoding='utf-8', newline='')
        # Verify the written extraction against every exact source span.
        written = excerpt_path.read_bytes()
        cursor = len(header.encode('utf-8'))
        for section in selected:
            section_bytes = section['text'].encode('utf-8')
            if written[cursor:cursor + len(section_bytes)] != section_bytes:
                raise ValueError('Selected source section changed: ' + slug)
            cursor += len(section_bytes)
        if cursor != len(written):
            raise ValueError('Unexpected bytes after selected source sections: ' + slug)
        selected_metadata = [{k: v for k, v in s.items() if k != 'text'} for s in selected]
        excluded_metadata = [{'number': s['number'], 'title': s['title'], 'reason': s['selection_reason']} for s in sections if not s['selected']]
        first_batch = slug in FIRST_CONTRACTS
        contract_path = f'blender/lemo_style_guard/profiles/{slug}/contract.json' if first_batch else None
        if contracts_ready and first_batch and not (ROOT / contract_path).is_file():
            raise ValueError('Requested ready status but contract missing: ' + slug)
        blender_status = ('contract_available' if contracts_ready else 'contract_in_preparation') if first_batch else 'reference_only'
        styles.append({
            'style_id': slug, 'slug': slug, 'title_zh': item['cn'], 'title_original': item['en'],
            'category_zh': item['category_cn'], 'category_original': item['category_en'],
            'source_path': original['path'], 'source_sha256': original['sha256'], 'source_url': original_url,
            'metadata_path': meta_copy['path'], 'metadata_sha256': meta_copy['sha256'],
            'source_attribution': source_credit(slug), 'document_license': 'CC-BY-NC-4.0',
            'metadata_license': 'MIT',
            'art_rules_path': str(excerpt_path.relative_to(ROOT)), 'art_extraction_status': status,
            'selected_sections': [{'number': s['number'], 'title': s['title']} for s in selected],
            'blender_status': blender_status, 'blender_contract_path': contract_path,
            'original_style_automatically_reproduced': False,
        })
        extracted.append({
            'style_id': slug, 'status': status, 'standard_section_layout': standard,
            'source_sha256': original['sha256'], 'excerpt_path': str(excerpt_path.relative_to(ROOT)),
            'excerpt_sha256': digest(written), 'selected_sections': selected_metadata,
            'excluded_sections': excluded_metadata,
        })

    allowed_sources = {item['path'] for item in source_files}
    actual_sources = {str(p.relative_to(ROOT)) for p in source_root.rglob('*') if p.is_file()}
    extras = sorted(actual_sources - allowed_sources)
    if extras:
        raise ValueError('Unexpected files in the style-only source tree: ' + ', '.join(extras))
    catalog = {
        'schema_id': 'lemo-style-reference-catalog/v1', 'source_repository': REPOSITORY,
        'source_commit': COMMIT, 'style_count': len(styles),
        'first_blender_contract_count': len(FIRST_CONTRACTS),
        'source_only_count': len(styles) - len(FIRST_CONTRACTS),
        'extraction_policy': EXTRACTION_POLICY, 'styles': styles,
    }
    write_json(ROOT / 'catalog/styles.json', catalog)
    report = {
        'schema_id': 'lemo-style-source-validation/v1', 'status': 'passed',
        'source_repository': REPOSITORY, 'source_commit': COMMIT,
        'style_count': len(styles), 'source_style_documents': len(styles),
        'source_metadata_files': len(styles), 'source_files_total': len(source_files),
        'source_bytes': sum(f['bytes'] for f in source_files),
        'source_files_sha256_verified': len(source_files),
        'source_files_git_blob_verified': len(source_files),
        'art_excerpts': len(extracted),
        'not_extracted': [s['style_id'] for s in extracted if s['status'] != 'extracted'],
        'nonstandard_section_layouts': unusual,
        'all_selected_sections_byte_verified': True,
        'extraction_policy': EXTRACTION_POLICY,
        'copied_demo_files': 0, 'copied_upstream_implementation_files': 0, 'copied_media_or_assets': 0,
        'not_claimed': ['99 Blender-native implementations', 'automatic aesthetic validation', 'upstream demo execution'],
        'source_files': source_files, 'art_section_coverage': extracted,
    }
    write_json(ROOT / 'validation/source_report.json', report)
    write_json(ROOT / 'source/ORIGIN.json', {
        'repository': REPOSITORY, 'commit': COMMIT,
        'preserved': '99 STYLE.md, 99 style.json, root LICENSE, REUSE.toml and LICENSES/*.txt only',
        'unchanged_original_bytes': True,
        'source_files': source_files,
        'not_imported': ['DEMO.md', 'demo code', 'CREDITS', 'footage', 'fonts', 'audio', 'models', 'textures', 'our earlier studies or modules'],
        'source_document_links': 'Original STYLE.md may contain links to upstream DEMO.md or engine files. Those files are deliberately absent; open the pinned GitHub source link to inspect that context.',
        'raw_metadata': 'Original style.json may name the upstream demo. These reference metadata fields are not imported into Blender or adopted as project content.',
    })
    return {key: report[key] for key in ['status', 'style_count', 'source_files_total', 'source_bytes', 'art_excerpts', 'not_extracted', 'nonstandard_section_layouts', 'all_selected_sections_byte_verified']}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--upstream', type=Path, default=ROOT / 'source/lemo-opuscar')
    parser.add_argument('--reference-catalog', type=Path)
    parser.add_argument('--reference-inventory', type=Path)
    parser.add_argument('--contracts-ready', action='store_true', default=None, help='Mark the eight existing reviewed contracts as available; does not claim automatic visual validation. Omit to retain the existing catalog status.')
    args = parser.parse_args()
    print(json.dumps(build(args.upstream.resolve(), args.reference_catalog, args.reference_inventory, args.contracts_ready), ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as error:
        print('Style-only extraction failed: ' + str(error), file=sys.stderr)
        sys.exit(2)
