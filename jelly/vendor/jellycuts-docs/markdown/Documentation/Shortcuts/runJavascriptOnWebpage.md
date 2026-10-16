Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/runJavascriptOnWebpage.html

# Run Javascript on Webpage

iOS 14 +

## Notes

Runs the given javascript on a webpage.

## Syntax

~~~~text
runJavascriptOnWebpage(url: <#Variable (Optional)#>, javascript: <#String (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
runJavascriptOnWebpage(url: ShortcutInput, javascript: "document.body.style.backgroundColor = 'yellow'; completion();")
~~~~
