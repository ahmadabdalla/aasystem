"""Exercise the copied, standalone helper through its public CLI."""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


HELPER = Path(__file__).resolve().parents[1] / "skills/bootstrap-verification/assets/check-temporary-references.py"


class TemporaryReferenceTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.root = self.base / "project"
        self.root.mkdir()
        self.helper = self.base / "standalone.py"
        shutil.copyfile(HELPER, self.helper)

    def write(self, name, text):
        target = self.root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target

    def cli(self, *files, roots=(), expected=0, root=None):
        command = [sys.executable, "-B", str(self.helper), "--root", str(root or self.root)]
        for directory in roots:
            command.extend(["--temporary-root", str(directory)])
        result = subprocess.run(command + ["--", *map(str, files)], cwd=self.base,
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        self.assertEqual(result.stderr, "")
        return result.stdout

    def test_common_posix_roots_file_uris_and_percent_encoding(self):
        references = ["/tmp", "/tmp/run/proof.png", "/private/tmp/run/report",
                      "/var/tmp/run", "/private/var/tmp/run", "/var/folders/ab/run", "/private/var/folders/ab/run",
                      "file:///tmp/a%20report.txt", "file://localhost/private/tmp/report",
                      "%2Ftmp%2Frun%2Fproof", "RESULT=/tmp/run/report", "/tmp/$RUN/report",
                      "file:/tmp/proof.json"]
        self.write("README.md", "\n".join(f"[proof]({path})" for path in references))
        output = self.cli("README.md", expected=1)
        self.assertEqual(set(output.splitlines()[:-1]),
                         {f"README.md:{number}: temporary reference" for number in range(1, len(references) + 1)})
        self.assertIn("Selected 1 file(s); checked 1 file(s).", output)

    def test_windows_native_slash_json_and_uri_forms_on_any_host(self):
        references = [r"C:\Users\Alice\AppData\Local\Temp\run\proof.png",
                      "c:/users/Alice/AppData/Local/Temp/run", r"C:\Windows\Temp\proof",
                      r'"C:\\Users\\Alice\\AppData\\Local\\Temp\\proof"',
                      "file:///C:/Users/Alice/AppData/Local/Temp/proof",
                      "file://C:/Windows/Temp/proof"]
        self.write("README.md", "\n".join(references))
        output = self.cli("README.md", expected=1)
        self.assertEqual(len(output.splitlines()), len(references) + 1)

    def test_delimited_windows_paths_and_custom_roots_with_spaces(self):
        self.write("docs/verification.md", "\n".join([
            r'"C:\Users\Jane Doe\AppData\Local\Temp\run"',
            r'`C:\\Users\\Jane Doe\\AppData\\Local\\Temp\\run`',
            '<C:/Users/Jane Doe/AppData/Local/Temp/run>',
            '[proof](../scratch/run 1/a report.txt)',
            '"../scratch/run 1/a report.txt"',
            '"/work/run 1/a report.txt"',
            '"../scratch/run 10/a report.txt"',
        ]))
        output = self.cli("docs/verification.md", roots=("scratch/run 1", "/work/run 1"), expected=1)
        self.assertEqual(set(output.splitlines()[:-1]),
                         {f"docs/verification.md:{number}: temporary reference" for number in range(1, 7)})

    def test_exact_custom_roots_relative_references_and_component_boundaries(self):
        self.write("docs/verification.md", "\n".join([
            "../scratch/run-1/proof.png", "../scratch/run-1", "../scratch/run-10/proof.png",
            "/work/disposable/run-1/proof", "/work/disposable/run-10/proof",
            "[proof](file:///work/disposable/run-1/a%20report)",
            r"D:\Disposable\run-1\proof", r"D:\Disposable\run-10\proof",
        ]))
        output = self.cli("docs/verification.md", roots=("scratch/run-1", "/work/disposable/run-1", r"d:\disposable\RUN-1"), expected=1)
        self.assertEqual(set(output.splitlines()[:-1]),
                         {f"docs/verification.md:{number}: temporary reference" for number in (1, 2, 4, 6, 7)})

    def test_urls_variables_and_unrelated_tmp_names_are_clean(self):
        self.write("README.md", "\n".join([
            "https://example.org/tmp/run/proof", "https://example.org/path?proof=/tmp/run",
            "https://example.org/C:/Users/Alice/AppData/Local/Temp/proof",
            "RESULT=https://example.org/tmp/run", "tmp/report.txt", "docs/tmp/report.txt",
            "RESULT=https://example.org/path?proof=/tmp/run", '"RESULT=https://example.org/path?proof=/tmp/run"',
            "/tmpest/proof", "/var/tmpest/proof", "/private/tmpest/proof",
            "C:/Windows/Temporary/proof", "C:/Users/Alice/AppData/Local/Temporary/proof",
            "$TMPDIR/proof", "${TEMP}/proof", "%TEMP%/proof", "temporary evidence lives in a run directory.",
            "/work/run-10/proof", "../scratch/run-10/proof",
        ]))
        self.assertEqual(self.cli("README.md", roots=("/work/run-1", "scratch/run-1")),
                         "Selected 1 file(s); checked 1 file(s).\n")

    def test_only_explicit_files_are_inspected_and_empty_files_are_valid(self):
        self.write("empty.md", "")
        self.write("unselected.md", "/tmp/must-not-be-read")
        self.assertEqual(self.cli("empty.md"), "Selected 1 file(s); checked 1 file(s).\n")
        self.cli(expected=2)

    def test_bom_and_exact_root_names_with_punctuation(self):
        self.write("README.md", "\ufeff/tmp/report\n[proof](/work/run./report)\n/work/run/report\n")
        self.assertEqual(self.cli("README.md", roots=("/work/run.",), expected=1),
                         "README.md:1: temporary reference\nREADME.md:2: temporary reference\n"
                         "Selected 1 file(s); checked 1 file(s).\n")

    def test_delimited_exact_root_keeps_terminal_punctuation(self):
        for punctuation in ".!?:":
            with self.subTest(punctuation=punctuation):
                directory = "/work/run" + punctuation
                self.write("README.md", '\n'.join([f'"{directory}"', f'`{directory}`', f'<{directory}>', f'[proof]({directory})']))
                output = self.cli("README.md", roots=(directory,), expected=1)
                self.assertEqual(set(output.splitlines()[:-1]),
                                 {f"README.md:{number}: temporary reference" for number in range(1, 5)})
                self.cli("README.md", roots=("/work/run",))

    def test_delimited_sibling_path_is_not_reinterpreted_as_fragments(self):
        self.write("README.md", '\n'.join([
            '"/work/run;archive/proof.json"', '"/work/run(archive)/proof.json"',
            '`/work/run;archive/proof.json`', '</work/run(archive)/proof.json>',
            '"/work/run,archive/proof.json"', '"run;archive/proof.json"',
        ]))
        self.cli("README.md", roots=("/work/run", "run"))

    def test_bare_and_quoted_prose_still_exposes_embedded_paths(self):
        self.write("README.md", '\n'.join([
            'See /work/run/proof.json.', '"Proof lives at /work/run/proof.json."',
            "'Proof lives at /tmp/proof.json.'", '"Proof lives at ../scratch/run/proof.json."',
        ]))
        output = self.cli("README.md", roots=("/work/run", "../scratch/run"), expected=1)
        self.assertEqual(set(output.splitlines()[:-1]),
                         {f"README.md:{number}: temporary reference" for number in range(1, 5)})

    def test_equals_in_absolute_paths_and_file_uri_queries_remains_literal(self):
        self.write("README.md", '\n'.join([
            '"/tmp/run=42/proof"', '/tmp/run=42/proof',
            'file:/tmp/proof?format=json', 'file:///tmp/proof?format=json',
            'RESULT=/tmp/run=42/proof', r'C:\Users\Alice\AppData\Local\Temp\run=42\proof',
        ]))
        output = self.cli("README.md", expected=1)
        self.assertEqual(set(output.splitlines()[:-1]),
                         {f"README.md:{number}: temporary reference" for number in range(1, 7)})

    def test_equals_in_supplied_roots_and_relative_paths_remains_literal(self):
        self.write("docs/verification.md", '\n'.join([
            '"/work/run=42/proof"', '/work/run=42/proof',
            '"../run=42/proof"', '../run=42/proof', '"run=42/proof"', 'run=42/proof',
            r'"D:\run=42\proof"', 'd:/run=42/proof', '/work/run=420/proof', 'run=420/proof',
        ]))
        output = self.cli("docs/verification.md", roots=("/work/run=42", "run=42", "docs/run=42", "d:/run=42"), expected=1)
        self.assertEqual(set(output.splitlines()[:-1]),
                         {f"docs/verification.md:{number}: temporary reference" for number in range(1, 9)})

    def test_bare_assignments_to_explicit_paths_and_uris(self):
        self.write("docs/verification.md", '\n'.join([
            'RESULT=../run=42/proof', 'RESULT=file:/tmp/proof?format=json',
            r'RESULT=C:\Users\Alice\AppData\Local\Temp\run=42\proof',
            'RESULT=https://example.org/path?proof=/tmp/run',
            '"RESULT=https://example.org/path?proof=/tmp/run"',
        ]))
        output = self.cli("docs/verification.md", roots=("run=42",), expected=1)
        self.assertEqual(set(output.splitlines()[:-1]),
                         {f"docs/verification.md:{number}: temporary reference" for number in range(1, 4)})

    def test_invalid_root_and_temporary_root_are_incomplete(self):
        self.write("README.md", "clean")
        self.cli("README.md", root=self.base / "missing-project", expected=2)
        self.cli("README.md", roots=("",), expected=2)
        self.cli("README.md", roots=("https://example.org/tmp",), expected=2)

    def test_selected_durable_files_must_not_be_within_supplied_disposable_roots(self):
        self.write("README.md", "Clean ordinary prose.")
        self.write("docs/verification.md", "Clean ordinary prose.")
        self.cli("README.md")  # The project itself may live in an OS temp directory.
        for directory in (".", str(self.root), "docs"):
            with self.subTest(directory=directory):
                output = self.cli("README.md", "docs/verification.md", roots=(directory,), expected=2)
                self.assertIn("Selected 2 file(s); checked 0 file(s).", output)

    def test_reference_result_is_independent_of_temporary_target_existence(self):
        self.write("README.md", "[proof](scratch/run-1/proof.txt)\n")
        before = self.cli("README.md", roots=("scratch/run-1",), expected=1)
        self.write("scratch/run-1/proof.txt", "original evidence")
        self.assertEqual(before, self.cli("README.md", roots=("scratch/run-1",), expected=1))

    def test_missing_directory_fifo_unreadable_and_invalid_utf8_are_incomplete(self):
        self.write("directory/file.md", "clean")
        unreadable = self.write("unreadable.md", "clean")
        unreadable.chmod(0)
        self.addCleanup(unreadable.chmod, 0o600)
        self.write("bytes.md", "").write_bytes(b"private-secret-decoder-bytes\xff")
        names = ["missing.md", "directory", "unreadable.md", "bytes.md"]
        if hasattr(os, "mkfifo"):
            os.mkfifo(self.root / "pipe")
            names.append("pipe")
        output = self.cli(*names, expected=2)
        self.assertIn(f"Selected {len(names)} file(s); checked 0 file(s).", output)
        self.assertNotIn("private-secret", output)

    def test_out_of_root_and_file_or_ancestor_symlinks_are_incomplete(self):
        inside = self.write("inside.md", "clean")
        outside = self.base / "outside.md"
        outside.write_text("outside-secret", encoding="utf-8")
        (self.root / "link.md").symlink_to(inside)
        (self.root / "directory-link").symlink_to(self.root, target_is_directory=True)
        output = self.cli("../outside.md", str(outside), "link.md", "directory-link/inside.md",
                          "directory-link/../inside.md", expected=2)
        self.assertIn("checked 0 file(s)", output)
        self.assertNotIn(str(self.base), output)
        self.assertNotIn("outside-secret", output)

    def test_root_itself_may_be_resolved_once(self):
        self.write("README.md", "clean")
        alias = self.base / "root-alias"
        alias.symlink_to(self.root, target_is_directory=True)
        self.cli("README.md", root=alias)

    def test_partial_failure_takes_precedence_and_diagnostics_are_sorted_deduplicated(self):
        self.write("b.md", "/tmp/secret-proof /tmp/another-secret\n")
        self.write("a.md", "/var/tmp/secret-proof\n")
        output = self.cli("b.md", "a.md", "b.md", "missing.md", expected=2)
        self.assertEqual(output, "a.md:1: temporary reference\nb.md:1: temporary reference\n"
                         "missing.md:1: incomplete file inspection\nSelected 3 file(s); checked 2 file(s).\n")
        self.assertEqual(output, self.cli("missing.md", "b.md", "a.md", expected=2))

    def test_no_source_snippets_or_matched_paths_and_no_write_operations(self):
        self.write("README.md", "private-secret-content /tmp/private-secret-proof\n")
        # A Python audit hook observes write attempts, including transient writes;
        # subprocess -B also forbids incidental bytecode files outside the project.
        audit = self.base / "audit.py"
        audit.write_text("import os, runpy, sys\n"
                         "def observe(event, args):\n"
                         "    if event == 'open' and isinstance(args[2], int) and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND):\n"
                         "        raise RuntimeError('unexpected write')\n"
                         "    if event in ('os.remove', 'os.rename', 'os.mkdir', 'os.rmdir', 'os.chmod', 'os.truncate', 'os.link', 'os.symlink'):\n"
                         "        raise RuntimeError('unexpected mutation')\n"
                         "sys.addaudithook(observe)\n"
                         "runpy.run_path(sys.argv.pop(1), run_name='__main__')\n", encoding="utf-8")
        result = subprocess.run([sys.executable, "-B", str(audit), str(self.helper), "--root", str(self.root), "--", "README.md"],
                                cwd=self.base, capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout, "README.md:1: temporary reference\nSelected 1 file(s); checked 1 file(s).\n")
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["README.md"])


if __name__ == "__main__":
    unittest.main()
