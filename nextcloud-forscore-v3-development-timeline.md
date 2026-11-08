# V3 development order and manual iPad checkpoints

Date: 7 November 2026  
Authority: [v3 plan](nextcloud-forscore-plan-v3.md)  
Status: Stage 2A has reported one-file/multi-file filename-preview passes, including Sunday slots, Monday exclusion, Thur and SunRemem. Quote-line artifacts and broader acceptance cases remain pending. No local builds or tests have been run. See [current sources/contracts](jelly/docs/v3-development.md) and [device evidence](jelly/tests/v3/README.md).

Naming evidence, 8 November: [updated Nextcloud listing analysis](jelly/docs/v3-development.md#nextcloud-naming-evidence-and-implementation-implications-8-november-2026) now informs the next date/ordering increment: single-date and range folders, preserved qualifiers, gaps that do not imply missing PDFs, and constrained discovery. Collection-specific and historical event formats remain separate from current weekly rules.

We will build one small, usable increment, transfer its `.jelly` through Copyover, inspect the generated actions, and then you will test it on the iPad. Your results determine the next increment. We will resolve generation problems inside that increment rather than restart a broad diagnostic programme.

I will review source, contracts, callers, documented signatures and recorded research. I will not run code, builds, automated tests or compilation to claim correctness. You will compile, inspect and execute on the iPad. This follows your current instruction over the repository's usual local-build requirement.

V3 is a ground-up creation under **V3 - ...** installed names. It has no legacy shortcut dependencies, compatibility adapters or backup prerequisite. Reuse research only. This user direction supersedes the earlier migration approach.

Current source pair: parser revision 3/interface 2.0 and preview revision 5/interface 3.0. Guarded processing and natural completion replace generated Output/Exit calls. Preview uses one native config File reference configured after import; no manual stop blocks are needed. Reported fixtures work, while exact installed revisions and saved-config persistence remain unconfirmed. See the [return history](jelly/docs/v3-output-resolution.md) and [current setup](jelly/tests/v3/README.md#current-setup-preview-revision-5-saved-config-file).

## Sequence at a glance

These are development/test cycles, not calendar commitments. A failed checkpoint adds a repair cycle to its stage. Some stages deliberately have two checkpoints so a failure does not require debugging the entire workflow.

| Stage | Increment | Your iPad checkpoint | Dependency |
| --- | --- | --- | --- |
| 0 | Establish the fresh V3 namespace and config | New names and disposable test area ready | None |
| 1 | Freeze the first implementation contracts and native update requirements | Review representative parsing/identity examples and available insertion fields | 0 |
| 2 | New shared config, parsing and read-only preview | 2A filenames first; dates/order in the next increment | 1 |
| 3 | Supplied-plan assembly route and score preparation | Native input survives; reuse/import and metadata behave correctly | 2 |
| 4 | Create one new service and persist its identity | Exact A/B/A sequence, two scores, one setlist; record survives restart | 3 |
| 5 | Additions-only reconciliation and interruption recovery | Unchanged rerun, A/C → A/B/C, manual edits and safe retry | 4 |
| 6 | Specific service from Share Sheet | One combined service, one confirmation, no second file selection | 5 |
| 7 | Weekly folder preview | Correct grouping, numeric order, dates and exclusions; no music writes | 2, 6 |
| 8 | Weekly execution and batch recovery | Multiple services, partial results and resume | 7 |
| 9 | Integrated acceptance and promotion | Both entry points target the same service; V3 names/contracts are reviewed | 8 |

The first end-to-end milestone is stage 4. The first v3-compliant update milestone is stage 5. Specific service is complete at stage 6; Weekly is complete after stages 8–9. Mass import remains deferred.

## Evidence we can build on

The [latest investigation results](jelly/tests/ipad-investigation/generation-groups-results.md) and [installed repair record](jelly/docs/ipad-assembly-lessons.md) take precedence over older status paragraphs elsewhere.

| Recorded observation | Implementation consequence |
| --- | --- |
| Name-first Copyover headers work by user report; the single-comment/header-free experiments improved generation | Deliver `.jelly` only, with one physical name-first metadata comment. Inspect each new export; this does not prove all comments safe. |
| Text `var collectedValues += RepeatItem` produced A/B/A by user report | Use the documented candidate form where applicable; inspect the generated Add to Variable action. |
| File collections counted repeated PDFs but the final Repeat visited only the distinct pair | A native File collection cannot be assumed to preserve occurrences. Represent occurrences separately from the unique file pool; verify both boundaries in integrated assembly. |
| Indexed File candidate failed on `type: Item at Index`; earlier selector spellings also failed | Do not use either failed selector as an established solution. Use supported source forms or explicit native completion slots. |
| Text assignments, two-Text extraction and some File assignments have narrow reported passes | Reuse those forms without extending their evidence to mixed dictionaries, nested values, Score transport or complete helpers. |
| G1C rejected equal counts; generated token/default/polarity defects occurred | Inspect actual operands and operators. Count equality never proves identity or sequence. |
| Repaired installed assembly can create services and offers replace/skip; archive-category/Genre draft is not fully device-tested | Implement new components from this research. Legacy automatic replacement is not the V3 default; explicitly chosen Replace contents is now part of the reviewed design and needs fresh native verification. Category transfer and unattended handling also need integrated checkpoints. |

Native forScore availability does not establish a Jelly binding, reliable identifier, arbitrary insertion position or recoverable error handling. Those remain implementation questions.

## Stage 0 - establish the fresh V3 workspace

**Development work:** Give every new installed shortcut a V3 - name and independent contracts. Keep the new config separate. No old shortcut is required, renamed, upgraded or used as a dependency. Historical source and research stay available as reference.

**Your checkpoint:** When installing the first increment, confirm the two V3 names and the V3-only Run Shortcut target. Use disposable copies of PDFs for filename cases. Record iPadOS and Jellycuts versions; record forScore/provider versions when those integrations are introduced. No legacy backup or installation audit is required.

**Advance when:** The new items are distinguishable in the Shortcuts list and their calls/config are independent of old shortcuts. The initial sources and inventory establish this in source; generated names and wiring await your inspection.

## Stage 1 — contracts and the update capability boundary

**Development work:** Write the concrete contracts before changing executable source. Keep these proposed defaults explicit until checked against the examples:

- Service identity: `YYYY-MM-DD/slot-key`; display names and prefix spellings are excluded. Distinct exceptional services require distinct slot keys.
- Plan envelope: `schemaVersion`, `serviceId`, `serviceDate`, `serviceSlot`, `serviceType`, `serviceName`, `sourceReference`, and ordered `items`, plus a documented link to the run's single config snapshot.
- Item: stable occurrence key, numeric position, piece reference preserving edition/movement/variant, source reference, optional metadata/category and resolution status. Occurrence keys must survive discovery-order changes and missing items; identical filenames alone cannot identify two occurrences.
- Keep a native PDF pool separate from occurrence records. Proposed transport is a native context List carrying a plan Dictionary, unique PDF Files, the config snapshot and required Folder context. Its exact cardinality/extraction is to be specified and checked in stage 3; do not assume nested values or native Files survive it.
- Assembly is a new V3 supplied-plan component, independent of the old `interactive` interface. Define preflight and approved execution separately so one confirmation can cover the whole run.
- Durable service records contain version, service ID, target locator, last confirmed request, occurrence mappings, unresolved positions and pending/verified progress. Store only serializable references, never native Score/Setlist objects or access tokens. A record is evidence of intent, not current contents.
- Resolve by a verified persistent setlist identifier if available. Otherwise use recorded names with exact unique lookup in the intended library. Missing/renamed/duplicate targets require explicit relinking before confirmation; never create another service solely because its display name changed.

**Your checkpoint:** Review the Sunday examples (`Sun` Eucharist, `Sunam` Mattins, `Sunpm` Evensong), special example `SunRemem1-Piece.pdf`, actual week-folder names, and their proposed parsed dates. Confirm separators and ambiguous examples before encoding those rules. Inspect native add/readback actions for insertion/anchor settings and usable score, entry and setlist identity information; record the actual fields rather than inferring them from action names.

**Advance when:** The first supported filename/folder conventions and contract are concrete, installed development names are documented, and we know which native operations need completion slots. Do not delay construction for unrelated probes. If insertion capability remains uncertain, carry the question into stage 5's disposable update, before building the production entry points around it.

## Stage 2 — shared configuration and parser preview

**Development work:** Create a separate versioned V3 config; no legacy config migration is needed. Arrange editable rules in v3's order: filename formats, week-folder dates, schedule, naming, then exceptions/run behavior. Preserve archive categories and folder settings.

Implement one ordered parser result containing day, slot, numeric position and canonical payload. Grouping and canonical naming must consume that same interpretation. Explicit sessions precede bare-day and special-suffix fallback. Unknown/conflicting matches stay unresolved. V3 grouping and naming will share the new parser result; no legacy caller adapter is required.

Use one config snapshot per run. Resolve saved week dates first, then explicit folder year, otherwise current year; persist resolved week context for reruns. Handle December/January explicitly without imposing historical weekday/year matching. No year prompt.

**Current delivery:** Stage 2A implements filename interpretation and recurring schedule switches only. Follow [its manual checkpoint](jelly/tests/v3/README.md) first. Dates, numeric sorting, saved context and dated overrides below belong to the next increment and are not implemented yet.

**Full-stage checkpoint:** Run a read-only preview on a small fixture folder containing Tuesday, Sunday bare/am/pm, `SunRemem`, a disabled Monday, aliases `Thu`/`Thur`/`Thurs`, positions 2 and 10, an unknown prefix and an edition-qualified name. Include one supported old/new format pair. Check grouping and canonical payload agree, qualifiers survive, and exclusions are called skipped. Check a date override, absent Mattins, a month boundary and a December/January week. Reload saved week context with a different default year and confirm unchanged service IDs.

**Advance when:** The preview is correct and performs no archive/import/metadata/setlist writes. Document exactly which conventions are supported; do not claim arbitrary naming schemes work.

## Stage 3 — supplied-plan assembly and preparation

**Development work:** Build the new V3 assembly supplied-plan route. Keep native Scores/Setlists inside it. First inspect the incoming plan and native file pool, then connect naming/archive/reuse/import and first-import Genre handling. An occurrence references its piece; it does not require duplicating native PDFs to represent A/B/A.

Move unresolved category/title/composer choices into preflight, reuse saved decisions, or leave the occurrence unresolved. The legacy experiments reveal category and metadata prompt risks: design the new V3 archive and assembly to resolve these before approval. Define an explicit prepared/batch contract with no legacy callers. Unknown required category must not become an automatic guessed `Other`.

**Your checkpoint A:** Supply two different PDFs and three occurrence records A/B/A. Inspect two usable native Files and three ordered occurrences at the receiver, then inspect the caller's actual return. Check malformed/missing plan fields are rejected before music writes. Check current named variables, Count operands, missing-value polarity and Run Shortcut targets.

**Your checkpoint B:** After approval, prepare one existing score and one new test score. Check archive save/reuse, canonical lookup, no overwrite of annotated scores, category transfer and Genre only on first import. Include a third unresolved occurrence: it must appear in the report without blocking the usable pieces. Confirm no routine category or metadata questions appear during execution. This stage does not yet write setlists.

**Advance when:** The actual transport and preparation paths work in this integrated context. Keep any native additions documented with adjacent stable ADD/RECONNECT/CHECK source comments. If native transport fails, change that boundary and retest it rather than stringify Files.

### Stage 3 Composer utility dependency

Implement and verify **V3 - Resolve Composer** before assembly Composer assignment. Input is an approved name Text; output is the native existing/new Composer object. Check standalone create without Score/Bookmark attachment, unique lookup, native return consumption, blank/ambiguous names, repeat calls and retry after unconfirmed creation. It must not fabricate unknown authorship or create objects during preflight. See the [utility contract](nextcloud-forscore-plan-v3.md#shared-utility-v3---resolve-composer). Current preview shortcuts have no new dependency.

### Stage 3 metadata requirement

Title, Composer and music Type are initial-release requirements. Type maps to forScore Genre using the shared archive/category mapping. See the [metadata plan](nextcloud-forscore-plan-v3.md#piece-metadata-in-forscore). Add the V3 piece-record contract and preflight metadata review to this stage, without routine execution-time prompts or legacy dependencies.

**Additional iPad checkpoint:** Prepare a new test Score with reviewed title/composer/type and inspect those actual values in forScore. Reuse it in another service and rerun: no duplicate Score/Composer/Genre, repeated review prompt or overwrite of manual edits. Test unknown Composer as pending, a required unknown category as unresolved, and an explicit per-field correction. Before enabling Title edits, establish whether native Rename changes filename as well, verify the saved Score association still resolves the same annotated Score after editing its title, and inspect supported metadata readback. Any unavailable readback remains unconfirmed, not a pass. The clean archived PDF must remain unchanged.

## Stage 4 — create a new service and its record

**Development work:** Create an unused target, add available occurrences individually in requested order and read back Manual order. Drive the write loop from occurrence records, not an assumed repeated-File/Score collection. Confirm deliberate repetitions are allowed. Persist the target association and verified occurrence mappings; keep pending intent before writes so a crash does not erase what was attempted.

Resolve existing targets during preflight. Show intended dates, target, sequence and unresolved items before a single confirmation. Cancelling it must leave music and setlists unchanged; progress/config bookkeeping must be documented separately. Opening the setlist is navigation, not verification.

**Your checkpoint:** First cancel a new-service preview and inspect for music writes. Then approve A/B/A: inspect three actual setlist entries in that order using two scores. A count of three alone is insufficient. Repeat with A/[missing B]/C: create A/C, report B at position 2. A service with no usable music remains pending without an empty setlist. Close/reopen the workflow and verify its record still resolves the original target.

**Advance when:** New-service creation, partial reporting, record persistence and actual identities/order are confirmed. Reruns stay guarded until stage 5 is implemented.

## Stage 5 — additions-only updates and recovery

**Development work:** Implement Add to existing as the default plus an explicitly selected, confirmed Replace contents route under the [replacement policy](nextcloud-forscore-plan-v3.md#explicit-replacement-policy). Legacy installed behavior is research only, not a dependency. Add must never fall back to clear/rebuild when insertion is unavailable. Compare actual entries against requested occurrences and saved mappings. Match repeated occurrences one-to-one; do not reduce the request to unique scores.

Proposed conflict policy: prefer verified saved occurrence-to-entry mappings; otherwise match unambiguously in existing relative order. If repeated identities or reversed anchors make placement ambiguous, leave the affected insertion unresolved. If native gap insertion is unavailable, leave it pending. Do not append it elsewhere or rebuild the list. Other unambiguous additions and services may proceed. Preserve source removals and all pre-existing entries, including manual extras. If a saved entry disappeared manually, flag the intent conflict rather than guessing whether to restore it.

Read actual contents immediately before applying the approved additions. If they changed after preview, do not silently broaden the approved work: leave the affected service pending and continue independent services. Checkpoint writes and read back after each operation whose result could otherwise be ambiguous on retry. Record an attempt separately from a verified result. A native action may still halt the shortcut; recovery on relaunch is required even where continuing within that run is impossible.

**Your checkpoint A:** In disposable services verify:

| Existing / request | Required result |
| --- | --- |
| A/B/A / identical rerun | No new scores, entries or setlist |
| A/C / A/B/C | Insert B in the gap; original A and C retain relative order |
| A/B / A/B/A | Add exactly the missing A occurrence |
| A/X/C, with manual X / A/B/C | Preserve X and all old entries; apply the documented unambiguous gap policy |
| A/B/C / A/C, or changed source positions | Retain all old entries and their relative order |
| Manually reordered C/A / A/B/C | Report conflicting anchors; do not move C or A |
| Ambiguous repeated entries | Resolve only from verified mapping or report pending |
| Same ID with changed display template | Reuse the same target |
| Two services on one date; duplicate/renamed targets | Keep distinct IDs; do not select first match or silently create duplicates |

**Your checkpoint B:** Interrupt after target creation, after one addition and after an addition before its record is confirmed. Relaunch, inspect actual contents and verify no duplicates. Resolve the previously missing B and confirm it fills A/C's gap. Change contents between preview and execution and check the service is deferred.

**Advance when:** Gap insertion and preservation work using actual supported native actions, or the feature is explicitly blocked. An insertion limitation blocks the claim that v3 updates are complete; it does not justify weakening the policy. Other read-only construction can continue, but do not promote either entry point as v3-ready.

Additional stage-5 replacement checks: show actual old/new contents; Cancel leaves music unchanged; incomplete/empty replacement preserves the old list; explicit complete replacement changes only that target's entries and preserves Scores/annotations; target changes reset mode to Add; interrupted replacement reconciles saved intent with actual entries without assumed rollback or blind clearing.

## Stage 6 — Specific service

**Development work:** Build the Share Sheet entry around the tested shared path. Target the Share Sheet title **V3 - Create Service**; record its exact installed name and every caller before delivery. Direct launch offers a file picker; shared input uses the received native Files. Reject/report links or unsupported objects without pretending they are PDFs.

Keep all selections in one service. Infer date/slot from usable context or let the user select an existing managed service. Its saved ID/date/slot populate the form. Ask once for genuinely missing context before the summary. Define a deterministic mixed/unprefixed order, expose it for adjustment, and persist occurrence identity independently of that adjustment. Suggested fallback: numeric positions where comparable, then canonical/source-name tie breakers; unresolved ties require an explicit order before approval.

**Your checkpoint:** Share from Files and Nextcloud separately; include mixed service prefixes, duplicate positions, unprefixed music and an unsupported link. Check no second file selection, exactly one combined service, editable order and one confirmation. Test direct launch, cancellation, missing date/slot, targeting an existing service, a repeated piece and an explicitly approved disabled-slot exception. An unrelated entry point must not bypass exclusions.

**Advance when:** Create, unchanged rerun and gap update work through the real Share Sheet path. Record support per provider and delivered input type; one provider's success does not establish all providers.

Stage-6 review checks: native Date + Service choice derives the full name; existing target contents appear before Add/Replace/Cancel; Edit proposal supports repeated name/date/service/order/metadata edits and returns to a refreshed proposal; Add preview preserves existing order, Replace/new uses the approved sequence; received-order fallback does not claim unavailable tap order. Weekly later reuses the interface per service without mandatory per-service gates.

## Stage 7 — Weekly preview

**Development work:** Add folder selection and file discovery around the shared parser and plan contract. Split only here. Use saved week context, enabled days/slots and dated overrides. Compute all target lookups and proposed additions before presenting one summary. Capture unresolved/skipped files and missing expected services. Absent optional Mattins is not a missing-piece error.

**Your checkpoint:** Select a representative small week with Tuesday/Thursday/Friday/Saturday Evensong; Sunday Eucharist/Evensong and optional Mattins; Monday music; one special service; positions 2/10; an unknown prefix; and a disabled slot. Check dates, names, IDs, grouping, numeric order, overrides, exclusions, unresolved files and missing expected services. Include a service seen in a prior run but absent now: report it without deleting anything. Cancel and confirm no music writes.

**Advance when:** The preview is accurate without routine per-service naming, ordering or year questions. A single run uses one config snapshot; an external edit takes effect next run.

## Stage 8 — Weekly execution and partial recovery

**Development work:** Submit the approved plans through the same assembly path, checkpoint between services, and aggregate unchanged/created/updated/partial/pending/failed/unconfirmed results. Known unresolved pieces must not prevent available music or independent services from processing. Distinguish validation issues that return a result from native fatal errors that can stop the run.

**Your checkpoint:** Approve a week with two usable services and one partial service. Verify no routine prompts during processing and one final report naming every unresolved occurrence and intended position. Rerun unchanged, then add music, remove a source file, change source positions and resolve the missing piece. Existing manual edits survive. Interrupt between services and within a write, then resume from actual readback. Check earlier services are not duplicated. If a native error halts the run, confirm durable progress and report recovery on relaunch rather than claim uninterrupted continuation.

**Advance when:** Batch behavior and resume are confirmed, including an honest account of action failures the runtime cannot catch.

## Stage 9 — integrated acceptance and promotion

**Development work:** Reconcile the V3 source headers, contracts, configuration setup, dependency inventory, native repair guide and manual evidence. Preserve historical research as evidence. Promote only the exact source revision plus documented native completions that you tested.

**Your checkpoint:** Create through Specific service and update the same ID through Weekly, then reverse the direction on another service. Confirm one target, additions-only behavior, repeated occurrences, partial resolution and no duplicate score import. Check prefix/template edits preserve identity, saved week dates survive a changed current-year default, disabled slots require an exception and first-import Genre does not change existing score metadata. Revisit source removal, conflicting anchors and interruption once through the completed entry points.

**Advance when:** The [v3 acceptance criteria](nextcloud-forscore-plan-v3.md#acceptance-criteria) for the initial release have recorded results. Keep failed or untested cases explicit. A repaired-runtime pass may support release with documented native completion, but must not be described as untouched-source generation working.

## Delivery and feedback for every stage

Each development delivery will contain the changed `.jelly` paths and revisions, exact installed names and dependency order, KEEP/EDIT/REMOVE/ADD/CHECK instructions for native changes, checkpoint inputs and expected observations, and affected contracts/docs. Preserve empty initializers; delete only identified replacement placeholders after reconnecting every consumer.

You will compile on the iPad and inspect the generated actions before running them. Record the received revision or hash where practical, actual installed names, warnings, missing actions, token/default/operator defects and repairs. Then record actual runtime and resulting archive/scores/setlist identities and order. A successful transfer or compilation is not a runtime pass.

Use this short result record after each checkpoint; screenshots are useful when an action or connection is uncertain:

```text
Stage / checkpoint:
Source revision or hash; actual installed name(s):
Device / app versions (or unchanged from recorded baseline):
Compilation: not attempted / failed / generated; warnings:
Generated actions inspected; missing or incorrect actions/tokens:
Native setup or repairs made:
Input / existing setlist sequence / requested sequence:
Observed archive, scores, setlist sequence and report:
Cancellation / interruption observations, if applicable:
Result: pass / fail / partial / not run:
```

After a failed checkpoint, fix the first failing boundary and repeat that case plus directly affected earlier cases. Do not rerun unrelated diagnostics. A focused probe is warranted only when the integrated failure cannot be understood without isolating it.

**Next work:** You compile, inspect and run stage 2A using the [one-file checkpoint](jelly/tests/v3/README.md). Report the first error or the actual preview, plus any native repairs. Then extend the new shared parser/config with actual week-folder examples, dates and numeric ordering before continuing into the independent V3 assembly. No legacy implementation is a prerequisite.
