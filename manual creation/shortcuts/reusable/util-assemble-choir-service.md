Preferred build updated 16 October 2026: [generate this helper from Jelly source](../../../jelly/shortcuts/reusable/util-assemble-choir-service.jelly), then insert native actions at its [FS markers](../../../jelly/docs/choir-service-assembly.md). The numbered blueprint below remains the manual fallback/reference, not an additional Shortcut to install.

```text
ASSEMBLE CHOIR SERVICE
======================

Shortcut name: UTIL - Assemble Choir Service
Purpose: Select service PDFs, archive clean copies, resolve working scores and apply an ordered setlist.
Input: One Text value exactly interactive.
Output: One Text report on completion, or explanatory Text for deliberate stops.

Category: Reusable
Specification revision: 2
Interface version: 1.0
Target: User-reported iPadOS 26.6; English editor
Required apps: Shortcuts, Files, forScore 15.2.5 where used
Implementation status: Designed
Launch methods: Run Shortcut with Text interactive; direct no-input instructions.
Permissions: Selected Files/iCloud folders; forScore access where used.
Side effects: Interactive file selection, PDF archive/import, metadata and setlist writes.

This is explicitly interactive, including when called. No unattended mode.
Input is required: missing/other Text returns instructions without selection.
Direct launch without input returns those instructions. The generated main
passes interactive. Native Files, Scores and Setlists remain inside this
helper or its native archive helper; no JSON or Dictionary interface is used.
A new score's composer/title are suggested from the filename and confirmed.
Existing scores default to being preserved, with optional metadata review.
New setlist names must be unused. Repeated services use Replace existing and
select the actual target. Return Text reports actions/readback, not success true.

========================
DEPENDENCIES AND BUILD ORDER
========================
Direct dependencies, interface 1.0: UTIL - Canonical Choir Name;
UTIL - Archive Choir PDF. Full dependency-first build order: canonical utility
(Jellycuts), archive helper (native), this helper (native), MAIN - Build Choir
Service (Jellycuts). External services: Nextcloud Files location, iCloud Drive,
forScore. The archive helper owns the only configured archive root.

========================
EDITOR SETUP
========================
Create the exact installed name; no Share Sheet banner needed. Select the
already-working import catalogue action. Build native steps as numbered.
Choose explicit token sources throughout. Empty optional category fields
must stay unset. ForScore action labels here match the user's inventory;
expanded cards may read Get score named Name / Create Setlist Name, etc.
The main is the production launcher. Do not replace the historical diagnostic.
Use text comparisons as shown rather than numeric equality fields that crashed
in the user's editor. Conditional input types must remain Text or native objects
as specified; do not convert Score/Setlist/File tokens to Text.

Notation: Numbers refer to assembly, not editor values. Names in value fields
mean select native variable tokens. Literal values are identified. Input,
Output, Files and Score describe field locations if the exact label differs.
Otherwise/End If/End Repeat/End Menu are automatic markers, not new actions.
NOTE and separators are documentation. For Text containing [Tokens], insert
the named variable tokens, not their brackets. Do not type variable names.

========================
NUMBERED ASSEMBLY
========================

[Shortcut Input]
Type expected: One native Text value; no default; exact allowed value interactive.

1. [If]
Input: Shortcut Input (Text)
Condition: is not
Value: interactive (literal Text)

    2. [Text]
    Launch MAIN - Build Choir Service, or call this helper with Text interactive.

    3. [Stop and Output]
    Output: Text above
    No-recipient behaviour: Respond

[Otherwise]
    Leave empty.
[End If]

4. [Select File]
Select Multiple: On

NOTE: Browse Locations > Nextcloud and select PDFs for one service.
The provider may download them at selection time.

5. [Set Variable]
Variable: SelectedFiles
Input: Files from Select File above

6. [If]
Input: SelectedFiles
Condition: does not have any value

    7. [Text]
    No files selected. No changes made.

    8. [Stop and Output]
    Output: Text above
    No-recipient behaviour: Respond

[Otherwise]
    Leave empty.
[End If]

9. [Count]
Count: Items
Input: SelectedFiles

10. [Set Variable]
Variable: PieceCount
Input: Count above

11. [Repeat]
Count: PieceCount

    12. [Text]
    Choose piece [Repeat Index] of [PieceCount] in the running order.

    NOTE: Insert this Repeat's Repeat Index and the PieceCount token.

    13. [Choose from List]
    List: SelectedFiles
    Prompt: Text above inside this ordering Repeat
    Select Multiple: Off

[End Repeat]

14. [Set Variable]
Variable: OrderedFiles
Input: Repeat Results from the ordering Repeat above

NOTE: Each iteration ends with Choose from List, yielding a native File.
The same file remains selectable for deliberate repetitions. The preview
is authoritative: check no piece was accidentally omitted or repeated.

15. [Repeat with Each]
Input: OrderedFiles
Item type: File

    16. [Get Details of Files]
    Detail: File Extension
    File: Repeat Item from this validation loop

    17. [Change Case]
    Input: File Extension inside this validation loop
    Case: lowercase

    18. [If]
    Input: Changed Text inside this validation loop
    Condition: is not
    Value: pdf (literal Text)

        19. [Text]
        A selected item is not a PDF. No archive/import/setlist writes were started.

        20. [Stop and Output]
        Output: Text above inside this validation loop
        No-recipient behaviour: Respond

    [Otherwise]
        Leave empty.
    [End If]

    21. [Get Details of Files]
    Detail: Name
    File: Repeat Item from this validation loop

[End Repeat]

22. [Combine Text]
Text: Repeat Results from validation loop (filename Texts)
Separator: New Lines

23. [Set Variable]
Variable: RunningOrder
Input: Combined Text above

24. [Ask for Input]
Input Type: Text
Prompt: Service name including date, for example 2026-10-18 - Evensong
Default Answer: Leave empty
Allow Multiple Lines: Off

25. [Replace Text]
Find: ^\s+|\s+$
Replace With: Leave empty
Input: Provided Input from Ask for Input above
Regular Expression: On
Case Sensitive: On

26. [Set Variable]
Variable: ServiceName
Input: Updated Text above

27. [If]
Input: ServiceName
Condition: does not have any value

    28. [Text]
    A service name is required. No changes made.

    29. [Stop and Output]
    Output: Text above
    No-recipient behaviour: Respond

[Otherwise]
    Leave empty.
[End If]

30. [Text]
[ServiceName]

[RunningOrder]

Continue to save clean PDFs and prepare working scores.
Existing scores are preserved unless you choose Review metadata.
Setlist entries are applied only after every score is ready.

NOTE: Insert ServiceName and RunningOrder tokens in the indicated positions.

31. [Show Alert]
Title: Confirm this service
Message: Text above
Show Cancel Button: On

32. [Nothing]

33. [Set Variable]
Variable: PreparedScores
Input: Nothing above

34. [Text]
[ServiceName]

NOTE: Insert ServiceName only.

35. [Set Variable]
Variable: SummaryLines
Input: Text above

36. [Repeat with Each]
Input: OrderedFiles
Item type: File

    37. [Set Variable]
    Variable: SourceFile
    Input: Repeat Item from this preparation loop

    38. [Get Details of Files]
    Detail: Name
    File: SourceFile

    39. [Run Shortcut]
    Shortcut: UTIL - Canonical Choir Name
    Input: Name above inside preparation loop

    40. [Set Variable]
    Variable: CanonicalStem
    Input: Shortcut Result from naming utility above

    41. [If]
    Input: CanonicalStem
    Condition: does not have any value

        42. [Text]
        Empty music identity. Service incomplete; earlier preparation may have completed.

        43. [Stop and Output]
        Output: Text above
        No-recipient behaviour: Respond

    [Otherwise]
        Leave empty.
    [End If]

    44. [Run Shortcut]
    Shortcut: UTIL - Archive Choir PDF
    Input: SourceFile

    45. [Set Variable]
    Variable: CleanFile
    Input: Shortcut Result from archive helper above (native File)

    46. [If]
    Input: CleanFile
    Condition: does not have any value

        47. [Text]
        No clean PDF returned for [CanonicalStem]. Service incomplete.
        Inspect the archive before retrying. Earlier pieces may be prepared.

        NOTE: Insert this preparation iteration's CanonicalStem.

        48. [Stop and Output]
        Output: Text above
        No-recipient behaviour: Respond

    [Otherwise]
        Leave empty.
    [End If]

    49. [Get score]
    Name: CanonicalStem
    Continue if not found: On
    Composers / Genres / Tags / Labels: Leave unset
    Reference: Leave empty

    50. [If]
    Input: Score output from this Get score
    Condition: has any value

        51. [Set Variable]
        Variable: WorkingScore
        Input: Score output from existing-score Get score above

        52. [Text]
        reused

        53. [Set Variable]
        Variable: ImportState
        Input: Text reused above

        54. [List]
        Reuse unchanged
        Review metadata

        55. [Choose from List]
        List: List immediately above
        Prompt: Existing score found. Preserve it, or review metadata?
        Select Multiple: Off

        56. [Set Variable]
        Variable: MetadataMode
        Input: Chosen Item from existing-score choice above

    [Otherwise]

        57. [Import file(s)]
        Files: CleanFile
        Conflict Handling: Skip

        NOTE: Use the same import catalogue action that worked in the earlier
        diagnostic. If that was Import score(s), select it instead and record
        that choice. Add only one import action. Its raw result is not used.

        58. [Get score]
        Name: CanonicalStem
        Continue if not found: On
        Composers / Genres / Tags / Labels: Leave unset
        Reference: Leave empty

        59. [If]
        Input: Score output from Get score after import
        Condition: does not have any value

            60. [Text]
            Import is unconfirmed for [CanonicalStem].
            Clean PDF may already be saved. Inspect forScore before retrying.
            No setlist entries have been replaced by this run.

            NOTE: Insert CanonicalStem.

            61. [Stop and Output]
            Output: Text above
            No-recipient behaviour: Respond

        [Otherwise]
            Leave empty.
        [End If]

        62. [Set Variable]
        Variable: WorkingScore
        Input: Score output from Get score after import

        63. [Text]
        imported

        64. [Set Variable]
        Variable: ImportState
        Input: Text imported above

        65. [Text]
        Review metadata

        66. [Set Variable]
        Variable: MetadataMode
        Input: Text Review metadata above

    [End If]

    67. [If]
    Input: MetadataMode
    Condition: is
    Value: Review metadata (literal Text)

        68. [Text]
        -

        69. [Set Variable]
        Variable: ComposerSuggestion
        Input: Text hyphen above

        70. [Set Variable]
        Variable: TitleSuggestion
        Input: CanonicalStem

        71. [Match Text]
        Pattern: ^(?!(?:NEH[0-9]|Ps[0-9]|OH[0-9]|[0-9]|Hy-|RSC-))(?!.*-Hebdom)[^-]+-.+$
        Text: CanonicalStem
        Case Sensitive: Off

        72. [If]
        Input: Matched Text from this metadata classification
        Condition: has any value

            73. [Replace Text]
            Find: ^([^-]+)-(.+)$
            Replace With: $1 (literal replacement)
            Input: CanonicalStem
            Regular Expression: On
            Case Sensitive: On

            74. [Set Variable]
            Variable: ComposerSuggestion
            Input: Updated Text from composer replacement above

            75. [Replace Text]
            Find: ^([^-]+)-(.+)$
            Replace With: $2 (literal replacement)
            Input: CanonicalStem
            Regular Expression: On
            Case Sensitive: On

            76. [Set Variable]
            Variable: TitleSuggestion
            Input: Updated Text from title replacement above

        [Otherwise]
            Leave empty. Uncertain patterns keep composer as a hyphen.
        [End If]

        77. [Replace Text]
        Find: ([a-z])([A-Z])
        Replace With: $1 $2 (literal replacement)
        Input: TitleSuggestion
        Regular Expression: On
        Case Sensitive: On

        78. [Replace Text]
        Find: -
        Replace With: space-hyphen-space (type one space, -, one space)
        Input: Updated Text from CamelCase replacement above
        Regular Expression: Off
        Case Sensitive: On

        79. [Ask for Input]
        Input Type: Text
        Prompt: Confirm readable title. Preserve movement and variant details.
        Default Answer: Updated Text from hyphen replacement above
        Allow Multiple Lines: Off

        80. [Replace Text]
        Find: ^\s+|\s+$
        Replace With: Leave empty
        Input: Provided Input from title Ask for Input above
        Regular Expression: On
        Case Sensitive: On

        81. [Set Variable]
        Variable: DisplayTitle
        Input: Updated Text above

        82. [If]
        Input: DisplayTitle
        Condition: does not have any value

            83. [Text]
            Empty title. Working score may already be imported.
            Rerun and choose Review metadata to finish it.

            84. [Stop and Output]
            Output: Text above
            No-recipient behaviour: Respond

        [Otherwise]
            Leave empty.
        [End If]

        85. [Ask for Input]
        Input Type: Text
        Prompt: Confirm composer. Enter a single hyphen if unknown or not applicable.
        Default Answer: ComposerSuggestion
        Allow Multiple Lines: Off

        86. [Replace Text]
        Find: ^\s+|\s+$
        Replace With: Leave empty
        Input: Provided Input from composer Ask for Input above
        Regular Expression: On
        Case Sensitive: On

        87. [Set Variable]
        Variable: ComposerName
        Input: Updated Text above

        88. [Rename score]
        Scores: WorkingScore
        Name: DisplayTitle

        89. [If]
        Input: ComposerName
        Condition: has any value

            90. [If]
            Input: ComposerName
            Condition: is not
            Value: - (literal Text)

                91. [Find composer]
                Name: ComposerName
                Continue if not found: On

                NOTE: The screenshot-expanded card reads Get composer named Name.

                92. [If]
                Input: Composer output from Find composer above
                Condition: has any value

                    93. [add metadata]
                    Score: WorkingScore
                    Bookmarks: Leave empty
                    Composers: Composer output from Find composer above
                    Genres / Tags / Labels: Leave unset

                [Otherwise]

                    94. [Create composer]
                    Name: ComposerName
                    Scores: WorkingScore
                    Bookmarks: Leave empty

                    NOTE: The screenshot shows creation can add directly to
                    Scores and/or Bookmarks. Do not add a second redundant
                    Add metadata action after successful create-and-assign.

                [End If]

            [Otherwise]
                Leave empty. Hyphen means no composer assignment.
            [End If]

        [Otherwise]
            Leave empty. Empty composer also means no assignment.
        [End If]

    [Otherwise]
        Leave empty. Existing metadata is preserved.
    [End If]

    95. [Add to Variable]
    Variable: PreparedScores
    Input: WorkingScore (native Score, not its display Text)

    96. [Text]
    [CanonicalStem]: [ImportState]; metadata mode: [MetadataMode]

    NOTE: Insert the three named Text variables from this iteration.
    This reports executed paths, not a fabricated receipt for metadata.

    97. [Add to Variable]
    Variable: SummaryLines
    Input: Text from this preparation iteration

[End Repeat]

NOTE: PreparedScores is built explicitly with native Score objects.
Repeat Results are unused; the final report action is not the score output.

98. [List]
Create new
Replace existing

99. [Choose from List]
List: List above
Prompt: Create a service with an unused name, or replace an existing running order?
Select Multiple: Off

100. [Set Variable]
Variable: SetlistMode
Input: Chosen Item from mode selection above

101. [If]
Input: SetlistMode
Condition: is
Value: Create new (literal Text)

    102. [new setlist]
    Name: ServiceName
    Folder: Leave unset

    NOTE: Screenshot-expanded label is Create Setlist Name.
    Use an unused name; the singular creation output is not assumed.

[Otherwise]
    Leave empty. The existing setlist will be selected below.
[End If]

103. [Get all setlists]

104. [Choose from List]
List: Setlists output from Get all setlists above
Prompt: Select the service to receive this running order (the new one, or the existing one to replace).
Select Multiple: Off

105. [Set Variable]
Variable: TargetSetlist
Input: Chosen Item from setlist selection above (native Setlist)

106. [Text]
[RunningOrder]

Apply this running order to the setlist you just selected?
Replace existing clears that setlist's entries first.
Scores and clean PDFs are retained.

NOTE: Insert RunningOrder. The selected setlist is the actual target;
ServiceName was the requested name and may differ for an existing choice.

107. [Show Alert]
Title: Apply service running order
Message: Text above
Show Cancel Button: On

108. [If]
Input: SetlistMode
Condition: is
Value: Replace existing (literal Text)

    109. [Remove all setlist entries]
    Setlist: TargetSetlist

[Otherwise]
    Leave empty.
[End If]

110. [Repeat with Each]
Input: PreparedScores
Item type: Score

    111. [add scores to setlist]
    Scores: Repeat Item from this setlist-writing loop
    Setlist: TargetSetlist
    Skip if already added: Off

[End Repeat]

NOTE: Order is supplied one score at a time. Skip is off to retain deliberate
repetitions. Confirm actual order in the following readback. Loop results
from entry-addition actions are not used.

112. [Get setlist entries]
Setlist: TargetSetlist
Sorting: Manual

113. [Set Variable]
Variable: ActualEntries
Input: Entries from Get setlist entries above

114. [Count]
Count: Items
Input: ActualEntries

115. [Set Variable]
Variable: ActualCount
Input: Count above

116. [Count]
Count: Items
Input: PreparedScores

117. [Set Variable]
Variable: RequestedCount
Input: Count of PreparedScores above

118. [Combine Text]
Text: SummaryLines
Separator: New Lines

119. [Set Variable]
Variable: PreparationReport
Input: Combined Text above

120. [Text]
[PreparationReport]

Requested entries: [RequestedCount]
Readback entries: [ActualCount]
The running order was submitted to the selected setlist.
Check its Manual-order readback and metadata in forScore.
Count equality alone does not verify order or score identity.

NOTE: Insert PreparationReport, RequestedCount and ActualCount tokens.

121. [Set Variable]
Variable: ServiceReport
Input: Text above

122. [Quick Look]
Input: ActualEntries

123. [open setlist]
Setlist: TargetSetlist

124. [Stop and Output]
Output: ServiceReport (Text)
No-recipient behaviour: Respond

========================
EXPECTED TEST RESULTS
========================
T1 - Integrated first service: launch the generated main, choose two PDFs,
order B then A, archive missing sources, reuse one score and import one, confirm
title/composer, create an unused service and inspect B then A in Manual order.
Actual result: Not run
T2 - Repeat the service: select Replace existing and the same setlist. Stable
lookup reuses scores/archives. Choose Review metadata for any incomplete item.
Actual result: Not run
T3 - Invalid mode/no input: direct launch without input returns instructions;
no selection or writes. Non-PDF selection stops before preview writes.
Actual result: Not run
T4 - Cancel initial preview: no archive/import/setlist writes. Later cancellation
may leave prepared scores or, after replacement starts, a partial setlist.
Actual result: Not run
T5 - Call via main: helper receives interactive Text; the returned service
report is displayed by the main if navigation returns control.
Actual result: Not run

========================
BUILD NOTES
========================
The native helper deliberately owns UI and forScore objects so the generated
caller only passes/receives Text. Keeping this workflow together reduces build
and integration cost; extract further utilities only when actually useful.
No filename property or whole-library-first-item lookup is used. The original
PDF stem remains a demonstrated lookup key after the test score was renamed.
Duplicate-name behaviour is not established: keep canonical identities unique.
Composer suggestions exclude special hymn/psalm/office/Proper/Hebdom/RSC
patterns. Review every proposed value; genre/tag automation is not included.
Changing a composer through Add metadata may add alongside existing composers;
this release does not automatically remove existing metadata.
Before commit, all sources have resolved and PreparedScores holds the intended
sequence. Replacement writes are non-transactional, with explicit confirmation.
Caller example: main-build-choir-service.jelly passes Text interactive through
Run Shortcut, captures the helper's report, and explicitly outputs that Text.

========================
ERRORS AND LIMITATIONS
========================
Cancellation or native action/provider errors can halt without an output.
Earlier writes are not rolled back. No If after an action catches an error
that prevented it from completing. Inspect actual state before retrying.
Select File options; native composer values in Add metadata; creation/assignment
outputs and effects; setlist collection selection, removal and ordered addition;
Manual entries readback/Quick Look; return-to-caller after open setlist. Resolve
any differences in the integrated build and retain actual failures as evidence.

========================
IMPLEMENTATION RECORD
========================
Current status: Designed
Static review: 2026-10-15; native variable paths, branches and dependencies reviewed.
Built revision / builder / device / date: Not built
Executed results: Not run
Resolve the open settings in the integrated service build, not as a separate
campaign of tests. Record exact changes/errors; update this spec afterward.

========================
CHANGE HISTORY
========================
Revision 2 | Interface 1.0 | 2026-10-16
Preferred construction now uses generated Jelly source and native FS insertions;
the manual action sequence below remains a reference/fallback. No contract change.

Revision 1 | Interface 1.0 | 2026-10-15
Initial production candidate. Build these actions once; no migration of the
historical diagnostic or existing user-built experiments is required.

========================
SOURCES AND OPEN VERIFICATION
========================
User screenshots/action inventory and native Get score/rename observations.
Apple variable, repeat, Dictionary and file action semantics support the design;
selected provider settings and forScore contracts still need device confirmation.
VERIFY ON DEVICE during first service: Select File options; native composer values in Add metadata; creation/assignment
outputs and effects; setlist collection selection, removal and ordered addition;
Manual entries readback/Quick Look; return-to-caller after open setlist. Resolve
any differences in the integrated build and retain actual failures as evidence.
```

Dependencies: [Canonical Choir Name](../../../jelly/shortcuts/reusable/util-canonical-choir-name.jelly), [Archive Choir PDF](util-archive-choir-pdf.md).

Caller: [MAIN - Build Choir Service](../../../jelly/shortcuts/main/main-build-choir-service.jelly). [Installation guide](../../../jelly/docs/choir-service-build.md), [integration record](../../../jelly/tests/choir-service.md).

Sources: [device evidence](../../../forscore-action-evidence.md), [action inventory](../../../forscore%20shortcut%20actions.md), [Apple repeats](https://support.apple.com/en-gb/guide/shortcuts/apdc11deb2c1/ios), [Apple variables](https://support.apple.com/en-gb/guide/shortcuts/apdd02c2780c/ios).
