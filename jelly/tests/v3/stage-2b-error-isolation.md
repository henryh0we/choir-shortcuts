# Stage 2B error record and separate test plan

9 November 2026. Status: **isolated Date routes have reported passes; loop investigation continues**. Ready-to-copy probe sources and expected results are linked in the [probe run sheet](stage-2b-probes.md). Each probe now collects its observations into one final copyable Text report on normal completion; native action failures may abort before the report. This consolidates the recent iPad reports and replaces the sequence of one-off troubleshooting instructions as the next testing plan. It does not claim a working Stage 2B workflow. No local code, compiler, build or automated tests were run to establish correctness.

## Current position

Latest workaround result: standalone **TEST - V3 Adjust Date Minutes**, revision 1, returned `2026-11-10 12:00:00` from `2026-11-09 12:00:00` using `1440 min`; extracted and adjusted Date counts were both 1. All specified outputs match. No manual repair was reported with this result; actual native fields/app versions were not supplied. Minute-based loops, clock-change behaviour and production adoption remain untested; production executable source is unchanged.

Standalone duration probe revision 1 now reproduces the mismatch without a loop or mutable Date cursor: from `2026-11-09 12:00:00`, source `1 day` returned `2026-11-09 12:00:01`, whereas the documented `10 min` control returned `2026-11-09 12:10:00`; all Date counts were 1. This isolates a day-duration interpretation/encoding discrepancy from cursor advancement. It does not identify the app's exact compiler fault or establish an alternative accepted day spelling. See the [duration evidence](stage-2b-probes.md#duration-binding-investigation-9-november).

Latest isolated results, 9 November: T01a revision 2 and T01b revision 3 returned all expected fixed-Date results. T02a revision 4 has a **repaired-runtime pass**: installed Adjust Date was Add 1 second despite source `duration: 1 day`; the user confirmed diagnostic/update connections were correct. After changing the unit to day, current dates advanced 9, 10, 11 November and adjusted Dates were 10, 11, 12 November, all counts 1. This validates the repaired probe's named Date update/consumption. Untouched day-unit generation, T02b completion and production E08 remain unverified. Next is T02b with Add 1 day and both completion-comparison operands inspected. See the [probe evidence and next step](stage-2b-probes.md#latest-device-results-and-correction).

The split sources load by user report. Selecting a copied folder under On My iPad gets past the Nextcloud picker failure. The date helper has returned controlled results through its caller. Four generated If comparisons were found with blank right-hand operands and manually reconnected.

The most recent unresolved failure is **Format Date cannot convert Text to Date**, reported after correcting the two loop date formats to Custom. The exact failing Format Date action and its actual input value have not been identified. Before that change, a seven-iteration trace showed:

```text
Start:   2026-11-09
Current: 2026-11-09
End:     2026-11-15
Complete: off
```

The same values appeared seven times. This proves the displayed cursor did not advance; it does not prove whether Adjust Date failed, the named variable was not updated, or the formatter read a stale value.

Use separate small tests below before another full-service debugging run. Keep the existing installed shortcuts and their native repairs as evidence. The [probe run sheet](stage-2b-probes.md) now supplies independent scratch sources for T01-T05 and T07, including separate extracted-Date and seven-day extension shortcuts. Installation and execution remain unreported.

## Files and versions

| Component | Current repo source | Evidence boundary |
| --- | --- | --- |
| Filename parser | [V3 - Parse Filename](../../shortcuts/reusable/v3-parse-filename.jelly), revision 3/interface 2.0 | Earlier Stage 2A fixture passes; not full Stage 2B acceptance |
| Date resolver | [V3 - Resolve Folder Dates](../../shortcuts/reusable/v3-resolve-folder-dates.jelly), revision 4/interface 1.0 | Installed native repairs are additional to source; date conversion/advancement unresolved |
| Context wrapper | [V3 - Load Folder Context](../../shortcuts/reusable/v3-load-folder-context.jelly), revision 1/interface 1.0 | CONTEXT 1/2 traces establish calls/returns on reported runs; persistence not yet passed |
| Row preparation | [V3 - Prepare Preview Rows](../../shortcuts/reusable/v3-prepare-preview-rows.jelly), revision 1/interface 1.0 | Integrated runtime not established |
| Report renderer | [V3 - Render Service Preview](../../shortcuts/reusable/v3-render-service-preview.jelly), revision 1/interface 1.0 | Integrated runtime not established |
| Main | [V3 - Preview Services](../../shortcuts/main/v3-preview-services.jelly), revision 2/interface 1.0 | Local picker succeeds; complete preview not established |
| Config | [Complete normal config](../../config/v3-config.example.json) | Version 3; already prepared for Copyover |

Loading, compiler acceptance, native action generation, import, manual repair and runtime are separate evidence stages. The user's statement that files load is not expanded into unreported stages. Record any new result against the exact source revision and installed changes.

