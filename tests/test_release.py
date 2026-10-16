"""Real local Git publication checks; the GitHub API is simulated, not proven."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / "repo"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns(".git", "__pycache__", ".DS_Store", ".venv"))
        self.version = json.loads((self.repo / "plugin.json").read_text())["version"]
        self.tag = "v" + self.version
        major, minor, patch = self.version.split(".")
        self.other_version = f"{major}.{minor}.{int(patch) + 1}"
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Release test")
        self.git("config", "user.email", "release-test@example.com")
        self.git("add", ".")
        self.git("commit", "-m", "Release candidate")
        self.sha = self.git("rev-parse", "HEAD").stdout.strip()
        self.remote = self.base / "remote.git"
        subprocess.run(["git", "init", "--bare", str(self.remote)], check=True, capture_output=True)
        self.git("remote", "add", "origin", str(self.remote))
        self.git("push", "-u", "origin", "main")
        self.state = self.base / "release.json"
        self.bin = self.base / "bin"
        self.bin.mkdir()
        gh = self.bin / "gh"
        gh.write_text("""#!/usr/bin/env python3
import json, os, pathlib, sys
args = sys.argv[1:]
state = pathlib.Path(os.environ['TEST_RELEASE_STATE'])
if args[0] == 'api':
    if os.environ.get('TEST_API_FAIL'): sys.exit(1)
    if any('/pulls/' in arg for arg in args):
        print(pathlib.Path(os.environ['TEST_PR_STATE']).read_text())
    elif state.exists(): print(state.read_text())
elif args[:2] == ['release', 'create']:
    if os.environ.get('TEST_CREATE_FAIL'): sys.exit(1)
    state.write_text(json.dumps({
        'tag_name': args[2], 'name': args[args.index('--title') + 1],
        'body': pathlib.Path(args[args.index('--notes-file') + 1]).read_text(),
        'draft': False, 'prerelease': False, 'assets': []
    }))
else:
    sys.exit('Unexpected gh call: ' + repr(args))
