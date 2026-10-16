# Example validation and manual tests

Sources: [utility](../examples/util-jelly-format-greeting.jelly) and [main](../examples/main-jelly-greeting-demo.jelly), specification revision 1, interface 1.0. See [compiler evidence and commands](../docs/jellycuts-reference.md) and [installation order](../docs/dependencies.md).

## Current evidence

```text
Reviewed date: 2026-10-14
Stage: Syntax reviewed
Candidate compiler source: Open-Jellycore
Candidate revision: e1ec31c2ee192c8721749f9eb3b50108e38891cf
Installed compiler/app/library version: Unknown
Compilation command actually run: None
Compiler diagnostics/artifacts: None; not compiled
Imported device / exact iOS / date: None; not imported
Execution reports: None; not run
Provisional design target: iOS 26, English
```

Syntax reviewed means checked against cited material, not accepted by an executed compiler. The presence condition combines language-guide semantics and compiler-test brace/global conventions; actual parser acceptance and empty-input runtime behaviour remain unverified.

Before testing, compile without diagnostics errors, inspect output/variable connections, import dependency first, and confirm exact names. The formatter accepts one Text or no input; do not expect supported behaviour from arbitrary other types. No external files, accounts, or provider apps are needed for the example actions.

## Expected test results

```text
T1 - Direct utility, absent input
Tap UTIL - Jelly Format Greeting in Shortcuts.
-> Hello, Friend! displayed through no-recipient Respond
-> No prompt, file/network/clipboard changes
Actual result: Not run

T2 - Main integration
Run MAIN - Jelly Greeting Demo, which supplies Henry.
-> Hello, Henry! displayed once
-> Utility returns its result without an extra display
-> Final main output is that same Text
Actual result: Not run

T3 - Different Text, punctuation boundary
Temporarily change the main's name literal to Anne-Marie & Jo.
Recompile/reimport that test revision and run the main.
-> Hello, Anne-Marie & Jo! exactly
Restore Henry, recompile/reimport, and rerun T2.
Actual result: Not run

T4 - Empty Text
Temporarily set the main's name literal to "".
Recompile/reimport and run.
-> Hello, Friend! if presence testing handles empty Text as designed
Record the actual outcome; do not assume missing and empty are identical.
Restore Henry, recompile/reimport, and rerun T2.
Actual result: Not run

T5 - Whitespace preservation
Temporarily set the main's name literal to " Henry ".
Recompile/reimport and run.
-> "Hello,  Henry !" (quotes are illustrative, not output)
Restore Henry, recompile/reimport, and rerun T2.
Actual result: Not run

T6 - Missing dependency diagnosis
In the main's imported Run Shortcut action, temporarily select no valid
utility or use a test copy naming an absent Shortcut; do not delete the
real utility. Run the test copy.
-> Failure/stop is expected; no recoverable error result is promised
-> Record the actual diagnostic and confirm no external side effects
Restore/reimport the main from unchanged source and rerun T2.
Actual result: Not run
```

Invalid non-Text input is outside this interface, with no guaranteed return. A production validator would need separately verified type checks and its own negative tests. Neither example prompts, so there is no prompt-cancellation test; manually stopping execution has no guaranteed successful output. If prompts or network/file operations are added later, add cancellation, permission, and action-failure cases then.

Run the main in its editor and inspect returned output to verify the result independently of Respond's display. Confirm the utility's input banner, if present, continues without input so its default branch is reachable. Inspect the generated stopping action and check the intended no-recipient behaviour on both direct and called paths.

Keep temporary diagnostic changes out of the lasting sources unless they become a separately named test Shortcut. Record the exact temporary source change and compiled/imported revision in test evidence. After restoration, prove the regular revision still produces T2.

## Evidence to add after validation

Record compiler/app/library version, source revision, commands actually run, complete diagnostics summary, export paths, import/signing outcome, installed names, tester, date, device and exact iOS, actual output/side effects per test, and unresolved failures. Promote Compiled, Imported, Tested, or Verified only when that stage has actually occurred. Both source headers and the inventory must agree with this record.
