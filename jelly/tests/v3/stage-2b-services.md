# Stage 2B: dated, grouped and ordered preview

**Current investigation, 9 November 2026:** use [the consolidated error record and separate test plan](stage-2b-error-isolation.md). It collates reported failures/repairs and starts with isolated Date conversion and advancement tests. The older troubleshooting paragraphs below are historical steps, not a sequence to keep applying. No new Shortcut source or config is delivered by that documentation update.

8 November 2026. **The user confirms all newly supplied split shortcuts load correctly.** This records successful loading; exact compile/import actions, native setup and integrated runtime have not yet been reported. No local code/builds/automated tests were run to establish correctness. Stage 2A filename-preview passes remain separate evidence.

## What to change now

**Latest concrete native defect:** revision-4 rerun still reports Please choose a value for each parameter; the user found the rollover If with left endMonthNumber and **blank right operand**, with Less Than highlighted red. Repair this installed action before further source changes: left is the Calculate output for endMonth (**endMonthNumber**), operator **is less than**, right is the earlier Calculate output for startMonth (**startMonthNumber**). Keep right-hand operand a Number token; do not type the variable name as literal Text. For INov9-15 both values should be 11, so the +1-year branch is skipped. Rerun the same main/local folder. This identifies a concrete missing parameter, but a successful full run is not yet recorded and other unset fields are not ruled out. Adjacent source comment V3-DATES-ROLLOVER records the manual repair. No reimport or config edit is needed; source already expresses the intended comparison. Do not attribute the earlier required-parameter error conclusively to blank optional Match input; that was an unverified candidate.

**Latest correction candidate: Resolve Folder Dates revision 4.** CONTEXT 1 followed by the required-parameter error persists after revision 3's Date relocation. The precise failing native action remains unknown. Source review identifies a likely blank-input boundary introduced by revision 2: matching absent optional year/end-day/end-month directly. Revision 4 constructs nonempty Text (year:/day:/month: plus the original capture) before each Match and anchors its regex to that prefix. Counts/defaults are unchanged. This candidate has no device pass; no local builds/tests were run.

To preserve installed Current Date wiring, apply three manual edits in **Resolve Folder Dates** instead of reimporting: add a Text immediately before each optional-capture Match Text action; use the literal prefix plus the original capture's actual variable token; connect Match Text input to that new Text output; change only its regex as follows. Leave Count connected to Match output and preserve existing 0/1 If comparisons.

| Optional check | New Text content (prefix plus token) | Match regex |
| --- | --- | --- |
| Year | `year:` + explicitYear | `^year:[0-9]{4}$` |
| End day | `day:` + endDayCapture | `^day:([12][0-9]|3[01]|[1-9])$` |
| End month | `month:` + endMonthName | `^month:[A-Za-z]{3}$` |

For INov9-15 with no saved context, expect year: (0 matches), day:15 (1), month: (0). Rerun the same main/local folder. If the error persists, identify the exact action with before/after alerts at these checks before further source changes. The full repo source also contains the edits; after replacement complete the top-level Current Date slot again. Other shortcuts/config/context remain unchanged.

**Latest setup simplification: Resolve Folder Dates revision 3.** Current Date is now stored at the very top: native Date (Current Date) -> Set Variable currentDate. Replace only the date helper source if adopting this revision, complete that top-level slot, and keep Set Variable connected to the new Date output. Later consumers use named currentDate. Optional-capture count corrections from revision 2 remain. No config/other shortcut changes. This does not claim to resolve the subsequently reported unspecified missing-parameter error; its action is still unidentified. Source review only, no local builds/tests.

**New targeted source delivery: Resolve Folder Dates revision 2.** The trace for local INov9-15 shows start-month key `nov`, followed by an empty end-month key inside a branch that should have been skipped. This identifies the failing optional end-month lookup; it does not establish whether native has-value semantics, generated If polarity or token wiring caused the branch to run.

Replace ONLY [V3 - Resolve Folder Dates](../../shortcuts/reusable/v3-resolve-folder-dates.jelly) with revision 2/interface 1.0 through Copyover. Complete its single V3-DATES-CURRENT native Current Date slot again, reconnecting the adjacent missing-value If and year Format Date. Keep all other shortcuts/config/context unchanged. Keep the two context-call alerts temporarily if useful. The [revision-1 resolver](fixtures/v3-resolve-folder-dates-revision-1-empty-month.jelly) is preserved as evidence.

