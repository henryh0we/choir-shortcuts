# Jellycuts editor versus Shortcuts compilation actions

Recorded 5 November 2026 from user-reported iPad action inspection. No device
execution, screenshots or exported artifacts were captured in this repository.
Exact current iPadOS/Jellycuts versions and compiler/library builds were not
recorded; do not assume the earlier device profile still applies.

## Confirmed comparison

The following minimal source eventually generated the expected actions when
entered directly in the Jellycuts editor:

```jelly
import Shortcuts
nothing() >> emptyValue
var currentValue = emptyValue
quicklook(input: currentValue)
```

| Compilation path | User-reported generated actions |
| --- | --- |
| Direct Jellycuts editor | Nothing named emptyValue, Set Variable currentValue connected to it, then Quick Look; connections reported correct. |
| Compile Jelly Text in Apple Shortcuts | Only Set Variable currentValue, referencing missing/broken emptyValue. Nothing and Quick Look absent. |
| Compile Jelly File in Apple Shortcuts | Same incomplete result as Compile Jelly Text. |

Direct-editor incremental checks also succeeded: Text alone; Text output named
greeting using `>>`, usable by a subsequent Set Variable; Nothing alone named
emptyValue; Nothing followed by Set Variable; finally the complete example above.
These establish generated-action inspection only, not runtime acceptance.

An earlier attempt entered directly in the editor was reported to produce the
same incomplete result. Later incremental editor tests and the final comparison
succeeded. Preserve this discrepancy: the evidence does not establish that the
editor always succeeds or identify what changed between those attempts.

## Original G1A symptoms and limits

Compiling [g1a-presence.txt](g1a-presence.txt) through Compile Jelly Text produced
an unexpected Calculate/Divide action containing the Dependencies header text,
followed by Stop This Shortcut, then remaining comments and functionality.
Changing the specification comment wording produced a different incomplete
export with no header comments and a broken currentValue assignment.

The repository's G1A `.txt` and `.jelly` copies were checked during this
investigation: byte-identical, LF line endings, no UTF-8 BOM. The known local
CRLF compiler defect therefore does not explain those repository bytes. The
bytes delivered to the iPad were not independently captured.

Earlier suggestions that comment punctuation or the word `return` caused the
fault were hypotheses, not established diagnoses. The later comparison points
to a difference involving the Shortcuts compilation paths; its mechanism is
unresolved. It does not justify rewriting valid action calls or comments across
the repository. The original full G1A source still needs a direct-editor comparison;
its presence-condition generation and expected runtime previews remain untested.

## Current development route

Transfer source from the PC, then compile/export from the Jellycuts editor and
inspect the generated actions. Avoid relying on Compile Jelly File or Compile
Jelly Text for this workflow until the minimal example generates all three
actions with intact connections. Keep malformed exports untouched for comparison;
manual reconnection would conceal the generation failure.

### Proposed source-file handoff: not yet tested

The user wants to select a `.txt` source in Files and open it as editable Jellycuts
source, without invoking either compilation action. The following is a candidate
manual Shortcut named **Save to Jellycuts**, not a confirmed app capability:

1. Add Select File, with multiple selection off.
2. Add Share, passing the selected File directly.
3. Select a `.txt` source and look for Jellycuts in the share sheet, including More.
4. If available, choose Jellycuts and check whether the source opens in its editor.

Only after that works, enable Show in Share Sheet, accept Files, and replace
Select File with Shortcut Input. The intended launch is Files → Share → Save to
Jellycuts → Jellycuts. This still requires choosing a share destination; automatic
save/open, file persistence, replacement behaviour and an import URL scheme have
not been established. If Jellycuts is absent or does not open editable source,
this proposed handoff is not validated. Do not substitute a compilation action.

## Next evidence to capture

- Exact device/app versions, action settings, input producer and input type.
- Exact source bytes/hash, compiler messages, and screenshots or exports from
  both paths using the same minimal example.
- Direct-editor result for the unchanged full G1A source.
- Whether the proposed Share handoff opens an editable source document.

Minimal bug-report summary: the example above generates Nothing → Set Variable
→ Quick Look in the successful direct-editor test, but both Shortcuts compilation
actions generate only Set Variable with a dangling emptyValue reference.
