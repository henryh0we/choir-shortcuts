Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/convertImage.html

# Convert Image

iOS 14 +

## Notes

Converts an image to a new format.

## Syntax

~~~~text
convertImage(image: <#Variable (Optional)#>, format: <#Enumeration (WFImageFormat)#>, metadata: <#Boolean (Optional)#>, quality: <#Number (Optional)#>)
~~~~

## Example

~~~~text
convertImage(image: Clipboard, format: JPEG, metadata: true, quality: 0.433)
~~~~
