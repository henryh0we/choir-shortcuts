# forScore Action Evidence

Initial screenshot review: 14 October 2026. Latest user evidence: 15 October 2026. The user reports iPadOS 26.6, forScore 15.2.5 and Jellycuts 2026.6.4. Nextcloud appears under Locations in Apple Files. Initially reported empty, the forScore library now contains three scores during diagnostic testing. The user's existing iCloud folder-creation Shortcut creates `Choir Music/Library` with music-type subfolders.

The following settings are visible in the two screenshots supplied in chat. They establish editor labels and displayed settings, not execution results or complete input/output contracts. The original [action inventory](forscore%20shortcut%20actions.md) is preserved separately.

| Action shown | Visible settings | Implication for the design |
| --- | --- | --- |
| Get all scores in Library | Library selector; Sort Order: Title | Score retrieval is scoped through a library selection. Available library choices and returned properties still need inspection |
| Filter Scores | Rule: Match All; Composers, Genres, Tags, Labels, Reference, Rating, Difficulty, Key | Filename/title filtering is not visible in this screenshot. Do not claim the filter can match canonical filenames |
| Import Files | Conflict Handling: Skip | Two import cards show the same wording/settings; the screenshot does not distinguish their catalogue identities. Test one at a time and identify its actual return type |
| Rename Scores to Name | Scores and Name inputs | Separate display-title and physical-filename effects remain unverified |
| Add metadata to Score and Bookmarks | Composers, Genres, Tags, Labels | These categories are configurable. Category object versus Text inputs and readback remain unverified |
| Get composer named Name | Continue if not found: off | Proposed lookup should enable this setting for a missing-composer branch; confirm whether absence produces an empty output |
| Create composer named Name and add to Scores and/or Bookmarks | Name, Scores, Bookmarks | Creation can visibly target scores/bookmarks. Test creation and assignment together instead of assuming a separate metadata action is always required |
| Create Setlist Name | Folder selector | Setlist folder is visible; library assignment and returned object are not established |
| Add Scores to Setlist | Skip if already added: off | Proposed ordinary retries enable this setting; repeated intentional occurrences require a separate tested policy |
| Get entries in Setlist | Sorting: Manual | Manual-order readback is selectable. This does not establish append order or guarantee arbitrary reordering |

## Proposed initial configuration

Use the current single forScore library. Retrieve scores in its verified selection; do not create a second library merely to mirror iCloud music types. Use genres for music type and setlists for services.

Use canonical filenames when staging/importing new scores. Keep a persistent mapping from canonical identity to actual imported score identity. Establish exact score lookup using exposed score properties or a tested identity field before a repeat import. Reference is a possible lookup field because it is visible in the filter, but its meaning and setter contract must be confirmed before assigning custom identity values.

For composer lookup, enable Continue if not found and test a missing composer before branching to creation. For import, begin with Conflict Handling: Skip and verify the skip outcome; it is not an import receipt. For normal setlist retries, enable Skip if already added and verify the actual entries using Sorting: Manual. Deliberate repeated scores must be tested independently so retry protection does not erase the running order.

## Focused trials still needed

1. Import one disposable PDF with a canonical filename. Inspect the import result and every score property available on that result and on Get all scores.
2. Rename that score, then inspect its display title and actual filename separately. Repeat import with Skip and record its output/library effect.
3. Retrieve a missing composer with Continue if not found enabled; inspect output. Create the composer with that score as its target and verify assignment through get composers.
4. Create a disposable setlist, add scores A and B, read Manual order, rerun with Skip if already added, and inspect the entries. Test A, B, A separately.

## Reported diagnostic results on 15 October 2026

- The shared fixture previews as a PDF in Quick Look.
- The user located the imported score under All Libraries; querying the named library Empty had returned zero. Import does not establish membership in that named library.
- After correcting the selected scope, the user reports repeat-run counts of 3 before and 3 after. This is consistent with no additional import, but counts alone do not establish exact identity.
- Get First Item selects from the entire retrieved library, not a match to the input PDF. Opening forScore from that result does not establish that the supplied PDF was selected.
- Tapping RetrievedScore in Open score shows Type: Score, with no additional properties reported.
- The numeric comparison editor crashed when entering 1. A Text comparison was suggested as a workaround; its exact installed configuration has not been recorded.

These are user-reported observations of a modified diagnostic, not a pass of the original single-score specification. Exact installed changes and import output type remain unrecorded. Composer/rename/setlist trials remain Not run. No native action identifiers or Jellycuts bindings have been inferred.

## Get score fields reported on 15 October 2026

The user reports an expanded action reading Get score named Name, with Continue if not found, Composers, Genres, Tags, Labels and a Reference Text field. Category selectors offer existing categories, a variable, or Ask Each Time. The initial value of Continue if not found was not specified.

This establishes a configurable Name input and additional category/reference selectors. It does not establish whether Name means display title or PDF filename, exact/case-insensitive matching, library scope, absence output, or duplicate-name handling.

Confirmed by the user on 15 October 2026: supplying the PDF filename without its extension finds the test score; changing to a nonmatching name finds no score. This establishes the known-name and missing-name cases on the reported device/app. The complete installed test configuration and exact absent-output representation were not supplied.

Use Get score named Name as the primary lookup route, passing the complete canonical payload without `.pdf`. Preserve movement/variant/verse qualifiers. Do not select the first item of Get all scores as a substitute for matching.

Subsequent user-reported rename results on 15 October 2026: after the disposable score was renamed to Choir Lookup Renamed, both original and new lookup names returned Choir Lookup Renamed in Quick Look. An unrelated lookup name returned no score. This supports retaining the original PDF stem as a usable lookup key after changing the displayed name for this fixture. It does not identify the underlying storage field or establish duplicate-name behaviour.

Still unverified: matching case/diacritics; duplicate-name handling; full library scope; and behaviour across different editions/name collisions. The user has requested proceeding with the whole workflow rather than more isolated tests. Resolve remaining contracts during construction and the first integrated service run; see the release 1 build guide.
