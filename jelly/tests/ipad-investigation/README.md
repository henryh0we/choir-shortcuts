# iPad Jellycuts questions and test plan

Created 23 October 2026. These are proposed small experiments, **not executed
tests or ready-to-compile Jelly signatures**. Their purpose is to establish which
source forms generate correct actions and native tokens without manual repair.
Use the installed Jellycuts app for acceptance; the older local CLI is a separate
profile. Read [the incident record](../../docs/ipad-assembly-lessons.md) first.

## Run and record consistently

Create each future probe as a separate TEST shortcut in this directory, with a
.jelly source and byte-identical .txt copy. Check relevant local documentation
before writing unfamiliar bindings; do not guess date or forScore functions.
Reuse [existing compatibility probes](../compatibility/README.md) when they answer
the same question. Compile locally through the repository wrapper when creating
source, then compile/export/import on iPad and inspect actions before execution.

Compare an untouched export with a duplicate repaired in Shortcuts. Record every
manual edit. Keep production shortcuts unchanged. P01-P08 can use constant Text
and disposable Files; P09-P12 use a disposable forScore setlist/library. Clear only
that explicit test setlist when testing replacement. Record app versions, library
selection and actual side effects. Do not claim a repaired probe passed untouched.

## Priority 1: references, operators and text

| ID / question | Small test and expected evidence | Current evidence / result |
| --- | --- | --- |
| P01: Does nil export with the correct polarity? | Four checks: empty has value / empty has no value / populated has value / populated has no value. Use a Nothing-initialised named variable, then assign Alpha. Inspect all native operators and inputs; distinct marker outputs must show absent before assignment, present after it. | WorkingScore absence exported/was installed as presence in this incident; cause unresolved. Isolated test: Not run. |
| P02: Do named variables resolve their latest assignment? | Initialise Nothing, assign Alpha then Beta; preview before/after, after a loop and after a branch. Repeat with a disposable PDF and native Score separately. Consumers must show current values, not initialisers. | Multiple consumer reselections repaired service run. General source pattern: Not established. |
| P03: Are count comparisons wired to both outputs? | Collect one then two items; compare actual count against matching and deliberately different expected count. Show numeric operands. Equal must continue; unequal must stop. Inspect **is not** and both tokens, including inside/outside loops. | COL01-COL03 and readback reselections worked manually. Untouched probe: Not run. |
| P04: Which Ask for Input defaults become tokens? | Use known Text Alpha as default, named Text Beta, literal empty default, title/composer-style defaults and a dedicated Text action as default. Inspect Default Answer before running; expect values, no literal expressions or quote characters. | Title/composer interpolation and empty service default failed in full export; manual token replacement worked. Probe: Not run. |
| P05: Which List forms preserve values and native types? | Run existing two-Text sender/receiver and native context probes, then generate callers with filename/regex and PDF/Folder/Dictionary. Inspect each row token, show receiver count and each item's actual use: PDF preview, Folder enumeration, Dictionary key lookup. | Text interpolation probe and native context loop have prior device evidence. Full sender combinations need isolated untouched tests. |
| P06: Do action replacement and renaming preserve consumers? | Duplicate a harmless probe. Replace one Nothing slot with Text; inspect every old consumer before and after explicit reconnection. Test a renamed installed callee with an exact constant marker to identify target. | Wrong Archive target received naming List in this session. Replacement auto-reconnection must not be assumed. Probe: Not run. |
| P07: Which branch forms duplicate magic-variable registration? | Two minimal equivalent sources: If/Otherwise each capturing distinct outputs, versus complementary If checks. Exercise both branches and inspect action counts. Test nesting/loop placement separately, not all at once. | Assembly 14 duplicate captures failed; Assembly 15 complementary checks compiled. Cause and wider scope: unresolved. |
| P08: Do Output actions return native objects through callers? | Existing Output fixture for Text, then native PDF return via a documented/manual return slot. Caller immediately previews actual Run Shortcut result. Test success and explicit error Text separately; inspect recipient behaviour and warning text. | Naming Text and archive PDF returned in repaired service. Untouched File-return generation remains unverified. |

