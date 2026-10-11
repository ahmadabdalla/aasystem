"""Real local Git publication checks; the GitHub API is simulated, not proven."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / "repo"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns(".git", "__pycache__", ".DS_Store"))
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
    if state.exists(): print(state.read_text())
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

    def publish(self, version="0.2.0", sha=None, **env):
        return subprocess.run(["bash", "scripts/publish-release.sh", version, sha or self.sha,
                               "https://github.com/example/aasystem/pull/2#issuecomment-1"],
                              cwd=self.repo, env=dict(self.env, **env), text=True, capture_output=True)

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
        self.assertEqual(self.git("rev-parse", "v0.2.0^{commit}").stdout.strip(), self.sha)
        self.assertEqual(self.git("cat-file", "-t", "v0.2.0").stdout.strip(), "tag")
        tag_before = self.git("rev-parse", "v0.2.0").stdout
        release_before = self.state.read_bytes()
        self.assert_success(self.publish())
        self.assertEqual(self.git("rev-parse", "v0.2.0").stdout, tag_before)
        self.assertEqual(self.state.read_bytes(), release_before)

    def test_resume_after_tag_push(self):
        self.assertNotEqual(self.publish(TEST_CREATE_FAIL="1").returncode, 0)
        self.assertFalse(self.state.exists())
        tag_before = self.git("rev-parse", "v0.2.0").stdout
        self.assert_success(self.publish())
        self.assertEqual(self.git("rev-parse", "v0.2.0").stdout, tag_before)

    def test_version_mismatch_stops_before_tag(self):
        self.assertNotEqual(self.publish(version="0.3.0").returncode, 0)
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
        self.git("tag", "-a", "v0.2.0", "-m", "Other release")
        self.git("push", "origin", "v0.2.0")
        self.git("checkout", "--detach", self.sha)
        self.assertNotEqual(self.publish().returncode, 0)
        self.assertEqual(self.git("rev-parse", "v0.2.0^{commit}").stdout.strip(), other)
        self.assertFalse(self.state.exists())

    def test_lightweight_tag_is_rejected(self):
        self.git("tag", "v0.2.0")
        self.git("push", "origin", "v0.2.0")
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
        manifest["version"] = "0.1.0"
        manifest_path.write_text(json.dumps(manifest))
        result = subprocess.run(["ruby", "scripts/validate-release.rb"], cwd=self.repo, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        manifest_path.write_text(original)
        shutil.rmtree(self.repo / "skills/product")
        result = subprocess.run(["ruby", "scripts/validate-release.rb"], cwd=self.repo, capture_output=True)
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