Revision 2 replaces optional year/end-day/end-month presence tests with Match Text -> Count Items -> Text comparisons. Inspect the new V3-DATES-END-MONTH block: Match input=endMonthName; Count input=that Match output; If=count Text **is 1**. For INov9-15 this count must be 0, preserving November and skipping the empty-key lookup. Year count 0 selects current year; end-day count 1 selects 15. Source review only; no local builds/tests or device pass are claimed.

Rerun the same local INov9-15 folder. Expected resolved range is 2026-11-09 through 2026-11-15 (unless saved context supplies the year); no end-month lookup should execute. Report the next result/error. Once this passes, check a single-date folder and an explicit end-month range to cover both default and supplied captures.

The general setup below is performed in the **Apple Shortcuts editor after generation/import**. It still applies to the replacement date helper. No JSON editing is required.

There are **three Nothing placeholders to replace in total**, plus existing action settings/connections to inspect. The latter need changing only if the generated actions differ from the settings below. Keep every other Nothing/initializer. There are no Stop/Output blocks to insert.

| Installed shortcut | Required additions | Existing actions to inspect |
| --- | --- | --- |
| V3 - Resolve Folder Dates | One Date action, set to Current Date | Date formats and Add 1 day |
| V3 - Load Folder Context | None | Get File and Save File use the same context location; date-helper target |
| V3 - Prepare Preview Rows | None | Filename-parser target; configured date format |
| V3 - Render Service Preview | None | Numeric comparisons and final Text result |
| V3 - Preview Services | One fixed File action; one single-folder picker | Three helper targets; folder recursion off |

Keep exact installed names as shown. **V3 - Parse Filename** remains revision 3/interface 2.0. Main Preview Services is revision 2/interface 1.0; Resolve Folder Dates is revision 4/interface 1.0; the three split helpers remain revision 1/interface 1.0. Earlier revision notes below are history, superseded by the latest delivery above.

## 1. Put the two JSON files in place

- Use the complete [normal Stage 2B config](../../config/v3-config.example.json) through Copyover, saved as **v3-config.json** in your chosen config location. Use this normal config, not a conflicting-rule, wrong-version or saved-context test config.
- For the first installation only, save [the supplied initial context](../../config/v3-week-context.empty.json) as **iCloud Drive/Shortcuts/V3-week-context.json**. This is a different file from config. If that context file already contains saved dates, retain it; do not replace it with the empty version.

Normal config/context are unchanged by the shortcut split. If these files are already in place, keep them. The config's `contextPath` supplies the filename **V3-week-context.json**; select **iCloud Drive/Shortcuts** as the base folder in both context actions below. Do not select the music folder as the context destination.

## 2. V3 - Resolve Folder Dates

Find **V3-DATES-CURRENT** immediately after import at the top of revision 3. The Current Date action and its Set Variable now live outside all branches.

1. Add native **Date**, set to **Current Date**, immediately before the Nothing directly below that comment.
2. Set the immediately following **Set Variable currentDate** input to the new Date action's actual output. Preserve this Set Variable.
3. The later missing-value If and current-year Format Date must read the **named currentDate variable**. The If is **does not have any value**; Format Date uses Custom **yyyy**. No additional Date action belongs in that branch.
4. Delete only the replaced top-level Nothing after reconnecting Set Variable.

Inspect the other existing actions; add no further placeholders/actions:

| Format Date output in source | Input | Custom format |
| --- | --- | --- |
| currentYear | Named currentDate set at the top | yyyy |
| checkedStart | nativeStart from Get Dates | yyyy-MM-dd |
| checkedEnd | nativeEnd from Get Dates | yyyy-MM-dd |
| cursorIso | Current named cursorDate | yyyy-MM-dd |
| cursorShort | Current named cursorDate | EEE |

Use Gregorian calendar, English (United Kingdom) locale and Europe/London time zone wherever the action exposes those settings. These are inspection requirements; do not add guessed fields when the UI does not offer them. EEE must produce Mon/Tue/Wed/Thu/Fri/Sat/Sun for the supplied mapping. The source errors on an unmapped weekday.

At **V3-DATES-RANGE**, the existing **Adjust Date** must be **Add 1 day** to current named **cursorDate**. The following Set Variable must update cursorDate from that Adjust Date output. The final executable action is **Get Dictionary from finalResult** outside all branches. No helper target needs selecting here.

