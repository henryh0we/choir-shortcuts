Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/math.html

# Math

iOS 14 +

## Notes

Solves a math equation. You can use +, -, ×, ÷, and … as operations. When using … you can apply a scientific operation type.

## Syntax

~~~~text
math(input: <#String or Number (Allows Variables)#>, operation: <#Dynamic Enum (WFMathOperation)#>, operand: <#String or Number (Allows Variables) (Optional)#>, scientific: <#Enumeration (WFScientificMathOperation) (Optional)#>)
~~~~

## Example

~~~~text
math(input: "10", operation: …, operand: "42", scientific: x^y)
~~~~
