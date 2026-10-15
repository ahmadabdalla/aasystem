"""Mutable run lifecycle and the lock, validate, commit transaction."""
from __future__ import annotations
import copy
import json
import os
from pathlib import Path
import tempfile
from datetime import datetime, timezone
from contextlib import contextmanager
from . import gates as policy
from .gates import proof_errors
from .evidence import (
    VERSION,
    SKILL_TREE,
    Rejected,
    require,
    digest,
    inside,
    local,
    fingerprint,
    read_json,
    text_fields,
    string_list,
    utc,
    file_refs,
    validate_brief,
    input_manifest,
    check_snapshot,
    read_report_record,
    check_record,
    snapshot,
)


def descendants(state, task_id):
    result = []
    for other_task in state['tasks'].values():
        parent = other_task.get('parent')
        while parent:
            if parent == task_id:
                result.append(other_task)
                break
            parent = state['tasks'][parent].get('parent')
    return result


def compatible_replacement(original, replacement):
    return (
        original.get('parent') is not None
        and replacement.get('parent') == original['parent']
        and set(replacement['actions']) <= set(original['actions'])
        and set(replacement['resources']) <= set(original['resources'])
        and set(original['claims']) <= set(replacement['claims'])
        and (original['proof_kind'] != 'production' or replacement['proof_kind'] == 'production')
        and (original.get('required_review_mode', 'independent-discovery') != 'independent-discovery' or replacement.get('required_review_mode', 'independent-discovery') == 'independent-discovery')
        and (not original.get('required', True) or replacement.get('required', True))
    )


def accepted_replacement(state, task, seen=None):
    seen = set() if seen is None else seen
    if task['id'] in seen:
        return False
    seen = seen | {task['id']}
    for replacement in state['tasks'].values():
        if replacement.get('supersedes') == task['id'] and compatible_replacement(task, replacement):
            if replacement['status'] == 'accepted' or accepted_replacement(state, replacement, seen):
                return True
    return False


def receipt_errors(state, task):
    """Keep accepted history intact without requiring its old live source forever."""
    errors = []
    if task['status'] != 'accepted' or not task.get('acceptance'):
        return errors
    for path, expected in task['acceptance']['evidence'].items():
        if fingerprint(path, True) != expected:
            errors.append(f"{task['id']}: stale accepted evidence: {path}")
    try:
        require(
            task['acceptance'].get('authority_revision') == state['authority_revision'],
            'acceptance predates resume',
        )
        policy.check_decision_review(state, task['acceptance'].get('decision_review'), task, current=False)
        for report_id in set(task['returns']) | set(task['acceptance'].get('proof_reports', [])):
            record = state['reports'][report_id]
            check_record(record)
            if record['report'].get('snapshot'):
                check_snapshot(state, record['report']['snapshot'], current=False, current_authority=False)
    except (Rejected, KeyError, TypeError, ValueError, OSError) as exc:
        errors.append(f"{task['id']}: {exc}")
    errors.extend(proof_errors(state, task['id'], current=False))
    return errors


def resumption_errors(state):
    errors = []
    for resumed in state['resumptions']:
        try:
            checkpoint = resumed['checkpoint']
            require(fingerprint(checkpoint['package'], True) == checkpoint['hash'], 'checkpoint package changed')
            require(fingerprint(resumed['human_response'], True) == resumed['hash'], 'human response changed')
            policy.check_hashes(resumed['hashes'])
        except (Rejected, KeyError, TypeError, ValueError, OSError) as exc:
            errors.append('stale resumption evidence: ' + str(exc))
    return errors


def resources_overlap(state, left, right):
    return policy.resources_overlap(state, left, right)


