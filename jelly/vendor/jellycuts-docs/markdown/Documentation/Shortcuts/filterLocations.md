Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/filterLocations.html

# Filter Locations

iOS 14 +

## Notes

Filters the given locations.

## Syntax

~~~~text
filterLocations(input: , filterType:  , filter: , sortBy: , order: , limit: )
~~~~

## Example

~~~~text
filterLocations(input: locationArray, filterType: Any, filter: {City: == : Philadelphia}, sortBy: Title, order: A to Z, limit: 20)
~~~~
