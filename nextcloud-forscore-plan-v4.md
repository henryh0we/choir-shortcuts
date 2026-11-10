# V4: Select PDFs, check/import, build a setlist

Date: 10 November 2026  
Status: Implementation plan; shortcuts not yet built or device-tested.

## Purpose

Create a simple first version with three shortcuts:

1. **V4 - Check or Upload**: resolve one PDF to an existing or newly imported forScore Score.
2. **V4 - Create Service**: select PDFs, a date and a service type, then build a service setlist.
3. **V4 - Add to Rehearsal**: select PDFs and create or add to that date's rehearsal setlist.

The user chooses the files and date. This version does not need folder scanning, inferred dates, weekly schedules or automatic service detection. Keep V4 separate from the existing shortcuts and V3 work.

## 1. V4 - Check or Upload

This is the shared shortcut used by both setlist creators. It accepts **one native PDF File** and returns the **native forScore Score** to use, together with a small result report. Preserve native objects when passing them between shortcuts; do not convert the PDF or Score to text.

### Flow

1. Validate that the supplied file is a PDF.
2. Clean its filename: remove recognised service/day/order prefixes and the terminal `.pdf` extension. Preserve composer, work, movement, edition and other distinguishing qualifiers in the lookup name.
3. Look up the complete cleaned name in forScore.
4. If one intended Score exists, reuse it and preserve its annotations and metadata. Do not ask the new-piece questions.
5. If no Score exists, suggest metadata and let the user confirm or correct:
   - **Title**: the work name, with the composer separated out.
   - **Composer**: suggested only from recognised filename conventions; editable and optional if unknown.
   - **Music type**: selected through a Choose from List action using the established categories.
6. Import the PDF using its cleaned filename. Apply the approved display title, Composer and music type to the imported Score.
7. Return the resolved Score and a result identifying whether it was reused or imported, with its title, composer, type and any issues.

For example, `Tue1-Walsh-Responses.pdf` has the cleaned lookup name `Walsh-Responses`, with suggested title `Responses` and composer `Walsh`. Do not blindly split every filename at its first hyphen: unfamiliar names need editable suggestions rather than guessed authorship.

Music type maps to **forScore Genre**. Reuse the established category names, including Anthems, Canticles, Hymns, Psalms, Gloria, SanctusBenedictus, AgnusDei and Kyrie, plus the remaining categories already agreed in the project. Copy the complete existing list during implementation rather than inventing a new taxonomy. Reuse existing Composer and Genre entries where available; create missing entries when needed for the approved metadata.

Service types such as Evensong and Eucharist belong to setlist context, not permanent piece metadata.

### Reports and caller behaviour

Standalone use shows a report for the new piece, for example:

```text
Imported into forScore

Title: Responses
Composer: Walsh
Type: [selected category]
```

When called by a setlist shortcut, return the same details for one final batch report. The new-piece metadata questions still appear when needed, but the user does not have to dismiss a separate completion report for every PDF. A simple caller option can control whether the helper displays its report.

If multiple Scores could match, let the user select the intended Score or skip the piece. Never silently choose the first result or import another copy to resolve ambiguity. A skipped or failed piece must not return an unrelated Score.

## 2. V4 - Create Service

1. Accept multiple PDFs from the share sheet. If none are supplied, open the Files picker with multiple selection enabled.
2. Ask for the service date.
3. Ask for the service type, using the established service choices.
4. Run **V4 - Check or Upload** for each PDF and collect the successfully resolved Scores.
5. Show the pieces in an editable running order. Use recognised filename position numbers as the starting order where available; do not assume picker order is the musical running order.
6. Find or create the setlist using the selected date, its English abbreviated weekday and the selected service type:

   `2026-11-10 - Tue - Evensong`

   Naming format: `yyyy-MM-dd - EEE - Service type`.

7. Add the resolved Scores and show a completion report with reused/imported counts and any skipped or failed pieces.

**Proposed default for repeat runs:** reuse the setlist with that exact name and append Scores that are not already present. Preserve existing entries, their order and manual changes. If several setlists have the same name, ask which to use rather than choosing silently.

## 3. V4 - Add to Rehearsal

1. Accept multiple PDFs from the share sheet, or select them through Files.
2. Ask for the rehearsal date, defaulting to today.
3. Run **V4 - Check or Upload** for each PDF.
4. Find or create the setlist named:

   `2026-11-10 - Rehearsal`

   Naming format: `yyyy-MM-dd - Rehearsal`.

5. Append successfully resolved Scores that are not already present, preserving existing entries and order.
6. Show a completion report, including any pieces that could not be added.

Running the shortcut again later with the same date adds to the same rehearsal setlist. Handle ambiguous setlist names in the same way as the service shortcut.

## Keep implementation small

- Start with three installed shortcuts. Keep composer and Genre handling inside Check or Upload rather than introducing more installed helpers immediately.
- Use native Shortcuts and forScore actions first, reusing working filename-cleanup rules where practical.
- Select PDFs through Files or the share sheet. Nextcloud works through its Files provider; no Nextcloud API integration is required. Selected cloud files must be available for download.
- Import into forScore only when the intended Score is absent. Preserve existing annotated Scores.
- Do not add a separate archive, metadata database, saved service records, schedule configuration or overwrite mode to this release.
- The initial append policy prevents accidental duplicate entries. Deliberate repeated occurrences of the same Score within a setlist are deferred.
- Report failures clearly and add only successfully resolved Scores. If no pieces resolve, report that outcome without creating an empty setlist.

## Build order and acceptance checks

### Step 1: Check or Upload

Build and test the shared helper before either setlist creator:

- An existing annotated Score is returned without another import or metadata changes.
- A new PDF prompts for editable title/composer and a music-type selection.
- The imported Score has the approved title, Composer and Genre.
- A second run with the same PDF reuses that Score, including after its display title has changed.
- Ambiguous matches allow selection or skipping rather than an automatic duplicate import.
- The native Score can pass back to a caller and be used by a forScore action.
- Standalone use displays the piece report; batch use returns the report details.

### Step 2: Rehearsal

- The first run creates the correctly named rehearsal setlist.
- A second run with an existing piece and a new piece appends only the new entry.
- Existing annotations, setlist order and manual additions survive.

### Step 3: Service

- Date and service selection produce the correct setlist name and weekday.
- The user can review and adjust the initial running order.
- A mixed batch of existing and new pieces uses the same helper successfully.
- A repeat run follows the append policy without duplicate Scores or setlists.
- The final report clearly identifies any skipped or failed pieces.

## Evidence and remaining checks

The [existing forScore action evidence](forscore-action-evidence.md) records successful known-name and missing-name lookup tests, plus a fixture where the original lookup name still worked after renaming the displayed score. This is useful evidence, but not a complete guarantee for every filename or library.

During the first integrated build, check lookup after renaming, import return values, Composer/Genre assignment, native Score transport between shortcuts, setlist lookup and append behaviour. Resolve these in the working flow rather than expanding V4 into another broad diagnostic programme.

This plan does not change the existing V3 sources or claim that V4 has already been implemented.
