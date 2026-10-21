# Installation review after incoming-List extraction tests

21 October 2026. Current production revisions: Canonical **11**, Archive **15**,
Assembly **13**, Main **4**. Interfaces remain 2.0 / 2.1 / 1.1 / 1.0.
This is a source/compiler/manual-work audit, not a successful full iPad build.

## Archive 15 follow-up

ARC01-ARC03 are now source assignments in a quoted-index Repeat loop; Nothing
initialization avoids introducing Text values for the native context objects.
This is a candidate extension of the successful Text tests, not a mixed-type
device pass. [Run the read-only probe](../tests/compatibility/archive-context-loop.md)
before enabling Archive 15. CFG02-CFG04 and the initial guard remain.
The probe passed local compiler/export checks with eight core-node warnings;
the full Archive 15 failed on the existing Output/File Details profile issues.

## Earlier review of Assembly 13 and Archive 14

Assembly 13 predeclares rootChildName, lowerExtension and canonicalStem, captures
each producing action under a distinct Result name, then assigns the named
variable immediately before its conditional use inside Repeat. This follows
the successful named-variable loop pattern and the earlier archive scope repair.
It addresses the same risk seen in the user's out-of-scope archive comparisons;
it does not establish that these complete assembly loops work on the iPad.

Canonical 11 already replaces NAME01/NAME02 with the user's confirmed incoming
two-Text loop and quoted `"1"`/`"2"` comparisons. Its full argument validation,
replacement actions and returned canonicalName still need the integrated check.
No selector aliases or unquoted numeric conditions were reintroduced. Archive 14
and Main 4 were not changed by this audit; preserve the working installed archive.

## Actual local compilation results

All four sources were attempted in dependency order using the build wrapper.
**0/4 passed.** Per-source JSON and captured streams contain the exact diagnostics;
the aggregate terminal capture is `jelly/build/pre-install-review.log`.

| Source | Observed blockers |
| --- | --- |
| Canonical 11 | Known positional Output incompatibility; brace/core-node events |
| Archive 14 | Positional Output, brace/core-node events and Get File Details unnamed-parameter diagnostics |
| Assembly 13 | Positional Output, brace/core-node events and Get File Details unnamed-parameter diagnostics |
| Main 4 | Positional Output only |

Raw CLI status 0 is not a pass; the wrapper returned 1. App evidence supports
positional Output, so it remains in production. The spaced File Extension form
comes from the local official action page, while alternate enum forms have prior
device failures. Do not declare it valid from a local failure, or replace it with
a guessed alias/declaration. In the iPad-generated archive/assembly, inspect the
actual Get Details of Files property: **Name** versus **File Extension**. The
declared ItemAtIndex test showed that an accepted enum argument can silently
produce the wrong default setting, so action inspection is essential.

## Remaining manual work

There are **23 active native insertion/configuration IDs** across the two larger
helpers (retired CFG01 and retired naming NAME01/NAME02 are excluded):

| IDs | Required native work / reason it remains |
| --- | --- |
| ARC01-ARC03 (retired in 15; excluded from count) | Replaced by source extraction. Native File/Folder/Dictionary preservation still requires the read-only device test |
| CFG02 | Save File native destination Folder; the inspected binding exposes no Folder destination argument |
| CFG03-CFG04 | Return the actual existing/saved native File; empty source Outputs are placeholders, not working File returns |
| CONF01-CONF02 | Select the actual Choir Music Folder and read its config File from that Folder |
| COL01-COL03 | Append ordered native Files, preview-name Texts and prepared native Scores. No verified Add to Variable binding was found in the inspected standard library/docs |
| SCORE01-SCORE02 | Select native Score results from lookups; do not substitute display-title Text |
| FS01-FS13 | The existing forScore native actions; no verified Jelly bindings were found in the selected setup |

Reconnection to actual replacement/native outputs remains part of each slot.
The archive's repaired post-loop existingCleanFile presence check must read the
current named variable. Native File returns, receiving configuration and repeated
Score transport are not validated by Text-only previews. Keep both initial
assembly guards until that helper's native slots and conditional wiring are
complete. Otherwise an incomplete template can skip work or use empty values.

## Attempt to reduce manual preview work

A new isolated [running-order Text accumulator](../tests/compatibility/running-order-text.md)
could replace COL02 and avoid the Custom separator enum. It uses a fixed
`First`, `Second`, `First` fixture, the successful quoted-index loop pattern,
and Text interpolation/assignment. Intended result: `First | Second | First`.

Actual local result: the CLI accepted it with six brace/core-node warnings, but
the wrapper **rejected its export** because a text attachment was outside the
string (`{1243, 1}`). This is the reproduced local interpolation defect; it is not
a validated replacement. The candidate is separate; COL02 remains unchanged in
production. Its iPad result is unknown. No generated-file patch was applied to
conceal the defect, and no more native slots were removed without evidence.

## Before treating the set as installable

Compile the actual updated sources in the user's Jellycuts app. Inspect the named
variable assignments/conditions added in Assembly 13, native file-detail properties,
both guards and all native slots. Full Canonical 11 must return the expected stem
to a caller; two preview values alone do not prove its replacement/return path.
Use disposable PDFs/setlists for the first integrated run. These remain guarded
templates requiring native completion, not four fully automatic install-and-run
Shortcuts. The user-authorized source-plus-native-slot route remains unchanged.
