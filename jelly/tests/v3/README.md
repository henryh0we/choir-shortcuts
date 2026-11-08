# V3 first manual iPad checkpoint — filenames

Next source delivery: [Stage 2B dated/grouped/ordered service preview](stage-2b-services.md). Revision 1 crashed in editor loading and at Compile Jelly Text; revision 2 splits the workflow into smaller installed helpers and has no successful device result yet. Start with its renderer-only compilation checkpoint. Working filename shortcuts are unchanged; the evidence below remains the Stage 2A record.

Status: **The current filename-preview checkpoint has reported passes for its working paths, report cleanup, saved config, Thursday aliases, conflicting rules and wrong config version. Normal config is restored.** Ready to begin the date/order increment; unknown-prefix/non-PDF results and broader matrix cases remain unconfirmed rather than implied passes. No local compilation or automated/runtime tests were performed. [Contracts and known limits](../../docs/v3-development.md) apply.

## Reported pass: conflicting rules and wrong config version, 8 November 2026

Using the supplied configs, the user reports (1) unresolved with Multiple configured rules matched and (2) the expected error for the unsupported version. The user confirms the normal config is restored. Record both targeted checks as passes, without assuming an exact full report or source hash. No source/config repair is needed. This supersedes older pending statements for these checks below.

The next implementation increment is read-only folder-date resolution, service grouping and numeric position ordering, using the real single-date/range examples. Unknown-prefix/non-PDF checks can be carried into its manual matrix; no additional broad diagnostic cycle is required before construction.

## Reported pass: Thu and Thurs aliases, 8 November 2026

Following the requested Thu1-Piece.pdf and Thurs1-Piece.pdf checks, the user reports that both work as described. Record both as Thursday Evensong passes. The same message does not separately identify the unknown-prefix or non-PDF results; leave those unconfirmed rather than infer a pass. Next are overlapping-rule and unsupported-version checks using a disposable config copy, followed by restoration of the normal config reference. No source change is required.

## Ready-made config files for the remaining checks

The user cannot edit JSON on the iPad. All future config changes must be prepared in the repo as complete copy/paste files for Copyover. These files supersede instructions below to edit individual config values/rules manually. Transfer JSON contents as config data, not as Jelly Shortcut source.

1. Copy [conflicting-rules config](../../config/v3-config.test-conflicting-rules.json) through Copyover into a separate JSON file in Files. Point V3-CONFIG-FILE at it and select a Tuesday PDF. It is the normal version-3 config plus a second matching Tuesday rule with distinct key tue-conflict. Expected: unresolved rather than a guessed service.
2. Copy [wrong-version config](../../config/v3-config.test-wrong-version.json) through Copyover into another separate JSON file. Point V3-CONFIG-FILE at it and run. It contains the normal rules, without the conflict, but top-level version 2. Expected: config error before the music picker.
3. Restore V3-CONFIG-FILE to your normal v3-config.json. If a fresh normal copy is needed, use [the normal config](../../config/v3-config.example.json), with version 3 and Monday off.

No source rebuild is needed. These are prepared fixtures, not reported test passes. No local builds or tests were run.

## Reported pass: saved config persistence and rereading, 8 November 2026

The user confirms the requested saved-config check works: rerun without selecting config again, temporarily enable Monday in the saved config, rerun the same Monday PDF expecting parsed, then restore Monday to off. This establishes persistence and rereading for the reported installed setup. No source change is needed. It does not establish moved/deleted config recovery, remaining Thursday aliases, overlapping rules, invalid config versions or raw return-type inspection.

Next: finish the remaining alias/invalid-input checks in the checkpoint-finalisation list below. Dates, grouping and numeric ordering remain the following implementation increment. This result supersedes older pending saved-config statements below.

## Reported pass: revision 6 report cleanup, 8 November 2026

After the revision-6 replacement delivery, the user confirms that it ran correctly, the output looks good, Monday files are skipped and the quote marks are gone. This confirms the cleanup and Monday exclusion in the reported run. No source change is needed from this result. Exact selected files/count, source hash, app versions, native repair history, saved-config repeat-run persistence and config/error cases were not supplied; do not infer those passes. Raw helper return type and preview output to a separate caller remain uninspected.

Next checkpoint action: run again without reselecting config, then temporarily change Monday enabled from off to on in the saved config, rerun the same Monday PDF and expect parsed, and restore off. Continue the remaining alias/invalid-input checks below before marking full Stage 2A acceptance complete. The revision-6 preparation notes below describe the pre-result source review; this newer report supersedes their untested status only for the observed behavior.

## Current replacement: preview revision 6, checkpoint finalisation

