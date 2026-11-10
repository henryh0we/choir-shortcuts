# V4 - Check or Upload

[Source](../shortcuts/reusable/v4-check-or-upload.jelly) implements the non-forScore parts of shortcut 1 in the [V4 plan](../../nextcloud-forscore-plan-v4.md). Specification revision 1, interface 1.0. No other installed shortcuts or external configuration files are required.

## Input and share sheet

After importing through Jellycuts/Copyover, name the shortcut **V4 - Check or Upload**. In Apple Shortcuts Details, enable **Show in Share Sheet** and accept **PDFs/Files**. Confirm that shared input remains a native File. Enable interactive prompts when running it; this is not an unattended workflow.

- Share one PDF from Files, Nextcloud or another app. The helper uses Shortcut Input directly.
- Launch without input to select one file using Files. It must be a PDF.
- Future service/rehearsal callers run this helper once per PDF. To suppress the displayed report, send a native List with two rows: the actual PDF File token and Text `batch`. Inspect the sender's File token after generation; bare variable names have previously become literal Text in generated Lists.
- Success after native completion returns a native List: row 1 is the actual forScore Score; row 2 is report Text. Invalid input, cancellation or unresolved setup produces no usable Score result. Native action failures can abort the shortcut. Callers must validate a returned result before adding anything to a setlist.

## Complete the native comments

Each FS comment deliberately occupies one physical source line, matching this Jellycuts version's Comment generation. No forScore bindings are invented.

| Slot | Native work to insert |
| --- | --- |
| FS01 | Lookup by full cleaned name; resolve ambiguity; assign existingScore and resolvedScore when found. Replace its setup Alert and Stop and Output. |
| FS02 | Import missing PDF; obtain the exact native Score and assign resolvedScore. Replace the following placeholder Stop and Output. |
| FS03 | Apply approvedTitle to the new Score. |
| FS04 | Lookup/create and assign the approved Composer, when supplied. |
| FS05 | Lookup/create and assign the approved music type as Genre; verify the writes. Remove the following setup stop after completing FS03-FS05. |
| FS06 | Return native List [resolvedScore, pieceReport] using native Stop and Output. Replace the final empty Stop and Output. |

The incomplete source intentionally stops at FS01. Removing its stop alone does not complete the workflow. Keep all lookup/import/write/return actions in the positions described by the comments; existing Scores must bypass the new-piece prompts and metadata writes. Preserve named-variable assignments and surrounding If blocks. Back up a completed native copy before regenerating from this template.

## Filename and metadata rules

The prefix pattern handles recognised weekday names, optional `am`/`pm`, a numeric position and a hyphen. Unrecognised prefixes remain unchanged. Complete piece identity retains composer, movements and edition qualifiers.

Alphabetic `Composer-Work` names produce editable title/composer suggestions, not confirmed authorship. Numbered NEH/AMR/OH references and explicit Psalm/Psalms names bypass that split. Other conventions can be corrected through the prompts. Unknown composer is entered as `-` and left unassigned. Music types use the complete category list from `config/config.example.json`, copied into this standalone source.

## Validation and manual acceptance

Stage: source reviewed only. No local build, signing, import or device execution is claimed. The target is the reported Jellycuts 2026.6.4 / iPadOS 26.6 / forScore 15.2.5 setup. Existing project instructions retain the on-device build route.

Syntax references are the vendored Shortcuts pages for selectFile, fileDetail, count, changeCase, replaceText, matchText, askForInput, choose, list, setName, alert, nothing, quicklook and output. Use the device-confirmed positional Output form rather than the conflicting older documentation signature. Flush-left bodies, quoted RepeatIndex comparisons and separate If blocks follow existing app compatibility evidence.

Unverified on this complete helper: shared native File reception, optional File/Text List extraction, generated prompt defaults, native Score/List return and forScore slot wiring. Inspect generated variable tokens and numeric/presence comparisons; previously repaired native settings are not guaranteed by generation. No extra diagnostic shortcuts are introduced.

1. Compile/import on the iPad; inspect share-sheet settings, If bodies, Count operands, prompt defaults and named-variable tokens.
2. Before filling slots, share one PDF and confirm filename cleanup reaches the FS01 setup message. Direct launch should offer Files; sharing a non-PDF should stop.
3. Complete FS01-FS06. Share `Tue1-Walsh-Responses.pdf`: check suggestions, choose Responses and verify the exact Score's title, Composer and Genre.
4. Share that PDF again: verify the same annotated Score is reused without metadata prompts or another import, including after the title change.
5. Check a hymn reference, an unfamiliar filename, an unknown composer and an ambiguous existing-score match. Cancelling or skipping must return no usable Score.
6. Call with native [PDF, batch]: confirm prompts for a new piece still appear, completion preview is suppressed, and native [Score, report] reaches the caller.
