Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/appendFile.html

# Append File

iOS 14 +

## Notes

Appends contents to the end of a file.

## Syntax

~~~~text
appendFile(input: <#String (Allows Variables)#>, path: <#String (Allows Variables)#>, newLine: <#Boolean (Optional)#>)
~~~~

## Example

~~~~text
appendFile(input: "This is a new line ${Clipboard}", path: "JellycutsHelper/Text.txt", newLine: true)
~~~~
