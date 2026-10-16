```text
FORSCORE IMPORT AND LOOKUP TEST
==============================

Shortcut name: TEST - forScore Import and Lookup
Purpose: Import one disposable PDF, retrieve the library independently,
         and open its single score without relying on an import receipt.
Input: One native File, required, supplied through Files Share Sheet.
Output: One diagnostic Text report if the run reaches Stop and Output.

Category: Diagnostic (Main)
Specification revision: 1
Interface version: 1.0
Target platform: User-reported iPadOS 26.6
Editor language: English, as shown in supplied screenshots
Implementation status: Designed
Required apps: Apple Shortcuts; forScore 15.2.5; Files
Permissions: Read the selected File; access forScore; allow opening forScore
Launch methods: Files Share Sheet; direct execution for no-input check
Side effects: Imports a test PDF into forScore; opens a retrieved score.
             No rename, metadata edit, file save, or source-file modification.

Input contract:
Use the supplied TEST-Choir-Import-Lookup.pdf fixture only.
One File, not a path string, URL, or Dictionary. Multiple Files are rejected.
Missing input produces an explanatory Text report without an import.
The extension check rejects non-PDF extensions; it does not validate PDF bytes.
Precondition: The chosen library is empty or contains only this test score.
Do not use this diagnostic once real scores have been added to that library.

Output contract:
Diagnostic Text includes before/after score counts and says that one score
was retrieved. It does not certify exact filename identity or import success.
Validation and unexpected-count branches return explanatory Text instead.
Action failures or cancellation may halt without a report.
No native score object crosses this Shortcut's output boundary.

Direct execution: No-input report; choose the File in Files to perform import.
Called through Run Shortcut: Unsupported for this initial interactive test.
Unsupported inputs: Multiple files, non-PDFs, real music, nonempty music library.

========================
DEPENDENCIES AND BUILD ORDER
========================

Required Shortcuts: None
External resources: Supplied PDF fixture in an accessible Files location.
Build order: Build this test directly in Apple Shortcuts, then run T1–T4.
Jellycuts generation is not required for this native capability probe.

========================
EDITOR SETUP
========================

1. Create a Shortcut with the exact name above.
2. Enable Show in Share Sheet and receive Files only. If a no-input setting
   is available, select Continue so the explicit missing-input branch runs.
3. Transfer the supplied fixture to a temporary Files location on your iPad.
   Preview it first. Keep it outside Choir Music/Library: it is not music.
4. In each Get all scores action below, choose the SAME current library.
   Inspect the Library selector once; record the exact selected option.
   Do not infer that leaving the selector blank means all libraries.
5. Add only ONE forScore import action. Start with the catalogue entry
   Import file(s), whose screenshot-expanded card reads Import Files.
   Record the catalogue entry selected. The two screenshot import cards
   are not evidence that both must be used.

Notation:
Assembly numbers are documentation references, not values to enter.
Bracketed labels are action search names or automatic control markers.
If creates Otherwise and End If automatically; do not search for markers.
Select named variables and action outputs as native tokens, not typed names.
Text tokens in brackets are inserted only as explained by their NOTE.
Input and Output below are descriptive field locators where the exact
native label is not established. Record differences on the target editor.
Get all scores and Open score are the catalogue labels from the inventory.

[Shortcut Input]
Type expected: One native File

========================
CHECK INPUT
========================

1. [If]
   Input: Shortcut Input
   Condition: has any value

       2. [Count]
          Count: Items
          Input: Shortcut Input

       3. [If]
          Input: Count from step 2
          Condition: is
          Value: 1 (Number)

           4. [Get Details of Files]
              Detail: File Extension
              File: Shortcut Input

           5. [Change Case]
              Input: File Extension from step 4
              Case: lowercase

           6. [If]
              Input: Changed Text from step 5
              Condition: is
              Value: pdf (literal Text, without a dot)

               7. [Get Details of Files]
                  Detail: Name
                  File: Shortcut Input

               8. [Set Variable]
                  Variable: SourceName
                  Input: Name from step 7

               ========================
               RETRIEVE BEFORE IMPORT
               ========================

               9. [Get all scores]
                  Library: The selected current library from EDITOR SETUP
                  Sort Order: Title

               10. [Count]
                   Count: Items
                   Input: Scores output from step 9

               11. [Set Variable]
                   Variable: BeforeCount
                   Input: Count from step 10

               12. [If]
                   Input: BeforeCount
                   Condition: is greater than
                   Value: 1 (Number)

                   13. [Text]
                       Test stopped before import: the selected library
                       contains more than one score. Use only the fixture
                       in an empty test library. No import was attempted.

                   14. [Stop and Output]
                       Output: Text from step 13
                       No-recipient behaviour: Respond

               [Otherwise]
                   Leave this branch empty.
               [End If]

               ========================
               IMPORT THE FIXTURE
               ========================

               15. [Import file(s)]
                   Files: Shortcut Input
                   Conflict Handling: Skip

               NOTE:
               This is forScore's action, shown as Import Files in the
               screenshot. Do not add the second import action.
               Do not convert Shortcut Input into Text or a file path.
               Import output is deliberately not consumed in this core
               test: it might be absent or have a different native type.

               ========================
               LOOK UP INDEPENDENTLY
               ========================

               16. [Get all scores]
                   Library: Exactly the same selection as step 9
                   Sort Order: Title

               17. [Set Variable]
                   Variable: RetrievedScores
                   Input: Scores output from step 16

               18. [Count]
                   Count: Items
                   Input: RetrievedScores

               19. [Set Variable]
                   Variable: AfterCount
                   Input: Count from step 18

               20. [If]
                   Input: AfterCount
                   Condition: is
                   Value: 1 (Number)

                   21. [Get Item from List]
                       Get: First Item
                       List: RetrievedScores

                   22. [Set Variable]
                       Variable: RetrievedScore
                       Input: Item from List from step 21

                   23. [Text]
                       Source file: [SourceName]
                       Scores before: [BeforeCount]
                       Scores after: [AfterCount]
                       One score was retrieved independently of import.
                       Verify that the opened score is the test PDF.
                       This is not yet an exact filename lookup.

                   NOTE:
                   Insert the named Text SourceName and Number BeforeCount
                   and AfterCount tokens created in steps 8, 11 and 19.
                   Only this report converts counts to displayed Text;
                   RetrievedScore remains a native object.

                   24. [Set Variable]
                       Variable: TestReport
                       Input: Text from step 23

                   25. [Open score]
                       Score: RetrievedScore

                   NOTE:
                   Select the native RetrievedScore token from step 22.
                   VERIFY ON DEVICE: exact input field and foreground/
                   return behaviour of Open score. If it cannot consume
                   this token, record the error; use the diagnostic
                   variation in BUILD NOTES rather than guessing a type.

                   26. [Stop and Output]
                       Output: TestReport
                       No-recipient behaviour: Respond

               [Otherwise]

                   27. [Text]
                       Source file: [SourceName]
                       Scores before: [BeforeCount]
                       Scores after: [AfterCount]
                       Test unresolved: expected exactly one test score.
                       Inspect import outcome and library scope before retrying.

                   NOTE:
                   Insert the same three named tokens as in step 23.

                   28. [Stop and Output]
                       Output: Text from step 27
                       No-recipient behaviour: Respond

               [End If]

           [Otherwise]

               29. [Text]
                   Test stopped: share the supplied PDF fixture only.
                   No import was attempted.

               30. [Stop and Output]
                   Output: Text from step 29
                   No-recipient behaviour: Respond

           [End If]

       [Otherwise]

           31. [Text]
               Test stopped: share exactly one PDF. No import was attempted.

           32. [Stop and Output]
               Output: Text from step 31
               No-recipient behaviour: Respond

       [End If]

[Otherwise]

    33. [Text]
        No input file. In Files, share TEST-Choir-Import-Lookup.pdf
        to TEST - forScore Import and Lookup. No import was attempted.

    34. [Stop and Output]
        Output: Text from step 33
        No-recipient behaviour: Respond

[End If]

========================
EXPECTED TEST RESULTS
========================

Prerequisites: Fixture previews in Files; current library contains no
real scores; identical library selections in steps 9 and 16.
Avoid concurrent imports/sync changes during the two count measurements.

T1 - First import
In Files, share the fixture to this test; accept required permissions.
-> Expected baseline 0, after 1, and the disposable test page opens.
-> Inspect forScore to confirm one copy, not merely a count increase.
-> The source fixture remains unchanged. No composer/title edit occurs.
Actual result: Not run

T2 - Independent retrieval and retry
Share the SAME fixture again, with the one test score still present.
-> Expected baseline 1 and after 1; the same test page opens.
-> Record whether Skip returns a value, empty output or an error.
-> An unchanged count alone is not proof of exact filename matching.
Actual result: Not run

T3 - No input
Run the test directly from Shortcuts without input.
-> No-input report; no import attempt.
Actual result: Not run

T4 - Cancel sharing or deny a permission
Cancel before execution, or deny file/forScore access when prompted.
-> No guaranteed output. Inspect the library if execution reached import
   before a later cancellation. No automatic rollback is assumed.
Actual result: Not run

T5 - Invalid/boundary input
Share two Files; separately share a .txt file if the Files banner permits it.
-> Multiple-item/non-PDF report before import. If Share Sheet does not
   offer the test for that input, record it as entry-point filtered.
-> A corrupt file named .pdf is out of contract and may stop the import;
   this diagnostic does not claim byte-level PDF validation.
Actual result: Not run

T6 - Empty retrieval
During first run, note whether Get all scores returns an empty collection
and Count reports 0. If it halts, record exact error/action and library
selection. Do not change to an assumed empty-list result.
Actual result: Not run

========================
BUILD NOTES
========================

1. This initial lookup uses a single-score test-library precondition,
   not an invented filename/title filter. It proves retrieval and native
   consumption if the retrieved score opens; properties inspection below
   determines the later exact matching implementation.

2. INSPECT PROPERTIES WITHOUT CHANGING TYPES:
   In the editor, tap RetrievedScore in step 25. Record the native Type
   and the full available property list. Do not change Type to Text/File
   to make an unavailable property appear. Capture any identifier,
   filename/path/title fields actually offered, including their exact
   names. A displayed description is not necessarily a filename.

3. INSPECT THE IMPORT OUTPUT:
   Look for the selectable output directly beneath step 15. If present,
   insert a temporary Quick Look action immediately after import and
   explicitly select that output. Inspect its variable Type/properties.
   Quick Look may convert or fail to render it; this is diagnostic only.
   Record that behaviour. If no output token exists, record that and do
   not wire Quick Look to another action's result. Remove the temporary
   action before rerunning the core test. No score-object return assumed.

4. OPEN FAILURE VARIATION:
   If step 25 rejects RetrievedScore or prevents returning the report,
   temporarily remove only step 25, leaving step 26's TestReport intact.
   Run and inspect the retrieved token properties, then manually open
   the fixture in forScore. Mark native opening unverified/failed, not
   passed. Restore step 25 after fixing its verified configuration.

5. If Import file(s) rejects the PDF or has an unsuitable contract,
   inspect the outcome in forScore first. Test Import score(s) as a
   replacement for step 15 in a separate recorded revision/trial. Never
   chain the two import actions or blindly rerun an uncertain import.

6. Capture these results for the next implementation:
   - Selected library label and chosen import catalogue entry.
   - Baseline/after counts for T1 and T2.
   - Import output Type/properties, or no selectable output.
   - RetrievedScore native Type and offered property list.
   - Actual PDF filename and displayed title in forScore/Files where visible.
   - Whether Open score works and returns control to the caller.
   - Any exact errors, prompts and the action where execution stops.

7. After reporting results, remove the disposable score manually in
   forScore and the fixture copy from its temporary Files location if
   desired. This Shortcut does not delete anything automatically.

========================
ERRORS AND LIMITATIONS
========================

Input validation -> CHECK INPUT returns Text before native library actions.
More than one baseline score -> Stops before import; no exact lookup claimed.
One unrelated baseline score -> Outside the fixture precondition; counts
alone cannot detect substitution. Verify the library before running.
Import failure -> May terminate execution; no try/catch or receipt invented.
Import completes but retrieval fails -> Score may already exist. Inspect
forScore and scope before retrying; do not assume failure means no write.
Wrong library -> May report zero despite a completed import elsewhere.
Open failure/foreground transition -> Report may not be returned; use the
documented temporary variation to separate retrieval from navigation.
Cloud sync/concurrent edits -> Can invalidate before/after counts; rerun only
after reconciling actual contents and selecting the correct scope.

========================
IMPLEMENTATION RECORD
========================

Current status: Designed
Static review: 2026-10-14; action sources, variable flow, exits and links checked.
Built revision / device / builder / date: Not built
Execution evidence: Not run
Remaining issues: Library selector choices and empty-return behaviour;
Count/Share Sheet settings on target version; import outputs; native score
properties; Open score field/consumption/foreground behaviour.

Record T1–T6 here after running, preserving failures and temporary variations.
Do not promote to Ready for manual construction until critical settings are
confirmed, or to Tested/Verified working until actual execution is recorded.

========================
CHANGE HISTORY
========================

Revision 1 | Interface 1.0 | 2026-10-14
Initial standalone capability diagnostic. Manual migration: create the
documented actions on iPad, select one library and transfer the fixture.

========================
SOURCES AND OPEN VERIFICATION
========================

User screenshots: Import Files/Skip; Get all scores/Library/Title.
User inventory: Get all scores, Import file(s), Import score(s), Open score.
Apple guides: native variable selection, property inspection, Share Sheet,
list-item selection, Quick Look, explicit Stop and Output.
Reviewed: 2026-10-14. Sources establish semantics, not this build's runtime.

VERIFY ON DEVICE: Empty Get all scores response and Count setting.
VERIFY ON DEVICE: Library selection includes the newly imported test score.
VERIFY ON DEVICE: Import action result token and native type, if any.
VERIFY ON DEVICE: RetrievedScore properties supporting exact future matching.
VERIFY ON DEVICE: Open score consumes the retrieved object without coercion.
VERIFY ON DEVICE: Action labels/settings and Share Sheet visibility on 26.6.
```

Fixture: [TEST-Choir-Import-Lookup.pdf](../../fixtures/TEST-Choir-Import-Lookup.pdf).

Project: [V2 plan](../../../nextcloud-forscore-plan-v2.md), [forScore guidance](../../../forscore.md), [screenshot evidence](../../../forscore-action-evidence.md), [action inventory](../../../forscore%20shortcut%20actions.md).

Sources: [Apple variable properties](https://support.apple.com/en-au/guide/shortcuts/apda36b9018b/ios), [Apple list actions](https://support.apple.com/en-za/guide/shortcuts/apd4dcacc115/9.0/ios/26), [Apple Share Sheet input](https://support.apple.com/guide/shortcuts/apd8195f96d6/ios), [Apple Shortcut completion](https://support.apple.com/en-gb/guide/shortcuts/apda9578f70f/ios).
