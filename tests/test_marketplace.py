"""Exercise catalog preparation with real local Git refs; no remote writes."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/prepare-marketplace.py"


class MarketplaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.catalog = self.repo / ".claude-plugin/marketplace.json"
        self.catalog.parent.mkdir()
        self.catalog.write_text(json.dumps({"plugins": [
            {"name": "other", "version": "0.3.0", "source": {"ref": "v0.3.0"}},
            {"name": "aasystem", "source": {"ref": "v0.3.0"}, "version": "0.3.0"},
        ]}, indent=2) + "\n")
        self.readme = self.repo / "README.md"
        self.readme.write_text("| [other](other) | Other | 0.3.0 |\n| [aasystem](aasystem) | Pilot | 0.3.0 |\n")
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.com")
        self.git("add", ".")
        self.git("commit", "-m", "Catalog")
        self.original = self.catalog.read_text()
        self.notes = self.readme.read_text()

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, check=True, capture_output=True, text=True)

    def prepare(self, version):
        output = self.repo / "outputs"
        output.write_text("")
        result = subprocess.run([sys.executable, str(SCRIPT), version], cwd=self.repo,
                                env=dict(os.environ, GITHUB_OUTPUT=str(output)), capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return output.read_text().strip() == "changed=true"

    def pending(self, version):
        self.assertTrue(self.prepare(version))
        self.git("add", ".claude-plugin/marketplace.json", "README.md")
        self.git("commit", "-m", "Pending adoption")
        self.git("update-ref", "refs/remotes/origin/automation/aasystem-release", "HEAD")
        self.git("checkout", "HEAD~1", "--", ".claude-plugin/marketplace.json", "README.md")

    def assert_unchanged(self):
        self.assertEqual(self.catalog.read_text(), self.original)
        self.assertEqual(self.readme.read_text(), self.notes)

    def test_new_release_changes_only_aasystem_version_ref_and_row(self):
        self.assertTrue(self.prepare("0.4.0"))
        before = json.loads(self.original)["plugins"]
        after = json.loads(self.catalog.read_text())["plugins"]
        self.assertEqual(after[0], before[0])
        self.assertEqual(after[1], dict(before[1], version="0.4.0", source={"ref": "v0.4.0"}))
        self.assertTrue(self.readme.read_text().startswith(self.notes.splitlines()[0] + "\n"))
        self.assertIn("| 0.4.0 |", self.readme.read_text())

    def test_adopted_and_older_releases_do_not_change_files(self):
        for version in ("0.3.0", "0.2.0"):
            with self.subTest(version=version):
                self.assertFalse(self.prepare(version))
                self.assert_unchanged()

    def test_older_retry_cannot_replace_a_newer_pending_adoption(self):
        self.pending("0.10.0")
        self.assertFalse(self.prepare("0.9.0"))
        self.assert_unchanged()

    def test_matching_retry_recreates_same_changes(self):
        self.pending("0.4.0")
        self.assertTrue(self.prepare("0.4.0"))
        expected = self.git("show", "refs/remotes/origin/automation/aasystem-release:.claude-plugin/marketplace.json").stdout
        self.assertEqual(self.catalog.read_text(), expected)

    def test_newer_release_supersedes_pending_adoption(self):
        self.pending("0.4.0")
        self.assertTrue(self.prepare("0.5.0"))

    def test_readme_drift_fails_before_writing_catalog(self):
        self.readme.write_text("No version table\n")
        result = subprocess.run([sys.executable, str(SCRIPT), "0.4.0"], cwd=self.repo,
                                env=dict(os.environ, GITHUB_OUTPUT=str(self.repo / "outputs")),
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Expected one aasystem version row", result.stderr)
        self.assertEqual(self.catalog.read_text(), self.original)


if __name__ == "__main__":
    unittest.main()
