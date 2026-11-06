# iPad generation results

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