Replace only **V3 - Preview Filenames** using [the updated source](../../shortcuts/main/v3-preview-filenames.jelly) through Copyover. Keep **V3 - Parse Filename** revision 3/interface 2.0 and your existing version-3 config. Preview interface remains 3.0. Complete V3-CONFIG-FILE again after fresh import using the saved-config setup below; confirm Run Shortcut still targets V3 - Parse Filename.

Revision 6 preserves the tested selection, parsing and report accumulation. A final Replace Text removes only whole lines containing two double quotes with optional spaces, before Quick Look and the final Text return. Blank lines may remain. Quotes within field values are preserved. This is a targeted presentation cleanup, not a proven diagnosis or repair of the compiler's multiline-string handling. The binding is backed by the pinned Replace Text documentation and existing parser usage; this revision is source-reviewed only.

Inspect V3-PREVIEW-CLEANUP: Replace Text must consume the current named report, with Regular Expression enabled and an empty replacement. Its result must set report, which feeds both Quick Look and final Get Text. The generated Find field must contain `(?m)^ *"{2} *$` (the source escape before the quote must not become report content).

Finish this checkpoint on the iPad:

1. Repeat the reported Sunday/Monday four-file selection, plus Thur and SunRemem. Confirm one row per file, unchanged parsed fields, Monday skipped and no standalone quote-pair lines. Report should still state that dates/sorting are absent.
2. Run again: only the music picker should appear, using the same saved config. Edit a recurring schedule switch in that config, rerun and confirm the changed status; restore the original value afterwards.
3. Cover the remaining Thursday aliases Thu/Thurs, an unknown prefix, a non-PDF selection and an edition-qualified payload. Unknown/non-PDF rows must be unresolved and qualifiers preserved. Provider order remains intentional.
4. Using a disposable config copy, test an overlapping rule (unresolved, no guessed service), then valid JSON with version 2 (error before music selection). Restore the normal config reference. Malformed JSON/regex can abort natively; no recoverable-error guarantee is claimed.

Record the installed revision, any native repairs and the resulting report. Revision 6 now has the reported cleanup/Monday pass above; saved-config and remaining config/error results are still needed for full Stage 2A acceptance. The broader matrix below remains available for additional cases.

## Reported pass: SunRemem special service, 8 November 2026

The user reports picker count 1 and this result:

```text
FILE: SunRemem1-NEH485-ThyHandOGodHasGuided
STATUS: parsed
DAY / SLOT: sun / special-remem
SERVICE: Remem
POSITION: 1
CANONICAL: NEH485-ThyHandOGodHasGuided
REASON: Recognised special suffix; date overrides are not yet applied.
```

This passes the special suffix fallback for SunRemem: readable service name Remem, lowercase stable slot special-remem and intact hymn-number/title payload. Standalone quote-pair lines remain in the displayed report. The exact installed revisions, source hashes, versions and native setup/repairs were not supplied. This does not establish other special suffixes, case-variant identity, disabled-day specials, actual service identity across reruns or dated overrides. No source change follows from this successful fixture.

## Reported pass: Thur alias, 8 November 2026

The user reports picker count 1 and the following row:

```text
FILE: Thur1-Rose-Responses(SATTB)
STATUS: parsed
DAY / SLOT: thu / evensong
SERVICE: Evensong
POSITION: 1
CANONICAL: Rose-Responses(SATTB)
REASON: Recognised regular service; filename position is not yet sorted or date-resolved.
```

This passes the Thur alias and voice-qualifier preservation for this fixture. The report still contains standalone quote-pair lines. It does not establish the other Thursday aliases Thu/Thurs, special suffix handling, ordering or dates. Exact installed revisions, hashes, app versions and native setup/repairs were not supplied for this attempt. No source change is needed from this result.

## Reported pass: four-file Sunday and Monday preview, 8 November 2026

The user supplied one report with Music picker item count: 4 and these four rows, in the displayed order:

| Source Name | Status | Day / slot | Service | Position | Canonical payload |
| --- | --- | --- | --- | --- | --- |
| Sunam1-Rose-Responses(SATTB) | parsed | sun / mattins | Mattins | 1 | Rose-Responses(SATTB) |
| Sunpm4-Sumsion-InG | parsed | sun / evensong | Evensong | 4 | Sumsion-InG |
| Mon3-Ps119vv49-64 | skipped | mon / evensong | Evensong | 3 | Ps119vv49-64 |
| Sun11-Ps150-Talbot | parsed | sun / eucharist | Eucharist | 11 | Ps150-Talbot |

