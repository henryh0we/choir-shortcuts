Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/askForInput.html

# Ask for Input

iOS 14 +

## Notes

Asks the user for input.

## Syntax

~~~~text
askForInput(prompt: <#String (Allows Variables) (Optional)#>, type: <#Enumeration (WFInputType)#>, default: <#Dynamic Enum (WFAskActionDefaultAnswer) (Optional)#>, allowDecimal: <#Boolean (Optional)#>, allowNegative: <#Boolean (Optional)#>)
~~~~

## Example

~~~~text
askForInput(prompt: "How old are you?", type: Number, default: 12, allowDecimal: true, allowNegative: false)
~~~~
