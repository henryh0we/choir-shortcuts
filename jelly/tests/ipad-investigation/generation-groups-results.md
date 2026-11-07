# iPad generation results

## G2A documented `var +=` variant, 7 November 2026

The user confirms that `var collectedValues += RepeatItem` generated Add to
Variable and returned 3, A, B, A without the previously required native insertion.
This is a reported generation and runtime pass for this Text fixture. It does
not establish File or Score behaviour, other contexts, exact consumed hash, app
version, or broader compiler compatibility. The local build attempt was blocked
by WSL access denial. See the [source](g2a-var-append-text.jelly) and
[paste copy](../pipeline/fixtures/g2a-var-append-text.txt).

## G2A generated-action inspection, 7 November 2026

The user subsequently reports that inserting native Add to Variable inside the
first Repeat produced 3, A, B, A. This is a repaired runtime pass, not an
untouched generation pass. The documented alternate was subsequently tested as above.

Two user-supplied screenshots show the revision-2 header, the A/B/A List,
Nothing and initialization of named collectedValues, followed by a Repeat over
sourceValues with **no action inside it**. The source calls for
`collectedValues += RepeatItem` there, but no Add to Variable action is visible.
The following Count and final Repeat visibly reference named collectedValues;
the latter contains a Quick Look of Repeat Item. The empty first Repeat explains
the reported zero for this export. The screenshots do not establish why the
append was omitted, the consumed source hash, or any repair history. A duplicate
with a native Add to Variable can test the remaining wiring separately; its
outcome must not be attributed to untouched generation.

## Name-first clipboard follow-up, 7 November 2026

The user confirms that the revised name-first G2A fixture and automatic naming
worked as intended through the Copyover helper. The generated shortcut still
outputs only `0`. Name extraction/default naming is therefore confirmed by user
report for this attempt; correct collection generation is not. No exact consumed
hash, installed action/token inspection, native repair history or current device
versions were supplied. The remaining extraction edge cases in the helper guide
are not established by this report. Preserve the earlier attempt below separately.

## Copyover clipboard attempt, 7 November 2026

The user reports that the Copyover receive/preview/name/Compile Jelly Text helper
showed all expected popups and created the G2A shortcut. Its only observed runtime
output was `0`, repeating the earlier single-comment collection failure below;
expected output remains Count 3 then A, B, A. This establishes reported transport
and shortcut creation, not correct collection generation. Exact received bytes,
installed action/token inspection, installed name, versions and repairs were not
confirmed. Do not attribute the failure to Copyover or Jellycuts from this alone.

The selected source at the time had the legacy `// Installed name: ... | ...`
header. The repository file's pre-edit SHA-256 was
`a64c6b6785de0d891030e90e3e3edb2dfcd15723e0e7d3a3e3bacde47ea0ac7d`;
this is a local reference, not a device-verified consumed hash. It is now a
revision-2 name-first header candidate; executable bytes after the first line
remain unchanged. The revised header and automatic name default are not yet
device-tested. Preserve the installed output for wiring inspection before repairs.

## Latest single-comment variants, 6 November 2026

User-reported results following the supplied Compile Jelly Text request commands.
These refer to the separate `.txt` fixtures in `../pipeline/fixtures/`, not the
original multi-comment sources in the historical table below. Exact build IDs,
consumed hashes, device versions, installed names and repair history were not
provided; no immutable request is assigned these reports.

| Single-comment fixture | Inspection reported | Actual runtime | Assessment |
| --- | --- | --- | --- |
| [G1B](../pipeline/fixtures/g1b-latest-value-single-comment.txt) | Everything looks good | Matches expected Alpha, Beta, Delta, Echo | Reported runtime pass for Text latest assignment |
| [G1C](../pipeline/fixtures/g1c-count-guards-single-comment.txt) | Looks good | 2, 2, 1, FAIL G1C EQUAL REJECTED, G1C MISMATCH DETECTED | Runtime failure: equal counts rejected; mismatch detected |
| [G1D](../pipeline/fixtures/g1d-file-assignment-single-comment.txt) | Looks good | Matches expected Count 2, PDF A, PDF B, PDF B | Reported runtime pass for File assignment |
| [G2A](../pipeline/fixtures/g2a-append-text-single-comment.txt) | Not separately described | 0; no A/B/A previews | Runtime failure: collection observed empty |
| [G2B](../pipeline/fixtures/g2b-append-files-single-comment.txt) | Not separately described | 2, 0; no further previews | Runtime failure: two selected Files, empty collection |

Next inspect G1C's actual native operators and both Count-output operands, and
G2A's first Repeat, Add to Variable actions, Count input and final Repeat input.
All collection consumers must select the current named collection, not the
Nothing initializer. Do not infer whether append generation or downstream token
binding failed from zero alone. Diagnose G2A before native-File G2B or Score G2C.
Preserve untouched outputs; any native edits belong on duplicates with separate
before/after observations. No production source rule changes follow yet.

## Original-source results table

All original-source device results start **Not run**. Use [the checklist](generation-groups.md)
for expected values and the full per-test result template. Record untouched
compilation/export/runtime separately from native fixture setup or later repairs.
Do not overwrite the source evidence or change production shortcuts based on
partial results.

Device versions / date / locale: Not recorded.

| Test | App compile | Export inspection | Runtime | Repairs / notes |
| --- | --- | --- | --- | --- |
| [g1a-presence](g1a-presence.jelly) | Not run | Not run | Not run | None recorded |
| [g1b-latest-value](g1b-latest-value.jelly) | Not run | Not run | Not run | None recorded |
| [g1c-count-guards](g1c-count-guards.jelly) | Not run | Not run | Not run | None recorded |
| [g1d-file-assignment](g1d-file-assignment.jelly) | Not run | Not run | Not run | None recorded |
| [g2a-append-text](g2a-append-text.jelly) | Not run | Not run | Not run | None recorded |
| [g2b-append-files](g2b-append-files.jelly) | Not run | Not run | Not run | None recorded |
| [g2c-append-scores](g2c-append-scores.jelly) | Not run | Not run | Not run | None recorded |
| [g3-exit-context](g3-exit-context.jelly) | Not run | Not run | Not run | None recorded |
| [g3-exit-echo](g3-exit-echo.jelly) | Not run | Not run | Not run | None recorded |
| [g3a-text-caller](g3a-text-caller.jelly) | Not run | Not run | Not run | None recorded |
| [g3b-file-caller](g3b-file-caller.jelly) | Not run | Not run | Not run | None recorded |
| [g3c-context-caller](g3c-context-caller.jelly) | Not run | Not run | Not run | None recorded |
| [g4a-default-direct](g4a-default-direct.jelly) | Not run | Not run | Not run | None recorded |
| [g4b-default-interpolated](g4b-default-interpolated.jelly) | Not run | Not run | Not run | None recorded |
| [g4c-default-controls](g4c-default-controls.jelly) | Not run | Not run | Not run | None recorded |
| [g4d-date-name](g4d-date-name.jelly) | Not run | Not run | Not run | None recorded |

G3 receivers are assessed through their callers, not direct no-input execution.
G2C fixture caller/native Open score setup is deliberate; record it separately
from any change to the generated += logic. List both returned counts and the
actual native A/B/A identities. For defaults, record the initial field contents
before typing, not only the value eventually entered.

Copy a detailed result block from the checklist below this table as tests run.
