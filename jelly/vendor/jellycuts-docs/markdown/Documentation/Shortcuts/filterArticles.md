Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/filterArticles.html

# Filter Articles

iOS 14 +

## Notes

Filters the given articles.

## Syntax

~~~~text
filterArticles(input: , filterType:  , filter: , sortBy: , order: , limit: )
~~~~

## Example

~~~~text
filterArticles(input: Articles, filterType: All, filter: {Name: .contains : NPR}, sortBy: Creation Date, order: Oldest First, limit: 5)
~~~~
