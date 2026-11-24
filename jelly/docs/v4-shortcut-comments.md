# V4 shortcut comments

In Apple Shortcuts, paste each code block into a separate **Comment** action at the top of the matching shortcut, in the order shown.

## V4 - Create Service

[Setup guide](v4-create-service.md)

### What this shortcut does

```text
Create a forScore setlist for a choir service from several PDFs. Run this shortcut to pick files, or select PDFs in Files and choose V4 - Create Service from the Share menu. Then choose the service date and type. Choose Other to enter your own service name.

The shortcut uses V4 - Check or Upload to find or import each score. If a piece is new, you’ll be asked to confirm its title and composer and choose a music type. The shortcut then opens the setlist named for your date and service type, such as 2026-11-12 - Thu - Evensong.

If that setlist already exists, its entries stay in place. Missing scores are added in the order Files sends the PDFs, which can differ from the order you tapped them.
```

### Before first use

```text
Set up V4 - Check or Upload first. Create Service needs that shortcut to send back each forScore score and its report.

To start from the Share menu, open this shortcut’s Details, turn on Show in Share Sheet and allow PDFs or Files.

If you imported a fresh copy, follow the comments marked DATE01 and SFS01 through SFS04 to add the date question and forScore setlist actions. Check that the file references are set to File. If the per-file assignment is empty, reselect Repeat Item from the loop that goes through the PDFs.
```

## V4 - Check or Upload

[Setup guide](v4-check-or-upload.md)

### What this shortcut does

```text
Check whether one PDF is already in your forScore library. If it’s there, the shortcut reuses that score and keeps its annotations and details. If it’s new, the shortcut asks you to confirm the title and composer and choose a music type before importing it. Leave the composer blank if it’s unknown or doesn’t apply.

When you run this shortcut on its own, it shows a report at the end. When Create Service calls it for a group of PDFs, you’ll still see questions about new pieces, and the shortcut sends each score and report back to Create Service in the background.
```

### How to start

```text
Run V4 - Check or Upload to pick one PDF in Files, or share one PDF to it from the Share menu. To make it appear there, open this shortcut’s Details, turn on Show in Share Sheet and allow PDFs or Files. Use V4 - Create Service when you want to put several PDFs into a service setlist.
```

### Before first use

```text
If you imported a fresh copy, add the forScore actions in Apple Shortcuts where the comments marked FS01 through FS06 show you. Set up the score lookup at FS01 first. The template stops there until that action is in place. Keep the surrounding If blocks so the import and music details questions only run for new pieces.
```

### How filenames are matched

```text
The shortcut looks up the score using the full filename after removing .pdf, extra spaces at the ends and any recognised service prefix such as Tue1-. For example, Tue1-Walsh-Responses.pdf is looked up as Walsh-Responses. The shortcut keeps unfamiliar prefixes and details such as movements or editions. The music type menu is built in.
```
