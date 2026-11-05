# iPad setup and first compilation experiment

Status: **instructions prepared; physical-device tests Not run**. No importable
Shortcut is supplied. Create these small diagnostic helpers manually in Apple
Shortcuts; do not modify working installed choir shortcuts. Jellycuts Bridge is
excluded and no premium Bridge capability is used.

The currently best observed route is the Jellycuts editor. Both compilation
actions have also generated incomplete output; see the existing
[path comparison](../tests/ipad-investigation/compilation-path-comparison.md).
An action returning without an error is not a successful generation test.

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

Create a new manually constructed Shortcut named **TEST - Compile Exchange Text**.
Run it directly in the foreground. The action names below are native action names
to search for; available labels/settings and provider behavior must be checked on
the physical device. No guessed Jelly bindings are involved.

| Step | Action and explicit variable connection |
| --- | --- |
| 1 | **Select File**, multiple selection Off. Select request.json in the intended build folder. |
| 2 | **Get Dictionary from Input**, input = selected request File, not its name. |
| 3 | **Set Variable** request = Dictionary from step 2. |
| 4 | **Get Dictionary Value**, key `build_id`, Dictionary = named request. Set named buildId from this output. |
| 5 | **Get Dictionary Value**, key `source`, Dictionary = named request. Set named sourceInfo from this nested Dictionary. |
| 6 | **Get Dictionary Value**, key `delivered_sha256`, Dictionary = named sourceInfo. Set named expectedHash. |
| 7 | **Select File**, multiple selection Off. Select source.txt from that exact buildId folder. Set named sourceFile from the selected native File. |
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
  distinguishes native Files from plain Text.
- Local pinned action references: [Get Text from Input](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/getTextFrom.md),
  [Hash](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/hash.md),
  [Quick Look](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/quicklook.md).
- Existing user reports establish the two Jellycuts compilation action names,
  successful examples and the incomplete-generation counterexample. They do not
  establish current action parameters, return types, diagnostics/export or the
  behavior of this newly described helper. All those require device evidence.
