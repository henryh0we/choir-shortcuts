# Config-based choir workflow

**21 October update:** Current sources are Canonical 10 / Archive 14 / Assembly
12 / Main 4. Read [the pre-iPad review](pre-ipad-review.md) first for Output fixes,
setlist preflights and exact transfer/native-token checks. The older revision and
Exit-return instructions below are historical. Interfaces remain unchanged;
the user's completed archive should be preserved.

**Current source: Archive 14 / Assembly 11.** The user confirms the small flush-left, parenthesized If probe returns Conditional output reached. The indented parenthesized probe dropped its Output; the unparenthesized probe dropped its If. Both helpers now keep code flush left and use positional `output("ERROR: ...")`, with no notes: label. Literal multiline message whitespace is preserved. Warnings about missing noResultBehaviour and response remain unresolved: the successful probe is not warning-free. This establishes only the tested conditional stop/Text fixture, not interpolation, File returns, nested loops or either complete helper. Existing native ARC/CFG/CONF/COL/SCORE/FS completion remains; no native validation construction is required.




17 October 2026. Current revisions: canonical **9 / interface 2.0**, archive **14 / completed interface 2.1**, assembly **11 / completed interface 1.1**, main **3 / interface 1.0**. Current sources are Drafted; config parsing, native context transfer and updated exports have not been tested on the iPad. Earlier successful naming/save fixtures apply to manually adjusted older versions, not these revisions.

For current archive/assembly source, follow the [18 October compatibility checklist](helper-compatibility-update.md). It supersedes older Output-field, selector and Repeat Results instructions below.

## Configuration location and keys

```text
Choir Music/
  config.json
  Library/
    Introits/
    Responses/
    ...
  Services/
```

Keep your existing config at the actual Choir Music root. The repository's [example](../config/config.example.json) copies the values supplied by the user; it is not automatically installed or substituted. No update to the existing config format is required. The downloaded Windows temporary file is not the on-device config location and is not edited by this change.

| Key | Current use |
| --- | --- |
| `version` | Required; only `1` supported. This is config schema version, independent of Shortcut interfaces. |
| `prefixRegex` | Required, nonempty. Used as supplied, case-insensitively, after removing a terminal `.pdf`. Invalid expressions halt before writes. Your supplied rule supports `Thur`; it does not strip `Thu` or `Thurs` unless you change the config. |
| `categories` | Required nonempty array of category names. Drives picker order. The chosen name must exactly match an immediate child Folder of Library before saving; no category folder is created automatically. |
| `libraryFolder` | Required name of an immediate child of Choir Music, e.g. `Library`. Resolved to a native Folder. It is not an absolute path or permission token. |
| `serviceType` | Optional array of names. Drives a service-type picker and appears in confirmation/report. If absent/empty, report uses `Other`. It does not automatically set a forScore genre/tag or alter the service name. |
| `servicesFolder`, `manifestFilename` | Reserved and retained. No manifests, service copies or persistent indexes are written by this release. |

Required-key presence/version, regex syntax, Library resolution, selected-category resolution and PDF extension are checked before archive saves. Invalid JSON fails at Get Dictionary from Input. Native Shortcuts may coerce value types: these checks are not a complete JSON schema validator. Keep the array/string/number types shown in the example. A native action failure halts the run; no try/catch is claimed.

## Input contracts and callers

We use native Lists instead of constructing a Dictionary containing Files. The inspected Dictionary/setValue bindings cannot establish that such construction preserves native File/Folder values. Lists contain whole native variable references, not interpolated filename/path strings. Native List behavior remains a device check; run [the context probe](../tests/compatibility/probe-config-context.jelly) or the equivalent read-only test before archive writes.

| Installed Shortcut | Input | Output |
| --- | --- | --- |
| UTIL - Canonical Choir Name | Exactly two Text items: `[filename, prefixRegex]` | Canonical Text; invalid/missing input returns no useful value after validation. |
| UTIL - Archive Choir PDF | Exactly three native items: `[one PDF File, Library Folder, parsed config Dictionary]` | Native existing/saved PDF after CFG completion; validation returns ERROR: Text which assembly rejects before import. |
| UTIL - Assemble Choir Service | Text `interactive`, as before | Report Text, now including selected service type. |
| MAIN - Build Choir Service | No input consumed | Calls updated assembly and returns report. |

User correction, 18 October 2026: set the naming helper receiving type to Text in Apple Shortcuts. Its config-based caller still supplies two separate Text items (filename and prefixRegex); verify this setting preserves both items for NAME01/NAME02. The archive must still receive the whole three-item native List without Text conversion. Configure no input to stop with an explanatory error. Old one-Text/one-File callers are incompatible and must be replaced. Tests and third-party callers must build the exact List contract. Count checks expose flattening or missing context; they do not prove object types.

