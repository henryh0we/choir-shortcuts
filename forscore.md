# forScore integration guidance

Documentation checked **2026-10-14**. Apply this file alongside [Jelly agent rules](jelly/AGENTS.md) and [manual-build rules](manual%20creation/AGENTS.md). The user has an **iPhone and iPad only**: provide an entirely on-device workflow; do not require a Mac, Homebrew, desktop compilation, or desktop signing. Jellycuts authors/compiles Shortcut source; Apple Shortcuts runs it and communicates with forScore. Jellycuts does not create a standalone iOS app.

Existing repository examples demonstrate native `runShortcut` composition, not forScore integration. The user has now supplied [the installed forScore action inventory](forscore%20shortcut%20actions.md), reviewed here on **2026-10-14**. It establishes user-reported action availability; expanded settings, input/output contracts, compilation, and execution remain unverified. This file establishes integration guidance, not an installed Shortcut project.

Current project context, as reported by the user: **iPadOS 26.6**, **forScore 15.2.5**, **Jellycuts 2026.6.4**, and a **signed-in Nextcloud account visible in Apple Files Locations**. The forScore library is empty. Reuse the existing iCloud `Choir Music/Library` type folders for clean PDFs and keep one current forScore library for working scores. The updated design is [Service Shortcut Draft V2 revision 2.1](nextcloud-forscore-plan-v2.md); [V1](nextcloud-forscore-plan-v1.md) remains the historical baseline. [Screenshot evidence](forscore-action-evidence.md) records visible settings separately from unverified runtime behaviour.

## Verify first

