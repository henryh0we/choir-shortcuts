#!/usr/bin/env python3
"""Prepare immutable source requests and collect evidence from manual iPad builds.

Standard library only. No network, device control, compiler invocation or signing.
See ../docs/ipad-pipeline.md and ../docs/ipad-pipeline-format.md.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
METHODS = ("editor", "compile-jelly-text", "compile-jelly-file")
STATUSES = ("not-attempted", "compilation-attempted", "compilation-failed",
            "output-unverified", "actions-correct", "device-passed",
            "device-failed", "inconclusive")
EVIDENCE = ("manual", "device-reported", "simulated")
ID = re.compile(r"\d{8}T\d{12}Z-[0-9a-f]{32}\Z")
HASH = re.compile(r"[0-9a-f]{64}\Z")
REQUEST_FIELDS = {"schema_version", "build_id", "created_at_utc", "status", "target",
                  "requested_method", "source", "local_validation", "artifacts"}
RESULT_FIELDS = {"schema_version", "build_id", "source_sha256", "delivered_sha256",
                 "reported_at_utc", "compilation_method", "status", "evidence_source",
                 "compilation_attempted", "error_reported", "compiler_messages",
                 "shortcut_generated", "actions_inspected", "action_sequence_correct",
                 "manual_repairs_required", "device_tested", "execution_outcome",
                 "developer_notes", "device"}
NAMED_REQUEST_FIELDS = REQUEST_FIELDS | {"shortcut_name", "name_from_build_id"}
NAMED_RESULT_FIELDS = RESULT_FIELDS | {"installed_shortcut_name"}


class PipelineError(ValueError):
    """Invalid or inconsistent exchange evidence."""


def require(condition, message):
    if not condition:
        raise PipelineError(message)


def now():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def identifier():
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ-") + uuid.uuid4().hex


def digest(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def parse_json(data):
    require(len(data) <= 2_000_000, "JSON exceeds the 2 MB manifest/result limit")
    def invalid_constant(value):
        raise PipelineError(f"Invalid JSON constant: {value}")
    return json.loads(data.decode("utf-8-sig"), object_pairs_hook=unique_object,
                      parse_constant=invalid_constant)


def fields(value, expected, label):
    require(isinstance(value, dict), f"{label} must be an object")
    require(set(value) == expected,
            f"{label} fields: missing {sorted(expected - set(value))}; unknown {sorted(set(value) - expected)}")


def timestamp(value):
    require(isinstance(value, str) and value.endswith("Z"), "Timestamp must be UTC with a Z suffix")
    datetime.fromisoformat(value.replace("Z", "+00:00"))


def safe_path(root, *parts):
    path = root.joinpath(*parts)
    require(path.resolve().is_relative_to(root), f"Path escapes exchange directory: {path}")
    require(not path.is_symlink(), f"Symlinks are not exchange artifacts: {path}")
    return path


def valid_id(value):
    require(isinstance(value, str) and ID.fullmatch(value), "Invalid build/observation ID")
    return value


def source_text(data):
    text = data.decode("utf-8-sig", errors="strict")
    require(text.strip() and "\x00" not in text, "Source must be nonempty UTF-8 text without NUL characters")
    return text


def shortcut_name(value):
    require(isinstance(value, str) and value.strip() and value == value.strip() and value.isprintable(),
            "Shortcut name must be nonempty printable text without surrounding whitespace")
    return value


def default_shortcut_name(filename):
    words = re.split(r"[-_\s]+", Path(filename).stem)
    role = words.pop(0).upper() if len(words) > 1 and words[0].lower() in ("util", "main", "test") else None
    acronyms = {"pdf", "url", "api", "id"}
    title = " ".join(word.upper() if word.lower() in acronyms else word.capitalize() if word.islower() else word
                     for word in words if word)
    return shortcut_name(f"{role} - {title}" if role else title)


def select_shortcut_name(root, source_path, explicit=None, from_build=None):
    require(not (explicit is not None and from_build is not None), "Use --shortcut-name OR --name-from-build")
    if explicit is not None:
        return shortcut_name(explicit), None
    if from_build is not None:
        previous = read_request(root, from_build)
        require("shortcut_name" in previous, "Legacy request has no intended name; specify --shortcut-name")
        return previous["shortcut_name"], previous["build_id"]
    requests = safe_path(root, "requests")
    if requests.exists():
        for folder in sorted(requests.iterdir(), reverse=True):
            if ID.fullmatch(folder.name):
                previous = read_request(root, folder.name)
                if "shortcut_name" in previous and os.path.normcase(previous["source"]["original_path"]) == os.path.normcase(str(source_path)):
                    return previous["shortcut_name"], previous["build_id"]
    return default_shortcut_name(source_path.name), None


def publish(parent, name, files):
    """Publish a complete bundle by rename; never update an existing bundle.

    Failed writes leave a .pending-* directory for diagnosis, never a ready request.
    No recursive deletion is needed. Sync clients may still deliver files in any order.
    """
    parent.mkdir(parents=True, exist_ok=True)
    destination = parent / name
    require(not destination.exists(), f"Refusing to overwrite immutable bundle: {destination}")
    staging = parent / (".pending-" + uuid.uuid4().hex)
    staging.mkdir()
    for filename, content in files.items():
        with (staging / filename).open("xb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
    # Windows sync/indexing/antivirus handles can briefly deny directory renames.
    # Retry only known sharing/access-denied errors; permanent failure stays visible.
    for attempt in range(5):
        require(not destination.exists(), f"Bundle appeared during publication: {destination}")
        try:
            staging.rename(destination)
            break
        except PermissionError as error:
            if getattr(error, "winerror", None) not in (5, 32) or attempt == 4:
                raise
            time.sleep(0.05 * (2 ** attempt))
    return destination


def result_template(request):
    return {"schema_version": 2, "build_id": request["build_id"],
            "source_sha256": request["source"]["sha256"],
            "delivered_sha256": request["source"]["delivered_sha256"],
            "reported_at_utc": request["created_at_utc"],
            "compilation_method": request["requested_method"], "status": "not-attempted",
            "evidence_source": "manual", "compilation_attempted": False,
            "error_reported": None, "compiler_messages": "", "shortcut_generated": None,
            "actions_inspected": False, "action_sequence_correct": None,
            "manual_repairs_required": None, "device_tested": False,
            "execution_outcome": "not-run", "developer_notes": "",
            "device": {"ipados_version": "", "jellycuts_version": "", "forscore_version": ""},
            "installed_shortcut_name": None}


def validate_result(result, request):
    require(isinstance(result, dict), "result must be an object")
    version = result.get("schema_version")
    require(type(version) is int and version in (1, 2), "Unsupported result schema_version")
    fields(result, NAMED_RESULT_FIELDS if version == 2 else RESULT_FIELDS, "result")
    require(result["build_id"] == request["build_id"], "Result build ID does not match request")
    for key, expected in (("source_sha256", request["source"]["sha256"]),
                          ("delivered_sha256", request["source"]["delivered_sha256"])):
        require(result[key] == expected, f"Result {key} does not match request")
    timestamp(result["reported_at_utc"])
    require(result["compilation_method"] in METHODS, "Unknown compilation method")
    require(result["status"] in STATUSES, "Unknown result status")
    require(result["evidence_source"] in EVIDENCE, "Unknown evidence source")
    for key in ("compilation_attempted", "actions_inspected", "device_tested"):
        require(type(result[key]) is bool, f"{key} must be a Boolean")
    for key in ("error_reported", "shortcut_generated", "action_sequence_correct", "manual_repairs_required"):
        require(result[key] is None or type(result[key]) is bool, f"{key} must be Boolean or null")
    for key in ("compiler_messages", "developer_notes"):
        require(isinstance(result[key], str), f"{key} must be text")
    fields(result["device"], {"ipados_version", "jellycuts_version", "forscore_version"}, "device")
    require(all(isinstance(v, str) for v in result["device"].values()), "Device versions must be text")
    require(result["execution_outcome"] in ("not-run", "passed", "failed", "inconclusive"), "Unknown execution outcome")
    attempted, generated = result["compilation_attempted"], result["shortcut_generated"]
    if version == 2 and result["installed_shortcut_name"] is not None:
        shortcut_name(result["installed_shortcut_name"])
        require(attempted and generated is True, "An installed name requires attempted compilation and a generated shortcut")
    inspected, correct = result["actions_inspected"], result["action_sequence_correct"]
    tested, outcome, status = result["device_tested"], result["execution_outcome"], result["status"]
    require(not inspected or generated is True, "Action inspection requires a generated shortcut")
    require(correct is None or inspected, "Action correctness requires inspection")
    require(result["manual_repairs_required"] is None or inspected, "Repair assessment requires action inspection")
    require(not tested or generated is True, "Device execution requires a generated shortcut")
    require(tested == (outcome != "not-run"), "device_tested and execution_outcome disagree")
    if not attempted:
        require(generated is None and not inspected and not tested and result["error_reported"] is None,
                "Unattempted compilation cannot claim generation, errors, inspection or execution")
    if status == "not-attempted":
        require(not attempted, "not-attempted status contradicts compilation_attempted")
    elif status != "inconclusive":
        require(attempted, f"{status} requires an attempted compilation")
    if status == "compilation-attempted":
        require(generated is None and not inspected and not tested and result["error_reported"] is None,
                "Use a more specific status when an outcome is known")
    if status == "compilation-failed":
        require(result["error_reported"] is True and not tested, "Compilation failure requires a reported error and no device run")
        require(correct is not True, "Failed compilation cannot claim correct generation")
    if status == "output-unverified":
        require(generated is True and not inspected and not tested and result["error_reported"] is not True,
                "output-unverified requires generation without inspection, device run or reported error")
    if status in ("actions-correct", "device-passed"):
        require(generated is True and inspected and correct is True and result["error_reported"] is False,
                "A correct-output status requires inspected correct actions and no reported compiler error")
        require(result["manual_repairs_required"] is not None, "State explicitly whether native repairs were required")
    if status == "actions-correct":
        require(not tested, "Use a device outcome status after execution")
    if status in ("device-passed", "device-failed"):
        require(tested and outcome == ("passed" if status == "device-passed" else "failed"),
                "Device status contradicts execution outcome")
    if tested:
        require(status in ("device-passed", "device-failed", "inconclusive"), "Device execution needs a device/inconclusive status")
    return result


def validate_local_report(data, source_hash):
    report = parse_json(data)
    require(isinstance(report, dict) and report.get("source_sha256") == source_hash,
            "Local report source hash does not match submitted source")
    require(type(report.get("success")) is bool and isinstance(report.get("stage"), str),
            "Local report needs Boolean success and text stage fields")
    return report


def read_request(root, build_id):
    folder = safe_path(root, "requests", valid_id(build_id))
    request = parse_json(safe_path(folder, "request.json").read_bytes())
    require(isinstance(request, dict), "request must be an object")
    version = request.get("schema_version")
    require(type(version) is int and version in (1, 2, 3), "Unsupported request schema_version")
    fields(request, NAMED_REQUEST_FIELDS if version >= 2 else REQUEST_FIELDS, "request")
    if version >= 2:
        shortcut_name(request["shortcut_name"])
        if request["name_from_build_id"] is not None:
            valid_id(request["name_from_build_id"])
            require(request["name_from_build_id"] != build_id, "Name inheritance cannot refer to the same request")
    require(request["build_id"] == build_id, "Request directory and build ID disagree")
    require(request["status"] == "prepared" and request["target"] == "ipad-jellycuts", "Invalid request status/target")
    require(request["requested_method"] in METHODS, "Unknown requested method")
    timestamp(request["created_at_utc"])
    source = request["source"]
    fields(source, {"filename", "original_path", "sha256", "delivered_sha256", "bytes", "encoding", "transformation"}, "source")
    require(all(isinstance(source[k], str) and source[k] for k in ("filename", "original_path")), "Missing source path/name")
    require(all(isinstance(source[k], str) and HASH.fullmatch(source[k]) for k in ("sha256", "delivered_sha256")), "Invalid source hash")
    require(source["sha256"] == source["delivered_sha256"] and source["transformation"] == "none",
            "Source delivery must be byte-exact without transformation")
    require(type(source["bytes"]) is int and source["bytes"] > 0, "Invalid source size")
    artifacts = request["artifacts"]
    require(isinstance(artifacts, dict), "artifacts must be an object")
    local = request["local_validation"]
    fields(local, {"status", "success", "stage"}, "local_validation")
    require(local["status"] in ("not-provided", "captured"), "Invalid local-validation status")
    expected = {"source.jelly", "feedback-template.json"}
    if version < 3:
        expected.add("source.txt")
    if local["status"] == "captured":
        expected.add("local-validation.json")
    else:
        require(local["success"] is None and local["stage"] is None, "Unprovided local checks cannot claim results")
    require(set(artifacts) == expected, "Unexpected/missing request artifacts")
    content = {}
    for name, sha in artifacts.items():
        require(isinstance(sha, str) and HASH.fullmatch(sha), "Invalid artifact hash")
        content[name] = safe_path(folder, name).read_bytes()
        require(digest(content[name]) == sha, f"Request artifact hash mismatch: {name}")
    data = content["source.jelly"]
    text = source_text(data)
    require(len(data) == source["bytes"] and digest(data) == source["sha256"], "Source snapshot/hash/size disagree")
    if version < 3:
        require(data == content["source.txt"], "Legacy source snapshots disagree")
    encoding = "utf-8-bom" if data.startswith(b"\xef\xbb\xbf") else "utf-8"
    require(source["encoding"] == encoding, "Source encoding declaration disagrees")
    require(text, "Empty source")
    validate_result(parse_json(content["feedback-template.json"]), request)
    if local["status"] == "captured":
        report = validate_local_report(content["local-validation.json"], source["sha256"])
        require(type(local["success"]) is bool and local["success"] == report["success"] and local["stage"] == report["stage"], "Local report summary disagrees")
    return request


def prepare(root, source_path, method="editor", local_report=None,
            name=None, name_from_build=None):
    source_path = Path(source_path).expanduser().resolve(strict=True)
    require(source_path.is_file(), "Source is not a file")
    require(source_path.suffix.lower() == ".jelly", "Choose a .jelly source")
    data = source_path.read_bytes()
    source_text(data)
    sha = digest(data)
    intended_name, inherited_from = select_shortcut_name(root, source_path, name, name_from_build)
    request = {"schema_version": 3, "build_id": identifier(), "created_at_utc": now(),
               "shortcut_name": intended_name, "name_from_build_id": inherited_from,
               "status": "prepared", "target": "ipad-jellycuts", "requested_method": method,
               "source": {"filename": source_path.name, "original_path": str(source_path),
                          "sha256": sha, "delivered_sha256": sha, "bytes": len(data),
                          "encoding": "utf-8-bom" if data.startswith(b"\xef\xbb\xbf") else "utf-8",
                          "transformation": "none"},
               "local_validation": {"status": "not-provided", "success": None, "stage": None}}
    files = {"source.jelly": data,
             "feedback-template.json": json_bytes(result_template(request))}
    if local_report:
        raw = Path(local_report).read_bytes()
        report = validate_local_report(raw, sha)
        files["local-validation.json"] = raw
        request["local_validation"] = {"status": "captured", "success": report["success"], "stage": report["stage"]}
    request["artifacts"] = {name: digest(content) for name, content in files.items()}
    files["request.json"] = json_bytes(request)
    root.mkdir(parents=True, exist_ok=True)
    publish(safe_path(root, "requests"), request["build_id"], files)
    return read_request(root, request["build_id"])


def save_result(root, request, result, origin):
    validate_result(result, request)
    raw, diagnostics = json_bytes(result), result["compiler_messages"].encode("utf-8")
    receipt = {"schema_version": 1, "observation_id": identifier(), "build_id": request["build_id"],
               "received_at_utc": now(), "origin": origin,
               "request_sha256": digest(safe_path(root, "requests", request["build_id"], "request.json").read_bytes()),
               "result_sha256": digest(raw), "diagnostics_sha256": digest(diagnostics)}
    parent = safe_path(root, "results", request["build_id"], "observations")
    publish(parent, receipt["observation_id"], {"result.json": raw, "diagnostics.txt": diagnostics,
                                              "receipt.json": json_bytes(receipt)})
    return receipt


def observations(root, request):
    parent = safe_path(root, "results", request["build_id"], "observations")
    result = []
    if not parent.exists():
        return result
    for folder in sorted(parent.iterdir()):
        if folder.name.startswith(".pending-"):
            raise PipelineError(f"Incomplete observation publication: {folder}")
        valid_id(folder.name)
        safe_path(parent, folder.name)
        receipt = parse_json(safe_path(folder, "receipt.json").read_bytes())
        fields(receipt, {"schema_version", "observation_id", "build_id", "received_at_utc", "origin", "request_sha256", "result_sha256", "diagnostics_sha256"}, "receipt")
        require(type(receipt["schema_version"]) is int and receipt["schema_version"] == 1, "Unsupported receipt schema")
        require(receipt["observation_id"] == folder.name and receipt["build_id"] == request["build_id"], "Receipt identity mismatch")
        require(receipt["origin"] in ("record", "ingest"), "Unknown receipt origin")
        timestamp(receipt["received_at_utc"])
        expected_request = digest(safe_path(root, "requests", request["build_id"], "request.json").read_bytes())
        require(receipt["request_sha256"] == expected_request, "Request manifest changed after feedback was accepted")
        raw = safe_path(folder, "result.json").read_bytes()
        diagnostics = safe_path(folder, "diagnostics.txt").read_bytes()
        require(digest(raw) == receipt["result_sha256"] and digest(diagnostics) == receipt["diagnostics_sha256"], "Stored observation hash mismatch")
        feedback = validate_result(parse_json(raw), request)
        require(diagnostics == feedback["compiler_messages"].encode("utf-8"), "Diagnostics and result messages disagree")
        result.append({"receipt": receipt, "result": feedback})
    return result


def summary(root, request):
    history = observations(root, request)
    incoming = safe_path(root, "results", request["build_id"], "result.json")
    incoming_state = "absent"
    if incoming.exists():
        feedback = validate_result(parse_json(incoming.read_bytes()), request)
        incoming_state = "already-ingested" if any(item["result"] == feedback for item in history) else "valid-uningested"
    latest = history[-1]["result"] if history else None
    actual = [item["result"] for item in history if item["result"]["evidence_source"] != "simulated"]
    device_evidence = actual[-1] if actual else None
    return {"build_id": request["build_id"], "source_filename": request["source"]["filename"],
            "shortcut_name": request.get("shortcut_name"),
            "installed_shortcut_name": device_evidence.get("installed_shortcut_name") if device_evidence else None,
            "name_matches": (device_evidence["installed_shortcut_name"] == request["shortcut_name"])
                if device_evidence and device_evidence.get("installed_shortcut_name") is not None and "shortcut_name" in request else None,
            "source_sha256": request["source"]["sha256"], "request_status": "prepared",
            "ipad_status": device_evidence["status"] if device_evidence else "not-attempted",
            "latest_observation_status": latest["status"] if latest else None,
            "latest_evidence_source": latest["evidence_source"] if latest else None,
            "validation_scope": ("repaired" if device_evidence["manual_repairs_required"] is True else
                                 "untouched" if device_evidence["manual_repairs_required"] is False else "unassessed") if device_evidence else "unassessed",
            "accepted_observations": len(history), "incoming_result": incoming_state,
            "local_validation": request["local_validation"]}


def tri(value):
    return {"yes": True, "no": False, "unknown": None}[value]


def manual_result(request, args):
    result = result_template(request)
    status = args.status
    result.update(status=status, reported_at_utc=now(), evidence_source=args.evidence,
                  compilation_method=args.method or request["requested_method"],
                  compilation_attempted=status != "not-attempted")
    if status == "compilation-failed":
        result["error_reported"] = True
    if status in ("output-unverified", "actions-correct", "device-passed", "device-failed"):
        result["shortcut_generated"] = True
    if status in ("actions-correct", "device-passed"):
        result.update(actions_inspected=True, action_sequence_correct=True, error_reported=False)
    if status in ("device-passed", "device-failed"):
        result.update(device_tested=True, execution_outcome="passed" if status == "device-passed" else "failed")
    for arg, field in (("attempted", "compilation_attempted"), ("error_reported", "error_reported"),
                       ("generated", "shortcut_generated"), ("actions_correct", "action_sequence_correct"),
                       ("repairs_required", "manual_repairs_required")):
        value = getattr(args, arg)
        if value is not None:
            result[field] = tri(value)
    if args.actions_inspected:
        result["actions_inspected"] = True
    result["compiler_messages"] = args.error_text or ""
    if args.diagnostics_file:
        text = Path(args.diagnostics_file).read_bytes().decode("utf-8-sig")
        result["compiler_messages"] += ("\n" if result["compiler_messages"] else "") + text
    result["developer_notes"] = args.notes
    result["installed_shortcut_name"] = args.installed_name
    result["device"] = {"ipados_version": args.ipados_version, "jellycuts_version": args.jellycuts_version,
                        "forscore_version": args.forscore_version}
    return result


def parser():
    cli = argparse.ArgumentParser(description=__doc__)
    commands = cli.add_subparsers(dest="command", required=True)
    for command, help_text in (("prepare", "Snapshot source; never compile or contact the device"),
                               ("list", "List validated requests and accepted evidence"),
                               ("status", "Inspect a request, incoming feedback and full history"),
                               ("ingest", "Validate/copy feedback into append-only evidence"),
                               ("record", "Record explicit human observations (not device automation)"),
                               ("verify", "Check all requests, source hashes and results without changing files")):
        sub = commands.add_parser(command, help=help_text)
        sub.add_argument("--exchange", type=Path, default=Path(os.environ.get("JELLY_EXCHANGE_ROOT", str(ROOT / "build/ipad-exchange"))),
                         help="Exchange root; default JELLY_EXCHANGE_ROOT or jelly/build/ipad-exchange")
        if command in ("status", "ingest", "record"):
            sub.add_argument("build_id")
        if command == "prepare":
            sub.add_argument("source", type=Path)
            sub.add_argument("--method", choices=METHODS, default="editor")
            sub.add_argument("--local-report", type=Path, help="Capture an existing matching build.py report, including failures")
            names = sub.add_mutually_exclusive_group()
            names.add_argument("--shortcut-name", help="Intended installed display name; otherwise inherit previous same-path build or derive from original filename")
            names.add_argument("--name-from-build", help="Reuse an existing request's name across a source-file rename/move")
        if command == "ingest":
            sub.add_argument("result", nargs="?", type=Path, help="Default: results/<build-id>/result.json")
        if command == "record":
            sub.add_argument("--status", required=True, choices=STATUSES)
            sub.add_argument("--method", choices=METHODS)
            sub.add_argument("--evidence", choices=EVIDENCE, default="manual")
            sub.add_argument("--attempted", choices=("yes", "no"))
            for option in ("error-reported", "generated", "actions-correct", "repairs-required"):
                sub.add_argument("--" + option, choices=("yes", "no", "unknown"))
            sub.add_argument("--actions-inspected", action="store_true")
            sub.add_argument("--error-text")
            sub.add_argument("--diagnostics-file", type=Path, help="UTF-8 diagnostic text (optional BOM)")
            sub.add_argument("--notes", default="")
            sub.add_argument("--installed-name", help="Actual observed installed name; omit if unknown (never inferred from intended name)")
            for option in ("ipados-version", "jellycuts-version", "forscore-version"):
                sub.add_argument("--" + option, default="")
    return cli


def execute(args):
    root = args.exchange.expanduser().resolve()
    if args.command == "prepare":
        request = prepare(root, args.source, args.method, args.local_report,
                          args.shortcut_name, args.name_from_build)
        return {"request": request, "exchange_root": str(root),
                "ipad_instruction": f"In Files open requests/{request['build_id']}/source.jelly; preview its CONTENTS, then use the documented {args.method} path. Intended shortcut name: {request['shortcut_name']}. Use this in the compiler name field when available; otherwise rename the newly generated test shortcut after installation. Check existing names/callers first. No iPad compilation has occurred."}
    require(root.is_dir(), f"Exchange directory unavailable: {root}. Prepare creates it; list/status/verify never create it.")
    if args.command in ("list", "verify"):
        requests_dir = safe_path(root, "requests")
        require(requests_dir.is_dir(), "Missing requests directory")
        entries, errors, known = [], [], set()
        for folder in sorted(requests_dir.iterdir()):
            try:
                request = read_request(root, folder.name)
                known.add(folder.name)
                entries.append(summary(root, request))
            except (OSError, ValueError, TypeError, KeyError, RecursionError) as error:
                errors.append({"path": str(folder), "error": str(error)})
        results_dir = safe_path(root, "results")
        if results_dir.exists():
            for folder in results_dir.iterdir():
                if folder.name not in known:
                    errors.append({"path": str(folder), "error": "Result directory has no valid matching request"})
        return {"exchange_root": str(root), "requests": entries, "errors": errors,
                "consistent": not errors}
    request = read_request(root, args.build_id)
    if args.command == "status":
        return {"summary": summary(root, request), "request": request,
                "observations": observations(root, request)}
    # Check all existing evidence before appending; never obscure corruption.
    summary(root, request)
    if args.command == "record":
        result = manual_result(request, args)
    else:
        incoming = args.result or safe_path(root, "results", args.build_id, "result.json")
        result = parse_json(incoming.read_bytes())
    receipt = save_result(root, request, result, args.command)
    return {"receipt": receipt, "result": result, "summary": summary(root, request)}


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        output = execute(args)
        print(json_bytes(output).decode("utf-8"), end="")
        return 1 if output.get("consistent") is False else 0
    except (OSError, ValueError, TypeError, KeyError, RecursionError) as error:
        print(f"ipad-pipeline: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main())