Each parsed row reports recognised regular service, not sorted/date-resolved. Monday reports Day disabled by configuration. These match the supplied defaults. Four selected items produced four distinct report rows; Sunday session separation, disabled Monday, multi-digit position extraction, voice qualifier and psalm verse-range preservation passed for this fixture. This is not numeric sorting evidence: the preview explicitly retains provider order.

Standalone quote-pair lines still surround report sections. No Notes UI or false no-selection error was reported in this attempt. The report arrived after the revision-5 saved-config change, but the user did not explicitly confirm the consumed revision, native File setup, repeat-run config persistence, versions, hashes or other repairs. Attribute this as a reported four-file runtime pass without assuming those missing details. Parser raw native return type and final preview-to-another-caller output remain uninspected.

No code change is made from this successful report. Next: special suffix, Thursday aliases, then config-only changes/conflicting-rule and invalid-input cases. The full matrix remains incomplete, and dates/ordering are separate implementation increments.

## Current setup: preview revision 5, saved config File

Requested change: choose config once in the shortcut editor rather than at every run. Replace only Preview Filenames with revision 5/interface 3.0; Parser remains revision 3/interface 2.0 and config version stays 3. No new parser install is needed. Revision 5 has no separately source-linked compilation/runtime result; the earlier Friday pass belongs to the revision-4 attempt, and the later four-file report does not explicitly identify its consumed revision.

After import, find **V3-CONFIG-FILE** near the top:

1. Replace its immediately following Nothing with the native **File** action, not Select File.
2. Tap the empty File field and choose your existing **v3-config.json** once.
3. Set the following missing-value If and Get Text from Input to that File action's actual output token; then delete only the placeholder Nothing. The missing-value If must say does not have any value.
4. Run twice and confirm only the music picker appears, using the same config both times. The config is reread each run, so editing its contents should affect the next run without selecting it again. A provider-moved/deleted config reference may need reselection in the editor; no path recovery is assumed.

This is one native config-reference setup action, explicitly requested by the user, not a return/stop workaround. The pinned file(file:) binding is labelled macOS and requires a Variable; it does not establish a valid empty iPad reference. The source therefore uses an explicit native completion slot rather than guessing an empty File call. Recompiling recreates the slot, so set it again after a fresh import. Do not execute the incomplete template expecting a runtime config picker; it reports a setup error if the placeholder remains.

## Reported pass: Friday filename, 8 November 2026

After the preview revision-4 selection change, the user reports Music picker item count: 1 and this result for Fri1-Clucas-Responses:

```text
FILE: Fri1-Clucas-Responses
STATUS: parsed
DAY / SLOT: fri / evensong
SERVICE: Evensong
POSITION: 1
CANONICAL: Clucas-Responses
REASON: Recognised regular service; filename position is not yet sorted or date-resolved.
```

The pasted report also includes standalone double-quote pairs before/between/after report sections. These are observed display artifacts; the multiline string delimiters are a candidate cause, not a proven compiler diagnosis. The parsed fields match the expected single-file result. Keep the working revision-4 flow unchanged while recording this pass; cosmetic cleanup must not be conflated with parsing correctness.

This is a reported integration pass for file selection, config/name Text transport, parsing and a Dictionary-compatible result decoded by the caller, plus report accumulation/display. It does not independently establish the raw return object's native type, the final preview result returned to a separate caller, full generated-action correctness, current app versions, exact consumed hashes or repair history. The intended source pair is parser 3 / preview 4; the user has not separately confirmed installed source identities. No new Notes UI or no-selection error was reported in this result. Do not extrapolate to multiple files, Sunday mappings, exclusions, malformed config or dates.

Next device checkpoint: select several PDFs in one run (including Sun, Sunam, Sunpm and a Monday example where available). Confirm picker count, one row per selected file, configured Sunday slots, Monday skipped, distinct canonical payloads and no rows lost during report accumulation. Then run the existing config-edit/conflicting-rule/error cases below. No recompile is needed for this matrix.

## Selection correction: preview revision 4 (8 November)

The user selected config and fri1-Clucas-Reponses, but revision 3 reported no music selected. This identifies the pre-parser selection guard as the reported failure path; the actual native connections/operator and consumed revision remain unconfirmed. It does not establish that the picker returned no File or that the parser ran.

Preview revision 4 removes the Nothing-initialised selectedFiles assignment and the selectedFiles missing-value guard. Count and Repeat now consume the original Select File output directly, in the same guarded scope. The empty-selection check compares Count converted to Text with literal 0; a nonempty preview includes Music picker item count. This correction is source-reviewed only, not compiled or executed.

