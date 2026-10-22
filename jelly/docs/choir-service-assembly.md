# Complete the generated choir Shortcuts

## Integrate the working archive

22 October 2026: the user confirms their manually repaired Archive 15 now saves
new PDFs and returns existing Files. Preserve that installed copy under a backup
name before further work; keep the active name **UTIL - Archive Choir PDF**.
The generated source does not preserve its condition-type, List-token or CFG
repairs. Do not reimport it just for integration.

1. Export/import the now user-confirmed compiled **UTIL - Assemble Choir Service** (source revision 15), keeping
   its initial guard. Complete **CONF01-CONF02**, **COL01-COL03**,
   **SCORE01-SCORE02** and **FS01-FS13** using the tables below.
2. CONF01 selects **Choir Music**; CONF02 reads its `config.json`. Confirm Library
   is resolved from that root and matches the one used for the successful archive
   test. Reselect the installed naming/archive helpers in Run Shortcut actions.
3. Inspect the generated naming-input List: actual sourceName and prefixRegex
   variable tokens; revision 14 uses the now user-confirmed Text interpolation
   form. Inspect archiveInput: actual PDF Repeat Item from this loop,
   native libraryRoot Folder and parsed workflowConfig Dictionary. These must
   not be typed names. Keep native items out of Text interpolation. See
   [the confirmed List defect](../tests/compatibility/list-variable-transport.md).
4. Inspect native condition types and current named-variable inputs, especially
   File and Score presence checks. Reconnect every consumer of replaced Nothing
   slots. Keep Overwrite off and leave Replace existing testing until later.
5. Once all native slots/wiring are complete, remove only Assembly's initial
   guard. Run Assembly directly with Text input `interactive`, using disposable
   PDFs and an unused test service name. Start with one PDF already archived.
   Confirm it is reused, its native score is found/imported, and Create new makes
   a test setlist with the selected score. Inspect the result in forScore.
6. Run a second test with one uniquely named unarchived PDF and one existing PDF.
   Check the category prompt only appears for the new archive item; inspect
   filenames, metadata, returned report and actual Manual setlist order. Then
   test deliberate repeats (A, B, A); verify identities and order, not just count.
7. Install/reselect **MAIN - Build Choir Service** after Assembly passes. Confirm
   its Run Shortcut calls this completed Assembly and returns its report.

Whole-service integration remains **Not run**. Record observed outcomes in
[choir-service tests](../tests/choir-service.md) and required failure cases in
[config tests](../tests/config-integration.md). The older revision/untested notes
below are historical where superseded by the specific installed-archive report.

**Archive 15 update, 21 October 2026:** ARC01-ARC03 manual extraction is replaced
in source by a quoted-index loop, with Nothing-initialized native variables.
Mixed File/Folder/Dictionary preservation is still unverified on the iPad; run
[the read-only context test](../tests/compatibility/archive-context-loop.md).
CFG02-CFG04 remain manual. Preserve the working installed archive and keep the
new initial guard until native extraction and CFG completion are checked.
Earlier ARC instructions below describe revision 14 and are superseded for 15.

**21 October update:** Current sources are Canonical 11 / Archive 15 / Assembly
13 / Main 4. [The pre-iPad review](pre-ipad-review.md) supersedes older current-
revision/Exit instructions below. Keep the existing slot IDs and guards. COL01 now
appends the current named native orderedFile (assigned from chosenOrderedFile);
reconnect its new presence check and all collection Count checks to the current
variables. Main/Canonical now use positional Text Output. Preserve working native
archive edits and inspect new generated actions before execution.

Canonical 11 replaces NAME01/NAME02 with the user-confirmed quoted-index incoming
Text loop. NAME slots are retired. Archive 15 also replaces ARC extraction with a native
loop candidate; SCORE/native collection/forScore slots remain unchanged.

**Current source: Archive 14 / Assembly 11.** The user confirms the small flush-left, parenthesized If probe returns Conditional output reached. The indented parenthesized probe dropped its Output; the unparenthesized probe dropped its If. Both helpers now keep code flush left and use positional `output("ERROR: ...")`, with no notes: label. Literal multiline message whitespace is preserved. Warnings about missing noResultBehaviour and response remain unresolved: the successful probe is not warning-free. This establishes only the tested conditional stop/Text fixture, not interpolation, File returns, nested loops or either complete helper. Existing native ARC/CFG/CONF/COL/SCORE/FS completion remains; no native validation construction is required.



