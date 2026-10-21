# Build the choir service workflow

**Archive 15 update, 21 October 2026:** ARC01-ARC03 manual extraction is replaced
in source by a quoted-index loop, with Nothing-initialized native variables.
Mixed File/Folder/Dictionary preservation is still unverified on the iPad; run
[the read-only context test](../tests/compatibility/archive-context-loop.md).
CFG02-CFG04 remain manual. Preserve the working installed archive and keep the
new initial guard until native extraction and CFG completion are checked.
Earlier ARC instructions below describe revision 14 and are superseded for 15.

**21 October update:** Transfer Canonical 11 / Assembly 13 / Main 4; preserve the
user's working completed Archive 14 when its interface matches. Follow
[the pre-iPad review](pre-ipad-review.md) for new collection/setlist checks,
Output compatibility fixes and the required native slot/variable inspection.
Older revision/Exit instructions below are historical. Changed revisions still
need compilation and testing in Jellycuts on the iPad.

**Current source: Archive 14 / Assembly 11.** The user confirms the small flush-left, parenthesized If probe returns Conditional output reached. The indented parenthesized probe dropped its Output; the unparenthesized probe dropped its If. Both helpers now keep code flush left and use positional `output("ERROR: ...")`, with no notes: label. Literal multiline message whitespace is preserved. Warnings about missing noResultBehaviour and response remain unresolved: the successful probe is not warning-free. This establishes only the tested conditional stop/Text fixture, not interpolation, File returns, nested loops or either complete helper. Existing native ARC/CFG/CONF/COL/SCORE/FS completion remains; no native validation construction is required.




17 October 2026. Current source revisions: canonical 9 (interface 2.0), archive 14 (completed interface 2.1), assembly 11 (completed interface 1.1), main 3 (interface 1.0). These config-based revisions are Drafted, not compiled or device-tested. Earlier manually adjusted naming/save fixtures remain historical evidence.

Start with [config integration and migration](config-integration.md), which owns the current input contracts and config slots. The existing [forScore assembly table](choir-service-assembly.md) still owns FS01-FS13. This release retains the user's generated-source plus native-insertion workflow.

Use the [current compatibility checklist](helper-compatibility-update.md) for ARC01-ARC03, SCORE01-SCORE02, COL01-COL03 and Exit return checks in addition to the existing config/forScore slots.

## Install in dependency order

| Order | Installed name | Completion |
| --- | --- | --- |
| 1 | [UTIL - Canonical Choir Name](../shortcuts/reusable/util-canonical-choir-name.jelly) | Revision 11 extracts both Text items in source; no NAME slots. Compile/import and inspect argument count, named-variable references, replacements and returned canonicalName Text. |
| 2 | [UTIL - Archive Choir PDF](../shortcuts/reusable/util-archive-choir-pdf.jelly) | Revision 15: compile/import; verify the three-item native context loop; complete CFG02-CFG04. No ARC insertion slots remain. |
| 3 | [UTIL - Assemble Choir Service](../shortcuts/reusable/util-assemble-choir-service.jelly) | Compile/import; complete CONF01-CONF02, COL01-COL03, SCORE01-SCORE02 and FS01-FS13. |
| 4 | [MAIN - Build Choir Service](../shortcuts/main/main-build-choir-service.jelly) | Compile/import and reselect the completed assembly helper. |

Preserve renamed working copies before replacement. Update the set together: old filename-Text and single-PDF callers are incompatible with the new utility contracts. The `.jelly` files are authoritative; matching `.txt` files are byte-identical transfer copies. No Mac is required. Keep each helper's initial ASSEMBLY GUARD until its native slots, control-flow markers and input/result tokens are checked.

## Configure once

In assembly CONF01 select the native **Choir Music** root, the parent containing `config.json` and Library. CONF02 gets `config.json` from that exact Folder. Get Dictionary from Input reads it once per service run. Set `libraryFolder`, `categories`, `prefixRegex` and optional `serviceType` in the file, using the [example format](../config/config.example.json). The existing config keys and version 1 are supported unchanged.

The service resolves `libraryFolder` to a native immediate child Folder. It passes the PDF, that Folder and the same parsed config Dictionary to archive in a native List. Old archive CFG01 is retired; do not configure a separate archive root. The category picker returns configured category Text, which archive resolves to a native Folder before saving. CFG02 must use named `typeFolder`, not the picker's Text.

The naming helper now receives a two-Text List `[filename, prefixRegex]`. Its caller supplies the pattern from config. Do not retain the earlier Text-only receiving setting. The archive receives `[PDF File, Library Folder, config Dictionary]`, not JSON-encoded objects or path strings.

## Run a service

Launch MAIN - Build Choir Service. Select a configured service type if available, choose disposable Nextcloud PDFs, establish running order, enter a dated name and review before writes. The helper then saves/reuses clean archive PDFs, retrieves/imports working scores and offers title/composer review. FS actions still require manual insertion because no forScore Jelly binding has been established.

Choose Create new for an unused name, or Replace existing and explicitly select/confirm the existing setlist after scores are prepared. Readback count and Manual order require inspection; count equality alone does not prove identity or ordering. Failed/cancelled native actions may leave prepared PDFs/scores or a partial setlist. Inspect state before retrying.

## Verification and boundaries

Use [config integration tests](../tests/config-integration.md) for the native List boundary, changed regex/category config, missing config/folders, save/reuse and the integrated service. A read-only [context probe](../tests/compatibility/probe-config-context.jelly) isolates native File/Folder/Dictionary transfer before archive writes. Inspect generated If/Repeat structure; an earlier export omitted an If wrapper. Check named variables and native output connections after export.

The service reads config once but archive still scans Library per PDF. Once-per-service archive indexing is not implemented. File selection may download PDFs before lookup. No automatic category inference, genre/tag assignment, manifest, Services-folder copying or persistent index is added. `servicesFolder` and `manifestFilename` remain reserved. Existing clean PDFs are not overwritten; duplicate canonical archive identities stop for review.

Re-export restores guards and manual slots. Reapply the [current setup](config-integration.md) and native FS wiring to new exports. Use Get Details of Files → Name → Show Result and inspect Files to validate returned PDFs; the earlier Quick Look UI error is separate from a successful save/filename result.
