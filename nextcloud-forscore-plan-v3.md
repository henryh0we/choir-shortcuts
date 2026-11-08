# Choir shortcuts implementation plan — version 3

Date: 7 November 2026  
Status: Proposed architecture and implementation plan; ready for expansion.  
Previous plan: [version 2](nextcloud-forscore-plan-v2.md)

Development order: [staged implementation timeline and manual iPad checkpoints](nextcloud-forscore-v3-development-timeline.md). This is the working sequence for implementing this plan; runtime acceptance remains manual on the iPad.

Implementation direction, 7 November 2026: build from the ground up under **V3 - ...** installed names. Reuse recorded research, not legacy shortcut dependencies or interfaces. No legacy migration, adapter or backup prerequisite is required. [Current implementation and contracts](jelly/docs/v3-development.md) describe the independent v3 sources and separate configuration.

Naming evidence update, 8 November 2026: [Nextcloud listing findings and implementation implications](jelly/docs/v3-development.md#nextcloud-naming-evidence-and-implementation-implications-8-november-2026) cover single-date/range folders, qualifiers, noncontiguous numeric order, hymn/psalm references, collection scope and historical event folders. These are planning notes; source/config behavior is unchanged.

Worked examples: [service creation, reordering, Add, Overwrite and rerun walkthroughs](jelly/docs/v3-workflow-walkthroughs.md). These illustrate the intended design rather than completed features or test results.

## Purpose and scope

Build two user-facing Apple Shortcuts for the initial release, with a third workflow reserved for a future addition:

1. **Weekly:** select a week folder, parse its PDFs into individual services and create or update their setlists.
2. **Specific service:** select a series of pieces, arrange them and create or update one service setlist.
3. **Mass import (future):** supply a spreadsheet export containing dates, services and pieces, then create or update multiple setlists. Consider compatibility now, but defer implementation and template decisions.

All workflows must use the same rules for piece identity, service identity, ordering, archiving, score reuse/import, metadata and setlist updates. Existing setlists default to Add to existing: preserve all existing entries and their order, including manual edits. An explicitly selected Overwrite contents mode may replace only that target setlist's entries with the approved proposal; it never deletes library scores or annotations. Repeating the same request must not create unintended duplicate scores, entries or setlists. Exact source order applies when first creating a setlist; later runs may intentionally retain a different order or extra entries.

### Confirmed user decisions

- Show one summary of the proposed work, then one confirmation starts processing without routine per-service prompts.
- Regular services: Tuesday, Thursday, Friday and Saturday Evensong; Sunday Eucharist and Evensong, with Mattins when present. Monday is excluded; Wednesday has no regular service in the supplied schedule.
- Derive special-service names from filename suffixes: `SunRemem` means Sunday service `Remem`.
- Add to existing is the default and preserves manual entries/order. The later target-review decision explicitly permits Overwrite contents for a chosen existing setlist; replacement must be selected for that run and shown in the final confirmation. It does not delete library scores or annotations.
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

Use date plus stable service-slot key for ordinary identity, for example `2026-11-08/evensong`. Changing the display template or source-prefix spelling must preserve that identity. Keep it independent of the enabled switch. At most one service of a given name occurs on a date; do not add a same-name service instance/disambiguation workflow.

The normal Weekly run should require selecting the folder and then process recognised, enabled services using the approved rules. Use saved week context or an explicit year when available; otherwise use the current year automatically. Year accuracy is not a blocker because the user cleans up setlists after use. Remember the resulting week dates so reruns across New Year still target the same service. Month/day boundaries must still be parsed consistently; a December-to-January week crosses into the next year. Show the assumed dates in the summary without requesting a separate year confirmation. Current-year defaulting is an implementation choice reflecting the user's preference, not a requirement to establish historical dates or infer years from weekday agreement.

Show one summary before processing: inferred dates and setlist names, new versus existing targets, proposed insertions, exclusions and known unresolved items. One confirmation starts the whole run. Routine recognised services need no per-service naming, ordering or confirmation prompts. Default to Add to existing and preserve existing entries and their relative order. Replacement requires an explicit per-service choice in preflight and must be included in the batch confirmation; it is never silently applied to the week. Queue unresolved cases for the final report instead of interrupting the batch with questions. Ask before confirmation only for essential context that cannot be defaulted; a missing year does not require a prompt.

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
| `items` | Ordered list of requested piece occurrences, including the final user-approved order |
| `updateMode` | Explicit create/add/overwrite mode for this target; Add is the existing-target default |
| `serviceNameOverride` | Optional edited display name; does not by itself change service identity |
| `targetReference` | Resolved target association and lookup context, or explicit new-target intent |
| `reviewedEntries` | Read-only snapshot of actual target entries/occurrences/order shown in the proposal, or empty for a new target |
| `proposedEntries` | Mode-specific resulting sequence shown for approval, including Add preservation/restored occurrences |
| `metadataDecisions` | Approved new-score metadata and any explicit existing-score corrections, with affected shared Scores identified |
| `proposalRevision` | Revision of the reviewed proposal; edits invalidate previous approval |
| `approvalState` | Draft/approved status tied to that exact proposal revision |
| `configSnapshotReference` | The immutable configuration snapshot used throughout this run |

Each item carries a piece reference, a distinct occurrence key, its original source position/reference, the final requested order position, and its metadata-decision reference. Repeated uses of one piece remain separate occurrences; changing order does not change the piece identity or silently drop a repeat. Piece resolution must preserve edition, movement, variant and other identity-bearing qualifiers.

This is a logical contract, not a requirement to serialize everything into JSON. Choose concrete native Dictionary/List transport while expanding the implementation design. Keep native PDF Files native where needed, and retain native Score and Setlist objects inside assembly where practical. Do not assume unverified nested-value transport works.

### Identity and ordering

- Service identity is separate from its display name. Renaming a setlist must not accidentally create another service.
- Date plus the stable configured service-slot key identifies the ordinary service. There will not be two services with the same name on the same date; no extra instance ID, time discriminator or additional-service UI is required. Different service names on the same date remain distinct.
- The same service must resolve to the same identity whether supplied by Weekly, Specific service or Mass import.
- A piece and its occurrences are separate: A/B/A means three setlist entries using two scores.
- Ordering is explicit. Neither file-picker order nor alphabetical filename order is a reliable musical running order.

## Common execution and update behaviour

Execution has four explicit phases; every entry point follows the same write boundary:

1. **Read-only preflight:** validate input/config, resolve requested music and existing Scores, read existing setlists/entries, and prepare metadata suggestions and target/order comparisons. Reading provider Files may materialise them for access, but no clean-archive save, score import, Composer/Genre creation, metadata/rename/setlist change is permitted. Resolve targets now; do not create them yet.
2. **Proposal and approval:** show the exact target, name/date, selected Add/Overwrite mode, reviewed old entries, proposed resulting order, reuse/import plans, metadata effects and unresolved work. Name/Date/Order edits invalidate the prior proposal revision and regenerate it. One final confirmation approves that specific plan (or all reviewed plans for Weekly); Cancel performs no music writes.
3. **Approved execution:** recheck the actual target, then archive/import only absent pieces, resolve/create approved metadata objects, apply approved metadata, and create/update the setlist in the selected mode. An existing matched forScore Score always supplies the performance copy, including its annotations; no source-version substitution. New/Add services may be partial; incomplete Overwrite stays pending without clearing. A changed target/content snapshot is returned for review or deferred, never silently broadened beyond approval.
4. **Readback and report:** compare actual entries with the mode-specific result and inspect supported metadata outcomes. Report completed, partial, pending, failed or unconfirmed results. If interrupted, the user reruns the ordinary workflow, reviews current contents and chooses Overwrite/Add to/Cancel; no separate restore or resume wizard is required.

In Add to existing mode, updates are strictly additions-only: never clear a setlist, remove entries, replace an existing score occurrence or reorder existing entries. Explicit Overwrite contents is the sole exception, governed by the replacement policy below. If source music disappears or its positions change, retain the actual setlist contents. If a source piece changes identity, add the newly requested piece while retaining the old one. Manual cleanup is outside the shortcut.

For Add to existing, match piece identities and occurrences, rather than testing simple membership. For requested A/B/A and existing A/B, add one A. For an unchanged rerun with all requested occurrences present, add nothing. If the user deleted a requested entry and reruns service creation, add that occurrence back; deletion is not a persistent omission preference. Use actual current entries rather than an old record to decide what is missing. If the actual list already contains extra occurrences, preserve them. Insert a newly requested piece between its matched source neighbours: existing A/C plus requested A/B/C becomes A/B/C. Insertions may change numeric entry indexes but must preserve the relative order of every pre-existing entry, including manual additions.

Keep occurrence mappings in the service record where possible so repeated pieces and later resolution of missing music target the correct gaps. Use actual setlist readback to verify that existing entries survived and new entries were inserted as planned. Conflicting anchors caused by manual reordering, or ambiguous repeated identities, must be reported without moving existing entries; unaffected insertions and other services may continue. Define a deterministic policy for these conflicts during implementation. If native actions cannot insert into the intended gap, report that limitation rather than clear/rebuild the setlist or silently substitute appending; the user can use the separate manual insertion/repair workflow.

For new services and Add to existing, unresolved music produces a partial service containing the available pieces. Overwrite contents is held pending if requested music is unresolved; keep its existing entries until the full approved replacement can be prepared. Flag each missing occurrence with its service, source reference and intended position in the final report; do not silently omit it or assume a native placeholder feature is available. A later rerun inserts a resolved piece into its intended gap. Only a service-level blocker, such as an ambiguous target or no usable music, leaves the whole service pending. Finish other independent services and report unresolved references, conflicting targets and required decisions afterwards. Do not prompt for each problem during processing. Initial preflight should catch recoverable validation issues before native writes. Some native action errors can terminate a Shortcut without a recoverable result; continuing after such errors requires supported error handling and must not be claimed without device evidence. On rerun, read actual current contents and use the ordinary Overwrite/Add to/Cancel choice; Add must avoid duplicate occurrences and restore requested deletions.

### Service records, cleanup and interruption

A small service record may retain the service ID, edited display-name/target association and last confirmed plan. It is a convenience for current requests, not an independent queue of work or authority over forScore contents. Actual live readback determines whether a target/occurrence currently exists.

If the user deletes a forScore setlist, treat that service as finished. Ignore/invalidate any stale association; do not resurrect it, access it again as a recovery task, or scan history to recreate deleted services. If the user explicitly requests creation for that date/service again later, resolve it as a new current request, without trying to restore the deleted object's identity/history. Absence caused by a failed lookup must still be distinguished from confirmed absence.

If a music Score is deleted, import it again from the available clean archive/current source when a current request needs it. Missing/stale piece records may be rebuilt as needed, reusing approved metadata where available; they must not block a fresh lookup/import. Reimport cannot recreate annotations that were deleted with the old Score. Never replace a Score that still exists merely because the source PDF or saved record differs.

After interruption, rerun the normal shortcut: choose date/service or week folder, show actual current contents, then choose Overwrite, Add to or Cancel. Add reconciles missing requested occurrences; Overwrite uses the complete approved requested sequence. Do not require a separate previous/current/intended recovery screen, rollback engine, deletion tombstones or automatic replay. Preserve normal completeness checks before overwriting; native failures may still leave partial contents and there is no transaction guarantee.

Prefer a verified persistent setlist identifier where available, with supported unique lookup fallback for current requests. Unexpected duplicate matches remain an error to report, not a reason to build a multiple-instance service feature or select the first match.

Reports distinguish unchanged, created, updated, partial, pending, failed and unconfirmed results, and state whether actual identities/order were verified. Missing occurrences retain their intended positions; metadata-pending is separate from missing music.

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

If a previously processed service disappears entirely from the selected folder, do not alter it or recreate it from saved history. A current-folder report may note that absence, but it does not create a recovery task for an old/deleted setlist. Unrecognised filenames and unrelated PDFs need explicit treatment in the preview.

## Specific-service workflow

Implement this entry point first because it establishes the shared execution path with the least input parsing:

1. Select music in Nextcloud, Files or another app and choose Share > Create Service. Receive the shared native files without making the user select them again. Direct launch may offer a file picker as a fallback.
2. Combine every selected piece into one service, regardless of its original day/service prefix. Use prefixes as ordering hints where useful, never as instructions to split this selection. Mixed prefixes or duplicate position numbers need a deterministic ordering fallback visible and adjustable in the summary. Do not assume an app preserves share order.
3. Use a native date picker and a configured service list (Evensong, Eucharist, Mattins) to select the target, prefilled from reliable context where available. Derive the name automatically; do not ask for the whole setlist name. A shared file may lack its date context, so collect the date once rather than guess. Special services use configured/suffix-derived options or an explicit custom-service route.
4. Read any uniquely resolved existing target contents, then offer Add to existing, Overwrite contents or Cancel. Present the proposal and an optional Edit proposal menu; after each edit rebuild the proposal and target comparison. One final confirmation starts writes.
5. After confirmation, call shared assembly, apply the explicitly approved Add/Overwrite mode and return the final result with unresolved items.

Target the Share Sheet title **V3 - Create Service**; exact installed naming and supported input types must be recorded during implementation. File-provider support depends on receiving usable file objects; arbitrary URLs are not assumed to be PDFs. Unsupported inputs appear in the resolution report. A mixed selection always creates one combined service; where its target date or service cannot be inferred uniquely, collect those details once before the summary confirmation. Weekly remains the entry point that automatically splits music into services.

The workflow should also allow targeting an existing service, using the same identity and update rules as Weekly. Define how a user selects an existing service and how its saved details populate the form.

### Target selection and proposal editing (8 November 2026)

Specific service uses a native Date input followed by a native Choose from List/Menu with configured Evensong, Eucharist and Mattins options. This is a native chooser, not a requirement for an embedded web-style dropdown. Do not require a full name to be typed: derive yyyy-MM-dd - EEE - Service. Prefill known context and let the user change it; any genuine special-service option remains available without misclassifying it as a regular service. Disabled dates/slots still need an explicit exception before approval.

Resolve by saved service identity/target association, with unique name lookup only as the supported fallback. If a target already exists, show its actual entries in Manual order, including repetitions and manual additions, then offer:

- **Add to existing** (default): preserve old entries/order; propose only missing occurrences in supported gaps.
- **Overwrite contents**: propose the exact requested occurrence sequence instead of the current entries. Show both sequences and the entries that will be removed from this setlist.
- **Cancel**: finish without music, metadata or setlist writes. The final execution confirmation remains separate from this mode choice.

An empty lookup is not proof of absence if the native action failed; duplicate/ambiguous matches never select the first. Target contents/readback and ambiguity behavior remain device checks. Re-query after a date/service change, and revalidate immediately before execution. If actual contents changed after approval, defer that service rather than silently applying an obsolete plan.

The main review screen shows date, service, derived/overridden name, new/existing target, chosen mode, existing sequence, proposed resulting sequence, imports/reuse and unresolved metadata/music. Offer **Proceed**, **Edit proposal**, **Cancel**. The edit menu has only three editing options: Change Name, Change Date and Change Order (plus Back). Service is chosen initially; Overwrite/Add to/Cancel belongs to target review, not another edit submenu. Music additions/removals are done separately, not in this proposal editor. Essential first-import metadata review remains part of read-only preflight, not a broad optional Edit Music/Metadata menu. The options are:

| Edit option | Result |
| --- | --- |
| Change Date | Date picker; recompute service ID/name and resolve the new target. Never move or delete the old service as a side effect. |
| Change Name | Optional display-name override; retain the date/slot identity. For an existing target, show an explicit proposed rename of the same associated setlist rather than creating a duplicate; apply only after confirmation and supported native behavior is checked. |
| Change Order | Rebuild the proposed requested occurrence sequence with native list choices; preserve the already-requested occurrences, including repetitions; this editor reorders rather than adds/removes pieces. |
| Back | Return to the proposal without an edit. |

After each completed edit, regenerate the full proposal and return to the same review screen. The user can make another edit or proceed; no mandatory sequence of edit questions. Cancelling an individual editor returns to the proposal where native cancellation behavior supports that; cancelling the overall run makes no music writes. A change that resolves a different target resets the old target's mode selection to Add to existing and requires a fresh explicit Overwrite selection if wanted. An earlier Overwrite choice must never carry over invisibly to another target or later run.

This is the intended UI behavior, not an invented Jelly while/break/return feature. Choose an implementation compatible with the app's supported control flow and normal-completion strategy; validate edit/review navigation during the actual entry-point build.

### Ordering proposal

Use recognised numeric file positions when they are comparable within the requested service: 2 precedes 10; gaps are retained and do not imply missing music. For unnumbered music or mixed/noncomparable prefixes, use the order delivered by the file provider/Share Sheet as the initial proposal and show it explicitly. Actual tap order is a useful preference only when that provider preserves it; do not claim the shortcut can reconstruct unavailable selection order. Duplicate positions and other ties must be visible, with received order as the proposed tie-breaker and user adjustment available.

Change Order edits the requested proposal before confirmation. For a new or explicitly replaced setlist, the approved proposal defines the final occurrence order. For Add to existing, preserve all existing relative order even if the proposal is rearranged; preview the actual merged result and identify unsupported/conflicting insertions. If the user wants a wholly different existing order, they must choose Overwrite contents explicitly. Name/date/order edits must not discard piece metadata decisions or flatten repeated occurrences.

### Explicit replacement policy

Overwrite contents changes the chosen setlist's entries only. Preserve library Scores, PDFs, annotations, unrelated setlists and metadata. Do not delete/reimport Scores merely to rebuild entries. Prepare all requested usable Scores and metadata requirements before clearing/removing any old entry. If any requested occurrence is unresolved, leave replacement pending with the original setlist intact; the user can correct/reselect the input music separately and start a new proposal, since the edit menu does not add/remove pieces. An empty replacement is blocked rather than interpreted as a request to clear the service.

Retain the chosen mode and reviewed old/proposed sequences for this execution and its report; saved history is not a prerequisite for later reruns. Recheck target identity and contents, then use only device-verified native replacement actions, verify the clear/remove result before population where applicable, add the complete approved sequence and read it back. A failed/interrupted replacement may leave partial contents; no transaction, automatic rollback or reliable native entry IDs are assumed. The user can rerun, inspect actual current contents and explicitly choose Overwrite/Add to/Cancel to repair the service. No separate recovery wizard or automatic replay of the previous attempt is required. Do not relabel partial replacement as complete, and never clear again without a fresh explicit Overwrite approval.

Weekly continues to infer dates/slots and default to Add to existing without per-service questions. Its batch review offers Edit service, then this same editing/mode interface for the selected service. All edits return to the regenerated batch proposal, and one final batch confirmation covers its explicit per-service modes. Routine automatic Weekly runs never enable replacement globally.

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

## Piece metadata in forScore

Title, Composer and music Type are part of the initial release, shared by Weekly and Specific service. Metadata belongs to the reusable piece/score, not to one service occurrence. Service names, dates and service types such as Evensong or Eucharist remain setlist context.

| Piece information | forScore destination | Policy |
| --- | --- | --- |
| Title | Score Title, using the native title/rename capability once its exact behavior is checked | Human-readable work/movement name; retain edition, voice, key and other distinguishing details. Keep the canonical source reference separately. |
| Composer | Native Composer metadata | Reuse an unambiguous existing Composer object or create an approved one, then assign it to the exact Score. Do not infer full names, authorship or hymn composers from numbers/surnames alone. |
| Type | Native Genre metadata | Use one configured primary music category, such as Psalms, Hymns, Canticles, Anthems, Gloria, SanctusBenedictus, AgnusDei or Kyrie. Archive category and forScore Genre must follow the same approved mapping. |

Use stable internal type keys with configured display, archive-folder and Genre names. For example, key psalm may display Psalm while mapping to existing Psalms folder/Genre. Do not create both Psalm and Psalms, or Anthem and Anthems, simply because callers use different wording. Additional categories can be added centrally. Service type must not become a permanent piece Genre, Tag or Label.

### Resolve and review before execution

1. Resolve the piece and intended existing/new Score using its full canonical identity, independently of editable Title. First preserve existing forScore metadata; an explicit current-run user correction takes precedence only for its approved fields. Saved approved piece decisions provide defaults for new/missing fields, then supported filename/category inference provides suggestions. Conflicts and ambiguous matches require review rather than silent overwrite.
2. Derive suggestions using explicit reference rules before generic composer/title splitting: NEH/AMR/OH identifiers, psalms and verse ranges, movements such as Gloria/Kyrie, then supported composer-work conventions. Preserve the original payload and qualifiers. A generic trailing number/token is not proof of a composer, category or edition meaning.
3. Include a metadata review section in preflight: piece, suggested Title, Composer, Type, source of each suggestion, unresolved/conflicting fields and intended changes. Let the user adjust new or uncertain values before the single run confirmation. Do not ask routine metadata questions while approved services are being processed. Review each distinct piece once per run, even if several services use it.
4. If Composer is unknown, leave it unassigned and report metadata pending; do not fabricate a value or block otherwise usable music. A readable Title can initially fall back to the full canonical payload. A required archive Type must be approved or resolved from a verified category before archive/import; otherwise leave that occurrence unresolved and continue independent usable music.
5. After confirmation, archive the unchanged clean PDF, reuse/import its working Score, and apply approved Title/Composer/Genre to a new Score. Existing Scores retain existing metadata by default; later corrections need an explicit per-field approved change. Do not remove unrelated Composer/Genre assignments or replace annotated Scores as a metadata update strategy.
6. Verify the exact target and the written fields using supported native readback where available. If a field cannot be read back reliably, mark its assignment unconfirmed and include an iPad inspection step; continuing past an action alone is not proof of a metadata write.
7. Persist approved piece-level decisions and their provenance/status in the V3 piece record. Reruns reuse those decisions without repeating questions, while preserving later forScore manual edits. Saved metadata does not prove current forScore contents or supersede those edits silently.

### Shared utility: V3 - Resolve Composer

Add an independently installed V3 utility used by shared assembly whenever an approved composer name needs a native forScore Composer object. Both Weekly and Specific service use this same path through assembly. This utility is part of the initial-release design, not a legacy dependency.

| Contract | Required behavior |
| --- | --- |
| Exact installed name | V3 - Resolve Composer |
| Input | Exactly one nonblank Text composer name, already approved/resolved by its caller. Direct use with supplied input follows the same rules. No interactive name prompt. |
| Success output | Exactly one native forScore Composer object, suitable for the Composers field of Add metadata. Never return the name Text as if it were that object. |
| Controlled unresolved result | No Composer value on blank/invalid input or ambiguous lookup; caller records composer metadata pending. Exact native empty-return wiring remains an implementation/device check. Native action failures can abort instead of returning. |
| Side effects | Create a Composer only when lookup establishes no existing match. Do not attach it to a Score/Bookmark, rename composers, merge entries or alter unrelated metadata. |
| Dependencies | forScore native lookup/create capabilities; no other installed shortcut dependency is currently required. |

Required flow:

1. Trim leading/trailing whitespace; reject empty input before lookup/creation. Do not guess full names, expand initials, remove accents/punctuation or apply surname aliases here. Preflight/shared approved mappings resolve spelling and identity before calling.
2. Look up the supplied name in the intended forScore context, with Continue if not found enabled where supported. Establish actual exact-match and zero/one/multiple behavior during integrated construction. Do not assume a first lookup result is unique or that a loose match is the intended person.
3. One unambiguous approved-name match: return that native Composer object unchanged.
4. No matches: create a Composer using that approved name, with Scores and Bookmarks unset. Return its native Composer output if supported and verified. If creation supplies no usable Composer output, re-query the same name and return only a unique verified result; do not run creation a second time just because its output was empty.
5. Multiple/ambiguous matches: do not create another item, choose the first, merge entries or prompt mid-run. Return no usable Composer; assembly reports pending resolution. Complete independent music where runtime control allows.
6. On retry, always look up again before creating, including after interrupted/unconfirmed creation. A failed/uncertain action is not proof that nothing was created. Concurrent-run uniqueness is not assumed; avoid overlapping creation attempts.

Assembly passes the returned native Composer to Add metadata for its exact verified Score only after the run's approval. Reuse the same resolved object for repeated occurrences/names within the run where native caching is verified; no native Composer serialization in saved records. The utility may be called once per distinct approved name per run, not once per occurrence. Persist the approved name/reference, not the live object, for subsequent runs.

A genuinely unknown composer remains unassigned/pending and is not sent to this utility as a fabricated name. A known composer absent from forScore is created by this utility. The resolver is not an author-identification service and does not infer a composer from hymn numbers or unclear filenames.

Native action research confirms lookup with Continue if not found and Create composer with optional Scores/Bookmarks fields. Standalone creation with those fields empty, lookup ambiguity, native Composer return, caller transport and Add metadata consumption still require device evidence. Do not invent Jelly forScore bindings or assume the older create-and-assign-to-Score path proves this utility's standalone return contract.

Acceptance during the stage-3 metadata increment: existing approved name returns the existing Composer; new approved name creates one item and returns a usable Composer; repeated/trimmed-name calls reuse it; blank input creates nothing; ambiguous matches create nothing; an interrupted/unconfirmed create is retried by lookup; and the returned object can actually be assigned to the intended test Score without touching another Score/Bookmark. Creation occurs only after confirmation, never while merely previewing metadata.

### Existing score reuse and shared metadata

When a matching piece already exists in forScore, always use that saved Score as the performance copy, preserving annotations from previous performances. Do not introduce revised-PDF comparison, content-hash/version review, automatic source replacement or an extra edition-conflict wizard. A different source PDF with the same canonical reference does not replace an existing Score. If the chosen saved music is wrong, the user can correct the insertion/import separately through a manually invoked repair shortcut/workflow; this is outside normal service creation and is not a new dependency of the current preview.

Only a genuinely absent Score needed by the current request is imported/readded. Distinct explicit canonical qualifiers continue to identify distinct references; do not invent aliases or merge pieces to force a match. Unexpected duplicate/ambiguous existing-score matches need manual resolution, not guessed selection or another import.

Title, Composer and Genre corrections on a reused Score affect every service containing that same Score. State that shared effect in preflight and apply only explicitly approved fields, preserving other metadata and annotations. Use approved composer aliases centrally rather than automatically expanding surnames. Multiple composer/arranger handling, if supported, must preserve existing assignments and use explicitly supplied roles/names; do not invent authorship or overwrite a composer's entry with an arranger. Essential first-import metadata decisions still occur before confirmation even though the optional edit menu is limited to Name/Date/Order.

### Canonical identity and persistence

Introduce a small V3 piece-metadata record keyed by the full canonical piece reference, separate from service records and occurrence positions. Proposed fields: record/schema version, canonical reference, source references, approved title, composer reference/display name, type key, relevant qualifiers, provenance/review status per field, verified Score locator where available, last applied/verified values and pending issues. Store serializable references, not native Score/Composer/Genre objects or access tokens. Shared plans reference this piece record; A/B/A still means three occurrences and two piece records.

forScore title changes must not break score reuse. The existing research has not established whether native Rename changes Title, filename or both, nor a reliable persistent Score identifier. During assembly construction, establish that behavior and store a usable target association before enabling title edits. Never depend only on the edited human-readable Title for identity or treat a failed old-name lookup as permission to import a duplicate. Ambiguous/unavailable target resolution is pending work. Canonical archive PDFs remain unchanged by score metadata edits.

### Initial metadata examples

These are review suggestions, not validated authorship/catalogue data:

| Canonical reference | Suggested Title | Composer proposal | Type proposal |
| --- | --- | --- | --- |
| Rose-Responses(SATTB) | Responses (SATTB) | Rose; expand only through an approved mapping | Responses |
| Sumsion-InG | In G, retaining more work detail when known | Sumsion; approved mapping if available | Canticles, subject to review because key alone does not establish work/type |
| NEH485-ThyHandOGodHasGuided | NEH 485 - Thy Hand, O God, Has Guided; user-reviewed spacing | Unknown unless supplied/approved; NEH485 is not a composer | Hymns |
| Ps119vv49-64 | Psalm 119, verses 49-64 | Unknown unless supplied/approved | Psalms |
| Mozart-Spatzenmesse-Gloria | Spatzenmesse - Gloria | Mozart; approved mapping if available | Gloria |

Implement metadata preparation and persistence in the new V3 shared assembly path, not as a legacy-shortcut dependency. Native Composer/Genre action fields have recorded research, but the V3 writes, title/filename semantics, lookup persistence and readback still need integrated manual iPad acceptance. Current filename-preview sources do not yet edit metadata.

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
- Add to existing adds missing occurrences without removing, clearing or reordering old entries. Source removals/manual edits survive default reruns. Explicit Overwrite contents instead requires an approved complete sequence, affects only target entries and preserves Scores/annotations.
- Existing A/C plus requested A/B/C becomes A/B/C by inserting B, without moving the existing entries. A piece resolved on a later run fills its intended gap.
- A/B/A preserves all three occurrences in the correct order while reusing scores.
- Differently named services on the same date remain distinct. Two services with the same name on the same date are outside the user's workflow and require no separate instance UI.
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
- After interruption, an ordinary rerun shows actual contents and offers Overwrite/Add to/Cancel. No dedicated recovery wizard or automatic rollback is required.
- V3 has its own installed namespace, configuration and contracts, with no legacy shortcut dependencies.
- First-time imports receive approved Title, Composer where known, and Type as Genre. Verify actual forScore values and target identity; unknown Composer is metadata pending, not an invented value.
- Reusing a piece across services or rerunning does not duplicate Composer/Genre objects, repeat approved metadata questions, overwrite manual metadata or import another Score after a Title change.
- Explicit metadata corrections affect only approved fields on the verified Score, preserve annotations and other assignments, and leave the clean archive PDF unchanged.

Additional lifecycle acceptance: no music writes occur during preflight; the exact target/mode/old/new sequences and edited order/name are carried into execution; an existing matched Score is always reused rather than replaced by a newer source; a requested entry deleted from a live setlist is restored on rerun; a deleted needed Score can be reimported from available source/archive; deleted setlists are not resurrected from history. Shared metadata changes are explicitly shown before approval.

Additional UI acceptance: Specific service uses Date + Service controls rather than mandatory full-name typing; actual existing contents are shown before choosing Overwrite/Add to/Cancel; edit options return to a refreshed proposal and permit repeated edits; changing target resets replacement selection; received-order fallback is honestly labelled; Add preserves old order while Overwrite follows the approved complete order. Cancellation before final approval causes no music writes. Replacement with unresolved/empty music leaves old entries intact. Verify interrupted replacement recovery separately from additions-only retries.

## Decisions to expand next

1. Exact service identity format and rules for sharing identities across entry points.
2. Service-plan item fields, supported piece-reference forms and native input/output contracts.
3. Confirm Sunday prefix mappings, special-service position/separator syntax and folder month/day rules. The regular weekly schedule and missing-year default are recorded above.
4. Ordering interface, including preserving existing requested repetitions and resolving conflicting positions without adding/removing pieces in the editor.
5. Minimal service-record storage and live lookup: deleted targets are retired, missing pieces/records rebuild only on current demand, and interrupted runs use ordinary Overwrite/Add to/Cancel.
6. Define occurrence matching and insertion-anchor conflict behaviour while preserving existing entries and their relative order. Gap insertion and partial services are confirmed requirements.
7. Share Sheet fallback date/service selection and deterministic ordering for unprefixed or mixed-prefix music. Combining the selection into one service is confirmed. CSV template and parser decisions remain deferred.
8. Exact V3 installed shortcut names, dependency order and installation instructions.
