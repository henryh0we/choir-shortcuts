Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/createPDF.html

# Create PDF

iOS 14 +

## Notes

Creates a pdf from the provided input.

## Syntax

~~~~text
createPDF(input: <#Variable (Optional)#>, margins: <#Boolean (Optional)#>, pages: <#Enumeration (WFPDFIncludedPages) (Optional)#>, singlePageNumb: <#String (Allows Variables) (Optional)#>, pageStart: <#String (Allows Variables) (Optional)#>, pageEnd: <#String (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
createPDF(input: images, margins: true, pages: All Pages, singlePageNumb: "", pageStart: "", pageEnd: "")
~~~~
