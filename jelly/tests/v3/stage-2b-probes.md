# Stage 2B ready-to-copy probes

Updated 9 November 2026. **T01a revision 2 has a user-reported runtime pass for its displayed results. T01b revision 2 failed compilation with a duplicate magic-variable name. Corrected sources are reviewed only; no local compiler, build or tests run.** These implement the [error-isolation plan](stage-2b-error-isolation.md). Keep the installed production shortcuts and their repairs as evidence.

## Latest device results and correction

T01a, TEST - V3 Date Format, source revision 2: user returned native direct and named cursorDate raw displays `9 Nov 2026 at 12:00`; both ISO outputs were `2026-11-09`, and both weekday outputs were `Mon`. All six displayed values match the expected results. App versions, exact generated settings/types and setup/repair history were not supplied. This establishes the reported fixed native Date routes; it does not establish ISO Text extraction, loop advancement or production resolver correctness. Keep this passing installed probe; no T01a reimport is needed.

T01b, TEST - V3 Extracted Date Format, source revision 2: user reported `Error (Line #29:1): You already have a magic variable named nextReport. You can not have two Magic Variables named the same thing.` No extracted-Date runtime result is established. The source reused `>> nextReport` at two different action sites; report accumulation must use a unique magic-variable capture per source action and then update the mutable named report.

**Revision 3 corrects those duplicate report captures in T01b, T02a, T02b, T03 and T04.** T01a, T05 and T07 remain revision 2 because each has only one report capture. All interfaces remain 1.1. Retry T01b from the complete updated file, then use updated T02a. Date/If logic, exact installed names and native fixture setup slots are unchanged. Compiler acceptance and runtime of revision 3 are pending.

## Run and return reports

Transfer each complete `.jelly` through Copyover. The first comment supplies its exact TEST name. Each shortcut launches directly, ignores incoming input and has no installed helper dependencies or writes. Import only the probe being investigated; no production reimports are needed.

Every current probe accumulates its observed values into **one final Text report**, displayed in Quick Look, then returned as Text on normal completion. Use Quick Look's Share menu to copy the report and paste it into this chat. The report includes the installed test name, source revision, expected results and observed results. T02 includes every iteration; T03 includes all five branches; T04 includes all four fixtures. Add app versions, manual repairs and provider/location when sending it. These cannot be inferred from the captured values.

Checkpoint alerts remain around risky actions. If an action aborts, the final report cannot be reached; send the exact error and last checkpoint instead. Report display strings are captured separately: the Date tests still feed the original native Date or current named Date into Format/Adjust Date. A raw display string does not establish its producer?s native type. Inspect REPORT-FINAL comments: report accumulation and the final cleanup must read current named report, including after loops and branches. Cleanup reuses the existing V3 multiline quote-artifact filter.

| Order | Source / installed name | Setup and expected observation |
| --- | --- | --- |
| T01a | [t01-date-format.jelly](t01-date-format.jelly) — TEST - V3 Date Format | Complete T01-DATE with a native fixed Date, 9 November 2026 at 12:00. Final report includes direct and named raw Date displays, ISO `2026-11-09`, weekday `Mon`. |
| T01b | [t01-extracted-date-format.jelly](t01-extracted-date-format.jelly) — TEST - V3 Extracted Date Format | No setup. Fixed source Text is extracted; count must be 1. Final report includes direct and named extracted Date raw displays, ISO `2026-11-09` and `Mon`. Run independently even if T01a fails. |
| T02a | [t02-date-advance.jelly](t02-date-advance.jelly) — TEST - V3 Date Advance | After a passing T01 native route, complete T02-DATE identically. Current ISO sequence: 9, 10, 11 November. Adjusted raw Dates: 10, 11, 12 November. |
| T02b | [t02-date-completion.jelly](t02-date-completion.jelly) — TEST - V3 Date Completion | After T02a passes, complete T02C-DATE. Seven traces advance 9–15 November. Last trace current/end=`2026-11-15`, complete=`on`. Final report includes all seven traces and complete=on; no failure alert. |
| T03 | [t03-if-operands.jelly](t03-if-operands.jelly) — TEST - V3 If Operands | No setup. Inspect both operands and operator in all five If actions before repair. Expected report branches: N1 TRUE, N2 FALSE, S1 TRUE, S2 TRUE, S3 FALSE. |
| T04 | [t04-folder-captures.jelly](t04-folder-captures.jelly) — TEST - V3 Folder Captures | Select the [complete normal config](../../config/v3-config.example.json), copied as v3-config.json. Reads it once; four names are built in. Expected table below. |
| T05 | [t05-context-lookup.jelly](t05-context-lookup.jelly) — TEST - V3 Context Lookup | Select [v3-week-context.empty.json](../../config/v3-week-context.empty.json). Final report contains fixture name, nonempty key, raw saved-entry display, saved entry count 0 and schema 1. Do not replace or clear the normal context. |
| T07 | [t07-folder-picker.jelly](t07-folder-picker.jelly) — TEST - V3 Folder Picker | Complete T07-PICKER with native Select File, Folders, Multiple off. Run local then Nextcloud with matching contents. Observe picker and enumeration checkpoints; final report includes selected name, direct count and completed boundaries. Add the chosen provider when returning it. |

