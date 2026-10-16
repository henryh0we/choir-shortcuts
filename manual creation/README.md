# Apple Shortcuts design repository

This repository contains instructions for people to build Apple Shortcuts manually on an iPhone. Codex designs and maintains the Markdown specifications; saving these files does not install a Shortcut.

Specifications use the readable layout of [the supplied parser blueprint](../Parse%20Choir%20Music%20Filename%20V2%20-%20Shortcut%20Blueprint.txt): bracketed actions, parameter lines, section separators, and indented logic inside a Markdown text block.

Start with the [Shortcut index](SHORTCUT_INDEX.md). Each linked file explains inputs, outputs, dependencies, editor setup, every action and variable connection, and manual tests.

| Location | Contents |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Agent rules, architecture, naming, action notation, and review standards |
| [SHORTCUT_TEMPLATE.md](SHORTCUT_TEMPLATE.md) | Template for a new specification |
| [examples/](examples/) | Two linked teaching Shortcuts |
| `shortcuts/main/` | Diagnostic and user-facing native workflows |
| `shortcuts/reusable/` | Native helpers called from generated workflows |
| [docs/](docs/) | Platform evidence and future project architecture notes |
| `nextcloud file structure.txt` | Existing reference listing, preserved unchanged |

To build the examples:

1. Read [platform notes](docs/platform-notes.md). The provisional target is iOS 26 with an English editor; these examples have not been built or run on an iPhone.
2. Build [UTIL - Format Greeting](examples/util-format-greeting.md) first, using its exact app name.
3. Build [MAIN - Show Greeting](examples/main-show-greeting.md), selecting that utility in its `Run Shortcut` action.
4. Follow the bracketed blueprint from top to bottom. Uppercase headings divide phases; indentation shows nested actions. Control-flow markers appear automatically. Insert bracketed tokens within Text as instructed by each NOTE; do not type their brackets. Source descriptions identify the action output to select.
5. Complete the manual tests and record your device, iOS version, specification revision, and actual results before changing status.

Dependency links in each specification determine which Shortcuts must exist first. The main specification supplies the full build order. Exact names matter when selecting a callee in `Run Shortcut`; repository links alone do not install it.

To add a Shortcut, inspect existing components, copy the template into the appropriate folder, define its contract, document complete actions, and add an index entry. Read [AGENTS.md](AGENTS.md) for details. When changing an interface, update callers and provide manual migration instructions so installed Shortcuts stay compatible.

For production choir music, follow [the hybrid build guide](../jelly/docs/choir-service-build.md). All four Shortcuts now have Jelly source. Generate the archive and assembly helpers too, then follow [their insertion-slot guide](../jelly/docs/choir-service-assembly.md). Their blueprints here are reference/fallback instructions, not the preferred route. The earlier single-score diagnostic remains historical and is not required for the production workflow.
