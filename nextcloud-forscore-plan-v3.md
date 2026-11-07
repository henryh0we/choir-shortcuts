# Choir shortcuts implementation plan — version 3

Date: 7 November 2026  
Status: Proposed architecture and implementation plan; ready for expansion.  
Previous plan: [version 2](nextcloud-forscore-plan-v2.md)

## Purpose and scope

Build at least three user-facing Apple Shortcuts for creating and updating choir service setlists in forScore:

1. **Weekly:** select a week folder, parse its PDFs into individual services and create or update their setlists.
2. **Specific service:** select a series of pieces, arrange them and create or update one service setlist.
3. **Mass import:** supply a spreadsheet export containing dates, services and pieces, then create or update multiple setlists.

All three workflows must use the same rules for piece identity, service identity, ordering, archiving, score reuse/import, metadata and setlist updates. Repeating the same request should produce the same ordered setlist without unintended duplicate scores or setlists.

Move into implementation rather than extending the current programme of isolated diagnostics. Resolve remaining generation and runtime problems as they arise during construction and integrated use. Preserve the working installed shortcuts and their native repairs before replacing them.

This version establishes the overall structure. It does not claim that the proposed interfaces or all required actions are already implemented or device-verified. Earlier plans remain reference material; this document guides the proposed multi-entry-point structure. Existing source contracts remain in force until explicitly migrated.

## Shared architecture

```text
Weekly folder --------+
                      |
Specific service -----+--> Service plan --> Shared assembly --> forScore setlist
                      |
Spreadsheet import ---+
```

Each entry point decides what belongs in a service and produces the same logical service plan. Shared assembly owns the execution of that plan.

| Component | Responsibility |
| --- | --- |
| Weekly entry point | Read the selected folder, identify services, order their pieces and submit approved services |
| Specific-service entry point | Select pieces, arrange their occurrences, collect service details and submit one service |
| Mass-import entry point | Read and validate spreadsheet rows, group them into services, resolve references and submit approved services |
| Shared assembly helper | Validate one service, prepare its music, resolve its target setlist, reconcile entries and return a report |
| Canonical naming utility | Apply consistent canonical piece naming across all entry points |
| Archive utility | Save or reuse canonical PDFs using shared archive rules |

Build on the existing naming, archive and assembly helpers. Initially keep score preparation and setlist updating together inside assembly so native forScore objects do not need to cross several helper boundaries. Extract further helpers only where there is a concrete reuse benefit.

The labels above describe responsibilities, not newly agreed installed names. Preserve established installed names and caller contracts during migration; document exact names before adding new shortcuts.

## Common service-plan contract

All entry points produce the following logical structure:

| Field | Purpose |
| --- | --- |
| `schemaVersion` | Version of the service-plan contract |
| `serviceId` | Stable service identity across reruns and entry points |
| `serviceDate` | Explicit ISO date, including year |
| `serviceType` | Eucharist, Evensong or another configured service type |
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
4. Compare the actual entries with the requested sequence.
5. Leave an unchanged service alone, or present and apply its proposed update.
6. Read back the entries and report the result.

Updates reconcile the complete sequence, including additions, removals, reordered pieces and deliberate repetitions. Appending only new pieces would leave stale entries behind.

Prepare replacement scores before clearing an existing setlist. Begin with the existing replacement approach, checking that clearing succeeded before adding entries. Selective entry editing can be considered later if it provides a clear benefit.

Unresolved music leaves the affected service pending by default. Do not silently omit pieces. The exact approval flow for individual and batch updates remains a design decision; retain explicit review of changes to existing setlists.

### Service records and recovery

Introduce a small persistent service record linking `serviceId` to the target setlist and the last confirmed plan. This is a proposed addition: the current architecture does not yet maintain such a manifest.

The record assists identity resolution and recovery; it is not proof of current forScore contents. After an interrupted update, read the actual setlist before deciding what remains to do. There is no assumed transaction or automatic rollback.

Prefer a verified persistent setlist identifier if one is available. Define a fallback lookup policy, including duplicate matches and renamed setlists, during implementation planning.

Reports should distinguish unchanged, created, updated, pending, failed and unconfirmed services, and state whether actual entry identities and order were verified. Preserve useful per-piece outcomes such as reused, imported and metadata pending.

## Weekly workflow

1. Select the week folder.
2. Confirm its dates and year.
3. Read the relevant PDFs.
4. Parse filename prefixes into day, service/session and numeric position.
5. Group files into services and preview the proposed running orders.
6. Resolve ambiguous files or ordering.
7. Submit approved services to shared assembly.

Existing folder examples distinguish prefixes such as `Sun`, `Sunam` and `Sunpm`. Store their meanings in shared configuration. Sort positions numerically so item 10 follows item 9.

