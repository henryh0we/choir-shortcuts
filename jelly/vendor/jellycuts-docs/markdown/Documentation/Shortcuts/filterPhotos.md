Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/filterPhotos.html

# Filter Photos

iOS 14 +

## Notes

Filters the given notes. Placing All Photos in the input will allow you to filter all of your photos.

## Syntax

~~~~text
filterPhotos(input: , filterType:  , filter: , sortBy: , order: , limit: )
~~~~

## Example

~~~~text
filterPhotos(input: All Photos, filterType: All, filter: {Album: is : a-Schoolwork}, sortBy: Creation Date, order: Oldest First, limit: 20)
~~~~
