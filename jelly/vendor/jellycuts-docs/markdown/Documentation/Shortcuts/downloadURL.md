Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/downloadURL.html

# Get Contents of URL

iOS 14 +

## Notes

Downloads the contents at the given URL. When making a form or JSON request, use the request JSON parameter. The JSON form does not except variables, it must be written in JSON or using the dictionary builder. When using a file request type, use the request variable parameter.

## Syntax

~~~~text
downloadURL(url: <#String (Allows Variables)#>, method: <#Enumeration (WFHTTPMethod) (Optional)#>, headers: <#Dictionary (Optional)#>, requestType: <#Enumeration (WFHTTPBodyType) (Optional)#>, requestJSON: <#Dictionary (Optional)#>, requestVar: <#Variable (Optional)#>)
~~~~

## Example

~~~~text
downloadURL(url: "https://jellycuts.com", method: POST, headers: {}, requestType: Json, requestJSON: {\, requestVar: : \)
~~~~
