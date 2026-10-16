Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/filterContacts.html

# Filter Contacts

iOS 14 +

## Notes

Filters the given contacts. Placing All Contacts in the input will allow you to filter all of your contacts.

## Syntax

~~~~text
filterContacts(input: , filterType:  , filter: , sortBy: , order: , limit: )
~~~~

## Example

~~~~text
filterContacts(input All Contacts, filterType: All, filter: {Name: == : Zach}, sortBy: Creation Date, order: Oldest First, limit: 5)
~~~~
