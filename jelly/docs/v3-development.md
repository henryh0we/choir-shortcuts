# V3 implementation and contracts

7 November 2026. User direction: build from the ground up, use `V3 - ...` names, and do not depend on the old shortcuts. This supersedes the earlier migration/legacy-compatibility approach for new v3 work. No old shortcut needs backing up, updating or installing to use v3. Historical files remain as evidence, and existing music is not deleted.

Development sequence: [timeline](../../nextcloud-forscore-v3-development-timeline.md). Requirements: [v3 plan](../../nextcloud-forscore-plan-v3.md). Device instructions and results: [first checkpoint](../tests/v3/README.md).

Current source delivery: **parser revision 3/interface 2.0; preview revision 5/interface 3.0**, with guarded processing and natural completion; no manual stop blocks. See the [commit-history review and output resolution](v3-output-resolution.md). Revision 1 generated unwanted Move Notes actions by user report. The untested revision-2 manual-slot proposal is retired.

Latest device results: **reported one-file and four-file integration passes**. The four-file report correctly separates Sunam/Mattins, Sunpm/Evensong and bare Sun/Eucharist, skips Monday, extracts position 11 and preserves voice/verse qualifiers. Four selected items produced four report rows. Later individual reports also confirm Thur as Thursday Evensong and SunRemem as Remem/special-remem with the hymn payload preserved. Quote-pair display artifacts remain. See the [exact four-file evidence and limits](../tests/v3/README.md#reported-pass-four-file-sunday-and-monday-preview-8-november-2026). The latest consumed revision and saved-config persistence are not explicitly confirmed. No local build or runtime tests were run; wider acceptance remains pending.

## Current delivery

Stage 2A implements filename parsing and recurring-schedule preview only. The earlier Notes generation and false no-selection results remain historical failed attempts. The reported one-file/four-file results supersede their blocking status only for those fixtures, not all branches. Exact hashes, app versions, installed-source identities and repairs remain unconfirmed.

| Exact installed name | Source | Dependency | Interface |
| --- | --- | --- | --- |
| V3 - Parse Filename | [v3-parse-filename.jelly](../shortcuts/reusable/v3-parse-filename.jelly) | None | 2.0 |
| V3 - Preview Filenames | [v3-preview-filenames.jelly](../shortcuts/main/v3-preview-filenames.jelly) | V3 - Parse Filename 2.0 | 3.0 |

Planned names, not yet implemented: `V3 - Create Service`, `V3 - Weekly`, `V3 - Assemble Service`, `V3 - Archive PDF`, and `V3 - Resolve Composer`. Only add further installed helpers when reuse warrants them. V3 - Create Service is the new Share Sheet title; this supersedes the earlier unprefixed title. There is no implicit naming/archive dependency on `UTIL - ...`, `MAIN - ...`, `2-util-...` or any TEST shortcut.

## Configuration ownership

Copy [v3-config.example.json](../config/v3-config.example.json) to one user-controlled Files location as **v3-config.json**. Do not replace the legacy config. Preview revision 5 uses one fixed native File reference configured once after import at V3-CONFIG-FILE. It rereads that file each run without a config picker. See the [one-time setup](../tests/v3/README.md#current-setup-preview-revision-5-saved-config-file). Only the selected file supplies rules; neither source embeds a second copy.

The config uses version **3**, independently of interface and result versions. Enable switches are literal Text **on/off**, not JSON Boolean values. This avoids assuming how native Boolean coercion is represented by the current action bindings. Malformed JSON or invalid regex may halt a native action; no catch mechanism is claimed.

Editable sections are ordered as required by the plan. This delivery implements `filenameFormats.rules`, the fixed case-insensitive terminal PDF extension rule, and recurring `weeklySchedule` day/slot switches/names only. `weekFolderDates`, `setlistNaming`, dated overrides, storage and categories reserve the shared settings for later increments; they do not affect current execution. The empty folder-format list is deliberate: do not guess a date convention from an unspecified folder name.

Every filename rule has a unique `key`, an anchored `pattern`, canonical `dayKey`, stable `slotKey`, and Text `special` switch. Rule capture groups must be:

1. Regular prefix, or the readable suffix for a special service.
2. Positive numeric position (no zero or leading zero in these initial defaults).
3. Complete identity-bearing piece payload.

Use noncapturing groups for internal alternatives. Only terminal `.pdf` is removed, case-insensitively; an extensionless Name is also accepted because Files name details may omit the extension. The parser does not trim or reinterpret the payload, expand composers or discard edition/movement qualifiers. The preview separately checks File Extension equals PDF; this is filename classification, not content/MIME validation.

All rules are examined. Exactly one match is required. Zero matches are unresolved; multiple matches are unresolved with empty parsed fields, rather than silently taking one. Explicit Sunday rules precede the special fallback, whose negative lookahead excludes am/pm mappings. Thursday special names initially require the longest alias, `Thurs`, so the fallback cannot interpret `Thurs1` as `Thu` plus suffix `rs`, or consume the R in `ThuRemem` as part of `Thur`. Shorter Thursday special prefixes remain unresolved until a boundary convention is agreed. If adding a convention creates overlaps, make the rule boundaries disjoint; rule order alone is not permission to guess.

Initial defaults remain candidates for the user's real naming conventions: Sun = Eucharist, Sunam = Mattins, Sunpm = Evensong; alphabetic special suffix, positive integer, hyphen, nonempty payload. Special suffix spelling is preserved for display; its lowercase form with the configured `special-` prefix becomes the stable slot. Monday and Wednesday are disabled by default. Wednesday has no regular rule/slot, but an alphabetic special suffix can be recognised and reported skipped. Adding a regular Wednesday mapping requires both a rule and a slot.

Config editing can add rules or change aliases/separators without modifying loops, provided the same capture contract is retained. Case-sensitive parsing and non-PDF terminal extension conventions are explicitly rejected by this increment. Date-specific exclusions cannot be evaluated before date resolution; this preview must not be treated as authorization to process a service.

## V3 - Parse Filename interface 2.0

Input: exactly two **Text** List items, in order: filename and full v3 config JSON snapshot. This is intentional Text transport of configuration data only; it does not serialize native music Files. The helper is called without prompts. When its receiving settings allow missing input, direct launch returns a Dictionary with status=error and an explanatory reason. Native receiving rules may stop before source execution.

Output on controlled success or validation failure: one native Dictionary, built from a static JSON template plus Set Dictionary Value actions. All result values are **Text**, including numeric position and schemaVersion:

| Field | Meaning |
| --- | --- |
| schemaVersion | `2` |
| status | `parsed`, `skipped`, `unresolved` or `error` |
| sourceName | Original supplied name |
| ruleKey | Unique matched rule; empty for unresolved match count |
| dayKey | mon/tue/wed/thu/fri/sat/sun |
| serviceSlot | Configured stable slot, or special suffix slot |
| serviceName | Configured regular name, or readable special suffix |
| position | Positive integer Text; later sorting must convert numerically |
| canonicalName | Full payload without prefix or terminal PDF extension |
| reason | Explanation; explicitly states this is not date-resolved |

Skipped rows keep their parsed identity/payload so exclusions can be explained. Unmatched/conflicting rows have empty parsed fields. Invalid input, unsupported config version/settings, incomplete rules or invalid extraction set status=error and reason, clear parsed fields, and skip dependent phases. There is no ERROR Text alternative return. A native JSON/regex/action failure may terminate without returning. This is focused validation, not a complete JSON schema validator; user-authored regex capture meanings still require inspection.

Native Dictionary creation, dynamic Set Dictionary Value interpolation, lowercase generation and the normal-completion Dictionary result remain unverified for this V3 revision. The helper ends with Get Dictionary from finalResult; the caller must receive that native Dictionary. No output/exit binding or manual native stop insertion is used. See the focused checkpoint before assuming the whole-shortcut result boundary works.

## V3 - Preview Filenames interface 3.0

Direct launch only; ignores incoming input. Shows a cancellable explanation, reads its configured native config File and selects multiple music Files. Its single native File-reference slot must be completed once after import; no runtime config chooser remains. It reads the config to Text once and reuses those same bytes for every helper call. JSON decoding inside the helper does not reload the file. It reads Name and File Extension directly from the original selection and never constructs a duplicate native File collection.

Each PDF name is sent to the helper. Non-PDF extensions become unresolved report rows. An error status from the helper sets the preview error state, preserves earlier report rows and skips later selections; invalid configuration is a run-level problem. The report includes every processed file's status, day/slot, service name, position, canonical name and reason. The final Get Text supplies report Text on natural completion, after Quick Look. This caller result path still requires device confirmation. Picker cancellation may terminate natively without a final report; no handling of a native-abort exception is claimed.

Rows use provider order only. There is **no numeric sort, grouping, date, service ID, occurrence plan, native PDF type validation, archive write, score import, metadata edit, setlist lookup/write or persistent state** in this delivery. A preview status of parsed means only that this filename matched the recurring rules, not that a service is ready to execute.

## Nextcloud naming evidence and implementation implications (8 November 2026)

Source: [updated Nextcloud listing](../../2026-11-08%20project_file_structure.txt). Compared with the [earlier listing](../../nextcloud%20file%20structure.txt). This is static listing analysis, not execution evidence, and does not modify source/config or expand initial-release scope. File/folder presence does not establish file contents, completeness or metadata meanings.

### Folder dates and discovery scope

| Observed convention | Examples | Planning implication |
| --- | --- | --- |
| Single-date folders | HNov7(ATB), HNov8 | Accept a single date as well as a range. A recognised day prefix must agree with the selected folder's resolved date/range before assignment; report conflicts rather than silently moving to another week. |
| Date-range folders | INov9-15, JNov16-22, KNov23-29 | Parse start/end explicitly, then assign service dates inside that range. Preserve current-year defaulting, saved context and month/year rollover rules. |
| Leading folder letter | H, I, J, K | Appears to be an organisational sequence; its meaning is unconfirmed. Do not treat it as a year or unique week ID. HNov7(ATB) and HNov8 already share H. |
| Folder qualifier | HNov7(ATB) | Preserve ATB as source context. Do not append it automatically to every canonical name or use it alone to split service identity. |
| Nonweekly collections | YouthChoir, NewMusic, ReadySteadyChoir!, Theory, Other Concerts, InstantUpload | A parsable filename does not authorise inclusion. Keep Weekly within the selected supported date folder; no unrestricted recursive sweep through ScannedChoirMusic. YouthChoir contains Sat-prefixed music that would otherwise look valid. |

A shared date/slot across separately selected folders should resolve through the normal service identity policy, not create another service because the folder letter or qualifier differs. Parent-folder context may be unavailable from the Share Sheet; Specific service still needs explicit missing context rather than an invented date.

### Piece names, ordering and metadata

| Observed convention | Examples | Planning implication |
| --- | --- | --- |
| Gaps in source positions | Fri1, Fri3, Fri4, Fri5; noncontiguous Sunday positions | Sort the available positions numerically without renumbering. Missing position numbers alone are not evidence of missing PDFs. Report missing occurrences only when an actual plan/reference or saved unresolved occurrence establishes one. |
| Multi-digit positions | Sun10, Sun11 | Numeric sort is required; current extraction of 11 is not a sorting pass. |
| Same piece across positions/services | Ps150-Talbot at Sun10 in HNov8 and Sun11 in INov9-15; Clucas-Responses under Tue/Fri/Sunpm | Position and source folder belong to occurrences, not score identity. Reuse scores while preserving distinct service occurrences and deliberate repetitions. |
| Hymn/source identifiers | NEH485, AMR577, OH01/OH02 | Reserve these ahead of generic composer/title inference. AMR is additional explicit evidence in this listing. Preserve leading zeros and do not label AMR577/OH01 as composers. |
| Tune/variant suffixes | NunDanket, Meirionydd, Blaenwern-CJR, AP | Keep the complete payload. AP/CJR meanings are unconfirmed; do not discard or expand them or merge different variants automatically. |
| Voice/key/movement qualifiers | Responses(SATTB), InG(ATB), LittleOrganMass-Gloria, InE-AgnusDei | Keep these identity-bearing distinctions, including attached SATB text in Tallis-IfYeLoveMeSATB. Folder voice context does not replace explicit piece qualifiers. |
| Psalm numbers/extracts | Ps070, Ps89vv19-29, Ps119vv137-160 | Preserve exact references and ranges. Do not automatically merge padded/unpadded numbering, whole psalms and extracts, or Moore-Psalm24 with a plain numbered psalm. An explicit future alias decision would be needed. |
| Numeric/dotted payload | Sun5-64.2ndBeforeAdvent.pdf | Payload is 64.2ndBeforeAdvent. Do not strip its leading number/dot or infer a composer from it. Its category/meaning is unresolved. |
| Numbered collection pieces | 1.RSC-ATallStory.pdf, 2.RSC-OverTheRainbow.pdf | Separate, context-specific ordering convention. Do not globally strip number-dot prefixes: that would damage other names such as 64.2ndBeforeAdvent. Supporting this collection is outside current Weekly parsing. |
| Possible collection aliases | Plumstead-AGratefulHeart.pdf and RSC-Plumstead-AGratefulHeart.pdf | Similar names are candidates for review, not proof of identical PDFs/editions. Keep references distinct until explicitly resolved. |
| Unprefixed pieces | Mozart-Spatzenmesse-Gloria.pdf, Jesus Walking On The Waves.pdf, Ave Maria elgar.pdf | Specific service must be able to accept usable files without a service prefix, supplying date/slot/order separately. Weekly must report unresolved/unassigned music rather than guess. No generic composer/title format is guaranteed. |
| Punctuation and spaces | World'sTrueLight, StJohn'sService, Responses(SATTB), complete-score names with commas/spaces | Preserve punctuation and payload text. Do not split all hyphens into a fixed number of fields or treat apostrophes/parentheses as disposable formatting. |

### Nonmusic and historical conventions

Ignore sync logs/databases, Desktop.ini and directories as music candidates. Reject the bare ScannedChoirMusic/.pdf as an empty-name candidate. Date PDFs, term dates, theory workbooks and schedules demonstrate that PDF extension alone is insufficient evidence of service music; use discovery scope and explicit review, not content claims inferred from filenames.

The earlier listing contained ExtraServices event folders such as Fri9Oct,11am-ChristopherDayRIP and Sat17Oct,11am-Wedding-BruceHargrave&Irene, with unprefixed music and a running-order document. The updated listing shows ExtraServices without those children; that does not prove deletion. Retain the historical convention for later event-context support: date/time/service can come from the folder, while ordering needs an explicit source or user input. Do not implement this format or revive removed selections automatically in the current increment.

### Implementation order and remaining decisions

1. Extend the shared config/date path with the evidenced single-date/range forms, optional leading letter and folder qualifier. Determine exact supported month/separator/rollover boundaries before writing the date parser; historical year accuracy is not a new requirement.
2. Add numeric ordering that tolerates gaps, with duplicate-position ambiguity handled separately from missing music. Keep occurrence identity independent of position.
3. Add explicit metadata/reference recognition for NEH, AMR, OH and psalms before generic composer/title suggestions, preserving variants and qualifiers throughout.
4. Keep folder discovery constrained and make unsupported collections/unprefixed inputs visible. Specific service's unprefixed-file route remains part of its planned implementation, not a new Weekly guessing rule.
5. Defer RSC collection parsing and historical event-folder expansion unless needed by an authorised entry-point increment. Initial release still consists of Weekly and Specific service; mass import remains deferred.

Open questions: meaning of folder letters and AP/CJR; which collection names are true aliases; exact out-of-range weekday conflict handling; further folder formats at month/year boundaries. No answers are assumed from this listing. Current service-prefix source/config stays unchanged: the new findings primarily affect dates, ordering, scope and later metadata resolution.

## Piece metadata requirement (8 November 2026)

The initial V3 release must save human-readable Title, Composer where known, and music Type in forScore. Type maps to native Genre; for example internal psalm -> configured Psalms archive folder/Genre. Keep spelling/singular-plural aliases in one shared mapping. Service type remains setlist context. See the [full metadata policy, record and acceptance criteria](../../nextcloud-forscore-plan-v3.md#piece-metadata-in-forscore).

Preflight reviews new/uncertain metadata once per distinct piece before the run's single confirmation. Preserve approved decisions in a new V3 piece-metadata record, shared across service occurrences; no routine metadata prompts during execution. New Scores get approved metadata. Reused Scores preserve manual values by default, with explicit per-field correction only. Unknown Composer stays unassigned/pending; an unresolved required archive category leaves the occurrence unresolved while independent music continues.

Do not confuse display Title with canonical identity. Establish native Rename/title/filename behavior and a verified Score association before applying title edits, so later reruns do not import duplicates. Native IDs, target resolution, write/readback and Composer/Genre reuse remain V3 integrated-check requirements. No metadata-writing source or config keys are implemented by this planning update; current previews remain read-only.

### Planned native Composer resolver

**V3 - Resolve Composer** takes one approved composer-name Text and returns one native forScore Composer object: reuse an unambiguous existing item, otherwise create and return it. Blank/ambiguous input yields no usable Composer; truly unknown authorship remains pending rather than creating a placeholder. It never assigns metadata to Scores/Bookmarks; assembly consumes its result through Add metadata after confirmation.

The [full utility contract](../../nextcloud-forscore-plan-v3.md#shared-utility-v3---resolve-composer) covers whitespace, duplicates, unconfirmed creation/retry and native action checks. Native object return/transport and standalone creation remain unverified. Implement this utility before wiring assembly's Composer assignment, and install it before any caller that requires it. It is planned, not an additional dependency of the current filename preview.

## Target controls, proposal editing and explicit replacement (8 November 2026)

User direction: Specific service selects Date with a native picker and Service with a configured Evensong/Eucharist/Mattins chooser, deriving the full name automatically. For an existing unique target, show actual contents then offer Add to existing / Replace contents / Cancel. The review screen offers Proceed / Edit proposal / Cancel; Edit contains Change Name, Change Date, Change Service, Change Order and music/metadata/mode options. Each edit returns to the regenerated proposal, allowing another edit without a mandatory sequence of prompts. Weekly offers these edits per selected service within its batch preview and retains one final confirmation.

This explicitly supersedes the earlier universal no-replace policy. Add remains the default, preserving manual entries/order. Replace affects only the selected target's entries and requires a complete nonempty approved sequence; preserve Scores, annotations, archive PDFs and unrelated metadata/setlists. Incomplete replacement stays pending without clearing. Changing target resets mode to Add; explicit Replace is never persisted as an invisible default. Readback and interruption recovery differ by mode and require device checks.

Prefer comparable numeric file positions; otherwise propose the received provider order. Actual tap order cannot be guaranteed without provider evidence. Change Order affects new/Replace sequences; Add must show the merged result while preserving existing relative order. Display-name overrides retain service identity; date/slot changes re-resolve identity/target. See the [full review/ordering/replacement policy](../../nextcloud-forscore-plan-v3.md#target-selection-and-proposal-editing-8-november-2026). This is design only: current filename preview/config still does not create services or replace entries.

## Next contracts and implementation boundaries

These decisions guide the next increments but are not executable contracts yet:

- Service identity: ISO date plus stable slot (`2026-11-08/evensong`). Display templates and prefix spelling do not identify a service. Display-name changes require record-based target resolution.
- Occurrences are separate from unique native PDF/Score objects: A/B/A remains three occurrence records and two pieces. Define durable occurrence matching before enabling reruns; picker order is not stable identity.
- Entry points provide the same plan schema. Assembly owns native Score and Setlist objects. The concrete plan/context transport remains to be implemented and checked on the iPad; this Text-only parser input does not validate native mixed transport.
- Preflight gathers essential context and unresolved work before one confirmation. No routine category/metadata prompts during approved batch execution. Unknown required details leave the occurrence unresolved.
- Default Add mode inserts verified missing occurrences into supported gaps while preserving old entries/order. Explicit per-service Replace contents is now authorised in the design, following the complete-sequence policy. Unavailable insertion, conflicting anchors or ambiguous targets remain pending; no silent replacement fallback.
- Records under the separately configured V3 records location link service ID to a verified locator and progress. Native readback, not a record, decides what already exists after interruption. Persistent identifiers and insertion fields require actual native-action inspection during assembly construction.

The next delivery after this checkpoint will extend the shared parsing/config path with actual week-folder date examples and numeric ordering, then connect the new supplied-plan assembly. No legacy adapter is needed.

## Source evidence used for this delivery

The pinned local documentation supplies candidate signatures: [JSON decoding](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/getDictionaryFrom.md), [key reads](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/valueFor.md), [key writes](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/setValue.md), [regex match](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/matchText.md), [regex replacement](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/replaceText.md), [case conversion](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/changeCase.md), [File details](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/fileDetail.md), [Get Text](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/getTextFrom.md), [selection](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/selectFile.md), [List](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/list.md), [Run Shortcut](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/runShortcut.md). Existing source uses lowercase; the documentation does not itself enumerate that case option, so its generated setting needs checking.

The [Text List evidence](../tests/compatibility/list-variable-transport.md) supports explicit interpolated Text tokens. [Quoted-index extraction](../tests/compatibility/name-item-extraction.md) and [recent generation results](../tests/ipad-investigation/generation-groups-results.md) support the selected candidate loop forms. None establishes compilation or execution of these new sources. No old helper is called to obtain their behavior.
