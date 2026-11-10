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


class BusinessModelTests(unittest.TestCase):
    def setUp(self):
        self.model = json.loads((SKILL / "examples" / "business-workflow.json").read_text())

    def reject(self, mutation, message):
        model = copy.deepcopy(self.model)
        mutation(model)
        with self.assertRaisesRegex(build.ModelError, message):
            build.validate(model)

    def test_reference_topology_and_performers(self):
        self.assertIs(build.validate(self.model), self.model)
        self.assertEqual([len(self.model[k]) for k in ["lanes", "components", "edges", "scenes"]], [3, 12, 13, 9])
        nodes = {node["id"]: node for node in self.model["components"]}
        self.assertEqual(nodes["allocation"]["lane"], "system")
        self.assertEqual(nodes["availability"]["lane"], "system")
        self.assertEqual(nodes["approve"]["lane"], "staff")
        self.assertEqual(nodes["qualify"]["label"], "Accept this request?")
        self.assertEqual(nodes["approve"]["label"], "Approve this allocation?")
        self.assertEqual(nodes["availability"]["scene"], nodes["input"]["scene"])
        self.assertNotIn("scene", nodes["closed"])
        self.assertEqual(next(e for e in self.model["edges"] if e["id"] == "confirmed")["kind"], "prerequisite")

    def test_unknown_profiles_fail_and_old_models_need_no_migration(self):
        for value in ["bpmn", "", [], None, True]:
            self.reject(lambda m: m["presentation"].update(profile=value), "presentation.profile")
        old = json.loads((SKILL / "examples" / "service-request.json").read_text())
        build.validate(old)
        old.setdefault("presentation", {})["profile"] = "technical"
        build.validate(old)

    def test_responsibility_scene_and_evidence_references(self):
        for mutation, message in [
            (lambda m: m["components"][0].update(lane="missing"), "lane.*unresolved"),
            (lambda m: m["components"][0].update(lane=[]), "lane"),
            (lambda m: m["lanes"][0].update(performer="owner"), "performer"),
            (lambda m: m["components"][0].update(scene="missing"), "scene.*unresolved"),
            (lambda m: m["components"][0].pop("scene"), "scene"),
            (lambda m: m["components"][0].update(scene="scene-9"), "selected scene"),
            (lambda m: m["components"][0].update(evidence=["missing"]), "evidence.*unresolved"),
            (lambda m: m["edges"][0].update(to="missing"), "unresolved"),
            (lambda m: m["components"][0].update(status="inferred"), "note"),
        ]:
            with self.subTest(message=message):
                self.reject(mutation, message)

    def test_state_dimensions_are_named_ordered_and_complete(self):
        # A second use case can use a different vocabulary and number of facts.
        self.model["stateDimensions"] = [{"id": "case", "label": "Case status"}]
        for scene in self.model["scenes"]:
            scene["states"] = {"case": "Open"}
        build.validate(self.model)
        for states in [{}, {"case":"Open", "unknown":"Bad"}, {"case":""}, []]:
            self.reject(lambda m: m["scenes"][0].update(states=states), "states")
        self.reject(lambda m: m["stateDimensions"].append(m["stateDimensions"][0]), "duplicate identifier")

    def test_branches_require_distinct_readable_alternatives(self):
        self.reject(lambda m: m["edges"][1].pop("condition"), "condition")
        self.reject(lambda m: m["edges"][1].update(condition="  "), "condition")
        self.reject(lambda m: m["edges"][1].update(kind="sequence"), "branch alternatives")
        self.reject(lambda m: m["edges"][3].update(condition=m["edges"][1]["condition"]), "distinct conditions")
        self.reject(lambda m: m["components"][1].update(label="Accept automatically"), "complete question")
        # Runtime meanings cannot leak into the workflow profile.
        self.reject(lambda m: m["edges"][0].update(kind="event"), "sequence, branch or prerequisite")

    def test_ordered_phases_cover_only_active_relationships(self):
        scene = self.model["scenes"][4]
        self.assertEqual(scene["phases"], [{"edges":["prepare"]}, {"edges":["priced"]}])
        for phases in [[], [{"edges":["missing"]}], [{"edges":["email"]}],
                       [{"edges":["prepare"]}], [{"edges":["prepare", "priced", "priced"]}],
                       [{"edges":[]}, {"edges":["prepare", "priced"]}],
                       [{"edges":["prepare", "priced"], "scene":"scene-4"}]]:
            with self.subTest(phases=phases):
                self.reject(lambda m: m["scenes"][4].update(phases=phases), "phases")
        self.reject(lambda m: m["scenes"][4].update(activeComponents=["availability", "allocation"]), "participants")
        scene.pop("phases")
        build.validate(self.model)

    def test_layout_hints_cannot_redefine_business_meaning(self):
        for key, value in [("label","Other"), ("lane","staff"), ("scene","scene-9"), ("step",2)]:
            self.reject(lambda m: m["components"][0]["layout"].update({key:value}), "layout fields")
        self.reject(lambda m: m["components"][0].update(step=1), "navigation uses scene IDs")
        self.reject(lambda m: m["edges"][0]["layout"]["label"].update(text="Other"), "layout fields")

    def test_layout_numbers_lanes_and_routes_are_bounded(self):
        for value in [True, "260", -1, float("nan"), float("inf"), 10**400, []]:
            self.reject(lambda m: m["components"][0]["layout"].update(x=value), "layout.x")
        self.reject(lambda m: m["presentation"].update(canvas={"width":1,"height":600}), "canvas.width")
        self.reject(lambda m: m["lanes"][0]["layout"].update(height=200), "lanes.*overlap")
        self.reject(lambda m: m["components"][0]["layout"].update(y=150), "performer lane")
        self.reject(lambda m: m["components"][0]["layout"].update(width=1180), "beyond the canvas")
        for points in [[], [[1,2]], [[1]], [[1,2],[2,3]], [[1,2],[1,2]], [[0,0],[0,601]], [None, [1,2]]]:
            self.reject(lambda m: m["edges"][0]["layout"].update(points=points), "layout.points")

    def test_business_fixture_builds_through_standard_command(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "business.html"
            result = subprocess.run([sys.executable, str(SKILL / "scripts" / "build.py"),
                str(SKILL / "examples" / "business-workflow.json"), "--output", str(output)],
                cwd=directory, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('"profile":"business-workflow"', output.read_text())
            self.assertNotIn("__SYSTEM_IN_MOTION_MODEL__", output.read_text())


if __name__ == "__main__":
    unittest.main()
