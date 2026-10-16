Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/adjustDate.html

# Adjust Date

iOS 14 +

## Notes

Adjusts the given date by adding or subtracting the given duration. If you use any get operation you do not need a duration.

## Syntax

~~~~text
adjustDate(operation: <#Enumeration (WFAdjustOperation)#>, duration: <#Time Span (Optional)#>, date: <#String (Allows Variables)#>)
~~~~

## Example

~~~~text
adjustDate(operation: Add, duration: 10 min, date: "10:30 pm")
~~~~