The assembly helper reads `config.json` once before PDF selection and all writes, resolves Library once, then passes that same native Dictionary/Folder to every archive call. The archive still scans Library for each PDF. A once-per-service recursive index is a separate optimization, not implemented here. Config is reread on the next service run; it is not reread midway through a run.

## Install and complete slots

The naming helper now also requires **NAME01** and **NAME02** after export. The installed compiler rejected the reviewed getItemFromList selector forms, so the source contains Nothing placeholders instead of guessing another spelling. Replace NAME01's Nothing with native Get Item from List: List = Shortcut Input, Item at Index = 1. Replace NAME02's Nothing with the same native action at index 2. Reconnect the filename presence If and filename Text action input to NAME01's output; reconnect the prefixRegex presence If and second Replace Text Find field to NAME02's output. Use native tokens, then delete each unused Nothing. Keep the first Nothing producing noNameResult for empty validation exits. There is no extra assembly-guard stop in this helper; uncompleted placeholders yield no usable name. Compile/export of the new skeleton and its Exit action still need confirmation.

Preserve renamed copies of your working installed shortcuts and their native edits. Compile/import in order: naming, archive, assembly, main. Keep exact installed names, reselect them in Run Shortcut actions and update all four as a set. Refreshing from `.jelly` reinstates guards and slots; `.txt` files are byte-identical transfer copies.

In the **assembly helper**, retain its first guard while completing:

| Slot | Native action/settings | Reconnect |
| --- | --- | --- |
| CONF01 | Replace Nothing with Folder selecting **Choir Music**, the parent containing config.json and Library. | Root Get Contents of Folder and CONF02's Folder. |
| CONF02 | Replace Nothing with native Get File from Folder: Folder = CONF01, file path = `config.json`, error if missing enabled. | Get Dictionary from Input immediately below must consume that File. |
| FS01â€“FS13 | Complete the existing [forScore slot table](choir-service-assembly.md). | Preserve all native Score/Composer/Setlist connections. `workingScore` is now a named variable, not an If Result. |

CONF02 is an explicit native insertion because the inspected Jelly Get File signature does not expose a native Folder destination. Do not substitute the legacy action's default Shortcuts folder, a cloud path string or an unrelated config picked elsewhere.

In the **archive helper**, old CFG01 is removed. Its Library Folder comes from context item 2; do not add a second independent root setting. Complete:

| Slot | Configure |
| --- | --- |
| CFG02 | Save File: input = native renamedFile; Ask Where to Save off; destination = **named native `typeFolder`**, resolved from the category name; Overwrite off. The picker now returns Text, so do not wire Chosen Item directly as a Folder. |
| CFG03 | Inspect Exit result = named native `existingCleanFile`. |
| CFG04 | Inspect final Exit result = native `savedCleanFile` from Save File. |

Current revisions use Exit variable returns instead of the Output binding. Archive validation returns noArchiveResult (Nothing); CFG03/CFG04 return native Files directly. Inspect those native tokens after export. Keep explanatory Text output on service failures. Check incoming List item extraction, Run Shortcut inputs, all If/End If and Repeat/End Repeat markers, mutable-variable references and final returns. Only after completion remove each helper's initial ASSEMBLY GUARD Stop and Output. Keep validation/return stops and Nothing initializers.

Only `//` comments are used; one source line creates one native Comment block in the user's app. There is no block-comment requirement.

## Test and recover

Use the [config integration checks](../tests/config-integration.md). For a standalone archive test, choose one disposable PDF, select the test Library Folder, read the parent config File using Get Dictionary from Input, then build a native three-row List using those whole variables. Run archive with the List and inspect the returned filename/location. Input item 2 is Library, not Choir Music.

Use Get Details of Files â†’ Name â†’ Show Result instead of requiring Quick Look, whose UI failed in the earlier fixture. Check the actual saved PDF in Files. Repeat the same source to check reuse, with no second save/category prompt. Re-export restores all manual-completion requirements; retain your working copies until the new version passes.

## Manual naming input/output repairs (18 October 2026)

The user reports changing the imported helper's receiving type to Text and correcting the final output to canonicalName. Revision 9 records both repairs in source comments, explicitly converts the extracted filename to Text before replacement, and retains the already-correct final exit(var: canonicalName) variable return. Inspect the final native Stop and Output and reselect the second Replace Text result if export does not preserve that connection. Do not use a literal variable name or the original input as the result. Receiving-type metadata is not available in the local documented Jelly metadata (Color and Icon only), so the Text receiving setting remains a post-import edit rather than a guessed directive. The two-Text List calling contract and configurable regex remain unchanged. Check extraction indexes 1/2, no-input behavior and the returned canonical name after regeneration; no new compiler/runtime pass is claimed.