## Error inventory

| ID | Reported symptom | What is established | Remaining question |
| --- | --- | --- | --- |
| E01 | Original Preview Services crashes during editor loading; Receive and Compile Jelly also crashes at Compile Jelly Text | Original main was 18,738 bytes. Splitting into smaller installed components allowed the new files to load by user report | Exact compiler/editor trigger; no byte limit or root cause established |
| E02 | Select Files finished with an error after selecting Nextcloud in Files | Selecting a copied local folder under On My iPad passes that boundary | Nextcloud/provider-specific access versus another picker difference; Nextcloud Weekly remains unresolved |
| E03 | No key was provided to Get Dictionary Value | CONTEXT 1 only initially localised it to Resolve Folder Dates. Context key displayed ScannedChoirMusic/INov9-15 and its lookup returned. Start-month key was nov, then optional end-month key was empty | Why the absent optional end-month branch executed: native presence semantics, generated condition or wiring remain unproven |
| E04 | Please choose a value for each parameter | User found a concrete blank right operand in the month-rollover If; more blank comparisons followed | That missing operand is real. Blank optional Match input was a separate hypothesis, not a confirmed explanation for every occurrence |
| E05 | End date failed exact calendar roundtrip | User found checkedEnd and checkedStart comparison RHS fields blank and reconnected them | Actual native parsing/type handling still needs an isolated check; do not remove roundtrip guards |
| E06 | Range reversed or exceeds 7 inclusive days | User found cursorIso/endIso equality broken and repaired it; error persisted. Trace showed 9 November repeated seven times with complete off | Date update, named-variable consumption, format settings and completion flag must be tested independently |
| E07 | Loop Format Date actions lacked expected Custom settings | User changed them to the intended custom formats | Need fresh generation inspection: source format parameters are not established as reliably emitted |
| E08 | Format Date cannot convert Text to Date after those format changes | Input conversion now fails somewhere in the date helper | Exact Format Date action, raw input value/type, and its producer are unknown. This is the first test priority |

These are related observations, not eight proven independent bugs. In particular, E04-E06 may share generation/wiring problems. Avoid changing several candidate causes in one test.

## Confirmed manual comparison repairs

All four right operands were reported blank/broken. Preserve the repairs when inspecting the installed date helper. Reimport may recreate the omissions.

| Source marker/location | Left | Operator | Right | Expected for INov9-15 in 2026 |
| --- | --- | --- | --- | --- |
| V3-DATES-ROLLOVER | endMonthNumber, Calculate Number output | is less than | startMonthNumber, earlier Calculate Number output | 11 < 11 is false |
| V3-DATES-START-ROUNDTRIP | checkedStart, formatted Text | is not | named startIso | Equal 2026-11-09; false |
| V3-DATES-END-ROUNDTRIP | checkedEnd, formatted Text | is not | named endIso | Equal 2026-11-15; false |
| V3-DATES-COMPLETE | cursorIso, this iteration's formatted Text | is | named endIso | True when cursor reaches 2026-11-15 |

Select actual variables/action outputs, not typed variable names. A token attached to the initial Text/Date action is not necessarily the current named variable after an update. The exact cause of these omissions is not established; source already contains both operands.

## Test order and method

Start with T01 and T02. They need no folder picker, config, context file or helper calls. Then test comparison generation (T03), optional captures (T04), context lookup (T05), and integration (T06). Return to Nextcloud (T07) after the local path works. Revisit source-size crashes (T08) only if they recur.

For T01-T05, use disposable independent TEST shortcuts. Do not run production helpers individually without the Lists their contracts require. Initially distinguish **manually assembled native capability** from **the same test generated from Jelly**. If native passes and generation fails, record that boundary rather than rewriting the runtime policy.

Complete `.jelly` files for Copyover are linked in the [probe run sheet](stage-2b-probes.md), with exact name-first headers, documented contracts and adjacent native completion comments. All config/fixture changes must be complete files in the repo; the user cannot edit JSON on the iPad. These probes reuse the existing normal config and empty-context fixtures without modification.

## T01 — native Date, named variable and Format Date

Proposed installed name: **TEST - V3 Date Format**. No input, calls, folders or writes. Purpose: isolate E08 without the range loop.

1. Use a native **Date** set to the fixed date **9 November 2026, 12:00**. This fixed test date is separate from production Current Date.
2. Feed that Date output directly to **Format Date**, Custom **yyyy-MM-dd**; preview the result. Repeat with Custom **EEE**.
3. Set named **cursorDate** to the original native Date output. Format this **named variable** with the same two formats and preview both results.
4. Separately, make Text **2026-11-09 12:00**, run **Get Dates from Input**, and confirm it produces exactly one Date. Feed its output directly into the same formats, then through Set Variable cursorDate and format again.

