# Local compiler smoke test

`hello-world.jelly` is one independent diagnostic Shortcut. It creates Text and
uses Quick Look with an explicit captured variable attachment. The two bindings
were checked against the pinned compiler source and local official docs.
It has no dependency on production or teaching examples.

Intended installed name: `TEST - Local Compiler Hello`. The upstream CLI hardcodes
`Function Tests` as the compilation name; verify and rename after any eventual import.

## Device test (not run)

Prerequisites: export, signing/import through an accepted Apple workflow, and an
iPhone/iPad with native Text and Quick Look. Import under the intended name.

1. Run directly: expect one displayed `Hello from local Jellycore!`.
2. Call with empty input: expect the same result.
3. Call with a nonempty Text input: expect the same result (input is ignored).
4. Dismiss the result: expect completion and no file/network side effects.

Actual device results: **Not run**. Local compilation/export evidence is recorded
separately; it cannot promote this Shortcut to device Tested or Verified.

## Local execution evidence, 21 October 2026

Host: Windows x64 build 26300.9711; WSL 2.7.10.0, kernel 6.18.33.2-2;
existing Ubuntu 26.04 WSL2. Official Open-Jellycore commit
`e1ec31c2ee192c8721749f9eb3b50108e38891cf`, clean source checkout, built unmodified
with Swift 6.4.1, using Package.resolved versions (TreeSitter 0.20.9-beta-2,
TreeSitterJelly 0.1.0, ArgumentParser 1.2.3). Release build took 102.99 seconds;
warnings were the existing grammar warning and unchecked createFile result.
The installed user launcher is `/home/henryhowe/.local/bin/jelly`.

The source revision is recorded as a SHA-256 in each generated `.build.json`;
the current source is the Quick Look variant. The initial Show Result/interpolation
variant compiled, but its one-character string had attachment range `{720, 1}`.
It was rejected after inspection. Direct native Quick Look input instead uses
the exact UUID exported by the Text action. No compiler-source patch was applied.

Validated smoke source SHA-256:
`047a8e5c1be1b02ce24af98730ef307988f683c945ee68dcb8498faa620e4b42`.
Final suites: **12 checks passed on Windows**, **13 on Linux**, including an
isolated repository on the native Linux filesystem. The default task's valid and
invalid invocations were resolved from both the root and `jelly/` task files.

| Check | Actual result |
| --- | --- |
| Basic Swift application | `swiftc` compiled and ran, printing `Swift local compilation works` |
| CLI launch/help | `jelly <file> [--export] [--out <out>]` confirmed |
| Valid source from WSL terminal | Compiled/exported; raw status 0, `Successfully Compiled Shortcut` |
| Windows wrapper through WSL | Passed; unsigned plist under `build/tests/compiler/hello-world.shortcut` |
| Invalid unterminated string | CLI emitted `SYNTAX ERROR, line: 2` and `Found 1 errors`, raw status **0**; wrapper status **1** |
| Unknown action | Diagnostic named the undefined function; captured as file-level error, wrapper status 1 |
| Correction/recompilation | Passed after replacing invalid source with valid source |
| Stale previous export | Removed before failed compile; no misleading `.shortcut` remained |
| Interpolated text | CLI accepted; wrapper rejected out-of-bounds UTF-16 attachment and retained rejected plist |
| CRLF source | Raw compiler produced corrupted action names; wrapper's temporary LF copy passed, original bytes unchanged |
| Difficult paths | Spaces, apostrophe, Unicode pound sign, dollar and semicolon passed |
| Missing source | Wrapper failed clearly, status 1 |
| VS Code task process/regex | Both workspace roots' resolved commands and real syntax/file-level matching tested; UI keypress/Problems display not exercised |
| Signing/import/device execution | Not performed |

Rerun `python jelly/scripts/validate.py` on Windows or `python3 scripts/validate.py`
from `jelly/` inside WSL. Generated host-specific reports are
`build/validation-results-win32.json` and `build/validation-results-linux.json`.
Each suite includes real compilation, mutation/failure/recovery, preserved source
hashes, UUID wiring and both VS Code task configurations. No mocked compiler.

## Existing repository compatibility audit

`python jelly/scripts/build.py --all` attempted 20 existing sources after line-ending
normalization. **3/20** passed compiler plus structural export checks. Five more
were accepted by the CLI but rejected by structural checks; twelve reported compiler
errors. All production sources were preserved. Full diagnostics are in each source's
mirrored `build/...build.json`, `.stdout.log`, `.stderr.log`, plus
`build/build-all-summary.log`.

| Source (relative to jelly/) | Result |
| --- | --- |
| `tests/compiler/hello-world.jelly` | Unsigned export accepted; Text → Quick Look UUID inspected |
| `tests/compatibility/probe-native-file-variable.jelly` | Unsigned export accepted; device/native type behaviour unverified |
| `tests/compatibility/probe-output-respond.jelly` | Unsigned export accepted; return behaviour unverified |
| `examples/main-jelly-greeting-demo.jelly` | CLI accepted; rejected dangling ActionOutput UUID |
| `examples/util-jelly-format-greeting.jelly` | CLI accepted; rejected interpolation attachment |
| `shortcuts/main/main-build-choir-service.jelly` | CLI accepted; rejected interpolation attachment |
| `shortcuts/reusable/util-canonical-choir-name.jelly` | CLI accepted; rejected interpolation attachment |
| `tests/compatibility/probe-repeat-capture.jelly` | CLI accepted; rejected interpolation attachment |
| `shortcuts/reusable/util-archive-choir-pdf.jelly` | Compiler errors, including core-node handling |
| `shortcuts/reusable/util-assemble-choir-service.jelly` | Compiler errors, including core-node handling |
| `tests/compatibility/probe-config-context.jelly` | Compiler errors, including core-node handling |
| `tests/compatibility/probe-file-extension.jelly` | Compiler rejected parameter form |
| `tests/compatibility/probe-list-item.jelly` | Compiler rejected parameter form |
| `tests/compatibility/probe-if-output-flush-left.jelly` | Compiler errors, including core-node handling |
| `tests/compatibility/probe-if-output-parenthesized.jelly` | Compiler errors, including core-node handling |
| `tests/compatibility/probe-if-output-unparenthesized.jelly` | Compiler errors, including core-node handling |
| `tests/functional/test-archive-config-error.jelly` | Compiler errors, including core-node handling |
| `tests/functional/test-archive-reuse.jelly` | Compiler errors, including core-node handling |
| `tests/functional/test-canonical-names.jelly` | Compiler errors, including core-node handling and positional Output |
| `tests/functional/test-choir-service.jelly` | Compiler rejected positional Output |

These are local-profile observations, not new iPad test results. The native-file
probe's export pass does not establish correct named-variable serialization or
runtime types. Keep prior device evidence and confirm each relevant action and
control-flow connection before use. The local compiler is operational, but it is
not a complete validator of the user's current Jellycuts app language.