**Replace only V3 - Preview Filenames with revision 4.** V3 - Parse Filename remains revision 3/interface 2.0; config is unchanged. No manual blocks are required. Recheck the same file. Expected picker count is 1, followed by either the parsed row or a more specific downstream error. The supplied spelling Reponses is preserved as part of canonical Clucas-Reponses; it is not the cause of an empty-selection message.

If this still fails, inspect the music Select File, Count, count-to-Text and following If: Count must use the picker output, If must be selectedFileCountText **is 0**, and Repeat must use the same picker output. Capture those adjacent generated actions, rather than changing parser rules. Native cancellation may still abort without a report.

## Return strategy: introduced in revision 3, no manual stop blocks

The user identified the revision-1 output calls as Move Notes to Folder. Revision 2's bulk native-stop proposal was rejected. **Do not add its 27 blocks.** Revision 3 uses error-state gates and normal completion with a final Dictionary/Text action. Read the [history review and focused checkpoint](../../docs/v3-output-resolution.md).

Current pair: parser revision 3 and preview revision 4, with parser interface 2.0 and preview interface 2.0. Parser schemaVersion is now Text 2 and controlled failures return status=error in the same Dictionary shape. No generated output/exit calls or manual stop slots remain. This source-level solution has not been compiled or executed; first confirm the final Dictionary reaches the actual caller.

## Reported first attempt: unexpected Notes selection

The user selected the config, then a file named Fri1-Clucas-Responses. A Notes folder picker appeared, followed by a notes list with Cancel/Done. Selecting a note and Done opened it and immediately prompted for a Notes folder again. No filename report or successful parser result was reported. The user referred to Parse Filename, but the config/music pickers belong to Preview Filenames in source; actual installed names, Run Shortcut target, source revisions, generated actions, versions and repair history remain unconfirmed.

Neither V3 source intentionally calls Notes. The follow-up identifies output-to-Move-Notes generation as the failing boundary; its internal compiler cause remains unknown. Repeated prompts do not establish recursion or an infinite loop. Keep this failed observation separate from any later repair/pass; the matrix below remains unverified.

## Install this delivery

1. Copy [v3-config.example.json](../../config/v3-config.example.json) into Files as **v3-config.json**. Use a separate file; leave the old config alone. Its location is your choice for this first preview.
2. For a fresh install, transfer [v3-parse-filename.jelly](../../shortcuts/reusable/v3-parse-filename.jelly) through Copyover and compile on the iPad. Confirm the installed name is exactly **V3 - Parse Filename**.
3. Inspect the generated helper before running it. Then transfer [v3-preview-filenames.jelly](../../shortcuts/main/v3-preview-filenames.jelly), compile and install as **V3 - Preview Filenames**. Complete the single V3-CONFIG-FILE slot above. Check its Run Shortcut action targets **V3 - Parse Filename**.
4. No old shortcut, library helper or forScore action is needed. Record Jellycuts/iPadOS versions and all warnings/errors. If compilation fails, keep the first diagnostic and its source line; do not try multiple invented enum spellings.

These sources each begin with the exact installed name for Copyover. No `.txt` source copy is needed. Do not run the helper alone expecting a preview: it requires its two Text arguments, supplied by the preview shortcut.

## Inspect generated actions first

- Helper extraction: two incoming Text items, quoted Repeat Index comparisons 1/2, config from the second item. Dynamic caller List items must be actual sourceName/configJson variable tokens.
- Rule Repeat: Dictionary key reads from its Repeat Item; Match Text uses that rule's pattern. Inside its match If, **Add to Variable** appends ruleKey to named matchedRuleKeys. Following Count uses the current named collection. Keep its Nothing initializer.
- Operators: missing value means **does not have any value**; present means **has any value**. Counts are converted to Text and compared to quoted 0/1/2. Inspect the actual native operators and both operands.
- Regex Replace actions: replacement fields are literal `$1`, `$2`, `$3`; input and find fields are actual filenameStem/selectedPattern tokens. The suffix lowercase action must say lowercase; its input is capture 1, while the readable name keeps its original case.
- Result chain: each Set Dictionary Value consumes the previous Dictionary and actual Text tokens. The final Get Dictionary consumes finalResult and is the last executable action outside all If/Repeat blocks. Caller must receive schemaVersion 2 and status/reason. No manual return action is required.
- Preview: Name and File Extension read the current selected native File; File Extension must be the real detail, not a literal word or wrong default. Run Shortcut returns the helper result; key reads use that result. Quick Look and final Get Text must read current named report after the Repeat, not its initial heading.