Expected for every successful route: **2026-11-09** and **Mon**. Use four y characters in yyyy-MM-dd. Inspect English UK/Gregorian/Europe London settings where the action exposes them; do not invent unavailable fields. Keep raw Date, source Text and formatted Text as distinct values.

Record which route first fails: direct native Date, named Date, ISO Text extraction, or named extracted Date. For a failed formatter, preview its exact input immediately beforehand and record that value and the token's displayed type. Do not assume a date-looking string is a native Date. No successful route here is yet recorded.

## T02 — three-day advancement without service logic

Proposed name: **TEST - V3 Date Advance**. No input, calls, folder/config/context or writes. Requires one passing native Date/format route from T01. Purpose: isolate E06.

1. Before the Repeat, set named cursorDate to native Date **9 November 2026, 12:00**.
2. Repeat exactly **three** times. At the start of each iteration, Format Date from **named cursorDate**, Custom yyyy-MM-dd, and show it.
3. **Adjust Date: Add 1 day to named cursorDate**. Inspect that adjusted result separately if necessary.
4. **Set Variable cursorDate** to that Adjust Date output, inside the Repeat. Keep the original initializer outside it.

Expected displayed sequence: **2026-11-09, 2026-11-10, 2026-11-11**. Each adjusted result should be the following day. A Date result must be stored back, not formatted Text.

| Observation | Next boundary to inspect |
| --- | --- |
| Adjusted result stays 10 November every time | Adjust Date may read the original Date rather than current named cursorDate |
| Adjusted result advances but formatted current stays 9 November | Formatter or Set Variable may read the wrong producer |
| First iteration works; next one gives conversion error | Inspect the value/type stored by the update Set Variable |
| All three dates advance | Add the seven-day/completion logic only after recording this pass |

After a three-day pass, extend to seven iterations with endIso Text **2026-11-15** and named complete initially Text **off**. Compare this iteration's formatted cursorIso with endIso; set complete to literal Text **on** when equal. Expected last iteration: current/end 2026-11-15, complete on. Final guard must read the current named complete value. Native-only and Jelly-generated versions require separate results.

## T03 — variable-to-variable If generation

Proposed name: **TEST - V3 If Operands**. No input/dependencies/writes. Purpose: isolate E04-E06 generation omissions without dates or loops.

Use two Calculate outputs with values **11** and **12**, and two named Text variables with values **A** and **B**. Inspect and run these comparisons independently:

| Case | Comparison | Expected branch |
| --- | --- | --- |
| N1 | Number 11 is less than Number 12 | True |
| N2 | Number 11 is less than Number 11 | False |
| S1 | Text A is Text A | True |
| S2 | Text A is not Text B | True |
| S3 | Text A is not Text A | False |

Show a distinct label in each branch so execution is observable. For generated source, inspect **both operand fields and operator before manual repair**; retain an untouched export/observation. Note whether RHS is missing, wrong type, an initializer, or a literal variable name. Then record any repair and rerun. A repaired pass is not a fresh-source generation pass.

Do not substitute hard-coded values into production dynamic comparisons as a workaround: that would lose date/range behavior.

## T04 — optional folder captures and safe lookup guards

Proposed name: **TEST - V3 Folder Captures**. Input fixed fixture names; reads the normal config once; no date parsing, context access or writes. Purpose: isolate E03 and the optional-Match hypothesis.

Use the regex/mappings from the existing [normal config](../../config/v3-config.example.json). Show each raw capture between visible delimiters, such as `endMonth=[...]`, so an absent capture is clear.

| Folder | Start month/day | End month/day capture | Explicit start year |
| --- | --- | --- | --- |
| HNov8 | Nov / 8 | Empty / empty | Empty |
| INov9-15 | Nov / 9 | Empty / 15 | Empty |
| Nov30-Dec6-2026 | Nov / 30 | Dec / 6 | 2026 |
| Dec28-Jan3-2026 | Dec / 28 | Jan / 3 | 2026 |

Revision 4's independent checks use these prefixed inputs:

| Check | Text | Regex | INov9-15 expected count |
| --- | --- | --- | --- |
| Year | year: + explicitYear token | `^year:[0-9]{4}$` | 0 |
| End day | day: + endDayCapture token | `^day:([12][0-9]|3[01]|[1-9])$` | 1 |
| End month | month: + endMonthName token | `^month:[A-Za-z]{3}$` | 0 |

Count each actual Match output; convert Count to Text; inspect the subsequent comparison to literal Text 0 or 1. Do not pass the prefixed Match result into the month dictionary: actual month keys remain lowercase original captures, such as nov/dec/jan.

For INov9-15, defaults must become start month 11, end month 11, start day 9 and end day 15. The end-month lookup must not execute. For a single-date folder endDay defaults to startDay. For an explicit end month, lookup uses its actual lowercase capture. A missing optional value must never become an empty Get Dictionary Value Key.