The fixed native Date and folder-picker slots use documented native completion comments rather than unverified Jelly bindings. Replace only the indicated Nothing action and reconnect its consumers before deleting it. Running an uncompleted slot is not a valid test. These are fixture setup changes; record them separately from later repairs to generated Format Date, If or variable wiring.

For T01, inspect generated Format Date settings **before changing them**. All should be Custom, Time None, with exact `yyyy-MM-dd` or `EEE`. Inspect English UK, Gregorian and Europe/London only where exposed. Each risky route is labelled and raw Date displays are captured separately for the final report before formatting. If an error occurs, record the last route label, exact failing action, actual input token/value and displayed type. A date-looking preview alone does not establish a native Date type. For the second formatter, inspect the same route's raw input token again if needed.

For T02, compare current versus adjusted results. Adjusted Dates stuck at 10 November suggest a stale Adjust Date input. Advancing adjusted results with a stuck current ISO suggest the Set Variable or formatter input. A conversion failure only after the first iteration calls for inspecting what the update stores. In T02b, the final guard and trace must read current named complete, not its original off initializer.

T03 deliberately retains variable-to-variable operands to reproduce the reported omission. Preserve an untouched export/observation before repairs. The source contains both operands; this does not establish that generation emits them. Record each case separately, including branch polarity. A repaired pass is not a fresh generation pass.

| T04 fixture | Raw start month/day | Raw end month/day | Raw year | Match counts year/day/month | Effective start → end | End-month lookup |
| --- | --- | --- | --- | --- | --- | --- |
| HNov8 | Nov / 8 | empty / empty | empty | 0 / 0 / 0 | 11/8 → 11/8 | skipped |
| INov9-15 | Nov / 9 | empty / 15 | empty | 0 / 1 / 0 | 11/9 → 11/15 | skipped |
| Nov30-Dec6-2026 | Nov / 30 | Dec / 6 | 2026 | 1 / 1 / 1 | 11/30 → 12/6 | executed, key dec |
| Dec28-Jan3-2026 | Dec / 28 | Jan / 3 | 2026 | 1 / 1 / 1 | 12/28 → 01/3 | executed, key jan |

T04 reports raw captures between brackets, actual Match counts, lookup entry and effective defaults. Config mappings use padded month Text, so January is `01`. It does not parse dates or calculate year rollover. Match inputs use year:/day:/month: prefixes; dictionary lookup uses original lowercase captures. An absent optional capture must not enter end-month lookup. Keep each Count connected to its own Match output, each guard compared to literal Text 0/1, and final reports connected to current named variables.

T06 remains the existing production local integration checkpoint in the [isolation plan](stage-2b-error-isolation.md), after the isolated tests pass. No duplicate integration shortcut or saving test is introduced. T08 remains conditional on a new loading/compilation crash; preserved crash sources are evidence, not baseline probes.

For each actual result, use the [evidence record template](stage-2b-error-isolation.md#record-one-result-per-test). T01b/T02a/T02b/T03/T04 are revision 3; T01a/T05/T07 are revision 2; all interfaces are 1.1. Record app versions, native-only versus Jelly-generated, untouched generation versus setup/repair, exact source, expected/observed outputs and first failing boundary. If comparing a manually assembled native version, use the same fixed inputs and actions and log it separately. Do not infer compiler acceptance or runtime passes from these source files.
