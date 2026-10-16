Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/getFile.html

# Get File

iOS 14 +

## Notes

Retrieves the file at a given path. It can also open a document picker if there is no path provided and the picker parameter is set to true.

## Syntax

~~~~text
getFile(picker: <#Boolean (Optional)#>, path: <#String (Allows Variables) (Optional)#>, error: <#Boolean (Optional)#>, multiple: <#Boolean (Optional)#>)
~~~~

## Example

~~~~text
getFile(picker: true, path: "", error: false, multiple: false)
~~~~
