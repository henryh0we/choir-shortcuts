Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/formatDate.html

# Format Date

iOS 14 +

## Notes

Formats the given date.

## Syntax

~~~~text
formatDate(date: <#String (Allows Variables)#>, dStyle: <#Enumeration (WFDateFormatStyle) (Optional)#>, tStyle: <#Enumeration (WFTimeFormatStyle) (Optional)#>, custom: <#String (Allows Variables) (Optional)#>, isoTime: <#Boolean (Optional)#>)
~~~~

## Example

~~~~text
formatDate(date: "10/20/30", dStyle: Short, tStyle: None, custom: "", isoTime: false)
~~~~
