# Copyover clipboard compiler helper

## Current evidence

7 November 2026: the user reports Windows/iPad clipboard transfer, all helper
popups and generated shortcut creation working. G2A executes with only `0`, not
the expected Count 3 then A, B, A. See [the result record](../tests/ipad-investigation/generation-groups-results.md).
Follow-up on 7 November: the user confirms the name-first G2A fixture's automatic
name extraction/default naming works as intended. G2A still outputs only `0`;
this confirms naming for that attempt, not correct collection generation or the
untested legacy-header, malformed-header, cancellation and name-edit cases below.
No working production shortcut needs regeneration.

## Source header convention

For all new source, generated Jellycuts code/paste snippets and source revised for
delivery, use one physical first comment line, with no preceding blank line:

```text
// TEST - G2A Append Text | Purpose/role: ... | Contract: ... | Dependencies: None.
import Shortcuts
```

The name is everything after the initial `//` and before the first `|`, with
surrounding whitespace removed. A name-only first comment is also accepted.
Do not use `|` within the intended name. Keep the complete contract metadata;
only the copy used for naming is cleaned. Do not add a second header comment to
a single-comment experiment. This convention does not set a compiler directive.

The current G2A fixture uses this format. Historical fixtures may still start
`// Installed name: TEST - ... | ...`; the extraction below also accepts that
label without modifying the original source. Original multi-comment evidence
and working production sources are not automatically migrated.

## Update the installed helper

1. Duplicate **TEST - Receive and Compile Jelly** as a backup. Edit the active
   helper only after the backup exists. Keep its working Receive PC, text capture,
   preview, compilation and export/install actions.
2. Find the named **sourceText** captured from Get Clipboard -> Get Text from
   Input. Keep this full Text unchanged. Keep the empty-source guard and preview.
3. Insert the actions below after the preview and before the existing Ask for
   Input for the shortcut name. All named inputs below mean selected variable
   tokens, not typed variable-name strings.

### Read the first comment

1. **Split Text**: input = named **sourceText**; separator = **New Lines**.
2. **Get Item from List**: select **First Item**; List = that Split Text output.
3. **Set Variable**: **firstHeaderLine** = that First Item.
4. **Match Text**: input = named **firstHeaderLine**; pattern exactly:

   ```regex
   ^\uFEFF?[ \t]*//
   ```

   This checks the first line starts with a line comment, allowing indentation
   and an optional UTF-8 BOM character. It is a header check, not source validation.
5. **Count**: count **Items** in the Match Text output, explicitly selected.
6. **If** that Count **is 0**: **Show Alert** `Missing name comment` with message
   `Start the source with // Desired Shortcut Name | other information`, then
   **Stop This Shortcut**, both inside the If. Leave Otherwise empty.

### Extract only the name

7. **Split Text**: input = named **firstHeaderLine**; separator = **Custom**;
   custom separator = literal `|` (one vertical bar).
8. **Get Item from List**: **First Item**, List = this second Split Text output.
9. **Replace Text**: input = that First Item; find exactly:

   ```regex
   ^\uFEFF?[ \t]*//[ \t]*(?:Installed name:[ \t]*)?
   ```

   Replace with an empty field; enable **Regular Expression**. This removes the
   comment prefix and, for older headers, the optional `Installed name:` label.
10. **Replace Text**: input = the preceding Replace Text output; find exactly:

    ```regex
    ^\s+|\s+$
    ```

    Replace with an empty field; enable **Regular Expression**. This trims the
    extracted name only; it must not receive or replace full sourceText.
11. **Set Variable**: **suggestedShortcutName** = the second Replace Text output.
12. **If** suggestedShortcutName **does not have any value**: **Show Alert**
    `Empty shortcut name`, then **Stop This Shortcut**, both inside the If.

### Set the editable default

13. Open the existing **Ask for Input** for the name. Keep input type **Text**
    and its existing prompt. Expand its options and find **Default Answer**.
14. Delete the fixed `TEST - Copyover Jelly` default. Insert the named
    **suggestedShortcutName** variable token there. Do not type its name as text.
15. Keep **Set Variable intendedShortcutName = Provided Input** immediately
    afterwards, and keep the empty-name guard and final Cancel/OK confirmation.
16. In **Compile Jelly Text**, source = original **sourceText**; the existing
    naming field where supported = **intendedShortcutName**, the user's final
    answer. Do not wire suggestedShortcutName directly if edits should be honoured.
17. Keep the existing compilation settings and export/install flow. If there is
    no naming field in this route, use the existing downstream naming action or
    manually rename only the newly generated test shortcut. Do not invent a field.

Apple documents the editable default for [Ask for Input](https://support.apple.com/en-hk/guide/shortcuts/apd68b5c9161/ios).
This guide uses native Shortcuts actions; it does not claim equivalent Jelly
bindings for all helper actions or automate edits to the installed helper.

## Check wiring before the first run

| Consumer | Explicit input |
| --- | --- |
| First Split Text | Complete sourceText |
| Match Text | firstHeaderLine |
| Second Split Text | firstHeaderLine |
| First Replace Text | First Item before the header's first pipe |
| Second Replace Text | First Replace Text output |
| Ask for Input Default Answer | suggestedShortcutName token |
| intendedShortcutName | Ask for Input answer |
| Compile Jelly Text source | Complete original sourceText |
| Existing compiler/name action | intendedShortcutName |

## Device acceptance

1. Copy the complete current G2A fixture from Windows and run the helper.
2. Preview must still include the whole first comment, metadata and all code.
3. Name prompt should already show **TEST - G2A Append Text**, with no `//`,
   `Installed name:` or pipe-separated metadata. Cancel this first attempt if
   the default is wrong. Do not type a correct name and call default extraction passed.
4. On another run, edit the default to a distinct TEST name; verify that final
   chosen name reaches the generated shortcut. Preserve existing installed tests.
5. A name-only comment should work. A legacy labelled header should work.
   An empty name or missing first comment must stop before compilation. These
   extraction-only checks can be cancelled at the name prompt without building.
6. Cancelling the final confirmation must not compile. A Receive PC network
   failure must not be mistaken for a fresh source transfer; preview remains
   necessary because this helper has no build ID, hash or freshness verification.

Record actual default, final chosen and installed names, whether full source
arrived, generated action inspection and runtime separately. G2A returning `0`
does not invalidate extraction if the correct name and full source were used;
it also does not establish whether collection generation or wiring caused zero.
