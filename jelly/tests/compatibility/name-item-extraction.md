# Source-based replacement test for NAME01/NAME02

21 October 2026. Independent test:
[probe-name-items-indexed.jelly](probe-name-items-indexed.jelly), also available
as the byte-identical [text transfer copy](probe-name-items-indexed.txt).
Intended installed name: `TEST - Jelly Name Items Indexed`.

This first test is self-contained. Its fixed List models the naming helper's
two inputs: filename Text, then prefixRegex Text. It selects indexes 1 and 2
entirely in Jelly, with no manual Get Item from List insertions. Two Quick Look
actions display the extracted values separately, avoiding the known local
interpolation defect and the separate Output-signature mismatch.

The executable source is:

```jelly
import Shortcuts
list(items: ["Fri1-TestComposer-TestPiece.pdf", "^Fri[0-9]+-"]) >> namingInput
getItemFromList(list: namingInput, type: ItemAtIndex, index: "1", startIndex: "", endIndex: "") >> filename
getItemFromList(list: namingInput, type: ItemAtIndex, index: "2", startIndex: "", endIndex: "") >> prefixRegex
quicklook(input: filename)
quicklook(input: prefixRegex)
```

The [vendored action page](../../vendor/jellycuts-docs/markdown/Documentation/Shortcuts/getItemFromList.md)
documents the argument slots but shows spaced `Item at Index`. The pinned local
compiler enum defines raw `ItemAtIndex`; this candidate follows that source and
supplies all slots, including the unused empty range arguments. The older
[probe-list-item.jelly](probe-list-item.jelly) retains the spaced form as historical
evidence. Bare ItemAtIndex has also previously failed in the larger iPad naming
helper. Therefore this is an isolated test of a locally accepted form, **not an
already established iPad fix** or an assertion that supplying all slots resolves
the earlier app error.

## Local result

Command from the repository root:

```powershell
python jelly/scripts/build.py jelly/tests/compatibility/probe-name-items-indexed.jelly
```

Open-Jellycore `e1ec31c2ee192c8721749f9eb3b50108e38891cf`, built with Swift
6.4.1 inside Ubuntu WSL2: **passed compilation and the build wrapper's structural
checks**, raw CLI status 0, wrapper status 0, no compiler diagnostics.

The exported non-comment actions were inspected:

1. List containing the two exact literal Text items.
2. Get Item from List, `WFItemIndex: "1"`, input UUID references that List.
3. Get Item from List, `WFItemIndex: "2"`, input UUID references the same List.
4. Quick Look references the first selection's UUID.
5. Quick Look references the second selection's UUID.

The local binding emits selector field `type: "Item At Index"` and empty range
fields. This is the compiler's observed serialization; it is **not independently
validated against Apple's complete action schema**. The wrapper's structural pass
does not prove that Shortcuts interprets this selector correctly. Inspect the
iPad-generated action settings and actual results below. No compiler patch or
generated-file repair was used, and no production NAME slot was removed.

Unsigned local export and logs:
`jelly/build/tests/compatibility/probe-name-items-indexed.shortcut`,
`.build.json`, `.stdout.log`, `.stderr.log`. The JSON records source/output hashes.
No signing, import or device execution was performed locally.

## iPad result for the original indexed probe

The user reports rejection at lines **13 and 14**: the variable `itematindex`
does not exist in scope. These are the two `getItemFromList` calls using bare
`ItemAtIndex`. This confirms the same failure in the isolated, full-slot form;
adding the unused range arguments did not resolve the app discrepancy. The original
probe and its transfer copy are preserved unchanged as failed evidence. No
generated-action inspection or runtime pass is available for this rejected source.

## Original probe's inspection procedure (for reference)

1. Open the `.jelly` source in Jellycuts (or paste the `.txt` contents). Compile
   **without changing the selector or inserting manual actions**. Record exact
   errors/warnings and the app/device versions. If rejected, stop and retain that
   result; do not replace the working naming helper.
2. If accepted, export and inspect both Get Item from List actions: each must use
   the same two-item List; mode must be **Item at Index**; indexes must be **1**
   and **2**, respectively. Check the two Quick Look inputs reference different
   selection outputs. A silently defaulted First Item selector is a failure.
3. Import under the intended diagnostic name, run in the foreground, and dismiss
   each preview to continue. Expect first `Fri1-TestComposer-TestPiece.pdf`, then
   `^Fri[0-9]+-`. Seeing the filename twice is a failure even if compilation passed.