def gates(state, task_id):
    errors = proof_errors(state, task_id)
    errors.extend(resumption_errors(state))
    try:
        policy.check_decision_review(state, state['tasks'][task_id].get('decision_review'), state['tasks'][task_id])
    except (Rejected, KeyError, TypeError, ValueError, OSError) as exc:
        errors.append(str(exc))
    if state['checkpoint']:
        errors.append('human checkpoint is pending')
    task = state['tasks'][task_id]
    if any(t.get('purpose') == 'implementation' for t in [task, *descendants(state, task_id)]):
        try:
            policy.check_obligations(state, 'implementation')
        except (Rejected, KeyError, TypeError, ValueError, OSError) as exc:
            errors.append(str(exc))
    if datetime.now(timezone.utc) >= utc(task['deadline_utc']):
        errors.append('deadline expired')
    if task['status'] == 'cancelled':
        errors.append('task is cancelled')
    for other_task in [task, *descendants(state, task_id)]:
        for attempt in state['attempts'].values():
            if attempt['task'] == other_task['id']:
                if 'outcome' not in attempt:
                    errors.append('pending native reservation: ' + attempt['id'])
                else:
                    try:
                        policy.check_hashes(attempt['hashes'])
                    except (Rejected, OSError, ValueError) as exc:
                        errors.append(str(exc))
        if other_task.get('uncertain'):
            errors.append(f"uncertain effects: {other_task['id']}")
        if other_task['id'] == task_id or other_task.get('required', True):
            errors.extend(receipt_errors(state, other_task))
        if other_task['id'] != task_id and other_task.get('required', True):
            if accepted_replacement(state, other_task):
                continue
            if other_task['status'] == 'cancelled':
                errors.append(f"required task cancelled: {other_task['id']}")
            elif other_task['status'] not in ('returned', 'accepted'):
                errors.append(f"unsettled task: {other_task['id']}")
            if other_task.get('claims') and other_task.get('role') != 'verifier' and (other_task['status'] != 'accepted'):
                errors.extend(proof_errors(state, other_task['id']))
    return errors


def can_act(state, event):
    require(event['task'] in state['tasks'], 'unknown task')
    task = state['tasks'][event['task']]
    allowed = {task['owner']}
    if task.get('parent'):
        allowed.add(state['tasks'][task['parent']]['owner'])
    require(event['actor'] in allowed, 'actor is not task/parent owner')
    return task


def assign_task(state, task, event):
    assignment = copy.deepcopy(event['assignment'])
    text_fields(assignment, ('id', 'parent', 'owner', 'objective', 'procedure'))
    require(event['actor'] == task['owner'], 'only parent owner assigns')
    require(
        assignment['parent'] == task['id'] and assignment['id'] not in state['tasks'],
        'invalid parent/duplicate task',
    )
    fingerprint(assignment['procedure'])
    for key in ('actions', 'resources', 'claims'):
        string_list(assignment.get(key), key, key == 'actions')
    for key in ('actions', 'resources'):
        parent_values = task[key] if isinstance(task[key], list) else list(task[key])
        require(set(assignment[key]) <= set(parent_values), f'child {key} widen parent authority')
    require(assignment.get('purpose') in ('implementation', 'verification', 'other'), 'explicit purpose required')
    require(assignment.get('required_review_mode', 'independent-discovery') in ('independent-discovery', 'confirmation-audit'), 'invalid required_review_mode')
    if assignment['purpose'] == 'implementation':
        policy.check_decision_review(state, assignment.get('decision_review'), assignment, implementation=True)
    if assignment['purpose'] == 'verification':
        review = assignment.get('review', {})
        require(review.get('target') in state['tasks'] and review.get('mode') in ('independent-discovery', 'confirmation-audit'), 'verification review target/mode required')
        string_list(review.get('claims'), 'review claims')
        require(set(review['claims']) <= set(state['tasks'][review['target']]['claims']), 'review claims outside target')
    require(assignment.get('proof_kind') in ('scoped', 'production'), 'invalid proof_kind')
    require('budget' not in assignment, 'child budget is inherited, not redefinable')
    file_refs(assignment.get('inputs'), 'inputs')
    string_list(assignment.get('expected_artifacts'), 'expected_artifacts')
    required_inputs = [assignment['procedure'], *assignment['inputs']]
    exclusions = [
        Path(state['runtime_directory']),
        *[Path(v) for v in state['brief']['source'].get('exclude', [])],
    ]
    require(
        not any(
            inside(Path(ref), excluded)
            for ref in required_inputs
            for excluded in exclusions
        ),
        'assignment inputs cannot be excluded; use external immutable briefs',
    )
    deadline = assignment.get('deadline_utc', task['deadline_utc'])
    require(utc(deadline) <= utc(task['deadline_utc']), 'child deadline widens parent')
    require(datetime.now(timezone.utc) < utc(deadline), 'child deadline expired')
    for other_task in state['tasks'].values():
        require(
            not (other_task.get('uncertain') and resources_overlap(state, other_task['resources'], assignment['resources'])),
            f"uncertain effects block retry: {other_task['id']}",
        )
    require(state['dispatched'] < state['brief']['budget']['dispatches'], 'root dispatch budget exhausted')
    if assignment.get('supersedes'):
        require(assignment['supersedes'] in state['tasks'], 'unknown superseded task')
        require(
            compatible_replacement(state['tasks'][assignment['supersedes']], assignment),
            'incompatible superseding assignment: parent, authority, claims, proof kind or required obligation',
        )
    assignment.update(status='assigned', deadline_utc=deadline, required=assignment.get('required', True), returns=[], uncertain=False)
    state['tasks'][assignment['id']] = assignment
    state['dispatched'] += 1
    state['attempts'][assignment['id']] = {'id': assignment['id'], 'task': assignment['id'], 'operation': 'spawn'}


