Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Language_Guide/property.html

# Property Modifier

If you want to retrieve a certain property from a variable you can use the
`.get(<#Property#>)` syntax. This will retrieve a certain aspect of a type variable. Such as a variables, name, file type, file extension etc... This is modifier's shortcut equivalent is the get menu when you tap on a
variable.

## Example

~~~~text
dictionary(meta) >> META
var meta = META.get(keys)
~~~~

or

~~~~text
text("${Shortcut Input.as(Dictionary).get(keys)"}
~~~~
