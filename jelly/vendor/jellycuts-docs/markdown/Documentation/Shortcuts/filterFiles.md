Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/filterFiles.html

# Filter File

iOS 14 +

## Notes

Filters the given files.

## Syntax

~~~~text
filterFiles(input: , filterType:  , filter: , sortBy: , order: , limit: )
~~~~

## Example

~~~~text
filterFiles(input: Files, filterType: All, filter: {Name: == :Meta}, sortBy: Creation Date, order: Oldest First, limit: 5)
~~~~
