# Jelly language and toolchain reference

Reviewed 2026-10-14; documentation integration updated 2026-10-16. This is a repository-specific evidence record, not a complete language specification. **Source-backed** means checked in official documentation or upstream code; **compiled** requires actually running the chosen compiler. No successful compilation, import or device execution is recorded here; device-reported compilation failures are preserved below and in the compatibility record.

The candidate source profile is Open-Jellycore commit `e1ec31c2ee192c8721749f9eb3b50108e38891cf`, inspected through the official GitHub repository/API. The user-reported profile is Jellycuts 2026.6.4, iPadOS 26.6 and forScore 15.2.5. Bundled compiler and action-library revisions remain unknown; the candidate source revision is not an established app match. Examples must be compiled against the actual toolchain before compatibility is claimed. English editor conventions are used here.

Use the [local documentation index](jellycuts-docs-index.md), pinned at docs commit `19306be1dd30c20e12058ebe144dd8342e64ca39`, and [compatibility evidence and probes](../tests/compatibility/README.md) before changing syntax. Exact device-tested forms take precedence for the recorded profile. The [vendor README](../vendor/jellycuts-docs/README.md) records provenance, licensing status and refresh instructions. No successful probe results have been recorded.

## Primary sources

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

- [Comment compilation](https://github.com/OpenJelly/Open-Jellycore/blob/e1ec31c2ee192c8721749f9eb3b50108e38891cf/Sources/Open-Jellycore/Core/Compiler/Compiler.swift) handles both comment and blockComment nodes and emits native Comment actions. Block comments in the new sources are real instruction cards, not a guessed comment function.
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

Later device evidence supersedes the earlier canonical review below: canonical revision 2's If-result capture leaves `sourceName` out of scope at line 21. Revision 3 removes that capture, uses an early empty-input return and passes ShortcutInput directly to Replace Text. No mutable variable is introduced. Filename patterns and interface remain unchanged; corrected app compilation is pending. Remaining assembly If/Repeat captures are not established as compatible merely because the older inspected compiler implements them.

Archive revision 5 supersedes the revision 4 capture approach: a documented mutable variable starts empty, receives the first native matching File and rejects a second match. `archiveMatches` and archive block-result capture are removed. Source: local [variables guide](../vendor/jellycuts-docs/markdown/Language_Guide/variables.md). The older pinned compiler's `compileVariableDeclaration` emits Set Variable but its `JellyVariableReference` maps declared values to ActionOutput references; that does not establish correct mutable-variable wiring in the installed app. Inspect the named variable references after export as detailed in CFG03. This is an app-documentation candidate, not proof that the older compiler supports this path correctly.

Assembly revision 3 replaces its remaining `FileExtension` and three `FirstItem` uses with the local [fileDetail](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/fileDetail.md) and [getItemFromList](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/getItemFromList.md) examples: `File Extension` and `Item at Index`, index `"1"`. [combineText](../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/combineText.md) uses documented Custom with `" | "`, avoiding the compiler-only `NewLines` spelling. Alerts and report Text use [documented multiline strings](../vendor/jellycuts-docs/markdown/Language_Guide/strings.md). Other action slot sets match the local docs, except the already recorded Output signature conflict; retain `result`/`noResultBehavior`/`response` rather than substituting the malformed web signature. `lowercase` remains the native spelling in the inspected WFCaseType enum; no contrary device diagnostic is recorded.

Canonical revision 2 and main revision 2 were reviewed and retained. The service helper still uses If/Repeat output capture backed by inspected compiler code, pending actual app validation; the optional repeat probe remains available. No forScore library binding was found in the new snapshot, so all FS and CFG assembly requirements remain. Compilation/import/runtime are unverified; the current evidence is documentation/source review.
