# Jellycuts app compatibility evidence

Archive 15 replaces ARC01-ARC03 with a native context loop candidate. Independent
read-only diagnostic **TEST - Archive Context Loop**: [source](probe-archive-context-loop.jelly),
[transfer copy](probe-archive-context-loop.txt), [contract, steps and evidence](archive-context-loop.md).
No dependencies; reads a supplied PDF/Folder/Dictionary, shows three previews,
and performs no saves or forScore writes. Local compiler/structural checks passed
with eight core-node warnings. The user reports iPad previews
`Fri4-Humfrey-InEMinor`, `13`, `1`, supporting the three native consumers;
confirm the selected Folder has 13 immediate children. Full archive save/reuse
and native File returns remain untested; see the linked evidence for scope.

New isolated manual-work candidate: [running-order Text accumulator](running-order-text.md).
The local CLI accepts it, but structural export checks reject the known
interpolation defect. Its iPad result is pending; production COL02 is unchanged.

Source-only NAME01/NAME02 experiments:
[indexed naming-item tests](name-item-extraction.md). The original fixed two-Text
probe compiled locally, but the user confirms iPad rejection at lines 13/14 because
ItemAtIndex was not in scope. The separate declared-selector candidate compiles
locally and, by user report, compiles/runs on the iPad, but the supplied screenshot
shows **both selectors defaulting to First Item**. It fails the required indexed
extraction and must not replace production NAME slots. Both failed probes are
preserved; successful compilation alone is insufficient evidence.

