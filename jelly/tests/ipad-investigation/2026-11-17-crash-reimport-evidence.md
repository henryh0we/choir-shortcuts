# Crash and reimport evidence — 17 November 2026

## Follow-up, 24 November 2026

The user reproduced the failure with both individual and grouped files and
isolated it to psalms and hymns whose composer default was `-`. They report
consistent success after leaving the default blank. V4 Check or Upload revision
3 incorporates that repair. The duplicate-score behaviour from the earlier
reimport has no separate follow-up result. [Composer repair and checks](../../docs/v4-check-or-upload.md#installed-composer-repair-confirmed-24-november-2026)

## User-reported sequence

The user attempted to create the service for tonight. The workflow asked for
the choir names and other expected setup information. When it reached the
preparation phase, the selected files were present. The app then crashed.

The user subsequently updated the piece information manually and tried the
import again. The following behaviour was observed for the first set of
pieces:

1. The composer, type and other identifying metadata were manually removed.
2. The files were renamed from `[composer]-[title].pdf` to `[title].pdf`.
3. Re-running the import asked the user to select the inputs for those pieces
   again.
4. The import created duplicate pieces. The duplicates were still named
   `[composer]-[title].pdf` and had the correct composer and type fields.
5. This run did not crash.
6. The service was created using the new `[composer]-[title].pdf` files.

Exact filenames, the number of pieces, the crash screen/message, device and
app versions, and the precise action at which the crash occurred were not
recorded.

## Evidence-supported interpretation

- The crash happened after the files were visible during preparation, so file
  presence alone does not explain the failure.
- Renaming a piece from `[composer]-[title].pdf` to `[title].pdf` appears to
  have changed the identity used by the import/reuse path, or at least made it
  impossible for that path to recognise the existing piece. The second run
  therefore requested inputs again and created a new piece rather than
  reusing the manually edited one.
- The successful second run suggests the crash is not reliably caused by the
  source PDFs being present or by the metadata prompts themselves. It may be
  in a later native action or in state left by the first run, but this is only
  a hypothesis.
- The fact that the newly created files regained the
  `[composer]-[title].pdf` form, with composer and type populated, suggests
  that the import/preparation path treats the canonical filename and metadata
  as authoritative when it creates a piece. This does not establish whether
  the original renamed piece was deliberately ignored, failed lookup, or was
  considered a different identity.

## Follow-up investigation

Preserve the crash-run and reimport-run artifacts before making another repair.
For a disposable pair of pieces, record the exact filename, title, composer,
type, score identity and setlist membership after each boundary:

1. source selection and preparation;
2. archive/clean-file lookup or save;
3. score lookup/import;
4. title/composer/type updates; and
5. service/setlist creation.

Then compare these cases:

- unchanged canonical `[composer]-[title].pdf`;
- the same piece renamed to `[title].pdf` with metadata removed; and
- the same piece restored to the canonical filename with metadata retained.

The key questions are whether filename canonicalisation is the lookup key,
whether metadata edits rename the underlying forScore score, and whether the
crash occurs before or after the first score/setlist write. Check for an
existing score before retrying so a failed run is not mistaken for a missing
piece and another duplicate is not created.
