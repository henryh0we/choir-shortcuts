# Jellycuts workspace

This directory contains Jelly source for Apple Shortcuts. Each `.jelly` file represents one Shortcut to compile, import, and test on an iPhone. The sibling `manual creation/` directory keeps the separate manual-blueprint workflow.

Start with [AGENTS.md](AGENTS.md). Read the [language/toolchain reference](docs/jellycuts-reference.md), [architecture](docs/architecture.md), and [Shortcut inventory and installation order](docs/dependencies.md).

## Current iPad status and avoiding repeat debugging

27 October update: `test-assemble-service` is confirmed to call
`2-util-assemble-choir-service`. A/B -> B/A replacement reached a readback-count
error; the actual entries are A/B/B/A; numeric Count operands remain unknown. Assembly source revision 17
adds piece identity to metadata prompts and numeric error diagnostics, and
replaces unconditional Create/Replace and target choosers with a native exact-name
resolver slot requiring device completion. Preserve the active installed copy;
see [latest repair/status record](docs/ipad-assembly-lessons.md).

23 October 2026: the user confirms a manually completed one-score Assembly run
populates and opens the forScore setlist. Direct use of New Setlist for Create new
and a prompted service-date/name default also work after native edits. Fresh
exports and multi-score, repeated-score and replacement cases remain unverified.
Preserve the working installed shortcuts; regenerating restores placeholders.

Read [the repairs and installed changes](docs/ipad-assembly-lessons.md) before
another import. Source comments marked WIRE/EDIT identify required checks beside
actions, in addition to CONF/COL/SCORE/FS insertion slots. In particular:

- Reconnect consumers after replacing Nothing; keep initializer Nothing actions.
- Reselect current named collections in Count, Combine Text and Repeat; reconnect
  both Count comparison operands and verify **is not**.
- Missing-value guards must say **does not have any value**; presence guards say
  **has any value**. Check the native operator after export.
- Insert real default-answer and List variable tokens; literal expressions and
  `""` are not working defaults. Preserve native File/Folder/Dictionary/Score types.
- Select each Run Shortcut target and matching List together: naming takes two
  Texts, archive takes PDF/Library/config, Assembly takes Text interactive.
- Diagnose actual action outputs before changing implementation. A count or
  editor Text label alone does not establish native type, identity or order.

For a repeatable route to better generation, use the separate
[iPad questions and test checklist](tests/ipad-investigation/README.md). It lists
small experiments, expected outcomes, existing evidence and a results template;
the proposed tests have not been executed. Improve source forms only from recorded
evidence, and leave explicit repair comments where generation is still uncertain.

Local compilation is now available through WSL2: Open-Jellycore `e1ec31c`, built with Swift 6.4.1. See [setup](docs/setup.md), [daily development](docs/development.md), [limitations/signing](docs/compiler-limitations.md), and [validation evidence](tests/compiler/README.md). From this repository's root, run:

```powershell
python jelly/scripts/build.py jelly/tests/compiler/hello-world.jelly
python jelly/scripts/validate.py
```

In VS Code, save a `.jelly` file and press **Ctrl+Shift+B**. Exports and diagnostics go under `jelly/build/`, mirroring source folders. Existing app sources may fail this older CLI profile; a compiler pass does not establish iPad compatibility. The notes below about absent local tooling describe the 14 October inspection, before this installation.

| Location | Purpose |
| --- | --- |
| `examples/` | Source-reviewed reusable formatter and composed demonstration |
| `shortcuts/main/` | Generated production entry points |
| `shortcuts/reusable/` | Generated shared components |
| `docs/` | Syntax evidence, design, dependencies, and compilation instructions |
| [tests/examples.md](tests/examples.md) | Expected results and actual validation record |
| `build/` | Ignored unsigned exports, build reports, captured logs, temporary validation files |
| `scripts/` | Cross-platform compiler wrapper, integration validation and WSL setup launcher |

The examples use signatures checked against Open-Jellycore source at revision `e1ec31c2ee192c8721749f9eb3b50108e38891cf`. They have **not been compiled, imported, or run**. No Jelly compiler was found on PATH in this Windows workspace on 2026-10-14. The user-reported device profile is Jellycuts 2026.6.4 on iPadOS 26.6, with forScore 15.2.5. Bundled compiler and action-library revisions remain unknown; the inspected compiler is not a confirmed match.

Before editing syntax, use the [local official documentation index](docs/jellycuts-docs-index.md) and [device compatibility evidence and small probes](tests/compatibility/README.md). The [pinned snapshot](vendor/jellycuts-docs/README.md) includes original HTML, searchable Markdown, provenance and a repeatable refresh script. Documentation review does not establish successful app compilation.

Build/import the [utility](examples/util-jelly-format-greeting.jelly) first, then the [main](examples/main-jelly-greeting-demo.jelly). Use the Jellycuts iOS app's onboarding and export flow or a compatible Open-Jellycore CLI on a supported host. The reference explains compiler commands, known documentation discrepancies, export/signing checks, and installed-name verification.

After import, use the exact source-header names: `UTIL - Jelly Format Greeting` and `MAIN - Jelly Greeting Demo`. Run the manual tests and record the actual compiler/device evidence before promoting their status. Editing source does not update an installed Shortcut automatically.

For new work, inspect existing components, define contracts, create one `.jelly` source per Shortcut, add a linked test specification and inventory entry, then validate against the actual toolchain. Do not invent bindings or treat an uncompiled example as proof of runtime compatibility.

## Build a choir service

Read [config setup and input contracts](docs/config-integration.md) first. Naming uses interface 2.0; Archive completed interface is 2.1; Assembly completed interface is 1.1. Assembly loads `Choir Music/config.json` once and needs CONF01-CONF02, COL01-COL03, SCORE01-SCORE02 and FS01-FS13; archive keeps CFG02-CFG04. The manually repaired installed fixture has the limited success recorded above; generated source is still a completion template.

Start with [the choir service build guide](docs/choir-service-build.md) for scope and dependency order, then [the assembly guide](docs/choir-service-assembly.md) and current repair record. Complete native slots and reconnections after export, inspect conditions and defaults, then run the one-score test. The older manual blueprints remain reference material.
