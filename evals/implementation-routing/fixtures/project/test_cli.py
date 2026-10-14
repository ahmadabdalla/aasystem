import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class LedgerSmokeTest(unittest.TestCase):
    def test_preview_output(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, "ledger.py", "--store", str(Path(directory) / "ledger.json"),
                 "preview", "First"], capture_output=True, text=True, check=True
            )
            self.assertEqual(json.loads(result.stdout), {"id": 1, "message": "First"})

    def test_added_message_is_listed(self):
        with tempfile.TemporaryDirectory() as directory:
            store = str(Path(directory) / "ledger.json")
            for command in (("add", "Saved"), ("list",)):
                result = subprocess.run(
                    [sys.executable, "ledger.py", "--store", store, *command],
                    capture_output=True, text=True, check=True
                )
            self.assertEqual(json.loads(result.stdout), [{"id": 1, "message": "Saved"}])


if __name__ == "__main__":
    unittest.main()
