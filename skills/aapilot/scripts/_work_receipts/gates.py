"""Read-only policy for recorded authority, native attempts and review intervals.

State owns all event mutation. These checks never supply approval, infer host IDs,
or turn a declaration into evidence of a real human or native tool invocation.
"""
from pathlib import Path
from .evidence import (
    require, text_fields, string_list, file_refs, fingerprint, read_json,
    check_record, check_snapshot, changed, Rejected, inside,
)


def governing_refs(brief):
    return set([brief['authority_source'], *brief['requirements'], *brief['decisions'],
                *brief['procedures'], *brief['principles']])


def retained(refs):
    return {ref: fingerprint(ref) for ref in set(refs)}


def check_hashes(hashes):
    for ref, expected in hashes.items():
        require(fingerprint(ref, True) == expected, 'retained gate evidence changed: ' + ref)


def validate_decision_review(state, event):
    text_fields(event, ('coverage', 'rationale'))
    require(type(event.get('authority_revision')) is int and event['authority_revision'] == state['authority_revision'], 'decision review authority mismatch')
    string_list(event.get('resources'), 'review resources', True)
    require(set(event['resources']) <= set(state['tasks'][event['task']]['resources']), 'review resources widen task')
    file_refs(event.get('artifact_refs'), 'artifact_refs')
    require(event['artifact_refs'], 'reviewed design/contract required')
    require(isinstance(event.get('decisions'), list) and isinstance(event.get('unresolved'), list), 'decisions and unresolved lists required')
    refs = governing_refs(state['brief']) | set(event['artifact_refs'])
    ids = []
    for decision in event['decisions']:
        text_fields(decision, ('id', 'question', 'selected', 'classification'))
        ids.append(decision['id'])
        require(decision['classification'] in ('product', 'architecture', 'routine'), 'invalid decision classification')
        refs.update(decision_origin_refs(state, decision))
    for entry in event['unresolved']:
        text_fields(entry, ('id', 'question', 'reason'))
        ids.append(entry['id'])
    require(len(ids) == len(set(ids)), 'duplicate decision ID')
    check_unresolved_choice_continuity(state, event)
    return retained(refs)


def decision_origin_refs(state, decision):
    """Validate authority origin and return its additional retained references."""
    refs = set()
    origin = decision.get('origin', {})
    kind = origin.get('kind')
    if kind == 'delegated':
        require(decision['classification'] == 'routine', 'consequential choice cannot be delegated')
    elif kind == 'source':
        require(origin.get('ref') in {state['brief']['authority_source'], *state['brief']['requirements'], *state['brief']['decisions']} and origin.get('status') == 'accepted', 'source must cite current accepted authority')
        text_fields(origin, ('locator',))
        refs.add(origin['ref'])
    elif kind == 'human':
        if origin.get('instruction_ref'):
            require(not origin.get('checkpoint_event'), 'ambiguous human origin')
            fingerprint(origin['instruction_ref'])
            refs.add(origin['instruction_ref'])
        else:
            matches = [r for r in state['resumptions'] if r['checkpoint']['event'] == origin.get('checkpoint_event') and r['event'] == origin.get('resume_event')]
            require(len(matches) == 1, 'human answer must cite retained checkpoint and resume')
            response = matches[0]['response']
            package = matches[0]['checkpoint']['content']
            require(decision['id'] in package['decision_ids'] and decision['question'] == package['question'], 'decision does not match recorded human question')
            require(decision['selected'] == response['answer'], 'decision selected must match actual answer')
            require(origin.get('selected_option') == response.get('selected_option'), 'human selected option mismatch')
            check_hashes(matches[0]['hashes'])
    else:
        require(False, 'decision origin required')
    return refs


def check_unresolved_choice_continuity(state, event):
    pending = {entry['id']: entry for prior in latest_reviews(state, event['task'], event['resources'])
               for entry in prior['unresolved']}
    recorded = {entry['id']: entry for entry in [*event['decisions'], *event['unresolved']]}
    for decision_id, previous in pending.items():
        replacement = recorded.get(decision_id, {})
        require(replacement.get('question') == previous['question'], 'known unresolved choice must be retained or resolved: ' + decision_id)
        if decision_id not in {entry['id'] for entry in event['unresolved']}:
            require(replacement.get('classification') in ('product', 'architecture') and replacement.get('origin', {}).get('kind') in ('source', 'human'),
                    'known consequential choice requires accepted source or human resolution: ' + decision_id)


def task_ancestors(state, task):
    ids = [task['id']]
    parent = task.get('parent')
    while parent:
        ids.append(parent)
        parent = state['tasks'][parent].get('parent')
    return ids


