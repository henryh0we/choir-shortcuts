# Config integration acceptance checks

## Archive 15 context extraction update, 21 October 2026

Interface remains 2.1. ARC01-ARC03 are replaced by a quoted-index Repeat loop
that assigns native Repeat Items to Nothing-initialized sourceFile, archiveRoot
and workflowConfig. Presence checks precede Dictionary/File actions. Save
configuration and native File returns CFG02-CFG04 remain manual; guard retained.
The unchanged List contract requires all three native items separately.

Local command (Open-Jellycore e1ec31c / Swift 6.4.1):

```powershell
python jelly/scripts/build.py jelly/shortcuts/reusable/util-archive-choir-pdf.jelly jelly/tests/compatibility/probe-archive-context-loop.jelly
```

- Archive 15: failed. Diagnostics include positional Output parameter errors,
  brace/core-node messages and File Details unnamed-parameter errors. These are
  the recorded older-profile blockers; no successful full archive build claimed.
- Read-only probe: compiler and structural export checks passed, with **eight**
  brace/core-node warnings. Unsigned export contains the enclosing Repeat,
  three matched If/End If pairs with quoted 1/2/3 comparisons, Repeat Item
  assignments and downstream references to the current named variables.
  No extraction value is converted to Text. Exact source hashes and diagnostics
  are in the corresponding `build/shortcuts/reusable/` and
  `build/tests/compatibility/` `.build.json` reports.
- iPad: **Not run** for Archive 15 or this probe. Prior Text-only success does
  not establish native preservation. Follow [context-loop steps](compatibility/archive-context-loop.md),
  then existing save/reuse, native File-return and invalid-input cases below.

User-reported naming result, 21 October 2026: after the revision 11 transfer and
native List → Run Shortcut → Quick Look instructions, the user reports the correct
output. This confirms a successful complete naming-helper call for their supplied
test input, extending the earlier extraction-only previews. The message does not
specify which/all of the proposed filename cases were run, exact installed source
hash or any native edits; do not mark missing-input/custom-regex cases passed.
No new archive or whole-service result was supplied in this report.

Latest installation review: [pre-install audit](../docs/pre-install-audit.md).
Current Assembly 13 predeclares three loop-comparison variables; its updated
transfer copy matches source. All four production compiler attempts failed on
the recorded older-profile diagnostics; aggregate log: `build/pre-install-review.log`.
A separate running-order Text accumulator was compiled but its export failed
interpolation range validation. COL02 and all native File/Score/provider/forScore
slots remain except ARC01-ARC03, replaced by the Archive 15 candidate above; no new device pass or complete installable build is claimed.

## Current pre-iPad review, 21 October 2026

Current source revisions: Canonical **11**, Archive **15** (native context loop candidate), Assembly
**13**, Main **4**; interfaces 2.0 / 2.1 / 1.1 / 1.0. See the
[review and device acceptance cases](../docs/pre-ipad-review.md) for the changes
and migration steps. These instructions supersede historical Exit/noNameResult
requirements below: Canonical now uses positional Output and no longer has that
Nothing initializer. Canonical 11 now also removes NAME01/NAME02; the final
canonicalName Text-token check still applies.

User-confirmed extraction update: the quoted-index fixed fixture and caller/
receiver test both produce the expected two previews on the iPad. The user edited
existing device sources, so exact hashes/settings are not independently confirmed.
Revision 11 applies that loop to the naming helper's incoming Shortcut Input,
with unchanged interface 2.0. The full helper was attempted locally and rejected
at positional Output (known profile mismatch); no full-helper iPad pass is claimed.
Next run the existing canonical naming cases against revision 11: valid prefixed
and unprefixed filenames, custom regex, missing argument, and actual returned Text.
Native File/Score extraction is outside this successful Text-only probe's scope.

Local compiler attempts were performed for all four sources. None passed this
older CLI: it rejects positional Output and reports additional existing core-node
handling errors in the large helpers. No matching iPad compiler pass is claimed
for the changed revisions, and no signing/import/runtime test was performed.
Generated JSON includes current source hashes and diagnostics. New collection,
Score, choice and readback checks are source-reviewed candidates awaiting the
integrated device cases in the review. Prior user-confirmed installed archive
save/reuse fixes remain evidence for that manually completed copy only.

Final static checks: all four `.jelly`/`.txt` pairs are byte-identical; executable
source remains flush left; assembly block nesting is balanced; orderedFiles and
orderedNames preflights are outside their collection loops; preparedScores
preflight is outside the preparation loop and before setlist mode/creation.
Per-source build reports match the final source SHA-256 values. These checks are
source inspection evidence, not Apple runtime or matching-compiler validation.
The final assembly retry is captured in `build/forscore-assembly-review-final.log`.

## Historical revisions and device observations

