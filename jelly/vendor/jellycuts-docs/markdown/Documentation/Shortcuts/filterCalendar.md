Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/filterCalendar.html

# Filter Calendar Events

iOS 14 +

## Notes

Filters the given events. Placing All Events in the input will allow you to filter all of your calendar events.

## Syntax

~~~~text
filterCalendar(input: , filterType:  , filter: , sortBy: , order: , limit: )
~~~~

## Example

~~~~text
filterCalendar(input: All Events, filterType: All, filter: {Name: == : Test}, sortBy: Creation Date, order: Oldest First, limit: 20)
~~~~
