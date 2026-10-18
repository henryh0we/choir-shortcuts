# Jelly language and toolchain reference

Reviewed 2026-10-14; documentation integration updated 2026-10-16. This is a repository-specific evidence record, not a complete language specification. **Source-backed** means checked in official documentation or upstream code; **compiled** requires actually running the chosen compiler. No successful compilation, import or device execution is recorded here; device-reported compilation failures are preserved below and in the compatibility record.

The candidate source profile is Open-Jellycore commit `e1ec31c2ee192c8721749f9eb3b50108e38891cf`, inspected through the official GitHub repository/API. The user-reported profile is Jellycuts 2026.6.4, iPadOS 26.6 and forScore 15.2.5. Bundled compiler and action-library revisions remain unknown; the candidate source revision is not an established app match. Examples must be compiled against the actual toolchain before compatibility is claimed. English editor conventions are used here.

Use the [local documentation index](jellycuts-docs-index.md), pinned at docs commit `19306be1dd30c20e12058ebe144dd8342e64ca39`, and [compatibility evidence and probes](../tests/compatibility/README.md) before changing syntax. Exact device-tested forms take precedence for the recorded profile. The [vendor README](../vendor/jellycuts-docs/README.md) records provenance, licensing status and refresh instructions. No successful probe results have been recorded.

## Primary sources

Current canonical revision 7 follows the [Exit Shortcut](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/exit.md) variable-return signature `exit(var: canonicalName)`. Invalid input exits with a Nothing result. This bypasses the unresolved Output binding instead of continuing to vary enum quoting. User diagnostics explicitly require bare ItemAtIndex, so both selectors now use that raw name without quotes. Revision 6's quoted selectors are known rejected. The replacement Exit binding is documentation-backed but still requires app compilation and result inspection.

Canonical revision 6 enum candidate, 17 October 2026: after the user's revision 5 out-of-scope diagnostics, quote Respond and use quoted ItemAtIndex. The pinned `Jelly_WFItemSpecifier` accepts raw `ItemAtIndex` and serializes it as `Item At Index`; it does not accept raw `Item at Index`. `Jelly_WFNoOutputSurfaceBehavior` accepts raw Respond. This resolves the source-evidence discrepancy, but quoted-argument acceptance in the installed app remains untested. Verify exported index settings and returned values before applying the candidate to other helpers.

Config integration, 17 October 2026: [Get Dictionary from Input](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/getDictionaryFrom.md), [valueFor](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/valueFor.md), [List](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/list.md), [item extraction](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/getItemFromList.md) and existing file/folder/text bindings are used by the config-based revisions. The pinned `JellyDictionary.convertJSONObjectToShortcutsDictionary` implementation includes a TODO for interpolation and handles JSON primitives; `setValue` takes JellyString. Neither establishes safe construction of native File/Folder dictionary entries. This implementation therefore passes native Lists, isolates that boundary in a read-only probe, and leaves native config File retrieval at CONF02 because Jelly Get File exposes no native Folder parameter. No guessed JSON parser, File path encoding or Dictionary interpolation is used. New List extraction/config actions have not been executed on the installed app. See [config integration](config-integration.md) for current contracts; older examples below describe earlier revisions.