Current naming skeleton: canonical revision 8/completed interface 2.0. Revision 7 failed at both bare ItemAtIndex calls. Revision 8 replaces them with NAME01/NAME02 native Get Item from List insertions. Complete indexes 1/2 from Shortcut Input and reconnect both presence checks and Replace Text consumers before tests. Keep noNameResult's Nothing initializer. Compilation/export, Exit returns, native completion and new-interface runtime remain Not run. Earlier enum experiments below are failed historical candidates, not instructions for the current helper.

Current canonical candidate: revision 7/interface 2.0. Revision 6 failed: the app explicitly disallows quoted ItemAtIndex and still rejects the full noResultBehavior argument. Revision 7 removes Output from this utility, uses documented `exit(var: ...)` for empty/value returns and uses bare ItemAtIndex. Its new Exit action must be compiled/imported and tested before claiming a pass. Check empty exits and both extraction indexes as well as the final Text returned to the caller. Earlier candidate descriptions below are historical.

Latest canonical candidate is revision 6/interface 2.0: revision 5 failed app compilation at both Item at Index and all four Respond output arguments. Revision 6 quotes enum literals using the pinned compiler raw selectors ItemAtIndex and Respond. Compilation/export/runtime remain Not run. Check extracted item 1 is filename and item 2 is regex before running replacement tests; a silently defaulted first-item selector is a failure. Other source revisions are unchanged.

17 October 2026. Canonical 5/interface 2.0; archive 8/completed interface 2.0; assembly 6/completed interface 1.1; main 3/interface 1.0. All new source revisions: Drafted. Compiler, native input types, config parsing, export/import and runtime results: **Not run**. Earlier manually completed naming/archive saves are historical fixtures; the new interfaces invalidate those results for this revision.

Follow [setup and contracts](../docs/config-integration.md). Use a disposable Choir Music root with the supplied config and matching category folders. Preserve your production installed copies. Compile on the recorded Jellycuts app, inspect complete native control flow/variable wiring, fill slots and retain the guards until ready. Do not equate a static schema/source check with device execution.

| Case | Steps and expected observation | Actual |
| --- | --- | --- |
| Native context | Parse the actual config File with Get Dictionary from Input, build native List [disposable PDF, test Library Folder, config Dictionary]. Run the [read-only probe](compatibility/probe-config-context.jelly). Exactly 3 items; correct PDF name/extension; folder can be enumerated; version 1 and 13 categories. No Text/JSON conversion of File or Folder. | Not run |
| Canonical configured rule | List [`Fri1-Walsh-Responses.pdf`, actual config.prefixRegex] → naming helper. Returns `Walsh-Responses`. Unprefixed `Jackson-InGminor.pdf` stays `Jackson-InGminor`. | Not run |
| Config edits take effect | Change the regex in disposable config to `^CUSTOM[0-9]+-`; next run `CUSTOM1-Walsh-Responses.pdf` → `Walsh-Responses`, while `Fri1-` is retained. No code edit/re-export. Restore original rule. | Not run |
| Root resolution | Set libraryFolder to `Test Library`, rename only disposable Library accordingly. Service resolves that native child of the configured Choir Music root. All archives stay beneath it. | Not run |
| Category order/content | Reorder categories or add a new category and matching Folder in disposable config/root. Next archive miss offers that order/name, resolves to Folder and saves there. Unlisted root items are not picker choices. | Not run |
| Archive miss | Native context with `Fri1-TestComposer-TestPiece.pdf`, absent from test Library. Choose Responses. Native `TestComposer-TestPiece.pdf` saved there with Overwrite off; return usable by Get Details of Files → Name. | Not run |
| Archive reuse | Run same input again: returns existing native File, no category prompt, no additional save. | Not run |
| Duplicate archive | Two PDFs in different test categories canonicalize to same identity. Stops before save/import and reports duplicates. | Not run |
| Missing config / malformed JSON | CONF02 fails if missing; Get Dictionary from Input fails if malformed. No PDF save/import/setlist changes occur. | Not run |
| Version / required keys | Unsupported version or missing prefixRegex/categories/libraryFolder stops before saves. Valid config uses Number version, Text regex/folder, Array categories; native coercions are not comprehensive schema validation. | Not run |
| Invalid regex | Broken regex in config halts validation before PDF operations; restore config before next test. | Not run |
| Missing category Folder | Select configured category with no matching child Folder. Stops before Set Name/Save File. Matching ordinary file instead of Folder fails Folder preflight. | Not run |
| Wrong context/legacy caller | Pass old filename Text or lone PDF instead of Lists. Count validation stops; no save. Flattened/mis-typed context must be fixed before use. | Not run |
| Service type | Config serviceType picker supplies chosen type to confirmation/report; no genre/tag writes are inferred. Omitted/empty serviceType uses Other. | Not run |
| Whole service / repair | With slots complete, prepare two disposable PDFs (existing/missing forScore score), choose B then A. Config read once; names, categories and report correct; Manual setlist readback preserves order. Repeat using Replace existing without duplicate archive copies. | Not run |
| Cancellation | Cancel preview before save/import: no writes. Cancellation later can leave prepared pieces or partial setlist; inspect state and rerun explicitly. | Not run |