def resources_overlap(state, left, right):
    mappings = state['brief']['resources']
    for left_resource in left:
        for right_resource in right:
            left_path, right_path = mappings[left_resource], mappings[right_resource]
            if left_path.startswith('named:') or right_path.startswith('named:'):
                if left_path == right_path:
                    return True
            elif inside(Path(left_path), Path(right_path)) or inside(Path(right_path), Path(left_path)):
                return True
    return False


def check_current_reviews(state, review_id, task, implementation):
    review = state['decision_reviews'][review_id]
    relevant_reviews = latest_reviews(state, review['task'], task['resources'])
    require(relevant_reviews and all(r['id'] == review_id for r in relevant_reviews), 'superseded decision review')
    ancestors = task_ancestors(state, task)
    require(review['task'] in ancestors, 'decision review outside task ancestry')
    for other in state['tasks'].values():
        subordinate = task['id'] in task_ancestors(state, other)
        relevant = other['id'] in ancestors or (not implementation and subordinate)
        if not relevant or not resources_overlap(state, other['resources'], task['resources']):
            continue
        for latest in latest_reviews(state, other['id'], task['resources']):
            require(not latest['unresolved'], 'unresolved consequential choices')
            # Historical child source may predate integrated work. Its retained
            # receipt is checked separately; new unresolved choices still bind.
            if other['status'] != 'accepted' or other['id'] in ancestors:
                require(latest['authority_revision'] == state['authority_revision'], 'decision review predates authority')
                check_hashes(latest['hashes'])


def latest_reviews(state, task_id, resources):
    # State is serialized with sorted keys; event IDs have no chronology.
    reviews = sorted((r for r in state['decision_reviews'].values() if r['task'] == task_id),
                     key=lambda r: r['expected_revision'])
    latest = {}
    for resource in resources:
        matches = [r for r in reviews if resources_overlap(state, r['resources'], [resource])]
        if matches:
            latest[matches[-1]['id']] = matches[-1]
    return list(latest.values())


def check_decision_review(state, review_id, task, implementation=False, current=True):
    require(review_id in state['decision_reviews'], 'current decision_review required')
    review = state['decision_reviews'][review_id]
    if current:
        check_current_reviews(state, review_id, task, implementation)
    require(review['authority_revision'] == state['authority_revision'], 'decision review predates authority')
    check_hashes(review['hashes'])
    require(not review['unresolved'], 'unresolved consequential choices')
    require(set(task['resources']) <= set(review['resources']), 'task outside decision review resources')
    if implementation:
        require(set(review['artifact_refs']) <= set(task['inputs']), 'assignment must include exact reviewed artifacts')
    else:
        require(review['task'] == task['id'], 'acceptance requires review of this task')
    check_obligations(state, 'implementation' if implementation else 'acceptance')
    if not implementation and task.get('purpose') == 'implementation':
        check_obligations(state, 'implementation')


def obligation_binding(brief):
    return {'obligations': brief.get('checkpoint_obligations', []),
            'governing': retained(governing_refs(brief))}


def check_obligations(state, trigger):
    for obligation in state['brief'].get('checkpoint_obligations', []):
        if obligation['before'] != trigger:
            continue
        matches = [r for r in state['resumptions'] if r['checkpoint']['id'] == obligation['id'] and r['checkpoint']['binding'] == obligation_binding(state['brief'])]
        require(matches, 'mandatory checkpoint unresolved: ' + obligation['id'])
        check_hashes(matches[-1]['hashes'])


def validate_package(state, event):
    package = read_json(event['package'])
    text_fields(package, ('question_id', 'question'))
    file_refs(package.get('artifact_refs'), 'artifact_refs')
    require(package['artifact_refs'], 'checkpoint concrete artifact required')
    string_list(package.get('decision_ids'), 'decision_ids', True)
    options = package.get('options', [])
    require(isinstance(options, list), 'options list required')
    if options:
        require(len(options) >= 2, 'choice question requires at least two options')
        for option in options:
            text_fields(option, ('id', 'label', 'consequences'))
        require(len({o['id'] for o in options}) == len(options) and len({o['label'] for o in options}) == len(options), 'distinct concrete options required')
        text_fields(package, ('recommendation',))
    else:
        require('selected_option' not in package, 'free-text question has no selected option')
    return package


def validate_response(state, event):
    checkpoint = state['checkpoint']
    response = read_json(event['human_response'])
    text_fields(response, ('checkpoint_event', 'question_id', 'package_hash', 'answer', 'source_ref'))
    require(response['checkpoint_event'] == checkpoint['event'] and response['question_id'] == checkpoint['content']['question_id'], 'response question/checkpoint mismatch')
    require(response['package_hash'] == checkpoint['hash']['sha256'], 'response package mismatch')
    require(type(response.get('authority_revision')) is int and response['authority_revision'] == state['authority_revision'] == checkpoint['authority_revision'], 'response authority mismatch')
    options = checkpoint['content'].get('options', [])
    if options:
        require(response.get('selected_option') in {o['id'] for o in options}, 'response selected_option mismatch')
    else:
        require('selected_option' not in response, 'free-text response has no selected_option')
    refs = [event['human_response'], response['source_ref'], checkpoint['package'], *checkpoint['content']['artifact_refs']]
    return response, retained(refs)


