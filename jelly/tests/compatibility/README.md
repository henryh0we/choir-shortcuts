# Jellycuts app compatibility evidence

Device profile reported in the existing project record: Jellycuts **2026.6.4**, iPadOS **26.6**, forScore **15.2.5**. The bundled compiler and action-library revisions remain unknown. Open-Jellycore `e1ec31c2ee192c8721749f9eb3b50108e38891cf` is a source-inspection candidate, not an established match for that app.

Documentation snapshot: `19306be1dd30c20e12058ebe144dd8342e64ca39`; navigate through the [local index](../../docs/jellycuts-docs-index.md). Prefer an exact device-tested form for this app profile over conflicting documentation or unmatched compiler source. Preserve discrepancies and their evidence rather than silently rewriting upstream examples.

## Known discrepancies

| Feature | Existing evidence, 16 October 2026 | Current candidate and next check |
| --- | --- | --- |
| Empty Stop and Output | User reported out-of-scope `DoNothing` in archive helper | Production uses `Respond` as an export workaround, with manual no-recipient repair. Test output probe before claiming acceptance. |
| File extension enum | User reported out-of-scope `FileExtension` | Official docs use `File Extension`; archive revision 4 uses it. Test file extension probe. |
| List item enum | User reported out-of-scope `FirstItem` | Official docs use `Item at Index`; archive revision 4 selects index `"1"`. Test list item probe. |
| Repeat result capture | User reported out-of-scope `archiveMatches` in larger helper | A cascading error is only a hypothesis. Test repeat capture probe independently. |
| Output signature | Web docs show `notes`/`folder`; inspected compiler reads `result`/`noResultBehavior`/`response` | Probe compiler-backed candidate; do not combine signatures or treat either as device-tested. |
| List literal example | Upstream `list.html` has incomplete example (`list(items: [\)`) | Probe existing project/source-backed string-array form; upstream example remains unchanged. |
| Repeat variables | Language guide uses spaced globals; inspected compiler tests use unspaced names | Repeat probe uses production candidate `RepeatItem`; confirm compiler acceptance and exported wiring. |

No successful compilation, import or execution of these probes has been recorded. Historical failures above come from the existing project reference, not a new device test performed during documentation import.

## Independent probes

Each source is one optional diagnostic Shortcut, revision 1, interface 1.0, with no installed Shortcut dependencies. They are not production dependencies. Install under the exact header name after successful compilation/export; comments do not set the name automatically. Compile each separately so a failure cannot hide an unrelated result.

| Source / installed name | Runtime steps and expected result | Stage / actual result |
| --- | --- | --- |
| [probe-output-respond.jelly](probe-output-respond.jelly) / TEST - Jelly Output Respond | Run directly: shows `Jelly output probe`. When called with a result recipient, returns that Text. Inspect generated Stop and Output fields. | Drafted / Not run |
| [probe-file-extension.jelly](probe-file-extension.jelly) / TEST - Jelly File Extension | Supply one synthetic PDF File named `probe.pdf` via a temporary Run Shortcut action. Inspect Get File Details output: `pdf`. Missing/non-File input is outside contract. | Drafted / Not run |
| [probe-list-item.jelly](probe-list-item.jelly) / TEST - Jelly List Item | Run directly, inspect List and Get Item from List. Result should be Text `Alpha`, selected from two items. Input ignored. | Drafted / Not run |
| [probe-repeat-capture.jelly](probe-repeat-capture.jelly) / TEST - Jelly Repeat Capture | Run directly, inspect Repeat with Each and captured result: two Text items `Alpha`, `Beta` in order. Input ignored. | Drafted / Not run |

These probes do not save, delete, transmit or modify files. The last three omit display/output actions to isolate compilation; inspect results in the Shortcuts editor. If temporary Quick Look actions are needed, record them as post-import test edits, separate from source compilation. The output probe alone tests explicit return behavior. Compile, inspect exported wiring, then run; successful parsing alone does not prove native types or runtime output.

## Record a result

Add a dated entry for each probe tested, including failures. Copy complete compiler diagnostics where practical, with private paths redacted. Revalidate after changing source; keep earlier results tied to their tested revision.

```text
Date / tester:
Probe filename / specification revision / source Git commit or SHA-256:
Jellycuts exact version/build:
Bundled compiler/library version (unknown if unavailable):
Device / iPadOS / editor language:
Documentation commit consulted:
Compilation action actually performed:
Exact diagnostics and affected line:
Compilation: Not run / Pass / Fail
Export artifact / action wiring inspection:
Import: Not run / Pass / Fail; installed name:
Runtime input / expected output / actual output / side effects:
Execution: Not run / Pass / Fail
Post-import edits, if any:
Conclusion and next change:
```
