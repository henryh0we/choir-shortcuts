Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/saveFile.html

# Save File

iOS 14 +

## Notes

Saves a file to a certain path. Can also show a save prompt if ask is true.

## Syntax

~~~~text
saveFile(input: <#Variable (Optional)#>, ask: <#Boolean (Optional)#>, path: <#String (Allows Variables) (Optional)#>, overwrite: <#Boolean (Optional)#>)
~~~~

## Example

~~~~text
saveFile(input: ShortcutInput, ask: false, path: "JellycutsHelper/${ShortcutInput}.txt", overwrite: true)
~~~~
