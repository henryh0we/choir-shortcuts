Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/getMatchGroup.html

# Get Match Group

iOS 14 +

## Notes

Gets the a certain group in a regex match.

## Syntax

~~~~text
getMatchGroup(type: <#Enumeration (WFGetGroupType)#>, matches: <#Variable#>, index: <#String (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
getMatchGroup(type: Group At Index, matches: ShortcutInput, index: "2")
~~~~