If one of these is wrong, record the untouched export before editing. Generation inspection points have stable `V3-...` comments at the relevant source actions.

First use the focused Fri1-Clucas-Responses and invalid-config checks in the [output resolution](../../docs/v3-output-resolution.md#manual-ipad-check-without-inserting-blocks). In particular, verify runState gates later phases after an error and every cross-phase consumer reads its current named variable. The broader checks below remain pending.

## Run the smallest useful case

Launch **V3 - Preview Filenames**. With the saved config File configured, select one PDF named `Tue1-Walsh-Responses.pdf` (a disposable renamed copy is sufficient because this increment only reads its name).

Expected: one report with parsed status, day tue, slot evensong, service Evensong, position 1 and canonical Walsh-Responses. File name details may omit `.pdf`; that does not change canonical output. No archive or forScore changes.

If this fails, report that first boundary before trying the wider matrix. In particular, an empty/wrong result may be a caller List, Dictionary mutation or return-token problem. A successful compile is insufficient.

## Check the remaining cases

Use actual PDFs or disposable copies renamed in a small Files folder. Select several in one run. Expected rows are independent of picker order; this increment does not sort. The examples below describe expected results, not measured outcomes.

| Filename | Expected result with supplied defaults |
| --- | --- |
| Tue1-Walsh-Responses.pdf | parsed; tue / evensong; position 1; Walsh-Responses |
| Sun1-Walsh-Responses.pdf | parsed; sun / eucharist; Eucharist |
| Sunam2-Smith-TeDeum-EditionB.pdf | parsed; sun / mattins; position 2; Smith-TeDeum-EditionB |
| Sunpm10-Harris-Anthem.pdf | parsed; sun / evensong; position 10; Harris-Anthem |
| SunRemem1-Piece.pdf | parsed; sun / special-remem; readable name Remem |
| sunREMEM1-Piece.PDF | parsed; sun / special-remem; readable name REMEM, same slot |
| Thu2-Piece.pdf; Thur2-Piece.pdf; Thurs2-Piece.pdf | Each parsed as thu / evensong, never special-rs or a conflict |
| ThursRemem1-Piece.pdf | parsed; thu / special-remem |
| ThuRemem1-Piece.pdf; ThurRemem1-Piece.pdf | unresolved; shorter Thursday special aliases need an explicit boundary convention |
| Mon1-Piece.pdf | skipped; mon / evensong; day disabled |
| WedRemem1-Piece.pdf | skipped; wed / special-remem; day disabled |
| Wed1-Piece.pdf | unresolved; no regular Wednesday rule; do not guess a service |
| Sun0-Piece.pdf; Sun01-Piece.pdf; Sun1-.pdf | unresolved; initial convention rejects zero, leading zero and empty payload |
| Unprefixed-EditionB.pdf | unresolved; empty parsed fields |
| Tue1-Piece.txt | unresolved non-PDF row from the caller |

Then edit only a **disposable copy** of the config and select that copy:

1. Turn Sunday mattins enabled to off: Sunam is skipped while Sunpm remains parsed.
2. Add a new nonoverlapping rule for `Tue_1_Piece` using the same three captures: `^(Tue)_([1-9][0-9]*)_(.+)$`, dayKey tue, slotKey evensong, special off, unique key. Old and new names should both parse without source edits.
3. Duplicate a matching rule under another unique key: the affected name is unresolved due to multiple matches, with empty parsed fields. Other names continue.
4. Change version to 1: the caller reports an error before music selection/processing. Malformed JSON or malformed regex can stop natively; capture the actual error without claiming a returned report.
5. Cancel the initial explanation and music picker in separate launches; revision 5 has no runtime config picker. Native picker cancellation may exit immediately. Confirm no music or forScore writes.

## Result record

| Checkpoint | Result |
| --- | --- |
| Helper compilation and generated-action inspection | Not run |
| Preview compilation and target/List inspection | Not run |
| One-file parser/caller/report path, parser 3 + preview 4 intended | Reported pass: Fri1-Clucas-Responses; quote-line artifacts; raw native type not independently inspected |
| Filename/schedule matrix and qualifier preservation | Reported partial pass: Sunam/Sunpm/Mon/Sun, Thur and SunRemem fixtures; remaining aliases, configuration/error and other cases pending |
| Config-only format change, exclusions and overlap | Not run |
| Invalid config and cancellation | Not run |

Send back the source revision (parser 3, preview 5), actual installed names, app versions, first error if any, any unexpected generated actions and actual preview rows. No bulk manual stop completion is part of revision 3. Please also supply one or two actual week-folder names for the next date-parsing increment; dates are deliberately absent here.
