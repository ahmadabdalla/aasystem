"""Exercise the package validator against disposable, deliberately broken exports."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = "skills/product/SKILL.md"
ADAPTER = "skills/product/agents/openai.yaml"


class ReleaseValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / "repo"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns(".git", "__pycache__", ".DS_Store", ".venv"))
        subprocess.run(["git", "init", str(self.repo)], check=True, capture_output=True)

    def validate(self, cwd=None):
        return subprocess.run([sys.executable, str(self.repo / "scripts/validate-release.py")],
                              cwd=cwd or self.repo, text=True, capture_output=True)

    def assert_invalid(self, message):
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("FAIL: " + message, result.stderr)
        self.assertNotIn("PASS: aasystem", result.stdout)

    def reject_edit(self, path, content, message):
        target = self.repo / path
        original = target.read_text()
        try:
            target.write_text(content)
            self.assert_invalid(message)
        finally:
            target.write_text(original)

    def test_valid_export_from_another_working_directory(self):
        result = self.validate(cwd=self.base)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("skills and adapters;", result.stdout)
        self.assertIn("Host installation, invocation, workflow evaluations and link anchors are separate checks.", result.stdout)

    def test_manifest_identity_version_and_parity(self):
        portable = json.loads((self.repo / "plugin.json").read_text())
        claude = json.loads((self.repo / ".claude-plugin/plugin.json").read_text())
        self.reject_edit("plugin.json", json.dumps(dict(portable, name="other")),
                         "Installation identity must remain aasystem")
        for version in ("01.2.3", "1.2.3-beta", "1.2", 123):
            with self.subTest(version=version):
                self.reject_edit("plugin.json", json.dumps(dict(portable, version=version)), "Use a stable X.Y.Z version")
        for key in ("name", "version"):
            with self.subTest(key=key):
                self.reject_edit(".claude-plugin/plugin.json", json.dumps(dict(claude, **{key: "different"})),
                                 f"Manifest {key} values differ")

    def test_missing_required_exports(self):
        for path in ("README.md", "LICENSE", "skills/aapilot/agents/openai.yaml",
                     "docs/design/skill-system.md", "docs/ops/codex.md", "docs/ops/releasing.md"):
            with self.subTest(path=path):
                target = self.repo / path
                contents = target.read_bytes()
                target.unlink()
                try:
                    self.assert_invalid(f"Missing export file: {path}")
                finally:
                    target.write_bytes(contents)

    def test_former_entry_point_is_rejected(self):
        (self.repo / "skills/aasystem").mkdir()
        self.assert_invalid("Former entry point must not remain")

    def test_inventory_drift_is_rejected(self):
        shutil.rmtree(self.repo / "skills/product")
        self.assert_invalid("System inventory and portable skill tree differ")

    def test_frontmatter_shape_name_and_description(self):
        self.reject_edit(SKILL, "No metadata\n", "Missing metadata:")
        self.reject_edit(SKILL, "---\n- list\n---\nBody\n", "Metadata must be a mapping:")
        original = (self.repo / SKILL).read_text()
        self.reject_edit(SKILL, original.replace("name: product", "name: other"), "Skill name differs from directory:")
        self.reject_edit(SKILL, "---\nname: product\ndescription: '  '\n---\nBody\n", "Missing description:")

    def test_malformed_yaml_is_rejected(self):
        for path, contents in ((SKILL, "---\nname: [\n---\nBody\n"), (ADAPTER, "policy: [\n")):
            with self.subTest(path=path):
                self.reject_edit(path, contents, f"Invalid YAML in {path}:")

    def test_invalid_tagged_scalars_include_filename(self):
        for path, policy, value in ((SKILL, "disable-model-invocation", "true"),
                                    (ADAPTER, "allow_implicit_invocation", "false")):
            original = (self.repo / path).read_text()
            for scalar in ("!!bool invalid", "!!int invalid", "!!float invalid"):
                with self.subTest(path=path, scalar=scalar):
                    contents = original.replace(f"{policy}: {value}", f"{policy}: {scalar}")
                    self.reject_edit(path, contents, f"Invalid YAML in {path}:")

    def test_skill_invocation_policy_requires_boolean_true(self):
        original = (self.repo / SKILL).read_text()
        for value in ("false", "'true'", "1", "null"):
            with self.subTest(value=value):
                self.reject_edit(SKILL, original.replace("disable-model-invocation: true", f"disable-model-invocation: {value}"),
                                 "Explicit invocation policy missing:")

    def test_adapter_invocation_policy_requires_boolean_false(self):
        for value in ("true", "'false'", "0", "null"):
            with self.subTest(value=value):
                self.reject_edit(ADAPTER, f"policy:\n  allow_implicit_invocation: {value}\n", "Adapter invocation policy differs:")
        for contents in ("- list\n", "policy: false\n", "policy: {}\n", "{}\n"):
            with self.subTest(contents=contents):
                self.reject_edit(ADAPTER, contents, "Adapter invocation policy differs:")

    def test_missing_adapter_is_rejected(self):
        (self.repo / ADAPTER).unlink()
        self.assert_invalid("[Errno 2]")

    def test_local_link_paths_and_exemptions(self):
        path = self.repo / "README.md"
        # URLs, anchors, fenced examples and the two owning-file placeholders are exempt.
        with path.open("a") as document:
            document.write("\n[web](https://example.com/missing) [anchor](#missing)\n"
                           "```md\n[example](missing-example.md)\n```\n")
        (self.repo / "a file.md").write_text("Target\n")
        with path.open("a") as document:
            document.write('[encoded](<a%20file.md#anchor> "Title")\n')
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        (self.repo / "a file.md").unlink()
        self.assert_invalid("Missing link target in README.md: a file.md")

    def test_placeholder_exemption_is_limited_to_owning_document(self):
        original = (self.repo / "README.md").read_text()
        for placeholder in ("VERIFIER_PATH", "MAP_PATH"):
            with self.subTest(placeholder=placeholder):
                self.reject_edit("README.md", original + f"\n[invalid]({placeholder})\n",
                                 f"Missing link target in README.md: {placeholder}")

    def test_versioned_release_notes_must_exist_and_have_content(self):
        version = json.loads((self.repo / "plugin.json").read_text())["version"]
        for contents in ("# Changelog\n", f"## [{version}]\n\n## [older]\nOther notes\n"):
            with self.subTest(contents=contents):
                self.reject_edit("CHANGELOG.md", contents, "Missing versioned release notes")

    def test_shell_syntax_and_guard_failure(self):
        guard = "skills/bootstrap-verification/assets/check-verification-output.sh"
        self.reject_edit(guard, "if\n", "Shipped helper syntax failed")
        self.reject_edit(guard, "exit 23\n", "Verification output guard failed")

    def test_guard_rejects_indexed_temporary_output(self):
        output = self.repo / ".verification/runs/evidence.txt"
        output.parent.mkdir(parents=True)
        output.write_text("Temporary evidence\n")
        subprocess.run(["git", "add", "-f", str(output)], cwd=self.repo, check=True, capture_output=True)
        self.assert_invalid("Verification output guard failed")


if __name__ == "__main__":
    unittest.main()
