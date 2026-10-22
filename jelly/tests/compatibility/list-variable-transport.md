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

## User-confirmed Text-only source fix, 22 October 2026

The user confirms installing the interpolation probe, seeing variables inserted
in its List and receiving their Text contents rather than their names. This
establishes that the explicit interpolation form works in this isolated iPad
test. Exact installed hash/settings and a fresh full production run were not
supplied. Archive **16** now uses it in both naming Lists; Assembly **14** uses
it in its naming List. Interfaces remain 2.1 and 1.1. Matching .txt transfer
copies are synchronized. Native archiveInput transport is unchanged.

The pinned compiler's `ListParameter.swift` uses
`JellyArray<JellyVariableReference>`; its `JellyArray.swift` dispatches string
entries through `JellyString`. The user-confirmed interpolated Text form is:

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
At that attempt production sources were unchanged; no generated-file patch was
applied. The later user confirmation now supports the production source changes.

Independent device test:
[TEST - List Text Interpolation](probe-list-text-interpolation.jelly)
([transfer copy](probe-list-text-interpolation.txt)). It needs no dependencies
and ignores caller input. Expected two previews, in order:

1. `Fri4-Humfrey-InEminor.pdf`
2. `^Fri[0-9]+-`

Inspect its List entries for actual attached variable tokens. A preview of
`sourceName`, `${sourceName}` or `prefixRegex` is a failure. Device result:
**User-reported success**: List tokens and value previews confirmed. The three
production naming Lists are now updated; full caller/return paths still require
retesting. Keep the user's working archive copy during that change.

Local recheck of Archive 16 and Assembly 14 (22 October):

```powershell
python jelly/scripts/build.py jelly/shortcuts/reusable/util-archive-choir-pdf.jelly jelly/shortcuts/reusable/util-assemble-choir-service.jelly
```

Both failed the older compiler's recorded Output parameter, File Details
unnamed-parameter and brace/core-node diagnostics. No successful production
export is claimed. Exact diagnostics/source hashes are in their respective
`build/shortcuts/reusable/*.build.json` reports. Preserve the device-supported
form rather than reverting it to satisfy that older profile.

Migration: use Assembly 14 when continuing integration and inspect its naming
List. Preserve the repaired installed Archive 15; its Lists are already fixed
manually. If you choose to regenerate Archive 16, reapply CFG02-CFG04 and the
File-typed presence-condition repair, inspect named variables and rerun save/reuse
before switching callers. Existing guards and native slots remain in source.

This strategy is for Text values only. It does not establish a source fix for
native File, Folder, Dictionary or Score List entries. Preserve their native
tokens and inspect the generated sender after every regeneration.