| Source | Evidence |
| --- | --- |
| [Official documentation](https://docs.jellycuts.com/) | Language and action-library reference; some older examples remain |
| [Importing libraries](https://docs.jellycuts.com/Language_Guide/importing.html) | Native `import Shortcuts`; imports expose bindings for following code |
| [Variables](https://docs.jellycuts.com/Language_Guide/variables.html) | Mutable declarations/assignment; some expression features described may depend on compiler version |
| [First-script tutorial](https://docs.jellycuts.com/Getting_Started/writing_first_script.html) | Lowercase text call, `>>` capture, interpolation, app onboarding/export route |
| [If/else](https://docs.jellycuts.com/Language_Guide/if_else.html) | Conditions including `!= nil` for has-any-value; else syntax |
| [Repeats](https://docs.jellycuts.com/Language_Guide/repeat.html) | Repeat and repeatEach concepts; legacy spaced loop-variable examples |
| [Functions/macros](https://docs.jellycuts.com/Language_Guide/functions_macros.html) | Separate function dispatch and macro expansion semantics |
| [Run Shortcut](https://docs.jellycuts.com/Documentation/Shortcuts/runShortcut.html) | Native composition binding |
| [Output page](https://docs.jellycuts.com/Documentation/Shortcuts/output.html) | Explicit output intent; signature conflicts with inspected compiler |
| [Metadata](https://docs.jellycuts.com/Language_Guide/metadata.html) | Metadata documentation; no installed-name directive adopted here |
| [Official compiler repository](https://github.com/OpenJelly/Open-Jellycore) | CLI and implementation; linked legacy Jellycuts repository redirects here |

Pinned compiler evidence:

- [Language feature tests](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Tests/Open-JellycoreTests/LanguageFeaturesTests.swift): imports, `var`, `ShortcutInput`, conditions, loops, functions/macros.
- [Global-variable tests](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Tests/Open-JellycoreTests/VariableTests.swift): unspaced input/date/item/index names. These tests were read, **not run** here.
- [Text binding](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Sources/Open-Jellycore/Core/Compiler/Lookup%20Tables/Apps/Shortcuts/Actions/TextParameter.swift): `text` argument name.
- [Run Shortcut binding](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Sources/Open-Jellycore/Core/Compiler/Lookup%20Tables/Apps/Shortcuts/Actions/RunShortcutParameter.swift): name/input/show fields and variable-reference input.
- [Output binding](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Sources/Open-Jellycore/Core/Compiler/Lookup%20Tables/Apps/Shortcuts/Actions/OutputParameter.swift) and [no-output enum](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Sources/Open-Jellycore/Core/Compiler/Lookup%20Tables/Apps/Shortcuts/Enums/Jelly_WFNoOutputSurfaceBehavior.swift): actual argument slots and enum spellings.
- [String serialization](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Sources/Open-Jellycore/Core/Language/Primitives/JellyString.swift): interpolated values become variable attachments, rather than literal variable names.
- [CLI source](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Sources/jelly/jelly.swift): file argument, export/output options, diagnostics, and naming limitation.

## Source-backed patterns

Imports, variables, strings, and output capture:

```jelly
import Shortcuts
var name = "Henry"
name = "Friend"
text(text: "Hello, ${name}!") >> greeting
```

`var` creates mutable values; `>>` captures a call's output as a Magic Variable. `${name}` is string interpolation. `ShortcutInput` refers to incoming content. Do not use the older spaced `Shortcut Input` examples or capitalized `Text(...)` calls found on some guide pages for this candidate profile.

Conditions use Jelly's documented operators rather than arbitrary JavaScript truthiness. The examples combine the guide's `!= nil` presence condition with the brace form used by compiler tests:

```jelly
var name = "Friend"
if ShortcutInput != nil {
    name = ShortcutInput
}
```

This is a source-reviewed candidate, not an executed parser/runtime check. Compile it and inspect the resulting presence condition, input token type, and empty-input path. If a Receive banner appears, ensure its no-input setup allows the branch logic to run rather than stopping first.

Inspected compiler tests demonstrate loop forms without parentheses:

```jelly
repeat 3 {
    text(text: "Iteration ${RepeatIndex}")
}
repeatEach ShortcutInput {
    text(text: "${RepeatItem}")
}
```

These fragments illustrate syntax only; they are not separate installed examples. The second requires iterable input. Check actual item/index types and collected output on import. Nested loop names differ among official materials: inspected tests use `RepeatIndex1`/`RepeatItem1` for an inner loop, while some app release notes use other suffix examples. Confirm against the selected build before writing nested loops.

Top-level Shortcut output for the inspected bindings:

```jelly
output(result: "${greeting}", noResultBehavior: Respond, response: "${greeting}")
```

The binding requires these three named slots. The web output page instead shows `notes` and `folder`; do not use that signature for this candidate compiler. `Respond`, `DoNothing`, and `CopyToClipboard` are inspected enum spellings. Verify the generated stopping action and no-recipient behaviour. Only Text output is exercised by the example design; preservation of native Dictionary/File/List output through this binding is not established here.

Composition:

```jelly
var name = "Henry"
runShortcut(name: "UTIL - Jelly Format Greeting", input: name, show: false) >> greeting
```

Pass a variable reference, capture the result, and consume it explicitly. The exact installed name must exist. A language import does not install that Shortcut. The inspected binding reports missing arguments for omitted input/show, even though the web guide labels them optional; the examples supply all three.

Functions/macros are supported in the inspected feature tests, but were not used in these examples. The guide describes functions as dispatching within the same installed Shortcut through a Dictionary/self-call and macros as copying their body into the call site. Define them before calls. Do not equate them with separate installed utilities or assume recent typed parameters/expression returns are supported by an older compiler.

## Data types and collections

Text and Number declarations, variable references, string interpolation, and Boolean action arguments appear in the inspected material. Native contract types can additionally include Date, File, URL, List, and Dictionary when their actions and serialization are confirmed. These are not automatically all valid literal forms or Share Sheet filters.

The inspected [Dictionary binding](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Sources/Open-Jellycore/Core/Compiler/Lookup%20Tables/Apps/Shortcuts/Actions/DictionaryParameter.swift) reads a `json` slot; the [List binding](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Sources/Open-Jellycore/Core/Compiler/Lookup%20Tables/Apps/Shortcuts/Actions/ListParameter.swift) reads `items`; [key retrieval](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Sources/Open-Jellycore/Core/Compiler/Lookup%20Tables/Apps/Shortcuts/Actions/ValueForParameter.swift) reads `key` and `dictionary`.

These signatures alone do not verify a complete structured interface. Before using them, compile minimal fixtures to establish literal syntax, dynamic variables, nested values, native Boolean types, missing-key behaviour, and output preservation. Do not assume `JSON.parse`, JavaScript object access, null literals, zero-based indexing, or generic object support. Recent language-doc expression examples require matching-version verification.

No conventional try/catch capability was established. Handle expected validation conditions with supported checks, and distinguish returned validation errors from action-level failures that halt execution.

## Build, export, import

Local discovery on 2026-10-14 found no `jelly`, `jellycuts`, or `jellyc` command on PATH. This does not prove the user lacks a Jellycuts app on another device. No compiler was installed as part of creating these files.

The official app tutorial directs users to install/open Jellycuts, complete its onboarding connection to Shortcuts, create/open a project, and export into Shortcuts. Transfer/open each example's `.jelly` source in that app, check the console, export/import the utility first, and verify its installed name before importing the main. Exact menus depend on the installed app build. Record that build and any app-specific signature differences before claiming a match.

The official compiler repository documents this CLI shape on a supported host with `jelly` installed. Run from the `jelly/` workspace directory after creating `build/`:

```text
jelly --help
jelly examples/util-jelly-format-greeting.jelly
jelly examples/util-jelly-format-greeting.jelly --export --out build/util-jelly-format-greeting.shortcut
jelly examples/main-jelly-greeting-demo.jelly
jelly examples/main-jelly-greeting-demo.jelly --export --out build/main-jelly-greeting-demo.shortcut
```

These are documented commands, **not commands run here**. Confirm them with the actual installed CLI's help. Compiler installation instructions vary between official repository/formula pages; use current matching release instructions rather than copying an old Homebrew tap blindly. Do not assume this Swift-based CLI has a supported Windows binary.

Important inspected CLI limitations:

- It can print compiler errors and return without setting a failing exit code. Check diagnostics and artifact creation, not exit code alone.
- Its inspected entry point passes a fixed `Function Tests` name to compilation. Therefore source comments and output filenames do not establish installed names. Inspect/rename after import; this matters especially for function self-dispatch.
- Export writes the compiled representation to a file. Successful export does not prove that Apple's current import/signing checks accept it.

Inspect exports as property lists and inspect actions in the receiving editor. Where Apple's import flow requires signing, use the selected toolchain's documented Apple-compatible process or the Jellycuts app route. The reference does not establish a Windows signing command. Preserve useful installed versions and avoid creating duplicates with identical names.

## Comment slots and generated helpers

Additional pinned-source inspection on 2026-10-16 supports generating the archive/service helpers with post-import completion. The app version is now user-reported as Jellycuts 2026.6.4, with iPadOS 26.6 and forScore 15.2.5; its bundled compiler revision is still unknown.

- Historical [comment compilation source](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Sources/Open-Jellycore/Core/Compiler/Compiler.swift) handles comment and blockComment nodes. The user's installed Jellycuts 2026.6.4 build instead reports that `/* ... */` does not work: use only `//`, with one source line producing one separate native Comment block. This device evidence supersedes the earlier claim that block comments in these templates become usable instruction cards. Existing source block comments await conversion when those sources are next revised.
- The same compiler and Repeat/Conditional node classes implement `} >> result` capture. New helpers collect native loop results rather than inventing an append operator. End each preparation iteration with the native File/Score-producing action; trailing instructions can change collected output.
- [OutputParameter](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Sources/Open-Jellycore/Core/Compiler/Lookup%20Tables/Apps/Shortcuts/Actions/OutputParameter.swift) encodes its result using JellyString. Native File return fields are therefore explicitly completed after export at CFG03/CFG04; do not assume Text interpolation preserves a File object.
- SaveFileParameter accepts `input`, `ask`, `path` and `overwrite`, but no native Folder destination. CFG02 edits the generated Save File destination; CFG01 inserts the saved Folder reference. This avoids embedding an invented filesystem path or unsupported Folder action signature.
- The compiler leaves a bare identifier comparison operand unresolved as a TODO. The archive equality uses an interpolated Text operand (`archiveStem == "${canonicalStem}"`) instead of assuming two bare identifiers compare their runtime contents.

The [Shortcuts lookup table](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Sources/Open-Jellycore/Core/Compiler/Lookup%20Tables/Apps/Shortcuts/ShortcutsLookupTable.swift), associated Parameter files, and enum definitions were read for every new binding: `selectFile(type, multiple)`, `count(type, input)`, `choose(list, prompt, multiple, all)`, `fileDetail(input, property)`, `changeCase(text, case)`, `getFolderContents(folder, recursive)`, `getItemFromList(list, type, index, startIndex, endIndex)`, `setName(input, name, dontIncludeExtension)`, `saveFile(input, ask, path, overwrite)`, `askForInput(prompt, type, default, allowDecimal, allowNegative)`, `list(items)`, `combineText(text, combine, separator)`, `nothing()`, `alert(alert, title, cancel)` and `quicklook(input)`. All required slots are supplied. Array arguments contain native references or literal Text entries according to JellyArray serialization; actual list flattening/collection and native types remain device integration checks.

Historical pinned-source enum spellings included Files, Items, FileExtension, Name, lowercase, FirstItem, Text and NewLines. Device reports below reject FileExtension and FirstItem; archive revision 4 uses documented spaced alternatives pending recompilation. These historical spellings are not an app compatibility guarantee. No forScore binding is claimed. The first Stop and Output in each new helper is an assembly guard; remove it only after completing every applicable slot in [the assembly guide](choir-service-assembly.md).

### Remaining validation

Compile the example sources and the four production files on the chosen compiler/app build; reconcile any signature or grammar differences. Verify native action wiring, Text interpolation, presence checks, output fallback, artifact/import acceptance and installed names. Use [example tests](../tests/examples.md) for examples and the [integrated service run](../tests/choir-service.md) for production. Record exact tool versions/revisions and actual results; source inspection cannot replace these checks.

### Device-reported enum mismatch (16 October 2026)

The user reports that the archive helper fails with an out-of-scope error at each DoNothing value. The pinned-source spelling is therefore not established as compatible with this installed app. Archive revision 3 uses Respond as an export workaround; change all seven empty-result outputs to Do Nothing for no recipient in Apple Shortcuts after export. Indentation is unchanged. Corrected compilation/export remains unverified.

Archive revision 4, 16 October 2026: user reports out-of-scope FileExtension, FirstItem and archiveMatches. Updated archive to the official documentation's spaced enum forms: property File Extension, type Item at Index with index 1 (equivalent to first item). References: https://docs.jellycuts.com/Documentation/Shortcuts/fileDetail.html and https://docs.jellycuts.com/Documentation/Shortcuts/getItemFromList.html . Leave repeat-result capture unchanged pending recompilation: archiveMatches may be a cascading diagnostic from errors inside its loop. Corrected compilation remains unverified.

### Local-doc review corrections (16 October 2026)

Current block syntax candidate after repeated missing-wrapper reports: use `if(condition) {` and `repeatEach(items) {`, exactly as documented in the local If/Else and Repeat guides. Archive 6 and assembly 4 adopt these forms. Earlier unparenthesized compiler-source examples in this record are historical evidence for a different candidate toolchain, not the current installed-app recommendation. Parser cause and corrected native structure remain unverified until the user re-exports and inspects the blocks.

Latest device evidence: canonical revision 3's generated empty-input Stop and Output has no enclosing If and runs unconditionally. Revision 4 removes the guard; only two replacements and the final output remain. This establishes a generated-control-flow discrepancy in that project, not its compiler/parser cause. Do not treat other If/Repeat structures as faithfully exported without inspecting their native markers. Runtime acceptance of revision 4 is pending.

Later device evidence supersedes the earlier canonical review below: canonical revision 2's If-result capture leaves `sourceName` out of scope at line 21. Revision 3 removes that capture, uses an early empty-input return and passes ShortcutInput directly to Replace Text. No mutable variable is introduced. Filename patterns and interface remain unchanged; corrected app compilation is pending. Remaining assembly If/Repeat captures are not established as compatible merely because the older inspected compiler implements them.

Archive revision 5 supersedes the revision 4 capture approach: a documented mutable variable starts empty, receives the first native matching File and rejects a second match. `archiveMatches` and archive block-result capture are removed. Source: local [variables guide](../vendor/jellycuts-docs/markdown/Language_Guide/variables.md). The older pinned compiler's `compileVariableDeclaration` emits Set Variable but its `JellyVariableReference` maps declared values to ActionOutput references; that does not establish correct mutable-variable wiring in the installed app. Inspect the named variable references after export as detailed in CFG03. This is an app-documentation candidate, not proof that the older compiler supports this path correctly.

Assembly revision 3 replaces its remaining `FileExtension` and three `FirstItem` uses with the local [fileDetail](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/fileDetail.md) and [getItemFromList](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/getItemFromList.md) examples: `File Extension` and `Item at Index`, index `"1"`. [combineText](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/combineText.md) uses documented Custom with `" | "`, avoiding the compiler-only `NewLines` spelling. Alerts and report Text use [documented multiline strings](../vendor/jellycuts-docs/markdown/Language_Guide/strings.md). Other action slot sets match the local docs, except the already recorded Output signature conflict; retain `result`/`noResultBehavior`/`response` rather than substituting the malformed web signature. `lowercase` remains the native spelling in the inspected WFCaseType enum; no contrary device diagnostic is recorded.

Canonical revision 2 and main revision 2 were reviewed and retained. The service helper still uses If/Repeat output capture backed by inspected compiler code, pending actual app validation; the optional repeat probe remains available. No forScore library binding was found in the new snapshot, so all FS and CFG assembly requirements remain. Compilation/import/runtime are unverified; the current evidence is documentation/source review.

## Helper compatibility revision, 18 October 2026

Archive 9/interface 2.0 and assembly 7/interface 1.1 remove Output enum arguments, all getItemFromList bindings and all block-result captures. Returns use documented exit(var: ...); native ARC01-ARC03/SCORE01-SCORE02 slots handle selection and COL01-COL03 Add to Variable slots handle ordered native collections. Archive File returns now directly reference existingCleanFile/savedCleanFile; inspect exported tokens. Both initial guards remain. Config keys/call contracts unchanged. Assembly Quick Look removed after earlier failed UI fixture; FS13 and report remain. See [completion checklist](helper-compatibility-update.md). New compiler/export/device results: Not run. Native List shape, named variable wiring, collection emptiness/ordering and repeated scores still require the integrated run. MAIN is unchanged and retains the unresolved Output form.

## Archive loop-condition scope correction, revision 10

User reports revision 9 errors at archiveExtensionLower (94), archiveStem (98) and childName (123). These are If inputs captured inside Repeat bodies. Revision 10 declares the three comparison variables before their loops, captures each native action output under a distinct Result name, and assigns it to the declared variable immediately before the corresponding If. This uses the local traditional-variables guide's Magic Variable assignment pattern; it is a candidate workaround, not a confirmed compiler diagnosis. Preserve existingCleanFile/typeFolder File references, guards, config contracts and manual slots. After export, check all three If inputs use the named variables and their Set Variable actions consume the immediately preceding correct action results. Corrected app compilation/export/runtime: Not run. Source and .txt copy are byte-identical.

## Output candidate after failed Exit generation

User confirms exit() does not work and has no known working Output source line. Archive 11 / assembly 8 therefore test exactly the local Output documentation signature with optional enum omitted: output(notes: "..."). No result/noResultBehavior/response or folder argument is used. Reference: jelly/vendor/jellycuts-docs/markdown/Documentation/Shortcuts/output.md. This is documentation-backed but not compiler/device-confirmed. All validation/guard/service returns use this candidate. Archive success outputs are intentionally empty placeholders at CFG03/CFG04 and must be wired to native existingCleanFile/savedCleanFile in Shortcuts. Inspect native stops within every branch, guard and success return before execution; successful compilation alone is insufficient. New compile/export/runtime results: Not run. Naming helper and main are unchanged; naming retains its separately reported manual repair and main its unresolved older Output binding.

Archive 12 / Assembly 9: replaced entire affected If blocks with AV/SV native If-Alert-Stop-End If slots after user reports both message and stop missing in export. Removed generated Output/Exit calls, including guard/final returns; AGUARD/SGUARD MUST be inserted as native stops before any execution, and ARETURN/SRETURN must be completed. Existing manual slots remain. This is a manually completed template, not a claimed automatic export fix. Compilation/export/runtime of these revisions: Not run. See native-validation-blocks.md for all conditions/messages/results.

## Restored documented If/Output validation (Archive 13 / Assembly 10)

User explicitly requested executable source fixes instead of native validation slots. Replaced all 30 AV/SV slots with full parenthesized If blocks. Failure bodies directly call output(notes: "ERROR: descriptive problem"); separate Alert/Text/Exit generation is removed from those branches. Initial guards and final assembly report also use direct Output. Optional folder enum omitted per vendored output.md. Successful archive-reuse If is restored; CFG03/CFG04 require native File result tokens because documented Output accepts String, not a demonstrated native File parameter. Assembly uses documented getType(input: cleanFile), with a predeclared comparison variable, to propagate Text errors before import. Archive completed interface is 2.1 (File success / ERROR: Text failure), assembly completed interface remains 1.1. No manual validation/guard/report construction is requested. Existing native provider/list/forScore slots remain. Docs support this syntax; original branch omission cause is not established. New compilation/export/runtime: Not run. Check missing-prefixRegex error and stop, plus saved/reused native Files, during the integrated run.

## Device-confirmed flush-left If/Output fixture

User reports both the unparenthesized and flush-left probes warn about missing noResultBehaviour and response content in output. The flush-left parenthesized probe nevertheless exports/runs and returns Conditional output reached; the output inside the If therefore exists and returns in this fixture. Earlier parenthesized/indented probe exported the If without its Output; unparenthesized probe exported no If. Positional payload avoids the observed literal notes: prefix. Archive 14 and Assembly 11 apply flush-left executable source and positional output("...") throughout; preserve multiline string content. New full helper compilation/export/runtime: Not run. Keep missing-parameter warnings unresolved rather than claiming a clean compile or guessing named arguments. Conditional interpolation, nested control flow, native object transport and CFG03/CFG04 File returns still need the integrated device check. AGENTS formatting instructions now record this device-backed exception. No native AV/SV validation construction is requested.

## User-confirmed Archive 14 export/import

The user confirms UTIL - Archive Choir PDF revision 14 loaded correctly into Apple Shortcuts and all Output actions are present as expected. This confirms the full archive's export/import action-presence result, extending the earlier flush-left probe. Parenthesized If, flush-left bodies and positional output("...") are the current device-supported forms. Do not generalize this result to Assembly 11, native slot completion, File returns or end-to-end archive execution: those remain unverified. Prior missing noResultBehaviour/response warnings have not been reported resolved. Next: complete ARC01-ARC03 and CFG02-CFG04, retain the initial guard until completion, then check a missing-config-key error and native save/reuse results using disposable input.