Record date, tester, exact app/device versions, source hashes/revisions, compiler diagnostics, native slot/token changes, actual results and unresolved errors for each executed case. Quick Look's earlier UI error does not establish that the returned File is invalid; use filename inspection and Files readback.

Static verification on 17 October 2026: 174 action calls across four production sources and the context probe matched local documented parameter-slot sets, with the recorded compiler-backed Output exception. Delimiters balanced; block headers are parenthesized; Magic Variable capture names are unique per source; all production comments are line comments. Four utility callers supply the required List arity, assembly has one config parse, and all four `.txt` hashes match `.jelly`. The supplied example JSON parsed with 13 categories and four service types. Seven configured-name cases passed under .NET regular expressions, including a changed pattern and the supplied rule's intentional retention of `Thu1-`. Fifty-two local navigation links and `git diff --check` passed. No Jelly/Swift compiler is installed on PATH; no compiler, export, import or native runtime pass is claimed.

18 October 2026, canonical revision 9/interface 2.0: user reports manual repairs to receiving type (Text) and final output (canonicalName). Source now explicitly converts extracted filename to Text and documents post-import receiving/output wiring. Final exit(var: canonicalName) was already present and is retained; its exported native token must be checked. Caller still supplies two Text items via List; receiving Text must preserve their separate extraction. Regenerated revision compilation and runtime: Not run. See config-integration setup notes for the repair checklist.

## Helper compatibility revision, 18 October 2026

Archive 9/interface 2.0 and assembly 7/interface 1.1 remove Output enum arguments, all getItemFromList bindings and all block-result captures. Returns use documented exit(var: ...); native ARC01-ARC03/SCORE01-SCORE02 slots handle selection and COL01-COL03 Add to Variable slots handle ordered native collections. Archive File returns now directly reference existingCleanFile/savedCleanFile; inspect exported tokens. Both initial guards remain. Config keys/call contracts unchanged. Assembly Quick Look removed after earlier failed UI fixture; FS13 and report remain. See [completion checklist](../docs/helper-compatibility-update.md). New compiler/export/device results: Not run. Native List shape, named variable wiring, collection emptiness/ordering and repeated scores still require the integrated run. MAIN is unchanged and retains the unresolved Output form.

## Archive loop-condition scope correction, revision 10

User reports revision 9 errors at archiveExtensionLower (94), archiveStem (98) and childName (123). These are If inputs captured inside Repeat bodies. Revision 10 declares the three comparison variables before their loops, captures each native action output under a distinct Result name, and assigns it to the declared variable immediately before the corresponding If. This uses the local traditional-variables guide's Magic Variable assignment pattern; it is a candidate workaround, not a confirmed compiler diagnosis. Preserve existingCleanFile/typeFolder File references, guards, config contracts and manual slots. After export, check all three If inputs use the named variables and their Set Variable actions consume the immediately preceding correct action results. Corrected app compilation/export/runtime: Not run. Source and .txt copy are byte-identical.

## Exported archive validation defect (user report)

Archive revision 10 compiled and imported on the user's iPad, but the user now reports an empty native If body for missing prefixRegex, with no effective stop. Compilation/import therefore do not establish faithful branch generation. Source contains both an Alert and exit(var: noArchiveResult) inside that If; the report alone does not establish whether Exit, Alert or branch placement caused the omission. Treat current archive runtime as defective until repaired. Do not remove the initial guard or rely on it without inspecting the actual native stop action. In the installed shortcut, put Show Alert and Stop This Shortcut (or Stop and Output with no output) INSIDE the missing-prefixRegex If before End If. Inspect and repair every other validation branch similarly, preserving the CFG03/CFG04 native File returns. Assembly uses the same Exit pattern and needs the same native inspection. The correct installed-app Output call signature is still unresolved; request the exact working output line before substituting another guessed signature. No successful runtime pass is claimed.

## Output candidate after failed Exit generation

User confirms exit() does not work and has no known working Output source line. Archive 11 / assembly 8 therefore test exactly the local Output documentation signature with optional enum omitted: output(notes: "..."). No result/noResultBehavior/response or folder argument is used. Reference: jelly/vendor/jellycuts-docs/markdown/Documentation/Shortcuts/output.md. This is documentation-backed but not compiler/device-confirmed. All validation/guard/service returns use this candidate. Archive success outputs are intentionally empty placeholders at CFG03/CFG04 and must be wired to native existingCleanFile/savedCleanFile in Shortcuts. Inspect native stops within every branch, guard and success return before execution; successful compilation alone is insufficient. New compile/export/runtime results: Not run. Naming helper and main are unchanged; naming retains its separately reported manual repair and main its unresolved older Output binding.

