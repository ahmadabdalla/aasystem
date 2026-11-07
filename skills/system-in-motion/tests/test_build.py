"""Run: python3 -m unittest discover -s <skill>/tests -v"""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SKILL = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("system_in_motion_build", SKILL / "scripts" / "build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class ModelTests(unittest.TestCase):
    def setUp(self):
        self.model = json.loads((SKILL / "examples" / "service-request.json").read_text())

    def test_reference_resolves(self):
        self.assertIs(build.validate(self.model), self.model)

    def test_rich_visual_fields_preserve_plain_data_and_validate(self):
        self.model["presentation"] = {"name": "Example", "mark": "EX", "navigation": ["Intake", "Review"], "boundary": {"label": "Application", "detail": "Logical boundary"}, "accent": "#c9a84c"}
        scene = self.model["scenes"][0]["experience"]
        scene.update(layout="review", mode="explanation", items=[{"title":"Validate","detail":"Inspect input"}], columns=["Field","Result"], rows=[["Status","Pending"]], audit=[{"label":"Received"}], stages=[{"label":"Input"}], packet="REQUEST")
        build.validate(self.model)
        scene["rows"] = [["Too short"]]
        with self.assertRaisesRegex(build.ModelError, "row width"):
            build.validate(self.model)

    def test_presentation_does_not_accept_styles_as_executable_input(self):
        self.model["presentation"] = {"accent":"url(https://invalid.example/image)"}
        with self.assertRaisesRegex(build.ModelError, "hex color"):
            build.validate(self.model)

    def test_unknown_endpoint_and_active_edge_are_rejected(self):
        for mutation in [lambda m: m["edges"][0].update(to="missing"), lambda m: m["scenes"][0].update(activeEdges=["missing"])]:
            model = copy.deepcopy(self.model)
            mutation(model)
            with self.assertRaisesRegex(build.ModelError, "unresolved"):
                build.validate(model)

    def test_duplicate_cells_and_identifiers_are_rejected(self):
        duplicate = copy.deepcopy(self.model["components"][0])
        self.model["components"].append(duplicate)
        with self.assertRaisesRegex(build.ModelError, "duplicate identifier"):
            build.validate(self.model)
        duplicate["id"] = "another-person"
        with self.assertRaisesRegex(build.ModelError, "same lane/row/column"):
            build.validate(self.model)

    def test_current_exchanges_cannot_target_unhighlighted_components(self):
        self.model["scenes"][0]["activeComponents"] = ["visitor"]
        with self.assertRaisesRegex(build.ModelError, "participants"):
            build.validate(self.model)

    def test_uncertainty_is_explicit(self):
        node = self.model["components"][0]
        node.update(status="unknown", evidence=[])
        with self.assertRaisesRegex(build.ModelError, "note"):
            build.validate(self.model)
        node["note"] = "Implementation was not available for inspection."
        build.validate(self.model)
        node.update(status="implemented")
        with self.assertRaisesRegex(build.ModelError, "supporting source"):
            build.validate(self.model)

    def test_malformed_status_and_duration_are_useful_errors(self):
        self.model["scenes"][0]["status"] = []
        with self.assertRaisesRegex(build.ModelError, "status"):
            build.validate(self.model)
        self.model["scenes"][0]["status"] = "implemented"
        for duration in [True, 0, 31, float("nan"), float("inf"), 10**400]:
            self.model["scenes"][0]["duration"] = duration
            with self.assertRaisesRegex(build.ModelError, "duration"):
                build.validate(self.model)

    def test_model_cannot_close_its_script_or_inject_markup(self):
        unsafe = '</script><script>globalThis.injected=true</script>&\u2028'
        self.model["summary"] = unsafe
        template = '<script id="model" type="application/json">__SYSTEM_IN_MOTION_MODEL__</script>'
        html = build.render(build.validate(self.model), template)
        self.assertEqual(html.count("</script>"), 1)
        payload = html.split('application/json">', 1)[1].rsplit("</script>", 1)[0]
        self.assertEqual(json.loads(payload)["summary"], unsafe)

    def test_rejects_nonfinite_json_and_ambiguous_template(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text('{"duration":NaN}')
            with self.assertRaisesRegex(build.ModelError, "non-finite"):
                build.load_model(path)
        for template in ["no marker", "__SYSTEM_IN_MOTION_MODEL__ __SYSTEM_IN_MOTION_MODEL__"]:
            with self.assertRaisesRegex(build.ModelError, "exactly one"):
                build.render(self.model, template)

    def test_cli_failure_does_not_overwrite_existing_output(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            model = directory / "invalid.json"
            output = directory / "existing.html"
            model.write_text("{}")
            output.write_text("Preserved")
            result = subprocess.run([sys.executable, str(SKILL / "scripts" / "build.py"), str(model), "--output", str(output)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(output.read_text(), "Preserved")
            self.assertNotIn("Traceback", result.stderr)

    def test_cli_runs_outside_the_project_and_cannot_overwrite_input(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            model = directory / "model.json"
            template = directory / "template.html"
            output = directory / "preview.html"
            model.write_text(json.dumps(self.model))
            template.write_text('<script type="application/json">__SYSTEM_IN_MOTION_MODEL__</script>')
            command = [sys.executable, str(SKILL / "scripts" / "build.py"), str(model), "--template", str(template), "--output"]
            built = subprocess.run(command + [str(output)], cwd=directory, capture_output=True, text=True)
            self.assertEqual(built.returncode, 0, built.stderr)
            rejected = subprocess.run(command + [str(model)], cwd=directory, capture_output=True, text=True)
            self.assertEqual(rejected.returncode, 1)
            self.assertEqual(json.loads(model.read_text()), self.model)


if __name__ == "__main__":
    unittest.main()