For each required capability, check [official Jellycuts documentation](https://docs.jellycuts.com/) and [forScore automation documentation](https://forscore.co/developers-automation/). Record iOS/iPadOS, forScore, and Jellycuts versions, review date, exact source, and evidence stage. Check the actual Jellycuts build's action libraries, signature, expanded parameters, enums, and input/output types; native Shortcuts availability alone does not establish generation support.

Do not invent a forScore import/library, internal action identifier, function signature, parameter, object type, or return value. forScore is not listed in the reviewed [Jelly library list](https://docs.jellycuts.com/Language_Guide/importing.html); this establishes no verified binding, rather than proving all versions lack support. Recheck when tools change.

Treat actions, action information, expanded options, and selectable variables visible in the user's Shortcuts editor as evidence for that installed version. Record exact names/configuration and confirm outputs through execution. Separate **documentation/source verified**, **proposed design**, and **awaiting device testing**. When missing details block a specific step, continue independent work and ask for the exact action name, expanded settings, input/output description, or screenshots needed. Do not silently fill gaps with guesses.

## Capability matrix

The URL rows below are documentation-confirmed. Native rows are based on the user's installed-action inventory and screenshots: availability is user-reported and some settings are editor-visible, while full contracts and runtime behaviour remain unverified. Preserve the spelling in the inventory when citing a catalogue label; distinguish it from the expanded wording recorded in [screenshot evidence](forscore-action-evidence.md). The inventory contains mixed capitalisation and `get dificulty`. Do not treat a transcribed label as an internal action identifier or a Jelly function.

| Capability | Integration method | Evidence/source | Verification status | Limitations |
| --- | --- | --- | --- | --- |
| Open score by filename | `forscore://open?path=My%20Score.pdf` | [forScore automation](https://forscore.co/developers-automation/) | Documented; device not tested | Targets library filename, not an arbitrary Files path; no result receipt |
| Open named setlist | `forscore://open?setlist=Sunday` | Same official page; Sunday is an illustrative name | Command documented; device not tested | Requires matching content; no query result |
| Advance page | `forscore://action?type=nextpage` | Same official command table | Documented; device not tested | Current-view dependent; repeated calls advance again |
| Call an installed helper | Jelly `runShortcut(name: ..., input: ..., show: false) >> result` | [Official binding](https://docs.jellycuts.com/Documentation/Shortcuts/runShortcut.html), [local compiler evidence](jelly/docs/jellycuts-reference.md) | Syntax/source reviewed; local examples uncompiled | Exact installed name and native data transfer need testing |
| Retrieve and match existing scores | Prefer `Get score named Name`; other retrieval/filter actions for diagnostics | [Action inventory](forscore%20shortcut%20actions.md), [device evidence](forscore-action-evidence.md) | User confirms known PDF stem finds the score and nonmatching name finds none, 2026-10-15 | Filename versus title after rename, duplicates, case rules, scope and exact absence representation remain unverified |
| Import missing PDFs | `Import file(s)`, `Import score(s)`; `add scores to library` separately | User action inventory | Availability reported; contracts/runtime unverified | Determine which import consumes native Files and returns imported scores; library assignment is not assumed to import |
| Composer and tags | `Find composer`, `Create composer`, `Find tag`, `Create Tag`, `add metadata`, `Check for metadata`, `get composers`, `get tags` | User action inventory | Availability reported; contracts/runtime unverified | Verify object versus Text inputs, search ambiguity, metadata categories, add/replace behaviour, and reads after writes |
| Title and reference | `Rename score`, `get reference`, `set reference` | User action inventory | Availability reported; contracts/runtime unverified | Distinguish display title from disk filename; reference meaning/type is unknown and must not be assumed to store arbitrary provenance |
| Create or retrieve service setlists | `new setlist`, `Get all setlists`, `Get setlist`, `Rename setlist` | User action inventory | Availability reported; contracts/runtime unverified | Verify naming, library scope, returned setlist object, and duplicate-name behaviour |
| Populate and inspect ordered services | `add scores to setlist`, `add entries to setlist`, `Get setlist entries`, `Sort Setlist Entries` | User action inventory | Availability reported; contracts/runtime unverified | Verify append/insertion order, sort options, and repeated-score support; a sort action may not support arbitrary running order |
| Reconcile setlist entries | `remove setlist entries`, `Remove all setlist entries`, `Duplicate Setlist` | User action inventory | Availability reported; contracts/runtime unverified | Verify exact target/type and update policy; do not clear an existing service before replacements are ready |
| Open service or score natively | `open setlist`, `Open score`, `open setlist entry` | User action inventory | Availability reported; contracts/runtime unverified | Check required object type, foreground behaviour, and whether any confirmation is returned |
| Jelly generation of listed native actions | Direct generation if verified; otherwise manually built native helper | Actual Jellycuts compiler libraries required | No binding verified | Native availability does not imply generation support |
| Pass forScore objects between Shortcuts | Native input/output without serialization | Individual helper and caller tests required | Unknown | Identity/type preservation and caller consumption unverified |

Keep statuses granular: documentation confirmation is neither compilation nor successful operation on a device. Update evidence after each compiler/app change.

## Use the supplied action inventory

The [inventory](forscore%20shortcut%20actions.md) is the authoritative transcription of the user's listed actions. It also covers bookmarks, placeholders, automation URLs, format conversions, metadata categories, cropping, duplication, setlist folders, library movement, removal, renaming, entry-to-score conversion, and sorting. Keep that file intact as evidence rather than replacing it with a corrected or inferred action catalogue.

For the Nextcloud service workflow, prefer native retrieval/filtering, one verified import path, metadata assignment, and native setlist operations. URL navigation and Open Setlist files are fallbacks where needed, rather than the primary library-management route. Do not equate `convert text to 4ss` with accepting the documented XML format without inspecting its contract.

Inspect these action groups first:

1. `Get score named Name`: the user confirms a known PDF stem finds its score and a nonmatching name finds none. Use the complete canonical payload without `.pdf`. Next establish rename effects, duplicate names and scope. Selecting the first item of Get all scores is not identity matching. The native Score exposes no additional properties in the user's reported variable editor.
2. `Import file(s)` / `Import score(s)`: establish File inputs, PDF handling, collision policy, output cardinality and actual imported filename. Choose one path; never run both on the same PDF as a routine sequence.
3. `Rename score` / `Find composer` / `Create composer` / `add metadata` / `get composers`: distinguish title from filename and category objects from Text, then verify a write by reading the same score.
4. `Get all setlists` / `Get setlist` / `new setlist` / `add scores to setlist` / `Get setlist entries`: establish setlist identity, duplicate-name handling, ordered insertion and repeated entries.
5. `remove setlist entries` / `Remove all setlist entries` / `Sort Setlist Entries`: establish safe updates only after creation and readback work. Prefer comparing entries over clearing everything.
6. `open setlist`: test final navigation separately from write confirmation.

No automatic composer expansion, arbitrary reference storage, reliable filename renaming, transactional update, or error-catching behaviour follows from the action names. Keep native objects in native variables. Use `get score from setlist entry` or `get scores from setlist entries` only when their actual input/output types have been checked; a score and a setlist entry are different concepts.

## Screenshot settings and clean archive policy

The supplied screenshots show Library and Sort Order: Title for score retrieval; Filter Scores fields for composer, genre, tag, label, reference, rating, difficulty and key, with Rule: Match All. They do not expose filename/title filtering. Verify exact identity through score properties or a suitable tested field instead of assuming a filename filter exists.

The two import cards both display Import Files with Conflict Handling: Skip; their catalogue identities and outputs remain unresolved. Rename exposes Scores and Name without establishing whether it changes the title or physical filename. Add metadata exposes Composers, Genres, Tags and Labels.

Composer lookup exposes Continue if not found, currently off. Enable it for a proposed missing-composer branch only after testing the resulting output. Create composer visibly supports adding directly to Scores and/or Bookmarks. Setlist creation exposes a Folder field. Adding scores exposes Skip if already added, currently off; use a tested skip policy for retries and separately test deliberate repetitions. Get entries exposes Sorting: Manual; this establishes a readback option, not append/reorder semantics.

Save the source PDF as supplied by Nextcloud in the existing clean iCloud type folder before working-copy import or metadata modification. Mirror type through forScore genres; use setlists for services. Resolve archive presence and forScore presence independently: a missing archive may require a Nextcloud download even when forScore already has the score; a present archive can supply a missing working score without downloading again. Do not overwrite revised sources or existing annotated scores automatically. Keep the actual imported identity in a persistent mapping, especially if Rename changes the filename.

forScore has native iCloud syncing, separate from this clean-folder archive. A full 4SB archive also retains private app data that plain PDFs do not. Keep backup creation manual until a supported automation action is established. [Sync documentation](https://forscore.co/documentation/sync/), [backup and archive documentation](https://forscore.co/kb/understanding-backups-syncing-and-icloud/).

## Choose a hybrid architecture

The user has requested implementation without further isolated action tests and now explicitly prefers generating every Shortcut with Comment slots for unsupported actions. Use [the build guide](jelly/docs/choir-service-build.md) and [slot assembly guide](jelly/docs/choir-service-assembly.md): all four have Jelly source. Insert native forScore actions after export, complete archive Folder/save/return fields, and reconnect outputs. This user-authorized route supersedes the default preference below for separately hand-built helpers. Remaining settings are integrated construction checks, not reasons to stop. Existing diagnostics are evidence, not required dependencies.

Implement supported menus, branching, loops, validation, processing, and orchestration in `.jelly` files, one installed Shortcut per file. Prefer direct forScore bindings only after verifying them in the actual compiler and on-device runtime. The default is to isolate unsupported actions in native helpers; for this project the user's explicit Comment-slot instruction takes precedence. Keep inserted actions confined to the generated assembly helper, document every insertion and native output connection, and preserve/reapply those edits on regeneration.

Store helper specifications under `manual creation/shortcuts/reusable/` when first needed, using the repository's lowercase filenames and `UTIL - <Verb Phrase>` installed names. Keep their installed names distinct from generated workflows and examples. Generated sources remain under `jelly/`; regenerate/replace only their own installed Shortcuts. Never overwrite manual helpers during export/import.

Each helper should have a coherent responsibility and be directly runnable when useful. Define explicit interactive mode if prompting differs from called use; missing input does not identify launch origin. Keep dependencies acyclic and link helpers from caller headers and the [dependency inventory](jelly/docs/dependencies.md). List native helpers and generated dependencies in dependency-first installation order, with required interface versions.

Use the reviewed `runShortcut` binding to pass a variable and capture output, following the [existing composition example](jelly/examples/main-jelly-greeting-demo.jelly). Its formatter/return pattern does not prove arbitrary forScore object support. Preserve native objects where required; do not stringify, interpolate into Text, convert to JSON, or reuse a Text-only output binding for those objects without testing. A Dictionary may carry several named inputs, but its entry types and the caller/helper boundary must also be verified.

## Helper contracts and manual construction

For every helper, supply the template below with complete real actions, exact variable sources, and expanded settings. Use the preferred bracketed/indented blueprint style, with **numbered assembly steps** for forScore helpers. These numbers are documentation references, not editor values. Generated Otherwise/End If/End Repeat markers must be identified as automatic, rather than actions to search for.

Specify missing input, cancellation, no matches, duplicate matches, failure, permission prompts, user interaction, and foreground requirements. Mark unverified behaviour explicitly. If an action returns no confirmation, report no confirmed operation result: never manufacture `success: true` just because control continued. A returned validation error cannot catch an action failure that stops execution. State intentional output and no-output behaviour so a caller does not accidentally consume another action's result.

Keep user settings in one documented configuration location per project, such as a designated configuration helper or a clearly labelled configuration section in one source. Record where/how to change each value, its native type/default, and whether recompile/reimport is needed. Use that same configuration across callers; do not require repeated edits to imported generated actions. Keep credentials and private library contents out of committed examples.

## URL navigation

Verify command/parameter spelling before constructing a link. The documented `open` command uses `path` for filename and `setlist` for name; `action` accepts `nextpage`. Content references may fall back from exact to case/diacritic-insensitive matches; missing content can fail silently. Duplicate-name resolution must be tested rather than assumed. [Official URL reference](https://forscore.co/developers-automation/).

Encode **individual parameter values**, then combine them with literal scheme, command, `?`, `&`, and `=` separators. Do not encode the whole URL or double-encode already escaped input. Test spaces, `&`, `+`, `#`, `%`, apostrophes, and non-ASCII names; match the received content exactly. Verify the selected Jellycuts/native encoding action and settings before using it; a generic encoding function name is not enough evidence of correct query-component handling.

URLs are navigation requests, not a general library-query/editing API. Opening a URL proves no successful content lookup or modification. Use native actions when structured output or another unsupported URL capability is needed. Account for forScore becoming foreground, the current view, missing content, and unknown return-to-caller behaviour. Do not assume URL callback support or automatic success confirmation.

## Compile, install, and update on iPhone/iPad

1. On the target device, record app/OS versions and inspect needed forScore actions in Shortcuts. Create manual helpers from their numbered specifications, using exact installed names. Test each independently.
2. Open/transfer each `.jelly` file into Jellycuts using Files or its supported import flow. Complete the app's Shortcuts connection/onboarding if needed. The [official first-script tutorial](https://docs.jellycuts.com/Getting_Started/writing_first_script.html) documents the app-based export route.
3. Compile in Jellycuts and read its diagnostics. Fix source against that app's actual bindings. Export/import through the supported on-device flow, dependency first. Menu labels may vary; obtain the specific screen/details if the route fails rather than prescribing a Mac fallback.
4. Inspect imported actions, native variable connections, input types, helper selections, and exact installed names. Resolve app/permission prompts. If the current export/import/signing route fails, document its error and determine a supported on-device route before claiming import success.
5. Run the small end-to-end integration. For updates, change configuration/helper/source in its owning location, recompile/reimport affected generated files, preserve manual helpers, and rerun affected tests. Document migrations for interface/name changes and protect useful installed edits.

## Validate incrementally

Start with one small, non-modifying end-to-end case chosen for the user's actual task. Test the native helper alone, then its generated caller, before adding a large workflow. Cover known and missing content, spaces/punctuation, duplicate names, cancellation when applicable, direct/called execution, and repeated execution. Record current/foreground app and any interaction needed. Use disposable data for modifying actions; define duplicate detection or another verified retry policy before retrying. Never assume a timed-out or unconfirmed write did nothing.

Record source revision, compiler/app versions, diagnostics, import outcome, exact installed name, device/OS, date, tester, expected/actual outputs and side effects. Use the Jelly stages **Syntax reviewed → Compiled → Imported → Tested → Verified** and manual-helper stages from its AGENTS.md. Failed tests remain evidence. No stage may be promoted merely because design seems correct.

## Manual helper template

This is a documentation template, not an implemented helper. Replace all placeholders, verify every action, and remove instructional placeholders before publishing a build specification. Put clickable dependency/source links outside its text block.

```text
<HELPER DISPLAY TITLE>
========================
Shortcut name: <Exact installed UTIL - name>
Purpose / when to use: <One responsibility>
Revision / interface: <Versions>
Input: <Native type, cardinality; required/optional fields and defaults>
Example input: <Concrete safe example; preserve object types>
Output: <Actual native type/value, or no confirmed result>
Example output: <Evidenced example, or unavailable; do not invent success>
Direct execution: <Useful default/prompt or unsupported>
Called execution: <Input, UI, output differences>
Dependencies / build order: <Exact names, versions, linked specs>
Configuration: <Single owning location, settings, update procedure>
Permissions / interaction / foreground: <Verified needs or unknowns>
Missing / cancellation / no matches / duplicates / failures: <Policy>
Status / device / OS / forScore version: <Evidence and unknowns>

========================
NUMBERED ASSEMBLY
========================
1. Create the Shortcut using the exact name above; configure entry input.
2. [<Verified native action name>]
   <Exact parameter>: <Literal, menu choice, or selected variable>
   <Expanded setting>: <Exact value>
   NOTE: Select <complete token/type/property> from <specific source
   step/action>. Notes are documentation, not actions.
3. <Continue with every required action, branch/loop marker, and exit.
   Indent nested actions four spaces; identify automatic markers.>
4. <Specify actual return/no-output behaviour and its native wiring.
   Do not assume an arbitrary object survives Text conversion.>

========================
EXPECTED TEST RESULTS
========================
Prerequisites: <Apps, helpers, safe library fixtures, permissions>
T1 - Direct execution: <Exact launch/input>
-> <Observable output and side effects>
Actual result: Not run
T2 - Generated caller: <Exact source/revision, input and Run Shortcut wiring>
-> <Expected native result or observed operation; no fabricated receipt>
Actual result: Not run
T3 onward - <Missing/duplicate names, punctuation, cancellation, repeat/retry>
-> <Expected handling; identify unknown behaviour>
Actual result: Not run

========================
BUILD NOTES AND EVIDENCE
========================
<Variable-selection tips, limitations, restoration after diagnostic edits>
<Source links below; date checked; captured editor/settings evidence>
<Actual build/test results; tester/device/revision/date>
VERIFY ON DEVICE: <Specific unresolved capability and next check>
```

Outstanding checks: full input/output contracts and remaining settings for the native actions; direct generation support in Jellycuts 2026.6.4; native object transfer; permissions/foreground behaviour; app export/import; filename versus title identity; exact lookup without a visible filename filter; library selector choices; ordered entry updates and error/retry behaviour; existing iCloud root selection and provider-save behaviour. Versions, empty-library state, Nextcloud Files visibility and screenshot settings are now recorded. Resolve the remaining checks using editor and execution evidence. The linked generated sources are Drafted templates with completion slots; neither compilation nor installed operation is established by this guidance.