4. Repeat while supplying unrelated caller input: the same two fixed values
   should appear, since this diagnostic ignores Shortcut Input. No Files/provider
   access, saves, imports or forScore writes should occur.
5. If Quick Look reports the previously observed UI-context error, record it
   separately. It does not establish success or failure of extraction. Preserve
   the generated selection actions and their settings for diagnosis.

| Stage | Actual evidence |
| --- | --- |
| Local compilation | Passed |
| Local basic structural export checks and UUID/index inspection | Passed, with selector-schema caveat above |
| Exact-source iPad compilation | Failed by user report: selector variable not in scope at lines 13/14 |
| iPad selector/index inspection | Not reached because compilation failed |
| iPad first/second value execution | Not reached because compilation failed |
| Production NAME01/NAME02 replacement | Not applied |

If a candidate passes on the iPad, the next step is an input-driven probe with the same
calls reading the incoming native two-Text List. That checks the receiving-type
boundary before removing NAME01/NAME02 from the production helper. This first
test alone does not validate that boundary or native File/Score extraction.

## Next candidate: declare the selector identifier

Use [probe-name-items-declared-selector.txt](probe-name-items-declared-selector.txt)
([Jelly source](probe-name-items-declared-selector.jelly)), installed name
`TEST - Jelly Declared Selector`. It keeps the same fixture, two indexed calls
and previews, but adds this declaration before the List:

```jelly
var ItemAtIndex = "Item At Index"
```

This is a bounded diagnostic hypothesis: the app's error says the bare identifier
is not in scope, so this candidate puts that identifier in scope. Traditional
variables (including capitalized names) are documented in the
[variables guide](../../vendor/jellycuts-docs/markdown/Language_Guide/variables.md).
The identifier and serialized value are taken from the pinned local enum source.
That local enum initializer reads the identifier's content, so a local pass does
not prove the declared variable's value is evaluated as an enum by the iPad.
The app's internal parameter resolution is unknown. This is **not** a claim that
Text and enum arguments are interchangeable or that declaring an enum name is
the documented general solution. We are not repeating the already rejected quoted
enum argument or changing the production helper.

Compile the candidate unchanged on the iPad. If accepted, check the actual mode
is Item at Index, with indexes 1 and 2, and run both previews. Do not count the
disappearance of the scope error alone as a pass. Wrong/default selector modes,
two identical results, or a new error are failures to record. No manual repairs
should be made to this diagnostic before recording the result.

Local candidate compilation/export inspection: **Passed** with wrapper/raw status
0 and no diagnostics. The declaration generated Text/Set Variable actions; both
selection actions still export indexes 1/2 with `type: "Item At Index"`, share
the fixture List input, and feed distinct preview UUIDs. The `.txt` transfer copy
is byte-identical. The selector-schema caveat from the original test still applies.
### iPad result: compiles/runs, but selector generation fails

The user reports that this declared-selector candidate compiles and runs. Their
Shortcuts editor screenshot shows the expected Text `Item At Index` and Set
Variable `ItemAtIndex` generated by the declaration, followed by the fixed List.
However, **both Get Item from List actions are configured as First Item**, not
Item at Index 1 and 2. The Quick Look inputs are labelled filename and prefixRegex,
but those labels do not correct the two producers' selection mode. The visible
result is the filename. The user has not separately reported each preview's value;
the generated selectors themselves already fail the required inspection.

Classification: **app compilation accepted; user reports execution; indexed
extraction failed generated-action inspection**. The declaration only bypassed
the scope error; it is not a working source replacement for NAME01/NAME02.
Preserve this source and its transfer copy as failed evidence. Do not apply the
workaround to production, generalize it to other enums, or count successful
compilation/execution without the expected results as a test pass.

The local export inspection already observed `type: "Item At Index"`. The
installed local binding serializes its Swift property named `type` without an
explicit CodingKeys mapping. The screenshot is consistent with a selector that
was omitted, ignored or serialized under an unexpected field/value by the iPad
compiler. It does not identify that app's exact internal cause. Correct selector
serialization requires further evidence; merely declaring more enum names is
not a justified repair. Native NAME01/NAME02 remain required in production.

## Next candidate: avoid selectors with a loop

Use [probe-name-items-loop.txt](probe-name-items-loop.txt)
([Jelly source](probe-name-items-loop.jelly)); intended name
`TEST - Jelly Name Items Loop`. The fixed two-Text fixture is unchanged, but
there is no enum declaration and no Get Item from List call. It initializes
two named Text variables, repeats over the fixture, and assigns Repeat Item to
filename when RepeatIndex is 1 or prefixRegex when it is 2. The previews consume
the current named variables after the loop, not their empty initial Text actions.

