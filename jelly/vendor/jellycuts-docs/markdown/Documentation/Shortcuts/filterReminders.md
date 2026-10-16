Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/filterReminders.html

# Filter Reminders

iOS 14 +

## Notes

Filters the given reminders. Placing All Reminders in the input will allow you to filter all of your reminders.

## Syntax

~~~~text
filterReminders(input: , filterType:  , filter: , sortBy: , order: , limit: )
~~~~

## Example

~~~~text
filterReminders(input: All Reminders, filterType: All, filter: {Name: == : Test}, sortBy: Creation Date, order: Oldest First, limit: 20)
~~~~
