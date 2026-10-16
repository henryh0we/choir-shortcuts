# Shortcut index

Each specification owns its interface, dependency details, and execution evidence. Status here mirrors its Implementation record. These specifications include teaching examples and a forScore diagnostic; saving them does not install Shortcuts.

| Shortcut | Purpose | Category | Direct dependencies | Status |
| --- | --- | --- | --- | --- |
| [UTIL - Format Greeting](examples/util-format-greeting.md) | Turn a supplied name into greeting Text; default to Friend without input | Example (Reusable) | None | Designed |
| [MAIN - Show Greeting](examples/main-show-greeting.md) | Ask for a name, call the utility, and display its returned greeting | Example (Main) | [UTIL - Format Greeting](examples/util-format-greeting.md), interface 1.0 | Designed |
| [TEST - forScore Import and Lookup](shortcuts/main/test-forscore-import-and-lookup.md) | Import one disposable PDF, independently retrieve its native score, and inspect identity/retry behaviour | Diagnostic (Main) | None | Designed |
| [UTIL - Archive Choir PDF](shortcuts/reusable/util-archive-choir-pdf.md) | Reuse/save a canonical clean PDF in the existing iCloud type folders | Reusable | [UTIL - Canonical Choir Name](../jelly/shortcuts/reusable/util-canonical-choir-name.jelly), interface 1.0 | Designed |
| [UTIL - Assemble Choir Service](shortcuts/reusable/util-assemble-choir-service.md) | Native selection, ordering, import/metadata and ordered service setlist | Reusable | UTIL - Canonical Choir Name; [UTIL - Archive Choir PDF](shortcuts/reusable/util-archive-choir-pdf.md), interfaces 1.0 | Designed |

Example build order: UTIL - Format Greeting, then MAIN - Show Greeting. Follow the detailed setup and tests in each file.

forScore diagnostic build order: TEST - forScore Import and Lookup only. Transfer its linked PDF fixture to Files on the iPad, then follow the numbered assembly and tests. It is built manually before generating the production Jellycuts workflow.

Production build order: [Canonical Choir Name](../jelly/shortcuts/reusable/util-canonical-choir-name.jelly), [Archive Choir PDF](../jelly/shortcuts/reusable/util-archive-choir-pdf.jelly), [Assemble Choir Service](../jelly/shortcuts/reusable/util-assemble-choir-service.jelly), then [MAIN - Build Choir Service](../jelly/shortcuts/main/main-build-choir-service.jelly), all generated in Jellycuts. Complete the [CFG/FS insertion slots](../jelly/docs/choir-service-assembly.md) after export. Archive/assembly rows above preserve companion manual-blueprint status, not a claim that those generated sources are installed. The historical diagnostic is not a production dependency. See [the build guide](../jelly/docs/choir-service-build.md) for the integrated acceptance run.
