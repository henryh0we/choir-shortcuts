```text
UPDATE THE INSTALLED CHOIR SERVICE SHORTCUT
==========================================

Shortcut name: 2-util-assemble-choir-service
Purpose: Update the working installed shortcut without regenerating it.
Input: One Text value exactly interactive, supplied by test-assemble-service.
Output: The existing service-report Text, or explanatory error Text.

Category: Reusable; manual update guide for the Jelly-generated installed helper.
Specification revision: 1
Interface: Existing installed interactive contract; no caller change.
Target: User-reported iPadOS 26.6; English Shortcuts editor.
Status: Proposed edits; automatic name lookup and revised prompts not device-tested.
Required apps: Apple Shortcuts, forScore 15.2.5, Files/Nextcloud as already configured.
Permissions: Retain existing file-provider and forScore permissions.
Launch: test-assemble-service -> 2-util-assemble-choir-service.
Backup: 2-util-assemble-choir-service 2. Do not edit this backup.
Side effects: Existing PDF/archive/import/metadata preparation; create/replace setlists.

CONFIRMED FIX:
The replacement If had the literal TestReplace existing. Changing it to
Replace existing fixed the failure to clear the setlist, by user report.
Keep that correction. The count guard was catching the real A/B/B/A mismatch.
This guide adds the remaining improvements; it does not treat clearing as broken.

Defaults/cardinality: Keep existing selection, ordering, date/name and metadata
defaults. One prepared native Score per requested occurrence. Native File,
Folder, Dictionary, Score and Setlist objects must remain native objects.
Unsupported: Unattended operation and direct launch without interactive input.
Cancellation/native failures may leave prepared files/scores or partial writes.

========================
DEPENDENCIES AND BUILD ORDER
========================

Existing dependencies; no new shortcuts to install:
1. 2-util-canonical-choir-name: two Texts, filename and prefixRegex -> stem Text.
2. 2-util-archive-choir-pdf: PDF File / Library Folder / config Dictionary -> PDF
   File or error Text. It also calls the installed naming helper.
3. 2-util-assemble-choir-service: edit this installed helper only.
4. test-assemble-service: keep its target and Text interactive input unchanged.

========================
EDITOR SETUP
========================

Open Apple Shortcuts on the iPad, not the Jellycuts source editor.
Edit 2-util-assemble-choir-service, without the final 2.
Do not reimport or replace the naming/archive helpers.

Change labels used below:
KEEP = existing actions remain in their existing positions.
EDIT = change fields in an existing action; retain its output connections.
REMOVE = remove the named old action/block, including only its owning markers.
MOVE = reuse an existing action in the new position, then reconnect consumers.
ADD = insert the complete action/block shown.
CHECK = inspect/reselect inputs; no new action needed if already correct.

Numbered steps are guide locations, not action names or values to enter.
Action names are on their own bracketed lines. NOTE is documentation.
Names in Input/List/Setlist/Output fields mean select real variable tokens.
Inside Text/Prompt fields, [name] means insert that actual token, not brackets.
Text values Create new and Replace existing are typed exactly, including spaces.
Use numeric 0 and 1 in Count comparisons, not quoted text.
Choose named mutable variables such as targetSetlist/preparedScores rather than
their initial Nothing outputs. Explicitly select inputs instead of implicit chaining.
Adding If/Repeat supplies Otherwise/End If/End Repeat automatically. Remove unused
Otherwise branches. Keep the indentation shown, including both nested End Ifs.
All deliberate Stop and Output actions: no-recipient behaviour Do Nothing.
Expanded action labels may differ slightly; fields below identify their purpose.

This is based on the repository and your reports, not an inspection of the actual
installed action list. Locate by comments, prompts and neighbours, not line numbers.
If a block is already in the requested final form, keep it; do not add a duplicate.

========================
STEP 1 - KEEP THE WORKING SETUP AND PREPARATION
========================

KEEP all existing actions from the start through score preparation:
- Text interactive validation and config loading.
- Service type, PDF selection and running-order selection.
- Your working Date -> formatted date -> editable service-name default.
- The trim action producing serviceName and the initial service preview.
- Canonical-name/archive calls and their native input Lists.
- Existing-score reuse, missing-score import, title/composer processing.
- Add workingScore to preparedScores once per preparation iteration.

Only the three prompts within that preparation area change in Steps 2-4.
Do not remove initialiser Nothing actions or alter these preparation loops.

========================
STEP 2 - EDIT THE EXISTING METADATA CHOICE PROMPT
========================

FIND: Choose from List with Reuse unchanged / Review metadata, inside the
existingScore presence If within the preparation Repeat.
EDIT only its Prompt. KEEP its List, selection settings and output consumers.

[Choose from List]
List: Existing metadataChoices List (Reuse unchanged / Review metadata)
Prompt: [canonicalStem] - preserve the existing metadata, or review it?
Select Multiple: Off

NOTE: canonicalStem is the current named Text identity for this piece, such as
Humfrey-InEMinor. Keep the following assignment to metadataMode and its checks.

========================
STEP 3 - EDIT THE EXISTING TITLE QUESTION
========================

FIND: Ask for Input that currently says Confirm title, retaining movement and
variant details. It follows the readableTitle Replace Text action.
EDIT its Prompt. CHECK its Default Answer; KEEP the downstream title trimming.

[Ask for Input]
Input Type: Text
Prompt: [canonicalStem] - confirm title, retaining movement and variant details.
Default Answer: readableTitle from this iteration's final title Replace Text

NOTE: Default Answer must be an actual readableTitle token, not literal
${readableTitle}, $[readableTitle], or quote characters.

========================
STEP 4 - EDIT THE EXISTING COMPOSER QUESTION
========================

FIND: Ask for Input that currently says Confirm composer; a single hyphen means
unknown/not applicable. It follows title validation.
EDIT its Prompt. CHECK its Default Answer; KEEP all metadata-writing actions.

[Ask for Input]
Input Type: Text
Prompt: [canonicalStem] - confirm composer for [displayTitle]; a single hyphen means unknown/not applicable.
Default Answer: Named composerSuggestion variable

NOTE: canonicalStem/displayTitle are tokens in the Prompt. composerSuggestion
is a token in Default Answer. Retain the current Text outputs and trimming.

========================
STEP 5 - KEEP THE PREPARED-SCORE COUNT CHECK
========================

FIND: After the preparation Repeat, immediately before the old Create/Replace
questions. Its error contains Prepared score count does not match the running order.
KEEP this whole block, including its End If. CHECK both Count/If connections.

[Count]
Count: Items
Input: Named preparedScores variable

[If]
Input: Count from STEP 5
Condition: is not
Value: pieceCount from the original selected-files Count

    [Stop and Output]
    Output: Existing prepared-score-count error Text
    No-recipient behaviour: Do Nothing

[End If]

NOTE: The new target-resolution section starts AFTER this End If.

========================
STEP 6 - REMOVE OLD CHOOSERS; RETAIN ACTIONS TO REUSE
========================

FIND THE TWO BOUNDARIES:
Start: Immediately after STEP 5's End If.
End: Immediately before the final Repeat with Each over preparedScores (FS11).
Do not remove STEP 5, that final Repeat, or the report/readback after it.

Within those boundaries, use this existing-block checklist:

REMOVE: List containing Create new / Replace existing (setlistChoices).
REMOVE: Choose from List asking Create an unused service name, or replace...?
REMOVE: Assignment of that Chosen Item to setlistMode, if present.
REMOVE: No setlist mode selected error If/Stop/End If.

MOVE/REUSE: Existing Create Setlist (FS08) and its New Setlist assignment;
these belong inside STEP 11's new Create new If.

REMOVE: Get all setlists (old FS09).
REMOVE: Choose from List selecting the service to replace.
REMOVE: Assignment of that chooser's Chosen Item to targetSetlist.
REMOVE/REBUILD: Old target-missing If, using STEP 12 below.

EDIT/MOVE: Old Apply running order alert becomes STEP 13's replacement-only
alert. There must be no replacement confirmation in the new-service path.

MOVE/REUSE: The corrected If setlistMode is Replace existing and its working
Remove all setlist entries (FS10), using STEP 13. Retain the corrected literal.

Remove empty/redundant old If/Otherwise/End If markers as their actions are moved.
Keep one targetSetlist initialiser in this section, positioned as STEP 9.
Remove superseded old assignments here so they cannot overwrite the new target.

NOTE: Move reusable actions out before deleting their enclosing old blocks.
If an action must be recreated, select its new output in every consumer.
The authoritative final order for this section is STEPS 7-14 below, followed
by the existing writing Repeat in STEP 15. Build/check each block in that order.

========================
STEP 7 - ADD LOOKUP BY THE EDITED SERVICE NAME (FS09)
========================

ADD after STEP 5, in the gap identified in STEP 6:

[Get setlist]
Name: serviceName from the existing edited-name trim action
Continue if not found: On

[Set Variable]
Variable: matchingSetlists
Input: Native Get setlist output from STEP 7

[Count]
Count: Items
Input: matchingSetlists

[Set Variable]
Variable: matchingSetlistCount
Input: Count from STEP 7

NOTE: Use Get setlist, not Get all setlists. Name and Continue if not found are
confirmed fields. If a library control is exposed, select the intended library.
Verify on device that absent names return no items and existing names resolve
the intended exact service. Duplicate-name return behaviour is not established.

========================
STEP 8 - ADD THE MULTIPLE-MATCH STOP
========================

ADD after STEP 7:

[If]
Input: matchingSetlistCount (Number)
Condition: is greater than
Value: 1 (Number)

    [Text]
    ERROR: More than one service matches [serviceName]. Resolve the duplicate names in forScore before continuing. Prepared files or scores may already have changed; setlist entries have not been changed.

    [Stop and Output]
    Output: Text from STEP 8
    No-recipient behaviour: Do Nothing

[End If]

NOTE: serviceName in the Text is a token. This catches multiple returned items;
it cannot catch duplicates silently reduced to one by Get setlist itself.

========================
STEP 9 - ADD OR MOVE THE TARGET INITIALISER AND DEFAULT MODE
========================

ADD after STEP 8, or MOVE the existing local target initialiser here:

[Nothing]

[Set Variable]
Variable: targetSetlist
Input: Nothing from STEP 9

[Text]
Create new

[Set Variable]
Variable: setlistMode
Input: Text Create new from STEP 9

NOTE: Preserve this Nothing. It is an initialiser, not an incomplete action slot.

========================
STEP 10 - ADD THE UNIQUE EXISTING-TARGET BLOCK (TARGET01)
========================

ADD after STEP 9:

[If]
Input: matchingSetlistCount (Number)
Condition: is
Value: 1 (Number)

    [Get Item from List]
    Get: Item at Index
    Index: 1
    List: matchingSetlists

    [Set Variable]
    Variable: targetSetlist
    Input: Native Item from STEP 10's Get Item from List

    [Text]
    Replace existing

    [Set Variable]
    Variable: setlistMode
    Input: Text Replace existing from STEP 10

[End If]

NOTE: First Item is also suitable for index 1. Select a native Setlist, not its
displayed name as Text. No chooser belongs in this block.

========================
STEP 11 - MOVE/EDIT THE EXISTING CREATE BLOCK (FS08)
========================

PLACE after STEP 10. REUSE Create Setlist and the working New Setlist assignment:

[If]
Input: Named setlistMode variable
Condition: is
Value: Create new (literal Text)

    [Create Setlist]
    Name: serviceName
    Folder: [leave empty]

    [Set Variable]
    Variable: targetSetlist
    Input: Native New Setlist from STEP 11's Create Setlist

[End If]

NOTE: This path runs when lookup returns zero items. No Create/Replace question
or service chooser. Retain the working library selection wherever available.

========================
STEP 12 - EDIT/REBUILD THE EXISTING MISSING-TARGET CHECK
========================

PLACE after STEP 11:

[If]
Input: Named targetSetlist variable
Condition: does not have any value

    [Text]
    ERROR: No target service was found or created for [serviceName]. Inspect forScore before retrying. A new empty setlist may already exist; no entries have been submitted.

    [Stop and Output]
    Output: Text from STEP 12
    No-recipient behaviour: Do Nothing

[End If]

NOTE: Reselect named targetSetlist. Do not retain the deleted chooser's output.

========================
STEP 13 - MOVE/EDIT THE WORKING REPLACEMENT BLOCK (FS10)
========================

PLACE after STEP 12. REUSE the corrected replacement If and clearing action.
EDIT/move the existing alert into this If before clearing. ADD STEP 14 inside
the same If before the outer End If, as indicated below.

[If]
Input: Named setlistMode variable
Condition: is
Value: Replace existing (literal Text; NEVER TestReplace existing)

    [Show Alert]
    Title: Replace [serviceName]?
    Message: A service named [serviceName] already exists. Running order: [runningOrder]. Replace its existing entries with this running order? Scores and clean PDFs remain.
    Show Cancel Button: On

    [Remove all setlist entries]
    Setlist: Named targetSetlist variable

    --- INSERT STEP 14 HERE, STILL INSIDE THIS IF ---

[End If]

NOTE: serviceName/runningOrder in the alert are tokens. Cancel must stop before
Remove all setlist entries. The clear action already works after your literal
correction; reconnect its target only as needed for the new name-based lookup.

========================
STEP 14 - ADD POST-CLEAR VERIFICATION (FS10R)
========================

ADD immediately after Remove all setlist entries, INSIDE STEP 13's If.
The indentation below is part of that same outer If. Do not close STEP 13 early.

    [Get setlist entries]
    Setlist: Named targetSetlist variable
    Sorting: Manual

    [Count]
    Count: Items
    Input: Entries from STEP 14's Get setlist entries

    [Set Variable]
    Variable: remainingEntryCount
    Input: Count from STEP 14

    [If]
    Input: remainingEntryCount (Number)
    Condition: is not
    Value: 0 (Number)

        [Text]
        ERROR: [serviceName] still contains [remainingEntryCount] entries after clearing. No replacement entries have been added. Inspect the selected service before retrying.

        [Stop and Output]
        Output: Text from STEP 14
        No-recipient behaviour: Do Nothing

    [End If]

NOTE: After the inner End If shown here comes STEP 13's outer End If.
Only then comes the final writing Repeat. This is an added check, not another
clearing action. Do not use the later FS12 readback output here.

========================
STEP 15 - KEEP/CHECK THE EXISTING FINAL WRITING REPEAT (FS11)
========================

KEEP after STEP 13's outer End If. CHECK and reconnect the target token:

[Repeat with Each]
Input: Named preparedScores variable

    [add scores to setlist]
    Scores: Native Repeat Item from THIS final writing Repeat
    Setlist: Named targetSetlist variable
    Skip if already added: Off

[End Repeat]

NOTE: This Repeat must remain OUTSIDE the replacement If so it also populates
new services. Do not use the preparation loop's Repeat Item or a deleted chooser.

========================
STEP 16 - KEEP/CHECK THE FINAL READBACK (FS12)
========================

KEEP after STEP 15. CHECK native target, Count sources and If polarity:

[Get setlist entries]
Setlist: Named targetSetlist variable
Sorting: Manual

[Count]
Count: Items
Input: Entries from STEP 16's Get setlist entries

[Set Variable]
Variable: actualCount
Input: Entry Count from STEP 16

[Count]
Count: Items
Input: Named preparedScores variable

[Set Variable]
Variable: requestedCount
Input: Prepared-score Count from STEP 16

[If]
Input: actualCount
Condition: is not
Value: requestedCount

    [Text]
    ERROR: [serviceName]. Requested entries: [requestedCount]. Actual entries: [actualCount]. Entries may already have changed. Inspect the service in forScore before retrying.

    [Stop and Output]
    Output: Text from STEP 16's mismatch branch
    No-recipient behaviour: Do Nothing

[End If]

NOTE: If existing captured Count outputs already provide actualCount and
requestedCount, keep them instead of adding duplicate Set Variable actions.
The three names in the error Text are actual tokens. Keep the existing guard;
only its error wording needs editing to include the numeric operands.

========================
STEP 17 - KEEP/CHECK THE EXISTING REPORT AND OPEN (FS13)
========================

KEEP the report-producing Text after STEP 16, including its existing fields.
CHECK that serviceName, runningOrder, selectedServiceType, requestedCount and
actualCount still refer to their intended current values.

[Text]
[serviceName]
[runningOrder]
Service type: [selectedServiceType]
Requested entries: [requestedCount]
Readback entries: [actualCount]
Running order submitted. Check Manual order and metadata; count equality alone does not verify identity or order.

[open setlist]
Setlist: Named targetSetlist variable

[Stop and Output]
Output: Existing serviceReport Text, produced by the report Text in STEP 17
No-recipient behaviour: Do Nothing

NOTE: If the report is assigned to named serviceReport, keep that assignment
between Text and open setlist. Keep the final output connected to that report,
not to open setlist. The Text block's bracketed fields are actual tokens.

========================
EXPECTED TEST RESULTS
========================

Run through test-assemble-service. Use disposable pieces and setlists.

1. New name: choose A/B and a genuinely unused serviceName. No mode or target
   chooser, no replacement alert. Exactly A/B in the new setlist, Manual order.
2. Same name: choose B/A and enter EXACTLY the same final serviceName. One named
   replacement alert, no chooser. Clearing passes the zero-entry check; exactly
   B/A afterwards, two entries. No second setlist with that name.
3. Cancel: same name, cancel the replacement alert. Existing B/A entries remain.
   Prepared PDF/score/metadata changes may already have happened before the alert.
4. Metadata: review A and B. Every metadata choice/title/composer prompt identifies
   the current piece. Default answers contain values, not interpolation syntax.
5. Lookup semantics: confirm an absent name gives Count 0 and an existing exact
   name Count 1. Check similar names cannot target another service. Duplicate-name
   behavior is unverified; verify separately before relying on the multiple-match
   stop for ambiguous libraries. Do not proceed to clearing an ambiguous target.

If a count error occurs, inspect the actual setlist before retrying. Record which
check stopped, both operand values, target identity and actual Manual entries.
Defer A/B/A repetition testing; two selected files currently give two order slots.

========================
BUILD NOTES
========================

This is an incremental native edit guide, not a new standalone shortcut to install.
Existing actions are identified by prompts, variables and FS markers where present.
Keep all unrelated working wiring. Every action consuming a removed output must
be explicitly reconnected; deleting an action does not transfer its output token.
The full actual installed action list has not been inspected. If a stated old
block differs, use its function and boundaries, preserving all working preparation.
No Jelly source or transfer-copy edits are required to follow this guide.

========================
ERRORS AND LIMITATIONS
========================

Get setlist Name/Continue if not found fields are user-confirmed; its exact-name,
empty-result, duplicate-return and library-scope behavior still need device tests.
The new post-clear check verifies emptiness; it cannot restore removed entries.
Preparation occurs before lookup/confirmation and can change files or metadata.
A failure while adding may leave a partial setlist. Count equality does not prove
identity/order. The guide does not claim native errors are caught by later Ifs.

========================
IMPLEMENTATION RECORD
========================

27 October 2026, user report: correcting TestReplace existing -> Replace existing
fixed the installed failure to clear. Active caller/target and backup are confirmed.
Automatic lookup, new prompts and post-clear check from this guide: Not yet applied
or device-verified by this documentation work. Broader regression is not inferred.

========================
CHANGE HISTORY
========================

Revision 1, 27 October 2026: first incremental guide using the manual workspace's
bracketed blueprint style. Each existing/new block has an explicit edit status.
Preserves the confirmed clearing repair and working native date/create changes.

========================
SOURCES AND OPEN VERIFICATION
========================

Sources: User's installed-shortcut reports in this conversation; Jelly Assembly
revision 17; iPad repair record; manual Assembly and filename blueprint formatting.
Links are provided outside this text block.
Open verification: Get setlist matching/absence/duplicates/library behavior;
new native edits and creation/replacement/cancel/metadata tests listed above.
No new compiler run is needed for this documentation-only guide. No app import
or device execution was performed by creating this file.
```

Source and dependencies: [Assembly source](../shortcuts/reusable/util-assemble-choir-service.jelly), [canonical-name source](../shortcuts/reusable/util-canonical-choir-name.jelly), [archive source](../shortcuts/reusable/util-archive-choir-pdf.jelly).

Evidence and tests: [iPad repair record](ipad-assembly-lessons.md), [service test record](../tests/choir-service.md).

Presentation references: [manual Assembly blueprint](../../manual%20creation/shortcuts/reusable/util-assemble-choir-service.md), [original filename blueprint](../../Parse%20Choir%20Music%20Filename%20V2%20-%20Shortcut%20Blueprint.txt).
