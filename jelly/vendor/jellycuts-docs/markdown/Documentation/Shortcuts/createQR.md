Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/createQR.html

# Create QR Code

iOS 14 +

## Notes

Creates a QR for the given text.

## Syntax

~~~~text
createQR(text: <#String (Allows Variables)#>, correction: <#Enumeration (WFQRErrorCorrectionLevel) (Optional)#>)
~~~~

## Example

~~~~text
createQR(text: "https://www.youtube.com/watch?v=dQw4w9WgXcQ", correction: Medium)
~~~~
