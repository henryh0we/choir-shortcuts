```text
MAIN - SHOW GREETING
====================

Shortcut name:
MAIN - Show Greeting

Purpose:
Asks for a name, calls UTIL - Format Greeting, displays the returned
greeting, then returns the same Text to any caller.

Input: None consumed (always prompts)
Output: Text (one greeting)

Category: Example (Main)
Specification revision: 2
Interface version: 1.0
Target platform: iOS 26, provisional; exact patch not confirmed
Editor language: English
Implementation status: Designed
Required apps: Apple Shortcuts; no third-party apps
Permissions: No protected data access required by these actions
Launch methods: Direct execution; interactive Run Shortcut call
Side effects: Name prompt and greeting display;
             no file, network, or clipboard changes

Input contract:
Incoming Shortcut Input is ignored. Ask for Input always prompts for one
Text value with Friend pre-filled; submitted Text is passed unchanged.

Output contract:
One greeting Text value from UTIL - Format Greeting interface 1.0,
also displayed once. No added newline or Dictionary wrapper.
Example: Submit Henry -> Hello, Henry!

Direct execution:
Always prompts, then displays the result. Stop and Output uses
Do Nothing when there is no recipient to avoid an extra display.

Called through Run Shortcut:
Still prompts and displays. Returns greeting Text after dismissal.
This workflow is interactive and cannot be used as an unattended API.

Errors / cancellation:
Cancelling the initial prompt is expected to stop before a greeting is
displayed. No successful return is promised; confirm on the device.
A missing dependency or action failure may halt execution.

Unsupported inputs / contexts:
Unattended/background automation, Share Sheet, and Siri are not specified.
Caller-supplied content does not bypass the prompt.


========================
DEPENDENCIES AND BUILD ORDER
========================

Required Shortcuts:
- UTIL - Format Greeting
  Required interface: 1.0
  Required specification revision for these examples: 2
  Input: One Text value
  Output: One greeting Text value
  Specification linked below; install under the exact app name.

External services / resources: None

Build order:
1. Resolve device checks and build UTIL - Format Greeting revision 2.
   Run its direct test T1.
2. Build this main and select that utility in CALL FORMATTER.
3. Run this main's tests and the utility's integration tests.
   Record actual results in both specifications.


========================
EDITOR SETUP
========================

1. Create a Shortcut named exactly MAIN - Show Greeting.
2. Leave Show in Share Sheet off. No Receive banner is required.
3. Ensure UTIL - Format Greeting exists in your Shortcuts collection.

Notation:
Bracketed labels below are actions to add, in top-to-bottom order.
Select output sources as variable tokens rather than typing their names.
"Answer from ASK FOR NAME" means the output beneath Ask for Input.
"Shortcut Result from CALL FORMATTER" means that Run Shortcut's output.
These are source descriptions, not named variables to create.
NOTE and separator headings are documentation, not actions.
Prompt, Input Type, Result, and No-recipient behaviour are descriptive
field locators; confirm the exact UI labels in the installed editor.


========================
ASK FOR NAME
========================

[Ask for Input]
Prompt: What name should I greet?
Input Type: Text
Default Answer: Friend
Allow Multiple Lines: Off (if available)


========================
CALL FORMATTER
========================

[Run Shortcut]
Shortcut: UTIL - Format Greeting
Input: Answer from ASK FOR NAME

NOTE:
Expand Run Shortcut if needed to select its input. Choose the complete
Text answer output beneath Ask for Input, not Shortcut Input, the prompt,
or Default Answer. Do not select a property or convert the value.


========================
SHOW GREETING
========================

[Show Result]
Result: Shortcut Result from CALL FORMATTER


========================
RETURN GREETING
========================

[Stop and Output]
Output: Shortcut Result from CALL FORMATTER
No-recipient behaviour: Do Nothing

NOTE:
Select the output beneath Run Shortcut explicitly. Do not use the output
of Show Result or assume that the display action passes content through.


========================
EXPECTED TEST RESULTS
========================

Prerequisites:
iPhone with Shortcuts. Resolve both specifications' device checks.
Build utility and main revision 2. No external accounts/files required.

T1 - Tap main tile; replace Friend with Henry; submit and dismiss result
-> Shows Hello, Henry! once
-> No file, network, or clipboard changes
Actual result: Not run

T2 - Run again; submit pre-filled Friend without editing
-> Shows Hello, Friend! once
Actual result: Not run

T3 - Enter Anne-Marie & Jo and submit
-> Shows Hello, Anne-Marie & Jo! exactly
Actual result: Not run

T4 - Cancel the initial name prompt
-> No greeting displayed; no successful result expected
-> Record the actual cancellation outcome on the target device
Actual result: Not run

T5 - Run from the editor with Henry; dismiss display; inspect final output
-> Returned Text is Hello, Henry!, sourced from Run Shortcut
Actual result: Not run

T6 - Temporary integration wiring diagnostic
In the utility's FORMAT GREETING Text, temporarily change "Hello, " to
"Welcome, ". Run this main with Henry.
-> Shows Welcome, Henry!
Restore "Hello, " immediately and rerun T1.
Record the diagnostic separately from the unchanged revision's tests.
Actual result: Not run

T1/T3 test native composition; greeting formatting must come from the
utility. T2 covers the prompt default. The utility's tests cover missing
and empty input. No unsupported-type success is promised.
If using interactive Run Shortcut launch in a larger project, document
that caller and test the returned Text after dismissing this display.


========================
BUILD NOTES
========================

1. This main owns interaction. UTIL - Format Greeting owns formatting.
   Do not duplicate the greeting Text or default-selection logic here.
2. Type the prompt and Friend as literals. Do not select Shortcut Input
   in Ask for Input; this main deliberately ignores incoming content.
3. CALL FORMATTER must pass the complete submitted answer to the utility.
   A Markdown link does not install or select that Shortcut.
4. SHOW GREETING must use the Run Shortcut result, not the raw answer.
   Select the output beneath Run Shortcut in CALL FORMATTER.
5. Dismiss Show Result so that RETURN GREETING can run. It must return
   the same Run Shortcut output explicitly, regardless of display output.
6. Expand Stop and Output and choose Do Nothing without a recipient.
   The utility's Respond option should apply only without a recipient.
7. No Set Variable is needed here: the uniquely identified Run Shortcut
   output can be selected in both SHOW GREETING and RETURN GREETING.


========================
ERRORS AND LIMITATIONS
========================

Utility missing or renamed
-> CALL FORMATTER may halt. Build the utility first and reselect its
   exact name. No runtime dependency detector is implemented.

Input prompt cancelled
-> Expected halt before call/display; confirm actual device behaviour.

Empty answer
-> Utility defaults to Friend if empty Text reaches it. The prompt may
   prevent empty submission; use the utility's empty-input diagnostic.

Only raw name displayed
-> SHOW GREETING has the wrong source; select CALL FORMATTER's result.

Greeting displayed twice
-> Check utility Respond applies only without a recipient and this main
   uses Do Nothing in RETURN GREETING.

Unexpected utility output
-> Displayed/returned as received; no schema check. Verify installed
   utility revision, interface 1.0, and variable connections.

Other runtime failure
-> No catch or guaranteed output. Inspect and record the failed action.


========================
IMPLEMENTATION RECORD
========================

Current status: Designed
Static review: 2026-10-14; checked dependency, contract agreement, four
               actions, variable sources, tests, and converted layout
Built revision / device / exact iOS / builder / date: Not built
Execution evidence: Not run; no device execution report available
Remaining issues: Confirm input/default settings, Run Shortcut selectors,
                  Show Result, Stop and Output, and prompt cancellation;
                  resolve utility checks and execute manual tests


========================
CHANGE HISTORY
========================

Revision 1 | Interface 1.0 | 2026-10-14
Initial example using numbered action cards.

Revision 2 | Interface 1.0 | 2026-10-14
Reformatted to the user's bracketed, indented blueprint layout.
Manual migration: None; actions, wiring, and interface are unchanged.


========================
SOURCES AND OPEN VERIFICATION
========================

Apple sources below reviewed 2026-10-14 for provisional iOS 26:
- Run a shortcut using a URL scheme: use Run Shortcut for native calls
- Ask for Input: Text answers and a pre-filled default
- Shortcut completion: explicit return and no-recipient Do Nothing
Documentation review does not confirm a device build or execution.

VERIFY ON DEVICE:
- Ask for Input field labels/default and Allow Multiple Lines option
- Expanded Run Shortcut input field and returned-output selector
- Show Result action availability/name and Text display behaviour
- Expanded Stop and Output no-recipient selector and utility return
- Cancellation of the input prompt
If Show Result is unavailable, document a Quick Look variant before
building it; do not silently substitute the action.
Unresolved implementation checks keep status at Designed.
```

Dependency specification: [UTIL - Format Greeting](util-format-greeting.md).

Sources: [Apple: Run a shortcut using a URL scheme](https://support.apple.com/en-au/guide/shortcuts/apd624386f42/ios), [Apple: Ask for Input](https://support.apple.com/en-gb/guide/shortcuts/apd68b5c9161/ios), [Apple: Shortcut completion](https://support.apple.com/en-gb/guide/shortcuts/apda9578f70f/ios), and [platform notes](../docs/platform-notes.md).