def dispatch_ready(state, task):
    require(not state['checkpoint'], 'human checkpoint pending')
    require(task['status'] in ('assigned', 'returned'), 'task is closed')
    require(datetime.now(timezone.utc) < utc(task['deadline_utc']), 'deadline expired')
    require(not any(t.get('uncertain') and resources_overlap(state, t['resources'], task['resources']) for t in state['tasks'].values()), 'uncertain effects block dispatch')
    if task.get('purpose') == 'implementation':
        policy.check_decision_review(state, task.get('decision_review'), task, implementation=True)
    if task.get('purpose') == 'verification':
        require(task.get('preflight'), 'review preflight required before verifier dispatch')
        policy.check_hashes(task['preflight']['hashes'])
        check_snapshot(state, task['preflight']['snapshot'])
        require(not task.get('initial_findings'), 'new review attempt required after frozen findings')


def dispatch_errors(state, task):
    errors = []
    if not any(a['task'] == task['id'] and 'outcome' not in a for a in state['attempts'].values()):
        errors.append('pending native reservation required')
    try:
        dispatch_ready(state, task)
    except (Rejected, KeyError, TypeError, ValueError, OSError) as exc:
        errors.append(str(exc))
    return errors


def reserve_followup(state, task, event):
    text_fields(event, ('attempt_id', 'reason', 'worker_id'))
    require(event.get('operation') == 'followup', 'only followup needs extra reservation')
    require(event['attempt_id'] not in state['attempts'], 'duplicate native attempt reservation')
    policy.started_dispatch(state, task, event['worker_id'])
    dispatch_ready(state, task)
    require(state['dispatched'] < state['brief']['budget']['dispatches'], 'root dispatch budget exhausted')
    require(task['status'] in ('assigned', 'returned'), 'followup requires live assignment')
    state['attempts'][event['attempt_id']] = {'id': event['attempt_id'], 'task': task['id'], 'operation': 'followup', 'worker_id': event['worker_id'], 'reason': event['reason']}
    state['dispatched'] += 1


def record_dispatch(state, task, event):
    require(event.get('attempt_id') in state['attempts'], 'pre-call reservation required')
    attempt = state['attempts'][event['attempt_id']]
    require(attempt['task'] == task['id'] and attempt['operation'] == event.get('operation'), 'native attempt/task/operation mismatch')
    require('outcome' not in attempt, 'native attempt receipt already recorded')
    require(event.get('outcome') in ('started', 'failed', 'unknown'), 'native outcome required')
    text_fields(event, ('request_ref', 'host_ref'))
    if event['outcome'] == 'started':
        dispatch_ready(state, task)
        text_fields(event, ('worker_id',))
        if attempt['operation'] == 'followup':
            require(event['worker_id'] == attempt['worker_id'], 'followup worker mismatch')
        elif any(a.get('worker_id') == event['worker_id'] and a.get('operation') == 'spawn' for a in state['attempts'].values() if a is not attempt):
            require(False, 'spawn requires fresh native worker')
    elif attempt['operation'] == 'followup':
        require(event.get('worker_id') in (None, attempt['worker_id']), 'followup worker mismatch')
    if task.get('purpose') == 'verification' and event['outcome'] == 'started':
        require(event['request_ref'] == task['preflight']['host_request_ref'], 'native request differs from preflight')
    # Failed/unknown actual calls must remain recordable after a prospective
    # gate closes. They retain the charge and uncertainty, never authorize work.
    hashes = policy.retained([event['request_ref'], event['host_ref']])
    attempt.update(outcome=event['outcome'], worker_id=event.get('worker_id'), event=event['id'], request_ref=event['request_ref'], host_ref=event['host_ref'], hashes=hashes)
    if event['outcome'] == 'unknown':
        task['uncertain'] = True


