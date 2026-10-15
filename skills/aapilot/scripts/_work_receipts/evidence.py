"""Input identity, protected archives and immutable proof interpretation."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
from datetime import datetime
STATE_VERSION = 2
SNAPSHOT_VERSION = 1
VERSION = STATE_VERSION
ENTRY_PATH = Path(__file__).resolve().parent.parent / 'work_receipts.py'
SKILL_TREE = ENTRY_PATH.parents[2]

class Rejected(Exception):
    pass


def require(condition, message):
    if not condition:
        raise Rejected(message)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def inside(path, parent):
    return path == parent or parent in path.parents


def local(value, exists=True):
    require(isinstance(value, str) and value, 'nonempty absolute path required')
    path = Path(value)
    require(path.is_absolute() and '..' not in path.parts, f'absolute path without traversal required: {value}')
    for component in [path, *path.parents]:
        require(not component.is_symlink(), f'symlink input unsupported: {component}')
    if exists:
        require(path.exists(), f'missing input: {path}')
        mode = path.stat().st_mode
        require(stat.S_ISREG(mode) or stat.S_ISDIR(mode), f'special input unsupported: {path}')
        require(mode & 0o444, f'unreadable input: {path}')
        if stat.S_ISDIR(mode):
            require(mode & 0o111, f'unsearchable directory: {path}')
    return path


def fingerprint(path, missing=False):
    input_path = local(str(path), exists=not missing)
    if not input_path.exists():
        return {'missing': True}
    require(input_path.is_file(), f'file required: {input_path}')
    data = input_path.read_bytes()
    return {'sha256': hashlib.sha256(data).hexdigest(), 'mode': stat.S_IMODE(input_path.stat().st_mode), 'size': len(data)}


def read_json(path):
    input_path = local(str(path))
    require(input_path.is_file(), f'JSON file required: {input_path}')
    return json.loads(input_path.read_text())


def text_fields(obj, fields):
    for key in fields:
        require(isinstance(obj.get(key), str) and bool(obj[key].strip()), f'nonempty {key} required')


def string_list(value, name, nonempty=False):
    require(
        isinstance(value, list) and all((isinstance(x, str) and x for x in value)),
        f'{name} must be a string list',
    )
    require(len(value) == len(set(value)) and (value or not nonempty), f'{name} duplicates or empty')
    return value


def utc(value):
    require(isinstance(value, str), 'deadline_utc must be an ISO UTC timestamp')
    deadline = datetime.fromisoformat(value.replace('Z', '+00:00'))
    require(
        deadline.tzinfo is not None and deadline.utcoffset().total_seconds() == 0,
        'deadline_utc must use UTC',
    )
    return deadline


def budget(value):
    require(isinstance(value, dict), 'budget required')
    require(
        type(value.get('dispatches')) is int and value['dispatches'] >= 0,
        'dispatches must be a nonnegative integer',
    )
    utc(value.get('deadline_utc'))


def file_refs(values, name):
    for value in string_list(values, name):
        fingerprint(value)


def implementation_files():
    package = local(str(ENTRY_PATH.parent / '_work_receipts'))
    paths = [ENTRY_PATH]
    for folder, directories, filenames in os.walk(package, followlinks=False):
        current = Path(folder)
        for directory in directories:
            local(str(current / directory))
        paths.extend((current / name for name in filenames if name.endswith('.py')))
    for path in paths:
        fingerprint(path)
    return sorted(paths, key=str)


def brief_refs(brief):
    refs = [brief['authority_source'], brief['environment'], *[str(path) for path in implementation_files()]]
    for name in ('requirements', 'decisions', 'procedures', 'principles'):
        refs.extend(brief[name])
    refs.extend(brief['source'].get('required', []))
    return sorted(set(refs))


def validate_brief(brief, state_path):
    text_fields(brief, ('id', 'owner', 'objective', 'authority_source', 'environment', 'next_action'))
    root = local(brief['project_root'])
    require(root.is_dir(), 'project_root must be a directory')
    for name in ('requirements', 'decisions', 'procedures', 'principles'):
        file_refs(brief.get(name), name)
    require(brief['requirements'], 'at least one requirements reference required')
    fingerprint(brief['authority_source'])
    fingerprint(brief['environment'])
    read_json(brief['environment'])
    string_list(brief.get('actions'), 'actions', True)
    string_list(brief.get('claims'), 'claims')
    require(brief.get('purpose') in ('implementation', 'verification', 'other'), 'explicit purpose required')
    require(brief.get('required_review_mode', 'independent-discovery') in ('independent-discovery', 'confirmation-audit'), 'invalid required_review_mode')
    string_list(brief.get('checkpoints'), 'checkpoints')
    obligations = brief.get('checkpoint_obligations', [])
    require(isinstance(obligations, list), 'checkpoint_obligations must be a list')
    for obligation in obligations:
        require(obligation.get('id') in brief['checkpoints'] and obligation.get('before') in ('implementation', 'acceptance'), 'invalid checkpoint obligation')
    require(len({(o['id'], o['before']) for o in obligations}) == len(obligations), 'duplicate checkpoint obligation')
    require(brief.get('proof_kind') in ('scoped', 'production'), 'invalid proof_kind')
    require(brief['proof_kind'] != 'production' or bool(brief['claims']), 'production requires nonempty claims')
    for key in ('constraints', 'expected_outputs'):
        require(key in brief, f'{key} required')
    resources = brief.get('resources')
    require(isinstance(resources, dict) and resources, 'resources map required')
    for key, value in resources.items():
        require(isinstance(key, str) and key and isinstance(value, str), 'invalid resource mapping')
        if value.startswith('named:'):
            require(len(value) > 6, 'empty named resource')
        else:
            local(value)
    budget(brief.get('budget'))
    source = brief.get('source', {})
    require(source.get('mode') in ('git', 'roots'), 'source mode must be git or roots')
    for name in ('exclude', 'required'):
        string_list(source.get(name, []), f'source.{name}')
    for value in source.get('exclude', []):
        local(value, exists=False)
    for value in source.get('required', []):
        fingerprint(value)
    if source['mode'] == 'roots':
        for value in string_list(source.get('roots'), 'source.roots', True):
            local(value)
    run = state_path.parent
    require(not inside(state_path, SKILL_TREE), 'runtime state cannot be in the loaded skill tree')
    require(run != root and (not inside(root, run)), 'runtime directory cannot contain the project')
    for ref in brief_refs(brief):
        require(not inside(local(ref), run), f'required input inside runtime exclusion: {ref}')
    exclusions = [local(v, False) for v in source.get('exclude', [])] + [run]
    for ref in brief_refs(brief):
        require(not any((inside(local(ref), e) for e in exclusions)), f'required input excluded: {ref}')


def input_manifest(state):
    brief = state['brief']
    root = local(brief['project_root'])
    source = brief['source']
    excludes = [local(v, False) for v in source.get('exclude', [])] + [Path(state['runtime_directory'])]
    paths = set()
    if source['mode'] == 'git':
        result = subprocess.run(['git', '-C', str(root), 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], capture_output=True, check=False)
        require(result.returncode == 0, 'git source discovery failed')
        paths.update((root / os.fsdecode(v) for v in result.stdout.split(b'\x00') if v))
    else:
        for value in source['roots']:
            source_path = local(value)
            if source_path.is_file():
                paths.add(source_path)
            else:
                for folder, directories, filenames in os.walk(source_path, followlinks=False):
                    current = Path(folder)
                    directories[:] = [
                        directory
                        for directory in directories
                        if not any(inside(current / directory, excluded) for excluded in excludes)
                    ]
                    for directory in directories:
                        local(str(current / directory))
                    paths.update((current / filename for filename in filenames))
    paths = {
        source_path
        for source_path in paths
        if not any(inside(source_path, excluded) for excluded in excludes)
    }
    required = set(brief_refs(brief))
    paths.update((Path(v) for v in required))
    for task in state['tasks'].values():
        required.update(task.get('inputs', []))
        paths.update((Path(v) for v in task.get('inputs', [])))
        if task.get('procedure'):
            paths.add(Path(task['procedure']))
            required.add(task['procedure'])
    for value in required:
        fingerprint(value)
    return {str(source_path): fingerprint(source_path, missing=True) for source_path in sorted(paths, key=str)}


def changed(old, new):
    return sorted((k for k in old.keys() | new.keys() if old.get(k) != new.get(k)))


def check_snapshot(state, path, current=True, current_authority=True):
    require(
        inside(local(path), Path(state['runtime_directory'])),
        'snapshot manifest must be in runtime directory',
    )
    manifest = read_json(path)
    require(manifest.get('schema_version') == SNAPSHOT_VERSION, 'unsupported snapshot schema')
    require(manifest.get('run') == state['brief']['id'], 'snapshot belongs to another run')
    if current_authority:
        require(
            manifest.get('authority_revision') == state['authority_revision'],
            'snapshot predates current authority revision',
        )
    require(manifest.get('id') == digest(manifest['inputs']), 'snapshot identity is malformed')
    if current:
        paths = changed(manifest['inputs'], input_manifest(state))
        require(not paths, 'stale source inputs: ' + ', '.join(paths))
    archive = local(str(Path(path).parent))
    for source, metadata in manifest['inputs'].items():
        if not metadata.get('missing'):
            relative = Path(manifest['copies'][source])
            require(
                not relative.is_absolute() and '..' not in relative.parts and (relative.parts[0] == 'files'),
                'invalid protected copy path',
            )
            copied = archive / relative
            require(fingerprint(copied) == metadata, f'protected snapshot changed: {source}')
    return manifest


def read_report_record(state, path):
    report = read_json(path)
    text_fields(report, ('id', 'task', 'producer', 'host_ref'))
    require(report['task'] in state['tasks'], 'report task not assigned')
    refs = [str(local(path)), report['host_ref']]
    for name in ('artifacts', 'evidence'):
        values = report.get(name, [])
        file_refs(values, name)
        refs.extend(values)
    if report.get('snapshot'):
        refs.append(report['snapshot'])
    for name in ('environment', 'verifier'):
        if report.get(name):
            refs.append(report[name])
    context = report.get('context', {})
    if isinstance(context, dict):
        for exposure in context.get('exposures', []):
            refs.append(exposure['source_ref'])
    hashes = {v: fingerprint(v) for v in refs}
    record = {'report': report, 'hashes': hashes, 'authority_revision': state['authority_revision']}
    previous = state['reports'].get(report['id'])
    require(previous is None or previous == record, 'conflicting repeated report ID')
    return (report['id'], record)


def check_record(record):
    paths = [p for p, expected in record['hashes'].items() if fingerprint(p, True) != expected]
    require(not paths, 'stale report/evidence inputs: ' + ', '.join(paths))


def snapshot(state, task, out, write_manifest):
    require(task in state['tasks'], 'unknown task')
    require(
        inside(out, Path(state['runtime_directory'])) and out != Path(state['runtime_directory']),
        'snapshot must be inside runtime directory',
    )
    require(not out.exists(), 'snapshot output already exists')
    before = input_manifest(state)
    try:
        (out / 'files').mkdir(parents=True)
        copies = {}
        for index, (source, metadata) in enumerate(before.items()):
            if metadata.get('missing'):
                continue
            destination = Path('files') / f'{index:06d}'
            shutil.copyfile(source, out / destination)
            os.chmod(out / destination, metadata['mode'])
            require(fingerprint(out / destination) == metadata, f'input changed during copy: {source}')
            copies[source] = str(destination)
        after = input_manifest(state)
        require(before == after, 'source changed during snapshot: ' + ', '.join(changed(before, after)))
        manifest = {
            'schema_version': SNAPSHOT_VERSION,
            'run': state['brief']['id'],
            'task': task,
            'authority_revision': state['authority_revision'],
            'state_revision': state['revision'],
            'id': digest(before),
            'inputs': before,
            'copies': copies,
            'source_mode': state['brief']['source']['mode'],
            'exclusions': state['brief']['source'].get('exclude', []) + state['automatic_exclusions'],
        }
        write_manifest(out / 'manifest.json', manifest)
        return {
            'manifest': str(out / 'manifest.json'),
            'id': manifest['id'],
            'source_mode': manifest['source_mode'],
            'exclusions': manifest['exclusions'],
        }
    except Exception:
        if out.exists():
            shutil.rmtree(out)
        raise
