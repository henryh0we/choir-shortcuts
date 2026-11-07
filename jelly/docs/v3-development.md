# V3 implementation and contracts

7 November 2026. User direction: build from the ground up, use `V3 - ...` names, and do not depend on the old shortcuts. This supersedes the earlier migration/legacy-compatibility approach for new v3 work. No old shortcut needs backing up, updating or installing to use v3. Historical files remain as evidence, and existing music is not deleted.

Development sequence: [timeline](../../nextcloud-forscore-v3-development-timeline.md). Requirements: [v3 plan](../../nextcloud-forscore-plan-v3.md). Device instructions and results: [first checkpoint](../tests/v3/README.md).

## Current delivery

**Stage 2A: filename parsing and recurring-schedule preview. Drafted only; not compiled, imported or executed.** No builds or tests were run, following the user's instruction. This is the first implementation slice, not a complete Weekly preview.

| Exact installed name | Source | Dependency | Interface |
| --- | --- | --- | --- |
| V3 - Parse Filename | [v3-parse-filename.jelly](../shortcuts/reusable/v3-parse-filename.jelly) | None | 1.0 |
| V3 - Preview Filenames | [v3-preview-filenames.jelly](../shortcuts/main/v3-preview-filenames.jelly) | V3 - Parse Filename 1.0 | 1.0 |

Planned names, not yet implemented: `V3 - Create Service`, `V3 - Weekly`, `V3 - Assemble Service`, and `V3 - Archive PDF`. Only add further installed helpers when reuse warrants them. V3 - Create Service is the new Share Sheet title; this supersedes the earlier unprefixed title. There is no implicit naming/archive dependency on `UTIL - ...`, `MAIN - ...`, `2-util-...` or any TEST shortcut.

## Configuration ownership

Copy [v3-config.example.json](../config/v3-config.example.json) to one user-controlled Files location as **v3-config.json**. Do not replace the legacy config. The preview asks for this file each run; a pinned native Folder/config reference will follow in a later increment. Only the selected file supplies rules; neither source embeds a second copy.

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

## V3 - Parse Filename interface 1.0

Input: exactly two **Text** List items, in order: filename and full v3 config JSON snapshot. This is intentional Text transport of configuration data only; it does not serialize native music Files. The helper is called without prompts. Direct launch with no input returns an explanatory ERROR Text.

Output on a valid config: one native Dictionary, built from a static JSON template plus Set Dictionary Value actions. All result values are **Text**, including numeric position and schemaVersion:

| Field | Meaning |
| --- | --- |
| schemaVersion | `1` |
| status | `parsed`, `skipped` or `unresolved` |
| sourceName | Original supplied name |
| ruleKey | Unique matched rule; empty for unresolved match count |
| dayKey | mon/tue/wed/thu/fri/sat/sun |
| serviceSlot | Configured stable slot, or special suffix slot |
| serviceName | Configured regular name, or readable special suffix |
| position | Positive integer Text; later sorting must convert numerically |
| canonicalName | Full payload without prefix or terminal PDF extension |
| reason | Explanation; explicitly states this is not date-resolved |

Skipped rows keep their parsed identity/payload so exclusions can be explained. Unmatched/conflicting rows have empty parsed fields. Invalid input, unsupported config version/settings, incomplete rules or invalid extraction return `ERROR: ...` Text. A native JSON/regex/action failure may terminate without returning. This is focused validation, not a complete JSON schema validator; user-authored regex capture meanings still require inspection.

Native Dictionary creation, dynamic Set Dictionary Value interpolation, lowercase generation and native Dictionary return are documentation/source-backed candidates, **not device-confirmed v3 behavior**. The first checkpoint deliberately exercises them in the real caller. Inspect the generated return and its caller before attributing success to the helper. If `exit(var: finalResult)` is rejected or wired incorrectly, replace only that boundary with native Stop and Output returning finalResult, and record the repair. Do not convert the result to interpolated Text to hide a transport failure.

## V3 - Preview Filenames interface 1.0

Direct launch only; ignores incoming input. Shows a cancellable explanation, selects one config File and then multiple Files. It reads the config to Text once and reuses those same bytes for every helper call. JSON decoding inside the helper does not reload the file. It reads Name and File Extension directly from the original selection and never constructs a duplicate native File collection.

Each PDF name is sent to the helper. Non-PDF extensions become unresolved report rows. ERROR Text from the helper aborts the preview; malformed configuration is a run-level problem. The report includes every processed file's status, day/slot, service name, position, canonical name and reason. Output is one report Text, also displayed in Quick Look. Picker cancellation may terminate natively without a final report; no handling of a native-abort exception is claimed.

Rows use provider order only. There is **no numeric sort, grouping, date, service ID, occurrence plan, native PDF type validation, archive write, score import, metadata edit, setlist lookup/write or persistent state** in this delivery. A preview status of parsed means only that this filename matched the recurring rules, not that a service is ready to execute.

## Next contracts and implementation boundaries

These decisions guide the next increments but are not executable contracts yet:

- Service identity: ISO date plus stable slot (`2026-11-08/evensong`). Display templates and prefix spelling do not identify a service. Display-name changes require record-based target resolution.
- Occurrences are separate from unique native PDF/Score objects: A/B/A remains three occurrence records and two pieces. Define durable occurrence matching before enabling reruns; picker order is not stable identity.
- Entry points provide the same plan schema. Assembly owns native Score and Setlist objects. The concrete plan/context transport remains to be implemented and checked on the iPad; this Text-only parser input does not validate native mixed transport.
- Preflight gathers essential context and unresolved work before one confirmation. No routine category/metadata prompts during approved batch execution. Unknown required details leave the occurrence unresolved.
- Updates only add verified missing occurrences into supported gaps. No clear/replace path will be implemented. Unavailable insertion, conflicting anchors or ambiguous targets remain pending.
- Records under the separately configured V3 records location link service ID to a verified locator and progress. Native readback, not a record, decides what already exists after interruption. Persistent identifiers and insertion fields require actual native-action inspection during assembly construction.

The next delivery after this checkpoint will extend the shared parsing/config path with actual week-folder date examples and numeric ordering, then connect the new supplied-plan assembly. No legacy adapter is needed.

## Source evidence used for this delivery

The pinned local documentation supplies candidate signatures: [JSON decoding](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/getDictionaryFrom.md), [key reads](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/valueFor.md), [key writes](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/setValue.md), [regex match](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/matchText.md), [regex replacement](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/replaceText.md), [case conversion](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/changeCase.md), [File details](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/fileDetail.md), [Get Text](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/getTextFrom.md), [selection](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/selectFile.md), [List](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/list.md), [Run Shortcut](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/runShortcut.md), and [variable return](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/exit.md). Existing source uses lowercase; the documentation does not itself enumerate that case option, so its generated setting needs checking.

The [Text List evidence](../tests/compatibility/list-variable-transport.md) supports explicit interpolated Text tokens. [Quoted-index extraction](../tests/compatibility/name-item-extraction.md) and [recent generation results](../tests/ipad-investigation/generation-groups-results.md) support the selected candidate loop forms. None establishes compilation or execution of these new sources. No old helper is called to obtain their behavior.
