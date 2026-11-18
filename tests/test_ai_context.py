"""Exercise the offline CLI against real source-backed style documents."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "tools/ai_context.py"
spec = importlib.util.spec_from_file_location("ai_context", CLI)
ai_context = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ai_context)
ADAPTED = {
    "spy-titles", "silhouette-rhythm", "shadow-puppet", "paper-lantern",
    "paper-popup", "backrooms", "white-model", "lowpoly-island",
}


def source_hashes():
    return {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (ROOT / "source").rglob("*") if p.is_file()}


class AIContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original_sources = source_hashes()

    @classmethod
    def tearDownClass(cls):
        if source_hashes() != cls.original_sources:
            raise AssertionError("The CLI changed preserved source files")

    def run_cli(self, *args, success=True, cwd=None):
        process = subprocess.run(
            [sys.executable, str(CLI), *args], cwd=cwd or ROOT,
            capture_output=True, text=True, encoding="utf-8",
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            timeout=20,
        )
        if success:
            self.assertEqual(process.returncode, 0, process.stderr)
            self.assertEqual(process.stderr, "")
        else:
            self.assertNotEqual(process.returncode, 0)
            self.assertEqual(process.stdout, "")
        return process

    def export(self, style_id, *extra):
        return json.loads(self.run_cli("export", style_id, "--format", "json", *extra).stdout)

    def test_catalog_and_blender_filter(self):
        all_styles = json.loads(self.run_cli("list", "--json").stdout)
        adapted = json.loads(self.run_cli("list", "--blender-only", "--json").stdout)
        self.assertEqual(all_styles["count"], 99)
        self.assertEqual(len({s["style_id"] for s in all_styles["styles"]}), 99)
        self.assertEqual(adapted["count"], 8)
        self.assertEqual({s["style_id"] for s in adapted["styles"]}, ADAPTED)
        self.assertTrue(all(s["blender_adapted"] for s in adapted["styles"]))

    def test_search_chinese_names_rules_and_original_text(self):
        chinese = json.loads(self.run_cli("search", "剪影", "--json").stdout)
        self.assertIn("spy-titles", {s["style_id"] for s in chinese["styles"]})
        rule = json.loads(self.run_cli("search", "四种主墨色", "--json").stdout)
        self.assertEqual([s["style_id"] for s in rule["styles"]], ["spy-titles"])
        self.assertIn("blender_contract", rule["styles"][0]["matched_in"])
        original = json.loads(self.run_cli("search", "flying white", "--json").stdout)
        self.assertIn("watercolor", {s["style_id"] for s in original["styles"]})
        self.assertIn("spy-titles", self.run_cli("search", "SPY-TITLES").stdout)
        self.assertEqual(json.loads(self.run_cli("search", "unmatchable_query_xyz_947", "--json").stdout)["count"], 0)
        self.run_cli("search", "   ", success=False)

    def test_all_eight_contracts_preserve_rules_and_provenance(self):
        total_rules = 0
        for style_id in sorted(ADAPTED):
            with self.subTest(style_id=style_id):
                context = self.export(style_id)
                contract = json.loads((ROOT / "blender/lemo_style_guard/profiles" / style_id / "contract.json").read_text())
                self.assertEqual(context["status"], "contract_available")
                self.assertTrue(context["blender_adapted"])
                self.assertFalse(context["original_style_automatically_reproduced"])
                for field in ("scope", "rules", "palette", "material_recipe", "not_automated"):
                    self.assertEqual(context[field], contract[field])
                self.assertTrue(all(r["id"].startswith(style_id + "-") and r["review"] == "manual" for r in context["rules"]))
                self.assertEqual(context["manual_review"]["status"], "not_performed")
                self.assertTrue(context["manual_review"]["required"])
                self.assertIn(context["source"]["commit"], context["source"]["url"])
                self.assertEqual(context["source"]["sha256"], contract["source"]["sha256"])
                self.assertEqual(context["license"]["id"], "CC-BY-NC-4.0")
                self.assertNotIn(str(ROOT), json.dumps(context))
                total_rules += len(context["rules"])
        self.assertEqual(total_rules, 150)

    def test_single_style_export_does_not_mix_other_contracts(self):
        context = self.export("spy-titles")
        self.assertEqual(len(context["rules"]), 18)
        self.assertNotIn("art_reference_markdown", context)
        self.assertEqual(context["palette"]["status"], "source_example")
        self.assertTrue(context["palette"]["editable"])
        output = self.run_cli("export", "spy-titles").stdout
        self.assertIn("required", output)
        self.assertIn("原文章节：3. Colour logic", output)
        self.assertIn("Blender 转译建议", output)
        self.assertIn("source_example", output)
        self.assertIn("尚未执行", output)
        self.assertIn("Lemo-Opuscar by Lemomo (LemoLab)", output)
        self.assertIn("https://creativecommons.org/licenses/by-nc/4.0/", output)
        self.assertIn("modifications", json.dumps(context))
        for other in ADAPTED - {"spy-titles"}:
            self.assertNotIn(other, output)
            self.assertNotIn(other, json.dumps(context))

    def test_reference_only_exports_original_art_without_fabricated_contract(self):
        context = self.export("watercolor")
        self.assertEqual(context["status"], "reference_only")
        self.assertFalse(context["blender_adapted"])
        for field in ("rules", "palette", "scope", "material_recipe", "not_automated"):
            self.assertNotIn(field, context)
        self.assertIn("## 3. Colour logic", context["art_reference_markdown"])
        self.assertIn("Paper is the white.", context["art_reference_markdown"])
        self.assertNotIn("../docs/", context["art_reference_markdown"])
        self.assertIn("未适配 Blender", " ".join(context["usage_boundaries"]))
        self.assertIn("未适配 Blender", self.run_cli("export", "watercolor").stdout)

    def test_all_ninety_one_reference_only_sources_export(self):
        catalog = ai_context.load_catalog()
        reference_ids = [s["style_id"] for s in catalog["styles"] if s["blender_status"] == "reference_only"]
        self.assertEqual(len(reference_ids), 91)
        for style_id in reference_ids:
            with self.subTest(style_id=style_id):
                context = ai_context.export_context(catalog, style_id)
                self.assertFalse(context["blender_adapted"])
                self.assertTrue(context["art_reference_markdown"])
                self.assertNotIn("rules", context)
                self.assertIn("Lemo-Opuscar by Lemomo (LemoLab)", context["attribution"])

    def test_special_authors_and_document_license_survive_json_export(self):
        for style_id, author in (("memphis-diorama", "EianLu"), ("crayon-world", "2nd1st")):
            with self.subTest(style_id=style_id):
                context = self.export(style_id)
                self.assertIn(author, context["attribution"])
                self.assertEqual(context["license"]["id"], "CC-BY-NC-4.0")
                self.assertIn(context["source"]["commit"], context["license"]["upstream_notice_url"])
                self.assertTrue(context["modifications"])

    def test_invalid_ids_and_internal_path_traversal_fail(self):
        for style_id in ("../../source/ORIGIN", "/tmp/watercolor", "..", "SPY-TITLES", "unknown-style", "spy-titles/../backrooms", "spy-titles\\backrooms"):
            with self.subTest(style_id=style_id):
                self.run_cli("export", style_id, success=False)
        for relative in ("../outside.json", "/etc/passwd", "catalog/../../outside", "catalog\\styles.json"):
            with self.subTest(relative=relative):
                with self.assertRaises(ai_context.ContextError):
                    ai_context.repository_file(relative)

    def test_export_from_another_working_directory_and_refuse_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "context.json"
            expected = self.run_cli("export", "spy-titles", "--format", "json", cwd=directory).stdout
            written = self.run_cli("export", "spy-titles", "--format", "json", "--output", str(path), cwd=directory)
            self.assertEqual(written.stdout, "")
            self.assertEqual(path.read_text(encoding="utf-8"), expected)
            error = self.run_cli("export", "backrooms", "--output", str(path), success=False)
            self.assertIn("refusing to overwrite", error.stderr)
            self.assertEqual(path.read_text(encoding="utf-8"), expected)
            link = Path(directory) / "link.md"
            link.symlink_to(path)
            self.run_cli("export", "backrooms", "--output", str(link), success=False)
            self.assertEqual(path.read_text(encoding="utf-8"), expected)
            missing = Path(directory) / "missing" / "context.md"
            self.run_cli("export", "backrooms", "--output", str(missing), success=False)
            self.assertFalse(missing.parent.exists())

    def test_output_cannot_modify_preserved_source_tree(self):
        destination = ROOT / "source" / "ai-context-must-not-be-created.md"
        self.run_cli("export", "spy-titles", "--output", str(destination), success=False)
        self.assertFalse(destination.exists())


if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(AIContextTests))
    report = {
        "schema_id": "lemo-ai-context-validation/v1",
        "status": "passed" if result.wasSuccessful() else "failed",
        "tests_run": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "catalog_styles": 99,
        "adapted_exports": 8,
        "reference_only_exports": 91,
        "adapted_rules": 150,
        "checks": [
            "real CLI list, filtered list and Chinese/original-text search",
            "all eight Blender contracts preserve source, strength, palette provenance and manual review",
            "all 91 reference-only styles preserve selected original sections and deny Blender adaptation",
            "single-style boundary, original attribution and document license",
            "invalid identifiers and internal path traversal refused",
            "new-file output, existing-file and symlink refusal, no implicit parent creation",
            "preserved source directory is never modified",
        ],
        "scope": "Offline standard-library CLI and document checks; no Blender rendering or visual art acceptance is claimed.",
    }
    (ROOT / "validation/ai_context_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    raise SystemExit(not result.wasSuccessful())
