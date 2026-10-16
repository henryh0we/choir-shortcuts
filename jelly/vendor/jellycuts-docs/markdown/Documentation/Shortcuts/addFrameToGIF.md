Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/addFrameToGIF.html

# Add Frame To GIF

iOS 14 +

## Notes

Adds the given photo to a GIF as a frame.

## Syntax

~~~~text
addFrameToGIF(photo: <#Variable#>, gif: <#Variable#>, delay: <#Number (Optional)#>, autoSize: <#Boolean (Optional)#>, width: <#Number (Allows Variables) (Optional)#>, height: <#Number (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
addFrameToGIF(photo: ShortcutInput, gif: GIF, delay: 0.25, autoSize: false, width: 500, height: 500)
~~~~
