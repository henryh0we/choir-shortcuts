# Running-order Text accumulator candidate

Source: [probe-running-order-text.jelly](probe-running-order-text.jelly).
Transfer: [probe-running-order-text.txt](probe-running-order-text.txt).
Intended installed name: `TEST - Jelly Running Order Text`, interface 1.0.
No dependencies, input, file access or forScore operations; only a synthetic
Text fixture and a Quick Look preview. Production COL02 is not changed.

This tests whether the manual preview-name collection and Combine Text/Custom
separator can be replaced with a named Text accumulator. The first loop item
initializes runningOrder. Later items use Text interpolation to append
` | ` and the current Repeat Item, assigning that new Text to runningOrder.
The fixture includes an intentional repeated value to catch lost/overwritten items.

Forms used: the user-confirmed quoted RepeatIndex comparisons and named-variable
assignments, plus documented Text/interpolation from the local
[variables guide](../../vendor/jellycuts-docs/markdown/Language_Guide/variables.md)
and existing source patterns. The complete accumulator is not device verified.

Local test, 21 October 2026:

```powershell
python jelly/scripts/build.py jelly/tests/compatibility/probe-running-order-text.jelly
```

Open-Jellycore e1ec31c / Swift 6.4.1 accepted the source (raw 0), with six
brace/core-node warnings. The wrapper returned **1**, rejecting the export for
out-of-range interpolation attachment `{1243, 1}`. The rejected plist and JSON/logs
are under `jelly/build/tests/compatibility/`. This is **Compiled, export rejected**,
not a passing build or an import-ready artifact.

Optional iPad evaluation uses the `.jelly`/`.txt` source, not that rejected local
export. Compile unchanged and record diagnostics before repairs. If accepted,
inspect the first-item assignment and later-item Text/assignment inside the Repeat.
The final preview must read the named runningOrder after End Repeat. Run directly
in the foreground and expect exactly **First | Second | First**, with no leading
separator and the repetition preserved. Empty, partial or literal variable-name
results are failures. Changing/removing fixture values is a separate test revision.

Actual iPad compilation, action inspection and execution: **Not run**. Do not
promote this into COL02 until that exact result is confirmed. It does not replace
native File/Score collection append operations in COL01/COL03.
