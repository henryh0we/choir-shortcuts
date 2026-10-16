Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/searchItunes.html

# Search iTunes

iOS 14 +

## Notes

Searches iTunes based of the parameters you provide..

## Syntax

~~~~text
searchItunes(query: <#String (Allows Variables)#>, category: <#Enumeration (WFMediaType) (Optional)#>, by: <#Enumeration (WFAttribute) (Optional)#>, results: <#Enumeration (WFEntity) (Optional)#>, count: <#Number (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
searchItunes(query: "Rick Astley", category: Music, by: All, results: Songs, count: 5)
~~~~
