# Architecture and contracts

Design complete projects before individual files. Main Shortcuts own user interactions and orchestration. Reusable Shortcuts own focused behaviour with explicit native inputs/outputs. A shared component should justify the cost of compiling, installing, and testing it; no separate core layer is needed yet.

The example flow is:

```text
MAIN - Jelly Greeting Demo
    Creates one Text value: Henry
    Calls UTIL - Jelly Format Greeting with that variable
        Uses incoming Text, or Friend when it has no value
        Produces one greeting Text and explicitly outputs it
    Explicitly outputs the returned greeting
    Respond displays it when there is no output recipient
```

The utility is independently useful with its default. The main is a fixed-input demonstration rather than an interactive production workflow. It ignores incoming content and introduces no prompt. These installed names deliberately differ from the sibling manual examples.

Source headers own each contract. Specify cardinality, native type, missing/empty/whitespace behaviour, direct/called execution, output, side effects, dependencies, and unsupported contexts. Missing input does not prove direct launch; neither example attempts to infer its caller.

## Required first-line shortcut name

Every new source or Jellycuts code/paste snippet, and source revised for delivery,
starts on its first physical line with this ordinary comment:

```text
// <exact installed shortcut name> | Purpose/role: ... | Specification revision: ...; interface ... | Contract: ... | Dependencies: ...
```

The name is the first pipe-separated segment after `//`, without a label such as
`Installed name:`. Do not put a blank line or preamble before it, or use `|` inside
the name. Keep header metadata on that same physical comment line; editor soft
wrapping is fine. Preserve existing exact installed names and native completion
comments beside the actions they describe. Matching `.jelly`/`.txt` copies use the
same header; intentional historical mismatches remain evidence, not migration targets.

The [Copyover helper](ipad-copyover-compiler.md) extracts and trims this name to
prefill an editable name prompt. Its compiler input remains the complete original
sourceText. The user's edited answer supplies the existing naming field. This
does not rename dependencies, set Jelly metadata, or change the file-based
pipeline's explicit/history-based name selection. Do not rewrite historical
fixtures or working installed shortcuts merely to apply the convention.

7 November 2026: automatic naming from the G2A first comment is confirmed by user
report. G2A still outputs only `0`; collection runtime remains unresolved.

For richer interfaces, pass one native Dictionary with explicit case-sensitive keys, field types/defaults, and output/error rules. Prefer lowerCamelCase keys for new contracts; preserve existing conventions when reusing established components. Verify Jelly Dictionary construction and key operations on the actual compiler. Do not use JSON serialization merely to connect native Shortcuts.

Simple components return simple values. A structured success/error envelope is optional; define its native Boolean/value representations and omitted-versus-present fields before implementation. Native action failures can abort a run without returning an envelope. Type conversion, cancellation, missing permissions, and missing dependency behaviour must be documented and tested.

## Config-based choir service

28 October draft extension: Archive 2.2 optionally accepts fourth Text
`with-category` and returns native List `[PDF File, category Text]` instead of
the default PDF. Legacy three-item callers keep their contract. Assembly 18
extracts that context and assigns the category as Genre only for missing-score
imports. Category reuse is resolved within configured folders, not by parsing
provider paths or storing shared state. Native return/Genre slots are not yet
device-verified; migration and tests are in the
[Genre update guide](ipad-genre-update-guide.md).

See [config integration](config-integration.md) for current contracts and migration. Assembly reads config.json once from its single native Choir Music root, validates required values, resolves Library and passes a native three-item List (PDF, Library Folder, parsed Dictionary) to archive. Naming receives a two-Text List (filename, configured prefixRegex). Dictionary construction of native Files is avoided because the inspected writer does not establish preservation of those types. Native List transport remains a device check.

Main keeps its existing Text launch contract with assembly. Config is an immutable snapshot for a run; the next run rereads it. Archive still scans Library per PDF, rejects duplicate canonical matches and resolves category names to immediate native child Folders. No manifest, persistent index or service-folder copy is created. Native forScore actions remain FS slots inside assembly. Working scores stay native, using named variables in place of rejected If-result captures. Repeat-result captures still require export inspection.

Preserve earlier installed manual edits before replacing the set. Config/File/Folder slots, native result wiring, control-flow markers and loop variables must be checked on the iPad before removing guards. Source changes do not round-trip native edits. Earlier successful naming/save fixtures are not tests of the new interfaces.
