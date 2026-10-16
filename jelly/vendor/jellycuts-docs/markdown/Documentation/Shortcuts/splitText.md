Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/splitText.html

# Split Text

iOS 14 +

## Notes

Splits the text by a separator. If the separator is set to Custom you can add a customSeparator to split by any character you want.

## Syntax

~~~~text
splitText(text: <#arrayorstring#>, separator: <#Enumeration (WFTextSeparator)#>, customSeparator: <#String (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
splitText(text: [\, separator: , \, customSeparator: "")
~~~~
