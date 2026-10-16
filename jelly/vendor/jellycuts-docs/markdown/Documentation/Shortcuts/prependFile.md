Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/prependFile.html

# Prepend File

iOS 14 +

## Notes

Prepends contents to the file.

## Syntax

~~~~text
prependFile(input: <#String (Allows Variables)#>, path: <#String (Allows Variables)#>, newLine: <#Boolean (Optional)#>)
~~~~

## Example

~~~~text
prependFile(input: "This is a new line ${Clipboard}", path: "JellycutsHelper/Text.txt", newLine: true)
~~~~
