# V3 first manual iPad checkpoint — filenames

Status: **Not run** for both new shortcuts. No local compilation or automated/runtime tests were performed. [Contracts and known limits](../../docs/v3-development.md) apply.

## Install this delivery

1. Copy [v3-config.example.json](../../config/v3-config.example.json) into Files as **v3-config.json**. Use a separate file; leave the old config alone. Its location is your choice for this first preview.
2. Transfer [v3-parse-filename.jelly](../../shortcuts/reusable/v3-parse-filename.jelly) through Copyover and compile on the iPad. Confirm the installed name is exactly **V3 - Parse Filename**.
3. Inspect the generated helper before running it. Then transfer [v3-preview-filenames.jelly](../../shortcuts/main/v3-preview-filenames.jelly), compile and install as **V3 - Preview Filenames**. Check its Run Shortcut action targets **V3 - Parse Filename**.
4. No old shortcut, library helper or forScore action is needed. Record Jellycuts/iPadOS versions and all warnings/errors. If compilation fails, keep the first diagnostic and its source line; do not try multiple invented enum spellings.

These sources each begin with the exact installed name for Copyover. No `.txt` source copy is needed. Do not run the helper alone expecting a preview: it requires its two Text arguments, supplied by the preview shortcut.

## Inspect generated actions first

- Helper extraction: two incoming Text items, quoted Repeat Index comparisons 1/2, config from the second item. Dynamic caller List items must be actual sourceName/configJson variable tokens.
- Rule Repeat: Dictionary key reads from its Repeat Item; Match Text uses that rule's pattern. Inside its match If, **Add to Variable** appends ruleKey to named matchedRuleKeys. Following Count uses the current named collection. Keep its Nothing initializer.
- Operators: missing value means **does not have any value**; present means **has any value**. Counts are converted to Text and compared to quoted 0/1/2. Inspect the actual native operators and both operands.
- Regex Replace actions: replacement fields are literal `$1`, `$2`, `$3`; input and find fields are actual filenameStem/selectedPattern tokens. The suffix lowercase action must say lowercase; its input is capture 1, while the readable name keeps its original case.
- Result chain: each Set Dictionary Value consumes the previous result Dictionary and real Text tokens. The last action must return the final Dictionary. The documented `exit(var: finalResult)` return is unverified here; if needed insert native Stop and Output with **finalResult**, no-recipient behavior Do Nothing. Record that as a repair, not generated success.
- Preview: Name and File Extension read the current selected native File; File Extension must be the real detail, not a literal word or wrong default. Run Shortcut returns the helper result; key reads use that result. Quick Look and final Output must read current named report after the Repeat, not its initial heading.

If one of these is wrong, record the untouched export before editing. Native completions/reconnections have stable `V3-...` comments at the relevant source actions.

## Run the smallest useful case

Launch **V3 - Preview Filenames**. Select the separate v3-config.json, then one PDF named `Tue1-Walsh-Responses.pdf` (a disposable renamed copy is sufficient because this increment only reads its name).

Expected: one report with parsed status, day tue, slot evensong, service Evensong, position 1 and canonical Walsh-Responses. File name details may omit `.pdf`; that does not change canonical output. No archive or forScore changes.

If this fails, report that first boundary before trying the wider matrix. In particular, an empty/wrong result may be a caller List, Dictionary mutation or return-token problem. A successful compile is insufficient.

## Check the remaining cases

Use actual PDFs or disposable copies renamed in a small Files folder. Select several in one run. Expected rows are independent of picker order; this increment does not sort. The examples below describe expected results, not measured outcomes.

| Filename | Expected result with supplied defaults |
| --- | --- |
| Tue1-Walsh-Responses.pdf | parsed; tue / evensong; position 1; Walsh-Responses |
| Sun1-Walsh-Responses.pdf | parsed; sun / eucharist; Eucharist |
| Sunam2-Smith-TeDeum-EditionB.pdf | parsed; sun / mattins; position 2; Smith-TeDeum-EditionB |
| Sunpm10-Harris-Anthem.pdf | parsed; sun / evensong; position 10; Harris-Anthem |
| SunRemem1-Piece.pdf | parsed; sun / special-remem; readable name Remem |
| sunREMEM1-Piece.PDF | parsed; sun / special-remem; readable name REMEM, same slot |
| Thu2-Piece.pdf; Thur2-Piece.pdf; Thurs2-Piece.pdf | Each parsed as thu / evensong, never special-rs or a conflict |
| ThursRemem1-Piece.pdf | parsed; thu / special-remem |
| ThuRemem1-Piece.pdf; ThurRemem1-Piece.pdf | unresolved; shorter Thursday special aliases need an explicit boundary convention |
| Mon1-Piece.pdf | skipped; mon / evensong; day disabled |
| WedRemem1-Piece.pdf | skipped; wed / special-remem; day disabled |
| Wed1-Piece.pdf | unresolved; no regular Wednesday rule; do not guess a service |
| Sun0-Piece.pdf; Sun01-Piece.pdf; Sun1-.pdf | unresolved; initial convention rejects zero, leading zero and empty payload |
| Unprefixed-EditionB.pdf | unresolved; empty parsed fields |
| Tue1-Piece.txt | unresolved non-PDF row from the caller |

Then edit only a **disposable copy** of the config and select that copy:

1. Turn Sunday mattins enabled to off: Sunam is skipped while Sunpm remains parsed.
2. Add a new nonoverlapping rule for `Tue_1_Piece` using the same three captures: `^(Tue)_([1-9][0-9]*)_(.+)$`, dayKey tue, slotKey evensong, special off, unique key. Old and new names should both parse without source edits.
3. Duplicate a matching rule under another unique key: the affected name is unresolved due to multiple matches, with empty parsed fields. Other names continue.
4. Change version to 1: the caller reports an error before music selection/processing. Malformed JSON or malformed regex can stop natively; capture the actual error without claiming a returned report.
5. Cancel the initial explanation, config picker and music picker in separate launches. Native picker cancellation may exit immediately. Confirm no music or forScore writes.

## Result record

| Checkpoint | Result |
| --- | --- |
| Helper compilation and generated-action inspection | Not run |
| Preview compilation and target/List inspection | Not run |
| One-file parser call and native Dictionary return | Not run |
| Filename/schedule matrix and qualifier preservation | Not run |
| Config-only format change, exclusions and overlap | Not run |
| Invalid config and cancellation | Not run |

Send back the source revision (both currently 1), actual installed names, app versions, first error if any, native repairs and actual preview rows. Distinguish untouched-source success from success after a native repair. Please also supply one or two actual week-folder names for the next date-parsing increment; dates are deliberately absent here.