Current archive 9 / assembly 7: follow the [18 October compatibility checklist](helper-compatibility-update.md). Its native selector/collection slots and Exit returns supersede older selector, Output-field and Repeat Results instructions on this page.

17 October 2026. Config-based source revisions: canonical 8, archive 8, assembly 6, main 3. Read [config integration](config-integration.md) for current contracts and setup. Compile all four Jelly files, then finish the marked fields/actions in Apple Shortcuts. Comments explain the required work; Nothing actions are temporary result placeholders. This is a generated template requiring manual completion, not a fully generated forScore integration.

The user's installed Jellycuts build supports `//` line comments, with one source line becoming one separate native Comment block. The user reports that `/* ... */` block comments do not work, despite older compiler-source evidence; use line comments for instructions. All affected production source comments have now been converted to line comments. No guessed `comment()` or forScore function call is used. The native binding for Output handles Text; native File returns therefore have marked fields to reconnect after export. Source evidence and remaining version checks are recorded in [the compiler reference](jellycuts-reference.md).

## Install in dependency order

All current blocks use documented parenthesized syntax. Inspect native If/End If and Repeat/End Repeat markers before removing guards. The first ASSEMBLY GUARD stop is intentionally unconditional; later validation stops belong inside their conditions. Updated exports remain unverified.

1. [UTIL - Canonical Choir Name](../shortcuts/reusable/util-canonical-choir-name.jelly).
2. [UTIL - Archive Choir PDF](../shortcuts/reusable/util-archive-choir-pdf.jelly).
3. [UTIL - Assemble Choir Service](../shortcuts/reusable/util-assemble-choir-service.jelly).
4. [MAIN - Build Choir Service](../shortcuts/main/main-build-choir-service.jelly).

Open each source in Jellycuts 2026.6.4, compile and inspect diagnostics, export/import, and confirm the exact installed name. These files have not been compiled here. Both large helpers start with a Stop and Output assembly guard; retain it until that helper is complete. Incomplete imports should stop before any file/provider/forScore operations. The main has no insertion slots, but calls the guarded assembly helper.

If you already built a helper manually, keep a renamed copy before importing the generated replacement. Use one active Shortcut per exact name. Canonical and archive now require interface 2.0 List inputs. Assembly is interface 1.1; main remains 1.0. Update every caller; preserve the earlier installed setup separately.

## How to fill a slot

Find its ID in a Comment action. Keep the comment for reference.

For a result-producing action, insert the real native action immediately above the next Nothing action. Set its inputs as the comment describes. Reconnect **every downstream use** of the dummy output to the new action's native output, using Select Variable. Then delete the now-unused Nothing action. Deleting Nothing alone does not transfer its Magic Variable UUID to the new action.

Jelly names such as `existingScore`, `canonicalStem` and `workingScore` label outputs in the source. In Apple Shortcuts, identify the producing action in that phase; the token may display Score, Text, Chosen Item or If Result instead. Never replace a Score with its displayed title. Do not treat the content of a Comment as a runnable action.

For an action whose result is unused, insert/configure the native action and remove the adjacent Nothing. No output connection is required. Keep all If, Otherwise, Repeat and End markers in their generated positions.

## Archive helper configuration

Current setup is owned by [config integration](config-integration.md). Old CFG01 is retired: Library comes from input List item 2, resolved once by assembly using config.libraryFolder. Assembly CONF01 now selects the parent Choir Music Folder; CONF02 reads its config.json.

| ID | Complete in Apple Shortcuts |
| --- | --- |
| CFG02 | Save File: Ask Where to Save off, destination = named native typeFolder resolved from selected category Text, input = renamedFile, Overwrite off. |
| CFG03 | Existing-file Stop and Output result = named native existingCleanFile. |
| CFG04 | Final Stop and Output result = native savedCleanFile from Save File. |

Set all empty-result outputs to Do Nothing for no recipient. Keep CFG03/CFG04 native results. Check named-variable and native input/result connections, then remove only the initial guard. The config category picker returns Text, not a Folder; do not wire its Chosen Item directly into Save File. No independent archive-root setting remains.
## forScore actions in the service helper

Labels below use the supplied action inventory; the expanded wording may differ. Keep unspecified category fields unset and Reference empty.

