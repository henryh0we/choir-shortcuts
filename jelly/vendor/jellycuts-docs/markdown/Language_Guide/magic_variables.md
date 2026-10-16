Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Language_Guide/magic_variables.html

# Magic Variables

Magic variables, are use to capture the output of a function. These are not mutable variables (meaning there values can not be edited). To assign the output of a function to a variable you can use the following syntax

~~~~text
Text("Hello World!") >> HelloWorld
~~~~

You can use magic variables in the input to other functions the same as you can with regular variables.

## Generated Magic Variable Names

When Jelly creates internal magic variables automatically (for example while resolving expressions), generated names now use a compact `GMV-` prefix. You can still assign your own descriptive names with `>>` when needed.

## Magic Variable within a string

Check out the [Strings](https://docs.jellycuts.com/Language_Guide/strings.html) documentation to see how to place a magic variable into a string
