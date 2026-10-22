# Choir service integration record

23 October 2026, user report: completed installed Assembly prepares one score,
passes repaired readback and opens its setlist. Native direct New Setlist capture
and the prompted date/name default also work. This is a manually repaired fixture;
fresh-source fidelity, two-score order, repetitions and Replace existing remain
unverified. See [exact changes and evidence limits](../docs/ipad-assembly-lessons.md)
and [the next iPad tests](ipad-investigation/README.md). Historical “Not run” entries
below are not current results for this specific one-score fixture.

Current config-based revisions (17 October 2026) are recorded separately in [config integration tests](config-integration.md): canonical 5/interface 2.0, archive 7/interface 2.0, assembly 5/interface 1.1, main 3/interface 1.0. The historical records below do not validate the changed input contracts. The user confirmed a correctly named PDF saved to the selected test category and a usable returned filename in the earlier manually configured archive; a subsequent Quick Look action failed with a UI-context error. No config-based runtime pass is recorded.

Release 1, 15 October 2026. Current stage: Drafted. Native helpers: Designed. Target reported by user: iPadOS 26.6, forScore 15.2.5, Jellycuts 2026.6.4. Actual compiler/import results for these new files: Not run.

Build using [the installation guide](../docs/choir-service-build.md). Record compiler messages and any action-setting differences here during construction; those are integration fixes, not a prerequisite test campaign.

| Case | Steps and expected observations | Actual result |
| --- | --- | --- |
| Whole service | Select two disposable Nextcloud PDFs, order them B then A, one existing in forScore and one missing. Clean PDFs retained, existing score reused, missing score imported, confirmed title/composer applied, one service contains B then A | Not run |
| Repeat and repair | Run same selection, choose Replace existing and the same setlist. No duplicate scores/archives; chosen running order restored. Choose Review metadata for any pending metadata | Not run |
| Cancel before writes | Cancel initial filename preview. No archive, score or setlist writes | Not run |
| Invalid/missing input | Run canonical helper without input: empty Text, no writes. Call assemble with other mode: explanatory Text, no writes. Non-PDF selection in assemble: stop before writes. Archive missing input: no File returned and explanatory alert | Not run |
| Unprefixed/variants | Use Jackson-InGminor.pdf and a separate movement/verse-qualified score. Full canonical identities retained; reviewed metadata does not merge variants | Not run |
| Failure after import | If an action fails after importing, rerun using the same canonical filename and Review metadata. Existing working score is reused. Inspect actual state before retrying an uncertain import | Not run |

For Canonical Choir Name, source-reviewed examples are Fri1-Walsh-Responses.pdf → Walsh-Responses; Sunam4-Howells-CollegiumRegale-TeDeum.pdf → Howells-CollegiumRegale-TeDeum; Sat3-Ps89vv30-50(Plainsong).pdf → Ps89vv30-50(Plainsong); Jackson-InGminor.pdf → Jackson-InGminor. These examples are expectations, not recorded compiler/device passes.

Implementation record: revision, builder, device, date, compiler/import outcome, actual results and unresolved failures: Not recorded. Only promote the current release after its actual integration run. Preserve the earlier user-reported native lookup/rename evidence separately.

Static validation on 15 October 2026: 66 local links across the implementation and affected indexes resolved. Seven canonical-name cases passed using the patterns extracted from the Jelly source and .NET regular expressions. This checks the patterns and expected identities, not Jelly string compilation, Shortcuts generation, or Apple runtime behaviour. No Jelly compiler was available locally. Native branch/loop nesting and source call/dependency names were reviewed separately.

Assembly revision 2, 16 October 2026: archive and assembly now have generated Jelly source. Their native CFG/FS insertions replace the previous hand-build route. Interfaces stay 1.0 after completion. Preserve completed installed copies before regeneration; no prior build/test status transfers to these templates.

| Additional check | Expected observation | Actual result |
| --- | --- | --- |
| Unfinished template | Both helpers' initial Stop and Output prevents provider/forScore writes before slots are completed | Not run |
| Slot wiring | FS01/03/05/09/12 consumers use the newly inserted native outputs, not deleted Nothing outputs; FS11 uses its own writing loop Repeat Item | Not run |
| File return | Both archive return actions use native Files, not filenames or Text interpolation; saving targets the chosen type Folder | Not run |
| Re-export | Fresh exports restore guards/slots; completed installed helper copies remain available for reapplying insertions | Not run |

Static review on 16 October 2026: all four generated sources' call names and required parameter-slot sets were checked against the pinned compiler lookup table/Parameter files. The two new helpers contain 13 unique FS IDs and four unique CFG IDs; both have an initial stop guard. Delimiter balance was checked outside comments/strings. This is source review only; no compiler, export or device pass is claimed.


16 October 2026, user-reported compilation: archive helper fails at each DoNothing identifier with an out-of-scope error. Archive revision 3 replaces these seven enum arguments with Respond pending manual no-recipient configuration to Do Nothing after export. Corrected build/import/run: Not run.

