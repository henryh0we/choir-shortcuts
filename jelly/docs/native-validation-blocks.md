# Historical native validation proposal (retired)

**Retired:** Archive 13 and Assembly 10 restore executable documented If blocks with direct output(notes: "ERROR: ..."). Do not add the AV/SV/AGUARD/SGUARD/ARETURN/SRETURN native blocks described below to current exports. This page preserves the abandoned proposal for evidence only. Use current source and helper-compatibility-update.md.


Current sources: Archive revision 12 / completed interface 2.0; Assembly revision 9 / completed interface 1.1. User reports both messages and stopping actions missing from generated If bodies. These revisions remove entire affected If blocks and all generated Exit/Output calls. They provide Comment + Nothing insertion slots, not an automatic code-only export fix. New compilation/export/runtime: Not run.

## Before any execution

Duplicate your edited installed copies before reimporting. Immediately replace AGUARD/SGUARD Nothing with native Show Alert and Stop This Shortcut. **The uncompleted source template contains no functioning execution guard. Do not run it until you have inserted a native guard.** Keep the guard until every native slot is finished. Existing ARC/CFG/CONF/COL/SCORE/FS slots still apply.

## How to complete a validation slot

At each AV/SV Comment, replace its following Nothing with the WHOLE native block: If, optional Show Alert, Stop and Output, End If. Put Show Alert and Stop and Output INSIDE If, before End If; never insert the stop unconditionally after End If. Choose native input tokens from their producer actions or existing named variables. `== nil` means does not have any value; `!= nil` means has any value; `==`/`!=` mean is/is not. Quoted interpolations such as `${chosenCategory}` mean the actual variable value, not literal text. For an empty return, leave the Stop and Output result empty and choose Do Nothing if there is nowhere to output. For explanatory Text, set both the alert message and Stop and Output result to the stated message, inserting actual variable tokens where needed. For the successful reuse branch, use native existingCleanFile instead.

If a slot is inside a Repeat or another If, retain that position. Delete only its placeholder Nothing after inserting the complete block. If a Comment is also missing from export, use its position between adjacent named producer actions in source; source comments are not executable validation. Inspect remaining business If/Repeat structures too: this change does not establish the compiler exports other bodies correctly.

## Archive blocks

| Slot | Native If condition | Alert title / message | Stop and Output result |
| --- | --- | --- | --- |
| AV01 | contextCountText != "3" | "Archive input needs updating" / "Supply a native List: one PDF File, Library Folder, parsed config Dictionary." | empty |
| AV02 | configVersionText != "1" | "Unsupported config" / "Only config version 1 is supported." | empty |
| AV03 | libraryFolderName == nil | "Missing Library name" / "Set libraryFolder in config.json." | empty |
| AV04 | actualLibraryName != "${libraryFolderName}" | "Wrong Library Folder" / "Input item 2 must be the native ${libraryFolderName} Folder beneath Choir Music." | empty |
| AV05 | prefixRegex == nil | "Missing prefix pattern" / "Set prefixRegex in config.json." | empty |
| AV06 | categories == nil | "Missing categories" / "Set a nonempty categories array in config.json." | empty |
| AV07 | sourceFile == nil | "No source PDF" / "Supply one PDF File." | empty |
| AV08 | inputCountText != "1" | "One PDF required" / "Supply exactly one PDF File." | empty |
| AV09 | lowerExtension != "pdf" | "PDF required" / "No file saved. Select a PDF." | empty |
| AV10 | canonicalStem == nil | "Empty music identity" / "A file named only .pdf is not supported." | empty |
| AV11 | existingCleanFile != nil | "Multiple clean copies" / "Resolve duplicate canonical PDFs in iCloud before retrying." | empty |
| AV12 | existingCleanFile != nil | None; successful archive reuse | native existingCleanFile |
| AV13 | chosenCategory == nil | None (cancelled category selection) | empty |
| AV14 | typeFolder != nil | "Ambiguous category" / "Multiple Library children match the selected category." | empty |
| AV15 | typeFolder == nil | "Category folder missing" / "Library has no folder named ${chosenCategory}. Fix config.json or the folders." | empty |

## Assembly blocks

| Slot | Native If condition | Alert title / message | Stop and Output result |
| --- | --- | --- | --- |
| SV01 | ShortcutInput != "interactive" | "Service stopped" / "Launch MAIN - Build Choir Service." | same explanatory Text |
| SV02 | configVersionText != "1" | "Service stopped" / "Only config.json version 1 is supported. No changes made." | same explanatory Text |
| SV03 | prefixRegex == nil | "Service stopped" / "config.json needs a nonempty prefixRegex. No changes made." | same explanatory Text |
| SV04 | categories == nil | "Service stopped" / "config.json needs a nonempty categories array. No changes made." | same explanatory Text |
| SV05 | libraryFolderName == nil | "Service stopped" / "config.json needs libraryFolder. No changes made." | same explanatory Text |
| SV06 | libraryRoot != nil | "Service stopped" / "Multiple root children match libraryFolder. No changes made." | same explanatory Text |
| SV07 | libraryRoot == nil | "Service stopped" / "Choir Music has no folder named ${libraryFolderName}. No changes made." | same explanatory Text |
| SV08 | chosenServiceType == nil | "Service stopped" / "No service type selected. No changes made." | same explanatory Text |
| SV09 | selectedFiles == nil | "Service stopped" / "No files selected. No changes made." | same explanatory Text |
| SV10 | lowerExtension != "pdf" | "Service stopped" / "A selected item is not a PDF. No changes made." | same explanatory Text |
| SV11 | serviceName == nil | "Service stopped" / "A service name is required. No changes made." | same explanatory Text |
| SV12 | canonicalStem == nil | "Service stopped" / "Empty music identity. Earlier pieces may already be prepared." | same explanatory Text |
| SV13 | cleanFile == nil | "Service stopped" / "No clean PDF returned for ${canonicalStem}. Inspect archive before retrying." | same explanatory Text |
| SV14 | importedScore == nil | "Service stopped" / "Import unconfirmed for ${canonicalStem}. Inspect forScore before retrying. Setlist entries have not been replaced." | same explanatory Text |
| SV15 | displayTitle == nil | "Service stopped" / "Empty title. Rerun and choose Review metadata to finish any imported score." | same explanatory Text |

## Final returns and completion

ARETURN / CFG04: native Stop and Output returning savedCleanFile from Save File. The successful existing-file AV block replaces CFG03 and must return named native existingCleanFile. SRETURN: native Stop and Output returning the report Text serviceReport. No filename/Text conversion on archive returns.

After completing every slot, remove only AGUARD/SGUARD's temporary unconditional stop and optional alert. Preserve validation stops and both File returns. Keep archive's receiving contract as native List [PDF File, Library Folder, config Dictionary]; Assembly receives Text interactive. No input/config interface changed.

Check a missing prefixRegex using a disposable config: alert must appear and execution must stop before save/import. Then check valid archive save and reuse return native Files. Perform the existing integrated service run before relying on the workflow. These are native block repairs requiring inspection, not a claimed successful Jelly compiler fix.
