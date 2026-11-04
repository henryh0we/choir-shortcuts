# Generation test groups

Created 4 November 2026. These test candidates investigate how to reduce manual
repairs when regenerating Archive and Assembly. **They do not update your working
shortcuts.** Local compiler results are in [the build record](generation-groups-builds.md).
All iPad compilation, import and execution results begin **Not run**.

Start with **G1A, G1B and G1C**. Report their exact preview sequence before moving
on if something differs. You do not need to import all 16 shortcuts at once.

## Install and record each test

1. Keep the working `2-util-*` shortcuts and their backups unchanged.
2. Open a source `.jelly` in Jellycuts, or paste its complete `.txt` twin. Use the
   **exact installed name in the first source comment** after export/import.
   Source filenames and comments do not automatically name the installed shortcut.
3. Record the actual iPadOS, Jellycuts and forScore versions. The earlier recorded
   profile was iPadOS 26.6 / Jellycuts 2026.6.4 / forScore 15.2.5; do not assume
   the installed versions are still identical.
4. Compile unchanged. Record errors and warnings verbatim. If it cannot compile,
   stop that test; do not try guessed enum spellings or delete its failing line.
5. Inspect the generated actions before running. An accepted source that omits an
   If, Add to Variable or default is a generation failure, not a pass.
6. Run in the foreground in Apple Shortcuts. Dismiss each Quick Look to continue.
   Quick Look can itself fail in some UI contexts: record that separately rather
   than assuming the producer failed. All preview inputs must explicitly select
   the output/variable under test, not the preceding diagnostic action's output.
7. Record the untouched result. If experimenting with a repair, duplicate the test
   first and record each change. A repaired pass does not establish generated success.

Every test has a byte-identical `.txt` copy linked below. These are source files
to compile in the iPad app, not signed/import-ready local `.shortcut` artifacts.
The older WSL compiler is a separate comparison profile. Even a local structural
pass cannot validate all native action fields or establish iPad compatibility.

These are interactive tests with synthetic Text and disposable PDFs. There are
no archive saves, PDF renames, imports, metadata writes or setlist mutations.
Selecting a cloud PDF may download it. G2C navigates to existing forScore scores.
Cancellation/missing input is not a success case; supply the stated fixtures.

## Group 1 — variables, missing values and Count guards

No dependencies or native completion slots. G1A–G1C need no input or provider access.

| Test / exact installed name | Files | Inspect before running | Expected sequence |
| --- | --- | --- | --- |
| G1A / `TEST - G1A Presence` | [source](g1a-presence.jelly), [paste copy](g1a-presence.txt) | Four Ifs: absent, present, present after assignment, absent after assignment. Each reads named currentValue. `== nil` = does not have any value; `!= nil` = has any value. | Exactly `G1A EMPTY ABSENT`, then `G1A FILLED PRESENT`. No `FAIL` marker. Missing, extra or reversed previews fail. |
| G1B / `TEST - G1B Latest Value` | [source](g1b-latest-value.jelly), [paste copy](g1b-latest-value.txt) | All four Quick Looks use current named currentValue. The loop and branch assignments remain inside their blocks. | `Alpha`, `Beta`, `Delta`, `Echo`, in that order. A stale initial value fails. |
| G1C / `TEST - G1C Count Guards` | [source](g1c-count-guards.jelly), [paste copy](g1c-count-guards.txt) | Three Count actions and four comparison Ifs. Both operands reference the correct Count outputs; check **is** versus **is not**. | `2`, `2`, `1`, `G1C EQUAL CONTINUES`, `G1C MISMATCH DETECTED`. No FAIL marker. |
| G1D / `TEST - G1D File Assignment` | [source](g1d-file-assignment.jelly), [paste copy](g1d-file-assignment.txt) | Select File allows multiple. The assignment and first Quick Look are inside the Repeat; the last Quick Look uses current named currentFile outside it. | Select two different PDFs. Count `2`; full PDF A, full PDF B, then B again. |

For G1D, A/B mean the order returned by Select File. Record it from the first two
previews; file-selection order must not be inferred from filenames. Select exactly
two PDFs or cancel/restart the fixture. Inspect actual PDF pages, not just names.

These results separate Text-variable behaviour from native File behaviour. A G1B
Text pass alone must not be promoted to a native Score or File rule.

## Group 2 — generated Add to Variable using `+=`

The [variables documentation](../../vendor/jellycuts-docs/markdown/Language_Guide/variables.md)
documents `+=`. This is a new candidate, not the existing running-order Text
accumulator probe. Generated Add to Variable actions must remain untouched.

