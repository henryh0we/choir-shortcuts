# Instructions for agents

## Scope and outcome

This repository designs and documents Apple Shortcuts for a human to build in the iPhone Shortcuts editor. Markdown specifications are the source of truth; they are not executable shortcuts. Produce complete, reproducible action sequences and practical manual tests. Never imply that writing a specification installs, builds, or executes a Shortcut.

For forScore integrations, also read [forscore.md](../forscore.md). Use its helper contract template and numbered assembly steps within the bracketed blueprint style, verify installed-device actions, and keep manual helpers separate from regenerated Jelly workflows. The user's build workflow must work entirely on iPhone/iPad without requiring a Mac.

Read existing specifications, the index, and relevant project notes before making changes. Use `Parse Choir Music Filename V2 - Shortcut Blueprint.txt` as the user's preferred presentation reference; preserve that original file. Its layout is authoritative for style, but individual actions/settings still need the normal accuracy checks. Preserve unrelated files, including `nextcloud file structure.txt`; it is reference material, not proof that those files are available on an iPhone. Do not infer Nextcloud credentials, server addresses, permissions, or file-provider behaviour from that listing.

## Repository layout and naming

```text
AGENTS.md
README.md
SHORTCUT_TEMPLATE.md
SHORTCUT_INDEX.md
shortcuts/
  main/                 User-facing workflows
  reusable/             Shared components, including utilities
examples/               Teaching specifications, one file per Shortcut
docs/                   Platform evidence and project architecture notes
```

Create directories only when adding content. Keep main and reusable Shortcuts one directory deep; do not introduce separate core/utility folders without a concrete discovery problem. Examples live only in `examples/`, even if their role is Main or Reusable. Link to an example rather than duplicating it elsewhere. A project note may describe several Shortcuts, but each implementation must have its own specification.

Use exact app names `MAIN - <Verb Phrase>` for workflows and `UTIL - <Verb Phrase>` for reusable components. Reserve `TEST - <Verb Phrase>` for persistent diagnostics when needed. Keep names short, unique across the repository, and descriptive. The Shortcut name field must match the app name exactly, including spaces and punctuation. The display title may be uppercase, as in the preferred blueprint. Use lowercase kebab-case filenames with the prefix: `util-format-greeting.md`. Directory location distinguishes examples; it does not change app names.

Add each specification to `SHORTCUT_INDEX.md` with its linked exact name, purpose, category, direct dependencies, and status. The specification owns the contract, dependency details, and test evidence; the index is only a navigation summary. Update both together. Add a project note under `docs/` only when a multi-Shortcut design needs shared context or a build order that cannot be explained briefly in its entry-point specification.

## Work sequence

1. Inspect the repository for existing components and callers. Establish the outcome, launch methods, interactions, data sources, outputs, external services, and constraints.
2. Establish the target iOS major version and editor language. If unspecified, declare a provisional design target and list it as an assumption; do not claim compatibility with the user's device. Ask for device details when they affect feasibility, while continuing independent design work.
3. Sketch the whole project's data flow and proposed components before writing actions. Decide which parts merit separation and explain that decision briefly in the main specification or project note.
4. Define every input/output interface first. Check that caller and callee agree on type, cardinality, missing values, keys, and failure behaviour.
5. Check action names and capabilities against Apple documentation or target-device evidence. Identify third-party actions and required app versions explicitly.
6. Copy `SHORTCUT_TEMPLATE.md` into one file per Shortcut; replace all placeholders. Write every action and editor setting needed to build it.
7. Review dependencies, variable wiring, every branch, loop output, side effect, and exit. Provide dependency-first build order and manual tests.
8. Update the index and affected callers. Report what is documented, what remains uncertain, and what still requires an iPhone build or execution.

Do not replace any action sequence with phrases such as "validate input", "parse the response", or "save the data". Document the actual actions that perform those operations. JSON is appropriate as an API payload example, but not as the primary representation of a Shortcut.

## Decide when to extract a component

Use native `Run Shortcut` for composition. Extract a component when it is shared, independently useful, a coherent function, a stable interface, likely to be reused for a concrete reason, or substantially simplifies its caller. Explain the benefit against the cost of building, naming, wiring, and testing another Shortcut. Keep a short one-off sequence inline when extraction adds little value. Do not split solely to increase modularity, create speculative layers, or use recursive calls as a default looping strategy.

