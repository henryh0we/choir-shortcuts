# Nextcloud and forScore Service Shortcut Draft V1

Create an ordered service setlist from music selected in Nextcloud. Reuse the exact score already in forScore, preserving its annotations. Download missing scores, give them stable filenames, and apply composer and other information extracted from the filename before adding them to the setlist.

Revision: 1.0. Date: 14 October 2026. Status: Designed. This is the complete first design draft; executable Jelly source and manual action blueprints follow in V2 once the installed actions are known.

## Target and scope

- iPadOS 26.6, as reported by the user.
- Signed-in Nextcloud app/account.
- forScore reported as the latest installed version; record its exact version in V2.
- Jellycuts version and compiler bindings to be recorded in V2.
- Build, import, and run on iPhone/iPad. No desktop build or signing requirement.
- Nextcloud is the source of released music; forScore owns scores, annotations, metadata, and service setlists.

V1 covers selecting music, parsing filenames, matching library content, importing missing pieces, assigning metadata, creating the service, handling partial runs, and testing. It does not change Nextcloud files, automatically replace revised scores, or reorganize the existing forScore library.

## Service selection and preview

Launch the proposed `MAIN - Build Choir Service` Shortcut. Choose a Nextcloud folder and either a recognised service group or individual music files. The default starting location is `ScannedChoirMusic`; the user can browse weekly folders, `ExtraServices`, `NewMusic`, or other locations when needed.

Weekly prefixes such as `Fri`, `Sun`, `Sunam`, and `Sunpm` suggest groups. Keep plain `Sun` separate from `Sunam` and `Sunpm`. Do not equate these codes with a particular service type without confirmation. A weekly folder suffix such as `(ATB)` remains visible in the service context.

Ask for a service date and name. Display an editable setlist name such as `2026-10-18 — Evensong`. Interpret dates using Europe/London. Weekly folder names omit the year; a date suggestion must be confirmed. Multiple services on the same date need distinct names.

Sort numbered items by their numeric position, so position 2 precedes position 10. Gaps are valid: `GOct12-18` contains groups without every numbered item. Duplicate positions require review. For unnumbered files, require an explicit running order. Allow additions, removals, and reordering before proceeding.

Show the final preview with order, original filename, proposed title/composer, variant, and any parse warnings. Exclude logs, databases, `Desktop.ini`, the empty `.pdf` filename, and obvious administration documents from suggested music. Allow deliberate selection of booklets and running orders, but do not assign guessed composers to them.

