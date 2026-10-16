# Platform evidence and assumptions

Reviewed on 2026-10-14. The examples provisionally target **iOS 26 with an English Shortcuts editor**. This is a design baseline, not a claim about the user's installed version or the latest iOS release. Select iOS 26 in Apple's guide when comparing instructions; unversioned guide links may later display a different version.

| Apple source | What it supports |
| --- | --- |
| [Use If actions](https://support.apple.com/en-gb/guide/shortcuts/apd83dcd1b51/ios) | If, Otherwise, End If; conditions depend on input type; If Result carries the output of the executed branch |
| [Use Repeat actions](https://support.apple.com/en-gb/guide/shortcuts/apdc11deb2c1/ios) | Repeat and Repeat with Each, closing markers, item/index variables, collected loop output |
| [Use variables](https://support.apple.com/en-gb/guide/shortcuts/apdd02c2780c/ios) | Magic Variables, special variables, and named variables; selecting outputs rather than typing variable names |
| [Shortcut completion](https://support.apple.com/en-gb/guide/shortcuts/apda9578f70f/ios) | Stop and Output explicitly returns content; no-recipient options include Respond and Do Nothing |
| [Run a shortcut using a URL scheme](https://support.apple.com/en-au/guide/shortcuts/apd624386f42/ios) | Apple recommends Run Shortcut for calling another Shortcut from within Shortcuts |
| [Ask for Input](https://support.apple.com/en-gb/guide/shortcuts/apd68b5c9161/ios) | Typed interactive input, selectable input type, and a pre-filled default |
| [About get actions](https://support.apple.com/en-lamr/guide/shortcuts/apd5c2bd430f/ios) | Text and other native actions supply content |
| [Limit input](https://support.apple.com/guide/shortcuts/limit-the-input-for-a-shortcut-apd8195f96d6/ios) | Input banner configuration is separate from ordinary actions; missing-input behaviour can be configured |

These sources support core semantics, not every label or layout in a specific editor build. In the examples, Editor setup identifies descriptive field locators whose exact UI labels remain to be checked. Bracketed action names are distinguished from those parameter lines. The plain-text blueprint presentation changes documentation layout, not action semantics.

Open device checks for the examples:

- Confirm `has any value` is available for Shortcut Input selected as Text, and that the missing-input branch yields Friend. If a Receive banner is present, its no-input behaviour must be Continue so that the If can handle missing input.
- Confirm the expanded no-recipient setting in Stop and Output and its exact label; select Respond for the utility and Do Nothing for the main. Confirm Respond does not add a second display when a Run Shortcut caller receives the output.
- Confirm Run Shortcut's input field and result selector on the installed version, and the action name/field for Show Result. If Show Result is unavailable, a documented Quick Look alternative can display Text; update the main's blueprint and tests before building that variant.
- Confirm Ask for Input's Text settings, Default Answer, and Allow Multiple Lines option on the installed version. Cancellation and empty submission should be tested separately; an editor may prevent submitting an empty answer.

No device/editor screenshots or execution reports were available. Both examples remain **Designed** until implementation-critical settings are confirmed; their manual tests are **Not run**. Documentation review is not execution evidence. If building on another iOS version or language, resolve labels and behaviour on that device and update the metadata and record.
