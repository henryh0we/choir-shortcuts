# Jellycuts app compatibility evidence

Device profile reported in the existing project record: Jellycuts **2026.6.4**, iPadOS **26.6**, forScore **15.2.5**. The bundled compiler and action-library revisions remain unknown. Open-Jellycore `e1ec31c2ee192c8721749f9eb3b50108e38891cf` is a source-inspection candidate, not an established match for that app.

Documentation snapshot: `19306be1dd30c20e12058ebe144dd8342e64ca39`; navigate through the [local index](../../docs/jellycuts-docs-index.md). Prefer an exact device-tested form for this app profile over conflicting documentation or unmatched compiler source. Preserve discrepancies and their evidence rather than silently rewriting upstream examples.

## Known discrepancies

Comment grouping clarification: one intended native Comment block must be written as one physical `//` source line, even when it contains several sentences. Consecutive `//` lines create separate Comment actions. Archive revision 8 and assembly revision 6 join each related assembly instruction group onto one line; individual header fields remain intentionally separate. This is a comment-formatting change only; interfaces and executable statements are unchanged.

17 October 2026 config update: native transport is a three-item List (PDF File, Library Folder, parsed config Dictionary), not a JSON Dictionary containing File paths. The inspected Dictionary writer lacks interpolation support; native object construction via it is not established. Use [probe-config-context.jelly](probe-config-context.jelly) and [config acceptance checks](../config-integration.md) to check extraction and types before writes. New config-based sources are uncompiled/untested; user-confirmed save/name behavior belongs to earlier manually completed versions. All revised production comments are now `//` only.

User-reported comment behavior in the installed Jellycuts 2026.6.4 build: `/* ... */` block comments do not work. Only `//` line comments work, with one source line producing one separate native Comment block. Use line comments for future source changes; do not infer block-comment support from the older inspected compiler. This note does not claim that existing source block comments have been converted.

Archive revision 5 also has a user-reported missing first If wrapper in the generated Shortcut. Archive 6 and assembly 4 now use the local guide's parenthesized `if(condition) {` and `repeatEach(items) {` forms throughout. Previous unparenthesized forms came from unmatched compiler-source examples. Parentheses are a documentation-backed correction to test, not a confirmed diagnosis or device pass. Inspect generated control-flow markers before execution. The initial ASSEMBLY GUARD Stop and Output is intentionally unconditional and must be distinguished from the missing-input validation stop.

User-confirmed runtime fixture: the manually adjusted canonical helper returned the expected name for `Fri1-Walsh-Responses.pdf` after removal of the unconditional early stop and native input/result wiring corrections. Its receiving configuration is Text, with an error message on missing input. This is one installed-fixture pass, not verification of unmodified exports or the larger helpers. Preserve these receiving/wiring settings on regeneration.

Latest device observation: canonical revision 3 compiled/generated, but its first empty Stop and Output was in the regular flow with no surrounding If action. Supplied filename input is confirmed; successful filename transformation/return is not yet confirmed. Canonical revision 4 removes this guard entirely and retains only the two replacements and final return. The cause of the missing If is not established. Inspect generated If/Otherwise/End If structure in archive and assembly before enabling their writes; compilation alone has not established faithful control-flow generation.

