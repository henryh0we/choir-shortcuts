# Shortcut inventory and installation order

Source headers own contracts and direct dependency details. This table is the navigation summary; update it alongside source and test records.

| Installed name / source | Role and purpose | Direct dependencies | Interface | Stage |
| --- | --- | --- | --- | --- |
| [UTIL - Jelly Format Greeting](../examples/util-jelly-format-greeting.jelly) | Example reusable utility: format one name, default to Friend | None | 1.0 | Syntax reviewed |
| [MAIN - Jelly Greeting Demo](../examples/main-jelly-greeting-demo.jelly) | Example main: pass Henry to utility and return its result | UTIL - Jelly Format Greeting, interface 1.0 | 1.0 | Syntax reviewed |
| [UTIL - Canonical Choir Name](../shortcuts/reusable/util-canonical-choir-name.jelly) | Canonical lookup stem from a choir filename | None | 1.0 | Drafted |
| [UTIL - Archive Choir PDF](../shortcuts/reusable/util-archive-choir-pdf.jelly) | Generated archive helper with CFG completion slots | UTIL - Canonical Choir Name, interface 1.0 | 1.0 | Drafted |
| [UTIL - Assemble Choir Service](../shortcuts/reusable/util-assemble-choir-service.jelly) | Generated service helper with forScore insertion slots | UTIL - Canonical Choir Name; UTIL - Archive Choir PDF, interfaces 1.0 | 1.0 | Drafted |
| [MAIN - Build Choir Service](../shortcuts/main/main-build-choir-service.jelly) | Generated interactive production entry point | UTIL - Assemble Choir Service, interface 1.0 | 1.0 | Drafted |

External provider apps/services: None for the example actions. Jellycuts or a compatible compiler is a build tool; Apple Shortcuts is the runtime. Target iOS 26 is provisional, not a confirmed device configuration.

1. Compile/export the utility, inspect generated actions, import it, and confirm its installed name is exactly `UTIL - Jelly Format Greeting`.
2. Run the utility's direct test. Record results without claiming the complete integration is verified yet.
3. Compile/export/import the main under `MAIN - Jelly Greeting Demo`. Confirm its Run Shortcut points to the installed utility and passes the intended Text variable.
4. Execute [all example tests](../tests/examples.md), including the changed-input integration case.

There is no cycle: main depends on utility; utility does not depend on main. Using the main to test the utility does not create a utility runtime dependency.

Compiler/app versions and installed source revisions have not been confirmed. Dependency comments and interface versions do not enforce runtime compatibility. Missing or renamed utilities may halt Run Shortcut rather than return a recoverable error. Check exact names and contracts before launch; do not claim a runtime catch is implemented.

## Choir service installation order

The [production build guide](choir-service-build.md) owns configuration, scope and the complete install sequence: canonical naming utility, archive helper, assembly helper, main. All four now have Jelly source. Complete the archive CFG slots and service FS slots using [the assembly guide](choir-service-assembly.md) before removing the two initial guards. No cycle: main calls assembly, assembly calls archive and canonical, archive calls canonical. Examples and the old diagnostic are not dependencies.

Production target reported by the user: iPadOS 26.6, forScore 15.2.5, Jellycuts 2026.6.4. Bundled compiler/action-library versions and all new export/import/device results remain unverified. Configure the signed-in Nextcloud Files location and existing iCloud archive root; permissions are requested by native actions. Record the single integrated run in [choir-service tests](../tests/choir-service.md).
