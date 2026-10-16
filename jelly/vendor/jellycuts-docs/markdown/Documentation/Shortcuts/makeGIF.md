Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/makeGIF.html

# Create GIF

iOS 14 +

## Notes

Creates a GIF from the provided input.

## Syntax

~~~~text
makeGIF(content: <#Variable (Optional)#>, frameTime: <#String (Allows Variables) (Optional)#>, loopOn: <#Boolean (Optional)#>, loopCount: <#Number (Optional)#>, autoSize: <#Boolean (Optional)#>, width: <#String (Allows Variables) (Optional)#>, height: <#String (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
makeGIF(content: images, frameTime: "1", loopOn: true, loopCount: 5, autoSize: false, width: "512", height: "512")
~~~~
