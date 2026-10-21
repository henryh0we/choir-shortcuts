# Archive native context loop

Archive revision **15**, interface **2.1**, replaces ARC01–ARC03 with the
quoted-index loop used successfully for naming Texts. Whole Repeat Items are
assigned to mutable variables initialized with Nothing. No File, Folder or
Dictionary is interpolated or converted to Text during extraction.

The user has now reported three previews from this probe; see evidence below.
The full archive's save/reuse and native File returns remain separate tests.
The separate [read-only probe](probe-archive-context-loop.jelly) exercises the
same extraction without saving or renaming anything. It has no dependencies and
is not required by production. The earlier failed selector probes are preserved.

## Device test

1. Import the probe as **TEST - Archive Context Loop**. Preserve your working
   Archive copy before importing revision 15.
2. In a temporary caller, select a disposable PDF with **File**, and select a
   test **Library** Folder containing exactly one subfolder, **Responses**.
3. Add a native **Dictionary** with the Number entry `version` = `1`.
4. Add **List**, containing the PDF variable, Library Folder variable and
   Dictionary variable, in that order. Insert native tokens, not typed names.
5. **Run Shortcut** → TEST - Archive Context Loop, input = that List.

Expected previews: the PDF's Name property (which may omit its extension), then
`1` (child count for this one-subfolder fixture), then `1` (config version).
For an existing Library, the middle number must match its actual immediate
child count, including both files and folders. Inspect the loop's three If conditions and assignments;
downstream actions must read current named sourceFile/archiveRoot/workflowConfig,
not the initial Nothing token. Any missing/wrong preview or native-action failure
means the mixed context path has not passed. Receiving settings must retain all
three native items.

After this passes, compile/import Archive 15 and inspect its same connections.
Complete **CFG02–CFG04**, then remove only the initial assembly guard. Test with
your real parsed config and disposable PDF: first save, then reuse the same
canonical PDF without a second save/category prompt. Verify the returned native
File opens as a PDF. Test missing input, a missing config key and a non-PDF; no
archive write should occur. Existing archive integration cases remain required
in [config tests](../config-integration.md).

## Evidence

Subsequent full Archive 15 test: the user fixed its sourceFile presence condition
by changing the expected content type from Text to File. The read-only probe
does not exercise these presence conditions. The user subsequently confirms
replacing literal variable names in the naming-input List with actual variable
tokens resolves the naming/reuse failure. Their installed archive now returns
an existing File, otherwise asks for a category and saves the PDF. See
[integration evidence](../config-integration.md); full service and failure-case
coverage are still pending.

User report, 21 October 2026: the probe returns `Fri4-Humfrey-InEMinor`, then
`13`, then `1`. This is evidence that the three extracted values can feed File
Name, Folder Contents/Count and Dictionary version lookup in that device run.
The middle value differs from the one-subfolder fixture; the actual selected
Folder contents have not been independently confirmed. If that Library contains
13 immediate children, the count is correct. The filename preview is the Name
property, not the canonical naming-helper result, and need not include `.pdf`.
Exact installed source/settings were not supplied for the probe. Its previews
alone do not establish PDF-content preservation or the full archive's behavior;
the later manually repaired save/reuse report is recorded separately above.

Local compiler/structural export checks passed with eight brace/core-node
warnings. Export inspection found the three quoted index branches, native Repeat
Item assignments and current named-variable consumers. The exact command/result is recorded in [config tests](../config-integration.md);
a local export does not establish native type preservation on the iPad.