def record_preflight(state, task, event):
    require(task.get('purpose') == 'verification', 'preflight requires verification assignment')
    require(not task.get('preflight'), 'review preflight immutable; new assignment required')
    require(not any(a['task'] == task['id'] and 'outcome' in a for a in state['attempts'].values()), 'preflight must precede native dispatch')
    require(event.get('mode') == task['review']['mode'], 'preflight review mode mismatch')
    manifest = check_snapshot(state, event['snapshot'])
    require(manifest['task'] == task['id'], 'snapshot must cover verifier assignment')
    require(event.get('environment') == state['brief']['environment'], 'preflight environment mismatch')
    policy.validate_context(event.get('context'))
    refs = [event['snapshot'], event['environment'], event['host_request_ref'], *[e['source_ref'] for e in event['context']['exposures']]]
    task['preflight'] = {**copy.deepcopy(event), 'hashes': policy.retained(refs)}


def record_initial_findings(state, task, event):
    require(task.get('purpose') == 'verification' and task.get('preflight'), 'review preflight required')
    require(not task.get('initial_findings'), 'initial findings immutable; new assignment required')
    require(event.get('preflight_event') == task['preflight']['id'], 'preflight event mismatch')
    attempts = policy.started_dispatch(state, task)
    require(any(a['event'] == event.get('dispatch_event') for a in attempts), 'started dispatch event mismatch')
    report_id, record = read_report_record(state, event['findings'])
    require(record['report']['task'] == task['id'], 'initial findings task mismatch')
    policy.started_dispatch(state, task, record['report']['producer'])
    policy.validate_context(event.get('context'), complete=True)
    policy.validate_context(record['report'].get('context'), complete=True)
    file_refs(event.get('context_evidence_refs'), 'context_evidence_refs')
    require(event['context_evidence_refs'], 'initial context evidence required')
    refs = [*event['context_evidence_refs'], *[e['source_ref'] for e in event['context']['exposures']], *[e['source_ref'] for e in record['report']['context']['exposures']]]
    task['initial_findings'] = {'event': event['id'], 'record': record, 'context': copy.deepcopy(event['context']), 'hashes': policy.retained(refs)}
    state['reports'][report_id] = record


def record_return(state, task, event):
    require(task['status'] in ('assigned', 'returned'), 'task cannot return in current state')
    report_id, record = read_report_record(state, event['report'])
    if task.get('parent'):
        policy.started_dispatch(state, task, record['report']['producer'])
    if task.get('purpose') == 'verification':
        require(task.get('initial_findings') and record['report'].get('initial_findings_event') == task['initial_findings']['event'], 'initial findings required before return')
    state['reports'][report_id] = record
    require(state['reports'][report_id]['report']['task'] == task['id'], 'return task mismatch')
    if report_id not in task['returns']:
        task['returns'].append(report_id)
    task['status'] = 'returned'


def record_verification(state, task, event):
    require(
        event['target'] in state['tasks'] and event['verifier_task'] in state['tasks'],
        'unknown verification assignment',
    )
    target = state['tasks'][event['target']]
    verifier = state['tasks'][event['verifier_task']]
    require(event['actor'] == target['owner'], 'target owner records verification')
    require(verifier.get('parent') and verifier['id'] != target['id'], 'separate budgeted verifier required')
    report_id, record = read_report_record(state, event['report'])
    state['reports'][report_id] = record
    require(state['reports'][report_id]['report']['task'] == verifier['id'], 'verifier report task mismatch')
    require(verifier.get('purpose') == 'verification' and verifier['review']['target'] == target['id'], 'verification assignment target mismatch')
    policy.started_dispatch(state, verifier, record['report']['producer'])
    require(verifier.get('initial_findings'), 'frozen initial findings required')
    verifier['role'] = 'verifier'
    state['proofs'].append({'target': target['id'], 'verifier_task': verifier['id'], 'report': report_id})


