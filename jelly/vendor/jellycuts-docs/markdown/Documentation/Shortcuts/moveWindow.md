Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/moveWindow.html

# Move Window

macOS 12 +

## Notes

Move the given window.

## Syntax

~~~~text
moveWindow(window: <#Variable#>, bringToFront: <#Enumeration (WFPosition)#>, position: <#Enumeration (WFBringToFront) (Optional)#>, xCoordinate: <#Number (Allows Variables) (Optional)#>, yCoordinate: <#Number (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
moveWindow(window: Found Window, bringToFront: Coordinates, position: false, xCoordinate: 100, yCoordinate: 100)
~~~~
