# Shortcut inventory and installation order

## V4 Check or Upload (10 November 2026)

Install **V4 - Create Service**, [source](../shortcuts/main/v4-create-service.jelly),
revision 2/interface 1.0, after the completed working **V4 - Check or Upload**.
The creator accepts multiple shared PDFs or opens Files, asks for date/service,
and reuses or creates an exactly named setlist with additions only. Complete
DATE01 and SFS01-SFS04 natively. Revision 2 sends [PDF, batch] and appends Scores
one at a time in received order. Prior installed creator works by user report
after opening forScore and retrying; revision 2 changes are source reviewed only.
See [setup, limitations and manual checks](v4-create-service.md).

**V4 - Check or Upload**, [source](../shortcuts/reusable/v4-check-or-upload.jelly),
revision 2/interface 1.1, has no installed shortcut dependencies. It accepts one
shared PDF or offers Files on direct launch; an optional second Text item `batch`
suppresses report display. Native forScore lookup/import/metadata/return slots
must be completed before use. Intended success result: native List [Score, report Text];
controlled early exits return diagnostic Text with a V4-E or V4-SETUP code.
Source reviewed; user reports the manually completed installed copy runs successfully
after reselecting Repeat Item and setting sourceFile references to File
(10 November 2026). Regenerated wiring and the broader acceptance matrix remain
unverified. See the
[setup and manual checks](v4-check-or-upload.md). V3 and legacy sources are unchanged.

## V3 installation order (7 November 2026)

Standalone minute workaround diagnostic: **TEST - V3 Adjust Date Minutes**, [source](../tests/v3/t02-adjust-date-minutes.jelly), revision 1/interface 1.0, no dependencies or setup slots. Adds 1440 min to a fixed extracted Date and returns a timestamp report. User-reported matching fixed-date output: 9 November 2026 at 12:00 to 10 November at 12:00, both Date counts 1; no repair reported, native fields/version details unspecified. Production behaviour is unchanged.

