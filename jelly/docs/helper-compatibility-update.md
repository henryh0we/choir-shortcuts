# Archive and assembly compatibility update

18 October 2026. Archive revision 9 / completed interface 2.0; assembly revision 7 / completed interface 1.1. These sources are Drafted: no new iPad compiler/export/runtime pass is claimed. This checklist supersedes older instructions to repair empty Output fields or capture Repeat Results for these two revisions. Input contracts and config keys are unchanged.

## What changed

- Replaced every `output(...)` binding with documented `exit(var: ...)`. Guards and service failures first create explanatory Text, then return that token. Archive validation returns Nothing; successful archive paths return native existingCleanFile or savedCleanFile directly. Inspect the exported return tokens.
- Removed all rejected list-selector calls from both helpers. Native ARC01-ARC03 and SCORE01-SCORE02 slots replace them.
- Removed all assembly `} >> result` captures. Named collection variables are initialized from Nothing, then filled by native Add to Variable actions at COL01-COL03. Preserve the named variables and append native objects in order.
- Retained parenthesized conditions/loops, spaced File Extension, and single-line Comment instructions. Config is read once in assembly and passed with native context to archive. No prefix rule is embedded in these helpers.
- Removed assembly Quick Look, whose UI failed in the earlier fixture. The final report and FS13 open-setlist action remain; review Manual order in forScore.
- Matching .txt files are byte-identical source copies. MAIN is unchanged and still contains its older Output binding; direct assembly experiments can supply Text interactive, but full workflow compatibility is not claimed.

## Complete Archive Choir PDF

Keep the initial ASSEMBLY GUARD Text and Exit until all slots are finished. Keep noArchiveResult's Nothing initializer and all later validation/return exits. Receive the complete native three-item List; do not configure this helper as Text-only.

| Slot | Native action or check | Reconnect |
| --- | --- | --- |
| ARC01 | Get Item from List: Shortcut Input, Item at Index 1 (PDF File) | sourceFile presence check, Count, File Details and Set Name inputs |
| ARC02 | Get Item from List: Shortcut Input, Item at Index 2 (Library Folder) | Library name check and both archiveRoot Get Contents of Folder inputs |
| ARC03 | Get Item from List: Shortcut Input, Item at Index 3 (parsed config Dictionary) | All valueFor/Get Dictionary Value Dictionary inputs |
| CFG02 | Save File: native renamedFile; Ask Where to Save off; destination named typeFolder; Overwrite off | Save destination must be the resolved native Folder, not chosenCategory Text |
| CFG03 | Inspect Exit/Stop and Output returning named existingCleanFile | Reselect native File token if necessary; no filename/Text conversion |
| CFG04 | Inspect final Exit/Stop and Output returning savedCleanFile | Reselect native Saved File token if necessary |

For each ARC slot, insert the action before Nothing, reconnect every listed consumer, then delete that unused Nothing. Keep noArchiveMatch/noCategoryFolder initializers and their named variables. The shared naming helper still requires NAME01/NAME02 and two separate Text inputs, filename and configured prefixRegex.

## Complete Assemble Choir Service

Set receiving type to Text and pass interactive. Retain the initial ASSEMBLY GUARD Text and Exit while editing. Keep all collection/workingScore initializers and native named variables.

| Slot | Native action or check | Reconnect |
| --- | --- | --- |
| CONF01 | Folder selecting Choir Music, the parent of config.json and Library | Root Get Contents of Folder and CONF02 |
| CONF02 | Get File from Folder: CONF01 Folder, path config.json, error if absent on | Get Dictionary from Input |
| COL01 | Add to Variable: orderedFile from the immediately preceding ordering Choose from List → orderedFiles | Replace the slot Nothing; keep inside ordering Repeat |
| COL02 | Add to Variable: orderedName from File Details → orderedNames | Replace the slot Nothing; keep inside validation Repeat |
| SCORE01 | Get Item from List: FS01 existingScore lookup, Item at Index 1 | Following Set Variable workingScore |
| SCORE02 | Get Item from List: FS03 importedScore lookup, Item at Index 1 | Following Set Variable workingScore |
| COL03 | Add to Variable: named workingScore → preparedScores | Replace slot Nothing at end of preparation Repeat |
| FS01-FS13 | Native forScore actions in the existing assembly guide | FS01 now feeds the presence check and SCORE01; FS03 feeds its presence check and SCORE02; FS12 feeds entry Count. Final Exit returns serviceReport |

Add to Variable appends; Set Variable replaces the collection and would lose earlier items. For SCORE slots reconnect before deleting Nothing. COL slots have no consumed dummy result: insert Add to Variable, then delete Nothing. Keep these actions inside their original loops/branches.

After all native slots and the archive helper are complete, remove only each helper's initial guard Exit (and optionally its now-unused explanatory Text). Preserve every other Exit, If/Otherwise/End If, Repeat/End Repeat and initializer.

## One integrated check

Inspect exported control-flow markers and named-variable wiring, then use a disposable config and Library. Confirm orderedFiles, orderedNames and preparedScores each accumulate one intended item per iteration; no leading empty item, Text-converted native object or lost repetition. Check ARC indexes return File/Folder/Dictionary respectively. Verify new archive save and existing-file reuse return a native File, category names resolve to native folders, and config edits affect the next run. Finish with two scores and a repeat setlist replacement; review Manual order. Record actual compiler/device outcomes in config-integration tests. No new isolated probe campaign is required.

Source basis: local documented [Exit](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/exit.md) variable returns and [traditional variables](../vendor/jellycuts-docs/markdown/Language_Guide/variables.md). Native action slots deliberately avoid guessing another Jelly selector or append binding.