""")
        gh.chmod(0o755)
        self.env = dict(os.environ, PATH=str(self.bin) + os.pathsep + os.environ["PATH"],
                        GH_TOKEN="test-token", GH_REPO="example/aasystem", TEST_RELEASE_STATE=str(self.state))

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, text=True, capture_output=True, check=True)

    def publish(self, version=None, sha=None, **env):
        if version is None:
            version = self.version
        return subprocess.run(["bash", "scripts/publish-release.sh", version, sha or self.sha,
                               "https://github.com/example/aasystem/pull/2"],
                              cwd=self.repo, env=dict(self.env, **env), text=True, capture_output=True)

    def resolve_pr(self, **changes):
        workflow = yaml.safe_load((self.repo / ".github/workflows/publish-release.yml").read_text())
        script = next(step["run"] for step in workflow["jobs"]["publish"]["steps"] if step.get("id") == "release")
        pr = dict(merged=True, title="release: " + self.tag, merge_commit_sha=self.sha,
                  base={"ref": "main", "repo": {"full_name": "example/aasystem"}})
        pr.update(changes)
        pr_state = self.base / "pr.json"
        pr_state.write_text(json.dumps(pr))
        output = self.base / "outputs"
        output.write_text("")
        result = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", script], cwd=self.repo,
                                env=dict(self.env, TEST_PR_STATE=str(pr_state), GITHUB_OUTPUT=str(output), RELEASE_PR="2"),
                                text=True, capture_output=True)
        return result, dict(line.split("=", 1) for line in output.read_text().splitlines())

    def test_workflow_resolves_and_publishes_exact_merged_release(self):
        result, outputs = self.resolve_pr()
        self.assert_success(result)
        self.assertEqual(outputs["sha"], self.sha)
        self.assertEqual(outputs["pr_url"], "https://github.com/example/aasystem/pull/2")
        self.assert_success(self.publish(version=outputs["version"], sha=outputs["sha"]))
        notes = json.loads(self.state.read_text())["body"]
        self.assertIn("Release PR: " + outputs["pr_url"], notes)
        self.assertNotIn("Host checks:", notes)

    def test_malformed_workflow_yaml_is_rejected(self):
        (self.repo / ".github/workflows/publish-release.yml").write_text("jobs: [\n")
        with self.assertRaises(yaml.YAMLError):
            self.resolve_pr()
        self.assert_no_remote_tag()

    def test_workflow_pip_caches_name_an_existing_dependency_file(self):
        for path in (self.repo / ".github/workflows").glob("*.yml"):
            workflow = yaml.safe_load(path.read_text())
            for job in workflow["jobs"].values():
                for step in job["steps"]:
                    settings = step.get("with", {})
                    if settings.get("cache") == "pip":
                        with self.subTest(workflow=path.name):
                            dependency = settings.get("cache-dependency-path")
                            self.assertIsNotNone(dependency, "Pip cache needs an explicit dependency file")
                            self.assertTrue((self.repo / dependency).is_file())

    def test_publication_bootstrap_supports_legacy_and_current_commits(self):
        workflow = yaml.safe_load((self.repo / ".github/workflows/publish-release.yml").read_text())
        install = next(step["run"] for step in workflow["jobs"]["publish"]["steps"]
                       if step.get("name") == "Install development dependencies")
        requirements = self.repo / "requirements-dev.txt"
        contents = requirements.read_text()
        self.git("rm", "requirements-dev.txt")
        self.git("commit", "-m", "Legacy release without development requirements")
        legacy_sha = self.git("rev-parse", "HEAD").stdout.strip()
        requirements.write_text(contents)
        self.git("add", "requirements-dev.txt")
        self.git("commit", "-m", "Migrate release development requirements")
        current_sha = self.git("rev-parse", "HEAD").stdout.strip()

        install_log = self.base / "install.log"
        python = self.bin / "python3"
        python.write_text('#!/bin/sh\nprintf "%s\\n" "$@" > "$TEST_INSTALL_LOG"\n')
        python.chmod(0o755)
        for sha, needs_dependencies in ((legacy_sha, False), (current_sha, True)):
            with self.subTest(needs_dependencies=needs_dependencies):
                self.git("checkout", "--detach", sha)
                result = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", install],
                                        cwd=self.repo, env=dict(self.env, TEST_INSTALL_LOG=str(install_log)),
                                        text=True, capture_output=True)
                self.assert_success(result)
                self.assertEqual(install_log.exists(), needs_dependencies)
                if needs_dependencies:
                    self.assertEqual(install_log.read_text().splitlines(),
                                     ["-m", "pip", "install", "-r", "requirements-dev.txt"])

    def test_workflow_rejects_unmerged_wrong_base_and_nonrelease_prs(self):
        cases = [dict(merged=False), dict(title="fix: ordinary change"), dict(title="release: " + self.tag + " extra"),
                 dict(base={"ref": "dev", "repo": {"full_name": "example/aasystem"}}),
                 dict(base={"ref": "main", "repo": {"full_name": "another/repo"}})]
        for change in cases:
            with self.subTest(change=change):
                result, outputs = self.resolve_pr(**change)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(outputs, {})
        self.assert_no_remote_tag()

    def assert_success(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def assert_no_remote_tag(self):
        self.assertEqual(self.git("ls-remote", "--tags", "origin").stdout, "")

    def test_exact_commit_after_main_moves_and_identical_retry(self):
        (self.repo / "later.txt").write_text("Later main commit")
        self.git("add", "later.txt")
        self.git("commit", "-m", "Later main")
        self.git("push", "origin", "main")
        self.git("checkout", "--detach", self.sha)
        self.assert_success(self.publish())
        self.assertEqual(self.git("rev-parse", self.tag + "^{commit}").stdout.strip(), self.sha)
        self.assertEqual(self.git("cat-file", "-t", self.tag).stdout.strip(), "tag")
        tag_before = self.git("rev-parse", self.tag).stdout
        release_before = self.state.read_bytes()
        self.assert_success(self.publish())
        self.assertEqual(self.git("rev-parse", self.tag).stdout, tag_before)
        self.assertEqual(self.state.read_bytes(), release_before)

    def test_resume_after_tag_push(self):
        self.assertNotEqual(self.publish(TEST_CREATE_FAIL="1").returncode, 0)
        self.assertFalse(self.state.exists())
        tag_before = self.git("rev-parse", self.tag).stdout
        self.assert_success(self.publish())
        self.assertEqual(self.git("rev-parse", self.tag).stdout, tag_before)

    def test_version_mismatch_stops_before_tag(self):
        self.assertNotEqual(self.publish(version=self.other_version).returncode, 0)
        self.assert_no_remote_tag()

    def test_wrong_checkout_stops_before_tag(self):
        self.assertNotEqual(self.publish(sha="0" * 40).returncode, 0)
        self.assert_no_remote_tag()

    def test_api_failure_stops_before_tag(self):
        self.assertNotEqual(self.publish(TEST_API_FAIL="1").returncode, 0)
        self.assert_no_remote_tag()

    def test_conflicting_remote_tag_is_preserved(self):
        self.git("commit", "--allow-empty", "-m", "Other commit")
        other = self.git("rev-parse", "HEAD").stdout.strip()
        self.git("tag", "-a", self.tag, "-m", "Other release")
        self.git("push", "origin", self.tag)
        self.git("checkout", "--detach", self.sha)
        self.assertNotEqual(self.publish().returncode, 0)
        self.assertEqual(self.git("rev-parse", self.tag + "^{commit}").stdout.strip(), other)
        self.assertFalse(self.state.exists())

    def test_lightweight_tag_is_rejected(self):
        self.git("tag", self.tag)
        self.git("push", "origin", self.tag)
        self.assertNotEqual(self.publish().returncode, 0)
        self.assertFalse(self.state.exists())

    def test_changed_release_notes_are_preserved(self):
        self.assert_success(self.publish())
        release = json.loads(self.state.read_text())
        release["body"] = "Different published notes"
        self.state.write_text(json.dumps(release))
        before = self.state.read_bytes()
        self.assertNotEqual(self.publish().returncode, 0)
        self.assertEqual(self.state.read_bytes(), before)

    def test_manifest_drift_and_missing_export_are_rejected(self):
        manifest_path = self.repo / ".claude-plugin/plugin.json"
        original = manifest_path.read_text()
        manifest = json.loads(original)
        manifest["version"] = self.other_version
        manifest_path.write_text(json.dumps(manifest))
        result = subprocess.run([sys.executable, "scripts/validate-release.py"], cwd=self.repo, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        manifest_path.write_text(original)
        shutil.rmtree(self.repo / "skills/product")
        result = subprocess.run([sys.executable, "scripts/validate-release.py"], cwd=self.repo, capture_output=True)
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
