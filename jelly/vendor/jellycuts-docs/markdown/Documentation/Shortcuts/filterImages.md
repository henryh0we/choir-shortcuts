Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/filterImages.html

# Filter Images

iOS 14 +

## Notes

Filters the given images.

## Syntax

~~~~text
filterImages(input: , filterType:  , filter: , sortBy: , order: , limit: )
~~~~

## Example

~~~~text
filterImages(input: Images, filterType: All, filter: {Width: == : 1024, Height: == 1024}, sortBy: Creation Date, order: Oldest First, limit: 5)
~~~~
