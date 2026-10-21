#!/usr/bin/env python3
"""End-to-end checks using the real installed compiler, never a mock."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from build import ROOT, SYNTAX, validate_export


def main():
    results = []
    valid = (ROOT / "tests/compiler/hello-world.jelly").read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory(prefix="compiler validation ", dir=ROOT / "tests/compiler") as temporary:
        # Spaces, Unicode, apostrophes, $, and ; must remain ordinary path characters.
        source = Path(temporary) / "Henry's £ test $ ;.jelly"
        output = ROOT / "build" / source.relative_to(ROOT).with_suffix(".shortcut")
        metadata = output.with_suffix(".build.json")

        def check(name, content, expected, artifact=True):
            source.write_text(content, encoding="utf-8")
            before = hashlib.sha256(source.read_bytes()).hexdigest()
            result = subprocess.run([sys.executable, str(ROOT / "scripts/build.py"), str(source)],
                                    capture_output=True, text=True, encoding="utf-8", timeout=180)
            report = json.loads(metadata.read_text(encoding="utf-8"))
            assert result.returncode == expected, (name, result.stdout, result.stderr)
            assert report["success"] == (expected == 0), (name, report)
            assert output.exists() == (artifact and expected == 0), name
            assert hashlib.sha256(source.read_bytes()).hexdigest() == before, "Build changed source"
            results.append({"test": name, "passed": True, "wrapper_exit": result.returncode,
                            "compiler_exit": report.get("compiler_exit_code")})
            print(f"PASS {name}", flush=True)
            return report

        check("valid source and difficult path", valid, 0)
        exported = validate_export(output)
        text, preview = exported["WFWorkflowActions"][-2:]
        assert text["WFWorkflowActionIdentifier"] == "is.workflow.actions.gettext"
        assert preview["WFWorkflowActionIdentifier"] == "is.workflow.actions.previewdocument"
        assert preview["WFWorkflowActionParameters"]["WFInput"]["Value"]["OutputUUID"] == text["WFWorkflowActionParameters"]["UUID"]
        results.append({"test": "Text-to-Quick-Look action wiring", "passed": True})
        report = check("invalid syntax and stale export removal", 'import Shortcuts\ntext(text: "unterminated)\n', 1)
        assert report["compiler_exit_code"] == 0, "Expected observed upstream zero-exit error behaviour"
        assert any(d.get("line") == 2 for d in report["diagnostics"]), report
        raw = output.with_suffix(".stdout.log").read_text(encoding="utf-8")
        assert any(SYNTAX.match(line) for line in raw.splitlines()), raw
        # Exercise the exact editor task process and its matchers using real errors.
        for workspace in (ROOT.parent, ROOT):
            config = json.loads((workspace / ".vscode/tasks.json").read_text(encoding="utf-8"))
            task = next(task for task in config["tasks"] if task.get("group", {}) == {"kind": "build", "isDefault": True})
            command = task.get("windows", {}).get("command", task["command"]) if os.name == "nt" else task["command"]
            arguments = [argument.replace("${workspaceFolder}", str(workspace)).replace("${file}", str(source)) for argument in task["args"]]
            task_result = subprocess.run([command, *arguments], capture_output=True, text=True, encoding="utf-8", timeout=180, cwd=workspace)
            assert task_result.returncode == 1, task_result
            located = re.compile(task["problemMatcher"][0]["pattern"]["regexp"])
            unlocated = re.compile(task["problemMatcher"][1]["pattern"]["regexp"])
            matched = [located.match(line) for line in task_result.stdout.splitlines() if located.match(line)]
            assert any(int(match.group(2)) == 2 and Path(match.group(1)) == source for match in matched), task_result.stdout
            assert not any(unlocated.match(match.group(0)) for match in matched), "Duplicate/wrong file-level matching"
            results.append({"test": f"resolved VS Code task and syntax matcher ({workspace.name})", "passed": True})
        check("correct source and recompile", valid, 0)
        report = check("undefined action captured", 'import Shortcuts\nthisActionDoesNotExist(text: "fail")\n', 1)
        assert any("thisActionDoesNotExist" in d["message"] for d in report["diagnostics"])
        diagnostic = next(d for d in report["diagnostics"] if "thisActionDoesNotExist" in d["message"])
        assert unlocated.match(f"{source}: error: {diagnostic['message']}"), diagnostic
        report = check("malformed interpolation export rejected", 'import Shortcuts\ntext(text: "Hello") >> greeting\nshowResult(text: "${greeting}")\n', 1)
        assert report["stage"] == "compiled" and "rejected_export" in report, report
        assert any("outside its UTF-16 string" in d["message"] for d in report["diagnostics"]), report
        check("final recovery", valid, 0)
        for workspace in (ROOT.parent, ROOT):
            config = json.loads((workspace / ".vscode/tasks.json").read_text(encoding="utf-8"))
            task = config["tasks"][0]
            command = task.get("windows", {}).get("command", task["command"]) if os.name == "nt" else task["command"]
            arguments = [argument.replace("${workspaceFolder}", str(workspace)).replace("${file}", str(source)) for argument in task["args"]]
            task_result = subprocess.run([command, *arguments], capture_output=True, text=True, encoding="utf-8", timeout=180, cwd=workspace)
            assert task_result.returncode == 0, task_result
            results.append({"test": f"resolved VS Code task valid export ({workspace.name})", "passed": True})

        # An unreadable/nonexistent source must also fail meaningfully.
        missing = subprocess.run([sys.executable, str(ROOT / "scripts/build.py"), str(source.with_name("missing.jelly"))],
                                 capture_output=True, text=True, encoding="utf-8", timeout=180)
        assert missing.returncode == 1 and ": error:" in missing.stdout, missing
        results.append({"test": "missing source", "passed": True})

    if sys.platform == "linux":
        with tempfile.TemporaryDirectory(prefix="jelly Linux filesystem ") as temporary:
            workspace = Path(temporary) / "jelly"
            (workspace / "scripts").mkdir(parents=True)
            (workspace / "tests/compiler").mkdir(parents=True)
            shutil.copy2(ROOT / "scripts/build.py", workspace / "scripts/build.py")
            shutil.copy2(ROOT / "tests/compiler/hello-world.jelly", workspace / "tests/compiler/hello-world.jelly")
            result = subprocess.run([sys.executable, str(workspace / "scripts/build.py"), str(workspace / "tests/compiler/hello-world.jelly")],
                                    capture_output=True, text=True, encoding="utf-8", timeout=180)
            assert result.returncode == 0, result
            validate_export(workspace / "build/tests/compiler/hello-world.shortcut")
            results.append({"test": "repository on Linux filesystem with spaces", "passed": True})
            print("PASS repository on Linux filesystem with spaces", flush=True)
    summary = ROOT / f"build/validation-results-{sys.platform}.json"
    summary.write_text(json.dumps({"host": sys.platform, "results": results}, indent=2) + "\n", encoding="utf-8")
    print(f"{len(results)} checks passed. Evidence: {summary}")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main())
