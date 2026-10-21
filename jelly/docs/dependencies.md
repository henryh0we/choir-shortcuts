# Shortcut inventory and installation order

**Current source: Archive 14 / Assembly 11.** The user confirms the small flush-left, parenthesized If probe returns Conditional output reached. The indented parenthesized probe dropped its Output; the unparenthesized probe dropped its If. Both helpers now keep code flush left and use positional `output("ERROR: ...")`, with no notes: label. Literal multiline message whitespace is preserved. Warnings about missing noResultBehaviour and response remain unresolved: the successful probe is not warning-free. This establishes only the tested conditional stop/Text fixture, not interpolation, File returns, nested loops or either complete helper. Existing native ARC/CFG/CONF/COL/SCORE/FS completion remains; no native validation construction is required.



Current archive 9 / assembly 7: follow the [18 October compatibility checklist](helper-compatibility-update.md). Its native selector/collection slots and Exit returns supersede older selector, Output-field and Repeat Results instructions on this page.

Source headers own contracts and direct dependency details. This table is the navigation summary; update it alongside source and test records.

| Installed name / source | Role and purpose | Direct dependencies | Interface | Stage |
| --- | --- | --- | --- | --- |
| [UTIL - Jelly Format Greeting](../examples/util-jelly-format-greeting.jelly) | Example reusable utility: format one name, default to Friend | None | 1.0 | Syntax reviewed |
| [MAIN - Jelly Greeting Demo](../examples/main-jelly-greeting-demo.jelly) | Example main: pass Henry to utility and return its result | UTIL - Jelly Format Greeting, interface 1.0 | 1.0 | Syntax reviewed |
| [UTIL - Canonical Choir Name](../shortcuts/reusable/util-canonical-choir-name.jelly) | Configured canonical name from a two-Text List | None | 2.0 | Drafted |
| [UTIL - Archive Choir PDF](../shortcuts/reusable/util-archive-choir-pdf.jelly) | Config-based archive with native context List and CFG slots | UTIL - Canonical Choir Name, interface 2.0 | 2.0 | Drafted |
| [UTIL - Assemble Choir Service](../shortcuts/reusable/util-assemble-choir-service.jelly) | Load config once, prepare service; CONF/FS slots | UTIL - Canonical Choir Name; UTIL - Archive Choir PDF, interfaces 2.0 | 1.1 | Drafted |
| [MAIN - Build Choir Service](../shortcuts/main/main-build-choir-service.jelly) | Generated interactive production entry point | UTIL - Assemble Choir Service, interface 1.1 | 1.0 | Drafted |

External provider apps/services: None for the example actions. Jellycuts or a compatible compiler is a build tool; Apple Shortcuts is the runtime. Current user-reported target: Jellycuts 2026.6.4 on iPadOS 26.6; no successful compilation or runtime validation is recorded for these sources.

1. Compile/export the utility, inspect generated actions, import it, and confirm its installed name is exactly `UTIL - Jelly Format Greeting`.
2. Run the utility's direct test. Record results without claiming the complete integration is verified yet.
3. Compile/export/import the main under `MAIN - Jelly Greeting Demo`. Confirm its Run Shortcut points to the installed utility and passes the intended Text variable.
4. Execute [all example tests](../tests/examples.md), including the changed-input integration case.

There is no cycle: main depends on utility; utility does not depend on main. Using the main to test the utility does not create a utility runtime dependency.

The app version is user-reported; bundled compiler/library revisions and installed source revisions remain unconfirmed. Dependency comments and interface versions do not enforce runtime compatibility. Missing or renamed utilities may halt Run Shortcut rather than return a recoverable error. Check exact names and contracts before launch; do not claim a runtime catch is implemented.

Optional independent diagnostic Shortcuts are inventoried in [compatibility tests](../tests/compatibility/README.md). They are not dependencies of examples or production sources.

The independent local-compiler smoke Shortcut, `TEST - Local Compiler Hello`, is
inventoried with its source, contract and validation evidence in
[compiler tests](../tests/compiler/README.md). It has no installed Shortcut
dependencies and is not a dependency of any production component.

## Choir service installation order

The [production build guide](choir-service-build.md) owns configuration, scope and the complete install sequence: canonical naming utility, archive helper, assembly helper, main. All four now have Jelly source. Use the current [config contracts](config-integration.md); complete archive CFG02-CFG04 and service CONF01-CONF02/FS01-FS13 using [the assembly guide](choir-service-assembly.md) before removing the two initial guards. No cycle: main calls assembly, assembly calls archive and canonical, archive calls canonical. Examples and the old diagnostic are not dependencies.

Production target reported by the user: iPadOS 26.6, forScore 15.2.5, Jellycuts 2026.6.4. Bundled compiler/action-library versions and all new export/import/device results remain unverified. Configure the signed-in Nextcloud Files location and existing iCloud archive root; permissions are requested by native actions. Record the single integrated run in [choir-service tests](../tests/choir-service.md).

Optional short test drivers and installation/input contracts: [functional tests](../tests/functional/README.md). These are not production dependencies.
