"""Exercise the real receipt CLI against transient projects and runtime state."""
import copy
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
HELPER = Path(__file__).resolve().parents[1] / 'skills/aapilot/scripts/work_receipts.py'

class WorkReceiptsCLI(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.project = self.base / 'project'
        self.project.mkdir()
        self.run = self.base / 'run'
        self.run.mkdir()
        self.state = self.run / 'state.json'
        self.req = self.write(self.project / 'requirements.md', 'Create once; duplicate leaves state unchanged.\n')
        self.procedure = self.write(self.project / 'procedure.md', 'Run actual CLI and inspect persisted state.\n')
        self.verifier = self.write(self.project / 'verify.py', 'print("verified")\n')
        self.config = self.write(self.project / 'config.json', '{}\n')
        self.source = self.write(self.project / 'app.py', 'print("create")\n')
        self.env = self.write(self.project / 'environment.json', '{"runtime":"python3","instance":"local-fixture"}\n')
        self.host = self.write(self.run / 'host.txt', 'synthetic host assignment; protocol fixture only\n')
        self.evidence = self.write(self.run / 'evidence.txt', 'observed exit=0 and persisted state unchanged\n')
        deadline = (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat()
        self.brief = {
            'id': 'root',
            'owner': 'lead',
            'project_root': str(self.project),
            'objective': 'bounded work',
            'purpose': 'other',
            'checkpoint_obligations': [],
            'required_review_mode': 'independent-discovery',
            'requirements': [str(self.req)],
            'decisions': [],
            'procedures': [str(self.procedure)],
            'principles': [],
            'authority_source': str(self.req),
            'actions': ['read', 'write', 'delegate'],
            'resources': {'repo': str(self.project), 'service': 'named:local-service'},
            'checkpoints': ['visual', 'decision'],
            'budget': {'dispatches': 10, 'deadline_utc': deadline},
            'claims': ['behavior'],
            'proof_kind': 'production',
            'source': {
                'mode': 'roots',
                'roots': [str(self.project)],
                'exclude': [],
                'required': [str(self.verifier), str(self.config)],
            },
            'environment': str(self.env),
            'constraints': ['local only'],
            'expected_outputs': ['working change'],
            'next_action': 'implement',
        }
        self.counter = 0
        self.initialize()

    def write(self, path, content):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return path

    def json_file(self, name, value):
        return self.write(self.run / name, json.dumps(value))

    def call(self, command, ok=True):
        result = subprocess.run([sys.executable, str(HELPER), *command], text=True, capture_output=True, cwd=self.base)
        log = os.environ.get('WORK_RECEIPTS_LOG')
        if log:
            with open(log, 'a') as log_file:
                log_file.write(json.dumps({
                    'test': self.id(),
                    'command': command,
                    'exit': result.returncode,
                    'stdout': result.stdout,
                    'stderr': result.stderr,
                }) + '\n')
        self.assertEqual(result.returncode, 0 if ok else 1, result.stdout + result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(data['ok'], ok)
        return data

    def initialize(self):
        if self.state.exists():
            self.state.unlink()
        return self.call(['init', '--state', str(self.state), '--brief', str(self.json_file('brief.json', self.brief))])

    def current(self):
        return json.loads(self.state.read_text())

    def status(self):
        return self.call(['status', '--state', str(self.state)])

    def event_data(self, kind, task='root', actor='lead', **payload):
        self.counter += 1
        return {
            'id': f'e{self.counter}',
            'expected_revision': self.current()['revision'],
            'type': kind,
            'actor': actor,
            'task': task,
            'source_ref': str(self.req),
            **payload,
        }

    def apply(self, kind=None, ok=True, event=None, **payload):
        self.ensure_transition_prerequisites(kind, payload)
        event = event or self.event_data(kind, **payload)
        before = self.state.read_bytes()
        result = self.call(['apply', '--state', str(self.state), '--event', str(self.json_file('event.json', event))], ok)
        if not ok:
            self.assertEqual(before, self.state.read_bytes(), 'rejected transition changed state')
        return result

    def ensure_transition_prerequisites(self, kind, payload):
        """Record required dispatch and decision review before the requested event."""
        if kind in ('accept', 'cancelled'):
            task_id = payload.get('task', 'root')
            assigned = self.current()['tasks'][task_id]
            attempt = self.current()['attempts'].get(task_id, {})
            if assigned.get('parent') and 'outcome' not in attempt:
                self.apply('dispatch', task=task_id, actor=assigned['owner'], attempt_id=task_id, operation='spawn',
                    request_ref=str(self.host), host_ref=str(self.host), outcome='failed' if kind == 'cancelled' else 'started',
                    worker_id=None if kind == 'cancelled' else task_id + '-worker')
        if kind == 'accept' and 'decision_review' not in payload:
            payload['decision_review'] = self.review(payload.get('task', 'root'), payload.get('actor', 'lead'))

    def review(self, task='root', actor='lead', **changes):
        event = self.event_data('decision_review', task=task, actor=actor, **({
            'resources': self.current()['tasks'][task]['resources'], 'artifact_refs': [str(self.req)],
            'coverage': 'Inspect fixture behavior, authority and contract; no unsettled consequential choice',
            'authority_revision': self.current()['authority_revision'], 'decisions': [], 'unresolved': [],
            'rationale': 'Requirements settle fixture behavior; helper internals are routine'} | changes))
        self.apply(event=event)
        return event['id']

    def assign(self, task_id='verify', parent='root', owner='worker', actor='lead', ok=True, **changes):
        assignment = {
            'id': task_id,
            'parent': parent,
            'owner': owner,
            'objective': 'bounded assignment',
            'purpose': 'verification' if ('verify' in task_id or 'verifier' in task_id) else 'other',
            'procedure': str(self.procedure),
            'actions': ['read'],
            'resources': ['repo'],
            'claims': [],
            'proof_kind': 'scoped',
            'inputs': [str(self.req)],
            'expected_artifacts': ['report'],
        }
        if assignment['purpose'] == 'verification':
            target = parent if parent != 'root' else ('replacement' if task_id == 'replacement-verifier' else 'root')
            assignment['review'] = {'target': target, 'mode': 'independent-discovery', 'claims': self.current()['tasks'][target]['claims']}
        assignment.update(changes)
        return self.apply('assign', task=parent, actor=actor, assignment=assignment, ok=ok)

    def snapshot(self, name='snapshot', task='root', ok=True):
        task = self.snapshot_task(task)
        result = self.call(['snapshot', '--state', str(self.state), '--task', task, '--out', str(self.run / name)], ok)
        return result.get('manifest')

    def snapshot_task(self, task):
        if task == 'root':
            reviews = [t for t in self.current()['tasks'].values() if t.get('purpose') == 'verification' and not t.get('preflight')]
            if reviews:
                task = reviews[-1]['id']
        return task

    def report(self, name='proof', task='verify', **changes):
        """Start the producer, freeze initial findings, then write its final report."""
        report = {
            'id': name,
            'task': task,
            'producer': task + '-native-worker',
            'host_ref': str(self.host),
            'editors': ['editor'],
            'review_mode': 'independent-discovery',
            'context': {
                'fresh': True,
                'prior_conclusions': False,
                'exposure': 'requirements and actual artifact only',
                'isolation_limits': ['shared filesystem; synthetic fixture'],
                'exposures': [],
                'interval_complete': True,
            },
            'snapshot': str(self.run / 'snapshot' / 'manifest.json') if (self.run / 'snapshot' / 'manifest.json').exists() else None,
            'environment': str(self.env),
            'verifier': str(self.verifier),
            'artifacts': [],
            'evidence': [str(self.evidence)],
            'claims': {'behavior': {'status': 'pass', 'observations': 'CLI and persistence inspected'}},
            'commands': [{'command': 'python3 app.py', 'exit_code': 0}],
            'effects': 'persisted state inspected',
            'coverage': 'required local behavior',
            'limitations': 'synthetic protocol metadata, not actual worker proof',
            'executable': True,
        }
        report.update(changes)
        assigned = self.current()['tasks'].get(task)
        if assigned and assigned.get('parent'):
            self.ensure_started_report_producer(task, assigned, report)
            self.ensure_frozen_initial_findings(name, task, assigned, report)
        return str(self.json_file(name + '.json', report))

    def ensure_started_report_producer(self, task, assigned, report):
        attempts = self.current()['attempts']
        if task not in attempts or 'outcome' not in attempts[task]:
            request = self.json_file(task + '-native-request.json', {'fixture': 'synthetic spawn', 'task': task})
            if assigned['purpose'] == 'verification':
                self.record_report_preflight(task, assigned, report, request)
            self.apply('dispatch', task=task, actor=assigned['owner'], attempt_id=task, operation='spawn',
                request_ref=str(request), host_ref=str(self.host), outcome='started', worker_id=report['producer'])

    def record_report_preflight(self, task, assigned, report, request):
        context = copy.deepcopy(report['context'])
        if not context:
            context = {'fresh': True, 'prior_conclusions': False, 'exposure': 'fixture scoped review', 'isolation_limits': ['synthetic fixture'], 'exposures': [], 'interval_complete': True}
            report['context'] = context
        # Ineligible proof facts remain in the initial report; preflight
        # is a separately observed declaration, not a cleanliness grant.
        preflight_context = copy.deepcopy(context)
        preflight_context.setdefault('exposures', [])
        if isinstance(preflight_context.get('isolation_limits'), str):
            preflight_context['isolation_limits'] = [preflight_context['isolation_limits']]
        self.apply('review_preflight', task=task, actor=assigned['owner'], snapshot=report['snapshot'],
            environment=str(self.env), mode=assigned['review']['mode'], context=preflight_context, host_request_ref=str(request))

    def ensure_frozen_initial_findings(self, name, task, assigned, report):
        if assigned['purpose'] == 'verification':
            assigned = self.current()['tasks'][task]
            if not assigned.get('initial_findings'):
                context = copy.deepcopy(report['context'])
                context.setdefault('exposures', [])
                context.setdefault('interval_complete', True)
                if isinstance(context.get('isolation_limits'), str):
                    context['isolation_limits'] = [context['isolation_limits']]
                report['context'] = context
                original = self.json_file(name + '-initial.json', {**report, 'id': name + '-initial'})
                attempt = self.current()['attempts'][task]
                initial = self.event_data('initial_findings', task=task, actor=assigned['owner'],
                    preflight_event=assigned['preflight']['id'], dispatch_event=attempt['event'], findings=str(original),
                    context=context, context_evidence_refs=[str(self.host)])
                self.apply(event=initial)
                report['initial_findings_event'] = initial['id']
            else:
                report['initial_findings_event'] = assigned['initial_findings']['event']

    def proof(self, **changes):
        self.assign()
        self.snapshot()
        report = self.report(**changes)
        self.apply('returned', task='verify', actor='worker', report=report)
        self.apply('verification', target='root', verifier_task='verify', report=report)
        return report

    def accept(self, ok=True):
        return self.apply('accept', rationale='Inspected requirements and observed effects', evidence_refs=[str(self.evidence)], ok=ok)

    def checkpoint_package(self):
        return self.json_file('package.json', {'question_id': 'fixture-question', 'question': 'What fixture should continue?',
            'artifact_refs': [str(self.req)], 'decision_ids': ['fixture-decision']})

    def checkpoint_response(self):
        checkpoint = self.current()['checkpoint']
        source = self.write(self.run / 'synthetic-human-source.txt', 'Synthetic schema fixture answer only; no actual human interaction')
        return self.json_file('human.json', {'checkpoint_event': checkpoint['event'],
            'question_id': checkpoint['content']['question_id'], 'package_hash': checkpoint['hash']['sha256'],
            'authority_revision': self.current()['authority_revision'], 'answer': 'Continue fixture', 'source_ref': str(source)})

    def test_hostless_owner_return_does_not_satisfy_independent_proof(self):
        report = self.report(name='owner-development', task='root', producer='lead', host_ref=None)
        self.apply('returned', report=report)
        self.assertEqual(self.status()['tasks']['root']['proof_status'], 'unverified')
        self.accept(ok=False)

    def test_owner_edit_accepts_only_with_separate_current_verifier(self):
        self.brief['purpose'] = 'implementation'
        self.initialize()
        self.review()
        self.write(self.source, 'print("corrected")\n')
        report = self.report(name='owner-development', task='root', producer='lead', host_ref=None)
        self.apply('returned', report=report)
        self.assertEqual(self.status()['observed_attempts'], 0)
        self.assertEqual(self.status()['remaining_dispatches'], 10)
        self.accept(ok=False)
        self.proof()
        self.accept()
        self.assertTrue(self.status()['tasks']['root']['currently_accepted'])
        self.assertEqual(self.status()['observed_attempts'], 1)
        self.assertEqual(self.status()['remaining_dispatches'], 9)
        self.write(self.source, 'print("changed after proof")\n')
        root = self.status()['tasks']['root']
        self.assertEqual(root['historical_status'], 'accepted')
        self.assertFalse(root['currently_accepted'])

    def test_hostless_root_return_requires_owner_producer(self):
        report = self.report(name='wrong-owner', task='root', producer='other', host_ref=None)
        self.apply('returned', report=report, ok=False)

    def test_hostless_child_return_remains_rejected(self):
        self.assign('child')
        report = self.report(name='hostless-child', task='child', host_ref=None)
        self.apply('returned', task='child', actor='worker', report=report, ok=False)

    def test_owner_cannot_verify_even_without_a_root_return(self):
        self.proof(producer='lead', editors=[])
        self.assertFalse(self.status()['tasks']['root']['verified_now'])
        self.accept(ok=False)

    # Lifecycle, authority and proof eligibility.
    def test_returned_is_not_verified_or_accepted(self):
        report = self.report(task='root', name='return', producer='editor')
        self.apply('returned', report=report)
        root = self.status()['tasks']['root']
        self.assertEqual(root['historical_status'], 'returned')
        self.assertIs(root['verified_now'], False)
        self.assertEqual(root['proof_status'], 'unverified')
        self.accept(ok=False)

    def test_claimless_status_through_return_and_acceptance_is_read_only(self):
        self.brief.update(claims=[], proof_kind='scoped')
        initialized = self.initialize()['tasks']['root']
        self.assertIs(initialized['verified_now'], False)
        self.assertEqual(initialized['proof_status'], 'no_claims')
        self.assertFalse(initialized['acceptance_eligible_now'])
        report = self.report(name='claimless-return', task='root', claims={}, snapshot=None,
            review_mode='scoped', executable=False)
        returned = self.apply('returned', report=report)['tasks']['root']
        self.assertEqual(returned['historical_status'], 'returned')
        self.assertIs(returned['verified_now'], False)
        self.assertEqual(returned['proof_status'], 'no_claims')
        accepted = self.accept()['tasks']['root']
        self.assertTrue(accepted['currently_accepted'])
        self.assertIs(accepted['verified_now'], False)
        self.assertEqual(accepted['proof_status'], 'no_claims')
        before = self.state.read_bytes()
        revision = self.current()['revision']
        modified = self.state.stat().st_mtime_ns
        for _ in range(2):
            self.assertEqual(self.status()['tasks']['root'], accepted)
        self.assertEqual(self.state.read_bytes(), before)
        self.assertEqual(self.current()['revision'], revision)
        self.assertEqual(self.state.stat().st_mtime_ns, modified)
        self.assertNotIn('verified_now', self.current()['tasks']['root'])
        self.assertNotIn('proof_status', self.current()['tasks']['root'])

    def test_nested_global_budget_and_literal_grants(self):
        self.brief['budget']['dispatches'] = 2
        self.initialize()
        self.assign('architect', owner='architect', actions=['read', 'delegate'])
        self.assign('arena', parent='architect', owner='arena', actor='architect', actions=['read'])
        self.assertEqual(self.status()['remaining_dispatches'], 0)
        self.assign('extra', ok=False)
        self.apply('cancelled', task='arena', actor='arena', reason='abandon optional candidate')
        self.assertEqual(self.status()['remaining_dispatches'], 0)

    def test_child_widening_rejects_without_mutation(self):
        for changes in ({'actions': ['publish']}, {'resources': ['unknown']}, {'deadline_utc': (datetime.now(timezone.utc) + timedelta(days=1)).isoformat()}, {'inputs': [str(self.run / 'host.txt')]}, {'procedure': '../bad'}):
            with self.subTest(changes=changes):
                self.assign(ok=False, **changes)

    def test_deadline_expiry_blocks_dispatch_and_acceptance(self):
        self.brief['budget']['deadline_utc'] = '2000-01-01T00:00:00Z'
        self.initialize()
        self.assign(ok=False)
        self.accept(ok=False)

    def test_production_proof_and_owner_acceptance(self):
        self.proof()
        before = self.status()['tasks']['root']
        self.assertIs(before['verified_now'], True)
        self.assertEqual(before['proof_status'], 'verified')
        self.assertFalse(before['currently_accepted'])
        self.accept()
        self.assertTrue(self.status()['tasks']['root']['currently_accepted'])

    def test_scoped_design_proof_does_not_require_execution(self):
        self.brief['proof_kind'] = 'scoped'
        self.initialize()
        self.proof(executable=False, commands=[])
        self.accept()

    def test_latest_claim_proof_cannot_fall_back_to_older_pass(self):
        self.proof()
        for status in ('fail', 'unverified', 'pass'):
            report = self.report(name='later-' + status, claims={'behavior': {'status': status, 'observations': 'new same-artifact observation'}})
            self.apply('returned', task='verify', actor='worker', report=report)
            self.apply('verification', target='root', verifier_task='verify', report=report)
            root = self.status()['tasks']['root']
            self.assertIs(root['verified_now'], False)
            self.assertEqual(root['proof_status'], 'unverified')
            self.accept(ok=False)
        self.integrated_proof_after_resume()
        self.accept()

    def test_editor_or_inherited_context_cannot_prove_production(self):
        cases = [{'producer': 'editor'}, {'context': {
            'fresh': True,
            'prior_conclusions': True,
            'exposure': 'lead findings',
            'isolation_limits': 'shared',
        }}, {'executable': False}, {'claims': {'behavior': {'status': 'unverified', 'observations': 'no runtime'}}}, {'commands': []}, {'environment': str(self.config)}]
        for changes in cases:
            with self.subTest(changes=changes):
                self.initialize()
                shutil.rmtree(self.run / 'snapshot', ignore_errors=True)
                self.proof(**changes)
                self.accept(ok=False)

    def test_all_declared_editors_and_producers_are_excluded(self):
        self.assign('implement', owner='editor')
        report = self.report(name='implementation', task='implement', producer='same-worker', editors=['same-worker'])
        self.apply('returned', task='implement', actor='editor', report=report)
        self.proof(producer='fresh-editor', editors=['fresh-editor'])
        self.accept(ok=False)

    # Source and retained evidence identity.
    def test_current_source_config_verifier_env_requirements_and_evidence(self):
        self.proof()
        for path in [self.source, self.config, self.verifier, self.env, self.req, self.evidence]:
            with self.subTest(path=path.name):
                original = path.read_bytes()
                path.write_bytes(original + b'\n')
                root = self.status()['tasks']['root']
                self.assertIs(root['verified_now'], False)
                self.assertEqual(root['proof_status'], 'unverified')
                result = self.accept(ok=False)
                self.assertIn(str(path), result['error'])
                path.write_bytes(original)
        added = self.project / 'dirty-new.txt'
        added.write_text('new')
        self.assertIn(str(added), self.accept(ok=False)['error'])
        added.unlink()
        original = self.source.read_bytes()
        self.source.unlink()
        self.assertIn(str(self.source), self.accept(ok=False)['error'])
        self.source.write_bytes(original)
        original_mode = self.source.stat().st_mode & 511
        self.source.chmod(0o755)
        self.assertIn(str(self.source), self.accept(ok=False)['error'])
        self.source.chmod(original_mode)
        self.accept()

    def test_protected_archive_cannot_be_modified(self):
        self.proof()
        manifest = json.loads((self.run / 'snapshot' / 'manifest.json').read_text())
        copied = self.run / 'snapshot' / manifest['copies'][str(self.source)]
        copied.write_text('changed archive')
        self.assertIn('protected snapshot changed', self.accept(ok=False)['error'])

    def test_required_missing_unreadable_and_symlink_inputs(self):
        self.source.unlink()
        # A missing nonrequired tracked/root file is observed as a source change;
        # explicitly required files cannot disappear.
        self.verifier.unlink()
        self.snapshot(ok=False)
        self.verifier.write_text('test')
        self.verifier.chmod(0)
        self.snapshot(ok=False)
        self.verifier.chmod(0o644)
        link = self.project / 'link'
        link.symlink_to(self.req)
        self.snapshot(ok=False)

    def test_explicit_exclusion_cannot_hide_required_inputs(self):
        self.state.unlink()
        self.brief['source']['exclude'] = [str(self.req)]
        result = self.call(['init', '--state', str(self.state), '--brief', str(self.json_file('brief.json', self.brief))], False)
        self.assertIn('excluded', result['error'])
        self.assertFalse(self.state.exists())

    # Checkpoints, interrupted effects and transaction guarantees.
    def test_checkpoint_stops_and_resume_invalidates_proof(self):
        self.proof()
        self.apply('checkpoint', checkpoint_id='visual', package=str(self.checkpoint_package()), reason='requires eyeballing', decision='approve preview')
        paused = self.status()
        self.assertIs(paused['tasks']['root']['verified_now'], True)
        self.assertEqual(paused['tasks']['root']['proof_status'], 'verified')
        self.assertFalse(paused['tasks']['root']['acceptance_eligible_now'])
        used = paused['remaining_dispatches']
        self.assign('blocked', ok=False)
        self.accept(ok=False)
        response = self.checkpoint_response()
        self.apply('resume', checkpoint_id='wrong', authority_revision=0, human_response=str(response), ok=False)
        self.apply('resume', checkpoint_id='visual', authority_revision=99, human_response=str(response), ok=False)
        wider = copy.deepcopy(self.brief)
        wider['budget']['dispatches'] = 99
        self.apply('resume', checkpoint_id='visual', authority_revision=0, human_response=str(response), updated_brief=wider, ok=False)
        self.apply('resume', checkpoint_id='visual', authority_revision=0, human_response=str(response))
        self.assertEqual(self.status()['remaining_dispatches'], used)
        self.accept(ok=False)
        self.assertEqual(self.current()['authority_revision'], 1)
        self.assertEqual(len(self.current()['resumptions']), 1)

    def test_interrupt_retry_new_id_stays_blocked_until_observed_known(self):
        self.assign('writer', owner='editor', actions=['read', 'write'])
        self.apply('interrupted', task='writer', actor='editor', intended_effects='write record', last_worker_ref='worker-1', observations='partial effects unknown')
        self.assign('retry-new-id', ok=False)
        self.apply('reconciled', task='writer', actor='editor', evidence_refs=[str(self.evidence)], worker_active=False, outcome='unknown', observations='not enough evidence')
        self.assign('retry-new-id', ok=False)
        self.apply('reconciled', task='writer', actor='editor', evidence_refs=[str(self.evidence)], worker_active=True, outcome='known', observations='file inspected', ok=False)
        self.apply('reconciled', task='writer', actor='editor', evidence_refs=[str(self.evidence)], worker_active=False, outcome='known', observations='worker gone and partial write inspected')
        self.assign('retry-new-id', supersedes='writer')
        self.assertEqual(self.status()['remaining_dispatches'], 8)

    def test_event_and_report_ids_idempotent_conflicts_rejected(self):
        assignment = {
            'id': 'child',
            'parent': 'root',
            'owner': 'worker',
            'objective': 'inspect',
            'purpose': 'other',
            'procedure': str(self.procedure),
            'actions': ['read'],
            'resources': ['repo'],
            'claims': [],
            'proof_kind': 'scoped',
            'inputs': [],
            'expected_artifacts': [],
        }
        event = self.event_data('assign', assignment=assignment)
        self.apply(event=event)
        original = self.state.read_bytes()
        self.apply(event=event)
        self.assertEqual(self.state.read_bytes(), original)
        conflict = copy.deepcopy(event)
        conflict['assignment']['objective'] = 'changed'
        self.apply(event=conflict, ok=False)
        report = self.report(task='child')
        self.apply('returned', task='child', actor='worker', report=report)
        self.apply('returned', task='child', actor='worker', report=report)
        content = json.loads(Path(report).read_text())
        content['producer'] = 'other'
        Path(report).write_text(json.dumps(content))
        self.apply('returned', task='child', actor='worker', report=report, ok=False)

    def test_revision_lock_and_unsupported_state(self):
        self.apply(event=self.event_data('cancelled', reason='old revision') | {'expected_revision': 99}, ok=False)
        lock = Path(str(self.state) + '.lock')
        lock.write_text('inspect me')
        self.call(['status', '--state', str(self.state)], False)
        self.assertEqual(lock.read_text(), 'inspect me')
        lock.unlink()
        value = self.current()
        value['schema_version'] = 99
        self.state.write_text(json.dumps(value))
        self.call(['status', '--state', str(self.state)], False)

    def test_concurrent_updates_commit_only_one_revision(self):
        events = [self.event_data('interrupted', intended_effects='read-only fixture', last_worker_ref='worker', observations='unknown') for _ in range(2)]
        paths = [self.json_file(f'concurrent-{i}.json', v) for i, v in enumerate(events)]
        processes = [subprocess.Popen([sys.executable, str(HELPER), 'apply', '--state', str(self.state), '--event', str(p)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=self.base) for p in paths]
        outputs = [p.communicate() for p in processes]
        self.assertEqual(sorted((p.returncode for p in processes)), [0, 1], outputs)
        self.assertEqual(self.current()['revision'], 1)

    def test_git_dirty_untracked_and_missing_paths(self):
        subprocess.run(['git', 'init', '-q', str(self.project)], check=True)
        subprocess.run(['git', '-C', str(self.project), 'add', '.'], check=True)
        self.source.write_text('dirty tracked source')
        new = self.write(self.project / 'untracked.txt', 'new')
        self.config.unlink()
        self.brief['source'] = {'mode': 'git', 'exclude': [], 'required': []}
        self.initialize()
        manifest_path = self.snapshot()
        manifest = json.loads(Path(manifest_path).read_text())
        self.assertIn(str(new), manifest['inputs'])
        self.assertTrue(manifest['inputs'][str(self.config)]['missing'])
        self.assertEqual(manifest['inputs'][str(self.source)]['size'], len('dirty tracked source'))

    def test_rejection_after_status_validation_never_commits(self):
        self.proof()
        self.accept()
        self.evidence.chmod(0)
        self.apply('interrupted', intended_effects='inspection', last_worker_ref='worker', observations='pending', ok=False)
        self.evidence.chmod(0o644)

    def stage_skill_tree(self):
        global HELPER
        original = HELPER
        staged_skills = self.base / 'staged' / 'skills'
        shutil.copytree(original.parents[2], staged_skills, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        HELPER = staged_skills / 'aapilot' / 'scripts' / 'work_receipts.py'
        self.addCleanup(self.restore_helper, original)
        return staged_skills

    def restore_helper(self, original):
        global HELPER
        HELPER = original

    def tree_identity(self, root):
        return {
            str(path.relative_to(root)): (path.read_bytes() if path.is_file() else None, path.stat().st_mode)
            for path in root.rglob('*')
        }

    def test_loaded_helper_change_stales_proof(self):
        staged_skills = self.stage_skill_tree()
        before = self.tree_identity(staged_skills)
        self.initialize()
        self.proof()
        manifest = json.loads((self.run / 'snapshot' / 'manifest.json').read_text())
        implementation = [HELPER, *sorted((HELPER.parent / '_work_receipts').rglob('*.py'))]
        for path in implementation:
            with self.subTest(module=path.name):
                self.assertIn(str(path), manifest['inputs'])
                original = path.read_bytes()
                try:
                    path.write_bytes(original + b'\n# changed implementation\n')
                    self.assertFalse(self.status()['tasks']['root']['verified_now'])
                    self.assertIn(str(path), self.accept(ok=False)['error'])
                finally:
                    path.write_bytes(original)
        self.accept()
        self.assertEqual(self.tree_identity(staged_skills), before)

    def test_new_recursive_module_stales_proof(self):
        self.stage_skill_tree()
        self.initialize()
        self.proof()
        added = self.write(HELPER.parent / '_work_receipts' / 'nested' / 'inert.py', '# inert module\n')
        self.assertIn(str(added), self.accept(ok=False)['error'])
        added.unlink()
        added.parent.rmdir()
        self.accept()

    def test_removed_module_stales_proof(self):
        self.stage_skill_tree()
        removed = self.write(HELPER.parent / '_work_receipts' / 'inert.py', '# inert module\n')
        self.initialize()
        self.proof()
        manifest = json.loads((self.run / 'snapshot' / 'manifest.json').read_text())
        self.assertIn(str(removed), manifest['inputs'])
        removed.unlink()
        self.assertIn(str(removed), self.accept(ok=False)['error'])

    def test_replayed_event_does_not_replace_state_file(self):
        event = self.event_data('interrupted', intended_effects='read', last_worker_ref='worker', observations='unknown')
        self.apply(event=event)
        original_bytes = self.state.read_bytes()
        original_stat = self.state.stat()
        self.apply(event=event)
        self.assertEqual(self.state.read_bytes(), original_bytes)
        self.assertEqual(self.state.stat().st_mtime_ns, original_stat.st_mtime_ns)
        self.assertEqual(self.state.stat().st_ino, original_stat.st_ino)

    def test_conflicting_report_precedes_return_task_mismatch(self):
        self.assign('child')
        report_path = Path(self.report(task='child'))
        self.apply('returned', task='child', actor='worker', report=str(report_path))
        report = json.loads(report_path.read_text())
        report['producer'] = 'changed producer'
        report_path.write_text(json.dumps(report))
        result = self.apply('returned', task='root', report=str(report_path), ok=False)
        self.assertEqual(result['error'], 'conflicting repeated report ID')

    def test_runtime_state_in_loaded_tree_rejected(self):
        forbidden = HELPER.parent / 'forbidden-state.json'
        self.call(['init', '--state', str(forbidden), '--brief', str(self.run / 'brief.json')], False)
        self.assertFalse(forbidden.exists())

    # Accepted descendant receipts and resumed authority.
    def accepted_child(self):
        self.assign('child', owner='child-owner', claims=['child-claim'])
        self.assign('child-verifier', parent='child', actor='child-owner', owner='child-reviewer')
        self.snapshot('child-snapshot')
        report = self.report(name='child-proof', task='child-verifier', snapshot=str(self.run / 'child-snapshot/manifest.json'), claims={'child-claim': {'status': 'pass', 'observations': 'inspected'}})
        self.apply('returned', task='child-verifier', actor='child-reviewer', report=report)
        self.apply('verification', task='child', actor='child-owner', target='child', verifier_task='child-verifier', report=report)
        accepted = self.write(self.run / 'child-acceptance.txt', 'owner inspected child')
        self.apply('accept', task='child', actor='child-owner', rationale='inspected child', evidence_refs=[str(accepted)])
        return (Path(report), accepted)

    def integrated_proof(self):
        self.assign('verify')
        snapshot = self.snapshot('integrated-snapshot')
        evidence = self.write(self.run / 'integrated-evidence.txt', 'integrated observations')
        report = self.report(name='integrated-proof', producer='integrated-verifier', snapshot=snapshot, evidence=[str(evidence)])
        self.apply('returned', task='verify', actor='worker', report=report)
        self.apply('verification', target='root', verifier_task='verify', report=report)
        return evidence

    def test_accepted_child_receipts_stay_intact_through_ancestor_acceptance(self):
        report, accepted = self.accepted_child()
        # Sequential implementation may follow an accepted design snapshot.
        self.source.write_text('later implementation')
        evidence = self.integrated_proof()
        self.apply('accept', rationale='integrated inspection', evidence_refs=[str(evidence)])
        self.assertTrue(self.status()['tasks']['root']['currently_accepted'])
        manifest = json.loads((self.run / 'child-snapshot/manifest.json').read_text())
        archive = self.run / 'child-snapshot' / manifest['copies'][str(self.source)]
        for path in (report, self.evidence, accepted, archive):
            with self.subTest(path=path):
                original = path.read_bytes()
                path.write_bytes(original + b'changed')
                status = self.status()['tasks']
                self.assertFalse(status['root']['currently_accepted'])
                self.assertTrue(status['root']['gates'])
                path.write_bytes(original)
        # A later passing proof cannot conceal mutation of the accepted receipt.
        alternative = self.report(name='alternative-child-proof', task='child-verifier', snapshot=str(self.run / 'integrated-snapshot/manifest.json'), evidence=[str(evidence)], claims={'child-claim': {'status': 'pass', 'observations': 'later inspection'}})
        self.apply('returned', task='child-verifier', actor='child-reviewer', report=alternative)
        self.apply('verification', task='child', actor='child-owner', target='child', verifier_task='child-verifier', report=alternative)
        original = self.evidence.read_bytes()
        self.evidence.write_bytes(original + b'changed')
        self.assertFalse(self.status()['tasks']['root']['currently_accepted'])
        self.evidence.write_bytes(original)
        self.source.write_text('new current source')
        self.assertFalse(self.status()['tasks']['root']['currently_accepted'])

    def test_superseded_review_cannot_accept_without_claims(self):
        self.brief['claims'] = []
        self.brief['proof_kind'] = 'scoped'
        self.initialize()
        old = self.review()
        latest = self.review(unresolved=[{'id': 'boundary', 'question': 'Who owns state?', 'reason': 'Architecture unresolved'}])
        self.apply('accept', decision_review=old, rationale='Try older review', evidence_refs=[str(self.evidence)], ok=False)
        self.assertEqual(self.current()['tasks']['root']['decision_review'], latest)

    def test_uncertainty_blocks_equal_parent_child_and_named_aliases(self):
        self.brief['resources'].update({'app': str(self.source), 'repo-alias': str(self.project), 'service-alias': 'named:local-service'})
        self.initialize()
        for original, retry in [('repo', 'app'), ('app', 'repo'), ('repo', 'repo-alias'), ('service', 'service-alias')]:
            with self.subTest(original=original, retry=retry):
                self.initialize()
                self.assign('writer', owner='editor', resources=[original])
                self.apply('interrupted', task='writer', actor='editor', intended_effects='write', last_worker_ref='worker', observations='unknown')
                self.assertIn('uncertain', self.assign('retry', resources=[retry], ok=False)['error'])

    def test_accepted_child_returned_artifact_is_protected(self):
        assigned = self.assign('child', owner='child-owner')['tasks']['child']
        self.assertIs(assigned['verified_now'], False)
        self.assertEqual(assigned['proof_status'], 'no_claims')
        artifact = self.write(self.run / 'child-artifact.txt', 'accepted design artifact')
        report = self.report(name='child-return', task='child', producer='designer', snapshot=None, claims={}, artifacts=[str(artifact)], evidence=[])
        returned = self.apply('returned', task='child', actor='child-owner', report=report)['tasks']['child']
        self.assertIs(returned['verified_now'], False)
        self.assertEqual(returned['proof_status'], 'no_claims')
        accepted = self.apply('accept', task='child', actor='child-owner', rationale='inspected returned design', evidence_refs=[str(self.evidence)])['tasks']['child']
        self.assertTrue(accepted['currently_accepted'])
        self.assertIs(accepted['verified_now'], False)
        self.assertEqual(accepted['proof_status'], 'no_claims')
        evidence = self.integrated_proof()
        self.apply('accept', rationale='integrated inspection', evidence_refs=[str(evidence)])
        artifact.write_text('changed design')
        status = self.status()['tasks']
        self.assertFalse(status['root']['currently_accepted'])
        self.assertFalse(status['child']['currently_accepted'])
        self.assertEqual(status['child']['proof_status'], 'no_claims')
        self.assertIs(status['child']['verified_now'], False)
        self.apply('accept', task='child', actor='child-owner', rationale='mutated artifact', evidence_refs=[str(self.evidence)], ok=False)

    def test_resume_allows_fresh_proof_and_acceptance_after_old_acceptance(self):
        self.proof()
        self.accept()
        package = self.checkpoint_package()
        self.apply('checkpoint', checkpoint_id='visual', package=str(package), reason='review', decision='approve')
        response = self.checkpoint_response()
        self.apply('resume', checkpoint_id='visual', authority_revision=0, human_response=str(response))
        self.assertFalse(self.status()['tasks']['root']['currently_accepted'])
        self.accept(ok=False)
        evidence = self.integrated_proof_after_resume()
        self.apply('accept', rationale='fresh resumed inspection', evidence_refs=[str(evidence)])
        self.assertTrue(self.status()['tasks']['root']['currently_accepted'])

    def integrated_proof_after_resume(self):
        self.assign('resumed-verifier', owner='resumed-worker')
        snapshot = self.snapshot('resumed-snapshot')
        report = self.report(name='resumed-proof', task='resumed-verifier', producer='resumed-independent', snapshot=snapshot)
        self.apply('returned', task='resumed-verifier', actor='resumed-worker', report=report)
        self.apply('verification', target='root', verifier_task='resumed-verifier', report=report)
        return self.evidence

    def test_compatible_replacement_chain_settles_cancelled_required_work(self):
        self.assign('original', owner='designer', claims=['design'])
        self.apply('cancelled', task='original', reason='failed dispatch')
        self.assign('repair', owner='repairer', claims=['design'], supersedes='original')
        self.apply('cancelled', task='repair', reason='repair interrupted')
        self.assign('replacement', owner='new-worker', claims=['design'], supersedes='repair')
        self.assign('replacement-verifier', owner='reviewer')
        snapshot = self.snapshot('replacement-snapshot')
        report = self.report(name='replacement-proof', task='replacement-verifier', snapshot=snapshot, claims={'design': {'status': 'pass', 'observations': 'inspected repaired design'}})
        self.apply('returned', task='replacement-verifier', actor='reviewer', report=report)
        self.apply('verification', task='replacement', actor='new-worker', target='replacement', verifier_task='replacement-verifier', report=report)
        self.apply('accept', task='replacement', actor='new-worker', rationale='inspected repair', evidence_refs=[str(self.evidence)])
        self.proof(producer='root-verifier')
        self.accept()
        state = self.current()
        self.assertEqual(state['tasks']['original']['status'], 'cancelled')
        self.assertEqual(state['tasks']['repair']['status'], 'cancelled')
        self.assertTrue(state['tasks']['replacement']['required'])
        self.assertTrue(self.status()['tasks']['root']['currently_accepted'])

    def test_incompatible_supersession_cannot_waive_required_work(self):
        self.assign('original', claims=['design'], proof_kind='production')
        for changes in ({'claims': []}, {'actions': ['read', 'write']}, {'resources': ['repo', 'service']}, {'proof_kind': 'scoped'}, {'required': False}, {'supersedes': 'root'}):
            with self.subTest(changes=changes):
                assignment = {
                    'claims': ['design'],
                    'proof_kind': 'production',
                    'supersedes': 'original',
                    **changes,
                }
                self.assign('replacement', ok=False, **assignment)
        self.assign('other-parent', actions=['read', 'delegate'])
        self.assign('unrelated', parent='other-parent', actor='worker', owner='other', claims=['design'], proof_kind='production', supersedes='original', ok=False)

    def test_checkpoint_package_must_match_before_resume(self):
        package = self.checkpoint_package()
        self.apply('checkpoint', checkpoint_id='visual', package=str(package), reason='review', decision='approve')
        response = self.checkpoint_response()
        package.write_text('different preview')
        self.assertIn('checkpoint package', self.apply('resume', checkpoint_id='visual', authority_revision=0, human_response=str(response), ok=False)['error'])

    def test_resumed_response_and_package_remain_current_acceptance_inputs(self):
        package = self.checkpoint_package()
        self.apply('checkpoint', checkpoint_id='visual', package=str(package), reason='review', decision='approve')
        response = self.checkpoint_response()
        self.apply('resume', checkpoint_id='visual', authority_revision=0, human_response=str(response))
        self.proof()
        for path in (response, package):
            with self.subTest(path=path):
                original = path.read_bytes()
                path.write_bytes(original + b'changed')
                self.assertIn('resumption', self.accept(ok=False)['error'])
                path.write_bytes(original)
        self.accept()
    def test_exposure_after_execution_before_initial_findings_cannot_pass_discovery(self):
        context = {'fresh': True, 'prior_conclusions': False,
            'exposure': 'Lead supplied passing-readiness conclusions after commands but before initial findings returned.',
            'post_execution_conclusion_exposure': True,
            'isolation_limits': ['shared host; synthetic protocol regression'],
            'interval_complete': True,
            'exposures': [{'kind': 'prior-conclusions', 'stage': 'after-execution-before-initial-findings',
                'source_ref': str(self.host), 'description': 'Prior lead passing-readiness conclusions received'}]}
        self.proof(context=context)
        root = self.status()['tasks']['root']
        self.assertIs(root['verified_now'], False)
        self.assertEqual(root['proof_status'], 'unverified')
        # A final report claiming clean context cannot improve frozen facts.
        final = self.report(name='clean-summary')
        self.apply('returned', task='verify', actor='worker', report=final)
        self.apply('verification', target='root', verifier_task='verify', report=final)
        self.accept(ok=False)
        frozen = self.current()['tasks']['verify']['initial_findings']['record']['report']
        self.assertEqual(frozen['context'], context)

    def test_decision_reviews_bind_design_authority_and_do_not_invent_agreement(self):
        self.assign('missing-review', purpose='implementation', ok=False)
        unresolved = self.review(unresolved=[{'id': 'export', 'question': 'Which data?', 'reason': 'Unsettled consequential choice'}])
        self.assign('unresolved', purpose='implementation', decision_review=unresolved, ok=False)
        valid = self.review(decisions=[{'id': 'routine', 'question': 'Helper name?', 'selected': 'plain helper',
            'classification': 'routine', 'origin': {'kind': 'delegated'}},
            {'id': 'export', 'question': 'Which data?', 'selected': 'Accepted requirement scope', 'classification': 'product',
             'origin': {'kind': 'source', 'ref': str(self.req), 'locator': 'line 1', 'status': 'accepted'}},
            {'id': 'source-settled', 'question': 'Duplicate behavior?', 'selected': 'Leave unchanged', 'classification': 'product',
             'origin': {'kind': 'source', 'ref': str(self.req), 'locator': 'line 1', 'status': 'accepted'}}])
        self.assign('settled', purpose='implementation', decision_review=valid)
        self.assign('wrong-design', purpose='implementation', decision_review=valid, inputs=[str(self.procedure)], ok=False)
        self.req.write_text('Changed governing authority')
        self.assign('stale', purpose='implementation', decision_review=valid, ok=False)
        # Invalid consequential delegation fails in the review transaction itself.
        event = self.event_data('decision_review', resources=['repo'], artifact_refs=[str(self.req)], coverage='Export policy',
            authority_revision=0, decisions=[{'id': 'export', 'question': 'Which data?', 'selected': 'all',
                'classification': 'product', 'origin': {'kind': 'delegated'}}], unresolved=[], rationale='No human source')
        self.apply(event=event, ok=False)
        event['decisions'][0]['origin'] = {'kind': 'source', 'ref': str(self.procedure), 'locator': 'line 1', 'status': 'accepted'}
        event['id'] += '-unapproved-source'
        self.apply(event=event, ok=False)

    def test_superseded_review_cannot_assign_or_accept_claimless_root(self):
        self.brief['claims'] = []
        self.brief['proof_kind'] = 'scoped'
        self.initialize()
        old = self.review()
        latest = self.review(unresolved=[{'id': 'boundary', 'question': 'Who owns state?', 'reason': 'Architecture unresolved'}])
        self.assign('implement', purpose='implementation', decision_review=old, ok=False)
        self.apply('accept', decision_review=old, rationale='Try older review', evidence_refs=[str(self.evidence)], ok=False)
        self.assertEqual(self.current()['tasks']['root']['decision_review'], latest)
        self.assertFalse(self.status()['tasks']['root']['currently_accepted'])

    def test_implementation_dispatch_and_followup_recheck_current_design(self):
        design = self.write(self.project / 'design.md', 'Settled A')
        review = self.review(artifact_refs=[str(design)])
        self.assign('implement', purpose='implementation', decision_review=review, inputs=[str(design)])
        design.write_text('Changed B')
        self.apply('dispatch', task='implement', actor='worker', attempt_id='implement', operation='spawn',
            request_ref=str(self.host), host_ref=str(self.host), outcome='started', worker_id='native', ok=False)
        design.write_text('Settled A')
        self.apply('dispatch', task='implement', actor='worker', attempt_id='implement', operation='spawn',
            request_ref=str(self.host), host_ref=str(self.host), outcome='started', worker_id='native')
        self.review(unresolved=[{'id': 'boundary', 'question': 'Who owns state?', 'reason': 'Architecture unresolved'}])
        self.apply('dispatch_reserved', task='implement', actor='worker', attempt_id='more', operation='followup',
            reason='Continue native state', worker_id='native', ok=False)

    def test_implementation_followup_reservation_rechecks_current_review(self):
        review = self.review()
        self.assign('implement', purpose='implementation', decision_review=review)
        self.apply('dispatch', task='implement', actor='worker', attempt_id='implement', operation='spawn',
            request_ref=str(self.host), host_ref=str(self.host), outcome='started', worker_id='native')
        self.review(unresolved=[{'id': 'boundary', 'question': 'Who owns state?', 'reason': 'Architecture unresolved'}])
        self.apply('dispatch_reserved', task='implement', actor='worker', attempt_id='more', operation='followup',
            reason='Continue native state', worker_id='native', ok=False)

    def test_dispatch_readiness_is_current_read_only_and_uses_reserved_budget(self):
        self.brief['budget']['dispatches'] = 1
        self.initialize()
        design = self.write(self.project / 'design.md', 'Settled A')
        review = self.review(artifact_refs=[str(design)])
        self.assign('implement', purpose='implementation', decision_review=review, inputs=[str(design)])
        before = self.state.read_bytes()
        status = self.status()
        self.assertEqual(status['remaining_dispatches'], 0)
        self.assertTrue(status['tasks']['implement']['dispatch_eligible_now'])
        self.assertEqual(before, self.state.read_bytes())
        design.write_text('Changed B')
        self.assertFalse(self.status()['tasks']['implement']['dispatch_eligible_now'])
        design.write_text('Settled A')
        self.review(unresolved=[{'id': 'boundary', 'question': 'Who owns state?', 'reason': 'Architecture unresolved'}])
        self.assertFalse(self.status()['tasks']['implement']['dispatch_eligible_now'])

    def test_reserved_followup_rechecks_gate_at_started_receipt(self):
        review = self.review()
        self.assign('implement', purpose='implementation', decision_review=review)
        self.apply('dispatch', task='implement', actor='worker', attempt_id='implement', operation='spawn',
            request_ref=str(self.host), host_ref=str(self.host), outcome='started', worker_id='native')
        self.apply('dispatch_reserved', task='implement', actor='worker', attempt_id='more', operation='followup',
            reason='Continue native state', worker_id='native')
        self.review(unresolved=[{'id': 'boundary', 'question': 'Who owns state?', 'reason': 'Architecture unresolved'}])
        self.assertFalse(self.status()['tasks']['implement']['dispatch_eligible_now'])
        self.apply('dispatch', task='implement', actor='worker', attempt_id='more', operation='followup',
            request_ref=str(self.host), host_ref=str(self.host), outcome='started', worker_id='native', ok=False)
        self.apply('dispatch', task='implement', actor='worker', attempt_id='more', operation='followup',
            request_ref=str(self.host), host_ref=str(self.host), outcome='unknown', worker_id='native')
        self.assertTrue(self.current()['tasks']['implement']['uncertain'])
        self.assertEqual(self.status()['observed_attempts'], 2)

    def test_production_root_requires_observable_claims(self):
        self.brief['claims'] = []
        self.state.unlink()
        self.call(['init', '--state', str(self.state), '--brief', str(self.json_file('brief.json', self.brief))], ok=False)
        self.assertFalse(self.state.exists())

    def test_known_unresolved_choice_cannot_disappear_in_clear_review(self):
        self.review(unresolved=[{'id': 'boundary', 'question': 'Who owns state?', 'reason': 'Architecture unresolved'}])
        event = self.event_data('decision_review', authority_revision=0, resources=['repo'], artifact_refs=[str(self.req)],
            coverage='Reinspect', decisions=[], unresolved=[], rationale='Try dropping known choice')
        self.apply(event=event, ok=False)
        event['id'] += '-routine'
        event['decisions'] = [{'id': 'boundary', 'question': 'Who owns state?', 'selected': 'worker',
            'classification': 'routine', 'origin': {'kind': 'delegated'}}]
        self.apply(event=event, ok=False)
        self.review(decisions=[{'id': 'boundary', 'question': 'Who owns state?', 'selected': 'Contract owner',
            'classification': 'architecture', 'origin': {'kind': 'source', 'ref': str(self.req), 'locator': 'line 1', 'status': 'accepted'}}])

    def test_current_reviews_follow_resource_scope_and_event_order(self):
        repo = self.review(resources=['repo'])
        self.review(resources=['service'], unresolved=[{'id': 'service', 'question': 'Who owns service?', 'reason': 'Unresolved'}])
        self.assign('repo-implementation', purpose='implementation', decision_review=repo)
        # Review IDs sort differently from event chronology after e9.
        for unused in range(10):
            repo = self.review(resources=['repo'])
        self.assign('latest-implementation', purpose='implementation', decision_review=repo)

    def test_new_unresolved_child_review_still_blocks_ancestor_after_acceptance(self):
        self.accepted_child()
        self.review()
        self.review(task='child', actor='child-owner', unresolved=[{'id': 'boundary', 'question': 'Who owns state?', 'reason': 'New unresolved architecture'}])
        self.assertIn('unresolved consequential choices', ';'.join(self.status()['tasks']['root']['gates']))

    def test_failed_and_unknown_native_receipts_survive_closed_design_gate(self):
        for outcome in ('failed', 'unknown'):
            with self.subTest(outcome=outcome):
                self.initialize()
                design = self.write(self.project / 'design.md', 'Settled A')
                review = self.review(artifact_refs=[str(design)])
                self.assign('implement', purpose='implementation', decision_review=review, inputs=[str(design)])
                design.write_text('Changed after actual invocation')
                self.apply('dispatch', task='implement', actor='worker', attempt_id='implement', operation='spawn',
                    request_ref=str(self.host), host_ref=str(self.host), outcome=outcome, worker_id=None)
                status = self.status()
                self.assertEqual(status['observed_attempts'], 1)
                self.assertEqual(status['allocated_dispatches'], 1)
                self.assertEqual(self.current()['tasks']['implement']['uncertain'], outcome == 'unknown')

    def test_explicit_purpose_and_claimless_root_acceptance_require_review(self):
        self.brief['claims'] = []
        self.brief['proof_kind'] = 'scoped'
        self.initialize()
        event = self.event_data('accept', rationale='claimless scope', evidence_refs=[str(self.evidence)])
        self.apply(event=event, ok=False)
        self.brief.pop('purpose')
        self.state.unlink()
        self.call(['init', '--state', str(self.state), '--brief', str(self.json_file('brief.json', self.brief))], False)
        self.assertFalse(self.state.exists())

    def test_mandatory_checkpoint_cannot_be_omitted_for_root_or_implementation(self):
        self.brief.update(purpose='implementation', claims=[], proof_kind='scoped', checkpoint_obligations=[{'id': 'decision', 'before': 'implementation'}])
        self.initialize()
        review = self.review()
        self.assign('implement', purpose='implementation', decision_review=review, ok=False)
        self.accept(ok=False)
        self.apply('checkpoint', checkpoint_id='decision', package=str(self.checkpoint_package()), reason='Need actual answer', decision='fixture-decision')
        self.apply('resume', checkpoint_id='decision', authority_revision=0, human_response=str(self.checkpoint_response()))
        self.accept()
        self.assertTrue(self.status()['tasks']['root']['currently_accepted'])

    def test_free_text_and_choice_answers_bind_exact_question_package_and_source(self):
        package = self.checkpoint_package()
        self.apply('checkpoint', checkpoint_id='decision', package=str(package), reason='Ask focused question', decision='fixture-decision')
        response = self.checkpoint_response()
        original = json.loads(response.read_text())
        for changes in ({'checkpoint_event': 'invented'}, {'question_id': 'wrong'}, {'package_hash': 'wrong'},
                        {'authority_revision': 99}, {'answer': ''}, {'selected_option': 'invented'}):
            response.write_text(json.dumps(original | changes))
            self.apply('resume', checkpoint_id='decision', authority_revision=0, human_response=str(response), ok=False)
        response.write_text(json.dumps(original))
        self.apply('resume', checkpoint_id='decision', authority_revision=0, human_response=str(response))
        review = self.review(decisions=[{'id': 'fixture-decision', 'question': 'What fixture should continue?',
            'selected': original['answer'], 'classification': 'product', 'origin': {'kind': 'human',
                'checkpoint_event': original['checkpoint_event'], 'resume_event': self.current()['resumptions'][-1]['event']}}])
        self.assign('answered', purpose='implementation', decision_review=review)
        # A second distinct checkpoint uses concrete choices, with no manufactured free-text selection.
        package2 = self.json_file('choice.json', {'question_id': 'choice', 'question': 'Which fixture?', 'artifact_refs': [str(self.req)],
            'decision_ids': ['choice'], 'options': [{'id': 'a', 'label': 'A', 'consequences': 'first'},
                {'id': 'b', 'label': 'B', 'consequences': 'second'}], 'recommendation': 'a'})
        self.apply('checkpoint', checkpoint_id='decision', package=str(package2), reason='Choice', decision='choice')
        response2 = self.checkpoint_response()
        content = json.loads(response2.read_text())
        self.apply('resume', checkpoint_id='decision', authority_revision=1, human_response=str(response2), ok=False)
        response2.write_text(json.dumps(content | {'selected_option': 'a'}))
        self.apply('resume', checkpoint_id='decision', authority_revision=1, human_response=str(response2))
        source = Path(content['source_ref'])
        source.write_text('mutated actual answer source')
        self.assertIn('resumption', ';'.join(self.status()['tasks']['root']['gates']))

    def test_native_allocations_results_followups_and_unknowns_are_not_refunded(self):
        self.brief['budget']['dispatches'] = 3
        self.initialize()
        self.assign('native', owner='native-owner')
        self.assertEqual(self.status()['allocated_dispatches'], 1)
        self.assertEqual(self.status()['pending_reservations'], 1)
        self.apply('dispatch', task='native', actor='native-owner', attempt_id='native', operation='spawn',
            request_ref=str(self.host), host_ref=str(self.host), outcome='started', worker_id='actual-fixture-worker')
        self.assertEqual(self.status()['allocated_dispatches'], 1)
        self.apply('dispatch_reserved', task='native', actor='native-owner', attempt_id='continue', operation='followup',
            reason='Retain live process state', worker_id='actual-fixture-worker')
        self.assertEqual(self.status()['allocated_dispatches'], 2)
        self.apply('dispatch', task='native', actor='native-owner', attempt_id='continue', operation='followup',
            request_ref=str(self.host), host_ref=str(self.host), outcome='started', worker_id='wrong', ok=False)
        self.apply('dispatch', task='native', actor='native-owner', attempt_id='continue', operation='followup',
            request_ref=str(self.host), host_ref=str(self.host), outcome='unknown', worker_id='actual-fixture-worker')
        self.assign('retry', ok=False)
        self.apply('reconciled', task='native', actor='native-owner', evidence_refs=[str(self.evidence)],
            worker_active=False, outcome='known', observations='Fixture effects inspected')
        self.assign('failed')
        event = self.event_data('dispatch', task='failed', actor='worker', attempt_id='failed', operation='spawn',
            request_ref=str(self.host), host_ref=str(self.host), outcome='failed', worker_id=None)
        self.apply(event=event)
        before = self.state.read_bytes()
        self.apply(event=event)
        self.assertEqual(before, self.state.read_bytes())
        status = self.status()
        self.assertEqual((status['allocated_dispatches'], status['observed_attempts'], status['started_attempts'],
            status['failed_attempts'], status['unknown_attempts'], status['remaining_dispatches']), (3, 3, 1, 1, 1, 0))
        self.apply('dispatch', task='failed', actor='worker', attempt_id='failed', operation='spawn',
            request_ref=str(self.host), host_ref=str(self.host), outcome='failed', worker_id=None, ok=False)
        self.apply('returned', task='failed', actor='worker', report=self.report(name='failed-return', task='root'), ok=False)

    def test_preflight_and_first_findings_cannot_be_late_missing_or_replaced(self):
        self.assign()
        self.apply('dispatch', task='verify', actor='worker', attempt_id='verify', operation='spawn',
            request_ref=str(self.host), host_ref=str(self.host), outcome='started', worker_id='native', ok=False)
        self.snapshot()
        report = self.report()
        frozen = self.current()['tasks']['verify']['initial_findings']
        self.apply('initial_findings', task='verify', actor='worker', preflight_event='wrong', dispatch_event='wrong',
            findings=report, context=frozen['context'], context_evidence_refs=[str(self.host)], ok=False)
        self.apply('returned', task='verify', actor='worker', report=report)
        self.apply('verification', target='root', verifier_task='verify', report=report)
        self.accept()
        initial_path = next(p for p in frozen['record']['hashes'] if p.endswith('-initial.json'))
        Path(initial_path).write_text('{}')
        self.assertFalse(self.status()['tasks']['root']['verified_now'])
        self.assertFalse(self.status()['tasks']['root']['currently_accepted'])

    def test_final_summary_cannot_upgrade_frozen_failed_claims_or_commands(self):
        for changes in ({'claims': {'behavior': {'status': 'fail', 'observations': 'Observed failure'}}},
                        {'commands': [{'command': 'actual failing check', 'exit_code': 1}]}):
            self.initialize()
            shutil.rmtree(self.run / 'snapshot', ignore_errors=True)
            self.proof(**changes)
            root = self.status()['tasks']['root']
            self.assertIs(root['verified_now'], False)
            self.assertEqual(root['proof_status'], 'unverified')
            final = self.report(name='upgraded')
            self.apply('returned', task='verify', actor='worker', report=final)
            self.apply('verification', target='root', verifier_task='verify', report=final)
            self.accept(ok=False)

    def test_authorized_audit_retains_qualifications_without_passing_discovery(self):
        context = {'fresh': True, 'prior_conclusions': True, 'exposure': 'Specified claims supplied',
            'isolation_limits': ['synthetic audit'], 'exposures': [], 'interval_complete': True}
        for required, eligible in [('independent-discovery', False), ('confirmation-audit', True)]:
            self.brief['required_review_mode'] = required
            self.initialize()
            shutil.rmtree(self.run / 'snapshot', ignore_errors=True)
            self.assign(review={'target': 'root', 'mode': 'confirmation-audit', 'claims': ['behavior']})
            self.snapshot()
            report = self.report(review_mode='confirmation-audit', context=context)
            self.apply('returned', task='verify', actor='worker', report=report)
            self.apply('verification', target='root', verifier_task='verify', report=report)
            self.assertEqual(self.status()['tasks']['root']['verified_now'], eligible)
            self.accept(ok=eligible)

    def test_nine_spawns_plus_one_followup_consume_ten_allocations(self):
        for index in range(9):
            task = 'native-' + str(index)
            self.assign(task, required=False)
            self.apply('dispatch', task=task, actor='worker', attempt_id=task, operation='spawn',
                request_ref=str(self.host), host_ref=str(self.host), outcome='started', worker_id=task + '-host-id')
        self.apply('dispatch_reserved', task='native-0', actor='worker', attempt_id='tenth', operation='followup',
            reason='Live fixture state retained', worker_id='native-0-host-id')
        reserved = self.status()
        self.assertEqual((reserved['allocated_dispatches'], reserved['observed_attempts'], reserved['pending_reservations']), (10, 9, 1))
        self.apply('dispatch', task='native-0', actor='worker', attempt_id='tenth', operation='followup',
            request_ref=str(self.host), host_ref=str(self.host), outcome='failed', worker_id='native-0-host-id')
        observed = self.status()
        self.assertEqual((observed['allocated_dispatches'], observed['observed_attempts'], observed['remaining_dispatches']), (10, 10, 0))
        self.assign('eleventh', ok=False)

    def test_missing_interval_and_wrong_preflight_request_reject_without_mutation(self):
        self.assign()
        snapshot = self.snapshot()
        context = {'fresh': True, 'prior_conclusions': False, 'exposure': 'Raw fixture inputs only',
            'isolation_limits': ['synthetic fixture'], 'exposures': []}
        self.apply('review_preflight', task='verify', actor='worker', snapshot=snapshot, environment=str(self.env),
            mode='independent-discovery', context=context, host_request_ref=str(self.host))
        self.apply('dispatch', task='verify', actor='worker', attempt_id='verify', operation='spawn',
            request_ref=str(self.evidence), host_ref=str(self.host), outcome='started', worker_id='native-fixture', ok=False)
        self.apply('dispatch', task='verify', actor='worker', attempt_id='verify', operation='spawn',
            request_ref=str(self.host), host_ref=str(self.host), outcome='started', worker_id='native-fixture')
        findings = self.json_file('raw-findings.json', {'id': 'raw', 'task': 'verify', 'producer': 'native-fixture',
            'host_ref': str(self.host), 'context': context})
        task = self.current()['tasks']['verify']
        self.apply('initial_findings', task='verify', actor='worker', preflight_event=task['preflight']['id'],
            dispatch_event=self.current()['attempts']['verify']['event'], findings=str(findings),
            context=context, context_evidence_refs=[str(self.host)], ok=False)
        self.apply('returned', task='verify', actor='worker', report=str(findings), ok=False)

    def presentation(self, minimal=False):
        self.brief.update(verification_requirement='owner-presentation', purpose='implementation',
            presentation_eligibility={'classification': 'prescribed-presentation', 'request_ref': str(self.req),
                'locator': 'line 1', 'prescription': 'Change the existing label from create to Create',
                'basis': 'Exact request; existing component; meaning, behavior, data, contracts, permissions, dependencies and deployment unchanged; all decisions settled',
                'components': [str(self.source)]})
        if minimal:
            for name in ('purpose', 'proof_kind', 'requirements', 'decisions', 'procedures', 'principles',
                         'checkpoints', 'checkpoint_obligations', 'source', 'constraints', 'expected_outputs', 'next_action'):
                self.brief.pop(name, None)
        self.initialize()

    def owner_report(self, name='owner-proof', **changes):
        report = {'id': name, 'task': 'root', 'producer': 'lead', 'proof_basis': 'owner-presentation',
            'snapshot': str(self.run / 'owner-snapshot' / 'manifest.json'), 'environment': str(self.env),
            'claims': {'behavior': {'status': 'pass', 'observations': 'Prescribed label and unchanged surrounding source checked'}},
            'commands': [{'command': 'inspect final source and diff', 'exit_code': 0}],
            'diff_ref': str(self.write(self.run / (name + '.diff'), '-create\n+Create\n')),
            'eligibility_review': 'Final diff only changes the prescribed case; eligibility still applies',
            'evidence': [str(self.evidence)], 'coverage': 'source and diff', 'effects': 'one label',
            'limitations': 'Appearance not exercised; source inspection only'}
        report.update(changes)
        return str(self.json_file(name + '.json', report))

    def owner_proof(self, **changes):
        self.source.write_text('print("Create")\n')
        self.snapshot(name='owner-snapshot')
        report = self.owner_report(**changes)
        self.apply('returned', report=report)
        return report

    def test_compact_public_cli_is_zero_worker_and_honest_about_owner_proof(self):
        self.brief['budget']['dispatches'] = 0
        self.presentation(minimal=True)
        before_edit = self.current()['presentation_eligibility']
        self.assertIn(str(self.source), before_edit['source_hashes'])
        self.owner_proof()
        # The compact entry generates routine review metadata; callers author no
        # native-worker packet and may reference that current review implicitly.
        self.apply(event=self.event_data('accept', rationale='Actual source and diff checked', evidence_refs=[str(self.evidence)]))
        status = self.status()
        root = status['tasks']['root']
        self.assertEqual((status['allocated_dispatches'], status['observed_attempts']), (0, 0))
        self.assertEqual(root['verification_requirement'], 'owner-presentation')
        self.assertEqual(root['actual_proof_basis'], 'owner-presentation')
        self.assertEqual(root['proof_status'], 'owner-checked')
        self.assertTrue(root['checked_now'])
        self.assertFalse(root['verified_now'])
        self.assertTrue(root['currently_accepted'])
        self.assertEqual(self.current()['tasks']['root']['acceptance']['proof_reports'], ['owner-proof'])
        self.assertEqual(list(self.current()['tasks']), ['root'])
        self.apply('returned', report=self.owner_report(name='later-failure',
            claims={'behavior': {'status': 'fail', 'observations': 'Later contradictory observation'}}))
        self.assertFalse(self.status()['tasks']['root']['currently_accepted'])
        self.accept(ok=False)

    def test_owner_requirement_rejects_missing_or_ineligible_basis_and_empty_claims(self):
        self.presentation()
        original = copy.deepcopy(self.brief)
        for changes in ({'claims': []}, {'presentation_eligibility': None},
                        {'presentation_eligibility': original['presentation_eligibility'] | {'classification': 'business-semantic'}},
                        {'presentation_eligibility': original['presentation_eligibility'] | {'request_ref': str(self.evidence)}},
                        {'presentation_eligibility': original['presentation_eligibility'] | {'components': []}}):
            self.brief = original | changes
            self.state.unlink(missing_ok=True)
            self.call(['init', '--state', str(self.state), '--brief', str(self.json_file('brief.json', self.brief))], False)
            self.assertFalse(self.state.exists())

    def test_owner_proof_cannot_cover_edits_outside_prescribed_components(self):
        self.presentation()
        self.owner_proof()
        self.req.write_text('Changed request meaning after eligibility')
        self.accept(ok=False)
        self.req.write_text('Create once; duplicate leaves state unchanged.\n')
        self.brief['source'] = {'mode': 'roots', 'roots': [str(self.project)], 'exclude': [], 'required': []}
        self.initialize()
        self.config.write_text('{"behavior":"changed"}\n')
        shutil.rmtree(self.run / 'owner-snapshot')
        self.owner_proof()
        self.assertIn('outside prescribed presentation components', ';'.join(self.status()['tasks']['root']['gates']))
        self.accept(ok=False)

    def test_owner_missing_later_failed_or_claimless_report_blocks_older_pass(self):
        self.presentation()
        self.accept(ok=False)
        for case, changes in (
                ('claimless', {'claims': {}}),
                ('failed', {'claims': {'behavior': {'status': 'fail', 'observations': 'Changed meaning'}}}),
                ('missing eligibility review', {'eligibility_review': ''}),
                ('missing diff', {'diff_ref': None}),
                ('missing commands', {'commands': []}),
                ('missing evidence', {'evidence': []}),
                ('wrong producer', {'producer': 'other'})):
            with self.subTest(case=case):
                self.presentation()
                shutil.rmtree(self.run / 'owner-snapshot', ignore_errors=True)
                self.owner_proof()
                self.assertTrue(self.status()['tasks']['root']['checked_now'])
                self.apply('returned', report=self.owner_report(name='later-' + str(self.counter), **changes))
                self.accept(ok=False)
                self.assertFalse(self.status()['tasks']['root']['checked_now'])

    def test_owner_older_pass_replay_cannot_replace_latest_failure(self):
        self.presentation()
        passing_report = self.owner_proof(name='pass-a')
        self.assertTrue(self.status()['tasks']['root']['checked_now'])
        self.apply('returned', report=self.owner_report(name='failure-b',
            claims={'behavior': {'status': 'fail', 'observations': 'Later contradictory observation'}}))
        self.assertFalse(self.status()['tasks']['root']['checked_now'])

        replay = self.event_data('returned', report=passing_report)
        before = self.state.read_bytes()
        result = self.apply(event=replay, ok=False)
        self.assertIn('older return cannot replace latest report', result['error'])
        self.assertEqual(before, self.state.read_bytes())
        self.assertEqual(self.current()['tasks']['root']['returns'], ['pass-a', 'failure-b'])
        self.accept(ok=False)
        self.assertFalse(self.status()['tasks']['root']['checked_now'])

    def test_owner_current_source_evidence_and_diff_are_required(self):
        for stale in ('source', 'evidence', 'diff'):
            with self.subTest(stale=stale):
                self.presentation()
                shutil.rmtree(self.run / 'owner-snapshot', ignore_errors=True)
                report = self.owner_proof()
                path = {'source': self.source, 'evidence': self.evidence,
                        'diff': Path(json.loads(Path(report).read_text())['diff_ref'])}[stale]
                path.write_text(path.read_text() + '\nchanged')
                self.accept(ok=False)
                before = self.state.read_bytes()
                self.assertFalse(self.status()['tasks']['root']['checked_now'])
                self.assertEqual(before, self.state.read_bytes())

    def test_escalation_strengthens_same_run_without_changing_authority_or_budget(self):
        self.presentation()
        self.owner_proof()
        original = self.current()
        self.apply('verification_escalated', requirement='independent', reason='Actual diff includes behavior',
            evidence_refs=[str(self.evidence)], actions=['write'], resources=['repo'])
        current = self.current()
        for key in ('budget', 'actions', 'resources'):
            self.assertEqual(current['brief'][key], original['brief'][key])
        for key in ('dispatched', 'authority_revision', 'reports', 'proofs'):
            self.assertEqual(current[key], original[key])
        self.assertEqual(current['brief']['verification_requirement'], 'independent')
        self.assertEqual(self.status()['tasks']['root']['actual_proof_basis'], 'none')
        self.accept(ok=False)
        self.apply('verification_escalated', requirement='owner-presentation', reason='Try downgrade', evidence_refs=[str(self.evidence)], ok=False)
        self.proof()
        self.accept()
        self.assertTrue(self.status()['tasks']['root']['verified_now'])

    def test_escalated_compact_root_has_explicit_non_dispatch_diagnostic(self):
        self.brief['budget']['dispatches'] = 0
        self.presentation(minimal=True)
        self.owner_proof()
        self.apply('verification_escalated', requirement='independent', reason='Actual diff includes behavior',
            evidence_refs=[str(self.evidence)])
        before = self.state.read_bytes()
        root = self.status()['tasks']['root']
        self.assertEqual(before, self.state.read_bytes())
        self.assertFalse(root['dispatch_eligible_now'])
        self.assertIn('root owner is not a native child assignment', root['dispatch_gates'])
        self.assertNotIn("'inputs'", root['dispatch_gates'])
        self.assertFalse(root['acceptance_eligible_now'])
        self.assertIn('missing verification', ';'.join(root['gates']))
        result = self.apply('accept', ok=False, rationale='Owner proof cannot satisfy independent requirement',
            evidence_refs=[str(self.evidence)])
        self.assertIn('missing verification', result['error'])
        self.assertIn('root dispatch budget exhausted', result['error'])

    def test_escalation_rejects_widening_and_records_exhausted_proof_obligation(self):
        self.presentation()
        payload = {'requirement': 'independent', 'reason': 'Broader effects', 'evidence_refs': [str(self.evidence)]}
        for changes in ({'actions': ['publish']}, {'resources': ['outside']}, {'budget': {'dispatches': 999}}):
            self.apply('verification_escalated', **(payload | changes), ok=False)
        self.brief['budget']['dispatches'] = 0
        self.initialize()
        self.apply('verification_escalated', **payload)
        self.assertEqual(self.status()['remaining_dispatches'], 0)
        self.assertEqual(self.status()['tasks']['root']['verification_requirement'], 'independent')
        self.assertIn('budget exhausted', ';'.join(self.status()['tasks']['root']['gates']))
        self.accept(ok=False)
        self.assign(ok=False)

    def test_owner_requirement_cannot_be_used_by_children_or_downgraded_on_resume(self):
        self.assign('child', verification_requirement='owner-presentation', ok=False)
        self.presentation()
        self.apply('verification_escalated', requirement='independent', reason='Need behavior proof', evidence_refs=[str(self.evidence)])
        self.apply('checkpoint', checkpoint_id='decision', package=str(self.checkpoint_package()), reason='Actual answer', decision='fixture-decision')
        self.apply('resume', checkpoint_id='decision', authority_revision=0, human_response=str(self.checkpoint_response()),
            updated_brief=self.brief, ok=False)

    def test_new_absent_requirement_is_independent_and_version2_is_read_only(self):
        self.assertEqual(self.current()['brief']['verification_requirement'], 'independent')
        self.proof()
        self.accept()
        self.assertEqual(self.status()['tasks']['root']['actual_proof_basis'], 'independent')
        self.assertTrue(self.status()['tasks']['root']['checked_now'])
        legacy = self.current()
        legacy['schema_version'] = 2
        self.state.write_text(json.dumps(legacy))
        before = self.state.read_bytes()
        root = self.status()['tasks']['root']
        self.assertEqual(root['historical_status'], 'accepted')
        self.assertFalse(root['verified_now'])
        self.assertFalse(root['checked_now'])
        self.assertEqual(root['verification_requirement'], 'unrecorded')
        self.apply(event=self.event_data('cancelled', reason='legacy mutation'), ok=False)
        self.snapshot(ok=False)
        self.assertEqual(before, self.state.read_bytes())

    def test_legacy_state_reports_history_without_inventing_recorded_gates(self):
        legacy = self.current()
        legacy['schema_version'] = 1
        legacy['tasks']['root']['status'] = 'accepted'
        for key in ('attempts', 'decision_reviews'):
            legacy.pop(key)
        self.state.write_text(json.dumps(legacy))
        before = self.state.read_bytes()
        result = self.status()
        self.assertTrue(result['legacy_unrecorded_gates'])
        self.assertEqual(result['tasks']['root']['historical_status'], 'accepted')
        root = result['tasks']['root']
        self.assertIs(root['verified_now'], False)
        self.assertEqual(root['proof_status'], 'unverified')
        self.assertFalse(root['currently_accepted'])
        self.assertFalse(root['acceptance_eligible_now'])
        self.assertFalse(root['dispatch_eligible_now'])
        self.assertEqual(root['gates'], ['legacy_unrecorded_gates: new version3 run required'])
        self.assertEqual(root['dispatch_gates'], root['gates'])
        self.assertNotIn('observed_attempts', result)
        self.apply(event=self.event_data('cancelled', reason='legacy mutation'), ok=False)
        self.snapshot(ok=False)
        self.assertEqual(self.state.read_bytes(), before)

if __name__ == '__main__':
    unittest.main(verbosity=2)