Archive revision 4, 16 October 2026: user reports out-of-scope FileExtension, FirstItem and archiveMatches. Updated archive to the official documentation's spaced enum forms: property File Extension, type Item at Index with index 1 (equivalent to first item). References: https://docs.jellycuts.com/Documentation/Shortcuts/fileDetail.html and https://docs.jellycuts.com/Documentation/Shortcuts/getItemFromList.html . Leave repeat-result capture unchanged pending recompilation: archiveMatches may be a cascading diagnostic from errors inside its loop. Corrected compilation remains unverified.

## Local documentation review, 16 October 2026

Later archive report: first validation If wrapper is missing from the generated Shortcut, similar to canonical revision 3. Archive revision 6 and service revision 4 replace all unparenthesized If/Repeat Each headers with the forms explicitly documented in the local language guides. Parentheses are a candidate correction, not yet device-confirmed. Compile/export into a fresh project and verify native If/End If and Repeat/End Repeat structure. Retain the intentional unconditional ASSEMBLY GUARD until configuration is complete; retain validation stops inside their conditions. Earlier successful generation does not validate control flow. CFG/FS slots and completed interfaces remain unchanged.

User-confirmed canonical result: after removing the initial unconditional Stop and Output and correcting native input/result connections, the supplied `Fri1-Walsh-Responses.pdf` test worked (expected `Walsh-Responses`). Installed receiving configuration was changed to Text with an error message when there is no input. This confirms that manually adjusted installed fixture, not an untouched revision 4 export or all filename cases. The installed no-input behavior now stops with an error instead of returning empty Text; callers must supply filename Text. Archive and service integration remain untested.

Latest canonical runtime investigation: user confirms input `Fri1-Walsh-Responses.pdf` reaches the helper, but the initial empty Stop and Output is not enclosed by an If in the generated Shortcut. It therefore stops normal execution. Revision 4 removes this guard, retaining two Replace Text actions and the final return. No successful runtime result is recorded yet. Re-test the supplied filename and empty input (with receiving configuration set to continue without input). Preserve native input/result token corrections made in the editor. Inspect all generated control-flow blocks in the larger helpers before their assembly guards are removed.

Later device report: canonical revision 2 fails at line 21 with `sourceName` not in scope. Revision 3 removes `} >> sourceName`, returns empty output immediately for missing input, and feeds ShortcutInput directly to Replace Text. Interface 1.0 and filename patterns are unchanged. Earlier static review did not establish acceptance of block captures in this app. Revision 3 compilation/import/execution: Not run. Recompile/import this utility under the same exact installed name before testing the archive helper. Check `Fri1-Walsh-Responses.pdf` returns `Walsh-Responses`, `Jackson-InGminor.pdf` returns `Jackson-InGminor`, and absent input returns no usable value without running replacements. Archive revision 5 generation is separately user-reported as successful; its configured runtime behavior remains unverified.

Current sources: canonical revision 2, archive revision 5, assembly revision 3, main revision 2; completed interfaces 1.0. Historical records above remain tied to their earlier revisions. The new snapshot identifies the spaced enums still missing from assembly; those are corrected. Archive no longer captures `archiveMatches`: it uses a named native File and stops on a second canonical match. CFG03 must return this named variable after export. Assembly uses Custom with ` | ` for running-order text and documented triple-quoted strings for multiline UI. No compiler/export/import/runtime pass is claimed.

| Regression case | Steps / expected observation | Actual result |
| --- | --- | --- |
| Archive reuse after a match | Existing clean PDF matches source stem. Complete CFG03 with named `existingCleanFile`; File returned, no save/type-folder prompt. Inspect presence checks use that named variable. | Not run |
| Archive miss after previous invocation | Invoke helper for another identity with no archive match. Initial Nothing resets named variable, so choose type folder and save one clean PDF. No stale File reused. | Not run |
| Duplicate canonical archive | Two disposable archived PDFs canonicalize to the same stem. Second match alerts and stops, returns no File, does not save/import or change setlist. | Not run |
| Source enum regression | Compile assembly 3: `File Extension` and all three `Item at Index` calls accepted; each index is `"1"`. Archive 5 has no `archiveMatches` use. | Not run |
| Running-order review | Pick B then A. Confirmation and report show B then A separated by ` | `; multiline UI contains actual line breaks. Confirm native preparedScores order and forScore readback too. | Not run |

Migration: preserve completed installed helpers, re-export archive 5 and assembly 3, reapply native CFG/FS insertions, repair/check named-variable references if necessary, then remove guards. Names and caller contracts are unchanged. Main and canonical were reviewed without source changes. Matching `.txt` transfer copies are refreshed with source. Continue with the whole-service, repeat/repair and cancellation cases above; optional probes are available only for diagnosing a specific compiler/wiring error.

Static validation for this review: 99 action calls across all four sources matched local documentation parameter-slot sets, with the recorded compiler-backed Output exception. Delimiters balanced outside comments/strings, rejected enum spellings were absent from executable production code, all four `.txt` copies matched source hashes, eight canonical-name regex cases passed using extracted source patterns, and 35 local documentation links resolved. `git diff --check` passed. No `jelly`, `jellycuts`, `jellyc` or Swift executable was found on PATH; no compilation, artifact, import or runtime result was produced.
