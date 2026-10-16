Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/overlayImage.html

# Overlay Image

iOS 14 +

## Notes

Overlays one image onto another image.

## Syntax

~~~~text
overlayImage(image1: <#Variable#>, image2: <#Variable (Optional)#>, editor: <#Boolean (Optional)#>, height: <#String (Allows Variables) (Optional)#>, width: <#String (Allows Variables) (Optional)#>, position: <#Enumeration (WFImagePosition) (Optional)#>, opacity: <#String (Allows Variables) (Optional)#>, rotation: <#String (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
overlayImage(image1: Profile Image, image2: Background, editor: false, height: "512", width: "512", position: Center, opacity: "1.0", rotation: "180")
~~~~
