# Stage 2B: dated, grouped and ordered preview

8 November 2026. **Source reviewed only; no local code, compilation, builds or automated tests were run. No iPad result is recorded for these new sources.** Stage 2A's filename-preview passes remain separate evidence.

## Delivery and installation

Keep the working **V3 - Preview Filenames** and **V3 - Parse Filename**. The parser remains revision 3/interface 2.0. This increment adds two independent installed Shortcuts:

1. Copy the complete [updated config](../../config/v3-config.example.json) through Copyover into Files as **v3-config.json**. All JSON changes are prepared in the repo; no iPad JSON editing is required. The config stays version 3 and retains the tested filename/schedule rules, so the old filename preview can still use it.
2. Copy [empty context](../../config/v3-week-context.empty.json) into **iCloud Drive/Shortcuts/V3-week-context.json** for this first installation. It is a separate file from config. Do not overwrite a context file containing dates you want to keep. Subsequent runs update it automatically; do not reset it between normal runs.
3. Transfer [v3-resolve-folder-dates.jelly](../../shortcuts/reusable/v3-resolve-folder-dates.jelly), compile on the iPad, and install with exact name **V3 - Resolve Folder Dates**. Complete its one **V3-DATES-CURRENT** slot: native Date set to Current Date, reconnect the adjacent missing-value If and year Format Date to that output, delete only the placeholder Nothing. No date/year prompt or stop block is required.
4. Transfer [v3-preview-services.jelly](../../shortcuts/main/v3-preview-services.jelly), compile, and install as **V3 - Preview Services**. Complete **V3-SERVICES-CONFIG** with a fixed File pointing to the updated config. Complete **V3-SERVICES-FOLDER** with native Select File configured to select one Folder. Reconnect every consumer named in the adjacent source comments before deleting only those placeholders.
5. Inspect **V3-SERVICES-CONTEXT-READ** and **V3-SERVICES-CONTEXT-SAVE**. Both must use the same **iCloud Drive/Shortcuts** base folder and actual config `contextPath` token (`V3-week-context.json`). Read: no picker, no error if missing, single result. Save: no picker, overwrite enabled. Readback must consume the new Save File output. This location is a V3 development default, not the Nextcloud music folder or future service-records folder.
6. Inspect both Run Shortcut targets: **V3 - Resolve Folder Dates** takes three actual Text List items (folder name/config JSON/context JSON); **V3 - Parse Filename** takes two (filename/the same config JSON snapshot).

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