def accept_task(state, task, event):
    require(event['actor'] == task['owner'], 'only owner accepts')
    text_fields(event, ('rationale',))
    file_refs(event.get('evidence_refs'), 'evidence_refs')
    require(bool(event['evidence_refs']), 'inspected evidence required')
    policy.check_decision_review(state, event.get('decision_review'), task)
    errors = gates(state, task['id'])
    require(not errors, '; '.join(errors))
    proof_reports = []
    proof_errors(state, task['id'], selected_reports=proof_reports)
    task['status'] = 'accepted'
    task['acceptance'] = {
        'rationale': event['rationale'],
        'decision_review': event['decision_review'],
        'evidence': {v: fingerprint(v) for v in event['evidence_refs']},
        'revision': state['revision'] + 1,
        'authority_revision': state['authority_revision'],
        'proof_reports': sorted(set(proof_reports)),
    }


def pause_at_checkpoint(state, task, event):
    require(not state['checkpoint'], 'checkpoint already pending')
    require(event['checkpoint_id'] in state['brief']['checkpoints'], 'undeclared checkpoint')
    text_fields(event, ('reason', 'decision'))
    package = policy.validate_package(state, event)
    state['checkpoint'] = {
        'id': event['checkpoint_id'],
        'event': event['id'],
        'content': package,
        'authority_revision': state['authority_revision'],
        'binding': policy.obligation_binding(state['brief']),
        'task': task['id'],
        'package': event['package'],
        'hash': fingerprint(event['package']),
        'reason': event['reason'],
        'decision': event['decision'],
    }


def validate_resumed_brief(state, updated_brief):
    """Return a validated copy without changing the run or its tasks."""
    brief = copy.deepcopy(updated_brief)
    validate_brief(brief, Path(state['state_path']))
    old = state['brief']
    for key in ('id', 'owner', 'project_root', 'resources', 'source', 'environment', 'proof_kind'):
        require(brief[key] == old[key], f'resume cannot change {key} in v0')
    require(set(brief['actions']) <= set(old['actions']), 'resume cannot widen actions')
    require({(o['id'], o['before']) for o in old.get('checkpoint_obligations', [])} <= {(o['id'], o['before']) for o in brief.get('checkpoint_obligations', [])}, 'resume cannot remove mandatory checkpoint obligations')
    require(old.get('required_review_mode', 'independent-discovery') != 'independent-discovery' or brief.get('required_review_mode', 'independent-discovery') == 'independent-discovery', 'resume cannot weaken required discovery')
    require(
        brief['budget']['dispatches'] <= old['budget']['dispatches'] and brief['budget']['dispatches'] >= state['dispatched'],
        'resume cannot widen/reset dispatch budget',
    )
    require(
        utc(brief['budget']['deadline_utc']) <= utc(old['budget']['deadline_utc']),
        'resume cannot extend deadline',
    )
    for other_task in state['tasks'].values():
        require(
            set(other_task['actions']) <= set(brief['actions']),
            'narrowed authority incompatible with existing task; new run required',
        )
    return brief


def resume_run(state, task, event):
    require(event['actor'] == state['brief']['owner'], 'only root owner resumes')
    require(state['checkpoint'] and event['checkpoint_id'] == state['checkpoint']['id'], 'checkpoint mismatch')
    require(
        fingerprint(state['checkpoint']['package'], True) == state['checkpoint']['hash'],
        'checkpoint package changed before resume',
    )
    require(
        type(event.get('authority_revision')) is int and event['authority_revision'] == state['authority_revision'],
        'authority revision mismatch',
    )
    response, response_hashes = policy.validate_response(state, event)
    if 'updated_brief' in event:
        brief = validate_resumed_brief(state, event['updated_brief'])
        state['brief'] = brief
        state['tasks'][brief['id']]['actions'] = brief['actions']
        state['tasks'][brief['id']]['claims'] = brief['claims']
        for other_task in state['tasks'].values():
            other_task['deadline_utc'] = min(other_task['deadline_utc'], brief['budget']['deadline_utc'], key=utc)
    state['resumptions'].append({'event': event['id'], 'checkpoint': state['checkpoint'], 'human_response': event['human_response'], 'hash': fingerprint(event['human_response']), 'response': response, 'hashes': response_hashes})
    state['checkpoint'] = None
    state['authority_revision'] += 1
    for other_task in state['tasks'].values():
        if other_task['status'] == 'accepted':
            other_task['status'] = 'returned'


