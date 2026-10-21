# Daily local development

Save one Shortcut per `.jelly` file, preserving the existing `shortcuts/main/`,
`shortcuts/reusable/`, `examples/` and `tests/` layout and header/contracts.
See [AGENTS.md](../AGENTS.md) for naming, dependency and device evidence rules.
Use exact installed names for reusable helpers and build them before callers.
Imports expose action libraries; they do not include or install helper sources.

From the repository root in Windows PowerShell:

```powershell
python jelly/scripts/build.py jelly/tests/compiler/hello-world.jelly
python jelly/scripts/build.py "jelly/path with spaces/shortcut.jelly"
python jelly/scripts/build.py --all
python jelly/scripts/validate.py
```

The second command illustrates a source path you would create. You can supply
several existing paths to one invocation. To build only production sources:

```powershell
python jelly/scripts/build.py jelly/shortcuts/reusable/util-canonical-choir-name.jelly jelly/shortcuts/reusable/util-archive-choir-pdf.jelly jelly/shortcuts/reusable/util-assemble-choir-service.jelly jelly/shortcuts/main/main-build-choir-service.jelly
```

These production files currently fail compilation or structural checks under the
selected CLI; see [evidence](../tests/compiler/README.md). Do not assume `--all`
should pass while app-profile probes remain in the repository.

Inside WSL, from the `jelly/` directory:

```sh
python3 scripts/build.py tests/compiler/hello-world.jelly
python3 scripts/build.py --all
python3 scripts/validate.py
```

Python's standard library supplies everything; no pip packages or virtualenv
are required. Windows Python 3.14.3 and Ubuntu Python 3.14 were used here.
The Windows wrapper invokes the named `Ubuntu` distribution; override with
`--distro <name>` or `JELLY_WSL_DISTRO` after installing the compiler there.
Linux runs the installed user launcher directly, including when the repository
resides in the Linux filesystem.

## Outputs and diagnostics

`jelly/tests/compiler/hello-world.jelly` produces:

```text
jelly/build/tests/compiler/hello-world.shortcut
jelly/build/tests/compiler/hello-world.build.json
jelly/build/tests/compiler/hello-world.stdout.log
jelly/build/tests/compiler/hello-world.stderr.log
```

Exit 0 means every requested source compiled and its unsigned export passed the
wrapper's structural checks. Exit 1 indicates a source/compiler/export/tooling
failure; argparse uses exit 2 for incorrect command arguments. The raw CLI's exit
code is recorded separately because compiler errors can return 0.

The JSON report includes the original source hash, configured compiler profile,
actual command/raw exit status, diagnostics, stage, output hash and signing/device
flags. Logs preserve both streams. Configured versions describe the pinned setup;
they are not a fresh interrogation of a manually replaced binary. An output from a
previous build is removed before compiling that source. A structurally rejected
candidate is kept as `.rejected.plist`, without publishing a `.shortcut` file.
Do not commit generated exports/logs; they can contain source content.

Input is copied to a temporary UTF-8/LF `.jelly` file under build/ because the
pinned compiler misreads CRLF source positions. Source bytes are never rewritten;
temporary source and candidate files are removed after the build. Syntax diagnostic
line numbers still refer to the original file. Semantic diagnostics lack locations
and are reported against the file without inventing a line number.

The wrapper checks nonempty plist/action structure, ActionOutput UUID existence
and UTF-16 text attachment ranges. It does not validate all Apple schemas, complete
source consumption, control-flow fidelity, action availability or device execution.
Inspect those independently before import or execution.

## VS Code

Open either this repository root or its `jelly/` subfolder. Each has a tasks file.
Save the active `.jelly` file, then press **Ctrl+Shift+B** to run **Jelly: build
active file**. **Terminal → Run Task** also offers **Jelly: build all** and
**Jelly: validate compiler integration**. Non-Jelly active files fail clearly.

Tasks use `python` on Windows and `python3` in a WSL-connected window. Active-file
diagnostics are converted into Problems entries: the observed `SYNTAX ERROR,
line: N` format supplies a line; other events remain file-level. No native column
positions are claimed. The task process commands and regexes were tested outside
the editor; an actual keypress/Problems UI check still needs the user in VS Code.

For Option A, use the installed Microsoft WSL extension and connect to Ubuntu,
then open a Linux checkout. For Option B, use the current Windows checkout and
the Windows task. The latter is recommended here; Swift build products stay on
the Linux filesystem. See [setup](setup.md) for the tradeoffs.

## Codex

Agents read the scoped AGENTS.md, invoke this exact wrapper after source edits,
read stdout/stderr and JSON, correct supported source errors, and recompile.
After three unsuccessful attempts at the same diagnosis, report the blocker.
Do not modify a device-confirmed form solely to appease this older CLI. A passing
local compile proves no iPad execution, signing or installation. There is no
background watcher: automatic compilation is an agent instruction, and Ctrl+B is
the editor entry point.

## Troubleshooting

| Symptom | Check/action |
| --- | --- |
| WSL access denied inside Codex sandbox | Run the same build with the permitted sandbox escalation; `wsl --status` and `wsl --list --verbose` establish actual installation state |
| Wrong distribution or missing launcher | Check `--distro`, then `wsl -d Ubuntu -- bash -lc 'command -v jelly; jelly --help'` |
| Missing Swift/shared library/C compiler | Source `~/.local/share/swiftly/env.sh`; check `swift --version`; install only dependencies reported by Swiftly (setup.md) |
| Compiler needs rebuilding | Run `bash scripts/setup-compiler.sh` in WSL; it refuses a different/dirty checkout instead of resetting it |
| Nonsensical parser offsets from CRLF | Use the wrapper; direct raw CLI calls do not normalize line endings |
| `Found N errors` with raw status 0 | This is observed upstream behaviour; use wrapper status/JSON |
| Out-of-range text attachment | Known upstream interpolation defect; inspect rejected plist and choose a verified alternative binding where possible |
| Positional Output or enum rejected | Check the compiler/app profile; current app and 2024 CLI signatures differ |
| Empty/missing export despite compiler success | Wrapper rejects it; inspect captured streams, permissions and candidate structure |
| Shortcut won't import | Output is unsigned; use an accepted signing/import workflow; see compiler-limitations.md |

No restart was needed for this installation. A fresh shell may be needed for user
PATH changes. Never reinstall or remove existing WSL distributions to fix a build
error; preserve the compiler log and investigate its actual cause.
