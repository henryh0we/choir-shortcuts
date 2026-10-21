# Compare Output acceptance on the iPad and local compiler

This test isolates a single argument-signature difference. It contains no If,
loops, interpolation, files or helper calls, so those cannot obscure the result.
Each `.jelly` file is one independent diagnostic Shortcut, with no dependencies.

The PC uses Open-Jellycore commit `e1ec31c2ee192c8721749f9eb3b50108e38891cf`
(May 2024), built with Swift 6.4.1. The recorded iPad profile is Jellycuts
2026.6.4 on iPadOS 26.6; its bundled compiler/library revision is unknown.
The [official repository](https://github.com/OpenJelly/Open-Jellycore#features-compared-to-private-jellycore)
distinguishes its open implementation from private Jellycore and documents feature
differences. Therefore they must not be assumed to accept identical source.
This is a compiler/binding compatibility question; Windows itself does not dictate
which arguments the Jelly language accepts, and our PC compilation runs in Linux.

The local source's `OutputParameter.swift` looks for `result`, `noResultBehavior`
and `response`. Existing user device evidence instead records successful positional
`output("...")`, with unresolved missing-argument warnings. The web documentation
has yet another signature; it is not used as proof of either implementation here.
This comparison can establish a particular behavioural difference, not identify
the iPad's exact internal compiler revision or diagnose every project failure.

## Files

| Test | File / intended installed name | Purpose |
| --- | --- | --- |
| A | [probe-output-positional.jelly](probe-output-positional.jelly) / `TEST - Jelly Positional Output` | New isolated positional Output test |
| B | [probe-output-respond.jelly](probe-output-respond.jelly) / `TEST - Jelly Output Respond` | Existing named-argument local control |

The important executable line in A is:

```jelly
output("COMPATIBILITY PROBE: positional output reached.")
```

## Local test

From the repository root:

```powershell
python jelly/scripts/build.py jelly/tests/compatibility/probe-output-positional.jelly
python jelly/scripts/build.py jelly/tests/compatibility/probe-output-respond.jelly
```

In VS Code, open each source, save it and press Ctrl+Shift+B. A local failure for
A is intentional evidence, not a request to repair its syntax. Do not replace its
positional call with named arguments: that would change the experiment.

Results and captured diagnostics are mirrored under `jelly/build/tests/compatibility/`.
The wrapper's failure must be distinguished from a raw CLI error and from rejection
of an otherwise compiled export. Check `compiler_exit_code`, `stage`, diagnostics
and captured stdout rather than relying on the raw process status alone.

## iPad test (user action; not yet performed for this file)

1. Transfer/open **the `.jelly` source** of A in Jellycuts on the iPad. Do not use
   the PC export: A is expected to have no successful local export.
2. Record Jellycuts and iPadOS versions and compile the source unchanged. Keep
   exact errors and warnings. Acceptance with warnings is distinct from rejection.
3. If export succeeds, inspect the generated Shortcut. It should contain one
   Stop and Output action with exactly `COMPATIBILITY PROBE: positional output reached.`
   as its result (plus any generated header Comment actions). Record its no-recipient
   settings; do not change source or silently repair actions for this first check.
4. Confirm the intended installed name and run it directly. Record whether the
   constant result is displayed/returned and whether any extra prompt appears.
   To check a returned value explicitly, call it using native Run Shortcut from a
   temporary device Shortcut and Quick Look that action's result.
5. Optionally repeat with B, expecting `Jelly output probe` if it imports/runs.
   This checks the opposite signature; its iPad outcome is currently unknown.
6. For runtime boundary checks, call A with no input, Text input and a Number.
   All should return the same constant Text because the source ignores input.
   Stop at compile/export failure; runtime cases cannot then be marked passed.

| Observation | A: positional | B: named control |
| --- | --- | --- |
| Local compiler acceptance, 21 October 2026 | Rejected: unnamed parameter plus missing result/noResultBehavior/response | Accepted on rerun |
| Local structural export acceptance | Not reached; no `.shortcut` published | Passed on rerun; unsigned export generated |
| Exact-source iPad acceptance/errors/warnings | Not run | Not run |
| iPad generated Output payload inspected | Not run | Not run |
| iPad execution / ignored-input cases | Not run | Not run |

Both were tested together using:

```powershell
python jelly/scripts/build.py jelly/tests/compatibility/probe-output-positional.jelly jelly/tests/compatibility/probe-output-respond.jelly
```

The tested A source SHA-256 is
`1fbc4b4da51f177f22340b372f6884c7c05e67834672e55ffdace875f62e1ffd`.
The combined wrapper
status was 1 because A failed; its summary was `1/2 exports passed compiler and
structural checks.` A's raw CLI status was 0 despite reporting errors; the wrapper
correctly identified the compiler rejection. B's `.build.json` records
`success: true`, `stage: exported-unsigned`. No source was changed to obtain
these results, and no signing or device execution was performed.

If the unchanged A is accepted on the iPad but rejected locally, that confirms
different acceptance rules for this exact source. If the iPad also rejects it,
the new test has not reproduced the historical discrepancy; retain the diagnostics
and check versions/source differences. A local B pass rules out a generally broken
compiler installation as the explanation for A's failure.
