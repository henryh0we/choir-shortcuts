# iPad generation results

All device results start **Not run**. Use [the checklist](generation-groups.md)
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
