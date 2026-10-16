# Build the choir service workflow

Implementation release 1, assembly revision 3, 16 October 2026. Current source revisions: canonical 4, archive 5, assembly 3, main 2; completed interfaces remain 1.0. Generate all four Shortcuts in Jellycuts, then insert native forScore actions at their Comment markers. Build the whole workflow and resolve remaining differences during its first service run. No further isolated action experiments are prerequisites. The sources are Drafted, not compiled or installed by this workspace.

## Install these four Shortcuts

| Order | Exact installed name | Build method |
| --- | --- | --- |
| 1 | [UTIL - Canonical Choir Name](../shortcuts/reusable/util-canonical-choir-name.jelly) | Compile/import in Jellycuts |
| 2 | [UTIL - Archive Choir PDF](../shortcuts/reusable/util-archive-choir-pdf.jelly) | Compile/import, then complete four CFG fields/actions |
| 3 | [UTIL - Assemble Choir Service](../shortcuts/reusable/util-assemble-choir-service.jelly) | Compile/import, then insert 13 forScore actions |
| 4 | [MAIN - Build Choir Service](../shortcuts/main/main-build-choir-service.jelly) | Compile/import in Jellycuts |

Use Jellycuts 2026.6.4 on the iPad for all four source files. Follow [the Comment-slot assembly guide](choir-service-assembly.md) after export. Keep both helpers' initial assembly Stop and Output guards until their slots are complete. Inspect compiler messages, import each export, and set its exact installed name. Existing source signatures are candidates for this app build, not a claim that its bundled compiler is identical. No compatible local Jelly compiler was found on PATH during this implementation.

The generated main is deliberately small. File selection, ordering, metadata prompts, branching and loops are generated inside the assembly helper. Only the native forScore action slots need insertion. The archive helper is generated too; four CFG markers cover a saved Folder reference, native save destination and two native File returns that the reviewed bindings cannot fully express. Native Scores and Setlists remain inside the assembly helper; the main passes/receives Text. Source comments become actual Comment actions, and temporary Nothing actions mark result-producing slots. After replacing an action, reconnect its downstream outputs as listed in the assembly guide.

## Configure the archive once

Canonical helper device setup: user-confirmed working for `Fri1-Walsh-Responses.pdf` after native variable wiring corrections and removal of the unconditional initial Stop and Output. Configure received input as Text and show an error if no input is supplied, matching the user's installed setup. Keep the final return connected to the second Replace Text result. These on-device changes must be checked/reapplied on re-export; they are not all encoded by the source. This fixture passed; other filename variants and archive integration still need testing.

Before configuring/running the archive, inspect its generated native If/End If and Repeat markers. The earlier canonical export omitted an If wrapper, so do not assume compilation preserved control flow. In particular, the archive's No source PDF alert and following empty Stop and Output must be inside an If testing that Shortcut Input has no value. Its other validation stops must also remain inside their conditions. Keep the initial ASSEMBLY GUARD until CFG01-CFG04 and these structure checks are complete.

At CFG01 in the generated Archive Choir PDF, insert a Folder action and select the existing iCloud `Choir Music/Library` folder. Keep its immediate children as the music-type folders. This is the only archive-root setting. The workflow selects one of those folders when saving a new clean PDF; it does not recreate your old folder-setup Shortcut.

Use one working forScore collection and search using Get score named Name. The user has confirmed that the original PDF stem still finds the renamed test score, that the new name also finds it, and that an unrelated name finds none. This is evidence for this fixture, not a guarantee about duplicate names or every forScore library configuration.

## Run a service

Launch MAIN - Build Choir Service. In the Files picker, browse the signed-in Nextcloud location and select the PDFs for one service. Confirm the running order using the sequential picker, enter a dated service name, and review the filename list (joined with ` | `) before any archive/import writes. This makes order explicit rather than relying on Files selection order or lexical sorting of Sun2/Sun10.

The workflow then saves/reuses each clean iCloud PDF, retrieves its canonical score, imports missing working copies, and offers readable title/composer metadata. Existing scores default to being preserved; choose Review metadata to finish an interrupted import or edit a score deliberately.

For a new service, choose Create new and use an unused name. For a repeat run, choose Replace existing, select the actual setlist, and confirm replacing its running order only after all working scores have resolved. The operation changes setlist entries, not the underlying scores. It is not transactional; a failure after clearing entries can leave a partial list, so rerun and replace that same setlist to recover.

Score identities retain complete movement, verse and variant qualifiers. Example: Fri1-Walsh-Responses.pdf becomes Walsh-Responses.pdf for the archive/import and Walsh-Responses for lookup. Composer/title suggestions are reviewed by the user, including uncertain hymn, psalm, RSC and administrative filenames. No full composer names are invented.

## Boundaries of this release

- Nextcloud file selection can download selected PDFs before lookup. This release does not promise metadata-only browsing or downloads restricted to missing scores.
- Music type is chosen from the existing iCloud folders for each new archive copy. Composer and title are applied in forScore; type/variant text stays in canonical identity and the archive path. Automatic genre/tag assignment and persistent classification mappings are deferred, rather than guessed from action names.
- Existing PDFs are never overwritten by the archive helper. Multiple archive matches or ambiguous names stop for review. The name lookup itself has no demonstrated duplicate-reporting contract: keep canonical names unique and resolve known collisions before running.
- Readback checks entry count and displays Manual order for review. Count equality alone does not prove score identity or ordering. Repeated scores are submitted with Skip if already added off; confirm the actual order in the readback.
- There is no automatic scan replacement, full library migration, cloud sync setup, or background automation. The run report is returned as Text; no hidden state or machine-readable recovery journal is written. Recovery uses stable lookup and explicit metadata review/setlist replacement.

## One integrated acceptance run

Compile/import and complete the marked native insertions once, then use two disposable PDFs for a single service: one score already present and one absent. Check clean archive copies, readable title/composer, the requested setlist order, and a repeat run using Replace existing. Also cancel at the initial preview and confirm no writes occur. Record results in [the service acceptance record](../tests/choir-service.md). Diagnose the first failing action in that real run; no separate action-by-action test campaign is required.

Keep the historical [import diagnostic](../../manual%20creation/shortcuts/main/test-forscore-import-and-lookup.md) for reference. Its single-score/First Item logic is not used by production.

Sources: [Jelly Run Shortcut](https://docs.jellycuts.com/Documentation/Shortcuts/runShortcut.html), [Jelly Replace Text](https://docs.jellycuts.com/Documentation/Shortcuts/replaceText.html), [existing compiler reference](jellycuts-reference.md), [forScore evidence](../../forscore-action-evidence.md). Source review does not establish compilation or operation on the device.

## Update from earlier exports

Preserve completed installed copies of Archive Choir PDF and Assemble Choir Service, then recompile source revisions 5 and 3 respectively. Reapply CFG01-CFG04 and FS01-FS13 to fresh exports before removing their guards. CFG03 now returns the named `existingCleanFile` variable; it no longer points to a Get First Item action. Verify its presence checks and native File value in the editor. Installed names and completed interfaces have not changed, so main revision 2 can stay installed if already compiled/imported. Canonical revision 4 must replace earlier revisions: it removes both the rejected If-result capture and the guard whose generated If wrapper was missing. Recheck the main's Run Shortcut selection and run the integrated cases, including duplicate archives and existing-file reuse.

Sibling `.txt` files are byte-identical transfer copies of the `.jelly` source for on-device use. Edit `.jelly` as authoritative, then refresh its matching `.txt`; do not use an older transfer copy.
