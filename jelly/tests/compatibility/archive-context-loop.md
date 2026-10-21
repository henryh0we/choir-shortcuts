# Archive native context loop

Archive revision **15**, interface **2.1**, replaces ARC01–ARC03 with the
quoted-index loop used successfully for naming Texts. Whole Repeat Items are
assigned to mutable variables initialized with Nothing. No File, Folder or
Dictionary is interpolated or converted to Text during extraction.

This extends the Text-only evidence; native preservation is **not yet confirmed**.
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

Expected previews: the PDF's filename, then `1` (the Folder child count), then
`1` (config version). Inspect the loop's three If conditions and assignments;
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

Device execution: **Not run** for this probe or the Archive 15 context loop.
Local compiler/structural export checks passed with eight brace/core-node
warnings. Export inspection found the three quoted index branches, native Repeat
Item assignments and current named-variable consumers. The exact command/result is recorded in [config tests](../config-integration.md);
a local export does not establish native type preservation on the iPad.
