Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Language_Guide/key.html

# Key Modifier

Isf you want to retrieve a key from a dictionary you can use the
`.key(<#Key Name#>)` syntax. This is modifier's shortcut equivalent is the "Get Value For Key" dialog when you select a dictionary value.

## Example

~~~~text
dictionary(meta) >> META
var meta = META.key(names)
~~~~

or

~~~~text
text("${Shortcut Input.as(Dictionary).key(names)"}
~~~~