Do not guess a year from a folder name that omits it. Define how week dates are confirmed and how year boundaries are handled.

On rerun, the current folder supplies the proposed complete contents of each represented service. A removed file therefore appears as a proposed removal from its service setlist. New files become additions; changed positions become reordering.

If a previously processed service disappears entirely from the folder, flag it for review rather than automatically deleting its setlist. Unrecognised filenames and unrelated PDFs need explicit treatment in the preview.

## Specific-service workflow

Implement this entry point first because it establishes the shared execution path with the least input parsing:

1. Select PDFs.
2. Review and adjust their order, including repeated pieces.
3. Enter the service date, type and name.
4. Preview the service.
5. Call shared assembly.

The workflow should also allow targeting an existing service, using the same identity and update rules as Weekly. Define how a user selects an existing service and how its saved details populate the form.

## Mass-import workflow

Start with a spreadsheet exported as CSV, with one row per piece occurrence. Direct workbook support can be considered later if needed.

Proposed initial template:

| serviceId | date | serviceType | serviceName | position | pieceReference |
| --- | --- | --- | --- | ---: | --- |
| 2026-11-08-eucharist | 2026-11-08 | Eucharist | Sunday Eucharist | 1 | Walsh-Responses.pdf |
| 2026-11-08-eucharist | 2026-11-08 | Eucharist | Sunday Eucharist | 2 | Ps023.pdf |

Use canonical filenames or explicit source references initially. Free-text titles alone can be ambiguous. Define the reference search locations and how missing or multiple matches are resolved.

Validate the whole import and show a batch preview before applying changes. Validation must cover required columns, dates, service grouping, conflicting details for one service, positions and piece references. Report issues by service and row.

A service containing unresolved music remains pending by default; other valid services can proceed. Rerunning the same file updates the same services. Each represented service is a complete requested sequence, so removing a row can propose removing an entry. Absence of an entire service from a later import does not imply deletion.

CSV parsing must support quoted fields, including embedded commas. Splitting every line on commas is insufficient. The template and parser must agree on encoding, delimiter and supported field contents.

## Shared configuration

Keep common settings in one place and use one immutable configuration snapshot per run. Extend the existing configuration rather than introducing separate copies in each entry point.

Configuration should cover source/archive locations, filename-prefix parsing, service-prefix mappings, setlist naming, piece-resolution policy and service-record storage. Keep credentials out of committed source and example records.

Retain the existing metadata direction: archive music category becomes Genre for first-time imports; service type does not become permanent piece Tags or Labels. Existing archive and score reuse policies should be shared by all entry points.

## Implementation sequence

1. **Expand the contracts and policies.** Finalise service identity, item references, native transport, filename grouping, ordering, update review and reports.
2. **Adapt shared assembly.** Add a supplied-service-plan route while preserving the established interactive caller during migration. Keep working installed copies backed up.
3. **Complete Specific service.** Establish selection, ordering, preview, execution and updates end to end.
4. **Add Weekly.** Implement folder reading, date resolution, parsing and grouping around the same assembly path.
5. **Add Mass import.** Provide the CSV template and translate validated rows into the same service plans.
6. **Run integrated acceptance cases.** Exercise reruns, updates, repetitions, unresolved music and interrupted execution, fixing issues encountered in the completed workflows.

Do not require another broad round of isolated probes before proceeding. Use focused diagnostics when an actual implementation problem needs them. Keep local compilation, generated structure, device import, repaired execution and untouched-source execution evidence separate.

## Acceptance criteria

- The same service plan produces the same ordered setlist from any entry point.
- An unchanged rerun creates no unintended duplicate scores or setlists.
- Updates handle additions, removals and reordering.
- A/B/A preserves all three occurrences in the correct order while reusing scores.
- Two distinct services on the same date remain distinct.
- Weekly numeric ordering handles positions such as 2 and 10 correctly.
- Ambiguous or missing music is reported and never silently omitted.
- Invalid CSV rows identify their service and row; valid independent services can still proceed.
- An interrupted run can resume by reconciling actual setlist contents.
- Existing working installed helpers remain recoverable during migration.

## Decisions to expand next

1. Exact service identity format and rules for sharing identities across entry points.
2. Service-plan item fields, supported piece-reference forms and native input/output contracts.
3. Week-date confirmation, service-prefix mappings and handling of unrecognised PDFs.
4. Ordering interface, including repeated pieces and conflicting positions.
5. Service-record format, storage, setlist lookup and recovery checkpoints.
6. Update preview and approval behaviour for one service and a batch.
7. Final CSV template, reference resolution rules and parser implementation.
8. Exact installed shortcut names, dependency order and migration instructions.
