"""Exercise the public identity CLI against real dirty Git working trees."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import tracemalloc
import unittest


HELPER = Path(__file__).resolve().parents[1] / 'skills/pilot/scripts/input_identity.py'


class InputIdentityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.root = self.base / 'app'
        self.root.mkdir()
        self.git('init', '-q')
        (self.root / '.gitignore').write_text('local.json\noutput/\n')
        (self.root / 'app.py').write_text('print("before")\n')
        self.git('add', '.')
        self.saved = self.base / 'tested.json'

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.root), *args], check=True, capture_output=True)

    def cli(self, *args, expected=0):
        result = subprocess.run([sys.executable, str(HELPER), '--root', str(self.root), *args],
                                capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return json.loads(result.stdout if result.stdout else result.stderr)

    def save(self, *args):
        record = self.cli(*args)
        self.saved.write_text(json.dumps(record))
        return record

    def test_unchanged_inputs_match_without_source_copies(self):
        before = sorted(str(p.relative_to(self.root)) for p in self.root.rglob('*'))
        original = (self.root / 'app.py').read_bytes()
        record = self.save()
        self.assertEqual(self.cli('--check', str(self.saved)), record)
        self.assertEqual(sorted(str(p.relative_to(self.root)) for p in self.root.rglob('*')), before)
        self.assertEqual((self.root / 'app.py').read_bytes(), original)

    def test_uncommitted_edit_invalidates_result(self):
        self.save()
        (self.root / 'app.py').write_text('print("after!")\n')
        self.cli('--check', str(self.saved), expected=1)

    def test_new_nonignored_file_invalidates_result(self):
        self.save()
        (self.root / 'api.py').write_text('new API\n')
        self.cli('--check', str(self.saved), expected=1)

    def test_deleted_tracked_file_and_changed_selection_are_visible(self):
        self.save()
        (self.root / 'app.py').unlink()
        self.cli('--check', str(self.saved), expected=1)
        missing = self.save()
        self.assertEqual(missing['inputs']['app.py'], {'missing': True})
        self.git('rm', '--cached', 'app.py')
        self.cli('--check', str(self.saved), expected=1)

    def test_ignored_output_does_not_invalidate_result(self):
        self.save()
        (self.root / 'output').mkdir()
        (self.root / 'output/log.txt').write_text('observations\n')
        self.cli('--check', str(self.saved))

    def test_required_ignored_configuration_is_remembered_at_check(self):
        config = self.root / 'local.json'
        config.write_text('{"mode":"test"}')
        record = self.save('--required', 'local.json')
        self.assertIn('local.json', record['inputs'])
        self.cli('--check', str(self.saved))
        config.write_text('{"mode":"live"}')
        self.cli('--check', str(self.saved), expected=1)

    def test_required_external_input_is_checked(self):
        config = self.base / 'settings.json'
        config.write_text('test')
        self.save('--required', str(config))
        config.unlink()
        self.cli('--check', str(self.saved), expected=2)

    def test_required_directory_fails_with_actionable_error(self):
        result = self.cli('--required', str(self.root), expected=2)
        self.assertIn('project-specific identity', result['error'])

    def test_symlink_and_fifo_refuse_without_reading_target(self):
        target = self.base / 'outside'
        target.write_text('keep')
        link = self.root / 'link'
        link.symlink_to(target)
        self.cli(expected=2)
        self.assertEqual(target.read_text(), 'keep')
        link.unlink()
        if hasattr(os, 'mkfifo'):
            os.mkfifo(self.root / 'pipe')
            self.cli('--required', 'pipe', expected=2)

    def test_executable_mode_change_invalidates_result(self):
        self.save()
        app = self.root / 'app.py'
        app.chmod(app.stat().st_mode ^ 0o100)
        self.cli('--check', str(self.saved), expected=1)

    def test_malformed_manifest_refuses(self):
        self.saved.write_text('{}')
        self.cli('--check', str(self.saved), expected=2)
        self.saved.write_text('null')
        self.cli('--check', str(self.saved), expected=2)

    def test_large_required_file_uses_bounded_memory(self):
        large = self.root / 'local.json'
        with large.open('wb') as stream:
            for _ in range(24):
                stream.write(b'x' * (1024 * 1024))
        spec = importlib.util.spec_from_file_location('input_identity', HELPER)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        tracemalloc.start()
        try:
            record = module.fingerprint(self.root, [str(large)])
            _, peak = tracemalloc.get_traced_memory()
        finally:
            tracemalloc.stop()
        self.assertEqual(record['inputs']['local.json']['size'], 24 * 1024 * 1024)
        self.assertLess(peak, 5 * 1024 * 1024)


if __name__ == '__main__':
    unittest.main()