Text processing, validation, dates, requests, file operations, configuration, and logging are candidates, not mandatory separate components. Prefer local variables and explicit inputs over shared clipboard state or hidden files. Keep useful components directly runnable when a default or prompt is appropriate. A prompt must never unexpectedly block an unattended caller: use an explicit documented mode when behaviour must differ. Missing input alone does not prove a Shortcut was launched directly.

## Required specification structure

Use the readable blueprint layout demonstrated by `Parse Choir Music Filename V2 - Shortcut Blueprint.txt`. Keep one Markdown file per Shortcut, but place its blueprint in one fenced `text` block so indentation, blank lines, and separator lines survive Markdown rendering. Put clickable dependency and source links outside that block. Do not replace the blueprint with numbered action cards, parameter tables, or a separate flow map.

Start with an uppercase display title and an equals-sign underline, then `Shortcut name:`, `Purpose:`, `Input:`, and `Output:`. Follow with concise labelled metadata and contract details, `DEPENDENCIES AND BUILD ORDER`, and `EDITOR SETUP`. The action sequence follows, divided into meaningful uppercase phases with equals-sign separators. End with `EXPECTED TEST RESULTS`, `BUILD NOTES`, `ERRORS AND LIMITATIONS`, `IMPLEMENTATION RECORD`, `CHANGE HISTORY`, and `SOURCES AND OPEN VERIFICATION`. Use these sections in this order; short empty sections may say `None` or `Not applicable`.

Metadata must retain category, specification revision, interface version, target iOS, editor language, status, required apps, permissions, launch methods, and side effects. Contract details must retain defaults, cardinality, direct/called behaviour, and unsupported inputs. Present them as short labelled lines, not tables. Put detailed explanations in BUILD NOTES rather than between routine actions.

### Bracketed action blocks

Use this style inside the blueprint's text fence:

```text
========================
FORMAT GREETING
========================

[Text]
Hello, [Shortcut Input]!

NOTE:
Insert Shortcut Input as a variable token between literal "Hello, "
and "!". Do not type the brackets or add a newline.

[Stop and Output]
Output: Text from FORMAT GREETING
No-recipient behaviour: Respond
```

- Write the exact action name on its own line in square brackets: `[Text]`, `[If]`, `[Run Shortcut]`. Follow it with one `Parameter: Value` line per setting. Do not number actions or add repetitive Action/Placement/Kind/Output-reference labels.
- Use blank lines between actions and larger gaps between phases. Use `========================` around uppercase phase headings and `--- SUBSECTION ---` for smaller divisions, like the supplied blueprint.
- Write Text action content directly beneath `[Text]`; do not prefix it with `Content:` unless that distinction is necessary to avoid ambiguity. Add a brief NOTE when content mixes literal text with selected tokens.
- Square brackets on a standalone action line identify an action or generated marker. Within Text content, `[Payload]` identifies a variable token only when a NOTE explicitly maps it to its source. `[leave empty]` is an instruction to leave a field blank, not literal text.
- Values in variable-bearing fields such as `Input: Payload` or `Output: ParserResult` mean select that variable, not type its name. State this convention in EDITOR SETUP. Identify literal values and menu choices where the field or context does not make them clear.
- Use full `[Set Variable]` blocks with `Variable:` and `Input:` where useful. The compact form `[Set Variable] Greeting = Text from FORMAT GREETING` is allowed when the source is unambiguous. Both represent real actions to add, not notes or assignment pseudocode.
- Use `NOTE:` for short construction explanations. It is documentation, not a Comment action. Add `[Comment]` only when a real Comment action is intended in the built Shortcut.
- Record expanded settings and deliberate blanks/defaults that affect execution. If a parameter label is only a descriptive locator, explain that once in EDITOR SETUP and identify the unresolved exact label in the verification section. Do not clutter every action with repeated caveats.
- `[Shortcut Input]` is a declaration of incoming content, not a searchable action to add. A Receive banner is editor setup. State its expected type beneath the declaration when input is consumed; omit it when incoming content is ignored. Never invent a Receive Shortcut Input action.
- Copy the reference blueprint's readability, not unsupported capabilities. In particular, an action label found in a legacy blueprint (such as `[Boolean]`) is not proof that a native action of that name exists. Verify it before documenting it as buildable; use confirmed native representations when appropriate.

### Variables and connections

Prefer readable variable names and native output names over `Magic(03)`, `Named(...)`, or `Special(...)` notation. No such wrapper notation is required in blueprints. To select a Magic Variable, tap the destination field, use the variable selector, and choose the output beneath the source action. Identify that source by its unique phase/subsection and action, even when it is adjacent. Never write only "use the previous result".

