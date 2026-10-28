```text
ADD MUSIC CATEGORY AS GENRE
===========================

Shortcut names: 2-util-archive-choir-pdf; 2-util-assemble-choir-service
Purpose: Use the existing archive music category as Genre on first-time score import.
Input: Assembly retains Text interactive. Archive adds an optional category-return mode.
Output: Assembly retains report Text. Archive's optional mode returns PDF plus category.
Category: Reusable; incremental native update of the installed Jelly helpers.
Specification revision: 1
Interface: Archive 2.2; Assembly launch remains 1.1.
Target: User-reported iPadOS 26.6; English editor; forScore 15.2.5.
Status: Drafted; native Genre fields confirmed, new wiring/transfer not device-tested.
Required apps/permissions: Existing Shortcuts, forScore, Files/cloud-provider setup.
Launch: test-assemble-service -> 2-util-assemble-choir-service.
Side effects: Existing archive/import writes; assign/create Genre for a newly imported Score.

REQUIREMENT:
Music category Anthems -> Genre Anthems; Canticles -> Canticles; Hymns -> Hymns.
Use the existing music-category question, not the service-type question.
Do not set service-type Tags or Labels. Do not ask a second category question.
An existing forScore score is left alone, even if Review metadata is chosen.
A PDF already archived but missing from forScore is still a new score: infer its
category from the configured archive folder before importing and assigning Genre.

========================
DEPENDENCIES AND BUILD ORDER
========================

1. Keep 2-util-canonical-choir-name unchanged (two Texts -> canonical Text).
2. Update Archive to optional mode 2.2 and test returns before changing Assembly.
3. Update Assembly's archive caller/extraction and add GEN01-GEN03.
4. Keep test-assemble-service unchanged. Existing append draft/tests using the
   three-item archive input keep their PDF-only contract and do not gain Genres.

ARCHIVE CONTRACT:
Legacy input: [PDF File, Library Folder, config Dictionary]
Legacy success output: PDF File (unchanged).
Opt-in input: [PDF File, Library Folder, config Dictionary, Text with-category]
Opt-in success output: [PDF File, category Text], exactly two native List items.
Failure: ERROR: Text, or native action abort. Never serialize the PDF to Text/JSON.
The optional fourth item must be exactly with-category. Other fourth values stop.

========================
EDITOR SETUP
========================

Edit Apple Shortcuts on the iPad; do not regenerate the working helpers.
Duplicate both CURRENT working shortcuts before editing. Keep the existing
2-util-assemble-choir-service 2 backup; use distinct names for these new backups.
Keep active shortcut names unchanged and record which backup is the pre-Genre copy.

KEEP/EDIT/ADD identify existing/new blocks below. Bracketed action names are
real actions; bracketed names inside Text/Prompt content mean actual variable tokens.
Names in Input/Output/List/Folder/Score fields mean select the named variable or
specified producing action output. Do not type variable names as literal values.
Keep native File/Folder/Dictionary/Score/Genre objects; no interpolation of these.
For later assignments, select the current NAMED variable, not initial Nothing.
Use numeric Count operands and quoted literals only as identified in Text fields.
Otherwise/End If/End Repeat are supplied by the editor; remove unused Otherwise.
All deliberate Stop and Output actions: no-recipient behaviour Do Nothing.
Four-space nesting is authoritative; NOTE and numbered headings are not actions.

========================
STEP 1 - EDIT ARCHIVE'S INPUT COUNT AND EXTRACTION
========================

FIND: Archive's initial Count of Shortcut Input and its input-count error.
EDIT the count guard so it accepts 3 or 4 items, while keeping all other existing
source-PDF, Folder, Dictionary, config and extension validation.

[Count]
Count: Items
Input: Shortcut Input

[Set Variable]
Variable: contextCount
Input: Count from STEP 1

[If]
Input: contextCount
Condition: is not
Value: 3 (Number)

    [If]
    Input: contextCount
    Condition: is not
    Value: 4 (Number)

        [Text]
        ERROR: Supply PDF File, Library Folder, config Dictionary; optional fourth item must be with-category.

        [Stop and Output]
        Output: Error Text from STEP 1

    [End If]

[End If]

ADD before the existing context-extraction Repeat:

[Text]
pdf

[Set Variable]
Variable: archiveReturnMode
Input: Text pdf from STEP 1

KEEP existing extraction of items 1/2/3 into sourceFile/archiveRoot/workflowConfig.
ADD this block inside that same Repeat, after the item-3 check:

    [If]
    Input: Repeat Index from the context-extraction Repeat
    Condition: is
    Value: 4

        [Set Variable]
        Variable: archiveReturnMode
        Input: Native Repeat Item from the context-extraction Repeat

    [End If]

ADD after the extraction End Repeat, before existing validation:

[If]
Input: contextCount
Condition: is
Value: 4 (Number)

    [If]
    Input: archiveReturnMode
    Condition: is not
    Value: with-category (literal Text)

        [Text]
        ERROR: Optional archive mode must be with-category.

        [Stop and Output]
        Output: Mode error Text from STEP 1

    [End If]

[End If]

========================
STEP 2 - KEEP ARCHIVE'S GLOBAL PDF SEARCH AND DUPLICATE CHECK
========================

KEEP the existing recursive scan of archiveRoot, canonical-name comparisons,
duplicate-canonical error and assignment to named existingCleanFile.
KEEP the category picker, category-folder resolution, rename and Save File.
Do not move the picker before existing-file reuse or add a second category prompt.

========================
STEP 3 - ADD CATEGORY RESOLUTION INSIDE EXISTING-PDF REUSE
========================

FIND: If existingCleanFile has any value, immediately after the global search.
Its existing CFG03 Stop and Output returns the existing PDF. KEEP that return.
INSERT the following BEFORE it, still INSIDE the existing-file If.

    [If]
    Input: archiveReturnMode
    Condition: is
    Value: with-category (literal Text)

        [Get Contents of Folder]
        Folder: Named archiveRoot
        Recursive: Off

        [Set Variable]
        Variable: categoryRootChildren
        Input: Folder contents from STEP 3

        [Nothing]

        [Set Variable]
        Variable: resolvedCategory
        Input: Nothing from STEP 3

        [Repeat with Each]
        Input: categories from the parsed config Dictionary

            [Set Variable]
            Variable: categoryName
            Input: Repeat Item from the OUTER category-name Repeat

            [Repeat with Each]
            Input: categoryRootChildren

                [Get Details of Files]
                Detail: Name
                File: Repeat Item from this MIDDLE root-child Repeat

                [If]
                Input: Name from the root-child Get Details of Files
                Condition: is
                Value: Named categoryName

                    [Get Contents of Folder]
                    Folder: Repeat Item from the MIDDLE root-child Repeat
                    Recursive: On

                    [Repeat with Each]
                    Input: Contents from this category-folder enumeration

                        [Get Details of Files]
                        Detail: File Extension
                        File: Repeat Item from this INNER category-file Repeat

                        [Change Case]
                        Case: lowercase
                        Text: File Extension from this iteration

                        [If]
                        Input: Lowercase extension from Change Case
                        Condition: is
                        Value: pdf (literal Text)

                            [Get Details of Files]
                            Detail: Name
                            File: Repeat Item from the INNER category-file Repeat

                            [List]
                            Item 1: Name Text from this inner Get Details of Files
                            Item 2: prefixRegex Text from config

                            [Run Shortcut]
                            Shortcut: 2-util-canonical-choir-name
                            Input: Two-Text List from this inner iteration

                            [If]
                            Input: Result from this Run Shortcut
                            Condition: is
                            Value: Named canonicalStem of the requested PDF

                                [If]
                                Input: Named resolvedCategory
                                Condition: has any value

                                    [Text]
                                    ERROR: Archive category is ambiguous. Inspect configured categories and folders before importing.

                                    [Stop and Output]
                                    Output: Ambiguous-category Text from STEP 3

                                [End If]

                                [Set Variable]
                                Variable: resolvedCategory
                                Input: Named categoryName from the OUTER Repeat

                            [End If]

                        [End If]

                    [End Repeat]

                [End If]

            [End Repeat]

        [End Repeat]

        [If]
        Input: Named resolvedCategory
        Condition: does not have any value

            [Text]
            ERROR: Existing archived PDF is outside the configured category folders. Resolve its folder/category before importing.

            [Stop and Output]
            Output: Missing-category Text from STEP 3

        [End If]

        [List]
        Item 1: Named existingCleanFile (native PDF File)
        Item 2: Named resolvedCategory (Text)

        [Stop and Output]
        Output: Native two-item List from STEP 3 (CFG03C)

    [End If]

    --- KEEP EXISTING CFG03 STOP AND OUTPUT BELOW THIS END IF ---
    --- ITS OUTPUT REMAINS NAMED existingCleanFile, NATIVE PDF ---

NOTE: The enclosing existingCleanFile If still closes AFTER legacy CFG03.
The new List return must be explicitly selected, not the PDF's name or Text.
This read-only extra scan is only for category-mode reuse. It keeps the original
global duplicate check and fails rather than guessing if no configured folder fits.

========================
STEP 4 - ADD THE NEW-SAVE CATEGORY RETURN
========================

FIND: Save File near Archive's end, immediately before CFG04's PDF return.
KEEP Save File, destination named typeFolder, Overwrite Off and savedCleanFile.
ADD after Save File, BEFORE the existing CFG04 Stop and Output:

[If]
Input: archiveReturnMode
Condition: is
Value: with-category (literal Text)

    [List]
    Item 1: Native savedCleanFile output of the existing Save File
    Item 2: chosenCategory Text from the existing music-category picker

    [Stop and Output]
    Output: Native two-item List from STEP 4 (CFG04C)

[End If]

KEEP the original CFG04 Stop and Output immediately afterwards, returning only
the native savedCleanFile for legacy callers. Do not change either legacy return.

========================
STEP 5 - TEST ARCHIVE RETURNS BEFORE EDITING ASSEMBLY
========================

Use a duplicate of your working archive test caller with disposable input.
Three-row List: confirm it still returns a usable PDF on save and reuse.
Four-row List: add literal Text with-category as item 4. Confirm exactly two
returned items: item 1 previews as a PDF; item 2 equals the selected category.
Repeat the four-row call: same category from its folder, no second picker/save.
Do not continue to Assembly if File/List preservation or category resolution fails.
These mixed native return tests have not been run by creating this guide.

========================
STEP 6 - EDIT ASSEMBLY'S ARCHIVE REQUEST AND ERROR CHECK
========================

FIND: archiveInput List and Run Shortcut targeting 2-util-archive-choir-pdf,
inside the preparation Repeat. KEEP the first three List rows and native tokens.
EDIT this block to:

[List]
Item 1: Current PDF from the PREPARATION Repeat
Item 2: Named libraryRoot (native Folder)
Item 3: Parsed workflowConfig (native Dictionary)
Item 4: with-category (literal Text)

[Run Shortcut]
Shortcut: 2-util-archive-choir-pdf
Input: Four-item List from STEP 6

[Set Variable]
Variable: archiveResult
Input: Result from STEP 6's Run Shortcut

[Get Type]
Input: archiveResult

[If]
Input: Type from STEP 6's Get Type
Condition: is
Value: Text (literal Text)

    [Stop and Output]
    Output: Named archiveResult (the Archive error Text)

[End If]

NOTE: This replaces the old Run-result-as-cleanFile wiring. Reconnect the import
and cleanFile consumers to the extracted named File in STEP 7 before any run.

========================
STEP 7 - ADD TWO-ITEM RETURN VALIDATION AND EXTRACTION
========================

ADD after STEP 6's error check, before existing FS01 score lookup:

[Count]
Count: Items
Input: archiveResult

[If]
Input: Count from STEP 7
Condition: is not
Value: 2 (Number)

    [Text]
    ERROR: Archive category mode must return PDF File and category Text. Check Archive's version and List return.

    [Stop and Output]
    Output: Invalid-return Text from STEP 7

[End If]

[Nothing]

[Set Variable]
Variable: cleanFile
Input: Nothing from STEP 7

[Nothing]

[Set Variable]
Variable: musicCategory
Input: Second Nothing from STEP 7

[Repeat with Each]
Input: archiveResult

    [If]
    Input: Repeat Index from this return-extraction Repeat
    Condition: is
    Value: 1

        [Set Variable]
        Variable: cleanFile
        Input: Whole native Repeat Item from this return-extraction Repeat

    [End If]

    [If]
    Input: Repeat Index from this return-extraction Repeat
    Condition: is
    Value: 2

        [Set Variable]
        Variable: musicCategory
        Input: Repeat Item from this return-extraction Repeat

    [End If]

[End Repeat]

EDIT the existing missing-PDF guard and ADD the category guard as follows:

[If]
Input: Named cleanFile
Condition: does not have any value

    [Stop and Output]
    Output: Existing missing-PDF error Text

[End If]

[If]
Input: Named musicCategory
Condition: does not have any value

    [Text]
    ERROR: Archive returned no music category. Inspect archive context before importing.

    [Stop and Output]
    Output: Missing-category Text from STEP 7

[End If]

Close both checks before the existing FS01 score lookup.

CHECK FS02 import Files=named cleanFile, NOT whole archiveResult and NOT the
deleted/old PDF-only Run result. Keep original native score lookup/reuse/import,
SCORE01/SCORE02 selection and the named workingScore presence check unchanged.

========================
STEP 8 - ADD NEW-SCORE-ONLY GENRE ASSIGNMENT (GEN01-GEN03)
========================

FIND: If named workingScore does not have any value -> error -> End If.
ADD immediately AFTER that End If and BEFORE metadataMode/reuse-review questions.
The enclosing preparation Repeat has NOT finished yet.

[If]
Input: existingScore from the ORIGINAL FS01 lookup, before import
Condition: does not have any value

    [Get genre]
    Name: Named musicCategory
    Continue if not found: On

    [Set Variable]
    Variable: existingGenre
    Input: Native Genre output from Get genre in STEP 8 (GEN01)

    [If]
    Input: existingGenre
    Condition: has any value

        [Add metadata]
        Score: Named workingScore (native Score)
        Genres: Native existingGenre from GEN01
        Composers: [leave empty]
        Tags: [leave empty]
        Labels: [leave empty]
        Bookmarks: [leave empty]

    [End If]

    [If]
    Input: existingGenre
    Condition: does not have any value

        [Create genre]
        Name: Named musicCategory
        Add to Scores: Named workingScore (native Score)
        Add to Bookmarks: [leave empty]

    [End If]

[End If]

NOTE: Fields for Get genre and Create genre are confirmed by your report.
GEN02 Add metadata uses the native Genre, not category Text in a Genre slot.
GEN03 creates AND assigns; do not additionally run GEN02 after creating it.
The complementary presence/absence Ifs both check the original GEN01 result.
No service type is used. Existing forScore scores skip this whole outer If,
including when you subsequently choose Review metadata.

========================
STEP 9 - KEEP ALL OTHER WORKING ASSEMBLY BLOCKS
========================

KEEP the working title/composer/default/reuse prompts, metadata writes, COL03
Add to Variable, prepared-score guard, name-based target resolution, replace/skip
choice, corrected clearing condition, optional post-clear guard, final writing
Repeat, readback, report and open. Do not reapply the older reconstruction guide.

========================
EXPECTED TEST RESULTS
========================

1. Archive three-input save/reuse still returns a PDF for old callers.
2. Archive four-input save returns usable PDF plus exact selected category.
3. Four-input reuse returns same category without asking again or creating a copy.
4. New PDF/new score/existing Genre: Genre assigned; title/composer still work.
5. New PDF/new score/new Genre: one Genre created and assigned to that score.
6. Already archived PDF/missing score: folder-derived Genre assigned on import.
7. Existing forScore score, Reuse unchanged: all existing metadata unchanged.
8. Existing forScore score, Review metadata: title/composer review still works;
   no automatic Genre added/removed by this feature.
9. Two different categories in one run: each score gets its own category, with no
   stale category or Genre from the previous iteration. Tags/Labels unaffected.
10. Archive outside configured category folders: explanatory error before import;
    do not guess a category or silently use the current service type.

Inspect actual Genres/title/composer/Tags/Labels in forScore and actual setlist
identity/order. Count equality alone does not verify metadata or native types.

========================
BUILD NOTES
========================

Back up both installed helpers; complete/test Archive before enabling the new
Assembly caller. If rolling back Archive, also restore Assembly's three-item
request and PDF-only extraction together. Keep matching source/installed revisions.
Native Files in Dictionaries are avoided; the extra output is an explicit List.
The source templates include adjacent CFG03C/CFG04C/GEN comments, but exports
still need native completion. This guide is not evidence that those slots passed.

========================
ERRORS AND LIMITATIONS
========================

Library is expected to have configured category folders as immediate children.
Category-mode reuse performs an extra read-only scan; no new archive index or
filesystem-path parsing. Unknown/ambiguous classification stops for repair.
Genre is assigned only on the missing-score path, not for backfilling old scores.
If assignment fails after import, the score may exist without Genre; inspect and
repair it before retrying, since a reused score will intentionally skip assignment.
Existing embedded metadata must be inspected to confirm Add metadata preserves it.
Native errors can abort the shortcut; no transaction or automatic rollback claimed.

========================
IMPLEMENTATION RECORD
========================

28 October 2026: user confirms Get genre exposes Name and Continue if not found;
Create genre exposes Name and add to Scores and/or Bookmarks.
Archive 17/interface 2.2 and Assembly 18 implement the source template/slot changes.
Source/build evidence is recorded in the service tests. Native List return,
mixed extraction, Genre lookup/create/add and all cases above: Not device-tested.

========================
CHANGE HISTORY
========================

Revision 1, 28 October 2026: optional backward-compatible Archive category mode,
existing-folder category recovery, new-score-only native Genre blocks.

========================
SOURCES AND OPEN VERIFICATION
========================

User-confirmed action fields; existing native Add metadata Genres selector;
existing file enumeration/canonical helpers and quoted-index extraction patterns.
Open: mixed List return/extraction, native field wiring, actual Genre assignment,
metadata preservation and the acceptance cases. See linked evidence outside fence.
```

Sources: [Archive source](../shortcuts/reusable/util-archive-choir-pdf.jelly), [Assembly source](../shortcuts/reusable/util-assemble-choir-service.jelly), [forScore action evidence](../../forscore-action-evidence.md).

Contracts and results: [config integration](config-integration.md), [service tests](../tests/choir-service.md), [installed repair record](ipad-assembly-lessons.md).
