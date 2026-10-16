# Jellycuts workspace

This directory contains Jelly source for Apple Shortcuts. Each `.jelly` file represents one Shortcut to compile, import, and test on an iPhone. The sibling `manual creation/` directory keeps the separate manual-blueprint workflow.

Start with [AGENTS.md](AGENTS.md). Read the [language/toolchain reference](docs/jellycuts-reference.md), [architecture](docs/architecture.md), and [Shortcut inventory and installation order](docs/dependencies.md).

| Location | Purpose |
| --- | --- |
| `examples/` | Source-reviewed reusable formatter and composed demonstration |
| `shortcuts/main/` | Generated production entry points |
| `shortcuts/reusable/` | Generated shared components |
| `docs/` | Syntax evidence, design, dependencies, and compilation instructions |
| [tests/examples.md](tests/examples.md) | Expected results and actual validation record |
| `build/` | Future generated exports; create when exporting |

The examples use signatures checked against Open-Jellycore source at revision `e1ec31c2ee192c8721749f9eb3b50108e38891cf`. They have **not been compiled, imported, or run**. No Jelly compiler was found on PATH in this Windows workspace on 2026-10-14. The user-reported device profile is Jellycuts 2026.6.4 on iPadOS 26.6, with forScore 15.2.5. Bundled compiler and action-library revisions remain unknown; the inspected compiler is not a confirmed match.

Before editing syntax, use the [local official documentation index](docs/jellycuts-docs-index.md) and [device compatibility evidence and small probes](tests/compatibility/README.md). The [pinned snapshot](vendor/jellycuts-docs/README.md) includes original HTML, searchable Markdown, provenance and a repeatable refresh script. Documentation review does not establish successful app compilation.

Build/import the [utility](examples/util-jelly-format-greeting.jelly) first, then the [main](examples/main-jelly-greeting-demo.jelly). Use the Jellycuts iOS app's onboarding and export flow or a compatible Open-Jellycore CLI on a supported host. The reference explains compiler commands, known documentation discrepancies, export/signing checks, and installed-name verification.

After import, use the exact source-header names: `UTIL - Jelly Format Greeting` and `MAIN - Jelly Greeting Demo`. Run the manual tests and record the actual compiler/device evidence before promoting their status. Editing source does not update an installed Shortcut automatically.

For new work, inspect existing components, define contracts, create one `.jelly` source per Shortcut, add a linked test specification and inventory entry, then validate against the actual toolchain. Do not invent bindings or treat an uncompiled example as proof of runtime compatibility.

## Build a choir service

Start with [the choir service build guide](docs/choir-service-build.md). It provides the implementation scope and dependency-first order for all four Jelly sources. Standard actions are generated; [Comment slots](docs/choir-service-assembly.md) identify forScore insertions and archive configuration. Complete those slots after export, then check one service run. Sources are Drafted, not compiled, installed or working. The older manual blueprints remain reference material.
