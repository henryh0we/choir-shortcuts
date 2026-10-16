Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/overlayText.html

# Overlay Text

iOS 14 +

## Notes

Overlay's Text onto an image

## Syntax

~~~~text
overlayText(image: <#Variable#>, text: <#String (Allows Variables)#>, position: <#Enumeration (WFTextPosition) (Optional)#>, xCoordinate: <#Number (Allows Variables) (Optional)#>, yCoordinate: <#Number (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
overlayText(image: Clipboard, text: "Jellycuts is awesome!", position: Custom, xCoordinate: 100, yCoordinate: 100)
~~~~
