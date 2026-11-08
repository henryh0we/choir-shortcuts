# Stage 2B: dated, grouped and ordered preview

8 November 2026. **Revision 1 crashes in the editor and at Compile Jelly Text by user report. Revision 2 splits the main workflow into smaller installed shortcuts; its compilation/import/runtime are unverified.** No local code/builds/automated tests were run to establish correctness. Stage 2A's filename-preview passes remain separate evidence.

## Reported loading crash, 8 November 2026

The user reports that loading Preview Services crashes Jellycuts before the source loads; Notes accepts the text, and pasting sections still crashes after some point. Follow-up confirms the editor loading phase crashes, and Receive and Compile Jelly ALSO crashes specifically at Compile Jelly Text. Editor bypass therefore failed. The offending source section, installed app version and crash log remain unknown. No successful compilation/import/runtime is established. Original main source was 18,738 bytes; date resolver 11,288 bytes; the working filename preview 7,234 bytes. No hard size threshold is established. The original main is preserved unchanged as [revision-1 crash evidence](fixtures/v3-preview-services-revision-1-crash.jelly); do not reinstall it.

Primary-source research: the [developer's App Store release history](https://apps.apple.com/gb/app/jellycuts/id1522625245) documents editor long-file stabilisation in 2.6.3 and an editing crash near comments/multiline strings fixed in 2026.6.4. [Official documentation](https://docs.jellycuts.com/) records March 2026 long-file highlighting/wrapping work. These establish a known class of editor problems, not the cause of this exact crash or a guarantee that an update fixes it.

Revision 2 separates context persistence, Text row preparation and ordering/rendering into independently installed components. The main retains native folder access and UI, flattening only filenames/extensions into a serializable file table. New boundaries carry Text JSON and return Dictionary/Text; no File/Folder objects cross shortcuts. This is a concrete workaround to test, not a confirmed repair or a proven size-limit diagnosis. No Bridge, local build, comment stripping or bulk native-stop repair is introduced.

## Revision 2: compile this small component first

Transfer [V3 - Render Service Preview](../../shortcuts/reusable/v3-render-service-preview.jelly) using Copyover and Compile Jelly Text. It is about 5.6 KB, has no dependencies/native setup/writes, and isolates the numeric selection/report logic. **Compile/install only; do not launch it expecting a full preview.** Its normal contract needs two supplied Text items.

If this still crashes, record that exact file/action rather than trying the large revision-1 source again. If it compiles, continue the install order below. Neither a smaller file nor successful compilation proves correct generation/runtime. The unchanged date resolver also remains separately unverified unless a device result is supplied.

## Delivery and installation

Keep the working **V3 - Preview Filenames** and **V3 - Parse Filename**. The parser remains revision 3/interface 2.0. Normal config and context files are unchanged by this split; do not reset existing saved context.

1. Copy the complete [updated config](../../config/v3-config.example.json) through Copyover into Files as **v3-config.json**. All JSON changes are prepared in the repo; no iPad JSON editing is required. The config stays version 3 and retains the tested filename/schedule rules, so the old filename preview can still use it.
2. Copy [empty context](../../config/v3-week-context.empty.json) into **iCloud Drive/Shortcuts/V3-week-context.json** for this first installation. It is a separate file from config. Do not overwrite a context file containing dates you want to keep. Subsequent runs update it automatically; do not reset it between normal runs.
3. Install **V3 - Render Service Preview** as the first compiler checkpoint above. It is revision 1/interface 1.0 and has no dependencies.
4. Transfer [v3-resolve-folder-dates.jelly](../../shortcuts/reusable/v3-resolve-folder-dates.jelly), compile on the iPad, and install as **V3 - Resolve Folder Dates** if not already installed. It is unchanged by the split. Complete **V3-DATES-CURRENT**: native Date set to Current Date; reconnect adjacent missing-value If and year Format Date, delete only placeholder Nothing. No year prompt or stop block.
5. Install [V3 - Load Folder Context](../../shortcuts/reusable/v3-load-folder-context.jelly), revision 1/interface 1.0. The **V3-SERVICES-CONTEXT-READ/SAVE** actions now live HERE. Both must use the same **iCloud Drive/Shortcuts** base folder and actual `contextPath` token. Read: no picker, no error if missing, single result. Save: no picker, overwrite enabled. Readback consumes Save File output. Inspect its Run Shortcut target **V3 - Resolve Folder Dates**, three Text items folder/config/context.
6. Install [V3 - Prepare Preview Rows](../../shortcuts/reusable/v3-prepare-preview-rows.jelly), revision 1/interface 1.0. Its Run Shortcut target is existing **V3 - Parse Filename**, with filename/config Text. It has no native slots/writes; duplicate/name/date behavior is preserved from revision 1.
7. Transfer [v3-preview-services.jelly](../../shortcuts/main/v3-preview-services.jelly), now **revision 2**, and install as **V3 - Preview Services**. Complete **V3-SERVICES-CONFIG** with fixed config File and **V3-SERVICES-FOLDER** with a single-folder picker. Reconnect every consumer named in adjacent comments before deleting only placeholders. The native Folder stays inside this main; Get Folder Contents remains nonrecursive.
8. Inspect main calls: **Load Folder Context** = folder/config Text; **Prepare Preview Rows** = config/date-result JSON/file-table JSON Text; **Render Service Preview** = rows JSON/heading Text. Get Text must serialize Dictionaries as JSON, not descriptions. These new JSON transport boundaries need integrated device confirmation.

There are three native placeholder replacements total across the two sources: Current Date, fixed config File and single-folder picker. Get/Save File and date formatting also require settings inspection. This does not claim those bindings generate correct settings automatically. If compilation or generation fails, record the first diagnostic/action and its source comment before repairing; no broad probe programme or legacy installation is required.

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
