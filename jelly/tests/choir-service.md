# Choir service integration record

Release 1, 15 October 2026. Current stage: Drafted. Native helpers: Designed. Target reported by user: iPadOS 26.6, forScore 15.2.5, Jellycuts 2026.6.4. Actual compiler/import results for these new files: Not run.

Build using [the installation guide](../docs/choir-service-build.md). Record compiler messages and any action-setting differences here during construction; those are integration fixes, not a prerequisite test campaign.

| Case | Steps and expected observations | Actual result |
| --- | --- | --- |
| Whole service | Select two disposable Nextcloud PDFs, order them B then A, one existing in forScore and one missing. Clean PDFs retained, existing score reused, missing score imported, confirmed title/composer applied, one service contains B then A | Not run |
| Repeat and repair | Run same selection, choose Replace existing and the same setlist. No duplicate scores/archives; chosen running order restored. Choose Review metadata for any pending metadata | Not run |
| Cancel before writes | Cancel initial filename preview. No archive, score or setlist writes | Not run |
| Invalid/missing input | Run canonical helper without input: empty Text, no writes. Call assemble with other mode: explanatory Text, no writes. Non-PDF selection in assemble: stop before writes. Archive missing input: no File returned and explanatory alert | Not run |
| Unprefixed/variants | Use Jackson-InGminor.pdf and a separate movement/verse-qualified score. Full canonical identities retained; reviewed metadata does not merge variants | Not run |
| Failure after import | If an action fails after importing, rerun using the same canonical filename and Review metadata. Existing working score is reused. Inspect actual state before retrying an uncertain import | Not run |

For Canonical Choir Name, source-reviewed examples are Fri1-Walsh-Responses.pdf → Walsh-Responses; Sunam4-Howells-CollegiumRegale-TeDeum.pdf → Howells-CollegiumRegale-TeDeum; Sat3-Ps89vv30-50(Plainsong).pdf → Ps89vv30-50(Plainsong); Jackson-InGminor.pdf → Jackson-InGminor. These examples are expectations, not recorded compiler/device passes.

Implementation record: revision, builder, device, date, compiler/import outcome, actual results and unresolved failures: Not recorded. Only promote the current release after its actual integration run. Preserve the earlier user-reported native lookup/rename evidence separately.

Static validation on 15 October 2026: 66 local links across the implementation and affected indexes resolved. Seven canonical-name cases passed using the patterns extracted from the Jelly source and .NET regular expressions. This checks the patterns and expected identities, not Jelly string compilation, Shortcuts generation, or Apple runtime behaviour. No Jelly compiler was available locally. Native branch/loop nesting and source call/dependency names were reviewed separately.

Assembly revision 2, 16 October 2026: archive and assembly now have generated Jelly source. Their native CFG/FS insertions replace the previous hand-build route. Interfaces stay 1.0 after completion. Preserve completed installed copies before regeneration; no prior build/test status transfers to these templates.

| Additional check | Expected observation | Actual result |
| --- | --- | --- |
| Unfinished template | Both helpers' initial Stop and Output prevents provider/forScore writes before slots are completed | Not run |
| Slot wiring | FS01/03/05/09/12 consumers use the newly inserted native outputs, not deleted Nothing outputs; FS11 uses its own writing loop Repeat Item | Not run |
| File return | Both archive return actions use native Files, not filenames or Text interpolation; saving targets the chosen type Folder | Not run |
| Re-export | Fresh exports restore guards/slots; completed installed helper copies remain available for reapplying insertions | Not run |

Static review on 16 October 2026: all four generated sources' call names and required parameter-slot sets were checked against the pinned compiler lookup table/Parameter files. The two new helpers contain 13 unique FS IDs and four unique CFG IDs; both have an initial stop guard. Delimiter balance was checked outside comments/strings. This is source review only; no compiler, export or device pass is claimed.


16 October 2026, user-reported compilation: archive helper fails at each DoNothing identifier with an out-of-scope error. Archive revision 3 replaces these seven enum arguments with Respond pending manual no-recipient configuration to Do Nothing after export. Corrected build/import/run: Not run.

Archive revision 4, 16 October 2026: user reports out-of-scope FileExtension, FirstItem and archiveMatches. Updated archive to the official documentation's spaced enum forms: property File Extension, type Item at Index with index 1 (equivalent to first item). References: https://docs.jellycuts.com/Documentation/Shortcuts/fileDetail.html and https://docs.jellycuts.com/Documentation/Shortcuts/getItemFromList.html . Leave repeat-result capture unchanged pending recompilation: archiveMatches may be a cascading diagnostic from errors inside its loop. Corrected compilation remains unverified.
