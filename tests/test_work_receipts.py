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
        self.call(['init', '--state', str(self.state), '--brief', str(self.json_file('brief.json', self.brief))])

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
        event = event or self.event_data(kind, **payload)
        before = self.state.read_bytes()
        result = self.call(['apply', '--state', str(self.state), '--event', str(self.json_file('event.json', event))], ok)
        if not ok:
            self.assertEqual(before, self.state.read_bytes(), 'rejected transition changed state')
        return result

    def assign(self, task_id='verify', parent='root', owner='worker', actor='lead', ok=True, **changes):
        assignment = {
            'id': task_id,
            'parent': parent,
            'owner': owner,
            'objective': 'bounded assignment',
            'procedure': str(self.procedure),
            'actions': ['read'],
            'resources': ['repo'],
            'claims': [],
            'proof_kind': 'scoped',
            'inputs': [str(self.req)],
            'expected_artifacts': ['report'],
        }
        assignment.update(changes)
        return self.apply('assign', task=parent, actor=actor, assignment=assignment, ok=ok)

    def snapshot(self, name='snapshot', task='root', ok=True):
        result = self.call(['snapshot', '--state', str(self.state), '--task', task, '--out', str(self.run / name)], ok)
        return result.get('manifest')

    def report(self, name='proof', task='verify', **changes):
        report = {
            'id': name,
            'task': task,
            'producer': 'fresh-verifier',
            'host_ref': str(self.host),
            'editors': ['editor'],
            'review_mode': 'independent-discovery',
            'context': {
                'fresh': True,
                'prior_conclusions': False,
                'exposure': 'requirements and actual artifact only',
                'isolation_limits': 'shared filesystem; synthetic fixture',
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
        return str(self.json_file(name + '.json', report))

    def proof(self, **changes):
        self.assign()
        self.snapshot()
        report = self.report(**changes)
        self.apply('returned', task='verify', actor='worker', report=report)
        self.apply('verification', target='root', verifier_task='verify', report=report)
        return report

    def accept(self, ok=True):
        return self.apply('accept', rationale='Inspected requirements and observed effects', evidence_refs=[str(self.evidence)], ok=ok)

    # Lifecycle, authority and proof eligibility.
    def test_returned_is_not_verified_or_accepted(self):
        report = self.report(task='root', name='return', producer='editor')
        self.apply('returned', report=report)
        self.assertEqual(self.status()['tasks']['root']['historical_status'], 'returned')
        self.accept(ok=False)

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
        self.assertTrue(before['verified_now'])
        self.assertFalse(before['currently_accepted'])
        self.accept()
        self.assertTrue(self.status()['tasks']['root']['currently_accepted'])

    def test_scoped_design_proof_does_not_require_execution(self):
        self.brief['proof_kind'] = 'scoped'
        self.initialize()
        self.proof(executable=False, commands=[], review_mode='scoped', context={})
        self.accept()

    def test_latest_claim_proof_cannot_fall_back_to_older_pass(self):
        self.proof()
        for status in ('fail', 'unverified', 'pass'):
            report = self.report(name='later-' + status, claims={'behavior': {'status': status, 'observations': 'new same-artifact observation'}})
            self.apply('returned', task='verify', actor='worker', report=report)
            self.apply('verification', target='root', verifier_task='verify', report=report)
            self.assertEqual(self.status()['tasks']['root']['verified_now'], status == 'pass')
            if status != 'pass':
                self.accept(ok=False)
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
        self.proof(producer='same-worker', editors=[])
        self.accept(ok=False)

    # Source and retained evidence identity.
    def test_current_source_config_verifier_env_requirements_and_evidence(self):
        self.proof()
        for path in [self.source, self.config, self.verifier, self.env, self.req, self.evidence]:
            with self.subTest(path=path.name):
                original = path.read_bytes()
                path.write_bytes(original + b'\n')
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
        self.apply('checkpoint', checkpoint_id='visual', package=str(self.evidence), reason='requires eyeballing', decision='approve preview')
        used = self.status()['remaining_dispatches']
        self.assign('blocked', ok=False)
        self.accept(ok=False)
        response = self.write(self.run / 'human.txt', 'SYNTHETIC human-response protocol fixture only')
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
        self.assign('child', owner='child-owner')
        artifact = self.write(self.run / 'child-artifact.txt', 'accepted design artifact')
        report = self.report(name='child-return', task='child', producer='designer', snapshot=None, claims={}, artifacts=[str(artifact)], evidence=[])
        self.apply('returned', task='child', actor='child-owner', report=report)
        self.apply('accept', task='child', actor='child-owner', rationale='inspected returned design', evidence_refs=[str(self.evidence)])
        evidence = self.integrated_proof()
        self.apply('accept', rationale='integrated inspection', evidence_refs=[str(evidence)])
        artifact.write_text('changed design')
        self.assertFalse(self.status()['tasks']['root']['currently_accepted'])

    def test_resume_allows_fresh_proof_and_acceptance_after_old_acceptance(self):
        self.proof()
        self.accept()
        package = self.write(self.run / 'package.txt', 'current artifact')
        self.apply('checkpoint', checkpoint_id='visual', package=str(package), reason='review', decision='approve')
        response = self.write(self.run / 'human.txt', 'synthetic response')
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
        package = self.write(self.run / 'package.txt', 'preview shown')
        self.apply('checkpoint', checkpoint_id='visual', package=str(package), reason='review', decision='approve')
        response = self.write(self.run / 'human.txt', 'synthetic response')
        package.write_text('different preview')
        self.assertIn('checkpoint package', self.apply('resume', checkpoint_id='visual', authority_revision=0, human_response=str(response), ok=False)['error'])

    def test_resumed_response_and_package_remain_current_acceptance_inputs(self):
        package = self.write(self.run / 'package.txt', 'preview shown')
        self.apply('checkpoint', checkpoint_id='visual', package=str(package), reason='review', decision='approve')
        response = self.write(self.run / 'human.txt', 'synthetic response')
        self.apply('resume', checkpoint_id='visual', authority_revision=0, human_response=str(response))
        self.proof()
        for path in (response, package):
            with self.subTest(path=path):
                original = path.read_bytes()
                path.write_bytes(original + b'changed')
                self.assertIn('resumption', self.accept(ok=False)['error'])
                path.write_bytes(original)
        self.accept()
if __name__ == '__main__':
    unittest.main(verbosity=2)
