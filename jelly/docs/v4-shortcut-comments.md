# V4 shortcut comments

In Apple Shortcuts, paste each code block into a separate Comment action at the top of the matching shortcut, in the order shown.

## V4 - Create Service

```text
==== What this shortcut does ====

Create a forScore setlist for a choir service from several PDFs. Run this shortcut to pick files, or select PDFs in Files and choose V4 - Create Service from the Share menu. Then choose the service date and type. Choose Other to enter your own service name.

The shortcut uses V4 - Check or Upload to find or import each score. If a piece is new, you’ll be asked to confirm its title and composer and choose a music type. The shortcut then opens the setlist named for your date and service type, such as 2026-11-12 - Thu - Evensong.

If that setlist already exists, its entries stay in place. Missing scores are added in the order Files sends the PDFs, which can differ from the order you tapped them.
```

```text
==== Using the shared shortcuts ====

Add both shared shortcuts to Apple Shortcuts. V4 - Create Service uses V4 - Check or Upload to find or import the scores for your setlist.

If V4 - Create Service is missing from the Share menu, open the shortcut’s Details, turn on Show in Share Sheet and allow PDFs or Files.
```

## V4 - Check or Upload

```text
==== What this shortcut does ====

Check whether one PDF is already in your forScore library. If it’s there, the shortcut reuses that score and keeps its annotations and details. If it’s new, the shortcut asks you to confirm the title and composer and choose a music type before importing it. Leave the composer blank if it’s unknown or doesn’t apply.

When you run this shortcut on its own, it shows a report at the end. When you use V4 - Create Service, you’ll be asked about new pieces as needed and go straight to the setlist when it’s ready.
```

```text
==== How to start ====

Run V4 - Check or Upload to pick one PDF in Files, or share one PDF to it from the Share menu. To make it appear there, open this shortcut’s Details, turn on Show in Share Sheet and allow PDFs or Files. Use V4 - Create Service when you want to put several PDFs into a service setlist.
```

```text
==== How filenames are matched ====

The shortcut looks up the score using the full filename after removing .pdf, extra spaces at the ends and any recognised service prefix such as Tue1-. For example, Tue1-Walsh-Responses.pdf is looked up as Walsh-Responses. The shortcut keeps unfamiliar prefixes and details such as movements or editions. The music type menu is built in.
```

## V4 - Upload Multi

```text
==== What this shortcut does ====

Add several PDFs to your forScore library in one go. V4 - Upload Multi passes each file to V4 - Check or Upload in turn, so existing scores are reused and new pieces are imported. You’ll be asked to confirm the details of each new piece.

This is useful for preparing music for your library when you don’t need a service setlist.
```

```text
==== How to start ====

Select your PDFs in Files, tap Share and choose V4 - Upload Multi. Keep V4 - Check or Upload in Apple Shortcuts as well, because Upload Multi uses it to process each file.
```

## V4 - Open Score

```text
==== What this shortcut does ====

Open one piece of music in forScore, ready for rehearsal. V4 - Open Score uses V4 - Check or Upload to find the score in your library or import it if it’s new, then opens it in forScore. For a new piece, you’ll be asked to confirm its details first.
```

```text
==== How to start ====

Select a PDF in Files, tap Share and choose V4 - Open Score. Keep V4 - Check or Upload in Apple Shortcuts as well, because Open Score uses it to find or import the score.
```
