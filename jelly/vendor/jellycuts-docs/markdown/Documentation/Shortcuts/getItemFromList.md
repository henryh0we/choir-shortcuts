Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/getItemFromList.html

# Get Item From List

iOS 14 +

## Notes

Gets an item from the given list. If you choose to get items in range you can use the startIndex and endIndex to define the range, you do not need to give it an index.

## Syntax

~~~~text
getItemFromList(list: <#Variable (Optional)#>, type: <#Enumeration (WFItemSpecifier)#>, index: <#String (Optional)#>, startIndex: <#String (Optional)#>, endIndex: <#String (Optional)#>)
~~~~

## Example

~~~~text
getItemFromList(list: options, type: Item at Index, index: "3", startIndex: "", endIndex: "")
~~~~
