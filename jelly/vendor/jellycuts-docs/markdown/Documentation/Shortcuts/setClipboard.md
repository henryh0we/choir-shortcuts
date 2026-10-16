Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/setClipboard.html

# Set Clipboard

iOS 14 +

## Notes

Sets the devices clipboard to the input.

## Syntax

~~~~text
setClipboard(variable: <#Variable (Optional)#>, local: <#Boolean (Optional)#>, expiration: <#Date (Optional)#>)
~~~~

## Example

~~~~text
setClipboard(variable: ShortcutInput, local: false, expiration: 3:00pm)
~~~~
