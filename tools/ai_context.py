#!/usr/bin/env python3
"""List, search and export one source-backed style for a local AI, offline.

The program uses only the Python standard library. It reads the checked-in
catalog and style documents; it neither imports Blender nor executes source
examples. Exported art documents retain their document license.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
STYLE_ID = re.compile(r"[a-z][a-z0-9-]{1,63}\Z")
SECTION = re.compile(r"^## (\d+)\. ([^\r\n]+)\r?$", re.MULTILINE)
LEVELS = {
    "required": "必须", "forbidden": "禁止", "recommended": "建议",
    "optional": "可选", "example": "示例",
}
LICENSE_URL = "https://creativecommons.org/licenses/by-nc/4.0/"


class ContextError(ValueError):
    """An invalid request or an inconsistent repository document."""


def repository_file(relative: str) -> Path:
    """Resolve catalog paths without allowing traversal or symlink escapes."""
    if not isinstance(relative, str) or "\\" in relative:
        raise ContextError("Invalid repository-relative path")
    path = PurePosixPath(relative)
    if path.is_absolute() or ".." in path.parts:
        raise ContextError("Repository path traversal is not allowed")
    resolved = (ROOT / path).resolve()
    if not resolved.is_relative_to(ROOT) or not resolved.is_file():
        raise ContextError("Missing or unsafe repository file: " + relative)
    return resolved


def read_json(relative: str) -> dict:
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))


def load_catalog() -> dict:
    catalog = read_json("catalog/styles.json")
    ids = [style["style_id"] for style in catalog["styles"]]
    if len(ids) != len(set(ids)) or any(not STYLE_ID.fullmatch(s) for s in ids):
        raise ContextError("Invalid or duplicate style identifier in catalog")
    return catalog


def selected_style(catalog: dict, style_id: str) -> dict:
    if not STYLE_ID.fullmatch(style_id):
        raise ContextError("Invalid style_id; use an identifier from list")
    for style in catalog["styles"]:
        if style["style_id"] == style_id:
            return style
    raise ContextError("Unknown style_id: " + style_id + "; use list or search")


def summary(style: dict) -> dict:
    return {
        "style_id": style["style_id"],
        "title_zh": style["title_zh"],
        "title_original": style["title_original"],
        "category_zh": style["category_zh"],
        "category_original": style["category_original"],
        "status": style["blender_status"],
        "blender_adapted": style["blender_status"] == "contract_available",
    }


def search_styles(catalog: dict, query: str) -> list[dict]:
    needle = query.strip().casefold()
    if not needle:
        raise ContextError("Search query must not be empty")
    results = []
    for style in catalog["styles"]:
        fields = {
            "metadata": "\n".join(str(v) for v in summary(style).values()),
            "art_reference": repository_file(style["art_rules_path"]).read_text(encoding="utf-8"),
        }
        if style["blender_contract_path"]:
            fields["blender_contract"] = repository_file(
                style["blender_contract_path"]
            ).read_text(encoding="utf-8")
        matches = [field for field, value in fields.items() if needle in value.casefold()]
        if matches:
            results.append({**summary(style), "matched_in": matches})
    return results


def source_sections(source_text: str) -> dict[tuple[int, str], str]:
    matches = list(SECTION.finditer(source_text))
    return {
        (int(match.group(1)), match.group(2)): source_text[
            match.start():matches[index + 1].start() if index + 1 < len(matches) else len(source_text)
        ]
        for index, match in enumerate(matches)
    }


def art_reference(style: dict, source_text: str) -> str:
    sections = source_sections(source_text)
    try:
        original = "".join(
            sections[(s["number"], s["title"])] for s in style["selected_sections"]
        )
    except KeyError as error:
        raise ContextError("Selected art section is absent from the pinned source") from error
    stored = repository_file(style["art_rules_path"]).read_bytes().decode("utf-8")
    separator = "\n---\n\n"
    if not original or separator not in stored or stored.split(separator, 1)[1] != original:
        raise ContextError("Art excerpt differs from the selected original sections")
    return original


def export_context(catalog: dict, style_id: str) -> dict:
    style = selected_style(catalog, style_id)
    raw_source = repository_file(style["source_path"]).read_bytes()
    source_hash = hashlib.sha256(raw_source).hexdigest()
    if source_hash != style["source_sha256"]:
        raise ContextError("Original source hash mismatch: " + style_id)
    source_text = raw_source.decode("utf-8")
    source_path = "styles/" + style_id + "/STYLE.md"
    repository = catalog["source_repository"].rstrip("/")
    commit = catalog["source_commit"]
    pinned_url = repository + "/blob/" + commit + "/" + source_path
    if style["source_url"] != pinned_url:
        raise ContextError("Source URL differs from the catalog version")
    status = style["blender_status"]
    if status not in ("contract_available", "reference_only"):
        raise ContextError("Unsupported Blender adaptation status")
    if style["document_license"] != "CC-BY-NC-4.0":
        raise ContextError("Unsupported art document license")
    adapted = status == "contract_available"
    context = {
        "schema_id": "lemo-ai-style-context/v1",
        "style_id": style_id,
        "title_zh": style["title_zh"],
        "title_original": style["title_original"],
        "status": status,
        "blender_adapted": adapted,
        "original_style_automatically_reproduced": False,
        "source": {
            "repository": repository, "commit": commit, "path": source_path,
            "url": pinned_url, "sha256": source_hash,
            "selected_art_sections": style["selected_sections"],
        },
        "attribution": style["source_attribution"],
        "license": {
            "id": "CC-BY-NC-4.0",
            "name": "Creative Commons Attribution-NonCommercial 4.0 International",
            "url": LICENSE_URL,
            "scope": "本次导出的原文摘录、中文整理与 Blender 转译文档；JSON 格式不改变文档许可。",
            "upstream_notice_url": repository + "/blob/" + commit + "/LICENSE",
            "additional_permission_notice": "上游对自有／客户影片制作另有额外许可，范围与条件见固定版本的 LICENSE。",
        },
        "modifications": [
            "从固定版本选择美术章节，加入来源、状态与使用边界说明；保留所选原文，不改动 source 文件。",
            *(["将已审阅的美术约束整理为中文规则，分列强度、原文引句与章节；Blender 建议为本库转译，不是上游原生 Blender 实现。"] if adapted else []),
            "以单一风格上下文重新编排；未增加故事、场景、影片、资产或动效模块。",
        ],
        "usage_boundaries": [
            "本上下文只选择 " + style_id + "；不得把其他风格的约束自动合并进来。",
            "保留原文的必须、禁止、建议、可选与示例强度；示例数值及 HEX 不自动升级为硬限制。",
            "原文资料作为美术参考；其中的代码或流程文字不在导出时执行。",
            "导出与规则读取成功不等于美术通过；构图、轮廓、材质与光影需要对照实际画面人工验收。",
            "只有用户明确要求制作具体项目时，才在独立项目中应用这些约束。",
        ],
        "manual_review": {"required": True, "status": "not_performed", "basis": "实际输出画面与所选原文／规则逐条对照"},
        "reference_files": {"source": style["source_path"], "art_rules": style["art_rules_path"]},
    }
    if adapted:
        contract = read_json(style["blender_contract_path"])
        expected_source = {"repo": repository, "commit": commit, "path": source_path, "sha256": source_hash}
        if contract["style_id"] != style_id or contract["source"] != expected_source:
            raise ContextError("Blender contract identity differs from the selected source")
        rules = contract["rules"]
        if not rules:
            raise ContextError("Blender contract has no rules")
        for rule in rules:
            if not rule["id"].startswith(style_id + "-") or rule["level"] not in LEVELS:
                raise ContextError("Blender rule identity or strength is invalid")
            if rule["review"] != "manual" or not rule["source_quote"] or rule["source_quote"] not in source_text:
                raise ContextError("Blender rule must retain its original quote and manual review")
        for key in ("scope", "rules", "palette", "material_recipe", "not_automated"):
            context[key] = contract[key]
        context["reference_files"]["contract"] = style["blender_contract_path"]
    else:
        if style["blender_contract_path"] is not None:
            raise ContextError("Reference-only style must not claim a Blender contract")
        context["usage_boundaries"].insert(0, "此风格未适配 Blender，没有已审阅的 Blender 中文合同；不能声称材质、场景或参数已实现。")
        context["art_reference_markdown"] = art_reference(style, source_text)
    return context


def markdown(context: dict) -> str:
    source = context["source"]
    license_info = context["license"]
    lines = [
        "# " + context["title_zh"] + " · 单风格 AI 上下文", "",
        "- 风格 ID：`" + context["style_id"] + "`",
        "- 原名：" + context["title_original"],
        "- 状态：`" + context["status"] + "`；" + ("已有 Blender 约束合同。" if context["blender_adapted"] else "未适配 Blender，无已审阅的 Blender 中文合同。"),
        "- 自动复现：否；人工美术验收：尚未执行。", "",
        "## 来源、署名与许可", "",
        "署名：" + context["attribution"], "",
        "原仓库：[Lemo-Opuscar](" + source["repository"] + ")；固定原文：[STYLE.md](" + source["url"] + ")。", "",
        "固定提交：`" + source["commit"] + "`；原文 SHA-256：`" + source["sha256"] + "`。", "",
        "文档许可：[CC BY-NC 4.0](" + license_info["url"] + ")。" + license_info["scope"], "",
        license_info["additional_permission_notice"] + " [上游许可原文](" + license_info["upstream_notice_url"] + ")。", "",
        "改动说明：", "",
        *["- " + item for item in context["modifications"]], "",
        "## 使用边界", "",
        *["- " + item for item in context["usage_boundaries"]], "",
    ]
    if context["blender_adapted"]:
        lines += ["## Blender 转译范围", ""]
        lines += ["- " + key + "：" + value for key, value in context["scope"].items()]
        lines += ["", "## 中文美术规则与原文依据", "", "规则强度保留为 required／forbidden／recommended／optional／example；Blender 转译建议与原文分列。", ""]
        for rule in context["rules"]:
            lines += [
                "### " + rule["id"] + " · " + LEVELS[rule["level"]] + " (`" + rule["level"] + "`)", "",
                "类别：`" + rule["category"] + "`；验收：人工 (`" + rule["review"] + "`)。", "",
                rule["rule_zh"], "",
                "原文章节：" + rule["source_section"], "",
                *["> " + line for line in rule["source_quote"].splitlines()], "",
                "Blender 转译建议：" + rule["blender_translation"], "",
            ]
        palette = context["palette"]
        lines += ["## 色板来源", "", "来源状态：`" + palette["status"] + "`；允许编辑：" + ("是" if palette.get("editable") else "否") + "。", "", palette.get("notes", ""), ""]
        if palette["colors"]:
            lines += ["| 名称 | HEX | 角色 |", "| --- | --- | --- |"]
            lines += ["| " + " | ".join(str(color.get(key, "")).replace("|", "\\|") for key in ("name", "hex", "role")) + " |" for color in palette["colors"]]
            lines += [""]
        else:
            lines += ["该合同未列出 HEX 色值；本导出不新增色板。", ""]
        recipe = context["material_recipe"]
        lines += ["## 材质实施起点（本库建议）", ""]
        lines += ["- " + key + "：" + str(value) for key, value in recipe.items()]
        lines += ["", "## 必须对照实际画面人工确认", ""]
        lines += ["- " + item for item in context["not_automated"]]
        lines += [""]
    else:
        lines += ["## 原文美术章节（参考资料）", "", "以下保留所选原文章节和措辞，尚未形成 Blender 约束合同。", "", context["art_reference_markdown"].rstrip(), ""]
    lines += ["## 仓库内原始文件", ""]
    lines += ["- " + key + "：`" + value + "`" for key, value in context["reference_files"].items()]
    return "\n".join(lines) + "\n"


def json_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def write_export(destination: str, text: str) -> None:
    path = Path(destination).expanduser()
    resolved = path.resolve()
    if resolved.is_relative_to((ROOT / "source").resolve()):
        raise ContextError("Export cannot write inside the preserved source directory")
    if not path.parent.is_dir():
        raise ContextError("Output parent directory must already exist")
    try:
        with path.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
    except FileExistsError as error:
        raise ContextError("Output already exists; refusing to overwrite") from error


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    listing = commands.add_parser("list", help="List available style identifiers")
    listing.add_argument("--blender-only", action="store_true", help="Only styles with a reviewed Blender contract")
    listing.add_argument("--json", action="store_true", help="Emit a JSON object with a styles array")
    searching = commands.add_parser("search", help="Search names, Chinese contracts and original art excerpts")
    searching.add_argument("query")
    searching.add_argument("--json", action="store_true")
    exporting = commands.add_parser("export", help="Export exactly one style; default: Markdown on stdout")
    exporting.add_argument("style_id")
    exporting.add_argument("--format", choices=("md", "json"), default="md")
    exporting.add_argument("--output", help="Create a new UTF-8 file; parent must exist; existing paths are refused")
    args = parser.parse_args(argv)
    try:
        catalog = load_catalog()
        if args.command == "export":
            context = export_context(catalog, args.style_id)
            output = json_text(context) if args.format == "json" else markdown(context)
            if args.output:
                write_export(args.output, output)
            else:
                sys.stdout.write(output)
        else:
            if args.command == "search":
                styles = search_styles(catalog, args.query)
            else:
                styles = [summary(s) for s in catalog["styles"] if not args.blender_only or s["blender_status"] == "contract_available"]
            if args.json:
                result = {"schema_id": "lemo-ai-style-list/v1", "count": len(styles), "source_commit": catalog["source_commit"], "styles": styles}
                if args.command == "search":
                    result["query"] = args.query
                sys.stdout.write(json_text(result))
            else:
                sys.stdout.write("style_id\t中文名称\tBlender 状态\n")
                for style in styles:
                    sys.stdout.write("\t".join(style[key] for key in ("style_id", "title_zh", "status")) + "\n")
                sys.stdout.write(str(len(styles)) + " style(s)\n")
        return 0
    except (ContextError, OSError, UnicodeError, KeyError, TypeError, json.JSONDecodeError) as error:
        # Do not put absolute workspace paths or stack traces in generated context.
        message = str(error) if isinstance(error, ContextError) else "Unable to read or write the requested repository data (" + type(error).__name__ + ")"
        parser.error(message)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
