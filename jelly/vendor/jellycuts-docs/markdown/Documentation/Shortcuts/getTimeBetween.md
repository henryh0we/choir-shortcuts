Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/getTimeBetween.html

# Get Time Between Dates

iOS 14 +

## Notes

Retrieves the time between the two dates.

## Syntax

~~~~text
getTimeBetween(first: <#Variable (Optional)#>, second: <#Variable#>, interval: <#Enumeration (WFTimeUntilUnit)#>)
~~~~

## Example

~~~~text
getTimeBetween(first: CurrentDate, second: AdjustedDate, interval: Minutes)
~~~~
