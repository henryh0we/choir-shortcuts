Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/filterAttendees.html

# Filter Attendees

iOS 14 +

## Notes

Filters the given Attendees. Attendees are people attending an event.

## Syntax

~~~~text
filterAttendees(input: , filterType:  , filter: , sortBy: , order: , limit: )
~~~~

## Example

~~~~text
filterAttendees(input: event, filterType: Any, filter: {Is Me}, sortBy: Creation Date, order: Oldest First, limit: 5)
~~~~
