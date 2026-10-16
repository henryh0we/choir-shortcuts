Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/cropImage.html

# Crop Image

iOS 14 +

## Notes

Crops an Image to the specified parameters.

## Syntax

~~~~text
cropImage(image: <#Variable (Optional)#>, position: <#Enumeration (WFImageCropPosition) (Optional)#>, height: <#Number (Allows Variables)#>, width: <#Number (Allows Variables)#>, x: <#Number (Allows Variables) (Optional)#>, y: <#Number (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
cropImage(image: ShortcutInput, position: Center, height: 128, width: 128, x: , y: )
~~~~