When several actions have the same output name, qualify it: `Text from FORMAT GREETING`, `Dictionary Value for Composer from READ PAYLOAD RESULT`, or `Shortcut Result from CALL FORMATTER`. Define these as source descriptions, not variable names to create. Explain the exact output selection in a brief NOTE or BUILD NOTES when necessary. Use `Set Variable` when it materially simplifies repeated/distant references, branch assignments, or a returned value reused after a display; do not add it merely to label every output.

Use descriptive named variables such as `SelectedMusicFiles` and do not reuse a name for unrelated values. State assignments on every path before use. Explicitly select the intended source rather than accepting automatic Set Variable chaining. Variables are local to a run, not storage shared between Shortcuts.

For Dictionary access, document `[Get Dictionary Value]`, literal key, source Dictionary, and expected value type in the contract. For `[Dictionary]`, use readable `Key = Value` rows and state which right-hand values are selected variables versus literal values, including each entry's editor type. Keep this native Dictionary construction distinct from JSON serialization. Automatic conversions must be deliberate and documented; add explicit conversion actions only when needed.

### Conditions, loops, and nesting

Use four spaces per nesting level throughout the fenced blueprint. Indent both action labels and their parameter lines. Align `[Otherwise]` and `[End If]` with their owning `[If]`; align `[End Repeat]` with its owning `[Repeat]` or `[Repeat with Each]`. Indent phase headings and NOTE blocks at the level where they belong. This single sequence communicates both order and nesting; do not duplicate it in a flow map.

Adding If automatically creates Otherwise and End If; adding Repeat/Repeat with Each creates End Repeat. Explain once in EDITOR SETUP that these bracketed markers are already supplied by the editor and must not be added as separate actions. Say explicitly if removing an Otherwise branch.

Document If input, selected type/property where relevant, exact condition, comparison value when required, and Any/All for multiple conditions. State which last action supplies each branch's result. If Result after End If must identify its owning conditional by phase/subsection; do not reference an unexecuted branch's action outside the branch.

For Repeat, specify count and source. For Repeat with Each, specify list source and item type. Qualify Repeat Item and Repeat Index by their owning loop, especially for nested loops. Explain which final action supplies each iteration's output and the resulting Repeat Results list type/order. If consuming that list, identify the closing loop. A side-effect action at the loop's end may change collected output; review it deliberately. Do not invent while, break, continue, or try/catch actions. Stopping ends the Shortcut, not just the enclosing loop.

## Input/output contracts

Every specification must explicitly define:

- Input type, one-versus-many cardinality, required/optional status, defaults, empty/missing/whitespace semantics, and supported entry points.
- For each structured field: exact case-sensitive key, value type, required status, default, and allowed values. Document list ordering and date/timezone interpretation where relevant.
- Output type/cardinality, exact structure or example, side effects, failure/cancellation outcome, and whether any user interface appears.
- Separate direct execution from `Run Shortcut` execution. Name any prompts and how callers prevent them. Share Sheet content filters are not general runtime validation for callers.

Use native Text, Number, Date, List, Dictionary, File, and URL content where suitable. Boolean is an interface meaning: explicitly document whether it is a native Dictionary Boolean, Number 0/1, or Text, and how actions compare it. These contract types are not all Share Sheet input choices. Do not conflate a File with a filesystem-path Text value.

Pass one value to `Run Shortcut`. Use a Dictionary when several related values are needed; choose stable lowerCamelCase keys. Do not serialize to JSON just to call another Shortcut. If an API requires JSON, document the conversion separately with real actions.

Prefer a simple typed output and explicit stop for simple components. For components that need recoverable validation errors, a project may adopt a Dictionary result with `ok` (Dictionary Boolean), `value` (defined success type), `errorCode` (Text), and `message` (Text). Define which keys are present on each path and document the actual Dictionary and comparison actions. Do not mandate this envelope for every utility; do not claim it catches action-level failures.

Use `Stop and Output` to make reusable return values explicit, including early exits. Specify its no-recipient behaviour where available. Display actions do not replace an output contract, and callers must consume the explicit callee result.

## Dependencies and changes

Each dependency entry must link to its specification outside the blueprint fence and give the exact app name, required interface version, and relevant app/platform prerequisite. List direct dependencies; derive transitive dependencies by following links. Write `None` if there are no dependencies. List required external apps/services separately from called Shortcuts.

