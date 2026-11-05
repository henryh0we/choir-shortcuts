"""Windows/Linux file-transport acceptance tests; no device or network required."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[2] / "scripts/ipad_pipeline.py"
SPEC = importlib.util.spec_from_file_location("ipad_pipeline", SCRIPT)
pipeline = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pipeline)


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="Jelly exchange £ with spaces ")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.root = self.base / "shared directory"
        self.source = self.base / "Henry's source £ $ ;.jelly"
        self.data = b'import Shortcuts\ntext(text: "Hello") >> greeting\nquicklook(input: greeting)\n'
        self.source.write_bytes(self.data)

    def prepare(self, **kwargs):
        return pipeline.prepare(self.root, self.source, **kwargs)

    def cli(self, *args, expected=0):
        output, error = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(error):
            code = pipeline.main([*args, "--exchange", str(self.root)])
        self.assertEqual(code, expected, error.getvalue() or output.getvalue())
        return json.loads(output.getvalue()) if output.getvalue() else error.getvalue()

    def test_prepare_preserves_exact_source_and_unique_revisions(self):
        one = self.prepare()
        old_files = {p.name: p.read_bytes() for p in (self.root / "requests" / one["build_id"]).iterdir()}
        self.assertEqual(self.source.read_bytes(), self.data)
        self.source.write_bytes(self.data.replace(b"Hello", b"Revised"))
        two = self.prepare()
        self.assertNotEqual(one["build_id"], two["build_id"])
        self.assertNotEqual(one["source"]["sha256"], two["source"]["sha256"])
        self.assertEqual(old_files, {p.name: p.read_bytes() for p in (self.root / "requests" / one["build_id"]).iterdir()})
        self.assertTrue(self.cli("verify")["consistent"])

    def test_preserves_bom_crlf_unicode_and_delivered_hash(self):
        data = b'\xef\xbb\xbfimport Shortcuts\r\ntext(text: "\xc2\xa3")\r\n'
        self.source.write_bytes(data)
        request = self.prepare()
        self.assertEqual(request["source"]["encoding"], "utf-8-bom")
        self.assertEqual(request["source"]["sha256"], pipeline.digest(data))
        self.assertEqual(request["source"]["delivered_sha256"], pipeline.digest(data))
        for name in ("source.txt", "source.jelly"):
            self.assertEqual((self.root / "requests" / request["build_id"] / name).read_bytes(), data)
        self.assertEqual(self.source.read_bytes(), data)

    def test_filename_names_overrides_and_same_path_persistence(self):
        source = self.base / "util-archive-choir-pdf.jelly"
        source.write_bytes(self.data)
        first = pipeline.prepare(self.root, source)
        self.assertEqual(first["shortcut_name"], "UTIL - Archive Choir PDF")
        self.assertIsNone(first["name_from_build_id"])
        override = pipeline.prepare(self.root, source, name="TEST - Archive Trial")
        original = (self.root / "requests" / first["build_id"] / "request.json").read_bytes()
        source.write_bytes(self.data.replace(b"Hello", b"New revision"))
        revised = pipeline.prepare(self.root, source)
        self.assertEqual(revised["shortcut_name"], "TEST - Archive Trial")
        self.assertEqual(revised["name_from_build_id"], override["build_id"])
        self.assertNotEqual(revised["source"]["sha256"], override["source"]["sha256"])
        self.assertEqual((self.root / "requests" / first["build_id"] / "request.json").read_bytes(), original)
        self.assertTrue(self.cli("verify")["consistent"])

    def test_name_reuse_across_source_rename_and_path_isolation(self):
        original = self.prepare(name="TEST - Stable Display Name")
        moved = self.base / "renamed-source.jelly"
        self.source.rename(moved)
        fresh = pipeline.prepare(self.root, moved)
        self.assertEqual(fresh["shortcut_name"], "Renamed Source")
        reused = pipeline.prepare(self.root, moved, name_from_build=original["build_id"])
        self.assertEqual(reused["shortcut_name"], "TEST - Stable Display Name")
        self.assertEqual(reused["name_from_build_id"], original["build_id"])
        other = self.base / "other" / moved.name
        other.parent.mkdir()
        other.write_bytes(self.data)
        self.assertEqual(pipeline.prepare(self.root, other)["shortcut_name"], "Renamed Source")

    def test_name_cli_and_installed_name_mismatch_feedback(self):
        prepared = self.cli("prepare", str(self.source), "--shortcut-name", "TEST - Hello World")
        build_id = prepared["request"]["build_id"]
        self.assertIn("TEST - Hello World", prepared["ipad_instruction"])
        wrong = self.cli("record", build_id, "--status", "output-unverified", "--installed-name", "source")
        self.assertEqual(wrong["summary"]["installed_shortcut_name"], "source")
        self.assertFalse(wrong["summary"]["name_matches"])
        corrected = self.cli("record", build_id, "--status", "output-unverified", "--installed-name", "TEST - Hello World")
        self.assertTrue(corrected["summary"]["name_matches"])
        self.assertEqual(corrected["summary"]["accepted_observations"], 2)
        self.assertEqual(self.cli("prepare", str(self.source))["request"]["shortcut_name"], "TEST - Hello World")

    def test_invalid_names_and_unobserved_installed_name_are_rejected(self):
        for name in ("", " ", "Name\nInjected", " name", "name ", 42):
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.prepare(name=name)
        self.assertFalse(self.root.exists())
        request = self.prepare()
        self.cli("record", request["build_id"], "--status", "not-attempted", "--installed-name", "source", expected=1)
        feedback = pipeline.result_template(request)
        feedback["installed_shortcut_name"] = "source"
        with self.assertRaisesRegex(ValueError, "installed name"):
            pipeline.validate_result(feedback, request)

    def test_legacy_requests_results_and_receipts_remain_readable(self):
        request = self.prepare()
        folder = self.root / "requests" / request["build_id"]
        legacy = dict(request)
        legacy["schema_version"] = 1
        del legacy["shortcut_name"], legacy["name_from_build_id"]
        template = pipeline.result_template(legacy)
        template["schema_version"] = 1
        del template["installed_shortcut_name"]
        raw_template = pipeline.json_bytes(template)
        (folder / "feedback-template.json").write_bytes(raw_template)
        legacy["artifacts"]["feedback-template.json"] = pipeline.digest(raw_template)
        (folder / "request.json").write_bytes(pipeline.json_bytes(legacy))
        before = {p.name: p.read_bytes() for p in folder.iterdir()}
        pipeline.save_result(self.root, legacy, template, "ingest")
        status = self.cli("status", legacy["build_id"])
        self.assertIsNone(status["summary"]["shortcut_name"])
        self.assertIsNone(status["summary"]["installed_shortcut_name"])
        self.cli("record", legacy["build_id"], "--status", "output-unverified", "--installed-name", "source")
        self.assertTrue(self.cli("verify")["consistent"])
        self.assertEqual(before, {p.name: p.read_bytes() for p in folder.iterdir()})
        with self.assertRaisesRegex(ValueError, "Legacy request"):
            self.prepare(name_from_build=legacy["build_id"])

    def test_existing_g1a_variants_remain_distinct_and_unchanged(self):
        jelly = SCRIPT.parents[1] / "tests/ipad-investigation/g1a-presence.jelly"
        text = jelly.with_suffix(".txt")
        before = {p: p.read_bytes() for p in (jelly, text)}
        one = pipeline.prepare(self.root, jelly)
        two = pipeline.prepare(self.root, text, allow_text=True)
        self.assertNotEqual(one["source"]["sha256"], two["source"]["sha256"])
        self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_integration_plan_hashes_match_exact_fixtures(self):
        plan = Path(__file__).with_name("README.md").read_text(encoding="utf-8")
        matched = 0
        for line in plan.splitlines():
            cells = [cell.strip() for cell in line.split("|")]
            if len(cells) == 5 and cells[2].startswith("tests/") and cells[3].startswith("`"):
                source = SCRIPT.parents[1] / cells[2]
                self.assertEqual(pipeline.digest(source.read_bytes()), cells[3].strip("`"), str(source))
                matched += 1
        self.assertEqual(matched, 5)

    def test_missing_source(self):
        self.source.unlink()
        self.assertIn("source", self.cli("prepare", str(self.source), expected=1).lower())
        self.assertFalse(self.root.exists())

    def test_bad_encoding_empty_nul_and_wrong_extension(self):
        for data in (b"\xff\xfe", b" \r\n", b"import\x00Shortcuts"):
            with self.subTest(data=data):
                self.source.write_bytes(data)
                self.cli("prepare", str(self.source), expected=1)
                self.assertFalse(self.root.exists())
        self.source.write_bytes(self.data)
        other = self.source.with_suffix(".txt")
        other.write_bytes(self.data)
        self.cli("prepare", str(other), expected=1)
        self.cli("prepare", str(other), "--allow-text-source")

    def test_unavailable_exchange(self):
        self.root.write_text("This is a file, not a directory")
        self.cli("prepare", str(self.source), expected=1)
        self.cli("list", expected=1)

    def test_permission_failure_does_not_publish_a_request(self):
        with patch.object(pipeline, "publish", side_effect=PermissionError("Access denied")):
            self.assertIn("Access denied", self.cli("prepare", str(self.source), expected=1))
        self.assertFalse((self.root / "requests").exists())

    def test_transient_windows_publication_lock_is_retried(self):
        rename = Path.rename
        locked = PermissionError("Temporary sharing violation")
        locked.winerror = 32
        attempts = []
        def transient(path, destination):
            attempts.append(path)
            if len(attempts) == 1:
                raise locked
            return rename(path, destination)
        with patch.object(Path, "rename", autospec=True, side_effect=transient), patch.object(pipeline.time, "sleep"):
            self.prepare()
        self.assertEqual(len(attempts), 2)
        self.assertTrue(self.cli("verify")["consistent"])

    def test_persistent_publication_lock_is_reported_not_ready(self):
        locked = PermissionError("Persistent sharing violation")
        locked.winerror = 5
        with patch.object(Path, "rename", side_effect=locked) as rename, patch.object(pipeline.time, "sleep"):
            self.cli("prepare", str(self.source), expected=1)
        self.assertEqual(rename.call_count, 5)
        folders = list((self.root / "requests").iterdir())
        self.assertEqual(len(folders), 1)
        self.assertTrue(folders[0].name.startswith(".pending-"))
        self.cli("verify", expected=1)

    def test_read_commands_do_not_create_an_exchange(self):
        for command in ("list", "verify"):
            self.cli(command, expected=1)
            self.assertFalse(self.root.exists())

    def test_no_compilation_is_implied_by_prepare_or_result_directory(self):
        request = self.prepare()
        (self.root / "results" / request["build_id"]).mkdir(parents=True)
        status = self.cli("status", request["build_id"])["summary"]
        self.assertEqual(status["ipad_status"], "not-attempted")
        self.assertEqual(status["accepted_observations"], 0)

    def test_manual_feedback_and_diagnostics_file(self):
        request = self.prepare()
        diagnostic = self.base / "diagnostics £.txt"
        diagnostic.write_bytes(b"\xef\xbb\xbfWarning: observed message\r\n")
        result = self.cli("record", request["build_id"], "--status", "output-unverified",
                          "--diagnostics-file", str(diagnostic), "--notes", "Human inspection pending")
        self.assertEqual(result["result"]["compiler_messages"], "Warning: observed message\r\n")
        self.assertEqual(result["summary"]["ipad_status"], "output-unverified")
        self.assertFalse(result["result"]["device_tested"])
        self.assertTrue(self.cli("verify")["consistent"])

    def test_append_only_corrected_observations_and_repaired_scope(self):
        request = self.prepare()
        first = self.cli("record", request["build_id"], "--status", "compilation-failed", "--error-text", "Scope error")
        receipt_path = self.root / "results" / request["build_id"] / "observations" / first["receipt"]["observation_id"] / "result.json"
        before = receipt_path.read_bytes()
        self.cli("record", request["build_id"], "--status", "device-passed", "--repairs-required", "yes")
        status = self.cli("status", request["build_id"])
        self.assertEqual(len(status["observations"]), 2)
        self.assertEqual(status["summary"]["validation_scope"], "repaired")
        self.assertEqual(receipt_path.read_bytes(), before)

    def test_simulated_evidence_is_visible(self):
        request = self.prepare()
        self.cli("record", request["build_id"], "--status", "device-passed", "--repairs-required", "no", "--evidence", "simulated", "--installed-name", "Simulated name")
        status = self.cli("list")["requests"][0]
        self.assertEqual(status["latest_evidence_source"], "simulated")
        self.assertEqual(status["latest_observation_status"], "device-passed")
        self.assertEqual(status["ipad_status"], "not-attempted")
        self.assertIsNone(status["installed_shortcut_name"])
        self.assertIsNone(status["name_matches"])

    def test_valid_incoming_requires_explicit_ingest(self):
        request = self.prepare()
        folder = self.root / "results" / request["build_id"]
        folder.mkdir(parents=True)
        feedback = pipeline.result_template(request)
        feedback.update(status="output-unverified", compilation_attempted=True, shortcut_generated=True)
        (folder / "result.json").write_bytes(pipeline.json_bytes(feedback))
        before = self.cli("status", request["build_id"])["summary"]
        self.assertEqual(before["ipad_status"], "not-attempted")
        self.assertEqual(before["incoming_result"], "valid-uningested")
        self.cli("ingest", request["build_id"])
        after = self.cli("status", request["build_id"])["summary"]
        self.assertEqual(after["ipad_status"], "output-unverified")
        self.assertEqual(after["incoming_result"], "already-ingested")

    def test_ingest_rejects_mismatched_ids_and_both_hashes(self):
        request = self.prepare()
        incoming = self.base / "result.json"
        for field, value in (("build_id", pipeline.identifier()), ("source_sha256", "0" * 64), ("delivered_sha256", "0" * 64)):
            with self.subTest(field=field):
                feedback = pipeline.result_template(request)
                feedback[field] = value
                incoming.write_bytes(pipeline.json_bytes(feedback))
                self.cli("ingest", request["build_id"], str(incoming), expected=1)
                self.assertFalse((self.root / "results").exists())

    def test_missing_malformed_duplicate_and_nonfinite_results(self):
        request = self.prepare()
        incoming = self.base / "result.json"
        self.cli("ingest", request["build_id"], str(incoming), expected=1)
        for content in (b"{", b"[]", b'{"build_id": "a", "build_id": "b"}', b'{"value": NaN}', b'"filename.txt"'):
            with self.subTest(content=content):
                incoming.write_bytes(content)
                self.cli("ingest", request["build_id"], str(incoming), expected=1)
        self.assertFalse((self.root / "results").exists())

    def test_result_schema_and_semantic_contradictions(self):
        request = self.prepare()
        base = pipeline.result_template(request)
        mutations = [
            {"schema_version": 3}, {"schema_version": True}, {"unknown": "value"},
            {"compilation_attempted": "false"}, {"reported_at_utc": "yesterday"},
            {"status": "success"}, {"shortcut_generated": True},
            {"compilation_attempted": True, "status": "output-unverified", "shortcut_generated": True, "actions_inspected": True, "action_sequence_correct": False},
            {"compilation_attempted": True, "status": "device-passed", "shortcut_generated": True, "device_tested": True, "execution_outcome": "passed"},
            {"status": "compilation-failed", "compilation_attempted": True, "error_reported": False},
            {"status": "actions-correct", "compilation_attempted": True, "shortcut_generated": True, "actions_inspected": True, "action_sequence_correct": True, "error_reported": False},
        ]
        for mutation in mutations:
            with self.subTest(mutation=mutation), self.assertRaises((ValueError, TypeError)):
                pipeline.validate_result(dict(base, **mutation), request)

    def test_incomplete_generation_cannot_be_device_pass(self):
        request = self.prepare()
        result = self.cli("record", request["build_id"], "--status", "inconclusive", "--generated", "yes",
                          "--actions-inspected", "--actions-correct", "no", "--error-reported", "no",
                          "--notes", "Only Set Variable; Nothing and Quick Look absent")
        self.assertEqual(result["summary"]["ipad_status"], "inconclusive")
        self.cli("record", request["build_id"], "--status", "device-passed", "--repairs-required", "no",
                 "--actions-correct", "no", expected=1)

    def test_all_statuses_have_distinct_valid_representations(self):
        request = self.prepare()
        for status in pipeline.STATUSES:
            with self.subTest(status=status):
                extra = ["--repairs-required", "no"] if status in ("actions-correct", "device-passed") else []
                result = self.cli("record", request["build_id"], "--status", status, *extra)
                self.assertEqual(result["summary"]["ipad_status"], status)

    def test_local_failure_does_not_block_submission(self):
        report = self.base / "local.build.json"
        report.write_bytes(pipeline.json_bytes({"source_sha256": pipeline.digest(self.data), "success": False,
                                              "stage": "failed", "diagnostics": [{"message": "Known mismatch"}]}))
        request = self.prepare(local_report=report)
        self.assertFalse(request["local_validation"]["success"])
        self.assertEqual(self.cli("status", request["build_id"])["summary"]["ipad_status"], "not-attempted")
        report.write_bytes(pipeline.json_bytes({"source_sha256": "0" * 64, "success": True, "stage": "exported-unsigned"}))
        with self.assertRaisesRegex(ValueError, "source hash"):
            self.prepare(local_report=report)

    def test_source_tampering_and_missing_artifact_are_detected(self):
        request = self.prepare()
        source = self.root / "requests" / request["build_id"] / "source.txt"
        source.write_bytes(b"wrong source")
        self.cli("verify", expected=1)
        self.cli("record", request["build_id"], "--status", "not-attempted", expected=1)
        source.unlink()
        self.cli("verify", expected=1)

    def test_observation_tampering_detected(self):
        request = self.prepare()
        saved = self.cli("record", request["build_id"], "--status", "output-unverified")
        folder = self.root / "results" / request["build_id"] / "observations" / saved["receipt"]["observation_id"]
        (folder / "diagnostics.txt").write_text("tampered")
        self.cli("verify", expected=1)
        self.cli("record", request["build_id"], "--status", "not-attempted", expected=1)

    def test_manifest_change_after_observation_detected(self):
        request = self.prepare()
        self.cli("record", request["build_id"], "--status", "not-attempted")
        path = self.root / "requests" / request["build_id"] / "request.json"
        data = json.loads(path.read_bytes())
        data["source"]["original_path"] = "changed"
        path.write_bytes(pipeline.json_bytes(data))
        self.assertIn("changed after feedback", str(self.cli("verify", expected=1)))

    def test_pending_orphan_and_invalid_incoming_results(self):
        request = self.prepare()
        (self.root / "requests/.pending-interrupted").mkdir()
        self.cli("verify", expected=1)
        (self.root / "requests/.pending-interrupted").rmdir()
        folder = self.root / "results" / request["build_id"]
        folder.mkdir(parents=True)
        (folder / "result.json").write_text("{")
        self.cli("verify", expected=1)
        self.cli("record", request["build_id"], "--status", "not-attempted", expected=1)
        self.assertFalse((folder / "observations").exists())
        (folder / "result.json").unlink()
        (self.root / "results" / pipeline.identifier()).mkdir()
        self.cli("verify", expected=1)

    def test_refuses_overwrite_and_path_traversal(self):
        request = self.prepare()
        before = (self.root / "requests" / request["build_id"] / "request.json").read_bytes()
        with self.assertRaisesRegex(ValueError, "overwrite"):
            pipeline.publish(self.root / "requests", request["build_id"], {"request.json": b"bad"})
        self.assertEqual((self.root / "requests" / request["build_id"] / "request.json").read_bytes(), before)
        for value in ("../outside", "..\\outside", "C:\\outside", "x/y"):
            self.cli("status", value, expected=1)

    def test_symlink_escape_is_rejected_when_supported(self):
        request = self.prepare()
        original = self.root / "requests" / request["build_id"] / "source.txt"
        original.unlink()
        try:
            original.symlink_to(self.source)
        except OSError:
            self.skipTest("Host does not permit symlink creation")
        self.cli("verify", expected=1)

    def test_environment_configuration_and_subprocess_cli(self):
        environment = dict(pipeline.os.environ, JELLY_EXCHANGE_ROOT=str(self.root))
        run = subprocess.run([sys.executable, "-B", str(SCRIPT), "prepare", str(self.source)],
                             capture_output=True, text=True, encoding="utf-8", env=environment)
        self.assertEqual(run.returncode, 0, run.stderr)
        output = json.loads(run.stdout)
        self.assertIn("CONTENTS", output["ipad_instruction"])
        self.assertEqual(Path(output["exchange_root"]), self.root)
        self.assertEqual(self.source.read_bytes(), self.data)


if __name__ == "__main__":
    unittest.main()
