import csv
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "ai-work-hub-deep-research" / "scripts"
spec = importlib.util.spec_from_file_location("research_validation", SCRIPTS / "validate_research.py")
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)


class ResearchWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def run_script(self, script, *args):
        return subprocess.run([sys.executable, str(SCRIPTS / script), *map(str, args)], capture_output=True, text=True)

    def init(self, *args):
        return self.run_script("init_deep_research.py", "--workspace-root", self.root,
                               "--industry", "Example", "--date", "2026-01-01", *args)

    def test_minimal_initializer_and_no_overwrite(self):
        self.assertEqual(self.init().returncode, 0)
        files = [p for p in self.root.rglob("*") if p.is_file()]
        self.assertEqual(sorted(p.suffix for p in files), [".json", ".md"])
        state = json.loads(next(self.root.rglob("*.json")).read_text())
        self.assertNotIn("evidence_ledger", state)
        self.assertIsNone(state["market_model_input"])
        before = {p: p.read_bytes() for p in files}
        self.assertNotEqual(self.init().returncode, 0)
        self.assertEqual(before, {p: p.read_bytes() for p in files})

    def test_project_output_and_explicit_market_model(self):
        self.assertNotEqual(self.init("--project-name", "Existing").returncode, 0)
        project = self.root / "项目" / "Existing"
        project.mkdir(parents=True)
        self.assertEqual(self.init("--project-name", "Existing", "--with-market-model").returncode, 0)
        outputs = project / "输出文档" / "03_研究与分析"
        self.assertEqual(len(list(outputs.glob("*.md"))), 1)
        self.assertEqual(len(list(outputs.glob("*.csv"))), 1)
        self.assertEqual(list((project / "输出文档").glob("*.md")), [])

    def test_focused_report_needs_no_market_or_ledger(self):
        report = self.root / "report.md"
        report.write_text("# Sample\n\n## Investment judgment\nUseful narrow finding.\n\n## Sources\nOriginal document.\n")
        result = self.run_script("validate_research.py", "--report", report)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("ledger not supplied", result.stdout)
        html = self.root / "report.html"
        rendered = self.run_script("render_report.py", "--input", report, "--output", html,
                                   "--title", "Sample", "--subtitle", "Example")
        self.assertEqual(rendered.returncode, 0, rendered.stdout + rendered.stderr)
        checked = self.run_script("validate_research.py", "--report", report, "--html", html)
        self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
        result = self.run_script("validate_research.py", "--report", report, "--require-module", "market")
        self.assertNotEqual(result.returncode, 0)

    def test_report_revision_preserves_edition_date_and_checks_the_reader_copy(self):
        report = self.root / "2024-01-02_sample.md"
        read_dir = self.root / "reader"
        output = read_dir / "study.html"
        (self.root / "source with spaces.md").write_text("# Evidence")
        text = ("# Sample\n\n## Investment judgment\nMeasured cost is 12.\n\n"
                "| Case | Units |\n|---|---|\n| Baseline | 32 |\n\n"
                "## Sources\n[Record](<source with spaces.md?view=read#record>) and "
                "[Publication](https://example.org/paper).\n")
        report.write_text(text)

        def check(*options):
            return self.run_script("validate_research.py", "--report", report, "--html", output, *options)

        render = self.run_script("render_report.py", "--input", report, "--output", output)
        self.assertEqual(render.returncode, 0, render.stderr)
        reader = output.read_text()
        self.assertIn("2024-01-02", reader)
        self.assertIn("../source%20with%20spaces.md?view=read#record", reader)
        checked = check()
        self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
        for original, changed in (("Measured cost is 12.", "Measured cost is 11."),
                                  ("<td>32</td>", "<td>16</td>"),
                                  ("https://example.org/paper", "https://example.org/old")):
            with self.subTest(original=original):
                output.write_text(reader.replace(original, changed))
                self.assertNotEqual(check().returncode, 0)
        output.write_text(reader)
        report.write_text(text.replace("Measured cost is 12.", ""))
        self.assertNotEqual(check().returncode, 0)

        # Legacy and separately edited editions have no source fingerprint.
        report.write_text(text)
        legacy = re.sub(r'<meta name="research-source-sha256"[^>]*>', "", reader)
        output.write_text(legacy.replace("<td>32</td>", "<td>16</td>"))
        self.assertNotEqual(check().returncode, 0)
        adapted = check("--adapted-html")
        self.assertEqual(adapted.returncode, 0, adapted.stdout)
        self.assertIn("WARNING: HTML article text", adapted.stdout)
        (self.root / "source with spaces.md").unlink()
        self.assertNotEqual(check("--adapted-html").returncode, 0)

    def test_forecast_retains_evidence_columns_and_accepted_result_on_failure(self):
        source = self.root / "drivers.csv"
        output = self.root / "model.csv"
        row = {key: "source" for key in validation.MARKET_COLUMNS}
        row.update(year="2026", addressable_units="100", paid_penetration="0.5", hardware_bom="10",
                   software_service_ratio="0", fx_to_cny="1", revision_note="supplier sample, revised")

        def forecast():
            with source.open("w", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(row))
                writer.writeheader()
                writer.writerow(row)
            return self.run_script("forecast_market.py", "--input", source, "--output", output)

        self.assertEqual(forecast().returncode, 0)
        with output.open(encoding="utf-8-sig", newline="") as handle:
            detail, total = list(csv.DictReader(handle))
        self.assertEqual(detail["revision_note"], row["revision_note"])
        self.assertEqual(total["total_revenue"], "500.0000")
        accepted = output.read_bytes()
        for invalid in ("broken", "Infinity", "NaN"):
            row["hardware_bom"] = invalid
            self.assertNotEqual(forecast().returncode, 0)
            self.assertEqual(output.read_bytes(), accepted)
        row["hardware_bom"] = "10"
        row["total_revenue"] = "old output"
        self.assertNotEqual(forecast().returncode, 0)
        self.assertEqual(output.read_bytes(), accepted)

    def test_non_hardware_model_single_year_single_region(self):
        path = self.root / "usage.csv"
        path.write_text("year,geography,active_users,annual_revenue_per_user\n2026,China,200,50\n")
        errors, warnings = [], []
        validation.validate_market(path, errors, warnings)
        self.assertEqual(errors, [])

    def test_shipment_model_checks_numeric_bounds(self):
        path = self.root / "model.csv"
        row = {key: "source" for key in validation.MARKET_COLUMNS}
        row.update(year="2026", geography="China", scenario="base", currency="CNY",
                   addressable_units="100", paid_penetration="0.5", hardware_bom="10",
                   software_service_ratio="0", fx_to_cny="1")
        def write_row():
            with path.open("w", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=sorted(row))
                writer.writeheader()
                writer.writerow(row)
        write_row()
        errors = []
        validation.validate_market(path, errors, [], "shipment-bom")
        self.assertEqual(errors, [])
        row["paid_penetration"] = "1.5"
        row["hardware_bom"] = "NaN"
        write_row()
        errors = []
        validation.validate_market(path, errors, [], "shipment-bom")
        self.assertEqual(len(errors), 2)


if __name__ == "__main__":
    unittest.main()