## 3. V3 - Load Folder Context

**No Nothing replacement or new action is required.** The two context-file settings now live in this shortcut, not in Preview Services.

At **V3-SERVICES-CONTEXT-READ**, inspect the existing Get File action:

| Setting | Required value |
| --- | --- |
| Base/source folder | iCloud Drive/Shortcuts |
| Path/subpath | Actual **contextPath** variable token, normally V3-week-context.json |
| Show document picker | Off |
| Error if not found | Off |
| Multiple files | Off, if exposed |

At **V3-SERVICES-CONTEXT-SAVE**, inspect the existing Save File action:

| Setting | Required value |
| --- | --- |
| Input | Actual **contextToSave** Text token |
| Destination/base folder | The SAME iCloud Drive/Shortcuts folder as Get File |
| Path/subpath | Actual **contextPath** token |
| Ask where to save | Off |
| Overwrite existing file | On |

The Get Text immediately after Save File must use **that Save File action's output**, not the earlier Get File output. Preserve the following Dictionary readback and range comparison.

Its Run Shortcut must target **V3 - Resolve Folder Dates**. Input is the preceding List with **three Text items in order**: folderName, configJson, contextJson. These must be variable tokens, not typed variable-name labels. Keep Get Dictionary connected to that Run Shortcut result.

## 4. V3 - Prepare Preview Rows

**No Nothing replacement or new action is required.**

- Select **V3 - Parse Filename** in its existing Run Shortcut. Input is the preceding two-item Text List: **sourceName**, then **configJson**. Get Dictionary must consume this Run Shortcut result.
- At **V3-SERVICES-NAME**, inspect existing Format Date: **Custom** format is the **nameDateFormat variable token** (normally yyyy-MM-dd). Input contains the **serviceDate token followed by literal ` 12:00`**. It must not contain typed `${serviceDate}` or `${nameDateFormat}` expressions. Inspect the same locale/calendar/time-zone settings as above where exposed.
- Keep the duplicate-position comparisons and Dictionary updates. Its last executable action remains **Get Dictionary from finalRows**. It does not display a report or take a config File directly.

## 5. V3 - Render Service Preview

**No setup values, helper targets or Nothing replacements are required.**

Inspect **V3-RENDER-SORT** only: the date/group/position comparisons must use the corresponding **Calculate Number outputs**, with the less-than/equality operators shown in source. They must not compare typed variable names or initial zero values. The final **Get Text** uses current named **report** after quote-line cleanup. Leave display to the main shortcut; do not add Quick Look or Stop actions here.

## 6. V3 - Preview Services

This is the shortcut to launch for the actual folder preview.

### A. Fixed config File

Find **V3-SERVICES-CONFIG**, near the top, outside the branches.

1. Insert native **File** immediately before its following Nothing. Choose your normal **v3-config.json** in that File action. This is a fixed reference, not Select File.
2. Reconnect the next missing-value If to the new File output, condition **does not have any value**.
3. Reconnect the following **Get Text** (inside the next ready-state If) to that same File output.
4. Delete only this replaced Nothing after both consumers are reconnected.

### B. Select one music folder

Find **V3-SERVICES-FOLDER**, inside the later ready-state branch.

1. Insert native **Select File**, set to **Folders**, with **Select Multiple off**, immediately before its following Nothing. Leave it at this position inside the branch.
2. Reconnect the following missing-value If to that picker output, condition **does not have any value**.
3. Reconnect the later **Get Details of Files: Name** to that same picker output. This supplies folderName.
4. Reconnect the later **Get Contents of Folder** at **V3-SERVICES-FILES** to that same picker output. Set **Recursive off**. Count and Repeat must continue using this Folder Contents output.
5. Delete only the replaced Nothing after all three consumers are reconnected.

### C. Select the three helper targets

Check the existing Run Shortcut actions in this order:

| Target | Preceding List contents, in order |
| --- | --- |
| V3 - Load Folder Context | folderName Text; configJson Text |
| V3 - Prepare Preview Rows | configJson Text; datesJson Text; filesJson Text |
| V3 - Render Service Preview | rowsJson Text; report Text |

Use actual variable tokens in each List. Do not select Resolve Folder Dates directly in this main: Load Folder Context owns that call. Keep JSON serialization/Get Dictionary connections as generated unless inspection shows a missing/wrong token. The final Quick Look and Get Text both use current named report.

## 7. Run the first check