This combines the [documented Repeat Each](../../vendor/jellycuts-docs/markdown/Language_Guide/repeat.md),
[variables](../../vendor/jellycuts-docs/markdown/Language_Guide/variables.md) and
[If](../../vendor/jellycuts-docs/markdown/Language_Guide/if_else.md) forms. Unspaced
RepeatIndex/RepeatItem come from pinned compiler tests and existing project
patterns. Parenthesized blocks and flush-left bodies follow the recorded app
evidence. It is a distinct extraction algorithm, not another selector spelling.
It has not been established that the combination works on the iPad.

Local command:

```powershell
python jelly/scripts/build.py jelly/tests/compatibility/probe-name-items-loop.jelly
```

Actual local result: raw/wrapper status 0, unsigned export generated; **six
`Unable to get core node` warnings** mentioning braces. Do not call this a clean
compiler pass. Inspection of the exported graph found the Repeat Each start,
both conditional start/end pairs testing Repeat Index against 1 and 2, an
assignment of Repeat Item to the corresponding variable inside each branch,
the repeat end, and both previews using the named variables. Start/end grouping
identifiers and branch/loop nesting were checked. No Get Item from List selector
is emitted. This checks the represented graph, not Apple's entire action schema
or actual runtime interpretation of the condition values/variable types.

### iPad procedure

1. Compile this new source unchanged; record any errors or warnings.
2. Inspect the generated Shortcut. It should initialize filename/prefixRegex,
   repeat over the two-item List, and contain two If blocks **inside** that repeat:
   Repeat Index is 1 sets filename to Repeat Item; Repeat Index is 2 sets
   prefixRegex to Repeat Item. There should be no First Item selectors.
3. Check each preview is **after** End Repeat and reads its named variable's
   current value, not the initial empty Text output.
4. Run in the foreground. Dismiss the first preview to continue. Expect
   `Fri1-TestComposer-TestPiece.pdf`, then `^Fri[0-9]+-`. Empty or repeated values,
   missing/misplaced If bodies, or incorrect variable tokens are failures.
5. Record the generated settings/results before applying any manual repair.
   If preview UI fails, distinguish that from the extraction result.

Exact-source iPad compilation: **Failed by user report** at lines 15/18:
the variables `1` and `2` do not exist in scope. These are the unquoted numeric
operands in the two If conditions. Generated-action inspection and two-value
execution were not reached. Preserve this source unchanged as failed evidence.
Earlier failed probes and production NAME slots remain unchanged.
Only after this fixture passes should an incoming-List version be tried at the
real naming-helper boundary. Do not claim native File/Score extraction from this
Text-only test.

## Next candidate: quoted loop-index comparisons

Use [probe-name-items-loop-text.txt](probe-name-items-loop-text.txt)
([Jelly source](probe-name-items-loop-text.jelly)), installed name
`TEST - Jelly Name Items Text Index`. It keeps the loop algorithm but changes
only the executable comparison operands to documented Strings:

```jelly
if(RepeatIndex == "1") {
filename = RepeatItem
}
if(RepeatIndex == "2") {
prefixRegex = RepeatItem
}
```

The If guide explicitly permits a Variable compared with a String. The user's
scope errors identify the unquoted operands, so this candidate uses that form;
it does not declare misleading variables named 1/2 or change the production helper.
Whether the app's Repeat Index condition evaluates these quoted operands as
intended still needs actual device testing.

Compile unchanged on the iPad. If accepted, inspect Repeat Index comparisons
against literal 1 and 2 inside the repeat, the two Set Variable inputs from Repeat
Item, and the current named-variable preview inputs after End Repeat. Then run:
the first preview must be the filename and the second the regex. Blank or repeated
values are failures; a compile pass alone is insufficient.

Local compilation/export inspection: raw/wrapper status **0**, unsigned export
generated, with the same six brace/core-node warnings. Both condition operands
are exported as `WFConditionalActionString` values `1` and `2`; assignments are
inside their respective conditional groups, and both named previews follow End
Repeat. The transfer copy is byte-identical. This is the same observed operand
representation as the numeric-source candidate in the local export; it does not
establish how the iPad compiler will handle the source quotes or runtime comparison.
Exact-source iPad compilation, action inspection and runtime: **Not run**.
