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

For richer interfaces, pass one native Dictionary with explicit case-sensitive keys, field types/defaults, and output/error rules. Prefer lowerCamelCase keys for new contracts; preserve existing conventions when reusing established components. Verify Jelly Dictionary construction and key operations on the actual compiler. Do not use JSON serialization merely to connect native Shortcuts.

Simple components return simple values. A structured success/error envelope is optional; define its native Boolean/value representations and omitted-versus-present fields before implementation. Native action failures can abort a run without returning an envelope. Type conversion, cancellation, missing permissions, and missing dependency behaviour must be documented and tested.

## Choir service release 1

The [build guide](choir-service-build.md) and [assembly guide](choir-service-assembly.md) define the current production architecture. All four Shortcuts now have Jelly source. The main passes Text `interactive` to assembly and receives Text; naming uses Text too. Native Files pass between archive and assembly; their return fields are completed at CFG slots. Native Scores and Setlists stay within assembly, inserted at FS slots. Comments provide instructions and Nothing actions serve as temporary outputs; reconnect their native consumers after inserting real actions. Both incomplete helpers have initial Stop and Output guards. Neither helper calls the main; archive depends only on naming.

Service ordering is confirmed interactively. Original canonical stems remain lookup keys, with readable score titles and composer assignment in forScore. Archive configuration belongs only to Archive Choir PDF. Source updates regenerate templates, so preserve a completed installed copy before replacement and reapply the native insertion/CFG checklist. Manual insertions do not round-trip into Jelly source. This release uses Files selection (which may download early), reviewed metadata, and explicit replacement of a chosen service. It does not claim unattended processing or a transactional update.

Use `runShortcut` for separate installed components. Functions/macros remain implementation details inside a source file and do not satisfy an independently useful component requirement. Verify any generated self-dispatch against the compiler profile and installed name before using it.

Compatibility changes require a caller audit, interface version change where appropriate, recompile/reimport instructions, and tests for affected integrations. The [dependency inventory](dependencies.md) is the starting point; also search all source and relevant manual designs for names and keys. Never silently overwrite an installed component with incompatible behaviour.