Newest native inspection: user reports both loop Format Date actions were not set to the expected Custom formats and changed them; the next error is Format Date cannot convert Text to Date. The exact failing Format Date/input value is not yet identified. Use Custom `yyyy-MM-dd` (four y) and `EEE`, but do not treat the format string as the cause of an input conversion failure. Inspect the failing action's actual input token; if it is the loop formatter it must receive current named cursorDate retaining a native Date from nativeStart/Adjusted Date, not a typed variable name, a formatted date Text initializer or another loop output. Temporary Quick Look immediately before that failing action, consuming the exact same input token, can reveal the actual value. Preserve the once-only cursorDate initializer and per-iteration native Date update. No passing advancement or new source repair is established.

Latest loop trace for local INov9-15: user reports seven identical alerts, start 2026-11-09/current 2026-11-09/end 2026-11-15/complete off, then CONTEXT 2. This establishes correct displayed endpoints and no displayed cursor progression; it does not distinguish a stale Format Date input from a failed/incorrectly wired Adjust Date/Set Variable. Inspect BOTH loop Format Date inputs and Adjust Date input for CURRENT NAMED cursorDate. Adjust must Add 1 day; its following Set Variable cursorDate must consume that Adjusted Date result within the complete-is-off branch. Preserve the once-only cursorDate=nativeStart initializer outside Repeat. Add a missing update Set Variable only if inspection confirms it is absent. V3-DATES-CURSOR records these exact native connections; no reimport/config change is needed. Rerun for dates 9 through 15 and complete on at the last iteration; no pass is recorded yet.

Newest range result: the user confirms the cursorIso/endIso equality was also broken and repaired, but INov9-15 still returns the same range-incomplete result. Four blank RHS comparisons are now reported (rollover, start roundtrip, end roundtrip, loop completion); do not infer that the remaining error is solved by those repairs. Next inspect actual loop values before changing the algorithm: add ONE temporary Show Alert inside the active Repeat, immediately after the cursorIso/endIso If ends and before the complete-is-off Adjust Date branch. Display startIso, cursorIso, endIso and CURRENT NAMED complete with actual tokens. Report alert count plus first/last values. Expected seven active iterations 2026-11-09 through 2026-11-15, with complete=on at the last. Constant cursor indicates advancement/consumer wiring; matching end with complete still off indicates equality/assignment wiring; complete on here but final unresolved indicates downstream guard reads the wrong value. These are diagnostic branches, not observed causes.

Latest native wiring reports: the user found BOTH checkedStart-is-not-startIso and checkedEnd-is-not-endIso generated with blank right operands, in addition to the earlier rollover comparison. After reconnecting them, the next reported result for local INov9-15 is unresolved with Range is reversed or exceeds 7 inclusive days. This means the controlled range-incomplete path returned; it does not prove actual dates are reversed or overlong. Next inspect the loop's `cursorIso is endIso` comparison, especially its right operand, and its true-branch Set Variable complete=literal on. Adjacent V3-DATES-COMPLETE records exact wiring. If correctly connected and still incomplete, inspect actual startIso/endIso and per-iteration cursorIso plus cursorDate advancement before changing date policy.

Latest result after the native rollover-If RHS repair: the user sees both CONTEXT 1 and CONTEXT 2 and receives `FOLDER: INov9-15 | STATUS: unresolved | REASON: End date failed exact calendar roundtrip`. This confirms the nested helper returned a controlled Dictionary-compatible result and the caller displayed its failure. It does not establish successful date resolution/context save or downstream row/render processing. The helper reached the native end-date roundtrip comparison; do not change folder conventions or remove that guard.

Next targeted inspection: insert a temporary Text/Quick Look immediately before `if(checkedEnd != endIso)` in the installed date helper. Display current named endIso (expected), endDateText (native parse input), checkedEnd (formatted result), and optionally startIso/checkedStart, using actual tokens. Preserve If operands/connections; Quick Look must not replace either date token. For INov9-15 in current-year 2026 expect endIso=2026-11-15, endDateText=2026-11-15 12:00, checkedEnd=2026-11-15. If display values agree but the If still fires, inspect native If polarity/operands and whitespace before changing calendar logic. No source/config replacement is required for this diagnostic.

