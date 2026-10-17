# Config integration acceptance checks

17 October 2026. Canonical 5/interface 2.0; archive 7/completed interface 2.0; assembly 5/completed interface 1.1; main 3/interface 1.0. All new source revisions: Drafted. Compiler, native input types, config parsing, export/import and runtime results: **Not run**. Earlier manually completed naming/archive saves are historical fixtures; the new interfaces invalidate those results for this revision.

Follow [setup and contracts](../docs/config-integration.md). Use a disposable Choir Music root with the supplied config and matching category folders. Preserve your production installed copies. Compile on the recorded Jellycuts app, inspect complete native control flow/variable wiring, fill slots and retain the guards until ready. Do not equate a static schema/source check with device execution.

| Case | Steps and expected observation | Actual |
| --- | --- | --- |
| Native context | Parse the actual config File with Get Dictionary from Input, build native List [disposable PDF, test Library Folder, config Dictionary]. Run the [read-only probe](compatibility/probe-config-context.jelly). Exactly 3 items; correct PDF name/extension; folder can be enumerated; version 1 and 13 categories. No Text/JSON conversion of File or Folder. | Not run |
| Canonical configured rule | List [`Fri1-Walsh-Responses.pdf`, actual config.prefixRegex] → naming helper. Returns `Walsh-Responses`. Unprefixed `Jackson-InGminor.pdf` stays `Jackson-InGminor`. | Not run |
| Config edits take effect | Change the regex in disposable config to `^CUSTOM[0-9]+-`; next run `CUSTOM1-Walsh-Responses.pdf` → `Walsh-Responses`, while `Fri1-` is retained. No code edit/re-export. Restore original rule. | Not run |
| Root resolution | Set libraryFolder to `Test Library`, rename only disposable Library accordingly. Service resolves that native child of the configured Choir Music root. All archives stay beneath it. | Not run |
| Category order/content | Reorder categories or add a new category and matching Folder in disposable config/root. Next archive miss offers that order/name, resolves to Folder and saves there. Unlisted root items are not picker choices. | Not run |
| Archive miss | Native context with `Fri1-TestComposer-TestPiece.pdf`, absent from test Library. Choose Responses. Native `TestComposer-TestPiece.pdf` saved there with Overwrite off; return usable by Get Details of Files → Name. | Not run |
| Archive reuse | Run same input again: returns existing native File, no category prompt, no additional save. | Not run |
| Duplicate archive | Two PDFs in different test categories canonicalize to same identity. Stops before save/import and reports duplicates. | Not run |
| Missing config / malformed JSON | CONF02 fails if missing; Get Dictionary from Input fails if malformed. No PDF save/import/setlist changes occur. | Not run |
| Version / required keys | Unsupported version or missing prefixRegex/categories/libraryFolder stops before saves. Valid config uses Number version, Text regex/folder, Array categories; native coercions are not comprehensive schema validation. | Not run |
| Invalid regex | Broken regex in config halts validation before PDF operations; restore config before next test. | Not run |
| Missing category Folder | Select configured category with no matching child Folder. Stops before Set Name/Save File. Matching ordinary file instead of Folder fails Folder preflight. | Not run |
| Wrong context/legacy caller | Pass old filename Text or lone PDF instead of Lists. Count validation stops; no save. Flattened/mis-typed context must be fixed before use. | Not run |
| Service type | Config serviceType picker supplies chosen type to confirmation/report; no genre/tag writes are inferred. Omitted/empty serviceType uses Other. | Not run |
| Whole service / repair | With slots complete, prepare two disposable PDFs (existing/missing forScore score), choose B then A. Config read once; names, categories and report correct; Manual setlist readback preserves order. Repeat using Replace existing without duplicate archive copies. | Not run |
| Cancellation | Cancel preview before save/import: no writes. Cancellation later can leave prepared pieces or partial setlist; inspect state and rerun explicitly. | Not run |

Record date, tester, exact app/device versions, source hashes/revisions, compiler diagnostics, native slot/token changes, actual results and unresolved errors for each executed case. Quick Look's earlier UI error does not establish that the returned File is invalid; use filename inspection and Files readback.

Static verification on 17 October 2026: 174 action calls across four production sources and the context probe matched local documented parameter-slot sets, with the recorded compiler-backed Output exception. Delimiters balanced; block headers are parenthesized; Magic Variable capture names are unique per source; all production comments are line comments. Four utility callers supply the required List arity, assembly has one config parse, and all four `.txt` hashes match `.jelly`. The supplied example JSON parsed with 13 categories and four service types. Seven configured-name cases passed under .NET regular expressions, including a changed pattern and the supplied rule's intentional retention of `Thu1-`. Fifty-two local navigation links and `git diff --check` passed. No Jelly/Swift compiler is installed on PATH; no compiler, export, import or native runtime pass is claimed.
