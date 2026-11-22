"""Run Design Judge's alignment capture on fixtures whose containers declare their expected findings."""
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import shutil
import struct
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CAPTURE = ROOT / "skills/design-judge/scripts/capture.mjs"
FIXTURES = ROOT / "tests/fixtures/design-judge"
WIDTHS = "1440,390"


class Expectations(HTMLParser):
    """Collects aria-label -> data-expect from a fixture page."""

    def __init__(self):
        super().__init__()
        self.expected = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "aria-label" in attrs and tag != "button":
            self.expected[attrs["aria-label"]] = sorted((attrs.get("data-expect") or "").split())


def finding(miss):
    count = f"x{miss['count']}" if miss["count"] > 1 else ""
    return f"{'+'.join(miss['edges'])}:{miss['delta']:+g}{count}"


def playwright_available():
    if not shutil.which("node"):
        return False
    if os.environ.get("PLAYWRIGHT_DIR"):
        return True
    return subprocess.run(["node", "-e", "require.resolve('playwright')"], cwd=ROOT, capture_output=True).returncode == 0


@unittest.skipUnless(playwright_available(), "needs node and Playwright (set PLAYWRIGHT_DIR and, optionally, CHROMIUM_PATH)")
class DesignJudgeCaptureTest(unittest.TestCase):
    def check(self, page, exit_code):
        parser = Expectations()
        parser.feed((FIXTURES / page).read_text())
        with tempfile.TemporaryDirectory(prefix="design-judge-") as out:
            run = subprocess.run(
                ["node", str(CAPTURE), (FIXTURES / page).as_uri(), out, "--widths", WIDTHS, "--settle", "100"],
                capture_output=True, text=True, timeout=180,
            )
            self.assertEqual(exit_code, run.returncode, run.stderr or run.stdout)
            for result in sorted(Path(out).glob("*.json")):
                capture = json.loads(result.read_text())
                png = result.with_suffix(".png").read_bytes()
                self.assertEqual(2 * capture["width"], struct.unpack(">I", png[16:20])[0], "captures are 2x and never widened")
                containers = {c["container"]: c for c in capture["containers"]}
                self.assertEqual(len(containers), len(capture["containers"]), "container names are unique")
                for name, expected in parser.expected.items():
                    with self.subTest(capture=result.stem, container=name):
                        self.assertIn(name, containers)
                        actual = sorted([*(["unmeasured"] if containers[name]["unmeasured"] else []), *map(finding, containers[name]["misses"])])
                        self.assertEqual(expected, actual)
                for name, container in containers.items():
                    if name not in parser.expected:
                        with self.subTest(capture=result.stem, unexpected=name):
                            self.assertEqual([], container["misses"])

    def test_planted_misses_are_reported_once_with_their_offsets(self):
        self.check("misses.html", 1)

    def test_aligned_layouts_report_nothing(self):
        self.check("aligned.html", 0)


if __name__ == "__main__":
    unittest.main()
