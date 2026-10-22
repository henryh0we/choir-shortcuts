# Conditional input connection audit

23 October 2026: installed Assembly failures confirmed that checking a source
condition is insufficient. The workingScore error branch used **has any value**
and needed **does not have any value**; several Count and collection consumers
worked after native reselection. Read [the current repair record](ipad-assembly-lessons.md)
for actual outcomes and the [iPad test plan](../tests/ipad-investigation/README.md)
for isolated polarity/reference tests. Old line numbers and “unverified” statements
below are historical; the completed one-score fixture now opens its setlist.
Fresh-source fidelity and full regression coverage are still unverified.

Assembly 13 scope review: rootChildName, lowerExtension and canonicalStem now use
named variables declared before the corresponding Repeat, with distinct Result
captures assigned immediately before conditional use. Inspect both Set Variable
inputs and current named-variable condition tokens. These are source fixes using
the established pattern, not a new full-device pass; see [the pre-install audit](pre-install-audit.md).

21 October source update: Canonical 11 / Archive 14 / Assembly 13 / Main 4.

Canonical 11 retires NAME01/NAME02 after the user's successful incoming-List
Text extraction test. Inspect both `RepeatIndex == "1"` / `"2"` conditions and
their named filename/prefixRegex assignments inside the loop, plus downstream
presence checks and Text/replacement inputs using the current named variables.
The complete naming helper remains unverified on the device for this revision.
The line-number tables below are the 19 October snapshot, not current line
locations. See [the pre-iPad review](pre-ipad-review.md). New assembly conditions
to inspect: orderedFile has no value (current named variable assigned this
iteration), orderedCount/orderedNameCount differ from pieceCount,
workingScore has no value, metadataMode has no value after assignment,
preparedCount differs from pieceCount (outside the preparation loop),
setlistMode/targetSetlist have no value, and actualCount differs from requestedCount.
Count inputs must use current populated collections; targetSetlist uses the actual
Choose output. These checks are not confirmed device runtime results.

19 October 2026. User confirms archive reuse now returns the correct existing File after reconnecting the post-search If input to named existingCleanFile. This demonstrates one wrong exported/native reference; it does not prove all If conditions fail. Current source cannot reveal the actual installed Magic Variable UUIDs or native edits. Audit priorities below are candidates for inspection, not additional confirmed bugs. Do not regenerate a working installed shortcut solely to inspect these connections.

For named variables updated later, select the named variable rather than the initial empty Nothing or an earlier action output. For replaced Nothing slots, reconnect every consumer to the replacement action. For comparisons with another value, inspect both operands and use actual variable tokens rather than literal variable names.

## All source conditions

### util-archive-choir-pdf.jelly

| Source line | Condition | Reference to inspect |
| --- | --- | --- |
| 23 | contextCountText != "3" | Producing action output for contextCountText |
| 34 | configVersionText != "1" | Producing action output for configVersionText |
| 40 | libraryFolderName == nil | Producing action output for libraryFolderName |
| 44 | actualLibraryName != "${libraryFolderName}" | Producing action output for actualLibraryName; right operand must also contain real variable token |
| 47 | prefixRegex == nil | Producing action output for prefixRegex |
| 50 | categories == nil | Producing action output for categories |
| 53 | sourceFile == nil | Replacement action output for sourceFile; reconnect after deleting Nothing |
| 58 | inputCountText != "1" | Producing action output for inputCountText |
| 63 | lowerExtension != "pdf" | Producing action output for lowerExtension |
| 69 | canonicalStem == nil | Producing action output for canonicalStem |
| 86 | archiveExtensionLower == "pdf" | Named variable archiveExtensionLower; use its current value, not initializer/earlier output |
| 91 | archiveStem == "${canonicalStem}" | Named variable archiveStem; use its current value, not initializer/earlier output; right operand must also contain real variable token |
| 92 | existingCleanFile != nil | Named variable existingCleanFile; use its current value, not initializer/earlier output |
| 100 | existingCleanFile != nil | Named variable existingCleanFile; use its current value, not initializer/earlier output |
| 106 | chosenCategory == nil | Producing action output for chosenCategory |
| 117 | childName == "${chosenCategory}" | Named variable childName; use its current value, not initializer/earlier output; right operand must also contain real variable token |
| 118 | typeFolder != nil | Named variable typeFolder; use its current value, not initializer/earlier output |
| 124 | typeFolder == nil | Named variable typeFolder; use its current value, not initializer/earlier output |

