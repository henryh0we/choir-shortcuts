```text
UTIL - FORMAT GREETING
======================

Shortcut name:
UTIL - Format Greeting

Purpose:
Receives one name, formats a greeting, and returns Text.
With no input, uses Friend. MAIN - Show Greeting calls this utility.

Input: Text (one value; optional)
Output: Text (one greeting)

Category: Example (Reusable)
Specification revision: 2
Interface version: 1.0
Target platform: iOS 26, provisional; exact patch not confirmed
Editor language: English
Implementation status: Designed
Required apps: Apple Shortcuts; no third-party apps
Permissions: No protected data access required by these actions
Launch methods: Direct execution in Shortcuts; Run Shortcut
Side effects: Displays output directly when no recipient exists;
             no file, network, or clipboard changes

Input contract:
Missing or empty Text uses Friend. Nonempty Text is preserved exactly,
including whitespace. Lists and other content types are not supported.

Output contract:
One Text value: Hello, <name>!
No added newline. <name> is supplied Text or literal Friend.
Example: Henry -> Hello, Henry!

Direct execution:
No name prompt. With no incoming input, displays Hello, Friend! using
the Stop and Output no-recipient Respond option.

Called through Run Shortcut:
Pass one Text value. Receives one greeting Text value, without a prompt.
Respond should display nothing when the caller receives the output;
confirm this on the target device.

Errors / cancellation:
Missing input is a normal default. Runtime failure or stopping execution
has no promised result or recovery.

Unsupported inputs / contexts:
Lists, Dictionaries, Files, Dates, Numbers, and other content types.
No arbitrary type validation or conversion is implemented.
Share Sheet, Siri, and unattended automation are not specified here.


========================
DEPENDENCIES AND BUILD ORDER
========================

Required Shortcuts: None
External services / resources: None

Build order:
1. Build this utility and run direct test T1.
2. Build MAIN - Show Greeting (linked below) for integration tests.
   The main is a test caller, not a runtime dependency of this utility.


========================
EDITOR SETUP
========================

1. Create a Shortcut named exactly UTIL - Format Greeting.
2. Leave Show in Share Sheet off. No Receive banner is required.
   If a banner appears, set its no-input behaviour to Continue.
3. Add the actions below in order. Otherwise and End If are created
   automatically with If; do not add them separately.

Notation:
[Shortcut Input] below declares incoming content, not an action to add.
Select variables as tokens; do not type their names or brackets.
A source description such as "Text from FORMAT GREETING" means select
the output beneath that action, not create a variable with that name.
NOTE and separator headings are documentation, not actions.
"No-recipient behaviour" is a descriptive locator for the expanded
Stop and Output setting; check its exact label on the target device.


[Shortcut Input]
Type expected: Text


========================
INPUT CHECK
========================

[If]
Input: Shortcut Input
Condition: has any value

    --- USE SUPPLIED NAME ---

    [Text]
    [Shortcut Input]

    NOTE:
    Insert the special Shortcut Input token as the entire Text body.
    Use its complete Text value; add no spaces or newline.

[Otherwise]

    --- DEFAULT NAME ---

    [Text]
    Friend

[End If]


========================
FORMAT GREETING
========================

[Text]
Hello, [If Result]!

NOTE:
Type "Hello, ", insert If Result from End If in INPUT CHECK, then "!".
Do not type the brackets or add a newline. Select the merged If Result,
not the Text output from an individual branch.


========================
RETURN GREETING
========================

[Stop and Output]
Output: Text from FORMAT GREETING
No-recipient behaviour: Respond


========================
EXPECTED TEST RESULTS
========================

Prerequisites:
iPhone with Shortcuts. Resolve device checks below and build revision 2.
For T2/T3, also build MAIN - Show Greeting revision 2, interface 1.0.
The main specification below provides the complete Run Shortcut call.

T1 - Tap this utility's tile with no input
-> Displays Hello, Friend!
-> No prompt, file, network, or clipboard changes
Actual result: Not run

T2 - Run MAIN - Show Greeting; enter Henry and submit
-> Caller displays Hello, Henry! once and returns that Text
-> Utility does not interrupt with a second display
Actual result: Not run

T3 - Run the main; enter Anne-Marie & Jo and submit
-> Displays and returns Hello, Anne-Marie & Jo!
Actual result: Not run

T4 - Temporarily change DEFAULT NAME's Text to Colleague; run directly
-> Displays Hello, Colleague!
Restore Friend and rerun.
-> Displays Hello, Friend!
Actual result: Not run

T5 - Empty Text diagnostic
In an editable test copy of the main, replace Ask for Input with a Text
action containing an empty body. Reconnect Run Shortcut's input to that
Text output, then run it.
-> Hello, Friend! if empty Text reaches the utility as documented
Restore Ask for Input and its connection before regular use.
Actual result: Not run

The prompt may prevent empty submission; T5 tests it separately.
Wrong-type input is outside the contract with no guaranteed result.
The interactive caller tests cancellation.


========================
BUILD NOTES
========================

1. This utility owns formatting; the main owns prompting and display.
   These two components are independently useful; no extra layers.
2. In INPUT CHECK, select Shortcut Input and its complete Text value.
   Set the selected token's type to Text if needed for the condition.
   This is a presence check, not validation of arbitrary content.
3. Each branch ends with Text. End If's If Result is the supplied name
   or Friend. Select that exact End If output in FORMAT GREETING.
4. In RETURN GREETING, select the Text output beneath FORMAT GREETING,
   not either Text action inside INPUT CHECK.
5. Expand Stop and Output to select Respond without an output recipient.
   Avoid an unconditional display here; the caller handles its display.
6. No Set Variable action is needed: the phase-qualified output sources
   distinguish all three Text actions without extra construction work.


========================
ERRORS AND LIMITATIONS
========================

Missing or empty input
-> INPUT CHECK selects Friend; FORMAT GREETING returns Hello, Friend!
   Check banner Continue setting and presence-condition behaviour.

Whitespace-only input
-> Preserved without trimming; this is not a name validator.

Wrong type or several values
-> Outside contract; caller must pass one Text value.

Brackets appear in displayed greeting
-> Construction error: insert selected tokens rather than literal labels.

Direct execution shows no greeting
-> Check RETURN GREETING's Respond setting; also inspect editor output.

Runtime failure or user stops execution
-> No catch or guaranteed output. Inspect and record the failed action.


========================
IMPLEMENTATION RECORD
========================

Current status: Designed
Static review: 2026-10-14; checked nesting, branch merge, variable sources,
               contract, caller wiring, and links after layout conversion
Built revision / device / exact iOS / builder / date: Not built
Execution evidence: Not run; no iPhone execution report available
Remaining issues: Confirm presence condition and no-recipient setting;
                  execute direct, empty-input, and integration tests


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
- Use If actions: branch markers and merged If Result
- Shortcut completion: Stop and Output and no-recipient Respond
- Use variables: selected variable tokens
Documentation review does not confirm a device build or execution.

VERIFY ON DEVICE:
- has any value for Shortcut Input selected as Text, including empty input
- Stop and Output expanded selector's exact label and direct/called behaviour
Unresolved implementation checks keep this specification at Designed.
```

Caller example: [MAIN - Show Greeting](main-show-greeting.md).

Sources: [Apple: Use If actions](https://support.apple.com/en-gb/guide/shortcuts/apd83dcd1b51/ios), [Apple: Shortcut completion](https://support.apple.com/en-gb/guide/shortcuts/apda9578f70f/ios), [Apple: Use variables](https://support.apple.com/en-gb/guide/shortcuts/apdd02c2780c/ios), and [platform notes](../docs/platform-notes.md).
