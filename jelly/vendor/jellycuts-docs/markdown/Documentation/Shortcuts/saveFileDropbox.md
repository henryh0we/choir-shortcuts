Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/saveFileDropbox.html

# Save Dropbox File

iOS 15 +

## Notes

Save a file to dropbox.

## Syntax

~~~~text
saveFileDropbox(file: <#Variable (Optional)#>, askToSave: <#Boolean (Optional)#>, path: <#String (Allows Variables) (Optional)#>, overwrite: <#Boolean (Optional)#>)
~~~~

## Example

~~~~text
saveFileDropbox(file: Ask, askToSave: false, path: "files/saves/", overwrite: false)
~~~~
