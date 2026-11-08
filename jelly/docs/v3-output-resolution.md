# V3 output resolution: revision 3

Follow-up: parser remains revision 3; preview is now revision 4 to address a reported false no-music-selected result. Interface 2.0 and the no-output/exit strategy are unchanged. See the [latest selection checkpoint](../tests/v3/README.md#latest-checkpoint-preview-revision-4-8-november); only preview needs replacing for that correction.

8 November 2026. Source-level replacement for the rejected manual-stop proposal. Both installed names stay the same. Both sources are specification revision **3**, interface **2.0**; replace the parser first, then the preview. No manually inserted blocks are required by this design. No compilation or execution has been performed here.

## Latest device evidence

The user reports the intended Friday parsed row and picker count 1 with preview revision 4. This supports the parser-to-preview result and report path for that one file. Standalone quote-pair display artifacts remain. Native return type, exact hashes/versions/repairs and other branches were not independently recorded. See the [reported pass](../tests/v3/README.md#reported-pass-friday-filename-8-november-2026). Older not-tested statements below describe the original proposal; this narrow result supersedes them only for the reported integration.

## What the commit history actually establishes

- `a97c0b1` changed rejected Output calls to documented exit(var: ...). Later records explicitly say exit did not work; it is not an established fallback.
- `76ac03e` introduced native validation/stop placeholders. `5a45f3a` subsequently removed that approach and restored executable validation, recording parenthesized Ifs, flush-left bodies and positional output("..."). The record includes successful full Archive output-action presence, not just the isolated probe.
- `f47c848` records the isolated positional Output test generating the expected Stop and Output action with no-recipient Do Nothing, alongside unresolved missing-parameter warnings.
- V3 revision 1 already used this same positional form. The new report identifies Move Notes to Folder at those call sites. Reapplying the old spelling or guessing another named signature does not resolve that contradictory device observation.
- Revision 2's 27 manual return/stop slots were a proposed workaround, not a device-tested fix. The user rejected that maintenance burden. They are removed from revision 3.

The internal Jellycuts cause remains unknown without the actual generated action identifiers/compiler profile. The observed incorrect action generation is established by user report. A binding/registry mismatch is a hypothesis, not a proven diagnosis. Preserve the old successful reports alongside this failure.

## Source-level solution

Avoid both problematic return bindings altogether. Use ordinary control flow and finish with a native value-producing action:

1. Initialise a named runState to ready.
2. Validation failures assign error and record a message, rather than invoke a stop action.
3. Each later dependent phase runs only while runState is ready. Inside the rule/file repeats, that check also gates later iterations. There is no recursion or self-call.
4. The parser always constructs one result Dictionary. On controlled validation failure it sets status=error and reason=the message, clearing parsed identity fields. On success it uses parsed/skipped/unresolved as before.
5. The parser's last executable action is Get Dictionary from the final result Dictionary, outside every If/Repeat. The shortcut reaches normal completion with that action's native result; there is no Stop and Output action to miscompile.
6. The preview reads schemaVersion/status/reason from the returned Dictionary, stops processing further selections by setting its own error state when needed, displays the accumulated report, and ends with Get Text from the current named report.

Values used across guarded phases are predeclared named variables; generated consumers must read their current value rather than their Nothing/empty initializer. No If-result capture, inferred implicit branch result, new language keyword or Dictionary-to-Text serialization is used for the parser's final result.

This replaces early exits structurally, not by changing the message syntax. It also preserves earlier preview rows if a later file encounters a parser/config error. Native malformed-JSON/regex failures and picker cancellation may still abort before normal completion; this design does not add exception handling.

## Contract change

Parser interface/result schema advance to **2.0 / schemaVersion Text 2**. Controlled errors now return the same native Dictionary shape as other results, with status Text error. ERROR Text is no longer an alternate parser return type. Config version stays **3**. Install both new sources together; a revision-1/2 parser is incompatible with the new caller.

The preview interface is 2.0 because it consumes the new parser contract and finishes naturally rather than through an explicit generated stop. The intended report Text output remains.

## Manual iPad check, without inserting blocks

1. Recompile/import V3 - Parse Filename revision 3, then V3 - Preview Filenames revision 3. Select the exact parser target in Run Shortcut if the export does not retain it. No source-native completion slots exist.
2. Inspect that neither generated shortcut contains Move Notes to Folder, Stop and Output placeholders, or an unexpected self-call. Helper ends with Get Dictionary; preview ends with Get Text after Quick Look.
3. Run the preview with the same config and Fri1-Clucas-Responses.pdf. Expected: parsed, fri, evensong, Evensong, 1, Clucas-Responses. No Notes UI.
4. Check the caller actually receives schemaVersion 2/status/reason and displays a result. Natural completion returning the final native Dictionary through this exact Jellycuts/Shortcuts combination is the remaining boundary to confirm; source review is not device evidence.
5. With a disposable config version 1, expect an error report and no music picker. Run the parser without arguments: expect a result Dictionary with status=error, not continued config decoding. A direct no-input run must be configured to allow Shortcut Input to be absent for this source path to execute; otherwise native receiving settings may stop first.
6. Remove a required slot/rule field in a disposable config, then check an error result without dependent processing or Notes prompts. Finally retry the valid file to check error state resets on a new run.

Do not broaden the manual matrix until this caller/result boundary works. If it fails, capture the final generated Get Dictionary and the caller's actual result. We will fix that one boundary in source; a failure does not justify returning to dozens of native insertions.

## Limits of the evidence

Normal completion is the proposed return path for this implementation; it is not a newly discovered historical fix and has not been device-verified here. The documentation-backed Get Dictionary/Get Text actions produce native results, but their exact generated connections and whole-shortcut caller behavior still require the user's manual check. No guarantee of runtime success is claimed.
