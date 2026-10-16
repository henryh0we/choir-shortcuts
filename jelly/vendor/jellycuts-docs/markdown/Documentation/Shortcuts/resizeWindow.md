Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/resizeWindow.html

# Resize Window

macOS 12 +

## Notes

Resize the given window.

## Syntax

~~~~text
resizeWindow(window: <#Variable#>, config: <#Enumeration (WFConfiguration)#>, bringToFront: <#Boolean (Optional)#>, height: <#Number (Allows Variables) (Optional)#>, width: <#Number (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
resizeWindow(window: Found Window, config: Dimensions, bringToFront: false, height: 100, width: 100)
~~~~