## Priority 2: collections and forScore

| ID / question | Small test and expected evidence | Current evidence / result |
| --- | --- | --- |
| P09: Do native collections preserve type and repetitions? | Add two known Scores to a Nothing-initialised named collection, then A again. Count must be 3. Writing Repeat sends each native Repeat Item to a disposable setlist with Skip off. Inspect A/B/A identity and Manual order. Compare editor Text label with actual consumption. | One Score reached setlist despite displayed Text label. Multiple/repeated Scores: Not run. |
| P10: Which import action imports a PDF into the intended library? | Test Import file(s) and Import score(s) independently, one uniquely named disposable PDF each, Conflict Handling Skip. Record expanded inputs, available library control, returned type, lookup after import and second import's effect. Do not run both on the same PDF as a routine workflow. | Both cards previously displayed Import Files; successful branch/action identity not recorded. Not run as isolated test. |
| P11: Does Create Setlist return a reusable native object? | Create an unused name, set named targetSetlist from New Setlist, then read entries and open that exact object without a chooser. Separately test existing-setlist chooser branch and cancel path. Check all consumers use named targetSetlist. | Native Create new assignment/open confirmed by user. Untouched Jelly generation and Replace existing branch: Not run. |
| P12: What do library and sorting controls do? | With two explicit disposable libraries, compare Current Library with explicit selection; record active library and results. Test blank only after recording defaults. Read a known B/A setlist in Manual order; distinguish retrieval Title sorting from entry sorting. Confirm score lookup, creation, import and setlist readback use intended library. | Current Library was selected in service fixture; switching/blank semantics remain unverified. |

## Priority 3: date and integration fidelity

| ID / question | Small test and expected evidence | Current evidence / result |
| --- | --- | --- |
| P13: Can the service-date default be generated faithfully? | Establish documented Ask Date / Format Date bindings first. Choose 23 October 2026; English UK custom yyyy-MM-dd - EEE and Evensong token must produce 2026-10-23 - Fri - Evensong. Use 1 January 2027 to catch week-year YYYY mistakes. Edit final name and confirm trim/report/Create Setlist consume the edited output. | Native date/name flow works by user report. Source generation: Not run. |
| P14: Are nested actions and stops preserved? | Use existing flush-left If/Output evidence. Add one nested presence branch and one loop, with unique markers. Inspect native structure, conditions, outputs and warnings. Keep positional Output; do not guess warning-suppression arguments. | Flush-left fixture and manually repaired full service work; untouched full nesting fidelity unverified. |
| P15: Does a fresh service export need fewer repairs? | After resolving priority probes, import a fresh annotated Assembly under a TEST name. Follow only marked native slots and reconnect comments. Run one score, then B/A, A/B/A, Replace existing on test setlist, reuse unchanged, review metadata and cancel before writes. Track every undocumented repair as a generation defect. | One-score completed installed fixture passed. Fresh regeneration and wider regression cases: Not run. |

## Capture a result

Copy this record per test; attach exact source/hash and exported artifact where
available. A screenshot of an operator/token and the action it came from is more
useful than “it worked”. Redact private file locations.

```text
Test ID / date / tester:
iPadOS / Jellycuts / forScore versions; compiler build if available:
Source file / revision / SHA-256:
Input fixture / selected library / active library:
Local compiler result and report path (separate profile):
iPad compile result; exact errors and warning text/count:
Untouched export inspection: actions, If polarity, token producers, defaults:
Import result / installed name / Run Shortcut targets:
Runtime expected / actual; actual counts and native object behaviour:
Manual repairs, in order (none if untouched):
Result before repair / result after repair:
Side effects and cancellation point:
Conclusion: confirmed scope / unresolved cause / next smallest experiment:
Source rule or repair comment to adopt, with evidence link:
```

A pattern earns a preferred-generation rule only after its untouched export and
runtime pass for the relevant type/scope. A manually repaired success earns an
explicit native repair instruction. Neither implies all shortcuts will work first
time; this record makes remaining uncertainty visible before a full service run.
