Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/filterMusic.html

# Filter Music

iOS 14 +

## Notes

Filters the given music. Placing All Music in the input will allow you to filter all of your music.

## Syntax

~~~~text
filterMusic(input: , filterType:  , filter: , sortBy: , order: , limit: )
~~~~

## Example

~~~~text
filterMusic(input: All Music, filterType: All, filter: {Artist: == : AJR}, sortBy: Title, order: Ascending, limit: 20)
~~~~
