Copy this template into the appropriate folder. Replace placeholders and remove this introduction. Follow [AGENTS.md](AGENTS.md). Keep the blueprint in one text fence; put clickable links beneath it.

```text
<SHORTCUT DISPLAY TITLE IN UPPERCASE>
===================================

Shortcut name:
<Exact name used in Apple's Shortcuts app>

Purpose:
<What the Shortcut does and why it is a useful component.>

Input: <Type and cardinality, or None consumed>
Output: <Type and cardinality>

Category: <Main / Reusable / Example (role)>
Specification revision: 1
Interface version: 1.0
Target platform: <iOS version; provisional or confirmed>
Editor language: <Language>
Implementation status: Designed
Required apps: <Shortcuts; other app versions, or None>
Permissions: <Required access and first-run prompts, or None>
Launch methods: <Supported direct/called/share/automation contexts>
Side effects: <Displays, files, network, clipboard, or None>

Input contract:
<Required/optional input, defaults, empty/missing/whitespace rules.>
<Dictionary keys: exact spelling, type, required status, allowed values.>

Output contract:
<Exact structure/value; Dictionary key types and list ordering if relevant.>
Example: <Input> -> <Exact output>

Direct execution:
<Where input comes from; prompts/defaults; displayed/returned result.>

Called through Run Shortcut:
<What to pass, what is returned, and whether UI appears.>

Errors / cancellation:
<Returned error value or halt without guaranteed output.>

Unsupported inputs / contexts:
<Explicit limitations.>


========================
DEPENDENCIES AND BUILD ORDER
========================

Required Shortcuts:
- <Exact app name; required interface version; linked specification below>
  <Relevant prerequisite; or write None if no dependencies.>

External services / resources: <Apps, accounts, file providers, or None>

Build order:
1. <Build/test transitive dependencies first, once each.>
2. <Build this Shortcut and run integration tests.>


========================
EDITOR SETUP
========================

1. Create the Shortcut with the exact Shortcut name above.
2. <Configure Share Sheet/Receive banner only if needed.>
3. <Configure accounts, permissions, and resources if needed.>

Notation:
Bracketed standalone labels are actions or generated control markers.
[Shortcut Input] declares incoming content; it is not an action to add.
Otherwise, End If, and End Repeat are created with their owning actions.
Values naming variables/output sources must be selected as tokens.
In Text content, bracketed tokens are inserted as explained by a NOTE;
do not type their brackets. [leave empty] means leave the field blank.
NOTE and separator headings are documentation, not actions.
<Explain any descriptive field locators whose exact labels need checking.>


[Shortcut Input]
Type expected: <Input type; omit declaration if input is not consumed>


========================
<PHASE NAME>
========================

[<Exact action name>]
<Parameter>: <Literal value, choice, or clearly identified variable source>
<Expanded setting>: <Explicit value when relevant>

NOTE:
<Include only if needed for variable wiring or construction.>

<Continue with ALL actions in execution order. Use four-space indentation
inside If/Otherwise/repeat bodies; align generated closing markers with
their owner. Remove these template instructions from finished files.>


========================
EXPECTED TEST RESULTS
========================

Prerequisites:
<Device/iOS, built dependencies, files/accounts/permissions.>
Caller example: <Reusable components must link a composed specification
or include complete bracketed call blocks with explicit input/output.>

T1 - <Happy path; exact launch/input steps>
-> <Exact expected output and side effects>
Actual result: Not run

T2 - <Missing/empty input or default>
-> <Expected handling>
Actual result: Not run

T3 - <Boundary or invalid case; label out-of-contract types>
-> <Expected result or explicitly no guaranteed behaviour>
Actual result: Not run

T4 - <Direct/integration/cancellation as applicable; add further cases>
-> <Observable expected behaviour>
Actual result: Not run

<Explain restoration after temporary test edits; remove irrelevant cases
with a brief reason. Do not claim execution without evidence.>


========================
BUILD NOTES
========================

1. <Explain responsibility boundaries and useful construction tips.>
2. <Resolve ambiguous variable sources by phase/subsection and action.>
3. <Explain branch/loop output selection if relevant.>


========================
ERRORS AND LIMITATIONS
========================

<Condition>
-> <Actual handling, implementing phase/actions, and diagnosis.>
<Runtime failure/cancellation>
-> <Verified recovery or documented halt; no invented try/catch.>


========================
IMPLEMENTATION RECORD
========================

Current status: Designed
Static review: <Date and checks, or Not reviewed>
Built revision / device / exact iOS / builder / date: Not built
Execution evidence (revision, tester, date, actual results): Not run
Remaining issues: <Specific open items, or None>


========================
CHANGE HISTORY
========================

Revision 1 | Interface 1.0 | <YYYY-MM-DD>
Initial design. Manual migration: <Create actions/configure resources.>


========================
SOURCES AND OPEN VERIFICATION
========================

<Source names, review date, selected platform version, supported claims;
clickable links below. Distinguish documentation from device evidence.>
VERIFY ON DEVICE: <Specific unresolved setting/capability/behaviour,
impact and fallback, or None.>
```

Dependency specifications: <Add relative Markdown links, or None.>

Caller example: <Add relative Markdown link when relevant.>

Sources: <Add direct authoritative links and applicable project notes.>