def record_reconciliation(state, task, event):
    require(task.get('uncertain'), 'no uncertain effects to reconcile')
    file_refs(event.get('evidence_refs'), 'evidence_refs')
    require(
        bool(event['evidence_refs']) and event.get('observations'),
        'inspection evidence and observations required',
    )
    require(event.get('outcome') in ('known', 'unknown'), 'outcome must be known or unknown')
    require(type(event.get('worker_active')) is bool, 'worker_active boolean required')
    if event['outcome'] == 'known':
        require(event['worker_active'] is False, 'worker still active')
        task['uncertain'] = False
    task['reconciliation'] = {'outcome': event['outcome'], 'evidence': {v: fingerprint(v) for v in event['evidence_refs']}, 'observations': event['observations']}


def transition(state, event):
    text_fields(event, ('id', 'type', 'actor', 'task', 'source_ref'))
    fingerprint(event['source_ref'])
    task = can_act(state, event)
    kind = event['type']
    prospective = kind != 'dispatch' or event.get('outcome') == 'started'
    if prospective and kind in ('assign', 'accept', 'dispatch_reserved', 'dispatch', 'review_preflight'):
        require(not state['checkpoint'], 'human checkpoint pending')
        require(task['status'] not in ('cancelled', 'accepted'), 'task is closed')
        require(datetime.now(timezone.utc) < utc(task['deadline_utc']), 'deadline expired')
    if kind == 'assign':
        assign_task(state, task, event)
    elif kind == 'decision_review':
        require(event['actor'] == task['owner'], 'only task owner reviews decisions')
        hashes = policy.validate_decision_review(state, event)
        state['decision_reviews'][event['id']] = {**copy.deepcopy(event), 'hashes': hashes}
        task['decision_review'] = event['id']
    elif kind == 'dispatch_reserved':
        reserve_followup(state, task, event)
    elif kind == 'dispatch':
        record_dispatch(state, task, event)
    elif kind == 'review_preflight':
        record_preflight(state, task, event)
    elif kind == 'initial_findings':
        record_initial_findings(state, task, event)
    elif kind == 'returned':
        record_return(state, task, event)
    elif kind == 'verification':
        record_verification(state, task, event)
    elif kind == 'accept':
        accept_task(state, task, event)
    elif kind == 'checkpoint':
        pause_at_checkpoint(state, task, event)
    elif kind == 'resume':
        resume_run(state, task, event)
    elif kind == 'interrupted':
        for key in ('intended_effects', 'last_worker_ref', 'observations'):
            require(event.get(key), f'{key} required')
        task['uncertain'] = True
        task['interruption'] = {k: event[k] for k in ('intended_effects', 'last_worker_ref', 'observations')}
    elif kind == 'reconciled':
        record_reconciliation(state, task, event)
    elif kind == 'cancelled':
        text_fields(event, ('reason',))
        task['status'] = 'cancelled'
        task['cancellation'] = event['reason']
    else:
        raise Rejected('unsupported event type: ' + kind)


@contextmanager

def locked(state_path):
    state_path.parent.mkdir(parents=True, exist_ok=True)
    path = state_path.with_name(state_path.name + '.lock')
    try:
        descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise Rejected(f'lock exists; inspect owning process/effects before explicit recovery: {path}')
    try:
        os.write(descriptor, str(os.getpid()).encode())
        os.close(descriptor)
        yield
    finally:
        path.unlink()


