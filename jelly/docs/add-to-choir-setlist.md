# Add pieces to an existing choir setlist

## Shortcut contract

**Installed name:** `MAIN - Add Pieces to Choir Setlist` (thin launcher) and `UTIL - Add to Choir Setlist` (workflow).

Launch the MAIN shortcut directly. It passes Text `interactive` to the utility. The utility reads the same Choir Music `config.json` as the service builder, resolves the configured Library Folder, asks you to choose an existing forScore setlist, then opens Files so you can select multiple Nextcloud PDFs. It prompts you to establish append order, prepares each score using the existing canonical-name, archive, import and metadata workflow, then adds them to the selected setlist. Existing entries are kept. The helper never calls Remove all setlist entries.

The selected PDFs must be available through Files/Nextcloud. Select one or more PDFs; running order applies to the new pieces only, and they are appended after the setlist's existing entries. A score already in the setlist may be appended again because `Skip if already added` is Off, matching the service builder's support for deliberate repetitions. Selecting the same setlist entry is not a way to move it; this workflow appends.

## Assembly slots

Compile/import the source using the project's established Jellycuts workflow. Keep its initial guard until every slot below is complete, all If/Repeat blocks and native object connections have been inspected, and required helper shortcuts are reselected.

| Slots | Native action/configuration |
| --- | --- |
| CONF01-CONF02 | Same as `UTIL - Assemble Choir Service`: native Choir Music Folder and `config.json` file from it. Get Dictionary consumes that file. |
| COL01 | Native Add to Variable appends named `orderedFile` File to `orderedFiles` inside the ordering Repeat. |
| COL02 | Native Add to Variable appends `orderedName` Text to `orderedNames` inside PDF validation Repeat. |
| COL03 | Native Add to Variable appends named native `workingScore` to `preparedScores` once per preparation loop. |
| AT01 | Get all setlists in the same forScore library as score lookup. |
| AT02 | Choose from List consumes AT01's Setlists output; returns the selected native Setlist as `targetSetlist`. |
| AT03 | Get score named `canonicalStem`, Continue if not found On; reconnect both complementary presence checks and SCORE01. |
| AT04 | Import file(s), Files=`cleanFile`, Conflict Handling=Skip. |
| AT05 | Get score named `canonicalStem` after import, Continue if not found On; reconnect absence check and SCORE02. |
| SCORE01/SCORE02 | Get Item from List at index 1 from the respective Get score output; Set Variable `workingScore` to this native Score. |
| AT06 | Rename score: Scores=`workingScore`, Name=`displayTitle`. |
| AT07 | Find composer named `composerName`, Continue if not found On. |
| AT08 | Add metadata: Score=`workingScore`, Composers=AT07 native Composer output. |
| AT09 | Create composer named `composerName`, adding to Scores=`workingScore`. |
| AT10 | Inside final Repeat over `preparedScores`, add scores to setlist: Scores=Repeat Item, Setlist=`targetSetlist`, Skip if already added Off. Do not add Remove/Clear actions. |
| AT11 | Get setlist entries for `targetSetlist`, Sorting Manual; reconnect `actualEntries` to Entries output. |
| AT12 | Open setlist with native `targetSetlist`. |

The AT01/AT02 target selection is intentionally before PDF selection and preparation. Recheck the target in the confirmation alert. Preparation occurs before AT10, so ordinary validation/import/metadata errors happen before changing the setlist. A native action failure during AT10 can still leave some additions applied.

The archive call must use the native context List `[Repeat Item PDF, libraryRoot Folder, workflowConfig Dictionary]`; the canonical-name helper receives two Text items `[sourceName, prefixRegex]`. Follow the current [config integration guide](config-integration.md) for native input extraction and archive CFG02-CFG04 setup. Preserve native tokens and reselect installed helper versions after import.

## Verification record

This shortcut is a new draft. It has not been compiled, imported, wired with forScore actions, or run on the iPad. Test with a disposable existing setlist and two PDFs, verify that the existing entries remain, then inspect the appended score identities and Manual order. Also check a score already present in the setlist, cancellation before AT10, and an import/preparation failure before AT10. Record outcomes in `jelly/tests/choir-service.md` or a dedicated test note.