### util-assemble-choir-service.jelly

| Source line | Condition | Reference to inspect |
| --- | --- | --- |
| 22 | ShortcutInput != "interactive" | Native Shortcut Input |
| 33 | configVersionText != "1" | Producing action output for configVersionText |
| 39 | prefixRegex == nil | Producing action output for prefixRegex |
| 42 | categories == nil | Producing action output for categories |
| 45 | libraryFolderName == nil | Producing action output for libraryFolderName |
| 55 | rootChildName == "${libraryFolderName}" | Producing action output for rootChildName; right operand must also contain real variable token |
| 56 | libraryRoot != nil | Named variable libraryRoot; use its current value, not initializer/earlier output |
| 62 | libraryRoot == nil | Named variable libraryRoot; use its current value, not initializer/earlier output |
| 69 | serviceTypes != nil | Producing action output for serviceTypes |
| 71 | chosenServiceType == nil | Producing action output for chosenServiceType |
| 78 | selectedFiles == nil | Producing action output for selectedFiles |
| 95 | lowerExtension != "pdf" | Producing action output for lowerExtension |
| 105 | serviceName == nil | Producing action output for serviceName |
| 124 | canonicalStem == nil | Producing action output for canonicalStem |
| 132 | archiveResultType == "Text" | Named variable archiveResultType; use its current value, not initializer/earlier output |
| 135 | cleanFile == nil | Producing action output for cleanFile |
| 144 | existingScore != nil | Replacement action output for existingScore; reconnect after deleting Nothing |
| 153 | importedScore == nil | Replacement action output for importedScore; reconnect after deleting Nothing |
| 162 | existingScore != nil | Replacement action output for existingScore; reconnect after deleting Nothing |
| 168 | metadataMode == "Review metadata" | Named variable metadataMode; use its current value, not initializer/earlier output |
| 172 | composerTitleMatch != nil | Producing action output for composerTitleMatch |
| 182 | displayTitle == nil | Producing action output for displayTitle |
| 190 | composerName != nil | Producing action output for composerName |
| 191 | composerName != "-" | Producing action output for composerName |
| 194 | existingComposer != nil | Replacement action output for existingComposer; reconnect after deleting Nothing |
| 210 | setlistMode == "Create new" | Producing action output for setlistMode |
| 222 | setlistMode == "Replace existing" | Producing action output for setlistMode |

### util-canonical-choir-name.jelly

| Source line | Condition | Reference to inspect |
| --- | --- | --- |
| 21 | argumentCountText != "2" | Producing action output for argumentCountText |
| 29 | filename == nil | Replacement action output for filename; reconnect after deleting Nothing |
| 32 | prefixRegex == nil | Replacement action output for prefixRegex; reconnect after deleting Nothing |

## Priorities

- Archive: both existingCleanFile presence checks (duplicate detection and post-loop return); both typeFolder presence checks (ambiguous/missing folder); archiveStem and childName comparisons, including right-side canonicalStem/chosenCategory tokens.
- Assembly: libraryRoot duplicate/missing checks; archiveResultType Text-error check; both existingScore checks plus importedScore and existingComposer checks after replacing FS01/FS03/FS05; metadataMode comparison; setlistMode Create new and Replace existing checks. Replace existing controls clearing entries: inspect before using a real setlist.
- Collections are another instance of the same reference issue: orderedFiles, orderedNames and preparedScores consumers must use named variables populated by COL01-COL03, not their empty initializers.
- Config presence and version checks use Get Dictionary Value outputs; ensure ARC03/CONF02 replacement consumers feed the correct Dictionary. Input validation should be checked with missing config keys; do not infer this branch works merely because the valid path works.

Targeted device checks: archive reuse (now user-confirmed), missing prefixRegex, missing category folder, known versus absent forScore score, and Create new versus Replace existing on a disposable setlist. These cover distinct reference mechanisms; no claim of exhaustive execution.