| Feature | Existing evidence, 16 October 2026 | Current candidate and next check |
| --- | --- | --- |
| Empty Stop and Output | User reported out-of-scope `DoNothing` in archive helper | Production uses `Respond` as an export workaround, with manual no-recipient repair. Test output probe before claiming acceptance. |
| File extension enum | User reported out-of-scope `FileExtension` | Official docs use `File Extension`; archive 5 and assembly 3 use it. Test file extension probe if needed. |
| List item enum | User reported out-of-scope `FirstItem` | Official docs use `Item at Index`; assembly 3 selects index `"1"`. Archive 5 no longer needs a list-item action. |
| Repeat result capture | User reported out-of-scope `archiveMatches` in larger helper | Archive 5 removes that capture using a named File variable and duplicate check. Other source-backed captures remain in assembly. Optional repeat probe isolates those. |
| If result capture | User reports canonical revision 2 fails at line 21: `sourceName` does not exist in scope after `} >> sourceName` | Canonical 3 stops early for absent input, then passes ShortcutInput directly to Replace Text. No block capture or mutable variable required. Corrected compilation remains unverified. Remaining assembly block captures must not be treated as app-confirmed. |
| Mutable File variable | Local variables guide documents assignment from native globals/Magic Variables; inspected older compiler has unresolved named-variable encoding | Archive 5 uses documented assignment. Inspect named-variable references after export and exercise first-match, no-match and duplicate paths. Optional native File variable probe isolates this. |
| Output signature | Web docs show `notes`/`folder`; inspected compiler reads `result`/`noResultBehavior`/`response` | Probe compiler-backed candidate; do not combine signatures or treat either as device-tested. |
| List literal example | Upstream `list.html` has incomplete example (`list(items: [\)`) | Probe existing project/source-backed string-array form; upstream example remains unchanged. |
| Repeat variables | Language guide uses spaced globals; inspected compiler tests use unspaced names | Repeat probe uses production candidate `RepeatItem`; confirm compiler acceptance and exported wiring. |

No successful compilation, import or execution of these probes has been recorded. Historical failures above come from the existing project reference, not a new device test performed during documentation import.

## Independent probes

Each source is one optional diagnostic Shortcut, revision 1, interface 1.0, with no installed Shortcut dependencies. They are not production dependencies. Install under the exact header name after successful compilation/export; comments do not set the name automatically. Compile each separately so a failure cannot hide an unrelated result.

| Source / installed name | Runtime steps and expected result | Stage / actual result |
| --- | --- | --- |
| [probe-config-context.jelly](probe-config-context.jelly) / TEST - Jelly Config Context | Supply native [PDF, Library Folder, parsed config Dictionary]. Displays correct filename/extension, Folder name, version 1 and 13 categories; Folder enumeration must succeed. See [config tests](../config-integration.md). | Drafted / Not run |
| [probe-output-respond.jelly](probe-output-respond.jelly) / TEST - Jelly Output Respond | Run directly: shows `Jelly output probe`. When called with a result recipient, returns that Text. Inspect generated Stop and Output fields. | Drafted / Not run |
| [probe-file-extension.jelly](probe-file-extension.jelly) / TEST - Jelly File Extension | Supply one synthetic PDF File named `probe.pdf` via a temporary Run Shortcut action. Inspect Get File Details output: `pdf`. Missing/non-File input is outside contract. | Drafted / Not run |
| [probe-list-item.jelly](probe-list-item.jelly) / TEST - Jelly List Item | Run directly, inspect List and Get Item from List. Result should be Text `Alpha`, selected from two items. Input ignored. | Drafted / Not run |
| [probe-repeat-capture.jelly](probe-repeat-capture.jelly) / TEST - Jelly Repeat Capture | Run directly, inspect Repeat with Each and captured result: two Text items `Alpha`, `Beta` in order. Input ignored. | Drafted / Not run |
| [probe-native-file-variable.jelly](probe-native-file-variable.jelly) / TEST - Jelly Native File Variable | Supply one synthetic PDF via temporary caller. Inspect Set Variable and Quick Look: the same native PDF should appear, with no Text conversion. Check the consumer selects named `selectedFile`, not initial Nothing. | Drafted / Not run |

These probes do not save, delete, transmit or modify files. The file-extension, list-item and repeat-capture probes omit display/output actions to isolate compilation; inspect results in the Shortcuts editor. If temporary Quick Look actions are needed, record them as post-import test edits, separate from source compilation. The output probe alone tests explicit return behavior. Compile, inspect exported wiring, then run; successful parsing alone does not prove native types or runtime output. Probes are optional diagnostics; they do not replace or block the integrated service run.

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