Latest date trace, 8 November: using local **INov9-15**, the user sees `DATE KEY: ScannedChoirMusic/INov9-15`, then `DATE CONTEXT LOOKUP RETURNED`. The dynamic context-key lookup is therefore populated and completes; do not change it or infer that the saved entry exists. The remaining missing-key failure lies later in the date resolver, subject to the continuing same-error report. Remaining Get Dictionary Value actions use lowerStartMonth, optional lowerEndMonth, and lowerWeekday. For INov9-15 normal flow expects nov, no end-month lookup (month omitted), then English weekday keys beginning mon in 2026. Temporary before-action alerts at those three lookups can identify the last reached action and actual key without changing source/config logic.

Trace result, 8 November: **CONTEXT 1 appears, then failure; CONTEXT 2 does not appear.** This localises the missing-key error to the nested **V3 - Resolve Folder Dates** call. Load Folder Context's post-return lookups/readback are not reached.

Next focused check: in the installed date resolver, find its first dynamic Get Dictionary Value after the Text joining sourceNamespace/folderName and Set Variable contextKey. This lookup's Key must use current named contextKey (or the immediately producing combined Text output), Dictionary=contexts; for HNov8 with normal config the key is ScannedChoirMusic/HNov8. A missing saved entry is allowed and must not be repaired by inventing a context key. Inspect both the key field and actual produced Text. If the key field is blank or linked to the initial empty contextKey value, reconnect it to the immediately preceding combined Text result. If still unclear, temporary Show Alerts immediately before/after this lookup distinguish earlier literal-key failure, this lookup, and later month/weekday lookups; preserve all existing output connections. No source/config replacement is inferred from the first trace alone.

Latest inspection: the user confirms the first two lookup Key fields in Load Folder Context appear correct, but the parent main only highlights Run Load Folder Context. The exact child lookup remains unknown. To locate the boundary without reimporting, add two temporary native Show Alert actions in the installed **V3 - Load Folder Context**, inside its ready-state branch: immediately BEFORE Run Resolve Folder Dates, literal `CONTEXT 1 - calling date helper`; immediately AFTER that Run and before Get Dictionary, literal `CONTEXT 2 - date helper returned`. Disable Cancel. Preserve Run input=the preceding dateInput List and Get Dictionary input=that Run's output, never either alert's output. Adjacent source comments V3-CONTEXT-TRACE-BEFORE/AFTER record this manual-only diagnostic; executable source is unchanged.

Rerun the normal main with the local folder. No first alert means failure in Load Folder Context before the nested date call (inspect the next literal `_schemaVersion` lookup as well as the already checked keys). First alert only means the error propagates from Resolve Folder Dates. Both alerts mean the helper returned and the failing lookup is later in Load Folder Context. Report which alerts appeared before changing keys/config. Remove only these temporary alerts after diagnosis. Do not run the helpers alone without their input Lists.

Latest follow-up, 8 November: a copied folder under On My iPad passes the earlier Select Files boundary. The next reported error is at the main's Run V3 - Load Folder Context: **No key was provided to the Get Dictionary Value action**. This is a missing lookup-Key input, not proof that a named JSON field is absent. The exact failing child action is not yet identified; the error may propagate from Resolve Folder Dates. Date resolution/context save and downstream rows/render remain unverified. No config/source repair is inferred yet.

Inspect the installed Load Folder Context Get Dictionary Value actions in order: literal keys `weekFolderDates`, `contextPath`, `_schemaVersion`, then (after Run Resolve Folder Dates) `schemaVersion`, `status`, `reason`, `startDate`, `endDate`, `qualifier`, `yearSource`, `contextKey`. The last readback lookup uses the actual current named `contextKey` token, not a literal expression or empty initializer. If the error comes from its nested Run Resolve Folder Dates, inspect that helper instead; do not replace all keys or regenerate every shortcut. Identify the first blank Key field and its position before choosing a lasting source repair.

Latest runtime attempt, 8 November: after completing the native reconnections, the user selected a folder in **Nextcloud in Files** and received **Select Files finished with an error. The operation couldn't be completed. Select Files finished with an error.** Treat folder selection as the first reported failing boundary; successful return of a Folder and downstream date/context/row/render execution are not established. No source repair or compiler failure is inferred from this native picker error.

Next diagnostic: in Files, COPY a small HNov8 folder (or create a local HNov8 folder containing copies of two or three of its PDFs) under **On My iPad**. Preserve its folder name and PDF names. Launch the unchanged main and choose that local folder. Keep config and context references as configured; no reimport or JSON edit is needed. If folder selection succeeds, continue to the next actual result/error. If the same Select Files error occurs locally, inspect the single-folder native picker/settings next. This is a provider-isolation check, not a permanent replacement for Nextcloud discovery.

