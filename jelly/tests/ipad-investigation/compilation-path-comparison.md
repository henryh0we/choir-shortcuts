# Jellycuts editor versus Shortcuts compilation actions

## Latest pipeline evidence, 5 November 2026

**Single-comment candidate: runtime passed by user report.** After the requested
Compile Jelly Text experiment, the user reports no random calculation blocks or
similar anomalies and EMPTY ABSENT then FILLED PRESENT. The candidate joins all
eight original header comments into one physical // line; executable bytes are
unchanged. The original headered failures remain valid observations. This supports
the combined-comment variant for this input, but does not isolate comment count
from changed line boundaries/separators. Exact build/hash, installed name,
complete action/token inspection, versions and repair history remain unconfirmed.
See [the experiment](../pipeline/README.md#single-large-header-comment-experiment).

**Header-free candidate: editor generation and runtime passed by user report.**
The Calculate block is gone, all four If statements are reported correct, and
execution shows EMPTY ABSENT then FILLED PRESENT as expected. This implicates
the removed header content, without identifying a particular triggering comment.
Exact consumed hash, versions and any native repairs remain unconfirmed. This
report belongs to the separate candidate, not the original headered request.
The subsequent Compile Jelly Text comparison also passed runtime by user report:
no Calculate block or unexpected Stop actions, then EMPTY ABSENT followed by
FILLED PRESENT. Installed name and complete four-If inspection were not separately
confirmed for that attempt. Exact build/hash and repair history remain unconfirmed;
this report is not attached to the original headered request. Repeated reliability
and the specific header trigger remain untested.

**Latest editor comparison:** the user copied the same G1A code into Jellycuts,
compiled and built through the editor, and reports the same erroneous Calculate
box; they state another screenshot would look exactly the same. No second image
was supplied. This disproves isolation of this G1A defect to Compile Jelly Text.
The exact shared internal component and triggering source feature remain unknown.
Do not continue presenting the editor as a verified solution for full G1A.

The user now reports successful three-action minimal-variable generation through
the compiler helper after locally copying the request folder, and confirms its
variable token is correct. That supersedes the earlier failure only for this new
minimal attempt; exact consumed hash/versions/settings were not supplied.

The subsequent full original G1A attempt via Compile Jelly Text reproduces the
earlier header anomaly. A screenshot supplied in chat shows three intended header
Comments followed by a division/calculation action whose operand contains the
Dependencies header text, then an unexpected Stop this shortcut, then more
Comments. G1A's source contains neither that calculation nor that stop. No inference
about all unseen downstream actions is made. This is incorrect generated output,
not proof that the source itself is invalid or that comment punctuation/return
caused the problem.

The shared exchange has a matching request
`20261105T232511572676Z-a8d9428214e646b8a8cb603b6c1f83a6`, submitted from
g1a-presence.jelly, SHA-256
`9052558758e35e63d3928d3ae79bbe5fa0a2094da87c5c5169bcc87c1b86496c`.
This is the only discovered G1A request and matches the user's supplied prepare
command and visible source header. Device-side consumed-byte verification,
compiler warnings/errors, exact versions, repairs and runtime remain unreported.
The screenshot is in the conversation, not a checked-in image artifact.

**Header-isolation experiment:** isolate the header while keeping every executable statement
and all four If blocks unchanged. New fixture
[g1a-presence-no-header.txt](../pipeline/fixtures/g1a-presence-no-header.txt)
is the original .jelly minus its eight leading // comment lines, byte-for-byte
identical otherwise. Original fixtures remain unchanged. First compile that
candidate in a separate editor project. A pass implicates header processing for
this input, without proving every comment or a particular word is broken. A
failure means header removal is insufficient; preserve the result before isolating
the executable constructs. Only compare the compilation action on that candidate
after recording the editor result. That editor result is now the reported pass
above, followed by the reported Compile Jelly Text runtime pass. Keep the same
candidate for repeated compilation checks before testing individual header
comments in separate variants. See [the candidate contract](../pipeline/README.md#header-isolation-after-both-paths-failed).

## Initial investigation record

Originally recorded 5 November 2026 from user-reported iPad action inspection. No device
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

The earlier investigation recorded G1A twins as byte-identical. That claim no
longer describes HEAD: commit d172232 changes only the .txt header, while the
original .jelly still has hash 9052558758e35e63d3928d3ae79bbe5fa0a2094da87c5c5169bcc87c1b86496c.
Both current variants have LF line endings and no UTF-8 BOM. The known local
CRLF compiler defect therefore does not explain those repository bytes. The
bytes delivered to the iPad were not independently captured.

Earlier suggestions that comment punctuation or the word `return` caused the
fault were hypotheses, not established diagnoses. The later comparison points
to a difference involving the Shortcuts compilation paths; its mechanism is
unresolved. It does not justify rewriting valid action calls or comments across
the repository. The original full G1A source still needs a direct-editor comparison;
its presence-condition generation and expected runtime previews remain untested.

## Current development route

Transfer the exact request snapshot from the PC, then compile/export from the Jellycuts editor and
inspect the generated actions. Avoid relying on Compile Jelly File or Compile
Jelly Text as the general authoritative pipeline merely because the minimal
example now generates all three actions: full G1A still fails. Keep malformed exports untouched for comparison;
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