| Test / exact installed name | Files | Setup | Expected sequence |
| --- | --- | --- | --- |
| G2A / `TEST - G2A Append Text` | [source](g2a-append-text.jelly), [paste copy](g2a-append-text.txt) | None. | Count `3`, then `A`, `B`, `A`. |
| G2B / `TEST - G2B Append Files` | [source](g2b-append-files.jelly), [paste copy](g2b-append-files.txt) | Select exactly two different disposable PDFs. | Initial Count `2`; collection Count `3`; type and full PDF preview for A, B, A. |
| G2C / `TEST - G2C Append Scores` | [source](g2c-append-scores.jelly), [paste copy](g2c-append-scores.txt) | Native fixture caller and one native Open score consumer described below. | Fixture Count `2`; collection Count `3`; three native score consumptions opening A, B, A. |

Inspect both `+= RepeatItem` and the final `+= firstFile/firstScore`: they must
be **Add to Variable**, not Set Variable or numeric/text concatenation. Preserve
the initial Nothing; it initialises the collection. Counts and Repeats must read
the current named populated collection. Confirm actual identities and repetitions.

### G2C: deliberate native fixture setup

G2C needs native Scores because no verified forScore Jelly binding is available.
This fixture is the only required manual setup in the suite. Its input and final
consumer must be configured, but **do not repair the generated accumulator**.

Choose two known, distinct scores already in the intended forScore library. The
source only reads/navigates; it does not create or populate a test setlist.

Create a temporary caller `TEST - G2 Score Fixture` manually:

```text
[Get score]
Name: Known unique score A lookup name
Continue if not found: On

[Get Item from List]
Get: Item at Index
Index: 1
List: Native result of the A lookup

[Set Variable]
Variable: fixtureScoreA
Input: Native Item from the A extraction

[Get score]
Name: Known unique score B lookup name
Continue if not found: On

[Get Item from List]
Get: Item at Index
Index: 1
List: Native result of the B lookup

[Set Variable]
Variable: fixtureScoreB
Input: Native Item from the B extraction

[List]
Item 1: Named fixtureScoreA (native Score)
Item 2: Named fixtureScoreB (native Score)

[Run Shortcut]
Shortcut: TEST - G2C Append Scores
Input: Two-Score List above
```

Variable names in fields mean actual tokens. Do not use score-title Text as List
rows. Check both lookups produce the intended native Score before using the fixture.
If either lookup is absent/ambiguous, repair the fixture, not the `+=` probe.

In the imported **G2C** shortcut find comment **G2S-CONSUME**. Replace only the
immediately following Nothing slot inside its final collection Repeat:

```text
[Open score]
Score: Native Repeat Item from the final Repeat over collectedScores
```

Keep the following **Wait to Return** in that Repeat. After each score opens,
inspect its identity in forScore, then return to Apple Shortcuts to continue.
If app navigation/wait behaviour prevents inspection, record that limitation;
do not claim order/native preservation from Count alone. Do not remove the earlier
Nothing used to initialise the collection.

Record **fixture setup completed; generated accumulation untouched** separately
from **probe repaired**. An editor type label alone is insufficient evidence:
actual native Open score consumption must work for all three items.

## Group 3 — native `exit(var:)` returns through a caller

Import the two receivers first under these exact names:

| Receiver | Files | Input → intended return |
| --- | --- | --- |
| `TEST - G3 Exit Echo` | [source](g3-exit-echo.jelly), [paste copy](g3-exit-echo.txt) | One Text or PDF → same native value. |
| `TEST - G3 Exit Context` | [source](g3-exit-context.jelly), [paste copy](g3-exit-context.txt) | One PDF → two-item native List `[PDF, Anthems]`. |

Do not run receivers directly without input. Their code after Exit is a failure
sentinel, not a success preview: `FAIL G3 ... EXIT DID NOT STOP` must never appear.
Absence of that sentinel alone is not proof of a return; inspect caller results.

Then import/run these callers. Check each Run Shortcut selects the matching
installed **test receiver**, not a production helper or similarly named old test.

| Caller / exact installed name | Files | Expected sequence |
| --- | --- | --- |
| G3A / `TEST - G3A Text Caller` | [source](g3a-text-caller.jelly), [paste copy](g3a-text-caller.txt) | Type Text, then `G3 ALPHA RETURN`. |
| G3B / `TEST - G3B File Caller` | [source](g3b-file-caller.jelly), [paste copy](g3b-file-caller.txt) | Select one PDF. Its baseline type, returned type, then the same usable full PDF. |
| G3C / `TEST - G3C Context Caller` | [source](g3c-context-caller.jelly), [paste copy](g3c-context-caller.txt) | Select one PDF. Returned Count `2`, extracted native PDF type, full PDF, category `Anthems`. |

Inspect Exit's native return input, the context receiver's List rows, and every
caller consumer. In G3C the File row must be a whole Shortcut Input token, never
the literal words ShortcutInput or a filename string. Extraction must use the
actual Run result and quoted-index pattern, preserving the File as a native item.

Use baseline-versus-returned type and actual PDF viewing rather than hard-coding
an English File/PDF type label. A returned name/Text or empty preview fails even
if a Count looks correct. G3B passing does not establish G3C's mixed List return.

