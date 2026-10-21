# Variable values in Lists

## Confirmed app issue and manual repair

The user confirms that Archive 15's naming-input List passed the literal variable
names instead of their values. Replacing entries with actual native variable
tokens fixed the naming call. They now report the archive returns an existing
File when present, otherwise prompts for its category and saves it. This applies
to the manually repaired installed copy; regeneration from source does not
preserve those edits. Full archive invalid-input and whole-service tests remain
separate.

Before using an exported caller, inspect each dynamic List entry. Bare
`list(items: [sourceName, prefixRegex])` is not dependable on the recorded app
profile. In Apple Shortcuts use Select Variable to insert the producing outputs.
Do this for both naming Lists in Archive and the naming List in Assembly.

Assembly's archiveInput List must also contain native tokens: this iteration's
PDF Repeat Item, the resolved Library Folder and the parsed config Dictionary.
Do not type their names or interpolate them into Text. The successful receiver
probe does not prove a generated sender List has preserved native entries.

## Text-only source candidate

The pinned compiler's `ListParameter.swift` uses
`JellyArray<JellyVariableReference>`; its `JellyArray.swift` dispatches string
entries through `JellyString`. Explicit interpolated Text entries are therefore
a source-backed candidate:

```jelly
list(items: ["${sourceName}", "${prefixRegex}"]) >> namingInput
```

Local attempt, 22 October 2026, Open-Jellycore e1ec31c / Swift 6.4.1:

```powershell
python jelly/scripts/build.py jelly/tests/compatibility/probe-list-text-interpolation.jelly
```

The CLI accepted the source with two brace/core-node warnings, but the wrapper
rejected its export: `Text attachment {960, 1} is outside its UTF-16 string`.
This is the recorded local interpolation defect, not a successful export.
Exact diagnostics/source hash: `build/tests/compatibility/probe-list-text-interpolation.build.json`.
Production sources remain unchanged; no generated-file patch was applied.

This candidate has not passed on the iPad. Test the independent
[TEST - List Text Interpolation](probe-list-text-interpolation.jelly)
([transfer copy](probe-list-text-interpolation.txt)). It needs no dependencies
and ignores caller input. Expected two previews, in order:

1. `Fri4-Humfrey-InEminor.pdf`
2. `^Fri[0-9]+-`

Inspect its List entries for actual attached variable tokens. A preview of
`sourceName`, `${sourceName}` or `prefixRegex` is a failure. Device result:
**Not run**. Only after this passes should the three production naming Lists be
updated and their caller/return paths retested. Keep the user's working archive
copy during that change.

This strategy is for Text values only. It does not establish a source fix for
native File, Folder, Dictionary or Score List entries. Preserve their native
tokens and inspect the generated sender after every regeneration.