Selection should obtain filenames and remote references before retrieving PDF contents. Verify whether the Nextcloud file provider or Share Sheet downloads selected files immediately. If it does, that entry route cannot promise to download only missing scores. For the strict route, evaluate a metadata browser using authenticated WebDAV through a supported on-device mechanism. Nextcloud supports WebDAV; support for listing requests and response parsing in the chosen Shortcut implementation still needs verification. [Nextcloud access documentation](https://docs.nextcloud.com/server/latest/user_manual/en/files/access_webdav.html)

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

Use these matching steps in order:

1. Look up the complete stable filename in the intended forScore library scope.
2. Consult an explicit mapping from that identity to an older library filename or verified score reference.
3. If necessary, offer plausible title/composer matches for the user to inspect and choose. Never substitute a different movement, extract, arrangement, or edition automatically.
4. Classify the piece as existing, missing, or unresolved. Multiple candidates remain unresolved until selected. A lookup failure is not proof that the score is missing.

For an existing piece, retain the actual library filename/reference and its annotations. Add that score to the service. Do not download and reimport it merely to adopt the new naming convention.

For a missing piece, retrieve the exact selected Nextcloud file, validate that it is a usable PDF, stage a renamed copy, apply the reviewed metadata, and import it. Confirm the resulting library reference before using it in the setlist. If metadata application fails after import, record the score as imported with metadata pending so a retry does not import it again.

Native lookup, import, metadata editing, and returned score types are V2 integration decisions. The documented forScore URL scheme opens content but supplies no existence-query result; missing content can fail silently. It cannot be used as the automatic matching test. [forScore automation](https://forscore.co/developers-automation/)

If native lookup is insufficient, evaluate a library metadata export/index with an explicit refresh step. An outdated index cannot establish that a score is absent; use a user check before importing uncertain items.

If native metadata actions are insufficient, evaluate PDF metadata or forScore library metadata import. forScore maps PDF Title to title, Author to composers, Subject to genres, and Keywords to tags. Writing those fields on-device and forScore adopting them require separate verification. Passing a normal Shortcut Dictionary to Share does not establish metadata transfer. [PDF metadata](https://forscore.co/developers-pdf-metadata/), [supported file types](https://forscore.co/developers-file-types/)

## Setlist creation and repeated runs

Create the service setlist only from resolved score references, in the approved order. For unresolved items, offer to stop or explicitly create a partial service; label any partial result clearly. Do not silently omit required music and report completion.

Prefer verified native setlist actions. A documented alternative is an Open Setlist `.4ss` XML file referencing the actual library filenames. forScore supports this format from version 12; unmatched entries with titles can become placeholders. Test special characters with proper XML escaping and inspect the imported setlist. Supplying embedded PDF data requires version 14.3 or later and can create adjusted filenames; avoid that route for automatic reuse. [Open Setlist format](https://forscore.co/developers-file-types/)

On a repeated run, resolve the existing service by its stored setlist reference where supported, otherwise by a confirmed name. Compare its contents with the planned order and offer an update. Do not assume creating/importing the same name replaces it. Test whether repeated occurrences of the same score can be preserved; do not remove deliberate repetitions.

Keep a small service record on-device containing the confirmed date/name, ordered source references, stable identities, resolved library references, and per-item outcomes. Record confirmed operations, not merely attempted actions. Recheck library state before retrying uncertain imports. Network or native-action failures may stop the Shortcut without returning a report; the record is a recovery aid, not an exception handler.

The final report counts reused scores, confirmed imports, metadata pending, unresolved items, and failures. Open the completed setlist only after its creation has been confirmed or explicitly checked by the user.

## Proposed components and contracts

These names identify proposed responsibilities, not existing actions or installed Shortcuts. Keep the forScore boundary together initially so native score objects need not cross several helper boundaries.

| Proposed Shortcut | Responsibility | Proposed input and output |
| --- | --- | --- |
| `MAIN - Build Choir Service` | Selection, preview, ordering, orchestration, summary | Interactive direct run; optionally a list of Files from a tested Share Sheet route. Produces one service report Dictionary |
| `UTIL - Parse Choir Music Filename` | Service-prefix and payload parsing | One filename Text; one metadata Dictionary; no UI or file changes |
| `UTIL - Read Nextcloud Music` | Account-specific browsing and retrieval | One request Dictionary with explicit `mode` of `browse` or `download`; browse returns ordered source descriptors, download returns one native File |
| `UTIL - Apply Choir Service in forScore` | Resolve scores, import missing PDFs, apply metadata, reconcile setlist | One service Dictionary; one outcome Dictionary, with native objects kept internal where practical |

The parser's new contract uses Text fields `originalFilename`, `payload`, `canonicalFilename`, `patternKind`, `day`, `session`, `titleRaw`, `title`, `composer`, `source`, `catalogueNumber`, `variant`, `psalmReference`, `properSheet`, `properNumber`, `liturgicalReference`, and `warning`. `position` is Number, using 0 when absent; absent Text fields are empty. `parseState` is Text: `recognised`, `needsReview`, or `invalid`. This is a proposed new interface; it does not silently replace the legacy parser's keys.

Source descriptors contain original filename, account-relative remote reference, and available revision information. They are not Files. The service Dictionary contains `serviceName` (Text), `serviceDate` (ISO date Text), and `items` (ordered List of parsed item Dictionaries with their source references). forScore outcomes use explicit Text states such as `reused`, `imported`, `metadataPending`, `unresolved`, `failed`, or `unconfirmed`. Final native value wiring and supported nested data types must be resolved in V2.

The forScore helper may call the Nextcloud helper to fetch a confirmed missing score. Both helpers are dependencies of the main; neither calls the main. Missing input returns a validation result where supported; called helpers never launch selection prompts unless the request explicitly allows interaction. Direct execution of the forScore helper without a complete service is unsupported. Test download Files and Dictionary outputs across `Run Shortcut` before implementation relies on them.

Keep settings in one designated configuration section owned by the main: Nextcloud starting folder, account selection, forScore library scope, setlist naming convention, and service-record location. Pass configuration into helpers. Authentication remains in the Nextcloud account or a verified private mechanism. If WebDAV is chosen, Nextcloud recommends an app password; keep it out of committed source and example records. [Nextcloud authentication guidance](https://docs.nextcloud.com/server/latest/user_manual/en/files/access_webdav.html)

## Build sequence and V2 decisions

1. Capture exact forScore action names, expanded settings, inputs, outputs, app version, and foreground behaviour. Record the Jellycuts version separately.
2. Prove one existing-score lookup with no modifications, then one disposable missing-score import and metadata assignment.
3. Resolve Nextcloud browsing and delayed download using the signed-in account. Test one folder and one PDF. Retain a Files/Share Sheet entry option only with its actual download behaviour documented.
4. Implement and test the payload/service parser against the reference listing.
5. Build Nextcloud and forScore helpers, then the main Shortcut. Add each implemented file to its workspace inventory, with contracts and dependencies linked.
6. Compile and import generated Shortcuts through Jellycuts on the device. Preserve manually built helpers. Test each helper before the complete service route.

V2 must settle library search scope, zero/multiple-match handling, import receipts, metadata fields, score identity across helper calls, setlist creation/update and ordering, cancellation, permissions, return-to-caller behaviour, and retry reconciliation. If an essential action is unavailable, record the exact assisted step rather than describing that step as automatic.

## Device acceptance tests

Use a disposable forScore library/setlist and a small Nextcloud test selection. For each test record app versions, date, specification revision, actual result, and any prompts. All results below are Not run.

| Test | Input or launch | Required observation | Result |
| --- | --- | --- | --- |
| Existing score | Select `Fri1-Walsh-Responses.pdf` with annotated `Walsh-Responses.pdf` already present | Existing score used; annotations preserved; no second import; strict route makes no PDF download | Not run |
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

## References and revision policy

The file examples come from [the Nextcloud listing](nextcloud%20file%20structure.txt). Architecture follows [forScore integration guidance](forscore.md), [Jelly agent rules](jelly/AGENTS.md), and [manual helper rules](manual%20creation/AGENTS.md). Official documentation linked above was reviewed on 14 October 2026; no device execution has been recorded for this project.

Keep V1 as the design baseline. When the user supplies the action information, create V2 with the resolved capability matrix, exact numbered helper blueprints, supported Jelly source, installation order, and updated tests. Record any changed interface or remaining assisted step explicitly.
