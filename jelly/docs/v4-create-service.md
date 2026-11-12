# V4 - Create Service

[Jelly source](../shortcuts/main/v4-create-service.jelly). Revision 2, interface 1.0. Depends only on your working **V4 - Check or Upload**, with FS06 returning a native List [Score, report Text] and the optional second input Text `batch`. Keep your completed native copies; use the in-place edits below rather than regenerating over them.

## Update the working installed shortcut

### Suppress per-piece completion reports

Inside the file-processing Repeat, immediately before Run Shortcut, add a native List with exactly two rows:

1. The actual `currentFile` File token (or the enclosing PDF Repeat Item), typed **File**.
2. Literal Text `batch`.

Change Run Shortcut's input from currentFile to that List action's result. The helper still receives one PDF, plus a separate mode item. In Check or Upload, confirm its incoming second item assigns named reportMode and that the final report Quick Look is inside **If reportMode is show**. Keep the successful FS06 List/return outside that If so batch mode still returns the Score and report. Remove temporary unconditional Quick Look diagnostics once the working path is verified. New-piece metadata questions and real errors remain visible; standalone use still shows its report. File/Text List transport and the helper's second-item assignment need inspection on device, especially given the previous Repeat Item/File type repairs.

### Append in received order

Leave **Add to Variable preparedScores: helperScore** inside the PDF loop, once per PDF, outside any new-piece-only condition. An existing library Score and a newly imported Score must both be collected at their input positions.

Replace the single bulk Add Scores to Setlist action with:

```text
Repeat with each item in preparedScores
    Add Scores [this Repeat Item] to Setlist [targetSetlist]
        Skip if already added: ON
End Repeat
```

This requests sequential appends in the received sequence; verify actual order using the setlist's Manual order. Do not sort the Score collection or process existing and new pieces separately. A Score that already exists in the library is still added at its selected position if absent from this setlist. A Score already in this setlist keeps its position under the existing additions-only policy. Reordering already-present setlist entries is a separate change requiring a tested native reorder/rebuild path; no clearing actions are introduced here.

The share sheet/Files provider determines the incoming sequence, which may differ from the order of taps. This implementation preserves that sequence; it cannot recover tap order discarded by the provider. If the provider does not preserve the intended order, an explicit order picker is needed before preparation.

### Current installed evidence

On 12 November 2026 the user reports that the creator loops through all files and works after opening forScore and rerunning it. The preceding New Setlist failure reported forScore quitting unexpectedly. This records the observed recovery, not proof that foregrounding is a required fix or an established crash cause. Exact return-extraction repairs and the full test matrix were not independently recorded. Revision 2's batch input and sequential-append changes are not yet device-tested.

## Setup

Compile/transfer through Copyover and install as **V4 - Create Service**. Enable **Show in Share Sheet** and accept PDFs/Files. No incoming files opens Files with multiple selection enabled. Selection and helper input references must be typed **File**, preserving actual File tokens. Reselect enclosing Repeat Item tokens if generation produces empty assignments, as required by the working helper.

Complete the following native slots in Apple Shortcuts. Each source comment gives the exact insertion position and placeholder to replace.

| Slot | Actions |
| --- | --- |
| DATE01 | Replace its Nothing with Ask for Input (Date), Format Date (custom `yyyy-MM-dd - EEE`, English UK locale, London timezone where exposed), then Set Variable serviceDateLabel to that formatting result. Keep its subsequent missing-date diagnostic guard. |
| SFS01 | Replace its setup stop with Get setlist named setlistName (Continue if not found ON), then Set Variable targetSetlist to its native result. Resolve duplicate-name matches with selection or stop. |
| SFS02 | Inside the missing-target If, replace its setup stop with Create Setlist named setlistName, then Set Variable targetSetlist to the new native Setlist. |
| SFS03 | Inside Repeat preparedScores, replace its setup stop with Add Scores to Setlist: Scores=this Repeat Item, Setlist=targetSetlist, Skip if already added=ON. |
| SFS04 | Replace its setup stop with Open setlist targetSetlist. |

These comments produce insertion instructions, not executable forScore actions. The uncompleted source stops with a diagnostic rather than claiming a completed service.

## Behaviour and limitations

The creator validates PDF extensions, asks for date and service type, then passes [PDF File, batch] to Check or Upload for each piece. Per-piece completion previews are suppressed. Other service type allows a custom name. The setlist name is, for example, `2026-11-12 - Thu - Evensong`.

The creator requires a two-item helper result before extracting its Score. Empty/diagnostic results are previewed and stop the run. Native object type/preservation still needs inspection: two items alone cannot prove correct identity or a genuine Score. The helper's completed FS06 is responsible for returning that native Score.

Prepared Scores are collected before any setlist actions. A failed preparation may leave Scores already imported by earlier helper calls, but the creator has not yet changed a setlist. Native failures during setlist creation/addition can leave partial results; retry uses the same exact setlist name and skips already added Scores. Duplicate-name setlists need explicit selection rather than an arbitrary first match.

This version preserves the supplied file sequence and requests one append per Score in that sequence, while preserving existing setlist order. There is no automatic filename-position sort or running-order editor yet. Inspect actual Manual order in forScore. Deliberately repeated occurrences of one Score are excluded by the skip-duplicates policy.

## Source review and manual checks

Revision 2 changes are source reviewed only; no local build or device pass is claimed for these changes. The prior installed version has the user-reported working run described above. Profile: reported Jellycuts 2026.6.4, iPadOS 26.6, forScore 15.2.5. Native date formatting follows the recorded working assembly flow; no unverified date bindings were added. Other forms follow the vendored Shortcuts references and existing app evidence. Get First Item replaces the nested result-extraction Repeat based on the manual troubleshooting guidance; fresh generated token/type settings still need inspection.

1. Inspect File types, both Repeat Item assignments, the exact Run Shortcut target, named variables after assignments, and the COL01 Add to Variable action. It must append each native Score rather than replacing the collection or appending Text.
2. Use two existing PDFs first. Verify the helper returns both intended Scores and the new setlist receives both in the inspected order. Check the selected date's weekday and English abbreviation.
3. Run the same pair again with the same date/type. Confirm the same setlist is used, no duplicate entries appear and manual changes are preserved.
4. Add a new PDF alongside an existing one. Confirm only the new piece needs metadata and both resolve to the intended Scores.
5. Check direct launch and sharing multiple PDFs. Check Other service type. On a diagnostic return, preview the creator's complete result rather than trying to open it as a Score.
6. With a new test setlist, select A (already in library), B (new import), C (already in library) in the intended order. Verify the received file sequence, preparedScores sequence and resulting Manual entry order agree. No per-piece completion reports should appear; B's metadata questions should still appear.
7. Verify batch mode returns two items even though it does not show the report. Confirm standalone Check or Upload still displays its report. On an existing setlist, verify existing entries retain position and only missing entries append.
