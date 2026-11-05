# iPad setup and first compilation experiment

Status: **minimal-variable generation reported; full G1A generation failed**.
The next G1A Compile Jelly Text attempt produced a division/calculation action
containing the Dependencies comment text and an unexpected Stop this shortcut,
visible in the user's screenshot. These are not intended G1A actions. Preserve
that failed output. The user subsequently copied the same code into the Jellycuts
editor, compiled and built, and reports the exact same Calculate-box problem.
This G1A failure is therefore not isolated to Compile Jelly Text. The next probe
removes only the eight header comments in a separate candidate; every executable
statement stays unchanged. See [the header-isolation experiment](../tests/pipeline/README.md#header-isolation-after-both-paths-failed).
The user copied the request folder locally, ran the helper for TEST - Pipeline
Minimal Variable, and reports Nothing → Set Variable currentValue to emptyValue
→ Quick Look currentValue. This matches the intended action sequence; the user
subsequently confirmed the variable token was correct. Exact consumed hash,
repairs and generated-shortcut runtime were not reported. The precise local
launch mode (picker versus Share Sheet) was not stated.
On 5 November the user confirmed the exchanged files appear as expected in Files.
This establishes reported file visibility, not byte-level verification or returned
feedback. Earlier user reports include a Hello World compilation hang followed by
a successful retry, with installed name source from a File-name naming input.
No importable Shortcut is supplied. Upgrade the diagnostic helper manually in
Apple Shortcuts; do not modify working installed choir shortcuts. Jellycuts Bridge
is excluded and no premium Bridge capability is used.

The editor has earlier successful minimal tests, but is not a demonstrated fix
for full G1A: both tested paths produced the same Calculate-box anomaly. Both compilation
actions have also generated incomplete output; see the existing
[path comparison](../tests/ipad-investigation/compilation-path-comparison.md).
An action returning without an error is not a successful generation test.

## Upgrade TEST -Jellycuts Compiler, step by step

This upgrades your existing **TEST -Jellycuts Compiler**. Keep its working
Jellycuts compilation action and any existing app-provided export/install flow.
Add the request-reading and validation actions before it, then reconnect its
source and name inputs. The final target is:

```text
Files → share build folder → Shortcut Input → requestFolder → get request.json
Read manifest → extract build/name/source metadata
Get source.txt from that same folder → verify File hash → preview source Text
Confirm build/name → existing Compile Jelly Text → existing export/install flow
```

The documented Share Sheet experiment starts from **Files**, passing one
build folder into the helper. Both files are then retrieved by their fixed relative
filenames. It replaces Select Folder, which is blocked for OneDrive on this device.
Folder sharing and child-file retrieval through OneDrive remain an iPad test;
visibility in Files does not establish that sharing grants directory access.

**Reported blocker, 5 November:** OneDrive and Jellycuts Exchange are greyed out
in the shortcut's picker while accessible in the Files app. The folder-selection
route is therefore blocked on this device/provider setup. A provider/picker access
limitation is a hypothesis, not a confirmed universal OneDrive restriction.
The subsequent folder Share operation was also reported unavailable/greyed out.

The user then copied the folder over and reports the expected minimal-variable
generation. This supports local staging for that reported fixture, without proving
the precise launch/permission path or end-to-end hash checks. The earlier proposed
isolation procedure was to copy one complete request folder to On My iPad and
retry the helper there. Local staging is a temporary manual transport fallback,
not verified bidirectional sync. Confirm the source hash/metadata on subsequent runs.
Do not change OneDrive accounts, reinstall apps or bypass source-hash checks for
this experiment. Direct OneDrive folder selection remains unresolved.

### 1. Back up the diagnostic helper

1. In Apple Shortcuts find **TEST -Jellycuts Compiler**.
2. Touch and hold its tile, choose **Duplicate**, and name the duplicate
   **TEST -Jellycuts Compiler - Backup**.
3. Open the original helper for editing. This guide leaves its name unchanged.
4. Find the existing **Compile Jelly Text** action. Leave it and its following
   working actions in place while adding the steps below above it.
5. If an existing Get Name action supplies the compiler name, retain it until
   the replacement is connected. Remove it afterwards only if nothing uses it.

Duplicate/rename are editor operations, not actions to insert into the shortcut.
No installed production helper is being replaced.

### 2. Use variable tokens, not typed variable names

In this guide a name such as `sourceText` means a selected variable token.
Typing the letters sourceText into an action field produces literal Text.

To reconnect a field, tap its old variable and clear it, then use the variable
picker/Select Variable to insert the required producer or named variable. Some
parameters require a touch-and-hold to reveal the picker. For every **Set Variable**,
type the variable name into its name field but explicitly select the producing
action in its input field. Do not accept automatic chaining after unrelated
diagnostic actions.

When an If is inserted, Shortcuts supplies Otherwise/End If. Do not insert those
as extra actions. Keep each error alert and Stop This Shortcut **inside its If**;
leave Otherwise empty. An accidentally unconditional Stop would prevent compilation.

### 3. Receive the shared build folder and retrieve request.json

First configure the helper's entry point in the Shortcuts editor:

1. Open its Details/settings and enable **Show in Share Sheet**. The exact
   navigation to Details varies with the installed Shortcuts version.
2. In the Receive input banner, change accepted content from Any to **Folder**
   (or Folders, depending on the UI). Apple lists Folder as a supported input type.
3. If the banner exposes a no-input choice, choose **Stop and Respond** and enter
   `Share one build folder from Files.`. Do not enable a fallback document picker.
4. Remove the existing **Select Folder** action. There is no picker inside this
   route: Files supplies the selection through **Shortcut Input**.

At the beginning of the action sequence add **Count**, type Items, input =
**Shortcut Input**. Add **If** that Count **is not** Number `1`: Show Alert
`Share exactly one build folder`, then Stop This Shortcut inside the If. Put the
remaining actions after End If. This catches empty/multiple input; the Share Sheet
input filter alone is not a general runtime type check for other callers.

Then add or reconnect these actions:

1. **Get Item from List**, First Item, List = **Shortcut Input**. The count guard
   has already required exactly one item; do not silently accept the first of many.
2. **Set Variable**: name `requestFolder`; input = the native Item from step 1.
   Do not select its Name or File Path property and do not force a URL into Folder.
3. **Get File from Folder**: Folder = named `requestFolder`; File Path = literal
   `request.json`. Use a relative filename, without a leading slash or a Windows
   path. If exposed, turn Show Document Picker Off and Error If Not Found On.
   The Folder slot can initially show a fixed folder such as Shortcuts: replace
   it with the requestFolder variable token rather than browsing for a fixed folder.
4. **Set Variable**: name `requestFile`; input = that retrieved native File.
5. **Get Text from Input**: input = named `requestFile`, with no Name property
   selected. This reads the JSON document contents.
6. **Get Dictionary from Input**: input = the Text output from step 5.
7. **Set Variable**: name `request`; input = the Dictionary output from step 6.

To launch it, open **Files**, find the long-ID build folder, touch and hold that
folder and choose **Share**, then select **TEST -Jellycuts Compiler**. Select the
folder itself, not the requests parent or one of its files. Sharing from inside
the OneDrive app may offer different content; test the Files route first.

**Share-input check:** OneDrive may supply a sharing URL or another representation
instead of a usable native Folder. The helper may then be absent from the Folder
Share Sheet, or Get File from Folder may fail. Share Sheet launch is a candidate
workaround, not proof that the picker restriction is bypassed. Do not treat a
OneDrive URL as a directory, download it as Jelly source, or relax hash checks.
If input is unclear, use a separate temporary diagnostic accepting Anything with
only **View Content Graph**, input=Shortcut Input. Share the same folder to that
diagnostic and record whether it receives a Folder, URL, archive or other type.
Apple recommends this inspection technique; the diagnostic must not compile.

If request.json is missing or the Folder cannot be read, stop that attempt. If
the Dictionary action errors, check the retrieved file. Do not feed request.json
itself or its JSON text into Compile Jelly Text. The pipeline's snapshot filenames
are always request.json/source.txt, so no file chooser is needed after the folder.

### 4. Extract the build ID and intended shortcut name

Add these four actions, in this order:

1. **Get Dictionary Value**: choose to get a **Value**; key = literal `build_id`;
   Dictionary = named `request`.
2. **Set Variable**: name `buildId`; input = the preceding Dictionary Value.
3. **Get Dictionary Value**: get Value; key = literal `shortcut_name`;
   Dictionary = named `request` again, not the previous buildId result.
4. **Set Variable**: name `intendedShortcutName`; input = the preceding Value.

Add two guards:

- **If** named buildId **does not have any value**: **Show Alert** `Missing build ID`,
  then **Stop This Shortcut** inside that If.
- **If** named intendedShortcutName **does not have any value**: Show Alert
  `This request has no shortcut_name. Select the new version-2 request.`, then
  Stop This Shortcut inside that If.

If Get Dictionary Value itself aborts on a missing key on your device, treat that
as a missing/invalid request and stop; a following If cannot catch an aborted action.
Do not invent a name, use the generic source filename, or edit an immutable manifest.

For the next test, choose the folder:

```text
20261105T174604824552Z-2b3d695d0fba4a3a8adf96066de49c62
```

Its intendedShortcutName must be **TEST - Pipeline Minimal Variable**. The older
Hello World folder `20261105T172144750788Z-202db3ef506c417c8eff750262eef4a3`
uses version 1 and has no shortcut_name. The feedback-template.json open in VS Code
is for reporting later; it is not the request to select for this upgrade test.

### 5. Extract the original filename and expected source hash

The `source` field is a nested Dictionary. Access it first; do not enter
`source.filename` as a single key.

1. **Get Dictionary Value**: Value; key = literal `source`; Dictionary = `request`.
2. **Set Variable**: name `sourceInfo`; input = that nested Dictionary Value.
3. **Get Dictionary Value**: Value; key = literal `filename`; Dictionary = `sourceInfo`.
4. **Set Variable**: name `originalSourceFilename`; input = the preceding Value.
5. **Get Dictionary Value**: Value; key = literal `delivered_sha256`;
   Dictionary = `sourceInfo` again, not originalSourceFilename.
6. **Set Variable**: name `expectedHash`; input = the preceding Value.
7. **If** named expectedHash **does not have any value**: Show Alert
   `Missing source hash`, then Stop This Shortcut inside that If.

Expected values for the selected test are:

```text
originalSourceFilename: minimal-variable.txt
expectedHash: 02e6099570c2aa5af935e95c4055b9b5e7ddfa72875a1a4cfb150cb0793a3cd2
```

The original filename is context for review. It is not the installed name.

### 6. Retrieve source.txt from the same selected folder

Replace the old source **Select File** action with another **Get File from Folder**.
This is automatic retrieval, not a second selection:

1. **Get File from Folder**: Folder = named `requestFolder` from step 3;
   File Path = literal `source.txt`. If exposed, Show Document Picker Off;
   Error If Not Found On.
2. **Set Variable**: name `sourceFile`; input = this Get File from Folder's
   native File output.
3. Reselect the new File output if an old token used the removed Select File or
   had its Name property selected. Reconnect downstream hashing/text extraction
   to named sourceFile. Do not connect them to requestFile by automatic chaining.

Use source.txt for this helper. source.jelly is the byte-identical editor-opening
alias. feedback-template.json is neither source alias. Keep the source/name/hash
steps below unchanged; the only user selection is the folder shared from Files.

**Provider check:** the retrieved requestFile and sourceFile must come from the
selected OneDrive build folder. If the action cannot accept that Folder token or
asks for another selection, record its actual fields/error before changing the
design. Do not silently substitute a fixed iCloud folder or path Text. These are
native Shortcuts actions; no new Jelly binding or Windows pipeline change is needed.

### 7. Verify the selected File's SHA-256

1. Add **Generate Hash** (search Hash), input = named `sourceFile`.
2. Select **SHA-256** as its algorithm. Do not leave a different default algorithm.
3. Add **Change Case** / Change Text Case: case = **lowercase**; input = the Hash
   output. This normalizes only the hex hash's letter case, never source content.
4. Add **Set Variable**: name `actualHash`; input = that lowercase Text output.
5. Add **If** named actualHash **is not** named expectedHash. Both comparison
   operands must be variable tokens, not typed variable names.
6. Inside that If add **Show Alert**, title `Source hash mismatch`, message with
   actualHash and expectedHash tokens on labelled lines; then **Stop This Shortcut**.

Device check: Generate Hash must hash the File contents. The expected hash above
is the raw 102-byte LF file. If the app hashes another representation, an option is
missing, or the result differs, stop this attempt and report both hashes/settings.
Do not bypass the mismatch or rewrite the source to force a pass. This upgraded
hash path has not been tested on the physical iPad.

### 8. Read and preview the actual source Text

1. Reuse/add **Get Text from Input**: input = named `sourceFile`, not its Name.
2. Add **Set Variable**: name `sourceText`; input = that Get Text output.
3. Add **If** sourceText **does not have any value**: Show Alert `No source text`,
   then Stop This Shortcut inside the If.
4. For these supplied fixtures add **If** sourceText **does not contain** the
   literal `import Shortcuts`: Show Alert `Expected source contents, not a filename`,
   then Stop This Shortcut inside the If. This is a fixture-specific check; other
   valid Jelly sources might use different imports. It is not a language validator.
5. Add **Quick Look**: input = named `sourceText`. Reconnect this explicitly after
   adding the guards; do not preview an Alert or the last Dictionary Value.

The preview must show these complete four lines, not just source.txt:

```jelly
import Shortcuts
nothing() >> emptyValue
var currentValue = emptyValue
quicklook(input: currentValue)
```

Dismiss Quick Look to continue. This previews code Text, not the generated
shortcut's empty runtime value. If code preview is wrong, cancel the run.

### 9. Add a review and cancellation checkpoint

Add a **Text** action with this layout, inserting actual variable tokens for the
bracketed entries:

```text
Build: [buildId]
Original source: [originalSourceFilename]
Shortcut name: [intendedShortcutName]
Compiler: Compile Jelly Text
Source SHA-256: [actualHash]
```

Add **Show Alert**: title `Compile this build?`; message = that Text action's
output. Enable **Show Cancel Button**. Confirm the intended TEST name does not
conflict with an installed working shortcut. Cancel if the metadata is wrong.

For a first wiring-only run, choose **Cancel** at this alert. That lets you check
the manifest, hash and source preview before invoking Jellycuts. The next real run
can proceed with OK. No temporary unconditional Stop action needs to be added.

### 10. Reconnect the existing Compile Jelly Text action

This is the key edit to your existing compiler action:

| Input in the existing action | Selected value |
| --- | --- |
| Jelly/source Text input | Named **sourceText** from Get Text from Input |
| Naming input that previously used the File's Name | Named **intendedShortcutName** extracted from request.json |

Clear the old File-name token from the naming input. Insert intendedShortcutName
as a variable token, not as literal letters. Preserve other working compiler
settings. The exact name-field label is not captured in the repository; use the
field you already configured when source became the installed name.

Reselect sourceText in the source-code input as well: after inserting the review
Text/Alert, automatic chaining could otherwise send the review message to Jellycuts.
Do not connect request, requestFile, sourceInfo, sourceFile Name or the summary Text
to the source-code input. Do not use originalSourceFilename as the display name.

Keep the existing export/install flow after this action. Do not add guessed
Save File/Import actions based on an assumed compiler return type. If a later
existing naming field also uses the File Name, inspect its purpose and replace it
with intendedShortcutName only when it sets the generated shortcut's display name.

### 11. Run the minimal-variable test and inspect the untouched output

1. Run TEST -Jellycuts Compiler in the foreground.
2. In Files share the new build's long-ID folder to TEST -Jellycuts Compiler.
   If it receives a usable Folder, it retrieves request.json and source.txt
   automatically. Check hash, code preview and displayed name.
3. At the confirmation alert choose OK for the real compilation attempt.
4. Record whether compilation completes, hangs or reports errors/warnings.
5. Inspect the generated shortcut's name. Expected: **TEST - Pipeline Minimal Variable**.
6. Inspect the generated actions before repairs. Expected: **Nothing** named
   emptyValue → **Set Variable** currentValue from emptyValue → **Quick Look** of
   the named currentValue. Missing actions or dangling tokens fail generation even
   if the compilation action reported no error.
7. If testing execution, note that currentValue is intentionally empty. An empty
   runtime Quick Look does not alone prove failure or success. Keep this separate
   from the required code-text preview in step 8.

If the installed name is still source, inspect both compiler inputs and any
downstream naming action. Record that actual name before manually renaming the
new diagnostic. Do not rename a working production helper or change callers.
If the app hangs, record that attempt before a retry; do not combine a hang and
a later success into one reliability pass. No automated feedback return is assumed.

### 12. Return the observation

Report the build ID, actual installed name, completion/hang, exact warnings/errors,
the action sequence/connections and whether you repaired or ran it. Windows can
then append the observation with record/ingest. Visible files and a successful
hash check are transport evidence, not compiled/inspected/executed status.

For a completed generation whose actions have not yet been inspected, the
corresponding Windows command would be:

```powershell
python jelly/scripts/ipad_pipeline.py record 20261105T174604824552Z-2b3d695d0fba4a3a8adf96066de49c62 --status output-unverified --method compile-jelly-text --installed-name 'TEST - Pipeline Minimal Variable' --notes 'Replace with the actual observations'
```

This is an example, not a result already obtained. Use the actual name and the
actual exchange root via --exchange when recording against a different root.
An inspected malformed output instead needs inconclusive/correct=false evidence;
see the [pipeline command examples](ipad-pipeline.md).

### Connection reference

| Named variable | Type | Producer |
| --- | --- | --- |
| requestFolder | Folder, to verify on device | Single shared Folder from Shortcut Input, extracted after Count=1 |
| requestFile | File | Get File from Folder: requestFolder + request.json |
| request | Dictionary | Get Dictionary from Input of requestFile's Text |
| buildId | Text | request key build_id |
| intendedShortcutName | Text | request key shortcut_name |
| sourceInfo | Dictionary | request key source |
| originalSourceFilename | Text | sourceInfo key filename |
| expectedHash | Text | sourceInfo key delivered_sha256 |
| sourceFile | File | Get File from Folder: requestFolder + source.txt |
| actualHash | Text | Lowercase SHA-256 of sourceFile |
| sourceText | Text | Get Text from Input of sourceFile |

Apple documents [duplicating shortcuts](https://support.apple.com/guide/shortcuts/duplicate-shortcuts-apd6b467942c/ios)
and [selecting variable properties](https://support.apple.com/en-ie/guide/shortcuts/apda36b9018b/ios).
The helper's exact Jellycuts UI and the new end-to-end wiring still require your
device test; the guide does not claim those actions were operated remotely.

## Get one complete request onto the iPad

1. Prepare the existing hello-world fixture using the [Windows commands](ipad-pipeline.md).
2. Make the entire `requests/<build-id>` folder available through Files. If using
   Nextcloud, first verify the actual Windows sync folder and iPad Files account.
   If no sync is configured, copy/download that one complete folder manually.
   Do not type source or recreate actions to compensate for transport problems.
3. In Files open its `request.json` and note build_id, source.filename,
   source.delivered_sha256 and requested_method. Confirm source.txt and source.jelly
   are present and downloaded, not just cloud placeholders. Do not rename/edit them.
4. Record actual iPadOS/Jellycuts versions and the exact build ID with every report.

### Read and apply the intended display name

For a version-2 request use **Get Dictionary Value**, key `shortcut_name`,
Dictionary=named request; **Set Variable** intendedShortcutName to that Text
output. Also retrieve source.filename from sourceInfo for context. Show buildId,
original filename and intendedShortcutName together before compilation. If using
a legacy request without this field, prepare a new named request on Windows;
do not edit the old immutable manifest or guess its historical intended name.

The user reports configuring the compilation action's name from the File name,
which generated an installed shortcut called **source**. In that existing helper,
replace the File-name token in its naming field with **intendedShortcutName** from
request.json. This is the reported configurable input; its exact current UI label
and its behavior on each compilation path still need recording. Do not pass the
name token into the source-code input. The source Text/File connection remains
the one specified below. Confirm the resulting installed name after compilation;
the Windows tool cannot apply the field or verify device behavior itself.

For any path with no editable name setting, rename only the newly generated test
shortcut after installation: open its editor, tap the arrow beside its name,
choose Rename, enter intendedShortcutName and finish. Inspect existing names
first. Never replace/rename a working choir helper to accommodate a test; exact
Run Shortcut targets must continue to match their established contracts.
[Apple's iOS 26 rename instructions](https://support.apple.com/en-il/guide/shortcuts/apdd57094696/9.0/ios/26)
document this manual fallback. Jellycuts' [pinned metadata reference](../vendor/jellycuts-docs/markdown/Language_Guide/metadata.md)
documents Color/Icon, not a shortcut-name directive; no `#Name` is assumed.

Use Windows `record --installed-name '<actual observed name>'` or the v2 feedback
field installed_shortcut_name. Keep null when not observed. Record the initial
name and any later manual rename as separate observations. A matching name is
not proof of correct actions or runtime. Avoid duplicate installed test names.

## Path A: diagnostic text compiler helper

For your existing TEST -Jellycuts Compiler, use the detailed upgrade above. The
compact table below is a separate reference if constructing a fresh diagnostic
Shortcut named **TEST - Compile Exchange Text**.
Run it directly in the foreground. The action names below are native action names
to search for; available labels/settings and provider behavior must be checked on
the physical device. No guessed Jelly bindings are involved.

| Step | Action and explicit variable connection |
| --- | --- |
| 1 | Enable Show in Share Sheet and accept Folder. Count Items in Shortcut Input; stop unless exactly 1. Get First Item, then Set Variable requestFolder to that native Folder. No Select Folder action. |
| 2 | **Get File from Folder**, Folder=requestFolder, relative File Path=request.json; Set Variable requestFile. Get Text from Input of requestFile, then Get Dictionary from Input of that Text. |
| 3 | **Set Variable** request = Dictionary from step 2. |
| 4 | **Get Dictionary Value**, key `build_id`, Dictionary = named request. Set named buildId from this output. |
| 5 | **Get Dictionary Value**, key `source`, Dictionary = named request. Set named sourceInfo from this nested Dictionary. |
| 6 | **Get Dictionary Value**, key `delivered_sha256`, Dictionary = named sourceInfo. Set named expectedHash. |
| 7 | **Get File from Folder**, Folder=requestFolder, relative File Path=source.txt; Set named sourceFile from that retrieved native File. No second picker. |
| 8 | **Generate Hash** (search Hash), algorithm SHA-256, input = named sourceFile. Set named actualHash. |
| 9 | **If** actualHash is not expectedHash: Show Alert "Source hash mismatch — stop", then **Stop This Shortcut**. Do not compile that file. |
| 10 | **Get Text from Input**, input = named sourceFile. Set named sourceText from this action's Text output. |
| 11 | **If** sourceText does not have any value: Show Alert "No source text", then Stop This Shortcut. |
| 12 | For the supplied integration fixtures only: **Match Text**, pattern `(?m)^import[ \t]+Shortcuts[ \t]*\r?$`, input = named sourceText. Count the Matches. If Count is 0: Show Alert "Expected source contents, not a filename/path", then Stop This Shortcut. |
| 13 | **Quick Look**, input = named sourceText, explicitly reselected. Inspect the complete source, including its first and last lines and header comments. Dismiss Quick Look to continue. |
| 14 | **Show Alert**, title = buildId token, message = intendedShortcutName, original filename and expectedHash tokens plus a reminder to compare the source with request.json. Enable Cancel; cancel if source or intended name is wrong/conflicting. |
| 15 | Jellycuts **Compile Jelly Text**, its source/input chip = named sourceText from step 10; naming field where available = intendedShortcutName. Never select sourceFile Name as the shortcut name or as source code, source.filename, a path Text or the preceding Alert output. Photograph/record available options; do not guess undocumented settings. |

**Device validation required:** step 8 must hash the actual File bytes. Confirm
its value against the Windows manifest on the initial LF fixture. Then test BOM
and CRLF separately if needed. If the device hashes a representation rather than
bytes or conversion changes content, do not label the bytes verified. Record the
discrepancy and return to the raw-file/editor path. Do not silently normalize and
reuse the old hash. The compiler's exact consumed bytes are not observable merely
because the file hash matches; record the conversion and input type too.

Step 12 is a deliberate anti-filename guard for fixtures containing `import
Shortcuts`, not a universal Jelly language validator. For another valid source
without that import, replace this fixture-specific guard with an explicit known
source marker check and full preview. Never change the submitted source to satisfy
the helper. A preview of only `source.txt`, an original filename or a path is a
failure before compilation.

If any selected action/setting above is unavailable, record it and use Path B
plus Windows manual recording. Do not guess an alternative File conversion.

### Inspect the compilation action's return contract

Do not initially wire output into Save File or assume an exported Shortcut exists.
First inspect the generated actions in Jellycuts/Shortcuts and compare the fixture
expectations. Record the exact app navigation, errors and warnings.

Only if the compilation action exposes a selectable output token, experiment in
a duplicate diagnostic helper with **Get Type** and **Quick Look**, both explicitly
connected to that compile output. Record actual type/content and whether execution
reaches them. No token, no result, action abort or Quick Look UI failure is a
separate observation—not evidence that compilation succeeded or failed.

A post-action If cannot catch an error that aborts the shortcut. There is no
promised try/catch or complete compiler diagnostic API in these instructions.
If unavailable, copy/transcribe the visible diagnostics and use Windows `record`.

### Compile Jelly File comparison

Duplicate the diagnostic helper as **TEST - Compile Exchange File**. Keep source
selection, hash and Text preview. Replace only step 15 with **Compile Jelly File**,
input = named sourceFile (native File from step 7). Do not pass sourceText or a
filename. Record all exposed action settings. Its output behavior is equally
unverified. Use a new request with `--method compile-jelly-file` for a separate
attempt, or record the actual method explicitly against the original request.

## Path B: editor fallback

1. In Files select the request's `source.jelly`, use Share, and look for Jellycuts,
   including More. Check whether it opens the exact editable source in the editor.
   This file/share integration is an **experiment**, not established capability.
2. If absent or it does not open editable source, use the preview helper through
   step 13, then replace the compilation action with **Copy to Clipboard**, input
   = named sourceText. Open Jellycuts, create a disposable source project, select
   all its editor contents and paste the complete source. Compare first/last lines
   and header comments against the snapshot before compiling. This uses the
   existing reported editor/paste route; end-to-end clipboard transfer of this
   prepared request still needs a physical-device check.
3. Compile/export through the app's normal existing flow. Inspect the generated
   actions and actual name before running. Use intendedShortcutName in any naming
   setting actually available, or the manual Rename fallback above. Do not use a
   Windows unsigned export as a substitute.
4. Keep any malformed generated shortcut unchanged for evidence. If investigating
   a native repair, duplicate it, record every edit and report repaired execution
   separately. This experiment uses small TEST shortcuts, never production helpers.

Copy/paste transfers source; it does not require manually rebuilding its generated
native actions. Existing production forScore slots are a separate unresolved
generation limitation and are not fixed by this transport. Preserve working
installed shortcuts rather than repeatedly regenerating them during these tests.

## Return feedback without assuming compiler output

The fully implemented fallback is Windows `record`, associated with buildId and
both request hashes. It works even when the app exposes no machine-readable output.
Return visible warnings/errors by transcription, copied text, or a manually
transferred UTF-8 diagnostic file. Keep screenshots/exports as supporting evidence
where the app actually permits them; their export is not automated here.

An optional manual note helper can use native **Ask for Input** (Text), **Text**
containing buildId/hash/method and the actual notes as variable tokens, and
**Save File** with Ask Where to Save On. Choose `results/<build-id>/device-note.txt`
in the same shared location. Do not overwrite request files. Verify on Windows
that the note arrived intact before using `record --diagnostics-file <path>` with
the matching build ID and explicit outcome. This is a provider-write experiment;
if Save File cannot reach the location, manually transfer the note instead.

For JSON feedback, copy feedback-template.json outside requests, update all fields
and reported_at_utc per the [format](ipad-pipeline-format.md), then return it as
`results/<build-id>/result.json` or any local file for explicit ingestion. Do not
assemble raw JSON with unescaped compiler messages in a Shortcuts Text action.
Automatic native Dictionary-to-JSON reporting is deferred until the action return
contract and provider saving have been demonstrated. No result folder, copied
template, zero-error return or saved note constitutes a compile pass.

## Sources and evidence boundary

- [Apple: Using Dictionaries, iOS 26](https://support.apple.com/en-in/guide/shortcuts/apd43b69f337/9.0/ios/26)
  supports Get Dictionary from Input for JSON/plist and dictionary key access.
- [Apple: Input types](https://support.apple.com/en-gb/guide/shortcuts/apd7644168e1/ios)
  distinguishes native Folder/Files from Text and URLs, and recommends View
  Content Graph to inspect what another app actually passes into a shortcut.
- Local pinned action references: [Get Text from Input](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/getTextFrom.md),
  [Hash](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/hash.md),
  [Quick Look](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/quicklook.md).
- [Cherri's native-action reference](https://cherrilang.org/language/standard/documents.html)
  documents Select Folder and folder-relative file retrieval. It is supporting
  action evidence, not a proposed compiler migration or proof of OneDrive behavior.
- Existing user reports establish the two Jellycuts compilation action names,
  successful examples and the incomplete-generation counterexample. They do not
  establish current action parameters, return types, diagnostics/export or the
  behavior of this newly described helper. All those require device evidence.