Reuse the existing [Text List interpolation probe](../compatibility/probe-list-text-interpolation.jelly)
and [native context extraction probe](../compatibility/probe-archive-context-loop.jelly)
if needed to isolate sender/extraction defects. They do not prove `exit` success.
Preserve working production positional Text Output; this group does not change it.

## Group 4 — dynamic defaults and the date/name flow

No shortcut dependencies or native insertion slots. Run the literal controls first.

| Test / exact installed name | Files | What to inspect and do |
| --- | --- | --- |
| G4C / `TEST - G4C Default Controls` | [source](g4c-default-controls.jelly), [paste copy](g4c-default-controls.txt) | First default is literal `Alpha`: accept unchanged, preview Alpha. Second must be genuinely blank, without quote characters: type `Delta`, preview Delta. |
| G4A / `TEST - G4A Default Direct` | [source](g4a-default-direct.jelly), [paste copy](g4a-default-direct.txt) | Direct captured variable default should show `Alpha`; current named-variable default should show latest `Gamma`, not initial Beta. Accept unchanged; expect Alpha, Gamma. |
| G4B / `TEST - G4B Default Interpolation` | [source](g4b-default-interpolated.jelly), [paste copy](g4b-default-interpolated.txt) | Same two cases using interpolation. Expect Alpha, Gamma, not `${capturedDefault}`, `${namedDefault}` or quote characters. |
| G4D / `TEST - G4D Date Name` | [source](g4d-date-name.jelly), [paste copy](g4d-date-name.txt) | Native Date question, custom date format, generated name Text, interpolated editable default, then trim of the entered name. Run twice as below. |

Inspect Default Answer **before accepting** each question. A correct final value
typed manually into a broken default does not pass. Record actual field contents
and whether its token points to a captured action or current named variable.
Direct variable defaults are a candidate being compared, not an established fix.

For G4D, inspect that Ask for Input really has type **Date**, Format Date really
has **Custom** format `yyyy-MM-dd - EEE`, and its input is the chosen date token.
The enum spellings Date/Custom/None were checked in the pinned compiler bindings;
this is not proof that the app accepts/exports them correctly. Stop and record any
scope error, wrong input type or silently defaulted format; do not guess another enum.

With English (UK) locale, run using:

| Chosen date | First preview | Second preview / editable default | Final preview after appending ` - TEST` |
| --- | --- | --- | --- |
| 31 December 2026 | `2026-12-31 - Thu` | `2026-12-31 - Thu - Evensong` | `2026-12-31 - Thu - Evensong - TEST` |
| 1 January 2027 | `2027-01-01 - Fri` | `2027-01-01 - Fri - Evensong` | `2027-01-01 - Fri - Evensong - TEST` |

The source uses lowercase calendar-year `yyyy`, not week-year `YYYY`. Record device
locale; different weekday language needs separate interpretation, not an assumed
token failure. Keep typed edits distinguishable from the original proposed name.
G4D combines formatting/defaults/interpolation: if it fails, the earlier G4 tests
help identify the boundary. A successful Date field alone is a partial result.

## Results to send back

Report one test at a time. Start with **G1A**.

```text
Test ID and date:
iPadOS / Jellycuts / forScore versions; locale where relevant:
Source revision/hash (see local build record):
App compile: pass/fail; exact errors and warnings:
Installed name / selected test receiver:
Generated actions/settings/tokens inspected:
Fixture supplied (PDF identities or native Scores, without private paths):
Exact previews / opened scores / default field values, in order:
Expected versus actual:
Native fixture setup only, or probe repaired? List every edit:
Result: not run / fixture invalid / compile failed / export defect / runtime failed / passed untouched / passed with repairs:
Scope established; remaining uncertainty:
```

No test initially has a recorded iPad pass. Source generation, local compilation,
structural export checks, iPad compilation, import and execution are separate stages.
Do not promote one Text success into a native File/Score rule or one probe into
full-service validation. Keep the production sources unchanged until relevant
untouched probes pass; then remove only the corresponding native repair slots.

Source references: [If conditions](../../vendor/jellycuts-docs/markdown/Language_Guide/if_else.md),
[variables and +=](../../vendor/jellycuts-docs/markdown/Language_Guide/variables.md),
[Exit](../../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/exit.md),
[Ask for Input](../../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/askForInput.md),
[Format Date](../../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/formatDate.md),
[Wait to Return](../../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/waitToReturn.md).
Pinned binding inspection: Open-Jellycore `e1ec31c` AskForInputParameter,
Jelly_WFAskActionDefaultAnswer, FormatDateParameter, Jelly_WFInputType,
Jelly_WFDateFormatStyle and Jelly_WFTimeFormatStyle. The old default-answer binding
is enum-based and can omit unsupported values, so even an accepted local export
must be inspected for actual default/type fields. Local compilation is not enough.