Archive 12 / Assembly 9: replaced entire affected If blocks with AV/SV native If-Alert-Stop-End If slots after user reports both message and stop missing in export. Removed generated Output/Exit calls, including guard/final returns; AGUARD/SGUARD MUST be inserted as native stops before any execution, and ARETURN/SRETURN must be completed. Existing manual slots remain. This is a manually completed template, not a claimed automatic export fix. Compilation/export/runtime of these revisions: Not run. See native-validation-blocks.md for all conditions/messages/results.

## Restored documented If/Output validation (Archive 13 / Assembly 10)

User explicitly requested executable source fixes instead of native validation slots. Replaced all 30 AV/SV slots with full parenthesized If blocks. Failure bodies directly call output(notes: "ERROR: descriptive problem"); separate Alert/Text/Exit generation is removed from those branches. Initial guards and final assembly report also use direct Output. Optional folder enum omitted per vendored output.md. Successful archive-reuse If is restored; CFG03/CFG04 require native File result tokens because documented Output accepts String, not a demonstrated native File parameter. Assembly uses documented getType(input: cleanFile), with a predeclared comparison variable, to propagate Text errors before import. Archive completed interface is 2.1 (File success / ERROR: Text failure), assembly completed interface remains 1.1. No manual validation/guard/report construction is requested. Existing native provider/list/forScore slots remain. Docs support this syntax; original branch omission cause is not established. New compilation/export/runtime: Not run. Check missing-prefixRegex error and stop, plus saved/reused native Files, during the integrated run.

## Device-confirmed flush-left If/Output fixture

User reports both the unparenthesized and flush-left probes warn about missing noResultBehaviour and response content in output. The flush-left parenthesized probe nevertheless exports/runs and returns Conditional output reached; the output inside the If therefore exists and returns in this fixture. Earlier parenthesized/indented probe exported the If without its Output; unparenthesized probe exported no If. Positional payload avoids the observed literal notes: prefix. Archive 14 and Assembly 11 apply flush-left executable source and positional output("...") throughout; preserve multiline string content. New full helper compilation/export/runtime: Not run. Keep missing-parameter warnings unresolved rather than claiming a clean compile or guessing named arguments. Conditional interpolation, nested control flow, native object transport and CFG03/CFG04 File returns still need the integrated device check. AGENTS formatting instructions now record this device-backed exception. No native AV/SV validation construction is requested.

## User-confirmed Archive 14 export/import

The user confirms UTIL - Archive Choir PDF revision 14 loaded correctly into Apple Shortcuts and all Output actions are present as expected. This confirms the full archive's export/import action-presence result, extending the earlier flush-left probe. Parenthesized If, flush-left bodies and positional output("...") are the current device-supported forms. Do not generalize this result to Assembly 11, native slot completion, File returns or end-to-end archive execution: those remain unverified. Prior missing noResultBehaviour/response warnings have not been reported resolved. Next: complete ARC01-ARC03 and CFG02-CFG04, retain the initial guard until completion, then check a missing-config-key error and native save/reuse results using disposable input.

## Archive runtime: first save passes, repeated input duplicates

User confirms manually completed Archive saves a PDF into the selected category. Category prompt was manually changed to a Text action with filename on its own line, then that Text token used as the prompt. User also repaired both naming-input Lists to use real filename/prefixRegex tokens instead of literal names. Repeat test now FAILS: another category save creates -2/-3 copies. Do not mark reuse/idempotency verified. First investigate installed archiveRoot recursive enumeration, the archiveStem == canonicalStem comparison's actual variable tokens, and Set Variable existingCleanFile from the search loop's native Repeat Item plus CFG03 return. Source interpolation and generated native connections are not proven by compilation. Numbered copies demonstrate missed reuse but do not identify which of these steps failed. Keep Overwrite off; enabling it would conceal the failure rather than establish reuse. No production PDFs are deleted by this investigation.

## Archive reuse repaired; conditional reference audit (19 October 2026)

User confirms reconnecting the post-loop existingCleanFile If to the current named variable and using has any value fixes reuse and returns the correct existing File. Prior search matched inside the loop but post-loop branch was skipped; this was a native input reference defect, not proof the lookup comparison failed. No source regeneration is claimed to preserve that manual correction. Added docs/conditional-input-audit.md enumerating source conditions and higher-risk named-variable/replaced-output connections in archive, assembly and naming helper. Other conditions remain unverified, not known broken.

Short executable drivers for targeted coverage are in [functional tests](functional/README.md). Four sources, identical text copies, two disposable config fixtures. All new driver compile/import/runtime results remain Not run.
