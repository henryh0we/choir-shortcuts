Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Language_Guide/strings.html

# Strings

Strings in Jelly are used in functions, and setting variables. To declare a String you can use the following syntax

~~~~text
"String Content"
~~~~

or you can have a multiline string

~~~~text
"""
String Content
"""
~~~~

## Variables within a string

If you want to place a variable within a string, you can use `${}` to insert the variable directly into the string.

~~~~text
"Hello ${username}"
~~~~

## Tricky things with strings

If you wish to include a " in your string you must escape it using a backslash \ . These backslashes will be automatically removed when you build the Jellycut.