def validate_context(context, complete=False):
    require(isinstance(context, dict), 'review context required')
    require(type(context.get('fresh')) is bool and type(context.get('prior_conclusions')) is bool, 'explicit context booleans required')
    text_fields(context, ('exposure',))
    string_list(context.get('isolation_limits'), 'isolation_limits', True)
    exposures = context.get('exposures')
    require(isinstance(exposures, list), 'typed exposures list required')
    for exposure in exposures:
        require(exposure.get('kind') in ('prior-conclusions', 'other') and exposure.get('stage') in ('before-execution', 'during-execution', 'after-execution-before-initial-findings'), 'invalid exposure kind/stage')
        text_fields(exposure, ('source_ref', 'description'))
        fingerprint(exposure['source_ref'])
    if complete:
        require(context.get('interval_complete') is True, 'complete context interval through initial findings required')


def discovery_context(context):
    require(context['fresh'] is True and context['prior_conclusions'] is False, 'discovery requires fresh context without prior conclusions')
    require(not context.get('post_execution_conclusion_exposure'), 'post-execution conclusion exposure disqualifies discovery')
    require(not any(e['kind'] == 'prior-conclusions' for e in context['exposures']), 'conclusion exposure through initial findings disqualifies discovery')


def started_dispatch(state, task, producer=None):
    attempts = [a for a in state['attempts'].values() if a['task'] == task['id'] and a.get('outcome') == 'started']
    require(attempts, 'started native worker receipt required')
    if producer is not None:
        require(any(a['worker_id'] == producer for a in attempts), 'report producer does not match started native worker')
    for attempt in attempts:
        check_hashes(attempt['hashes'])
    return attempts


def validate_review_attempt(state, report, verifier):
    require(verifier.get('purpose') == 'verification', 'verification purpose required')
    attempts = started_dispatch(state, verifier, report['producer'])
    require(any(a['worker_id'] == report['producer'] and a['host_ref'] == report['host_ref'] for a in attempts), 'report native host receipt mismatch')
    initial = verifier.get('initial_findings')
    require(initial and report.get('initial_findings_event') == initial['event'], 'frozen initial_findings reference required')
    check_record(initial['record'])
    check_hashes(initial['hashes'])
    preflight = verifier['preflight']
    check_hashes(preflight['hashes'])
    original = initial['record']['report']
    # Later summaries can add interpretation but cannot replace the exercised facts.
    for key in ('task', 'producer', 'host_ref', 'editors', 'snapshot', 'environment', 'verifier', 'claims', 'commands', 'effects', 'executable', 'review_mode'):
        require(report.get(key) == original.get(key), 'changed initial proof facts require new review attempt: ' + key)
    require(report['review_mode'] == verifier['review']['mode'] == preflight['mode'], 'review mode mismatch')
    require(report['snapshot'] == preflight['snapshot'], 'preflight snapshot mismatch')
    for context in (preflight['context'], initial['context'], original.get('context'), report.get('context')):
        validate_context(context, complete=context is not preflight['context'])
        require(context['fresh'] is True, 'fresh worker required throughout review attempt')
        if report['review_mode'] == 'independent-discovery':
            discovery_context(context)
    require(set(report.get('claims', {})) <= set(verifier['review']['claims']), 'report outside assigned claims')

def validate_production_proof(state, report, verifier):
    context = report.get('context', {})
    require(report.get('executable') is True, 'production requires executable proof')
    require(
        context.get('fresh') is True,
        'fresh verifier required',
    )
    require(
        isinstance(context.get('exposure'), str) and bool(context.get('isolation_limits')),
        'context exposure/isolation declarations required',
    )
    require(
        report.get('review_mode') in ('independent-discovery', 'confirmation-audit'),
        'production review_mode required',
    )
    editors = set(string_list(report.get('editors'), 'editors'))
    for other_task in state['tasks'].values():
        for report_id in other_task.get('returns', []):
            returned = state['reports'][report_id]['report']
            if other_task['id'] != verifier['id']:
                editors.update(returned.get('editors', []))
                editors.add(returned['producer'])
    require(report['producer'] not in editors, 'verifier is a declared editor/artifact producer')
    commands = report.get('commands')
    require(isinstance(commands, list) and bool(commands), 'executable commands required')
    require(
        all((isinstance(c, dict) and c.get('command') and (type(c.get('exit_code')) is int) and (c['exit_code'] == 0) for c in commands)),
        'command proof missing/failing',
    )