def save(path, state):
    fd, name = tempfile.mkstemp(prefix='.' + path.name, dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as stream:
            json.dump(state, stream, indent=2, sort_keys=True)
            stream.write('\n')
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def load(path):
    state = read_json(path)
    require(state.get('schema_version') in (1, VERSION), 'unsupported state schema version')
    require(state.get('state_path') == str(path), 'state path changed; explicit new run required')
    return state


def initialize(path, brief_path):
    brief = read_json(brief_path)
    validate_brief(brief, path)
    require(not path.exists(), 'state already exists')
    root = copy.deepcopy(brief)
    root.update(parent=None, resources=list(brief['resources']), status='assigned', deadline_utc=brief['budget']['deadline_utc'], required=True, returns=[], uncertain=False)
    state = {
        'schema_version': VERSION,
        'state_path': str(path),
        'runtime_directory': str(path.parent),
        'automatic_exclusions': [str(path.parent)],
        'brief': brief,
        'revision': 0,
        'authority_revision': 0,
        'dispatched': 0,
        'tasks': {brief['id']: root},
        'reports': {},
        'attempts': {},
        'decision_reviews': {},
        'proofs': [],
        'events': {},
        'history': [],
        'checkpoint': None,
        'resumptions': [],
    }
    input_manifest(state)
    result = status(state)
    save(path, state)
    return result


def status(state):
    if state['schema_version'] == 1:
        return {'schema_version': 1, 'legacy_unrecorded_gates': True,
                'revision': state['revision'],
                'remaining_dispatches': state['brief']['budget']['dispatches'] - state['dispatched'],
                'tasks': {key: {'historical_status': task['status'], 'verified_now': False,
                    'proof_status': 'unverified',
                    'acceptance_eligible_now': False, 'currently_accepted': False,
                    'dispatch_eligible_now': False, 'dispatch_gates': ['legacy_unrecorded_gates: new version2 run required'],
                    'gates': ['legacy_unrecorded_gates: new version2 run required']}
                    for key, task in state['tasks'].items()}}
    attempts = list(state['attempts'].values())
    result = {
        'schema_version': VERSION,
        'revision': state['revision'],
        'authority_revision': state['authority_revision'],
        'remaining_dispatches': state['brief']['budget']['dispatches'] - state['dispatched'],
        'allocated_dispatches': state['dispatched'],
        'observed_attempts': sum('outcome' in a for a in attempts),
        'started_attempts': sum(a.get('outcome') == 'started' for a in attempts),
        'failed_attempts': sum(a.get('outcome') == 'failed' for a in attempts),
        'unknown_attempts': sum(a.get('outcome') == 'unknown' for a in attempts),
        'pending_reservations': sum('outcome' not in a for a in attempts),
        'checkpoint': state['checkpoint'],
        'automatic_exclusions': state['automatic_exclusions'],
        'tasks': {},
    }
    for key, task in state['tasks'].items():
        errors = gates(state, key)
        dispatch = dispatch_errors(state, task)
        verified = bool(task['claims']) and not proof_errors(state, key)
        if not task['claims']:
            proof_status = 'no_claims'
        elif verified:
            proof_status = 'verified'
        else:
            proof_status = 'unverified'
        result['tasks'][key] = {
            'historical_status': task['status'],
            'verified_now': verified,
            'proof_status': proof_status,
            'acceptance_eligible_now': not errors,
            'currently_accepted': task['status'] == 'accepted' and (not errors),
            'dispatch_eligible_now': not dispatch,
            'dispatch_gates': dispatch,
            'uncertain_effects': task.get('uncertain', False),
            'gates': errors,
        }
    return result


def apply_event(path, state, event_path):
    event = read_json(event_path)
    require(isinstance(event, dict), 'event object required')
    event_id = event.get('id')
    checksum = digest(event)
    if event_id in state['events']:
        require(state['events'][event_id] == checksum, 'conflicting repeated event ID')
        result = status(state)
    else:
        require(
            type(event.get('expected_revision')) is int and event['expected_revision'] == state['revision'],
            'stale expected_revision',
        )
        transition(state, event)
        state['revision'] += 1
        state['events'][event_id] = checksum
        state['history'].append(event)
        result = status(state)
        save(path, state)
    return result


def execute_command(args):
    path = local(args.state, False)
    require(not inside(path, SKILL_TREE), 'runtime state cannot be inside loaded skill tree')
    with locked(path):
        if args.command == 'init':
            result = initialize(path, args.brief)
        else:
            state = load(path)
            require(args.command == 'status' or state['schema_version'] == VERSION, 'legacy state is read-only; create a new version2 run')
            if args.command == 'apply':
                result = apply_event(path, state, args.event)
            elif args.command == 'snapshot':
                result = snapshot(state, args.task, local(args.out, False), save)
            else:
                result = status(state)
    return result
