Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/replaceText.html

# Replace Text

iOS 14 +

## Notes

Replaces text based on the parameters.

## Syntax

~~~~text
replaceText(input: <#String (Allows Variables)#>, find: <#String (Allows Variables)#>, replace: <#String (Allows Variables)#>, isRegex: <#Boolean (Optional)#>, caseSensitive: <#Boolean (Optional)#>)
~~~~

## Example

~~~~text
replaceText(input: "Hello World!", find: "Hello", replace: "Hey", isRegex: false, caseSensitive: true)
~~~~