Research: [Nextcloud iOS issue 3261](https://github.com/nextcloud/ios/issues/3261) reports Shortcuts folder-access failures through its File Provider, with later discussion of other providers and Apple changes. Its reproduction uses other actions/versions, so it is related evidence only; it does not prove this exact picker failure's cause or that every Nextcloud folder operation fails.

Launch **V3 - Preview Services** and choose **HNov8**. Expect 2026-11-08, Sunday Eucharist, and numeric positions with 10 after 9. Run again: the same dates/order should return with year source **saved-context**. The detailed expected output is below.

If it stops, report the exact message and shortcut/action where it stopped. Successful loading is recorded; integrated runtime, JSON transport, context persistence and numeric order still require this device result. No regeneration is required merely to apply this guide.

## Earlier crash evidence and split

Revision 1 crashed while loading in the editor and specifically at Compile Jelly Text through Receive and Compile Jelly. Notes accepted it; section pasting still crashed. Its original 18,738-byte [source is preserved](fixtures/v3-preview-services-revision-1-crash.jelly), not an active dependency. No hard byte limit or exact source trigger was established. Revision 2 splits context handling, rows and rendering; the user now confirms all new files load successfully. Exact generation/import/runtime outcomes remain separately unconfirmed.

The [developer's release history](https://apps.apple.com/gb/app/jellycuts/id1522625245) documents earlier editor fixes; [official documentation](https://docs.jellycuts.com/) describes long-file highlighting/wrapping work. Those are historical context, not a diagnosis of this crash. No Bridge, local build, comment stripping or bulk Stop repair was introduced.

## What this delivery does

- Selects one supported date folder and reads only its direct contents. It does not recursively discover other collections or select the music again.
- Uses the existing shared filename parser and one config snapshot. No native PDF collection is rebuilt or indexed. Row Dictionaries contain serializable Text only.
- Resolves saved folder dates first, then an explicit start year in the folder name, then the current year. No historical weekday/year inference or year prompt.
- Enumerates at most seven inclusive calendar dates. Filename weekdays outside that range are unresolved. A single-date folder cannot assign music from another day.
- Groups available music by ISO date/stable slot. Service identity is `YYYY-MM-DD/slot`; leading folder letters, qualifiers and display names are excluded.
- Sorts dates chronologically and positions numerically within a service. Same-date services appear in their first-encounter order. This is provider order for service headings, not a tap-order claim. Gaps are preserved; missing numbers alone do not produce missing-music warnings.
- Marks every file sharing one service/position unresolved, rather than choosing one or inventing a tie break. Repeated pieces at distinct positions remain distinct occurrences. Nothing is deduplicated by canonical piece name.
- Uses `setlistNaming.dateFormat` and the `{date}`, `{dayShort}`, `{serviceName}` template for display. Qualifiers and canonical payloads are preserved.
- Shows unassigned/skipped entries separately. No usable music means no service proposal. Direct folders/non-PDF names are not parsed as music; PDF extension alone is not native PDF validation.

The only write is **folder-date bookkeeping** in the separate context JSON, after successful date resolution and before file discovery. This may happen even for an empty/over-limit folder or a later cancelled/failed preview. Config, source PDFs, archive and forScore remain untouched. Saved context is keyed by configured `sourceNamespace` plus exact folder name; this checkpoint assumes one source namespace. Selecting identically named folders from different roots is not a verified source-identity mechanism. Their eventual full source locators belong to the later plan/discovery contract.

No execution plan/native File transport, dated schedule overrides, archive, imports, metadata, setlist lookup/write, proposal editing or assembly is implemented here. Those requirements remain in the overall plan. This checkpoint does not complete every Stage 2 acceptance criterion or authorise promotion to Weekly execution.

## Supported folder syntax

English three-letter months Jan through Dec; optional single leading ASCII letter; positive day without leading zero; optional range; optional `-YYYY` giving the start year; optional final parenthesized qualifier. Matching is case insensitive. Spaces, full month names, ISO-named folders and historical event folders are not supported by this pattern.

| Folder | Interpretation with current year 2026 and no saved context |
| --- | --- |
| HNov8 | 2026-11-08 only |
| HNov7(ATB) | 2026-11-07 only; qualifier `(ATB)` preserved |
| INov9-15 | 2026-11-09 through 2026-11-15 |
| Nov30-Dec6-2026 | 2026-11-30 through 2026-12-06 |
| Dec28-Jan3-2026 | 2026-12-28 through 2027-01-03 |
| Nov30-6 | Unresolved; crossing months requires explicit end month |
| Nov9-16 | Unresolved; eight inclusive days exceed this checkpoint's limit |
| Nov31 | Unresolved on failed calendar extraction/roundtrip, or native action abort; never an authorised date |
| YouthChoir / ScannedChoirMusic | Unsupported; folder contents are not assigned |

Do not change the iPad's system date for these checks. Explicit folder years make boundary cases reproducible. Native Get Dates/date arithmetic/formatting are new device boundaries: inspect Gregorian calendar, English UK locale and Europe/London time zone wherever exposed. If EEE yields an unmapped local weekday, the resolver errors rather than inventing a day.

## First iPad checkpoint: HNov8

Start with **V3 - Preview Services**, selecting your actual **HNov8** folder (or disposable copies with that same folder name).

Expected on the first run in 2026:

- Dates: **2026-11-08 to 2026-11-08**, year source **current-year**.
- Heading: **2026-11-08 - Sun - Eucharist**, ID **2026-11-08/eucharist**, for the bare-Sun files.
- Positions in your recorded listing: **1, 2, 3, 5, 6, 7, 8, 9, 10**. Position 10 follows 9. No fabricated missing-position-4 warning.
- Payloads such as `Darke-InE-Gloria`, `Ps070` and `NEH494-ChristIsTheWorld'sTrueLight-NunDanket` remain intact. No composer/title inference yet.
- No stray quote-pair lines, second music picker or forScore actions.

Run again and choose the same folder. Expected: identical dates/ID/order, year source **saved-context**. Confirm the context file contains the resolved date range and config/music are untouched. This checks actual read/write persistence; successful formatting alone is insufficient.

If the first run fails, stop at that boundary and report the first diagnostic or the adjacent generated actions. In particular: missing folder/config slot, Date extraction/count/roundtrip, context Dictionary-to-Text JSON, common read/save destination, or numeric If operands. Do not proceed to broader cases until this small path works.

## Following manual checks

Use disposable renamed copies of usable PDFs where required; do not move unrelated music. Each row describes an expected result, not an observed pass.

| Check | Expected |
| --- | --- |
| INov9-15 with Tue, Thu/Thur/Thurs, Fri, Sat, Sun/Sunam/Sunpm and Mon music | Dates lie within 9-15 November; Sunday groups stay separate; Monday skipped |
| HNov7(ATB), including Sat music and one Sun file | Saturday assigned 7 November; qualifier preserved; Sunday unresolved outside range |
| One service with positions 10, 2, 1 in provider order | Output 1, 2, 10 |
| Same canonical piece at positions 1 and 3 | Both occurrences preserved |
| Two or three different filenames with the same service/position | Every conflicting row unresolved; independent positions/services still preview |
| A nested subfolder containing recognised files | Its children are absent; no recursion |
| Unknown1-Piece.pdf, a non-PDF, and a usable PDF | Unknown/non-PDF unresolved; usable music still processed |
| Nov30-Dec6-2026 and Dec28-Jan3-2026 | Correct month/year transitions and Sunday dates |
| Nov30-6 / Nov9-16 / unsupported folder | Unresolved folder; no new context range saved or contents assigned |
| Empty folder / a service with no music | No service proposal or setlist created |

For a saved-year precedence check without editing JSON: copy [the prepared saved-context fixture](../../config/v3-week-context.test-saved.json) to a **separate** file named `V3-week-context.test-saved.json` in the same Shortcuts base folder, and use [the matching complete test config](../../config/v3-config.test-saved-context.json) via the main shortcut's fixed config File. Select disposable **ZNov8** with a Sat PDF: dates must remain **2025-11-08**, year source **saved-context**, despite current year 2026. **ZDec28-Jan3** must retain **2026-12-28 through 2027-01-03**. Restore the fixed config File to normal v3-config.json afterwards. Normal context is not overwritten by this test.

Record the actual consumed revisions, warnings, native settings/repairs, returned report and context persistence. Raw native return types, cancellation/provider errors, Date conversion and numeric sort are not claimed passed until reported from the iPad.
