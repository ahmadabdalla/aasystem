#!/usr/bin/env python3
"""Read-only Git working-tree fingerprint. No copies, execution or deletion.

Print JSON to stdout; --check compares it with a previously saved fingerprint.
Include required ignored/external files with repeated --required FILE arguments.
Python 3.10+, Git. Source writers must be stopped by the caller.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys


def git(root, *args):
    result = subprocess.run(['git', '-C', str(root), *args], capture_output=True)
    if result.returncode:
        raise ValueError(result.stderr.decode(errors='replace').strip())
    return result.stdout


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def file_identity(path, required=False):
    for parent in path.parents:
        if parent.is_symlink():
            raise ValueError(f'symlink ancestor needs project-specific identity: {path}')
    try:
        before = path.lstat()
    except FileNotFoundError:
        if required:
            raise ValueError(f'missing required input: {path}')
        return {'missing': True}
    if not stat.S_ISREG(before.st_mode):
        raise ValueError(f'nonregular input needs project-specific identity: {path}')
    flags = os.O_RDONLY | os.O_NONBLOCK | getattr(os, 'O_NOFOLLOW', 0)
    with os.fdopen(os.open(path, flags), 'rb') as stream:
        opened = os.fstat(stream.fileno())
        if not stat.S_ISREG(opened.st_mode):
            raise ValueError(f'nonregular input: {path}')
        hasher = hashlib.sha256()
        size = 0
        while block := stream.read(1024 * 1024):
            size += len(block)
            if size > opened.st_size:
                raise ValueError(f'input grew while hashing: {path}')
            hasher.update(block)
        after = os.fstat(stream.fileno())
    signature = lambda info: (info.st_dev, info.st_ino, info.st_mode, info.st_size,
                              info.st_mtime_ns, info.st_ctime_ns)
    if (size != opened.st_size or signature(before) != signature(opened)
            or signature(opened) != signature(after)
            or signature(after) != signature(path.lstat())):
        raise ValueError(f'input changed while hashing: {path}')
    return {'sha256': hasher.hexdigest(), 'size': size, 'mode': stat.S_IMODE(after.st_mode)}


def selected_paths(root):
    raw = git(root, 'ls-files', '-z', '--cached', '--others', '--exclude-standard')
    return {root / os.fsdecode(name) for name in raw.split(b'\0') if name}


def fingerprint(root, required):
    root = root.resolve(strict=True)
    top = Path(os.fsdecode(git(root, 'rev-parse', '--show-toplevel')).strip()).resolve()
    if root != top:
        raise ValueError('--root must be the Git working-tree root')
    paths = selected_paths(root)
    required_paths = {Path(os.path.abspath(root / name)) for name in required}
    entries = {}
    for path in sorted(paths | required_paths):
        name = str(path.relative_to(root)) if path.is_relative_to(root) else str(path)
        entries[name] = file_identity(path, path in required_paths)
    if paths != selected_paths(root):
        raise ValueError('input selection changed while hashing')
    body = {'root': str(root), 'required': sorted(map(str, required_paths)), 'inputs': entries}
    return {'schema': 1, 'id': digest(body), **body}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--required', action='append', default=None, metavar='FILE')
    parser.add_argument('--check', type=Path, metavar='PREVIOUS_JSON')
    args = parser.parse_args()
    try:
        previous = json.loads(args.check.read_text()) if args.check else None
        if args.check and not isinstance(previous, dict):
            raise ValueError('previous identity must be a JSON object')
        required = args.required if args.required is not None else (previous['required'] if previous else [])
        current = fingerprint(args.root, required)
        if previous is not None:
            body = {key: previous[key] for key in ('root', 'required', 'inputs')}
            if previous.get('schema') != 1 or previous.get('id') != digest(body):
                raise ValueError('malformed previous identity')
            if current != previous:
                print(json.dumps({'ok': False, 'error': 'tested inputs changed', 'id': current['id']}))
                return 1
        print(json.dumps(current, sort_keys=True))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'ok': False, 'error': str(exc)}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
