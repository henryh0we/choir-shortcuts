Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/imageFromPDF.html

# Make Image from PDF Page

iOS 15 +

## Notes

Make an image from a PDF, 

## Syntax

~~~~text
imageFromPDF(pdf: <#Variable (Optional)#>, format: <#Dynamic Enum (WFMakeImageFromPDFPageImageFormat) (Optional)#>, colorspace: <#Enumeration (WFMakeImageFromPDFPageColorspace) (Optional)#>, resolution: <#Number (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
imageFromPDF(pdf: ShortcutInput, format: PDF, colorspace: RGB, resolution: 300)
~~~~
