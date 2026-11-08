# Stage 2B: dated, grouped and ordered preview

8 November 2026. **The user confirms all newly supplied split shortcuts load correctly.** This records successful loading; exact compile/import actions, native setup and integrated runtime have not yet been reported. No local code/builds/automated tests were run to establish correctness. Stage 2A filename-preview passes remain separate evidence.

## What to change now

Make the changes below in the **Apple Shortcuts editor after generation/import**. The `.jelly` files already contain the current code; no source replacement or JSON editing is needed for this setup guide.

There are **three Nothing placeholders to replace in total**, plus existing action settings/connections to inspect. The latter need changing only if the generated actions differ from the settings below. Keep every other Nothing/initializer. There are no Stop/Output blocks to insert.

| Installed shortcut | Required additions | Existing actions to inspect |
| --- | --- | --- |
| V3 - Resolve Folder Dates | One Date action, set to Current Date | Date formats and Add 1 day |
| V3 - Load Folder Context | None | Get File and Save File use the same context location; date-helper target |
| V3 - Prepare Preview Rows | None | Filename-parser target; configured date format |
| V3 - Render Service Preview | None | Numeric comparisons and final Text result |
| V3 - Preview Services | One fixed File action; one single-folder picker | Three helper targets; folder recursion off |

Keep exact installed names as shown. **V3 - Parse Filename** remains the existing revision 3/interface 2.0. Main Preview Services is revision 2/interface 1.0; the four other Stage 2B sources are revision 1/interface 1.0.

## 1. Put the two JSON files in place

- Use the complete [normal Stage 2B config](../../config/v3-config.example.json) through Copyover, saved as **v3-config.json** in your chosen config location. Use this normal config, not a conflicting-rule, wrong-version or saved-context test config.
- For the first installation only, save [the supplied initial context](../../config/v3-week-context.empty.json) as **iCloud Drive/Shortcuts/V3-week-context.json**. This is a different file from config. If that context file already contains saved dates, retain it; do not replace it with the empty version.

Normal config/context are unchanged by the shortcut split. If these files are already in place, keep them. The config's `contextPath` supplies the filename **V3-week-context.json**; select **iCloud Drive/Shortcuts** as the base folder in both context actions below. Do not select the music folder as the context destination.

## 2. V3 - Resolve Folder Dates

Find the Comment beginning **V3-DATES-CURRENT**. It is inside the branch used when there is no saved date range and no explicit folder year. Leave the replacement in that branch.

1. Add native **Date**, set to **Current Date**, immediately before the Nothing directly below that comment.
2. Change the following missing-value If to use the new **Date action's output**. Its condition must be **does not have any value**.
3. In the following current-year **Format Date**, replace the old Nothing token with that same Date output. Keep Custom format **yyyy**. It sits inside the following ready-state If; preserve that placement.
4. Delete only the replaced Nothing after reconnecting both consumers.

Inspect the other existing actions; add no further placeholders/actions:

| Format Date output in source | Input | Custom format |
| --- | --- | --- |
| currentYear | New Current Date output | yyyy |
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