Standalone duration diagnostic: **TEST - V3 Adjust Date Unit**, [source](../tests/v3/t02-adjust-date-unit.jelly), revision 1/interface 1.0, no dependencies or native setup slots. Compares independent 1 day and documented 10 min adjustments with seconds visible; see [run instructions](../tests/v3/stage-2b-probes.md#duration-binding-investigation-9-november). Source reviewed only; no compilation or execution recorded.

9 November: eight independent **TEST - V3** Stage 2B probes are listed with exact names, source paths, setup and expected results in the [probe inventory/run sheet](../tests/v3/stage-2b-probes.md). They have no installed helper dependencies and do not change production installation order. Compile/import each separately through Copyover; native fixture slots are documented beside their actions. Source review only; no compilation or execution recorded.

V3 is independent of every legacy Shortcut below. Install only:

1. **V3 - Parse Filename**, [source](../shortcuts/reusable/v3-parse-filename.jelly), interface 2.0, no installed dependencies.
2. **V3 - Preview Filenames**, [source](../shortcuts/main/v3-preview-filenames.jelly), interface 3.0, calls V3 - Parse Filename 2.0.

Stage 2B adds (source-reviewed only; iPad acceptance pending):

3. **V3 - Resolve Folder Dates**, [source](../shortcuts/reusable/v3-resolve-folder-dates.jelly), revision 4/interface 1.0, no installed dependencies. Optional-capture Match checks now consume nonempty prefixed Text. Current Date remains at the top via Set Variable currentDate. Required-parameter failure's exact action remains unknown; candidate awaits device check. Guide offers three manual edits preserving installed Date wiring, or replace only this helper and complete the top-level Date slot.
4. **V3 - Load Folder Context**, [source](../shortcuts/reusable/v3-load-folder-context.jelly), revision 1/interface 1.0, calls Resolve Folder Dates 1.0; owns the separate context read/save/readback.
5. **V3 - Prepare Preview Rows**, [source](../shortcuts/reusable/v3-prepare-preview-rows.jelly), revision 1/interface 1.0, calls Parse Filename 2.0; no native objects/writes.
6. **V3 - Render Service Preview**, [source](../shortcuts/reusable/v3-render-service-preview.jelly), revision 1/interface 1.0, no dependencies/writes. Compile this small component first as the focused crash checkpoint; dependency order among independent helpers is otherwise flexible.
7. **V3 - Preview Services**, [source](../shortcuts/main/v3-preview-services.jelly), revision 2/interface 1.0, calls Load Folder Context, Prepare Preview Rows and Render Service Preview 1.0. Keep working filename preview/parser unchanged.

Preview Services revision 1 crashed on editor loading AND at Compile Jelly Text by user report. Its [source is preserved](../tests/v3/fixtures/v3-preview-services-revision-1-crash.jelly). Revision 2's split is an unverified workaround; no byte limit/root cause or compiler pass is claimed. Main retains native folder access; helper transport is Text JSON only. Config/date resolver are unchanged. Context read/save settings moved into Load Folder Context.

Use the complete updated version-3 config and [Stage 2B setup/checkpoint](../tests/v3/stage-2b-services.md). The new preview reads one folder, groups dated occurrences and sorts numeric positions; its only write is a separate saved-date context JSON. Current Date, fixed config File and single-folder picker have three native setup slots total. Inspect the common Get/Save File base folder and date/numeric settings. No forScore, archive, metadata, setlist or legacy dependency is introduced.

Stage 2A sources remain parser revision 3 and filename preview revision 6. Parsing, report cleanup, config persistence/rereading, Thursday aliases, conflict and version-error checks now have user-reported passes; see the latest evidence rather than older pending notes. Exact source hashes/raw return types and broader matrix cases remain unverified. Preview revision 3 has a reported false no-selection result. They use normal completion, with no manual stop blocks; see [output resolution](v3-output-resolution.md). Revision 1 has a reported Notes-action generation failure. Use the separate
[v3 config](../config/v3-config.example.json), [contracts](v3-development.md)
and [manual checkpoint](../tests/v3/README.md). No local builds or tests are run
under the user's current instructions. Names are exact Copyover targets; no
rename of an old installed Shortcut is needed. The inventory below is legacy.

Planned metadata utility, not yet implemented or installed: **V3 - Resolve Composer**. It will accept one approved name Text and return a native Composer by lookup or creation. Install/verify it before the future V3 assembly caller; current filename previews do not call it. See the [contract](../../nextcloud-forscore-plan-v3.md#shared-utility-v3---resolve-composer).

4 November 2026: optional independent [generation test groups](../tests/ipad-investigation/generation-groups.md)
are available. The checklist owns exact installed TEST names, inputs and
dependencies. G3 Exit Echo/Context receivers install before their three callers;
G2C requires a temporary native two-Score fixture caller. None is a production
dependency. Production names/contracts and installed shortcuts are unchanged.

**28 October Genre draft: Canonical 11 / Archive 17 (interface 2.2) / Assembly 18
(launch interface 1.1) / Main 4.** Assembly now requires Archive's optional
`with-category` output. Complete/test Archive category mode before enabling that
caller. Legacy callers, including the append draft and functional archive tests,
continue using three items and receive a PDF; they do not gain Genre assignment.
GEN01-GEN03 and CFG03C/CFG04C are native completion slots, not verified generated
actions. Both local builds fail the recorded older-profile diagnostics. Preserve
working installed helpers; follow the [Genre guide](ipad-genre-update-guide.md).

Latest installed result, 28 October: user confirms matching names allow replace
or skip replacement in `2-util-assemble-choir-service`. Preserve that working
installed helper; no caller/dependency changes or reimports are needed. Remaining
checks are in the [service test record](../tests/choir-service.md). This validates
the reported installed path, not a fresh Assembly 17 export.

Historical installed result, 27 October: user confirms clearing now works after
correcting `TestReplace existing` to `Replace existing` in the installed If.
Active helper/caller names remain unchanged; backup is
`2-util-assemble-choir-service 2`. No dependencies need reimporting. Remaining
native edits are in the [installed update guide](ipad-assembly-update-guide.md).
This supersedes the unresolved-clearing status below, without validating all
replacement/order regressions or the proposed name-based lookup.

**27 October 2026: Assembly source revision 17; interfaces unchanged.** Active
iPad caller is confirmed as `test-assemble-service` ->
`2-util-assemble-choir-service`. A/B -> B/A replacement failed the readback guard;
actual entries are A/B/B/A; old entries remained before appending B/A. Revision 17 replaces the mode/target choosers
with a native exact-name resolver slot FS09, TARGET01 unique-match extraction and
direct FS08 target assignment; Get setlist Name and Continue if not found fields are confirmed; matching behavior needs checking. FS10R now verifies zero entries after clearing, before appending.
Metadata prompts show piece identity and count errors show numeric operands.
Source is not a repaired/validated installed replacement. Preserve native edits;
follow [latest repair instructions](ipad-assembly-lessons.md) before regeneration.

**Current, 23 October 2026: Canonical 11 / Archive 16 / Assembly 16 / Main 4.**
Assembly 16 adds adjacent repair/check comments without changing executable flow.
The user's completed installed one-score service now populates and opens its
setlist, with subsequent native date/default and New Setlist changes confirmed.
These native edits are not round-tripped by regeneration; see
[the repair record](ipad-assembly-lessons.md). Wider regressions remain untested.
Assembly 15 replaces its score lookup/import Otherwise branch with two complementary
presence checks after user-reported duplicate magic-variable errors. User confirms
Assembly 15 compiled on the iPad; later repaired execution has the limited scope
recorded above. See [compatibility evidence](../tests/compatibility/README.md).
Archive/Assembly now use the user-confirmed Text interpolation form in all three
naming Lists. Native object Lists and slot requirements remain unchanged.
Preserve the working repaired Archive 15; regeneration restores guards/native
slots. See [List evidence and migration](../tests/compatibility/list-variable-transport.md).
Both updated full local builds still fail the recorded older-profile diagnostics.

**Archive 15 update, 21 October 2026:** ARC01-ARC03 manual extraction is replaced
in source by a quoted-index loop, with Nothing-initialized native variables.
Mixed File/Folder/Dictionary preservation is still unverified on the iPad; run
[the read-only context test](../tests/compatibility/archive-context-loop.md).
CFG02-CFG04 remain manual. Preserve the working installed archive and keep the
new initial guard until native extraction and CFG completion are checked.
Earlier ARC instructions below describe revision 14 and are superseded for 15.

**Current, 21 October 2026: Canonical 11 / Archive 15 / Assembly 13 / Main 4.**
See [the pre-iPad review](pre-ipad-review.md) for implemented fixes, preserved
archive repairs and required checks. Interfaces remain 2.0 / 2.1 / 1.1 / 1.0.
The revision paragraphs below are historical; they do not override this review.

**Current source: Archive 14 / Assembly 11.** The user confirms the small flush-left, parenthesized If probe returns Conditional output reached. The indented parenthesized probe dropped its Output; the unparenthesized probe dropped its If. Both helpers now keep code flush left and use positional `output("ERROR: ...")`, with no notes: label. Literal multiline message whitespace is preserved. Warnings about missing noResultBehaviour and response remain unresolved: the successful probe is not warning-free. This establishes only the tested conditional stop/Text fixture, not interpolation, File returns, nested loops or either complete helper. Existing native ARC/CFG/CONF/COL/SCORE/FS completion remains; no native validation construction is required.



Current archive 9 / assembly 7: follow the [18 October compatibility checklist](helper-compatibility-update.md). Its native selector/collection slots and Exit returns supersede older selector, Output-field and Repeat Results instructions on this page.

Source headers own contracts and direct dependency details. This table is the navigation summary; update it alongside source and test records.

| Installed name / source | Role and purpose | Direct dependencies | Interface | Stage |
| --- | --- | --- | --- | --- |
| [UTIL - Jelly Format Greeting](../examples/util-jelly-format-greeting.jelly) | Example reusable utility: format one name, default to Friend | None | 1.0 | Syntax reviewed |
| [MAIN - Jelly Greeting Demo](../examples/main-jelly-greeting-demo.jelly) | Example main: pass Henry to utility and return its result | UTIL - Jelly Format Greeting, interface 1.0 | 1.0 | Syntax reviewed |
| [UTIL - Canonical Choir Name](../shortcuts/reusable/util-canonical-choir-name.jelly) | Configured canonical name from a two-Text List | None | 2.0 | Drafted |
| [UTIL - Archive Choir PDF](../shortcuts/reusable/util-archive-choir-pdf.jelly) | Config-based archive with native context List and CFG slots | UTIL - Canonical Choir Name, interface 2.0 | 2.1 | Drafted skeleton; older completed installed copy has user-reported save/reuse repairs |
| [UTIL - Assemble Choir Service](../shortcuts/reusable/util-assemble-choir-service.jelly) | Load config once, prepare service; CONF/FS slots | UTIL - Canonical Choir Name 2.0; UTIL - Archive Choir PDF 2.1 | 1.1 | Drafted |
| [MAIN - Build Choir Service](../shortcuts/main/main-build-choir-service.jelly) | Generated interactive production entry point | UTIL - Assemble Choir Service, interface 1.1 | 1.0 | Drafted |

External provider apps/services: None for the example actions. Jellycuts or a compatible compiler is a build tool; Apple Shortcuts is the runtime. Current user-reported target: Jellycuts 2026.6.4 on iPadOS 26.6; no successful compilation or runtime validation is recorded for these sources.

1. Compile/export the utility, inspect generated actions, import it, and confirm its installed name is exactly `UTIL - Jelly Format Greeting`.
2. Run the utility's direct test. Record results without claiming the complete integration is verified yet.
3. Compile/export/import the main under `MAIN - Jelly Greeting Demo`. Confirm its Run Shortcut points to the installed utility and passes the intended Text variable.
4. Execute [all example tests](../tests/examples.md), including the changed-input integration case.

There is no cycle: main depends on utility; utility does not depend on main. Using the main to test the utility does not create a utility runtime dependency.

The app version is user-reported; bundled compiler/library revisions and installed source revisions remain unconfirmed. Dependency comments and interface versions do not enforce runtime compatibility. Missing or renamed utilities may halt Run Shortcut rather than return a recoverable error. Check exact names and contracts before launch; do not claim a runtime catch is implemented.

Optional independent diagnostic Shortcuts are inventoried in [compatibility tests](../tests/compatibility/README.md). They are not dependencies of examples or production sources.

The independent local-compiler smoke Shortcut, `TEST - Local Compiler Hello`, is
inventoried with its source, contract and validation evidence in
[compiler tests](../tests/compiler/README.md). It has no installed Shortcut
dependencies and is not a dependency of any production component.

## Choir service installation order

The [production build guide](choir-service-build.md) owns configuration, scope and the complete install sequence: canonical naming utility, archive helper, assembly helper, main. All four now have Jelly source. Use the current [config contracts](config-integration.md); complete archive CFG02-CFG04 and service CONF01-CONF02/FS01-FS13 using [the assembly guide](choir-service-assembly.md) before removing the two initial guards. No cycle: main calls assembly, assembly calls archive and canonical, archive calls canonical. Examples and the old diagnostic are not dependencies.

Production target reported by the user: iPadOS 26.6, forScore 15.2.5, Jellycuts 2026.6.4. Bundled compiler/action-library versions and all new export/import/device results remain unverified. Configure the signed-in Nextcloud Files location and existing iCloud archive root; permissions are requested by native actions. Record the single integrated run in [choir-service tests](../tests/choir-service.md).

Optional short test drivers and installation/input contracts: [functional tests](../tests/functional/README.md). These are not production dependencies.
