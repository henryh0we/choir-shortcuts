Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/findWindows.html

# Find Windows

macOS 12 +

## Notes

Find's any windows with the specified parameters. To filter all windows, use All Windows as the input.

## Syntax

~~~~text
findWindows(input: , filterType:  , filter: , sortBy: , order: , limit: )
~~~~

## Example

~~~~text
findWindows(input: Images, filterType: All, filter: {Width: == : 1024, Height: == 1024}, sortBy: Creation Date, order: Oldest First, limit: 5)
~~~~
