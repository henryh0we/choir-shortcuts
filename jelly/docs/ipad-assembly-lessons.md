# iPad assembly repairs and working installed changes

Recorded 23 October 2026 from the user's reports in this conversation. Profile:
Jellycuts 2026.6.4, iPadOS 26.6, forScore 15.2.5; bundled compiler unknown.
This is evidence for the manually completed installed shortcuts, not proof that
freshly generated source preserves the repairs. Later records here supersede
older “Not run” statements for the specific cases described.

## What worked

- Assembly 14 produced duplicate-magic-variable errors for importedScore and
  importedWorkingScore despite single declarations. Assembly 15's complementary
  presence/absence If blocks compiled. The compiler's underlying cause is unknown.
- After native reconnections and condition repairs, a one-score run returned the
  canonical name Humfrey-InEMinor, previewed a clean PDF, populated a setlist with
  InEMinor by Humfrey, passed the repaired count check and opened it in forScore.
- Assigning Create Setlist's native New Setlist output to named targetSetlist
  removed the extra chooser in Create new. The user confirms this works.
- Asking for a service Date, formatting it and combining it with the selected
  service type as the editable name default works in the installed shortcut.

Not established: which score-import catalogue action ran on the successful path,
all metadata branches, two distinct scores, A/B/A repetitions, Replace existing,
cancellation/failure coverage, fresh-source fidelity, or warning-free compilation.
The editor displayed Text on Score collections; the working path demonstrates
successful consumption in that fixture, not a general explanation of the label.

## Repair before running

Use native Select Variable for connections. A typed name or literal interpolation
expression is not a token. For values assigned later, select the named variable,
not its initial Nothing output. Preserve Nothing actions used for initialisation;
replace only marked native-action slots. Replacing an action does not reconnect
its consumers automatically. Check If operator direction as well as its input.

| Area / symptom | Required connection or repair |
| --- | --- |
| No files selected after choosing a PDF | Following If uses actual Select File output and **does not have any value**. Original pieceCount Count and ordering Repeat use that same selected-files output. |
| No piece selected after choosing piece 1 | Set orderedFile from this ordering Choose's Chosen Item; following If uses named orderedFile and **does not have any value**. |
| COL01 / running order incomplete | Inside ordering Repeat, Add named orderedFile to named orderedFiles. Post-loop Count uses named orderedFiles. If compares that Count **is not** original pieceCount. |
| COL02 / preview incomplete | Inside validation Repeat, Add current File Details Name to orderedNames. Post-loop Count and Combine Text use named orderedNames. If compares that Count **is not** original pieceCount. |
| Helper rejected two-item input | In the actual incident the naming call selected Archive. Correct target to Canonical; do not diagnose a transport defect solely from this message. |
| No clean PDF despite correct PDF preview | Get Type, missing-file If and FS02 use the actual archive Run Shortcut result; missing-file If is **does not have any value**. Text-error check uses current archiveResultType equal to Text. |
| SCORE01 / SCORE02 | Get Item from List, index 1, takes its individual FS01 / FS03 lookup result. Set named workingScore from that branch's Item output. |
| No working Score despite a Score being present | Installed condition was **has any value**. Correct it to **does not have any value**, using named workingScore. Source already expressed absence; do not assume generated operator fidelity. |
| Literal `$[readableTitle]` default | In title Ask for Input, delete literal expression and insert preceding readableTitle Replace Text output token. |
| Literal composer default | Insert named composerSuggestion token in composer Ask for Input Default Answer. |
| COL03 / prepared count mismatch | Add named workingScore to named preparedScores at end of preparation Repeat, outside metadata Ifs. Post-loop Count uses named preparedScores; If compares its result **is not** pieceCount. |
| Final writing Repeat | Uses named preparedScores. FS11 consumes this Repeat's native Repeat Item, targetSetlist, Skip if already added off. |
| Readback mismatch with a populated setlist | FS12 gets targetSetlist entries, Sorting Manual. actualCount counts FS12 Entries; requestedCount counts named preparedScores. If compares those two Count outputs using **is not**. User reports reconnections fixed this. |

