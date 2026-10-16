# Nextcloud and forScore Service Shortcut Draft V2

Implementation decision updated 16 October 2026: proceed with [the build guide](jelly/docs/choir-service-build.md), all four Jelly sources, and [Comment-slot completion](jelly/docs/choir-service-assembly.md) for native actions. The user prefers generated standard actions and marked insertions rather than constructing entire helpers manually. That guide supersedes the component split and separate capability-testing prerequisites below. Remaining action differences will be resolved in the first complete service run. This document retains the broader design goals; the build guide states the narrower first-release behaviour and deferred automation explicitly.

Create an ordered service setlist from music selected in Nextcloud. Reuse the exact score already in forScore, preserving its annotations. Download missing scores, give them stable filenames, and apply composer and other information extracted from the filename before adding them to the setlist.

Revision: 2.2. Date: 15 October 2026. Status: Designed. The [user-supplied forScore action inventory](forscore%20shortcut%20actions.md) supports native score lookup, import, metadata and setlist actions. Known-name and missing-name lookup are now user-confirmed through Get score. Remaining action settings and contracts need inspection before completing executable source or construction blueprints. [V1](nextcloud-forscore-plan-v1.md) remains the baseline.

## Target and scope

- iPadOS 26.6, as reported by the user.
- Signed-in Nextcloud app/account.
- forScore **15.2.5**, as reported by the user.
- Jellycuts **2026.6.4**, as reported by the user; generation bindings still need verification.
- Nextcloud is visible under Locations in Apple Files.
- The forScore library is empty; start with the current single library. No legacy score migration is needed.
- Reuse the existing iCloud `Choir Music/Library` folders as the clean PDF archive.
- Build, import, and run on iPhone/iPad. No desktop build or signing requirement.
- Nextcloud is the source of released music; forScore owns scores, annotations, metadata, and service setlists.

V2 covers selecting music, retaining clean PDFs in iCloud, matching and importing forScore working copies, assigning metadata, creating services, and reconciling repeated runs. It does not change released Nextcloud files or automatically replace working scores with revised scans.

## Changes from V1

The primary forScore route uses `Get score named Name`, with known-name and missing-name cases confirmed by the user. Choose one verified import action, apply composer/tag metadata through the listed category actions, and create/populate services with native setlist actions. Whole-library retrieval is diagnostic or a fallback, not a replacement for matching.

These are proposed uses of user-reported action labels, not verified parameter signatures. In particular, `Rename score` does not establish whether the underlying PDF filename changes; `add metadata` does not establish whether it accepts Text or metadata objects. Native object handling remains within one manually built forScore helper until Jellycuts bindings are verified.

## Clean PDFs and the working library

Reuse the existing iCloud structure created by the user's folder-setup Shortcut:

```text
Choir Music/
    Library/
        AgnusDei/
        Anthems/
        Canticles/
        Gloria/
        Hymns/
        Introits/
        ... existing music-type folders
    _Workflow/    proposed records and identity mappings
    Backups/      proposed forScore archives
```

Select the existing Library folder once during setup and retain a supported folder reference; do not assume its parent path or recreate the hierarchy. The two proposed sibling folders should be created only during implementation if they do not exist. The existing folder-creation Shortcut remains a setup tool; invoking it as a dependency requires its exact name and input/output behaviour, so the workflow can initially use the folders it already created.

Keep one clean PDF per exact score identity under its confirmed music type, using its canonical filename. Clean means the PDF as supplied by Nextcloud, before any working annotations or metadata rewriting. Preserve any content already present in the released PDF; do not assume it is annotation-free or strip it automatically. Save a copy through the iCloud Files provider and verify it can be read before importing the working copy. That verifies a provider save, not completion of upload to every device.

Determine type from the parsed work/movement only when clear: an explicitly named Gloria or Agnus Dei can use those existing folders; a known NEH hymn can use Hymns. Broad classes such as Anthems, Canticles and Introits need review when the filename cannot establish them. Ask the user to choose an existing type once, then retain the approved mapping. Search the archive across type folders or through its verified index to avoid importing duplicates merely because classification changed. A classification correction moves the one clean copy after review.

Use the current single forScore library for the working scores. Mirror music types as genres where verified; use tags for hymn numbers, movements and variants. Services become setlists. Files folders and forScore libraries are independent structures, so do not create one forScore library per type.

