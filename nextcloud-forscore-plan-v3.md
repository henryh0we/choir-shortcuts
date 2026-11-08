# Choir shortcuts implementation plan — version 3

Date: 7 November 2026  
Status: Proposed architecture and implementation plan; ready for expansion.  
Previous plan: [version 2](nextcloud-forscore-plan-v2.md)

Development order: [staged implementation timeline and manual iPad checkpoints](nextcloud-forscore-v3-development-timeline.md). This is the working sequence for implementing this plan; runtime acceptance remains manual on the iPad.

Implementation direction, 7 November 2026: build from the ground up under **V3 - ...** installed names. Reuse recorded research, not legacy shortcut dependencies or interfaces. No legacy migration, adapter or backup prerequisite is required. [Current implementation and contracts](jelly/docs/v3-development.md) describe the independent v3 sources and separate configuration.

Naming evidence update, 8 November 2026: [Nextcloud listing findings and implementation implications](jelly/docs/v3-development.md#nextcloud-naming-evidence-and-implementation-implications-8-november-2026) cover single-date/range folders, qualifiers, noncontiguous numeric order, hymn/psalm references, collection scope and historical event folders. These are planning notes; source/config behavior is unchanged.

## Purpose and scope

Build two user-facing Apple Shortcuts for the initial release, with a third workflow reserved for a future addition:

1. **Weekly:** select a week folder, parse its PDFs into individual services and create or update their setlists.
2. **Specific service:** select a series of pieces, arrange them and create or update one service setlist.
3. **Mass import (future):** supply a spreadsheet export containing dates, services and pieces, then create or update multiple setlists. Consider compatibility now, but defer implementation and template decisions.

All workflows must use the same rules for piece identity, service identity, ordering, archiving, score reuse/import, metadata and setlist updates. Existing setlists use an additions-only policy: preserve all existing entries and their order, including manual edits. Repeating the same request must not create unintended duplicate scores, entries or setlists. Exact source order applies when first creating a setlist; later runs may intentionally retain a different order or extra entries.

### Confirmed user decisions

- Show one summary of the proposed work, then one confirmation starts processing without routine per-service prompts.
- Regular services: Tuesday, Thursday, Friday and Saturday Evensong; Sunday Eucharist and Evensong, with Mattins when present. Monday is excluded; Wednesday has no regular service in the supplied schedule.
- Derive special-service names from filename suffixes: `SunRemem` means Sunday service `Remem`.
- Always add; never remove existing entries or undo manual changes. Cleanup is manual.
- Setlist names follow `yyyy-MM-dd - EEE - Service`, for example `2026-11-08 - Sun - Eucharist`.
- Specific service is available from the Share Sheet for music shared from Nextcloud, Files or another provider that supplies usable files.
- Mass import is a future addition.
- Finish independent services and provide one final list of unresolved work.
- Insert newly requested pieces into the appropriate gap without moving or removing existing entries.
- Create/update a service with its available music even when a piece is missing, and flag the missing piece in the final report.
- Combine all Share Sheet selections into one service, even when their original prefixes refer to different services.
- Year accuracy is not important for these short-lived setlists. Use the current year by default without a year prompt; retain it for reruns of the same week.

Move into implementation rather than extending the current programme of isolated diagnostics. Resolve remaining generation and runtime problems as they arise during construction and integrated use. Build independent V3 shortcuts without replacing or depending on the old installed shortcuts.

This version establishes the overall structure. It does not claim that the proposed interfaces or all required actions are already implemented or device-verified. Earlier plans remain reference material; this document guides the proposed multi-entry-point structure. V3 defines its own contracts without inheriting legacy interfaces.

## Editable formatting and weekly schedule

Formatting and scheduling rules must be easy to find and change without editing the processing loops. Each user-facing shortcut starts, after its identifying comment, with a clearly labelled **SETTINGS / FORMATTING** section. This section exposes the shared configuration location and explains which settings control PDF prefixes, week-folder dates, service mappings, exclusions and setlist names. It must not maintain a separate copy of those rules in each shortcut.

Keep the actual editable rules together near the top of the shared V3 configuration, in this order:

1. **Filename formats:** supported prefix patterns, day aliases, session aliases, numeric position and where the piece-name payload begins.
2. **Week-folder dates:** supported folder-name formats, year source and date interpretation.
3. **Weekly schedule:** enabled days, service slots, their names and source-prefix mappings.
4. **Setlist naming:** date format and name template.
5. **Exceptions and run behaviour:** dated overrides, previews and update policy.

These are proposed configuration groups, not a claim that the existing config schema already supports them. Use a separately versioned V3 schema when implementing them.

### Filename formatting rules

Use one shared, ordered set of parsing rules for both service grouping and removal of the service prefix from canonical PDF names. A rule describes day, session, numeric position and remaining piece-name payload. Avoid maintaining unrelated expressions that can disagree about where the prefix ends.

Proposed mappings for the current examples:

| Source example | Day | Service slot | Position | Piece payload |
| --- | --- | --- | ---: | --- |
| `Tue1-Walsh-Responses.pdf` | Tuesday | `evensong` | 1 | `Walsh-Responses` |
| `Sun1-Walsh-Responses.pdf` | Sunday | `eucharist` | 1 | `Walsh-Responses` |
| `Sunam1-Walsh-Responses.pdf` | Sunday | `mattins` | 1 | `Walsh-Responses` |
| `Sunpm1-Walsh-Responses.pdf` | Sunday | `evensong` | 1 | `Walsh-Responses` |

The Sunday mappings above are proposed from the existing folder examples and must be confirmed with the initial structure approval. Match explicit session prefixes before a bare day prefix; `Sunam` must not be consumed as `Sun`. Day aliases such as `Thu`, `Thur` and `Thurs`, separators and case handling belong in these editable rules.

Allow additional format rules so old and new filename conventions can coexist during a transition. Unknown or conflicting matches are reported for review; they must not silently assign music to a guessed service. Changes to prefix spelling or separators should require a configuration edit, without changing the main workflow. A fundamentally different naming scheme may still require a parser change.

For a valid day prefix followed by an unrecognised service suffix, use that suffix as the service name. For example, `SunRemem1-Piece.pdf` parses as Sunday, special service `Remem`, position 1 and payload `Piece`. Explicit mappings such as `Sunam` and `Sunpm` take precedence over this fallback. A special suffix does not require a new schedule entry before use on an enabled day. Preserve the readable suffix for naming and derive a consistent slot key for reruns. An invalid day or an ambiguous boundary between suffix, position and payload remains unresolved. Confirm the exact position/separator convention for special services before implementation.

### Weekly schedule and exclusions

Represent each weekday with an `enabled` switch and a list of service slots. Each slot has a stable key, display name, its own `enabled` switch and source-prefix mapping. The default schedule is:

| Day | Enabled | Service slots | Notes |
| --- | --- | --- | --- |
| Monday | No | Evensong | Excluded for this user's workflow: Monday evening is sopranos only |
| Tuesday | Yes | Evensong | Regular service |
| Wednesday | No by default | None configured | No regular service in the supplied schedule; editable |
| Thursday | Yes | Evensong | Regular service |
| Friday | Yes | Evensong | Regular service |
| Saturday | Yes | Evensong | Regular service |
| Sunday | Yes | Eucharist, Evensong; Mattins when present | Do not expect Mattins or create an empty Mattins setlist every week |

Disabling a day skips all its slots. Disabling a slot skips only that service, allowing Sunday Eucharist to run while Sunday Mattins is excluded. Report excluded files and services as skipped by configuration, rather than as missing music. Exclusion does not delete or clear previously created setlists.

Support date-specific overrides for cancellations, extra services and a different service name. Overrides take precedence over the recurring schedule; they should not require changing the usual week. Applying a disabled slot through Specific service or Mass import requires an explicit exception, so an alternative entry point cannot silently bypass the exclusion.

### Automatic names and routine operation

Routine runs infer service type and name automatically. Use `{date} - {dayShort} - {serviceName}`, with date format `yyyy-MM-dd` and English weekday abbreviations. Examples: `2026-11-08 - Sun - Eucharist`, `2026-11-10 - Tue - Evensong` and `2026-11-08 - Sun - Remem`. Users do not re-enter these names for every week.

Use date plus stable service-slot key for ordinary identity, for example `2026-11-08/evensong`. Changing the display template or source-prefix spelling must preserve that identity. Keep it independent of the enabled switch. Multiple exceptional services require distinct slot keys.

The normal Weekly run should require selecting the folder and then process recognised, enabled services using the approved rules. Use saved week context or an explicit year when available; otherwise use the current year automatically. Year accuracy is not a blocker because the user cleans up setlists after use. Remember the resulting week dates so reruns across New Year still target the same service. Month/day boundaries must still be parsed consistently; a December-to-January week crosses into the next year. Show the assumed dates in the summary without requesting a separate year confirmation. Current-year defaulting is an implementation choice reflecting the user's preference, not a requirement to establish historical dates or infer years from weekday agreement.

Show one summary before processing: inferred dates and setlist names, new versus existing targets, proposed insertions, exclusions and known unresolved items. One confirmation starts the whole run. Routine recognised services need no per-service naming, ordering or confirmation prompts. Apply only additions to existing setlists; preserve existing entries and their relative order. Queue unresolved cases for the final report instead of interrupting the batch with questions. Ask before confirmation only for essential context that cannot be defaulted; a missing year does not require a prompt.

Infer known metadata and reuse saved decisions. If a piece cannot be prepared because its file, archive category or another required detail is missing, continue with the remaining pieces and record the unresolved occurrence and intended position. An optional service such as Mattins with no matching music is simply absent; do not create an empty setlist. An expected regular service with no music may be noted in the report. If no usable pieces remain for an identified service, report it as pending rather than creating an empty setlist.

## Shared architecture

```text
Weekly folder --------+
                      |
Specific service -----+--> Service plan --> Shared assembly --> forScore setlist
                      |
Spreadsheet import ---+  (future)
```

Each entry point decides what belongs in a service and produces the same logical service plan. Shared assembly owns the execution of that plan.

| Component | Responsibility |
| --- | --- |
| Weekly entry point | Read the selected folder, identify services, order their pieces and submit approved services |
| Specific-service entry point | Receive shared music files, infer service details and order where possible, summarise and submit one service |
| Mass-import entry point (future) | Translate spreadsheet rows into the same service plans; outside the initial release |
| Shared assembly helper | Validate one service, prepare its music, resolve its target setlist, reconcile entries and return a report |
| Canonical naming utility | Apply consistent canonical piece naming across all entry points |
| Archive utility | Save or reuse canonical PDFs using shared archive rules |

Create new V3 naming/parsing, archive and assembly components, informed by the recorded research. Initially keep score preparation and setlist updating together inside assembly so native forScore objects do not need to cross several helper boundaries. Extract further helpers only where there is a concrete reuse benefit.

All new installed names begin V3 - . Exact implemented and planned names are documented in the [V3 contracts](jelly/docs/v3-development.md). No legacy caller contract needs to be maintained.

## Common service-plan contract

All entry points produce the following logical structure:

| Field | Purpose |
| --- | --- |
| `schemaVersion` | Version of the service-plan contract |
| `serviceId` | Stable service identity across reruns and entry points |
| `serviceDate` | Explicit ISO date, including year |
| `serviceSlot` | Stable configured slot key used for identity and schedule lookup |
| `serviceType` | Eucharist, Evensong or another configured service type, normally inferred |
| `serviceName` | Display name for the setlist |
| `sourceReference` | Originating folder or import reference |
| `items` | Ordered list of piece occurrences |

Each item needs a piece reference, an explicit position and any supplied metadata. Piece resolution must preserve edition, movement, variant and other identity-bearing qualifiers.

This is a logical contract, not a requirement to serialize everything into JSON. Choose concrete native Dictionary/List transport while expanding the implementation design. Keep native PDF Files native where needed, and retain native Score and Setlist objects inside assembly where practical. Do not assume unverified nested-value transport works.

### Identity and ordering

- Service identity is separate from its display name. Renaming a setlist must not accidentally create another service.
- Date plus an explicit service identifier is the proposed basis for ordinary service identity. Multiple services of the same type on one date require a distinguishing value.
- The same service must resolve to the same identity whether supplied by Weekly, Specific service or Mass import.
- A piece and its occurrences are separate: A/B/A means three setlist entries using two scores.
- Ordering is explicit. Neither file-picker order nor alphabetical filename order is a reliable musical running order.

## Common execution and update behaviour

Shared assembly processes one complete service:

1. Validate the service plan.
2. Resolve the required music, archive PDFs where needed and prepare the ordered scores.
3. Resolve the existing target setlist, or create it when appropriate.
4. Compare actual entries with requested piece occurrences and determine which additions are missing.
5. After the run's single summary confirmation, leave an unchanged service alone or insert missing available occurrences into their intended gaps. For a new setlist, add the available requested sequence in source order and flag unresolved occurrences.
6. Read back the entries, verify preservation of existing entries and the planned additions, and report the result.

Updates are strictly additions-only. Never clear a setlist, remove entries, replace an existing score occurrence or reorder existing entries. If source music disappears or its positions change, retain the actual setlist contents. If a source piece changes identity, add the newly requested piece while retaining the old one. Manual cleanup is outside the shortcut.

Match piece identities and occurrences, rather than testing simple membership. For requested A/B/A and existing A/B, add one A. For an unchanged rerun, add nothing. If the actual list already contains extra occurrences, preserve them. Insert a newly requested piece between its matched source neighbours: existing A/C plus requested A/B/C becomes A/B/C. Insertions may change numeric entry indexes but must preserve the relative order of every pre-existing entry, including manual additions.

Keep occurrence mappings in the service record where possible so repeated pieces and later resolution of missing music target the correct gaps. Use actual setlist readback to verify that existing entries survived and new entries were inserted as planned. Conflicting anchors caused by manual reordering, or ambiguous repeated identities, must be reported without moving existing entries; unaffected insertions and other services may continue. Define a deterministic policy for these conflicts during implementation. If native actions cannot insert into the intended gap, report that limitation rather than clear/rebuild the setlist or silently substitute appending.

Unresolved music produces a partial service containing the available pieces. Flag each missing occurrence with its service, source reference and intended position in the final report; do not silently omit it or assume a native placeholder feature is available. A later rerun inserts a resolved piece into its intended gap. Only a service-level blocker, such as an ambiguous target or no usable music, leaves the whole service pending. Finish other independent services and report unresolved references, conflicting targets and required decisions afterwards. Do not prompt for each problem during processing. Initial preflight should catch recoverable validation issues before native writes. Some native action errors can terminate a Shortcut without a recoverable result; continuing after such errors requires supported error handling and must not be claimed without device evidence. Save progress between services so an interrupted run can resume without duplicate additions.

### Service records and recovery

Introduce a small persistent service record linking `serviceId` to the target setlist and the last confirmed plan. This is a proposed addition: the current architecture does not yet maintain such a manifest.

The record assists identity resolution and recovery; it is not proof of current forScore contents. After an interrupted update, read the actual setlist before deciding what remains to do. There is no assumed transaction or automatic rollback.

Prefer a verified persistent setlist identifier if one is available. Define a fallback lookup policy, including duplicate matches and renamed setlists, during implementation planning.

Reports should distinguish unchanged, created, updated, partial, pending, failed and unconfirmed services, and state whether actual entry identities and order were verified. A partial result must identify each missing piece and intended position. Preserve useful per-piece outcomes such as reused, imported and metadata pending.

## Weekly workflow

1. Select the week folder.
2. Infer its dates using saved context or folder information, defaulting a missing year to the current year without prompting.
3. Read the relevant PDFs.
4. Parse filename prefixes into day, service/session and numeric position.
5. Apply the weekly schedule and dated overrides, skip disabled services, and derive names and identities automatically.
6. Group and numerically order recognised music. Show one summary, including planned additions, exclusions and known issues, and request one confirmation.
7. Process enabled services with available music, inserting additions into gaps and preserving existing entries, then return one final report and list of missing pieces or other items to resolve.

Existing folder examples distinguish prefixes such as `Sun`, `Sunam` and `Sunpm`. Store their meanings in shared configuration. Sort positions numerically so item 10 follows item 9. Preserve gaps without inferring missing music solely from absent numbers. The updated listing includes single-date folders such as HNov8 and HNov7(ATB), plus ranges such as INov9-15; folder letters and voice qualifiers do not themselves define a service identity. Keep discovery within the selected supported folder rather than recursively collecting unrelated collections.

Year defaulting follows the routine-operation policy above. Retain the first resolved week context for reruns and handle month/year boundaries consistently. Historical year accuracy is not a requirement.

On rerun, the current folder supplies requested music for each represented service. New occurrences become additions. Removed files and changed positions do not remove or reorder existing entries. The source is a basis for additions, not authority to overwrite manual edits.

If a previously processed service disappears entirely from the folder, flag it for review rather than automatically deleting its setlist. Unrecognised filenames and unrelated PDFs need explicit treatment in the preview.

## Specific-service workflow

Implement this entry point first because it establishes the shared execution path with the least input parsing:

1. Select music in Nextcloud, Files or another app and choose Share > Create Service. Receive the shared native files without making the user select them again. Direct launch may offer a file picker as a fallback.
2. Combine every selected piece into one service, regardless of its original day/service prefix. Use prefixes as ordering hints where useful, never as instructions to split this selection. Mixed prefixes or duplicate position numbers need a deterministic ordering fallback visible and adjustable in the summary. Do not assume an app preserves share order.
3. Infer the date and service slot from available input and saved context, then derive the name automatically. A shared file may lack its parent folder/date context: ask for genuinely missing date or service details before confirmation, without guessing or repeatedly requesting known values.
4. Show one summary and confirmation, with optional adjustments for a one-off service.
5. Call shared assembly, preserve existing setlist entries and return the final result with unresolved items.

Target the Share Sheet title **V3 - Create Service**; exact installed naming and supported input types must be recorded during implementation. File-provider support depends on receiving usable file objects; arbitrary URLs are not assumed to be PDFs. Unsupported inputs appear in the resolution report. A mixed selection always creates one combined service; where its target date or service cannot be inferred uniquely, collect those details once before the summary confirmation. Weekly remains the entry point that automatically splits music into services.

The workflow should also allow targeting an existing service, using the same identity and update rules as Weekly. Define how a user selects an existing service and how its saved details populate the form.

## Mass-import workflow (future addition)

This section preserves an architectural direction only. Do not implement mass import or finalise its CSV template in the initial release. When added, it must use the same one-summary confirmation, naming, exclusions, additions-only updates and final resolution report.

Start with a spreadsheet exported as CSV, with one row per piece occurrence. Direct workbook support can be considered later if needed.

Proposed initial template (explicit names and IDs remain supported as overrides; ordinary rows can instead supply date and service slot, from which both are derived):

| serviceId | date | serviceType | serviceName | position | pieceReference |
| --- | --- | --- | --- | ---: | --- |
| 2026-11-08-eucharist | 2026-11-08 | Eucharist | Sunday Eucharist | 1 | Walsh-Responses.pdf |
| 2026-11-08-eucharist | 2026-11-08 | Eucharist | Sunday Eucharist | 2 | Ps023.pdf |

Use canonical filenames or explicit source references initially. Free-text titles alone can be ambiguous. Define the reference search locations and how missing or multiple matches are resolved.

Validate the whole import before applying changes, infer ordinary service names and identities using the same schedule as Weekly, and show one batch summary and confirmation. Validation must cover required columns, dates, service grouping, conflicting details for one service, exclusions, positions and piece references. Report issues by service and row. Process valid services without further routine prompts.

A service containing unresolved music is created or updated with its available pieces and reported as partial; other services also proceed. Rerunning the same file inserts newly available occurrences into the intended gaps. Removing a row or an entire service never removes existing setlist contents.

CSV parsing must support quoted fields, including embedded commas. Splitting every line on commas is insufficient. The template and parser must agree on encoding, delimiter and supported field contents.

## Shared configuration

Keep common settings in one separate v3-config.json and use one immutable configuration snapshot per run. Neither entry point maintains a second copy, and no legacy config is required.

Configuration should cover source/archive locations, filename-prefix parsing, service-prefix mappings, the weekly schedule and exclusions, dated overrides, setlist naming, piece-resolution policy, update policy and service-record storage. Put frequently changed formatting and schedule settings first, as specified above. Keep credentials out of committed source and example records.

Retain the existing metadata direction: archive music category becomes Genre for first-time imports; service type does not become permanent piece Tags or Labels. Existing archive and score reuse policies should be shared by all entry points.

## Source delivery

Maintain `.jelly` only for Shortcut source and use Copyover for transfer. Do not create `.txt` duplicates. Keep historical unique fixtures as `.jelly` variants, and preserve existing immutable build evidence.

## Implementation sequence

1. **Expand the contracts and policies.** Finalise service identity, item references, native transport, filename grouping, ordering, update review and reports.
2. **Build shared assembly.** Build a new supplied-service-plan assembly under the V3 namespace, with no legacy caller or helper dependency.
3. **Complete Specific service.** Establish selection, ordering, preview, execution and updates end to end.
4. **Add Weekly.** Implement folder reading, date resolution, parsing and grouping around the same assembly path.
5. **Run integrated acceptance cases.** Exercise Share Sheet input, reruns, additions-only updates, preservation of manual edits, repetitions, special prefixes, unresolved music and interrupted execution, fixing issues encountered in the completed workflows.
6. **Future: Mass import.** Revisit spreadsheet input after the first two entry points are established. The shared plan contract should accommodate it without requiring implementation now.

Do not require another broad round of isolated probes before proceeding. Use focused diagnostics when an actual implementation problem needs them. Keep local compilation, generated structure, device import, repaired execution and untouched-source execution evidence separate.

## Acceptance criteria

- The same service plan creates the same initial ordered setlist from either entry point; subsequent runs preserve existing entries and manual edits.
- An unchanged rerun creates no unintended duplicate scores or setlists.
- Updates add missing occurrences and never remove, clear or reorder existing entries. Source removals and manual edits survive reruns.
- Existing A/C plus requested A/B/C becomes A/B/C by inserting B, without moving the existing entries. A piece resolved on a later run fills its intended gap.
- A/B/A preserves all three occurrences in the correct order while reusing scores.
- Two distinct services on the same date remain distinct.
- Weekly numeric ordering handles positions such as 2 and 10 correctly.
- Prefix formats, aliases and separators can be changed in shared configuration without editing processing loops; supported old and new formats can coexist.
- After initial structure approval, recognised weekly services receive their names, identities and order automatically, without per-service prompts.
- Monday is disabled by default for this workflow; disabled days and individual slots are skipped and reported without deleting existing setlists.
- Date-specific overrides affect only their specified dates, and all entry points honour exclusions unless explicitly overridden.
- Display-name or prefix-format changes preserve the identity of existing managed services.
- One summary and confirmation starts the run; processing has no routine per-service prompts, and unresolved cases are listed at the end while independent services finish.
- Special prefixes such as `SunRemem` automatically produce names such as `2026-11-08 - Sun - Remem`.
- Regular names use `yyyy-MM-dd - EEE - Service`, and optional Mattins is created only when music is present.
- Share Sheet invocation receives selected music without asking the user to select the same files again.
- Share Sheet selections with different service prefixes are combined into one service.
- Missing pieces produce partial services and explicit final warnings; available music and other services are still processed.
- A missing year defaults automatically without an extra prompt, and a saved week retains its identity across reruns.
- Ambiguous or missing music is reported and never silently omitted.
- Future mass import will report invalid rows by service and row while processing valid independent services; it is not an initial-release acceptance requirement.
- An interrupted run can resume by reconciling actual setlist contents.
- V3 has its own installed namespace, configuration and contracts, with no legacy shortcut dependencies.

## Decisions to expand next

1. Exact service identity format and rules for sharing identities across entry points.
2. Service-plan item fields, supported piece-reference forms and native input/output contracts.
3. Confirm Sunday prefix mappings, special-service position/separator syntax and folder month/day rules. The regular weekly schedule and missing-year default are recorded above.
4. Ordering interface, including repeated pieces and conflicting positions.
5. Service-record format, storage, setlist lookup and recovery checkpoints.
6. Define occurrence matching and insertion-anchor conflict behaviour while preserving existing entries and their relative order. Gap insertion and partial services are confirmed requirements.
7. Share Sheet fallback date/service selection and deterministic ordering for unprefixed or mixed-prefix music. Combining the selection into one service is confirmed. CSV template and parser decisions remain deferred.
8. Exact V3 installed shortcut names, dependency order and installation instructions.