Before finishing, follow every dependency link and confirm the target exists, the app name matches the `Run Shortcut` selection, and input/output contracts agree. Search all specifications for the exact app name and file path before renaming or changing a component. Do not introduce cycles or self-dependencies. Provide an ordered dependency-first build list for every composed entry point, including transitive components once each. The index must show enough information to find that list without maintaining a second detailed dependency graph.

Increment specification revisions for documentation/action changes. Increment the interface major version for changed required inputs, output types/keys, default semantics, side effects, prompts, or error behaviour that existing callers cannot safely accept; increment the minor version for compatible additions. A version in metadata does not enforce runtime compatibility: the builder must install the documented revision. Explain breaking changes, update affected callers/tests/index, and give concrete manual migration steps. When preserving an old interface is necessary, use a distinctly named new component and document the transition rather than silently replacing it.

On maintenance work, evaluate all affected components together, reuse useful existing behaviour, and prefer incremental changes. Explain exactly which installed actions/settings must change; Markdown edits do not update an iPhone automatically. Retain historical build/test evidence, but mark the current revision as needing reconstruction/retesting when implementation changes invalidate it.

## Errors, permissions, and platform evidence

Prefer native actions. Never invent actions, configuration fields, conditions, or capabilities. If not confirmed, write `VERIFY ON DEVICE: <specific question>` and describe the impact and practical fallback. List such uncertainties in Sources and open verification; unresolved implementation-critical questions prevent Ready for manual construction status.

Check target-version Apple documentation and, where available, exact-device editor screenshots or reported execution. Record source link, review date, applicable version/language, and what each source supports. Distinguish documentation-confirmed action semantics from device-confirmed settings and runtime results. Online guides can change: select the relevant iOS version when using them. See `docs/platform-notes.md` for the initial evidence and example assumptions.

For third-party actions, list provider/app, version, installation, permissions, and whether a native alternative exists. Document file-provider locations, local versus cloud availability, account setup, and permission prompts for file or network workflows. Keep secrets out of specifications and examples; describe manual configuration instead.

Design explicit checks for missing or malformed inputs and unexpected output where practical, using real actions. State the chosen response, returned value or lack of output, and any UI. Some actions can abort execution on failure; an If after such an action cannot catch an error that prevents it running. Do not promise recovery from network failures, absent files, missing called Shortcuts, denied permissions, or cancellation unless supported and actually verified. Document each relevant limitation and how a builder diagnoses it. Use the simplest reliable policy; propose a practical alternative when native Shortcuts cannot reliably satisfy the requirement.

## Manual tests and truthful status

Every specification needs iPhone-executable tests with prerequisites, exact launch/input steps, expected output and side effects, and a result field initially `Not run`. Cover the happy path, missing/empty input, a relevant boundary or invalid case, cancellation when interactive, direct execution when supported, and integration for reusable/composed Shortcuts. Mark out-of-contract cases explicitly; do not invent expected success for unsupported types.

Every reusable Shortcut must link to a caller example or include complete bracketed call action blocks with exact input/output wiring. Persistent test Shortcuts get their own file; clearly separate temporary diagnostic modifications from production actions and explain restoration.

Use these status labels consistently:

| Status | Required evidence |
| --- | --- |
| Designed | Complete proposal or draft; outstanding platform/settings questions may remain |
| Ready for manual construction | Static review complete; implementation-critical action names/settings resolved for declared target; no claim of a device build |
| Built | Current revision recreated in the target editor; device, OS version, date, and builder confirmation recorded |
| Tested | Current revision executed; actual results recorded, including failures |
| Verified working | All required tests passed on the recorded device/version, including required integration tests |

Never promote status based solely on plausible logic or link checks. A human's reported execution is evidence; record it as reported and identify which tests it covers. Keep status separate from documentation verification. Record tested specification revision, device/iOS, date, tester, actual results, and remaining issues. Never erase failures to imply universal success.

## Review before completion

Check that all files link correctly, names/statuses match the index, and no placeholders remain in completed specifications. Trace every variable to its source and every branch to its exit/output. Match control markers, indentation and execution order. Check dependency build order and interfaces. Confirm that every builder instruction corresponds to an existing action, marker, token, or setup setting, with uncertainty labelled. Confirm manual tests have observable expectations and do not claim unperformed execution. Read the examples as a first-time builder: no essential setting or connection should require guessing.