| ID | Action and settings | Downstream output connections |
| --- | --- | --- |
| FS01 | **Get score** named canonicalStem; Continue if not found On | Replace dummy existingScore in BOTH complementary presence/absence Ifs, SCORE01, and the later metadata-choice presence If |
| FS02 | The **Import file(s)** or **Import score(s)** action that worked in your diagnostic; Files = cleanFile; Conflict Handling Skip | None; the next lookup retrieves the score independently |
| FS03 | **Get score** named canonicalStem; Continue if not found On | Replace dummy importedScore in the absence If and Get First Item after import |
| FS04 | **Rename score**: Scores = workingScore; Name = displayTitle | None; workingScore is the named native variable assigned from reuse/import |
| FS05 | **Find composer**, expanded Get composer named Name: composerName; Continue if not found On | Reconnect its presence If and supply this Composer output to FS06 |
| FS06 | **add metadata**: Score = workingScore; Composers = FS05 output; Bookmarks empty; Genres/Tags/Labels unset | None |
| FS07 | **Create composer** named composerName, adding to Scores = workingScore; Bookmarks empty | None; creation also assigns, so no duplicate Add metadata is needed |
| FS08 | **new setlist**, expanded Create Setlist: Name = serviceName; Folder unset | None; selection below retrieves the actual target |
| FS09 | **Get all setlists** | Reconnect the following Choose from List to its Setlists output |
| FS10 | **Remove all setlist entries**: Setlist = targetSetlist | None; keep it inside Replace existing and after all score preparation |
| FS11 | **add scores to setlist**: Scores = Repeat Item from the writing loop; Setlist = targetSetlist; Skip if already added Off | None; this loop's output is unused |
| FS12 | **Get setlist entries**: Setlist = targetSetlist; Sorting Manual | Reconnect the following entry Count to its Entries output |
| FS13 | **open setlist**: Setlist = targetSetlist | None; final Stop and Output still uses serviceReport Text |

All File, Score, Composer and Setlist inputs above are native tokens. The title/composer prompts and canonical lookup stem are Text. The Get First Item actions after FS01/FS03 operate on the individual lookup results, never on a whole library.

The source uses **Get Item from List: Item at Index, 1** wherever these instructions refer to Get First Item. It uses the documented `File Extension` enum throughout. Running-order filenames are joined with ` | ` using Custom, avoiding the unmatched `NewLines` enum spelling; multiline alerts/reports use documented triple-quoted strings.

Check that FS11 uses Repeat Item from the final writing loop, not the preparation loop. Check that the preparation loop's last Get Item from List still yields workingScore; its Repeat Results become preparedScores. The ordering loop ends with Choose from List so its Repeat Results are native Files. Keep comments above their slots, not after those final output actions. These remaining loop/If result captures are compiler-source-backed candidates, not device-confirmed. The optional repeat-capture probe isolates their syntax if the app reports another out-of-scope result.

After completing CONF01-CONF02, all 13 FS slots and the archive helper, remove only the **first** Stop and Output under the service ASSEMBLY GUARD. Leave the guard Comment as the checklist locator. Then run the main with one complete service as described in [the build guide](choir-service-build.md).

## Update and recovery

Manual completion changes the installed Apple Shortcut, not the `.jelly` source. Re-exporting the source produces the same guards/placeholders again. Duplicate the completed installed helpers before replacement, then reapply the CFG/FS table to the new exports and rerun the integrated service check. Installing a Jelly source does not preserve the inserted forScore actions automatically.

The previous [archive](../../manual%20creation/shortcuts/reusable/util-archive-choir-pdf.md) and [assembly](../../manual%20creation/shortcuts/reusable/util-assemble-choir-service.md) blueprints remain reference/fallback descriptions. They are not additional installed dependencies and should not be built alongside generated helpers under duplicate names.

### Historical archive export compatibility correction (16 October 2026)

Archive source revision 3 uses Respond temporarily for all seven empty-result output calls because the user reports that Jellycuts rejects the DoNothing identifier as out of scope. After export, set the no-recipient behaviour on all seven of those Stop and Output actions to Do Nothing, including the CFG03/CFG04 returns. Keep the initial assembly guard until this and CFG01-CFG04 are complete. This workaround has not yet been compiled or tested on the device.
