# V4 - Check or Upload

[Source](../shortcuts/reusable/v4-check-or-upload.jelly) implements the non-forScore parts of shortcut 1 in the [V4 plan](../../nextcloud-forscore-plan-v4.md). Specification revision 2, interface 1.1. No other installed shortcuts or external configuration files are required.

## Input and share sheet

After importing through Jellycuts/Copyover, name the shortcut **V4 - Check or Upload**. In Apple Shortcuts Details, enable **Show in Share Sheet** and accept **PDFs/Files**. Confirm that shared input remains a native File. Enable interactive prompts when running it; this is not an unattended workflow.

- Share one PDF from Files, Nextcloud or another app. The helper uses Shortcut Input directly.
- Launch without input to select one file using Files. It must be a PDF.
- Future service/rehearsal callers run this helper once per PDF. To suppress the displayed report, send a native List with two rows: the actual PDF File token and Text `batch`. Inspect the sender's File token after generation; bare variable names have previously become literal Text in generated Lists.
- Success after native completion returns a native List: row 1 is the actual forScore Score; row 2 is report Text. Controlled early exits return one diagnostic Text beginning `V4-E` or `V4-SETUP`; this is not a Score or success List. Native cancellation/action failures can abort without returning a diagnostic. Callers must distinguish diagnostic Text from a successful native result before adding or opening a Score.

## Locate an early exit in the installed shortcut

Preserve the native forScore actions already added on the iPad. Edit the existing Stop and Output actions in that installed copy using the messages below; regenerating this source would restore the unfilled native slots. Keep each stop inside its current If block. If needed, insert a Text action containing the message immediately before the stop, inside the same If, and set Stop and Output to that Text action's result. Values in brackets below are actual variable tokens, not typed variable names.

In the test caller, temporarily use **Run Shortcut -> Quick Look [the complete Shortcut Result]**. Bypass Get First Item and Open score for this diagnostic run so the early-exit text is displayed directly.

| Stop location / enclosing condition | Diagnostic Text |
| --- | --- |
| Unexpected incoming count (not 0, 1 or 2) | `V4-E01: Unexpected input count. Expected one PDF or PDF plus batch. Received: [incomingCountText].` |
| Second item is not batch | `V4-E02: Invalid second input. Expected Text batch. Received: [reportMode].` |
| sourceFile does not have any value | `V4-E03: sourceFile is empty after input selection. Check the picker or Repeat Item assignment.` |
| pdfCountText is not 1 | `V4-E04: sourceFile must contain one item. Count: [pdfCountText].` |
| lowerExtension is not pdf | `V4-E05: Input is not a PDF. Detected extension: [lowerExtension].` |
| canonicalName does not have any value | `V4-E06: canonicalName is empty after filename cleanup. Original name: [sourceName].` |
| approvedTitle does not have any value | `V4-E07: approvedTitle is empty after the title question. Piece: [canonicalName].` |
| approvedType does not have any value | `V4-E08: No music type was selected. Piece: [canonicalName].` |
| resolvedScore missing immediately after FS02 | `V4-E09: resolvedScore is empty immediately after import. Lookup name: [canonicalName]. Check the FS02 Get score result and its Set Variable connection.` |
| resolvedScore missing before final report | `V4-E10: resolvedScore is empty before the final report and return. Lookup name: [canonicalName]. Check FS01 for reused Scores or FS02 for new Scores.` |

Unfilled template stops also have distinct messages: `V4-SETUP-FS01`, `V4-SETUP-FS02`, `V4-SETUP-FS03-FS05` and `V4-SETUP-FS06`. Do not put those stops back into slots already completed natively. Keep the successful final Stop and Output connected to the native List; it must not be changed to diagnostic Text.

These diagnostics identify a reached guard, not necessarily the underlying fault. If a condition is wired incorrectly, its reported values may contradict the intended condition. Inspect the actual inputs/operator before changing the branch. A native error, cancellation or stop inside a manually added action may still end the run without one of these messages.

## Complete the native comments

Each FS comment deliberately occupies one physical source line, matching this Jellycuts version's Comment generation. No forScore bindings are invented.