A separate [loop-based candidate](name-item-extraction.md#next-candidate-avoid-selectors-with-a-loop)
now avoids enum selectors entirely. It compiles locally with brace/core-node
warnings; its exported loop, index conditions and named assignments were inspected.
Its unquoted numeric version failed iPad compilation as recorded below.

Loop update: the user reports the unquoted numeric comparisons fail app compilation
at lines 15/18 because variables 1 and 2 are not in scope. The separate
[quoted-index candidate](name-item-extraction.md#next-candidate-quoted-loop-index-comparisons)
uses `"1"` and `"2"`, following the documented String comparison form. It compiles
locally with the same warnings. The user now confirms that adding quotes to the
original loop makes it work as expected. The user subsequently confirms the
caller/receiver test also loads the two expected previews from the incoming List.
Canonical revision 11 now uses that source-only quoted-index loop instead of
NAME01/NAME02 slots. Full naming-helper validation and native File/Score transport
remain separate; preserve all earlier failed probes.

For a small same-source iPad/local experiment, use the new
[positional Output comparison](output-signature-comparison.md). It isolates the
Output argument form from control flow and interpolation; its exact-source iPad
compilation and generated action are now confirmed by user report: one Stop and
Output with the exact literal Text and no-recipient behaviour Do Nothing, despite
two missing-parameter warnings. Local Open-Jellycore rejects that positional form.
Runtime return behaviour remains untested. The existing named Output probe is the
local positive control; its iPad result remains unknown. See the comparison for
the exact warnings and limits of this evidence.

**Local CLI evidence, 21 October 2026:** the WSL compiler is now installed. The
native-file-variable and output-respond probes passed local compilation and
structural export checks; other probes failed compilation or export checks. See
the [per-file local audit](../compiler/README.md). This does not update the device
results below or establish that the 2024 CLI matches Jellycuts 2026.6.4.

Device profile reported in the existing project record: Jellycuts **2026.6.4**, iPadOS **26.6**, forScore **15.2.5**. The bundled compiler and action-library revisions remain unknown. Open-Jellycore `e1ec31c2ee192c8721749f9eb3b50108e38891cf` is a source-inspection candidate, not an established match for that app.

Documentation snapshot: `19306be1dd30c20e12058ebe144dd8342e64ca39`; navigate through the [local index](../../docs/jellycuts-docs-index.md). Prefer an exact device-tested form for this app profile over conflicting documentation or unmatched compiler source. Preserve discrepancies and their evidence rather than silently rewriting upstream examples.

## Known discrepancies

Canonical revision 7 still reports bare ItemAtIndex out of scope at both extraction actions. Revision 8 removes this binding from the helper entirely and uses NAME01/NAME02 native insertion slots: Get Item from List using Shortcut Input, indexes 1 and 2. Reconnect all downstream uses of the dummy results before removing Nothing. No selector spelling is now claimed compatible. Compile/export of the revised skeleton, Exit behavior, native insertions and runtime remain unverified. Other sources with getItemFromList still need reconciliation before they can be treated as compatible.

Canonical revision 6 failed in the installed app: quoted ItemAtIndex is explicitly rejected with advice to use bare ItemAtIndex; each Output call still reports the whole `noResultBehavior: "Respond"` argument out of scope. Revision 7 uses bare ItemAtIndex and replaces Output with the local documented `exit(var: ...)` native-variable return, including Nothing-based empty exits. The underlying Output signature remains unresolved; it is bypassed here rather than declared fixed. Revision 7 compilation/export/runtime are pending. Earlier quoted-enum guidance below is rejected historical evidence, not the current recommendation.

Canonical revision 5 compilation report: the two bare `Item at Index` arguments and four bare Respond/output arguments are reported as out-of-scope variables. Revision 6 tests quoted enum arguments: `type: "ItemAtIndex"` and `noResultBehavior: "Respond"`. ItemAtIndex is the exact raw selector in the inspected WFItemSpecifier enum; the spaced web example differs. Quoting is a candidate fix for identifier resolution, not an app-confirmed result. Inspect both exported list actions: they must select Item at Index with indexes 1 and 2 respectively; a missing/default selector must not silently select the first item twice. Other sources retain earlier enum forms pending this isolated check.

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

18 October 2026, canonical revision 9/interface 2.0: user reports manual repairs to receiving type (Text) and final output (canonicalName). Source now explicitly converts extracted filename to Text and documents post-import receiving/output wiring. Final exit(var: canonicalName) was already present and is retained; its exported native token must be checked. Caller still supplies two Text items via List; receiving Text must preserve their separate extraction. Regenerated revision compilation and runtime: Not run. See config-integration setup notes for the repair checklist.

## Helper compatibility revision, 18 October 2026

Archive 9/interface 2.0 and assembly 7/interface 1.1 remove Output enum arguments, all getItemFromList bindings and all block-result captures. Returns use documented exit(var: ...); native ARC01-ARC03/SCORE01-SCORE02 slots handle selection and COL01-COL03 Add to Variable slots handle ordered native collections. Archive File returns now directly reference existingCleanFile/savedCleanFile; inspect exported tokens. Both initial guards remain. Config keys/call contracts unchanged. Assembly Quick Look removed after earlier failed UI fixture; FS13 and report remain. See [completion checklist](../../docs/helper-compatibility-update.md). New compiler/export/device results: Not run. Native List shape, named variable wiring, collection emptiness/ordering and repeated scores still require the integrated run. MAIN is unchanged and retains the unresolved Output form.

## Archive loop-condition scope correction, revision 10

User reports revision 9 errors at archiveExtensionLower (94), archiveStem (98) and childName (123). These are If inputs captured inside Repeat bodies. Revision 10 declares the three comparison variables before their loops, captures each native action output under a distinct Result name, and assigns it to the declared variable immediately before the corresponding If. This uses the local traditional-variables guide's Magic Variable assignment pattern; it is a candidate workaround, not a confirmed compiler diagnosis. Preserve existingCleanFile/typeFolder File references, guards, config contracts and manual slots. After export, check all three If inputs use the named variables and their Set Variable actions consume the immediately preceding correct action results. Corrected app compilation/export/runtime: Not run. Source and .txt copy are byte-identical.

## Exported archive validation defect (user report)

Archive revision 10 compiled and imported on the user's iPad, but the user now reports an empty native If body for missing prefixRegex, with no effective stop. Compilation/import therefore do not establish faithful branch generation. Source contains both an Alert and exit(var: noArchiveResult) inside that If; the report alone does not establish whether Exit, Alert or branch placement caused the omission. Treat current archive runtime as defective until repaired. Do not remove the initial guard or rely on it without inspecting the actual native stop action. In the installed shortcut, put Show Alert and Stop This Shortcut (or Stop and Output with no output) INSIDE the missing-prefixRegex If before End If. Inspect and repair every other validation branch similarly, preserving the CFG03/CFG04 native File returns. Assembly uses the same Exit pattern and needs the same native inspection. The correct installed-app Output call signature is still unresolved; request the exact working output line before substituting another guessed signature. No successful runtime pass is claimed.

## Output candidate after failed Exit generation

User confirms exit() does not work and has no known working Output source line. Archive 11 / assembly 8 therefore test exactly the local Output documentation signature with optional enum omitted: output(notes: "..."). No result/noResultBehavior/response or folder argument is used. Reference: jelly/vendor/jellycuts-docs/markdown/Documentation/Shortcuts/output.md. This is documentation-backed but not compiler/device-confirmed. All validation/guard/service returns use this candidate. Archive success outputs are intentionally empty placeholders at CFG03/CFG04 and must be wired to native existingCleanFile/savedCleanFile in Shortcuts. Inspect native stops within every branch, guard and success return before execution; successful compilation alone is insufficient. New compile/export/runtime results: Not run. Naming helper and main are unchanged; naming retains its separately reported manual repair and main its unresolved older Output binding.

Archive 12 / Assembly 9: replaced entire affected If blocks with AV/SV native If-Alert-Stop-End If slots after user reports both message and stop missing in export. Removed generated Output/Exit calls, including guard/final returns; AGUARD/SGUARD MUST be inserted as native stops before any execution, and ARETURN/SRETURN must be completed. Existing manual slots remain. This is a manually completed template, not a claimed automatic export fix. Compilation/export/runtime of these revisions: Not run. See native-validation-blocks.md for all conditions/messages/results.

## Restored documented If/Output validation (Archive 13 / Assembly 10)

User explicitly requested executable source fixes instead of native validation slots. Replaced all 30 AV/SV slots with full parenthesized If blocks. Failure bodies directly call output(notes: "ERROR: descriptive problem"); separate Alert/Text/Exit generation is removed from those branches. Initial guards and final assembly report also use direct Output. Optional folder enum omitted per vendored output.md. Successful archive-reuse If is restored; CFG03/CFG04 require native File result tokens because documented Output accepts String, not a demonstrated native File parameter. Assembly uses documented getType(input: cleanFile), with a predeclared comparison variable, to propagate Text errors before import. Archive completed interface is 2.1 (File success / ERROR: Text failure), assembly completed interface remains 1.1. No manual validation/guard/report construction is requested. Existing native provider/list/forScore slots remain. Docs support this syntax; original branch omission cause is not established. New compilation/export/runtime: Not run. Check missing-prefixRegex error and stop, plus saved/reused native Files, during the integrated run.

## Latest device report: Output labels become literal payload

Archive 13 exported its first unconditional Output, but its result contains the literal notes: label as well as the error string; later conditional Outputs remain absent. This disproves compatibility of the local documented notes: form with this installed app. The app's Output parsing and If body generation must be isolated separately; no successful corrected signature is known. Official Open-Jellycore main still expects result/noResultBehavior/response and therefore is not evidence of a matching app compiler. Added two small probe-if-output files: positional output("message") (explicitly inferred, not documented or confirmed) with parenthesized versus unparenthesized If. Expected native structure is listed in each header. Neither performs writes. Full helpers intentionally unchanged pending a successful native export; do not describe archive 13 / assembly 10 as working.

## If syntax probe results and indentation hypothesis

User reports parenthesized If exports the If but no Output in its body; unparenthesized form exports no If. Therefore retain parenthesized syntax for this installed app. Neither probe passes. Added probe-if-output-flush-left: same parenthesized condition and positional Output but no leading indentation on the body action. This isolates leading whitespace as a possible cause, not an established diagnosis. Output payload correctness and conditional runtime stop are not yet confirmed. Full helper sources unchanged pending this focused result; do not apply unparenthesized If based on unmatched compiler-source examples.

## Device-confirmed flush-left If/Output fixture

User reports both the unparenthesized and flush-left probes warn about missing noResultBehaviour and response content in output. The flush-left parenthesized probe nevertheless exports/runs and returns Conditional output reached; the output inside the If therefore exists and returns in this fixture. Earlier parenthesized/indented probe exported the If without its Output; unparenthesized probe exported no If. Positional payload avoids the observed literal notes: prefix. Archive 14 and Assembly 11 apply flush-left executable source and positional output("...") throughout; preserve multiline string content. New full helper compilation/export/runtime: Not run. Keep missing-parameter warnings unresolved rather than claiming a clean compile or guessing named arguments. Conditional interpolation, nested control flow, native object transport and CFG03/CFG04 File returns still need the integrated device check. AGENTS formatting instructions now record this device-backed exception. No native AV/SV validation construction is requested.

## User-confirmed Archive 14 export/import

The user confirms UTIL - Archive Choir PDF revision 14 loaded correctly into Apple Shortcuts and all Output actions are present as expected. This confirms the full archive's export/import action-presence result, extending the earlier flush-left probe. Parenthesized If, flush-left bodies and positional output("...") are the current device-supported forms. Do not generalize this result to Assembly 11, native slot completion, File returns or end-to-end archive execution: those remain unverified. Prior missing noResultBehaviour/response warnings have not been reported resolved. Next: complete ARC01-ARC03 and CFG02-CFG04, retain the initial guard until completion, then check a missing-config-key error and native save/reuse results using disposable input.

## Archive runtime: first save passes, repeated input duplicates

User confirms manually completed Archive saves a PDF into the selected category. Category prompt was manually changed to a Text action with filename on its own line, then that Text token used as the prompt. User also repaired both naming-input Lists to use real filename/prefixRegex tokens instead of literal names. Repeat test now FAILS: another category save creates -2/-3 copies. Do not mark reuse/idempotency verified. First investigate installed archiveRoot recursive enumeration, the archiveStem == canonicalStem comparison's actual variable tokens, and Set Variable existingCleanFile from the search loop's native Repeat Item plus CFG03 return. Source interpolation and generated native connections are not proven by compilation. Numbered copies demonstrate missed reuse but do not identify which of these steps failed. Keep Overwrite off; enabling it would conceal the failure rather than establish reuse. No production PDFs are deleted by this investigation.

## Archive reuse repaired; conditional reference audit (19 October 2026)

User confirms reconnecting the post-loop existingCleanFile If to the current named variable and using has any value fixes reuse and returns the correct existing File. Prior search matched inside the loop but post-loop branch was skipped; this was a native input reference defect, not proof the lookup comparison failed. No source regeneration is claimed to preserve that manual correction. Added docs/conditional-input-audit.md enumerating source conditions and higher-risk named-variable/replaced-output connections in archive, assembly and naming helper. Other conditions remain unverified, not known broken.
