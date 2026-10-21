#!/usr/bin/env python3
"""Compile Jelly with the pinned WSL/Linux CLI; never sign or upload exports."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import plistlib
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from xml.parsers.expat import ExpatError

ROOT = Path(__file__).resolve().parents[1]
REVISION = "e1ec31c2ee192c8721749f9eb3b50108e38891cf"
SUCCESS = "Successfully Compiled Shortcut"
SYNTAX = re.compile(r"^SYNTAX ERROR, line: (\d+),\s*(.*)$")


def run(command, timeout=120):
    return subprocess.run(command, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=timeout)


def linux_path(path, distro):
    if os.name != "nt":
        return str(path)
    result = run(["wsl.exe", "-d", distro, "--exec", "wslpath", "-a", "-u", str(path)])
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "WSL path conversion failed")
    return result.stdout.strip()


def compiler_command(source, candidate, distro):
    arguments = [linux_path(source, distro), "--export", "--out", linux_path(candidate, distro)]
    if os.name == "nt":
        # Source and export paths are positional arguments, never shell source.
        return ["wsl.exe", "-d", distro, "--exec", "bash", "-lc",
                'exec "$HOME/.local/bin/jelly" "$@"', "jelly", *arguments]
    return [str(Path.home() / ".local/bin/jelly"), *arguments]


def validate_export(path):
    """Check plist/actions and known token defects, without claiming iOS validation."""
    with path.open("rb") as handle:
        document = plistlib.load(handle)
    if not isinstance(document, dict) or not isinstance(document.get("WFWorkflowActions"), list):
        raise ValueError("Export is missing the WFWorkflowActions array")
    actions = document["WFWorkflowActions"]
    if not actions:
        raise ValueError("Export contains no actions")
    uuids = set()
    for action in actions:
        if not isinstance(action, dict) or not isinstance(action.get("WFWorkflowActionIdentifier"), str):
            raise ValueError("Invalid action identifier")
        parameters = action.get("WFWorkflowActionParameters")
        if not isinstance(parameters, dict):
            raise ValueError("Invalid action parameters")
        if isinstance(parameters.get("UUID"), str):
            uuids.add(parameters["UUID"])

    def inspect(value):
        if isinstance(value, dict):
            if value.get("Type") == "ActionOutput" and value.get("OutputUUID") not in uuids:
                raise ValueError("ActionOutput references a missing action UUID")
            if "attachmentsByRange" in value:
                text = value.get("string")
                attachments = value["attachmentsByRange"]
                if not isinstance(text, str) or not isinstance(attachments, dict):
                    raise ValueError("Invalid text token attachments")
                encoded = text.encode("utf-16-le")
                for key in attachments:
                    match = re.fullmatch(r"\{(\d+), (\d+)\}", key)
                    if not match:
                        raise ValueError(f"Invalid text attachment range {key}")
                    start, length = map(int, match.groups())
                    if length != 1 or (start + length) * 2 > len(encoded):
                        raise ValueError(f"Text attachment {key} is outside its UTF-16 string (known upstream interpolation defect)")
                    if encoded[start * 2:(start + 1) * 2] != b"\xfc\xff":
                        raise ValueError(f"Text attachment {key} does not point to an object replacement character")
            for child in value.values():
                inspect(child)
        elif isinstance(value, list):
            for child in value:
                inspect(child)
    inspect(document)
    return document


def emit(source, severity, message, line=None):
    # Only actual CLI syntax diagnostics supply a line. Other events are file-level.
    location = f"{source}:{line}" if line is not None else str(source)
    print(f"{location}: {severity}: {message}", flush=True)


def build(source, distro):
    source = source.resolve(strict=True)
    relative = source.relative_to(ROOT)
    if source.suffix.lower() != ".jelly" or relative.parts[0] in {"build", "vendor"}:
        raise ValueError("Choose a .jelly source inside jelly/, outside build/ and vendor/")
    destination = ROOT / "build" / relative.with_suffix(".shortcut")
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Remove previous output before trying: an old successful export must never imply a new pass.
    destination.unlink(missing_ok=True)
    rejected = destination.with_suffix(".rejected.plist")
    rejected.unlink(missing_ok=True)
    before = hashlib.sha256(source.read_bytes()).hexdigest()
    report = {"source": str(source), "source_sha256": before,
              "configured_compiler_revision": REVISION, "configured_swift_version": "6.4.1",
              "utc": datetime.now(timezone.utc).isoformat(), "success": False,
              "stage": "failed", "signed": False, "device_tested": False,
              "diagnostics": []}
    fd, temporary = tempfile.mkstemp(prefix=destination.stem + "-", suffix=".plist", dir=destination.parent)
    os.close(fd)
    candidate = Path(temporary)
    fd, temporary_source = tempfile.mkstemp(prefix=destination.stem + "-", suffix=".jelly", dir=destination.parent)
    os.close(fd)
    normalized_source = Path(temporary_source)
    stdout = stderr = ""
    failure = None
    try:
        # The pinned parser misreads source offsets after CRLF. Normalize a disposable
        # UTF-8 copy, preserving the user's bytes and diagnostic line numbers.
        text = source.read_text(encoding="utf-8-sig")
        normalized_source.write_text(text, encoding="utf-8", newline="\n")
        report["input_normalization"] = "UTF-8 without BOM; LF line endings; original source preserved"
        command = compiler_command(normalized_source, candidate, distro)
        report["command"] = command
        result = run(command)
        stdout, stderr = result.stdout, result.stderr
        report["compiler_exit_code"] = result.returncode
        raw = stdout + "\n" + stderr
        compiler_failed = result.returncode != 0 or re.search(r"^Found \d+ errors\s*$", raw, re.M) or SUCCESS not in stdout.splitlines()
        for entry in raw.splitlines():
            if not entry.strip() or entry == SUCCESS or re.fullmatch(r"Found \d+ errors", entry):
                continue
            match = SYNTAX.match(entry)
            severity = "error" if compiler_failed else "warning"
            diagnostic = {"severity": severity, "message": entry}
            if match:
                diagnostic["line"] = int(match[1])
                diagnostic["message"] = match[2]
            report["diagnostics"].append(diagnostic)
            emit(source, severity, diagnostic["message"], diagnostic.get("line"))
        if compiler_failed:
            failure = f"Jellycore failed validation (raw exit {result.returncode}); see captured logs"
        else:
            report["stage"] = "compiled"
            document = validate_export(candidate)
            if hashlib.sha256(source.read_bytes()).hexdigest() != before:
                raise ValueError("Source changed during compilation; rerun the build")
            candidate.replace(destination)
            report.update(success=True, stage="exported-unsigned", output=str(destination),
                          output_sha256=hashlib.sha256(destination.read_bytes()).hexdigest(),
                          action_count=len(document["WFWorkflowActions"]))
            print(f"Exported unsigned: {destination}", flush=True)
    except (OSError, RuntimeError, ValueError, ExpatError, plistlib.InvalidFileException, subprocess.TimeoutExpired) as error:
        failure = str(error)
        if isinstance(error, subprocess.TimeoutExpired):
            stdout = (error.stdout or b"").decode("utf-8", errors="replace") if isinstance(error.stdout, bytes) else error.stdout or ""
            stderr = (error.stderr or b"").decode("utf-8", errors="replace") if isinstance(error.stderr, bytes) else error.stderr or ""
        if candidate.exists() and candidate.stat().st_size:
            candidate.replace(rejected)
            report["rejected_export"] = str(rejected)
    finally:
        candidate.unlink(missing_ok=True)
        normalized_source.unlink(missing_ok=True)
    if failure:
        report["diagnostics"].append({"severity": "error", "message": failure})
        emit(source, "error", failure)
    destination.with_suffix(".stdout.log").write_text(stdout, encoding="utf-8")
    destination.with_suffix(".stderr.log").write_text(stderr, encoding="utf-8")
    destination.with_suffix(".build.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report["success"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", help=".jelly paths relative to the current directory")
    parser.add_argument("--all", action="store_true", help="compile all sources, examples and probes independently")
    parser.add_argument("--distro", default=os.environ.get("JELLY_WSL_DISTRO", "Ubuntu"))
    args = parser.parse_args()
    if args.all == bool(args.files):
        parser.error("Specify source files OR --all")
    files = sorted(p for folder in ("shortcuts", "examples", "tests") for p in (ROOT / folder).rglob("*.jelly")) if args.all else [Path(p) for p in args.files]
    if not files:
        parser.error("No .jelly sources found")
    succeeded = 0
    for source in files:
        try:
            succeeded += bool(build(source, args.distro))
        except (OSError, ValueError) as error:
            emit(source.absolute(), "error", str(error))
    print(f"{succeeded}/{len(files)} exports passed compiler and structural checks.")
    return 0 if succeeded == len(files) else 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main())