| Slot | Native work to insert |
| --- | --- |
| FS01 | Lookup by full cleaned name; resolve ambiguity; assign existingScore and resolvedScore when found. Replace its setup Alert and Stop and Output. |
| FS02 | Import missing PDF; obtain the exact native Score and assign resolvedScore. Replace the following placeholder Stop and Output. |
| FS03 | Apply approvedTitle to the new Score. |
| FS04 | Lookup/create and assign the approved Composer, when supplied. |
| FS05 | Lookup/create and assign the approved music type as Genre; verify the writes. Remove the following setup stop after completing FS03-FS05. |
| FS06 | Return native List [resolvedScore, pieceReport] using native Stop and Output. Replace the final diagnostic setup Stop and Output. |

The incomplete source intentionally stops at FS01. Removing its stop alone does not complete the workflow. Keep all lookup/import/write/return actions in the positions described by the comments; existing Scores must bypass the new-piece prompts and metadata writes. Preserve named-variable assignments and surrounding If blocks. Back up a completed native copy before regenerating from this template.

## Filename and metadata rules

The prefix pattern handles recognised weekday names, optional `am`/`pm`, a numeric position and a hyphen. Unrecognised prefixes remain unchanged. Complete piece identity retains composer, movements and edition qualifiers.

Alphabetic `Composer-Work` names produce editable title/composer suggestions, not confirmed authorship. Numbered NEH/AMR/OH references and explicit Psalm/Psalms names bypass that split. Other conventions can be corrected through the prompts. Unknown composer is entered as `-` and left unassigned. Music types use the complete category list from `config/config.example.json`, copied into this standalone source.

## Validation and manual acceptance

Stage: source reviewed; the manually completed and repaired installed shortcut has a user-reported successful run on 10 November 2026. This does not establish that an unchanged export of this source works or that every acceptance case below has passed. No local build or signing is claimed. The target is the reported Jellycuts 2026.6.4 / iPadOS 26.6 / forScore 15.2.5 setup. Existing project instructions retain the on-device build route.

### Installed input repair confirmed, 10 November 2026

The diagnostic run returned V4-E03: sourceFile was empty after input selection. The user reports successful execution after removing and re-adding the Repeat Item token in the sourceFile assignment and inspecting all sourceFile references, changing their selected type to **File**. Most references had originally been set to **Text**.

For future generation/import, inspect the Set Variable sourceFile action inside the Repeat: its value must be the actual enclosing Repeat Item token. Inspect each sourceFile reference and select **File**, preserving the native PDF rather than a Text conversion. A variable's name alone does not establish either its originating token or selected type. These are confirmed repairs to the installed copy; no source-level guarantee of generated token/type settings is established. Preserve the working native copy rather than replacing it just to update comments or diagnostics.

The precise fixture, launch route and separate lookup/import/metadata/return results were not reported, so broader cases remain pending.

Syntax references are the vendored Shortcuts pages for selectFile, fileDetail, count, changeCase, replaceText, matchText, askForInput, choose, list, setName, alert, nothing, quicklook and output. Use the device-confirmed positional Output form rather than the conflicting older documentation signature. Flush-left bodies, quoted RepeatIndex comparisons and separate If blocks follow existing app compatibility evidence.

Unverified on this complete helper: shared native File reception, optional File/Text List extraction, generated prompt defaults, native Score/List return and forScore slot wiring. Inspect generated variable tokens and numeric/presence comparisons; previously repaired native settings are not guaranteed by generation. No extra diagnostic shortcuts are introduced.

1. Compile/import on the iPad; inspect share-sheet settings, If bodies, Count operands, prompt defaults and named-variable tokens.
2. Before filling slots, share one PDF and confirm filename cleanup reaches the FS01 setup message. Direct launch should offer Files; sharing a non-PDF should stop.
3. Complete FS01-FS06. Share `Tue1-Walsh-Responses.pdf`: check suggestions, choose Responses and verify the exact Score's title, Composer and Genre.
4. Share that PDF again: verify the same annotated Score is reused without metadata prompts or another import, including after the title change.
5. Check a hymn reference, an unfamiliar filename, an unknown composer and an ambiguous existing-score match. Cancelling or skipping must return no usable Score.
6. Call with native [PDF, batch]: confirm prompts for a new piece still appear, completion preview is suppressed, and native [Score, report] reaches the caller.