Equal counts do not verify identity or order. Inspect the actual Manual setlist.
When an error follows file/metadata/setlist writes, inspect state before retrying.

## Installed shortcut names and input contracts

Temporary installed names used during this session:

| Caller / target | Input and output |
| --- | --- |
| Test caller -> 2-util-assemble-choir-service | Literal Text interactive -> service report Text, or error |
| Assembly -> 2-util-canonical-choir-name | Two-item List: filename Text, prefixRegex Text -> canonical stem Text |
| Assembly -> 2-util-archive-choir-pdf | Three-item native List: current PDF File, libraryRoot Folder, workflowConfig Dictionary -> PDF File or error Text |
| Archive -> 2-util-canonical-choir-name | Same two-Text naming contract; inspect both internal naming calls |

These are installed aliases, not repository-wide renames. Select the correct
installed helper in every Run Shortcut and explicitly select the corresponding
List output. Counting rows establishes cardinality, not native item types.

FS09 exposed In Library options Variables, Current Library and Empty. Empty was
the user's separate test library, not a blank setting. Current Library was chosen
for this run; blank behaviour and switching libraries remain unverified. Keep
lookup/setlist actions consistent with the intended library. FS09 Sort Order Title
is for choosing setlists; FS12 Manual is for reading service entries.

## Preserve the working Create new flow

The committed executable template still retrieves and chooses a setlist for both
modes. Reapply this user-tested native change after regeneration:

```text
If setlistMode is Create new
    Create Setlist named serviceName
    Set variable targetSetlist to New Setlist [native action output]
Otherwise
    Get all setlists [FS09]
    Choose from List [FS09 output]
    Set variable targetSetlist to Chosen Item
End If
If named targetSetlist does not have any value
    Stop and Output error
End If
Apply running order confirmation
```

Reconnect validation and FS10-FS13 to named targetSetlist, not the old chooser
output. Keep clearing inside Replace existing, after score preparation and the
confirmation. This working native Otherwise is not evidence that Jelly's source
Otherwise compilation defect is fixed.

## Preserve the working date/name flow

Between building runningOrder and the existing service-name question, add:

1. Ask for Input, type Date: “What date is the service?”
2. Format that input date with custom `yyyy-MM-dd - EEE`; use English (UK) locale
   where available for Thu/Fri abbreviations.
3. Text with actual Formatted Date and selectedServiceType tokens, separated by
   ` - `, for example `2026-10-23 - Fri - Evensong`.
4. Existing Ask for Input, type Text: “Confirm the service name.” Default Answer
   is the preceding Text token. Remove literal `""` or interpolation placeholders.
5. Keep the existing trim action; its entered-name input and serviceName consumers
   must be reconnected as necessary.

Flow: service type -> select PDFs -> running order -> service date -> editable
service name -> confirmation -> score preparation -> create/replace setlist.
Date affects naming, not archive identity or score metadata. Replace existing
does not rename its selected setlist. Date actions and direct New Setlist capture
are recorded native edits; no guessed Jelly bindings have been added for them.

## Debug a boundary before changing implementation

Insert Quick Look directly after each Run Shortcut using that specific action's
result token: naming should show stem Text; archive should preview a PDF. Show
Get Type output if needed. Preview a named variable immediately before its failed
If and show both Count operands before a count failure. Verify the operator.
Do not let diagnostics replace downstream inputs with implicit Quick Look output.
Remove diagnostics after verification. Back up the completed installed shortcuts
before regeneration; regenerated sources restore guards and placeholders.

Next experiments: [iPad Jellycuts test questions](../tests/ipad-investigation/README.md).

## Repository checks for the documentation update

Assembly revision 16 changes comments/header only; executable lines match the
previous source, and its .txt transfer copy is byte-identical. The required build
command was run on 23 October 2026 through WSL:
`python jelly/scripts/build.py jelly/shortcuts/reusable/util-assemble-choir-service.jelly`.
The older pinned compiler rejects core/control-flow nodes and positional Output
parameters, as previously recorded. No accepted local export was produced, and
no new iPad execution was performed for the annotated revision. New investigation
tests remain a plan, not newly executed evidence.
