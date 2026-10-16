Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/output.html

# Output

iOS 15 +

## Notes

Outputs the given input as the shortcuts result. If there is no where too output, the result behavior is used to determine what should be done with the result.

## Syntax

~~~~text
output(notes: <#String (Allows Variables)#>, folder: <#Enumeration (WFNoOutputSurfaceBehavior) (Optional)#>)
~~~~

## Example

~~~~text
output(notes: "ShortcutInput", folder: Respond)
~~~~