For each piece, resolve both locations:

| Clean iCloud PDF | forScore score | Required operation |
| --- | --- | --- |
| Present and readable | Present | Reuse both; add the existing score to the service |
| Present and readable | Missing | Import a working copy from iCloud; no Nextcloud download |
| Missing | Present | Download from Nextcloud to complete the clean archive; reuse the forScore score without importing again |
| Missing | Missing | Download once, archive the clean PDF, then import a working copy |
| Unreadable or identity uncertain | Any | Resolve availability/identity before treating the item as absent |

This extends the original download-only-when-forScore-is-missing rule: completing the independent clean archive can also require a download. An unavailable iCloud placeholder is not proof of absence. Existing-file collisions and corrected releases need review; do not overwrite the clean original or replace an annotated working score automatically.

The proposed default is archive-first: if the clean file cannot be saved/read, stop that new import and retain a recoverable pending item. Keep clean-file path, type, source reference, available revision information and actual forScore identity in the record. Archive status and import/metadata status are separate, so a retry can finish either without repeating the other.

forScore already supports its own iCloud syncing for scores, annotations, metadata and setlists. That is separate from the readable clean-folder archive. If using both iPhone and iPad, enable and verify forScore syncing through its Sync panel after the first test import; do not infer it is currently enabled. [forScore sync documentation](https://forscore.co/documentation/sync/)

Clean PDFs do not retain forScore setlists or annotation data. Periodically create a full forScore 4SB archive and save a dated copy under the proposed Backups folder through the app's supported flow. Keep this manual initially; no backup Shortcut action is established by the supplied evidence. [Backup and archive documentation](https://forscore.co/kb/understanding-backups-syncing-and-icloud/)

## Service selection and preview

Launch the proposed `MAIN - Build Choir Service` Shortcut. Choose a Nextcloud folder and either a recognised service group or individual music files. The default starting location is `ScannedChoirMusic`; the user can browse weekly folders, `ExtraServices`, `NewMusic`, or other locations when needed.

Weekly prefixes such as `Fri`, `Sun`, `Sunam`, and `Sunpm` suggest groups. Keep plain `Sun` separate from `Sunam` and `Sunpm`. Do not equate these codes with a particular service type without confirmation. A weekly folder suffix such as `(ATB)` remains visible in the service context.

Ask for a service date and name. Display an editable setlist name such as `2026-10-18 — Evensong`. Interpret dates using Europe/London. Weekly folder names omit the year; a date suggestion must be confirmed. Multiple services on the same date need distinct names.

Sort numbered items by their numeric position, so position 2 precedes position 10. Gaps are valid: `GOct12-18` contains groups without every numbered item. Duplicate positions require review. For unnumbered files, require an explicit running order. Allow additions, removals, and reordering before proceeding.

Show the final preview with order, original filename, proposed title/composer, variant, and any parse warnings. Exclude logs, databases, `Desktop.ini`, the empty `.pdf` filename, and obvious administration documents from suggested music. Allow deliberate selection of booklets and running orders, but do not assign guessed composers to them.

Use the Nextcloud location in Apple Files as the initial selection route. Its availability is now user-confirmed. Prefer obtaining filenames and remote references before retrieving PDF contents. Verify whether choosing files or using Share Sheet downloads selected files immediately. If it does, that entry route cannot promise to download only missing scores. For the strict route, evaluate a metadata browser using authenticated WebDAV through a supported on-device mechanism. Nextcloud supports WebDAV; support for listing requests and response parsing in the chosen Shortcut implementation still needs verification. [Nextcloud access documentation](https://docs.nextcloud.com/server/latest/user_manual/en/files/access_webdav.html)

## Filename identity and metadata rules

Split each recognised service filename into day/session, numeric position, and payload. The payload plus `.pdf` is the proposed permanent filename. A file without a recognised service prefix goes directly to payload parsing.

For example, both `Fri1-Walsh-Responses.pdf` and `Tue1-Walsh-Responses.pdf` identify `Walsh-Responses.pdf`. The weekday, weekly folder, and service position belong to the service record, not the permanent score identity.

Preserve the complete payload, including movements, verse ranges, catalogue numbers, arrangement suffixes, and parenthesised qualifications. Do not merge files merely because they describe the same composition. Identical payloads are candidates for reuse, but a corrected scan or different edition can still require review.

| Filename example | Stable filename | Proposed interpretation |
| --- | --- | --- |
| `Fri1-Ireland-VesperHymn.pdf` | `Ireland-VesperHymn.pdf` | Composer Ireland; title Vesper Hymn |
| `Sunam4-Howells-CollegiumRegale-TeDeum.pdf` | `Howells-CollegiumRegale-TeDeum.pdf` | Composer Howells; work Collegium Regale; movement Te Deum |
| `Sun7-Palestrina-MissaBrevis-SanctusBenedictus.pdf` | `Palestrina-MissaBrevis-SanctusBenedictus.pdf` | Preserve this movement separately from Gloria and Agnus Dei |
| `Fri7-NEH205-ChristIsMadeTheSureFoundation-AP.pdf` | `NEH205-ChristIsMadeTheSureFoundation-AP.pdf` | Source NEH; number 205; title; variant AP |
| `Sun11-Ps150-Talbot.pdf` | `Ps150-Talbot.pdf` | Psalm 150; Talbot retained as attribution text pending an approved mapping |
| `Sat3-Ps89vv30-50(Plainsong).pdf` | `Ps89vv30-50(Plainsong).pdf` | Psalm 89, verses 30–50; Plainsong qualification |
| `Thur2-OH06.pdf` | `OH06.pdf` | Office hymn identifier 06; retain leading zero |
| `Sun5-60.Proper24.pdf` | `60.Proper24.pdf` | Sheet identifier 60; Proper identifier 24 |
| `Sun1-SiIniquitatesObservaverisDomine-HebdomXXVIII.pdf` | `SiIniquitatesObservaverisDomine-HebdomXXVIII.pdf` | Title and liturgical reference XXVIII; no inferred composer |
| `NewMusic/Jackson-InGminor.pdf` | `Jackson-InGminor.pdf` | Unprefixed piece; composer Jackson; title In G minor |

Recognise NEH, psalm, OH, Proper, and Hebdom patterns before the generic composer/title pattern. Treat `Hy`, `RSC`, and numbered RSC prefixes as special or uncertain patterns requiring review. Preserve the original text alongside any readable title. CamelCase spacing is a suggestion; verify cases such as `OGod`, `OLorde`, `TeDeum`, and `deSeverac`. Do not invent full composer names from surnames.

Proposed metadata fields are title, composer when identified, and suitable tags for source, number, movement, psalm reference, and variant. Keep service date/order in the setlist and service record. Preserve existing score metadata on reuse. Corrections approved during preview belong in one optional mapping table for future use.

The existing [filename parser blueprint](Parse%20Choir%20Music%20Filename%20V2%20-%20Shortcut%20Blueprint.txt) provides service-prefix parsing and identity rules. Its `Parse Choir Music Payload` dependency is absent from this workspace. Reuse its design and preserve its existing output keys if wrapping it; it is not an installed project dependency yet. Its documented workaround for unmatched optional regex groups should be retained and tested.

## Score matching and import policy

Use the complete canonical filename as the preferred identity. The match must include movement, extract, arrangement and edition qualifications. Store confirmed mappings to older score names instead of renaming existing annotated scores.

### Retrieve and resolve existing scores

1. Supply the complete canonical payload, without `.pdf`, to `Get score named Name`. The user confirms this finds the disposable score, while a nonmatching name finds none. Enable Continue if not found for the proposed branching flow and verify its exact absence output. Leave optional composer/genre/tag/label/reference filters unset initially.
2. Reuse the returned native Score when present; use the missing branch only after a completed lookup with no result. Never use the first score from the whole library as a substitute.
3. Test whether Name matches filename stem or display title when they differ. Resolve Rename score effects before automatically making titles readable. Preserve movement, variant and verse qualifiers; retain an approved mapping if a rename changes the lookup name.
4. Duplicate-name behaviour, case rules and scope still need testing. A singular result does not prove uniqueness. Resolve known ambiguities with verified category filters or user selection; do not assume the action reports every candidate.
5. Display the match decisions before writes. Keep the selected native score objects inside the forScore helper. Preserve existing metadata and annotations.

A failed or partial lookup is an unresolved result, never an instruction to import. Avoid relaxed matches between different movements, extracts or variants. Use title/composer suggestions only for explicit user selection.

### Download and import a missing score

Resolve the clean archive first. If the PDF exists there and is readable, use it. Otherwise request the selected remote PDF from the Nextcloud helper, confirm its type and identity, and save the clean copy under its reviewed type/canonical filename. Stage a separate working copy for import. The staging filename does not prove forScore retains it.

Both import cards in the screenshots display `Import Files`, with Conflict Handling: Skip. The screenshots do not establish which catalogue action each represents. Inspect `Import file(s)` and `Import score(s)` individually, then choose one that accepts the staged native File. Determine whether it returns an imported score, multiple scores, or no result, and inspect filename-collision behaviour. Never call both import actions for the same PDF as a routine sequence.

If the chosen action returns a score, verify its identity. Otherwise retrieve the library again and reconcile against the staged file. An ambiguous or unconfirmed import requires inspection before another attempt. `add scores to library` is a candidate for assigning an existing/imported score to the configured library, not an assumed PDF importer.

### Apply metadata to a new score

Use `Rename score` for the reviewed readable title only after establishing its title-versus-filename behaviour. If it also changes the filename, record the actual resulting identity and use that identity in future matches; do not assume the canonical filename remains available.

For a known composer, the screenshot shows `Get composer named Name` with Continue if not found switched off. Enable that setting for the proposed lookup-before-create flow and test its absence output. If its verified result is absent, use the shown `Create composer named Name and add to Scores and/or Bookmarks` after testing its score target. This may create and assign in one operation; do not add a redundant assignment step if the readback confirms it. Pass the resolved category to `add metadata` using the action's actual settings and target score. If the editor instead accepts composer Text directly, use that simpler verified path. Do not create a category after a failed or ambiguous search.

For music type, use the visible Genres option in `Add metadata to Score and Bookmarks`, with genre lookup/creation verified separately. For reviewed tags such as source, hymn number, movement, psalm range and variant, evaluate `Find tag`, `Create Tag` and `add metadata` with the same policy. Avoid assigning service date/order as permanent piece identity. Skip composer assignment when the filename cannot establish one.

Use `get composers`, `get tags` and `Check for metadata` to verify assignment once their outputs are known. Establish whether `Check for metadata` checks a particular value, any category, or something else. Read title through the verified score property; the inventory does not list a dedicated title getter.

Keep provenance in the local service record. The meaning and input type of `set reference` and `get reference` are unknown, so do not use them as arbitrary source-path storage.

Record an imported score with incomplete metadata as `metadataPending`. A retry should resolve that score and finish metadata, not import the PDF again.

### Integration fallbacks

Prefer the reported native lookup and metadata actions. If their actual contracts cannot meet the requirement, retain the V1 alternatives: a refreshed library index, an explicit user lookup, or a verified metadata-import method. URL opening is navigation, not an existence check. PDF metadata offers a documented mapping to forScore fields, but on-device writing and adoption require a supported mechanism. [forScore automation](https://forscore.co/developers-automation/), [PDF metadata](https://forscore.co/developers-pdf-metadata/)

## Setlist creation and repeated runs

Resolve the setlist independently of scores. Candidate `Get all setlists` provides a setlist collection; inspect name, library and identifier properties. Candidate `Get setlist` may retrieve a configured item or require selection. Prefer a stored verified setlist identity; otherwise match the confirmed service name within the intended scope. Several matches require user selection.

If no service exists, use `new setlist` after verifying its naming, library and output settings. If naming is a separate operation, evaluate `Rename setlist`. `Move Setlists to library` is only a candidate for setlist membership, not proof that it also assigns its scores to that library.

Populate the service with the shown `Add Scores to Setlist`. Its Skip if already added setting is off in the screenshot. Enable it for ordinary additions/retries after testing; handle intentional repeated pieces separately so duplicate protection does not remove them. Verify that a supplied list retains the approved order, or that adding one score per iteration appends reliably. If the action cannot preserve order, inspect `add entries to setlist` and its insertion settings. Do not assume `Sort Setlist Entries` supports arbitrary musical order; alphabetical sorting is unsuitable for the running order.

Read back using the shown `Get entries in Setlist` with Sorting: Manual. Where necessary, evaluate `get score from setlist entry` or `get scores from setlist entries` to compare actual score identities. Verify both entry count and sequence, including deliberate repetitions of the same score.

On repeated runs, compare planned and actual entries. An unchanged service needs no write. For an update, preview additions/removals/reordering before changing existing entries. Prefer verified targeted `remove setlist entries` operations plus ordered insertion. If only clearing/rebuilding meets the ordering requirement, require an explicit update choice after all replacement scores are ready; inspect and preserve the existing list, using `Duplicate Setlist` only if its actual copying behaviour is suitable. `Remove all setlist entries` is not a default retry step.

There is no assumed transaction or automatic rollback. If a write stops midway, re-read the service on the next run and reconcile actual contents. Do not create another setlist just because the first operation returned no receipt.

Unresolved items offer a stop or an explicitly approved partial service. If the user chooses placeholders, evaluate `add placeholder to setlist` and verify that placeholders remain distinguishable from resolved scores. Missing music is never silently omitted from a completion report.

The final report distinguishes reused, imported, metadata pending, unresolved, failed, and unconfirmed results; include whether setlist order was verified. Use `open setlist` for final navigation, not as proof the preceding writes succeeded.

If native setlist actions cannot satisfy the ordered service, the documented Open Setlist `.4ss` format remains a fallback using actual library filenames. Missing references can become placeholders. Do not assume the listed `convert text to 4ss` consumes this XML or matches that format. [Open Setlist documentation](https://forscore.co/developers-file-types/)

Keep a small record on-device with the service name/date, ordered source references, canonical identities, actual library references, verified operations and pending work. Save checkpoints after confirmed writes through a verified local storage mechanism. The record assists reconciliation; it cannot catch an action failure that terminates execution.

## Proposed components and contracts

These names identify proposed responsibilities, not existing actions or installed Shortcuts. Keep the forScore boundary together initially so native score objects need not cross several helper boundaries.

| Proposed Shortcut | Responsibility | Proposed input and output |
| --- | --- | --- |
| `MAIN - Build Choir Service` | Selection, preview, ordering, orchestration, summary | Interactive direct run; optionally a list of Files from a tested Share Sheet route. Produces one service report Dictionary |
| `UTIL - Parse Choir Music Filename` | Service-prefix and payload parsing | One filename Text; one metadata Dictionary; no UI or file changes |
| `UTIL - Read Nextcloud Music` | Account-specific browsing and retrieval | One request Dictionary with explicit `mode` of `browse` or `download`; browse returns ordered source descriptors, download returns one native File |
| `UTIL - Apply Choir Service in forScore` | Resolve scores and clean archive, import missing working copies, apply metadata, reconcile setlist | One service Dictionary; one outcome Dictionary, with native objects kept internal where practical |

The parser's new contract uses Text fields `originalFilename`, `payload`, `canonicalFilename`, `patternKind`, `day`, `session`, `titleRaw`, `title`, `composer`, `source`, `catalogueNumber`, `variant`, `psalmReference`, `properSheet`, `properNumber`, `liturgicalReference`, and `warning`. `position` is Number, using 0 when absent; absent Text fields are empty. `parseState` is Text: `recognised`, `needsReview`, or `invalid`. This is a proposed new interface; it does not silently replace the legacy parser's keys.

Source descriptors contain original filename, account-relative remote reference, and available revision information. They are not Files. The service Dictionary contains `serviceName` (Text), `serviceDate` (ISO date Text), and `items` (ordered List of parsed item Dictionaries with their source references). forScore outcomes use explicit Text states such as `reused`, `imported`, `metadataPending`, `unresolved`, `failed`, or `unconfirmed`. Final native value wiring and supported nested data types remain implementation checks; the action inventory alone does not resolve them.

The forScore helper calls the parser on supplied filenames where needed, checks the clean archive and forScore separately, then calls the Nextcloud helper only when a required clean PDF is absent. Keep archive processing inside this helper initially; extract a reusable archive helper only if that responsibility becomes useful to another workflow. The parser accepts Text, the Nextcloud download returns a native File, and forScore scores/setlists/entries remain inside the forScore helper. Do not serialize those objects into JSON or Text. Both helpers are dependencies of the main; neither calls the main. Missing input returns a validation result where supported; called helpers never launch selection prompts unless the request explicitly allows interaction. Direct execution of the forScore helper without a complete service is unsupported. Test download Files and Dictionary outputs across `Run Shortcut` before implementation relies on them.

Keep settings in one designated configuration section owned by the main: Nextcloud starting folder/account, existing iCloud Library folder reference, approved music-type mapping, current forScore library selection, setlist naming convention, and service-record/backup locations. Pass configuration into helpers. Authentication remains in the Nextcloud account or a verified private mechanism. If WebDAV is chosen, Nextcloud recommends an app password; keep it out of committed source and example records. [Nextcloud authentication guidance](https://docs.nextcloud.com/server/latest/user_manual/en/files/access_webdav.html)

## Capability checks and build sequence

### Capability checks before construction

The inventory establishes user-reported availability for every label below. It does not supply expanded settings, return types or execution evidence.

| Required behaviour | Reported action candidates | Specific implementation check |
| --- | --- | --- |
| Score lookup | `Get score named Name` | Known-name and missing-name cases user-confirmed; rename effects, duplicates, scope, case rules and exact absence representation remain open |
| PDF import | `Import file(s)`, `Import score(s)` | Native File acceptance, output type, filename collisions, actual imported identity |
| Library assignment | `add scores to library` | Existing-score input, target library selection, effect on other memberships |
| Display title | `Rename score` | Title versus PDF filename, retained object identity |
| Composer | `Find composer`, `Create composer`, `add metadata`, `get composers` | Text/category input, absent and duplicate category results, assignment versus replacement |
| Tags | `Find tag`, `Create Tag`, `add metadata`, `get tags`, `Check for metadata` | Category lookup, supported fields and readback |
| Setlist lookup/create | `Get all setlists`, `Get setlist`, `new setlist`, `Rename setlist` | Name/library scope, outputs, same-name setlists |
| Ordered population | `add scores to setlist`, `add entries to setlist`, `Get setlist entries` | Append/insertion behaviour, entry order and repeated scores |
| Service updates | `remove setlist entries`, `Remove all setlist entries`, `Sort Setlist Entries`, `Duplicate Setlist` | Targeted edits, ordering options, copying behaviour, failure effects |
| Navigation | `open setlist` | Accepted object type, foreground transition and caller continuation |

Inspect the first four groups and composer assignment before investing in the complete workflow. Record exact app versions, selected settings, exposed variables, and real outputs. Do not invent action identifiers or Jelly bindings from these labels.

### Build and installation order

Start with [TEST - forScore Import and Lookup](manual%20creation/shortcuts/main/test-forscore-import-and-lookup.md). It includes a disposable PDF, numbered native assembly, retry trial and property-inspection instructions. Status: Designed; device tests Not run. This diagnostic establishes import/retrieval before the production helpers are built.

1. Resolve the capability checks with editor inspection and small device trials, starting with a non-modifying lookup. Test one disposable import and composer/title assignment next.
2. Resolve Nextcloud metadata browsing and delayed download using the signed-in account. Retain the Files/Share Sheet option only with its actual download behaviour documented.
3. Build `UTIL - Parse Choir Music Filename`, adapting the legacy design and supplying payload parsing. Test its filename cases independently.
4. Build `UTIL - Read Nextcloud Music`; verify browse descriptors and native File download outputs.
5. Manually build `UTIL - Apply Choir Service in forScore` using verified action settings. It depends on the parser and Nextcloud helper; test native objects within the helper and Files across the download boundary.
6. Build `MAIN - Build Choir Service`, which depends on the parser, Nextcloud helper, and forScore helper. Compile/export generated components through Jellycuts, dependency first; preserve manually built helpers.
7. Run the complete acceptance suite and record the actual evidence before promoting status.

The component names and contracts remain proposed interface 1.0; no implemented interface has been replaced. Exact numbered action blueprints and executable Jelly source belong to the construction stage after parameter/type inspection. The action names now supplied resolve availability, not those construction details. Add implemented sources, specs and tests to their workspace inventories when created.

## Device acceptance tests

Use a disposable forScore library/setlist and a small Nextcloud test selection. For each test record app versions, date, specification revision, actual result, and any prompts. All results below are Not run. Use the resolved native action configuration in each fixture.

| Test | Input or launch | Required observation | Result |
| --- | --- | --- | --- |
| Existing score | Select `Fri1-Walsh-Responses.pdf` with annotated `Walsh-Responses.pdf` already present | With a clean archive copy also present, existing score used; annotations preserved; no second import; strict route makes no PDF download | Not run |
| Missing score | Select a valid PDF absent from the test library | One import with stable filename, reviewed title/composer, and correct setlist position | Not run |
| Mixed service | Select existing and missing Friday pieces | Approved order retained; summary agrees with actual library/setlist | Not run |
| Numeric order | Select `Sun2`, `Sun9`, `Sun10`, `Sun11` | Positions ordered 2, 9, 10, 11 | Not run |
| Group separation | Select a weekly folder containing `Sun`, `Sunam`, `Sunpm` | Only the confirmed group is included | Not run |
| Unprefixed music | Select `NewMusic/Jackson-InGminor.pdf` | Payload parsed directly; explicit service order requested | Not run |
| Variants | Provide psalm extracts, full psalms, separate movements, and AP variants | No automatic substitution between distinct identities | Not run |
| Ambiguous library | Provide two plausible existing matches | User resolves the match or item remains unresolved; no assumed import | Not run |
| Invalid selection | Empty input, `.pdf`, non-PDF, and uncertain RSC filename | Clear validation/review; no library modification before preview acceptance | Not run |
| Cancellation | Cancel selection, preview, or match resolution | Stop further writes; report already confirmed changes when execution allows | Not run |
| Failure and retry | Interrupt download/import or deny a permission, then rerun | No assumed success or absence; inspect uncertain state before another import | Not run |
| Repeat service | Run the same confirmed service twice | No duplicate score imports; setlist policy followed without unrequested duplicate setlist | Not run |
| Punctuation | Use apostrophes, ampersands, accented names, plus/hash/percent signs | Source access, filename lookup, and any XML/URL encoding preserve values | Not run |
| Helper boundary | Call each helper from a small caller and directly where supported | Native Files and structured values preserved; prompts match the declared mode | Not run |
| Lookup contract | Inspect native lookup with zero, one and two matching test scores | Distinguish complete absence from failure; expose exact identity and scope | Not run |
| Rename semantics | Import a disposable PDF, then use `Rename score` | Record separate title and disk filename before/after; retry resolves the same score | Not run |
| Metadata categories | Add a composer/tag already present, then a new test category | Correct assignment/readback; no category duplication; existing reused metadata untouched | Not run |
| Partial metadata | Interrupt after import and before metadata completion, then rerun | Resolve the imported score and finish metadata without another import | Not run |
| Entry order and repeats | Create a test service with score sequence A, B, A | Native readback preserves all three entries in that order or records a capability gap | Not run |
| Setlist update | Change an existing test service from A, B to B, C | Approved update produces exactly B, C; unrelated setlists remain intact | Not run |
| Same-name setlists | Provide two service candidates with the same name | Explicit resolution; no arbitrary update or third setlist | Not run |
| Clean PDF first | Select a new Nextcloud score | Clean PDF saved/read under the confirmed type before working-copy import; original bytes retained | Not run |
| Archive reuse | Clean PDF exists; forScore score absent | Import from iCloud with no new Nextcloud download | Not run |
| Archive gap | forScore score exists; clean PDF absent | Download/save clean source; do not import a second working score | Not run |
| Archive unavailable | Existing cloud file is a placeholder or cannot be read | Resolve provider availability; do not treat it as absent or overwrite it | Not run |
| Archive failure | Deny save access or interrupt the save | No new import under archive-first policy; retry can complete saving | Not run |
| Type correction | Same piece mapped to a different existing type | One reviewed clean copy; forScore identity preserved | Not run |
| Clean copy isolation | Annotate/rename the imported working score | Clean iCloud PDF remains as supplied by Nextcloud | Not run |

## References and revision policy

The file examples come from [the Nextcloud listing](nextcloud%20file%20structure.txt). Architecture follows [forScore integration guidance](forscore.md), [Jelly agent rules](jelly/AGENTS.md), and [manual helper rules](manual%20creation/AGENTS.md). Official documentation linked above was reviewed on 14 October 2026; no device execution has been recorded for this project.

V1 is preserved unchanged. Revision 2.1 incorporates the clean iCloud archive, single-library choice, reported versions and [screenshot evidence](forscore-action-evidence.md), as well as the action availability supplied in [forScore Shortcut Actions](forscore%20shortcut%20actions.md) and the revised [integration guidance](forscore.md). The transcription remains unchanged, including case and spelling. Next, inspect expanded settings and execute the small capability trials, then produce exact numbered native-helper blueprints and Jelly source against the actual compiler. Record any interface change, remaining assisted step, and device test outcome explicitly.
