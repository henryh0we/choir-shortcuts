Preferred build updated 16 October 2026: [generate this helper from Jelly source](../../../jelly/shortcuts/reusable/util-archive-choir-pdf.jelly), then complete its [CFG markers](../../../jelly/docs/choir-service-assembly.md). The numbered blueprint below remains the manual fallback/reference, not an additional Shortcut to install.

```text
ARCHIVE CHOIR PDF
=================

Shortcut name: UTIL - Archive Choir PDF
Purpose: Reuse or save a clean canonical PDF in the existing iCloud type folders.
Input: One native PDF File, required.
Output: One native clean File; validation/ambiguity returns no content after an alert.

Category: Reusable
Specification revision: 2
Interface version: 1.0
Target: User-reported iPadOS 26.6; English editor
Required apps: Shortcuts, Files, forScore 15.2.5 where used
Implementation status: Designed
Launch methods: Native Run Shortcut with one File; direct no-input diagnostic.
Permissions: Selected Files/iCloud folders; forScore access where used.
Side effects: Saves clean PDFs in the configured iCloud folder; no forScore writes.

Direct execution without input shows an alert and returns no content.
Called execution accepts one File and may prompt for type only if absent.
Source content is saved before working metadata edits. No input/source file
is intentionally modified. Type-folder selection is always interactive.
No Text path, URL or multi-file input is supported. Cloud-provider errors may
halt; a saved File is not proof that upload to every device has completed.

========================
DEPENDENCIES AND BUILD ORDER
========================
Direct dependency: UTIL - Canonical Choir Name, interface 1.0.
Build it in Jellycuts first, then this native helper. External service: iCloud Drive.
No dependency on the old folder-creation Shortcut; existing folders are reused.

========================
EDITOR SETUP
========================
Create the exact installed name. No Share Sheet banner required. Set the
Folder action once to the existing Library root. Keep only type folders at
that root. Configure explicit native Files for every Run Shortcut/Save field.

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
Type expected: One native File; no default or inferred path conversion.

1. [Folder]
Folder: Select existing iCloud Choir Music/Library once, during construction.

2. [Set Variable]
Variable: ArchiveRoot
Input: Folder from the configuration action above

3. [If]
Input: Shortcut Input
Condition: does not have any value

    4. [Show Alert]
    Title: No source PDF
    Message: Call this helper with one PDF File.
    Show Cancel Button: Off

    5. [Nothing]

    6. [Stop and Output]
    Output: Nothing above
    No-recipient behaviour: Do Nothing

[Otherwise]
    Leave empty.
[End If]

7. [Count]
Count: Items
Input: Shortcut Input

8. [Text]
[Count]

NOTE: Insert the Count output above, with no spaces or extra lines.

9. [If]
Input: Text from Count above
Condition: is not
Value: 1 (literal Text)

    10. [Show Alert]
    Title: One PDF required
    Message: Supply exactly one native File.
    Show Cancel Button: Off

    11. [Nothing]

    12. [Stop and Output]
    Output: Nothing above
    No-recipient behaviour: Do Nothing

[Otherwise]
    Leave empty.
[End If]

13. [Get Details of Files]
Detail: File Extension
File: Shortcut Input

14. [Change Case]
Input: File Extension above
Case: lowercase

15. [If]
Input: Changed Text above
Condition: is not
Value: pdf (literal Text)

    16. [Show Alert]
    Title: PDF required
    Message: No file has been saved.
    Show Cancel Button: Off

    17. [Nothing]

    18. [Stop and Output]
    Output: Nothing above
    No-recipient behaviour: Do Nothing

[Otherwise]
    Leave empty.
[End If]

19. [Set Variable]
Variable: SourceFile
Input: Shortcut Input

20. [Get Details of Files]
Detail: Name
File: SourceFile

21. [Run Shortcut]
Shortcut: UTIL - Canonical Choir Name
Input: Name from Get Details of Files above

22. [Set Variable]
Variable: CanonicalStem
Input: Shortcut Result from canonical helper above

23. [If]
Input: CanonicalStem
Condition: does not have any value

    24. [Show Alert]
    Title: Empty music identity
    Message: A file named only .pdf is not supported.
    Show Cancel Button: Off

    25. [Nothing]

    26. [Stop and Output]
    Output: Nothing above
    No-recipient behaviour: Do Nothing

[Otherwise]
    Leave empty.
[End If]

27. [Nothing]

28. [Set Variable]
Variable: ArchiveMatches
Input: Nothing above

29. [Get Contents of Folder]
Folder: ArchiveRoot
Recursive: On

30. [Repeat with Each]
Input: Contents of Folder above
Item type: File or Folder

    31. [Get Details of Files]
    Detail: File Extension
    File: Repeat Item from this archive search loop

    32. [Change Case]
    Input: File Extension inside this loop
    Case: lowercase

    33. [If]
    Input: Changed Text inside this loop
    Condition: is
    Value: pdf (literal Text)

        34. [Get Details of Files]
        Detail: Name
        File: Repeat Item from this archive search loop

        35. [Run Shortcut]
        Shortcut: UTIL - Canonical Choir Name
        Input: Name inside this loop

        36. [If]
        Input: Shortcut Result from canonical helper inside this loop
        Condition: is
        Value: CanonicalStem (native Text token)

            37. [Add to Variable]
            Variable: ArchiveMatches
            Input: Repeat Item from this archive search loop

        [Otherwise]
            Leave empty.
        [End If]

    [Otherwise]
        Leave empty.
    [End If]

[End Repeat]

NOTE: Loop results are unused. Only matched native Files are added to
ArchiveMatches. Each iteration's incidental output is ignored.

38. [If]
Input: ArchiveMatches
Condition: has any value

    39. [Count]
    Count: Items
    Input: ArchiveMatches

    40. [Text]
    [Count]

    NOTE: Insert Count of ArchiveMatches with no spaces/newlines.

    41. [If]
    Input: Text from Count of ArchiveMatches
    Condition: is
    Value: 1 (literal Text)

        42. [Get Item from List]
        Get: First Item
        List: ArchiveMatches

        43. [Stop and Output]
        Output: Item from List above (native File, not its name)
        No-recipient behaviour: Do Nothing

    [Otherwise]

        44. [Show Alert]
        Title: Multiple clean copies found
        Message: Resolve the duplicate canonical filenames in iCloud before running again.
        Show Cancel Button: Off

        45. [Nothing]

        46. [Stop and Output]
        Output: Nothing above
        No-recipient behaviour: Do Nothing

    [End If]

[Otherwise]
    Leave empty.
[End If]

47. [Get Contents of Folder]
Folder: ArchiveRoot
Recursive: Off

48. [Choose from List]
List: Contents of Folder immediately above
Prompt: Choose the existing music-type folder for this PDF.
Select Multiple: Off

49. [Set Variable]
Variable: TypeFolder
Input: Chosen Item above (native Folder)

NOTE: ArchiveRoot's immediate children must be type folders, not PDFs
or loose documents. Move loose documents elsewhere during setup.

50. [Text]
[CanonicalStem].pdf

NOTE: Insert CanonicalStem then the literal .pdf.

51. [Set Name]
Input: SourceFile
Name: Text from canonical filename above

NOTE: Use Set Name, not Rename File. Inspect the resulting name during
build so it ends in exactly one .pdf; extension options vary by editor.

52. [Save File]
File: Renamed Item from Set Name above
Ask Where to Save: Off
Destination: TypeFolder (native Folder token)
Overwrite If File Exists: Off

53. [Set Variable]
Variable: SavedCleanFile
Input: Saved File from Save File above

54. [Stop and Output]
Output: SavedCleanFile (native File)
No-recipient behaviour: Do Nothing

========================
EXPECTED TEST RESULTS
========================
Use the integrated service run in the linked guide.
T1: Call with a new disposable PDF -> choose a type folder, return saved File.
Actual result: Not run
T2: Call with the same PDF -> reuse the existing File without another save.
Actual result: Not run
T3: Missing input -> explanatory alert, no File output or save.
Actual result: Not run
T4: Cancel type selection -> no guaranteed output; no import in this helper.
Actual result: Not run
T5: Two matching archived PDFs -> alert and no File; no automatic overwrite.
Actual result: Not run

========================
BUILD NOTES
========================
Calling example: in Assemble Choir Service, select SourceFile in Run Shortcut
for this helper, capture its native File into CleanFile, then use CleanFile in
forScore Import Files. Do not put the File through Text or JSON.
Set Name changes the content item used for saving; never replace it with a
filesystem Rename File action against the source release.
The full archive is scanned so changing a type choice cannot create a second
canonical copy unnoticed. Availability of cloud placeholders must be resolved
by the provider; retrieval errors are not treated as missing files.

========================
ERRORS AND LIMITATIONS
========================
Cancellation or native action/provider errors can halt without an output.
Earlier writes are not rolled back. No If after an action catches an error
that prevented it from completing. Inspect actual state before retrying.
Folder/File handling in recursive contents; Add to Variable starting empty;
Set Name extension handling; Save File native destination/overwrite setting;
File output across Run Shortcut. Verify these in the first end-to-end run.

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
Preferred construction now uses generated Jelly source and CFG completion;
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
VERIFY ON DEVICE during first service: Folder/File handling in recursive contents; Add to Variable starting empty;
Set Name extension handling; Save File native destination/overwrite setting;
File output across Run Shortcut. Verify these in the first end-to-end run.
```

Dependencies: [UTIL - Canonical Choir Name](../../../jelly/shortcuts/reusable/util-canonical-choir-name.jelly).

Caller/build guide: [Assemble Choir Service](util-assemble-choir-service.md), [installation and scope](../../../jelly/docs/choir-service-build.md).

Sources: [forScore guidance](../../../forscore.md), [Apple variables](https://support.apple.com/en-gb/guide/shortcuts/apdd02c2780c/ios), [Apple repeats](https://support.apple.com/en-gb/guide/shortcuts/apdc11deb2c1/ios).