The original empty-key observation is confirmed; blank-input Match causing the generic parameter error is still a hypothesis. Record action-specific results before treating the prefix change as a proven fix.

## T05 — context lookup without saving

Proposed name: **TEST - V3 Context Lookup**. Fixed folder-name Text plus read of the supplied [empty-context fixture](../../config/v3-week-context.empty.json); no writes or dates. Purpose: separate a missing dictionary entry from a missing Key input.

Construct the nonempty Text **ScannedChoirMusic/INov9-15**. Use it as the actual Key token in Get Dictionary Value, Dictionary = parsed empty-context fixture. The lookup should return no saved range; it must not fail with No key was provided. `_schemaVersion` should read Text **1**.

This exact nonempty key and successful return were already observed inside the installed resolver. Repeat separately only if needed to verify generation/transport. Absence of a saved entry is expected; do not invent one or clear normal persisted context to make this test pass.

## T06 — local integration after the small tests

Use **V3 - Preview Services**, with the existing normal config/context and a copied **On My iPad/INov9-15** folder. Do not run its helpers alone. First confirm the repaired Date/If actions survive in the installed resolver; regeneration can replace manual repairs.

1. Resolver returns schema 1/status resolved, start 2026-11-09/end 2026-11-15, unless saved context supplies a different year.
2. Load Folder Context saves/readbacks only the separate context JSON when needed. Read/save base folders agree. A second run uses saved-context with identical dates.
3. Row preparation consumes the same config snapshot and date-result/file-table Text JSON; no native File transport is assumed.
4. Report groups date/slot and sorts numeric positions. Include positions 2 and 10; retain gaps and repeated pieces at distinct positions. Confirm Monday skipped.

Treat each step as a separate result. Do not claim context persistence, JSON transport, numeric ordering, repeated occurrences or forScore behavior solely because date resolution passes. There are no music/forScore writes in this delivery; separate folder-date bookkeeping may be written before a later failure.

## T07 — Nextcloud versus local folder selection

Proposed name: **TEST - V3 Folder Picker**. Native Select File set to Folders, Multiple off, followed by Name and nonrecursive Folder Contents/Count. No date helper, config/context or writes. Show selected name and direct item count.

Try the same small folder contents under On My iPad, then Nextcloud in Files. Record picker completion separately from folder enumeration. Local selection already passed in the main; Nextcloud selection failed. That comparison alone does not establish why. If provider access fails, keep it separate from date/parser repairs and do not declare Weekly ready.

## T08 — loading/compilation crash if it recurs

The original monolithic main is preserved as [revision-1 crash evidence](fixtures/v3-preview-services-revision-1-crash.jelly). Do not repeatedly resubmit it as the baseline. Record whether a new failure occurs during paste/loading, source preview, Compile Jelly Text, export, or import, plus the exact source/version and app versions. The original date resolver is also preserved as [revision-1 empty-month evidence](fixtures/v3-resolve-folder-dates-revision-1-empty-month.jelly).

The split files load by user report; a size threshold is not established. Only create a smaller reproducer if a specific new source still fails. Compiler acceptance and action generation remain distinct.

## Record one result per test

Copy this record into the evidence log for each actual test. Blank fields are unknown, not implied passes.

```text
Date/time:
Test ID and exact installed name:
Jellycuts / iPadOS / Nextcloud versions, where relevant:
Source path and revision, if generated:
Native-only or Jelly-generated:
Untouched generation or manually repaired:
Input / fixture location:
Compiler warnings/errors:
Action and parameter that failed:
Actual input value and displayed type:
Expected output:
Observed output:
Manual changes and retest result:
Next smallest unresolved boundary:
```

A test passes only when its specified output/action wiring is observed. A generic parent Run Shortcut error does not identify the failing child action. Use a minimal trace around the action being tested; remove only temporary diagnostic actions after preserving the result.

## Existing diagnostics to account for

- In Load Folder Context: CONTEXT 1 before Run Resolve Folder Dates and CONTEXT 2 after it. Preserve Run input and downstream Get Dictionary connection to the Run result.
- In Resolve Folder Dates: optional context-key/month/weekday alerts and the four-field loop alert. Their presence varies after reimports; do not assume they still exist.
- Source `V3-DATES-*` comments identify native checks/repairs; they do not themselves insert the diagnostic actions.
- All Date/Set Variable/If/format repairs made on the iPad must be recorded separately from source-generated behavior. Current repo source expresses intended connections but does not prove Jellycuts emits them correctly.

Installation/reference detail remains in [the Stage 2B guide](stage-2b-services.md). Historical Stage 2A results remain in [README](README.md). Use this document's test order for the current investigation rather than following the older troubleshooting paragraphs one by one.