def validate_claim_proof(state, task, claim, proof, current):
    record = state['reports'][proof['report']]
    report = record['report']
    require(record['authority_revision'] == state['authority_revision'], 'proof predates resume')
    check_record(record)
    require(
        report['claims'][claim].get('status') == 'pass' and report['claims'][claim].get('observations'),
        'claim is not observed passing',
    )
    require(report.get('snapshot'), 'tested snapshot required')
    check_snapshot(state, report['snapshot'], current=current)
    require(
        report.get('environment') == state['brief']['environment'],
        'environment descriptor identity missing/mismatched',
    )
    fingerprint(report.get('verifier'))
    require(
        report.get('coverage') and report.get('limitations') is not None and (report.get('effects') is not None),
        'coverage, effects and limitations required',
    )
    verifier = state['tasks'][proof['verifier_task']]
    require(verifier['status'] in ('returned', 'accepted'), 'verifier assignment must return')
    require(report['task'] == verifier['id'], 'verifier report assignment mismatch')
    validate_review_attempt(state, report, verifier)
    if task['proof_kind'] == 'production':
        validate_production_proof(state, report, verifier)
        require(report['review_mode'] == task.get('required_review_mode', 'independent-discovery'), 'review mode does not satisfy required proof obligation')


def validate_owner_proof(state, task, report_id, current):
    require(task['id'] == state['brief']['id'] and task.get('parent') is None, 'owner-presentation is root-only')
    require(task['claims'], 'owner-presentation requires nonempty claims')
    eligibility = state.get('presentation_eligibility')
    require(eligibility, 'before-edit presentation eligibility required')
    check_hashes(eligibility['request_hashes'])
    check_decision_review(state, task.get('decision_review'), task, current=current)
    record = state['reports'][report_id]
    report = record['report']
    check_record(record)
    require(record['authority_revision'] == state['authority_revision'], 'owner proof predates resume')
    require(report.get('proof_basis') == 'owner-presentation', 'owner-presentation proof_basis required')
    require(report['producer'] == task['owner'] and report['task'] == task['id'], 'root owner must produce owner proof')
    manifest = check_snapshot(state, report.get('snapshot'), current=current)
    scope = set(eligibility['declaration']['components'])
    require(set(changed(eligibility['source_hashes'], manifest['inputs'])) <= scope,
            'changes outside prescribed presentation components require independent proof')
    require(report.get('environment') == state['brief']['environment'], 'environment descriptor identity missing/mismatched')
    validate_owner_observations(task, report)


def validate_owner_observations(task, report):
    text_fields(report, ('diff_ref', 'eligibility_review', 'coverage', 'effects'))
    fingerprint(report['diff_ref'])
    require(report.get('limitations') is not None, 'limitations required')
    require(string_list(report.get('evidence'), 'evidence', True), 'owner evidence required')
    require(isinstance(report.get('commands'), list) and report['commands'], 'source/diff checks required')
    require(all(isinstance(c, dict) and c.get('command') and type(c.get('exit_code')) is int and c['exit_code'] == 0
                for c in report['commands']), 'source/diff check missing/failing')
    claims = report.get('claims', {})
    require(isinstance(claims, dict), 'claims map required')
    for claim in task['claims']:
        observation = claims.get(claim, {})
        require(isinstance(observation, dict) and observation.get('status') == 'pass' and observation.get('observations'),
                f'{claim}: owner claim missing or not observed passing')


def proof_errors(state, target, current=True, selected_reports=None):
    task = state['tasks'][target]
    if task.get('verification_requirement', 'independent') == 'owner-presentation':
        try:
            require(task['returns'], 'missing returned owner-presentation report')
            report_id = task['returns'][-1]
            validate_owner_proof(state, task, report_id, current)
            if selected_reports is not None:
                selected_reports.append(report_id)
            return []
        except (Rejected, KeyError, TypeError, ValueError, OSError) as exc:
            return [f'{target}: {exc}']
    errors = []
    for claim in task['claims']:
        candidates = [
            p
            for p in state['proofs']
            if p['target'] == target
            and claim in state['reports'][p['report']]['report'].get('claims', {})
        ]
        reasons = []
        passed = False
        # A later contradictory or invalid receipt cannot revive an older pass.
        for proof in candidates[-1:]:
            try:
                validate_claim_proof(state, task, claim, proof, current)
                passed = True
                if selected_reports is not None:
                    selected_reports.append(proof['report'])
                break
            except (Rejected, KeyError, TypeError, ValueError, OSError) as exc:
                reasons.append(str(exc))
        if not passed:
            errors.append(f'{target}:{claim}: ' + ('; '.join(reasons) or 'missing verification'))
    return errors

