#!/usr/bin/env python3
"""Check explicitly selected UTF-8 files for references to disposable directories.

Usage: python3 check-temporary-references.py --root PROJECT
       [--temporary-root EXACT_ROOT ...] -- README.md docs/verification.md

Temporary roots need not exist; relative roots are relative to PROJECT. The root
is resolved once, but selected files and their ancestors must not be symlinks.
Selected durable files must be outside every explicitly supplied temporary root.
No directories, recursion, writes, Git, or external dependencies are used.
Exit 0 means clean, 1 means references, and 2 means incomplete input/inspection.
Diagnostics contain only selected relative filenames, line numbers and fixed
messages; the summary reports unique selected and successfully checked files.

This is a lexical check of whitespace/quote/Markdown-delimited paths, including
file: URIs, percent encoding and Windows/JSON backslashes. It recognizes common
OS temporary paths and exact supplied roots (including relative references from
each selected file). It does not parse formats, expand variables, follow links,
inspect referenced targets, or infer arbitrary disposable-directory names.
Paths containing literal whitespace must be quoted, backticked, bracketed as a
Markdown target, angle-delimited or percent encoded. Non-file URLs and variable-
only recipes are ignored. Delimited paths preserve punctuation; bare prose paths
omit trailing sentence punctuation. NAME= prefixes in references are recognized
only before absolute paths, ./ or ../ paths, and URIs. Supplied roots are always
literal. A clean result covers only the selected files.
"""

import argparse
import os
from pathlib import Path
import posixpath
import re
import stat
from urllib.parse import unquote, urlsplit


TOKENS = re.compile(r"[^\s\ufeff<>\[\](){}\"'`;,]+")
DELIMITED = re.compile(r'''(["'`])([^\r\n]*?)\1|<([^<>\r\n]*)>|\(([^()\r\n]*)\)''')
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*://")
DRIVE = re.compile(r"^[A-Za-z]:/")
POSIX_TEMP = re.compile(r"^/(?:tmp|private/tmp|(?:private/)?var/(?:tmp|folders))(?:/|$)")
WINDOWS_TEMP = re.compile(r"^[a-z]:/(?:users/[^/]+/appdata/local/temp|windows/temp)(?:/|$)", re.I)


def local_path(token, prose=True):
    if prose:
        token = token.rstrip(".!?:")
    if SCHEME.match(token) or token.lower().startswith("file:"):
        if not token.lower().startswith("file:"):
            return None
        try:
            uri = urlsplit(token)
        except ValueError:
            return None
        authority = uri.netloc if DRIVE.match(uri.netloc + uri.path) else "//" + uri.netloc
        token = (authority if uri.netloc.lower() not in ("", "localhost") else "") + uri.path
    token = re.sub(r"\\+", "/", unquote(token))
    if re.match(r"^/[A-Za-z]:/", token):
        token = token[1:]
    if not token or token.startswith(("$", "%")):
        return None
    return posixpath.normpath(token)


def beneath(path, directory):
    if DRIVE.match(directory):
        path, directory = path.casefold(), directory.casefold()
    return path == directory or path.startswith(directory.rstrip("/") + "/")


def path_candidates(line):
    end = 0
    for match in DELIMITED.finditer(line):
        yield from ((token, True) for token in TOKENS.findall(line[end:match.start()]))
        quoted, angle, target = match.groups()[1:]
        text = quoted or angle or target or ""
        yield text, False
        # A quoted sentence may contain paths; a leading path stays one literal.
        words = text.split(maxsplit=1)
        if len(words) == 2 and not any(separator in words[0] for separator in "/\\"):
            yield from ((token, True) for token in TOKENS.findall(text) if "/" in token or "\\" in token)
        end = match.end()
    yield from ((token, True) for token in TOKENS.findall(line[end:]))


def has_reference(line, parent, temporary_roots):
    for token, prose in path_candidates(line):
        # A named assignment may carry a path; '=' inside a path/URI stays literal.
        token = re.sub(r"^[A-Za-z_][A-Za-z0-9_]*=(?=/|[A-Za-z]:[\\/]|\.{1,2}[\\/]|[A-Za-z][A-Za-z0-9+.-]*:)", "", token)
        path = local_path(token, prose=prose)
        if path is None:
            continue
        if POSIX_TEMP.match(path) or WINDOWS_TEMP.match(path):
            return True
        absolute = path if path.startswith("/") or DRIVE.match(path) else posixpath.normpath(parent + "/" + path)
        if any(beneath(absolute, directory) for directory in temporary_roots):
            return True
    return False


def read_selected(root, selection):
    candidate = root / selection
    relative = Path(os.path.abspath(candidate)).relative_to(root)
    # Inspect the uncollapsed ancestors too: link/../file is still a symlink path.
    for ancestor in (candidate, *candidate.parents):
        if ancestor == root:
            break
        if ancestor.is_symlink():
            raise ValueError
    mode = candidate.stat().st_mode
    if not stat.S_ISREG(mode) or not mode & 0o444:
        raise ValueError
    return relative.as_posix(), candidate.read_text(encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", required=True)
    parser.add_argument("--temporary-root", action="append", default=[])
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()
    selections = sorted(set(args.files))
    checked, issues, incomplete = set(), set(), False
    try:
        root = Path(args.root).resolve(strict=True)
        if not args.root or not root.is_dir() or not selections:
            raise ValueError
        temporary_roots = []
        for value in args.temporary_root:
            path = local_path(value, prose=False)
            if path is None:
                raise ValueError
            temporary_roots.append(path if path.startswith("/") or DRIVE.match(path) else posixpath.normpath(root.as_posix() + "/" + path))
        if any(beneath(Path(os.path.abspath(root / selection)).as_posix(), directory)
               for selection in selections for directory in temporary_roots):
            raise ValueError
    except (OSError, ValueError, RuntimeError):
        print("ERROR: incomplete check; invalid roots, empty selection, or disposable selected file.")
        print(f"Selected {len(selections)} file(s); checked 0 file(s).")
        return 2
    for selection in selections:
        try:
            name, contents = read_selected(root, selection)
        except (OSError, ValueError, UnicodeError):
            incomplete = True
            # Never expose an out-of-root path, exception text or decoder bytes.
            try:
                name = Path(os.path.abspath(root / selection)).relative_to(root).as_posix()
            except ValueError:
                name = "(selection)"
            name = ascii(name)[1:-1]
            issues.add(f"{name}:1: incomplete file inspection")
            continue
        checked.add(name)
        for number, line in enumerate(contents.splitlines(), 1):
            if has_reference(line, (root / name).parent.as_posix(), temporary_roots):
                issues.add(f"{ascii(name)[1:-1]}:{number}: temporary reference")
    for issue in sorted(issues):
        print(issue)
    print(f"Selected {len(selections)} file(s); checked {len(checked)} file(s).")
    return 2 if incomplete else 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
