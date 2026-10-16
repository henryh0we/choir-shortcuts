Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/xCallbackURL.html

# Open X-Callback URL

iOS 14 +

## Notes

Run an x-callback URL.

## Syntax

~~~~text
xCallbackURL(url: <#String (Allows Variables)#>, custom: <#Boolean (Optional)#>, success: <#String (Allows Variables) (Optional)#>, cancel: <#String (Allows Variables) (Optional)#>, error: <#String (Allows Variables) (Optional)#>, customXSuccess: <#Boolean (Optional)#>, xSuccess: <#String (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
xCallbackURL(url: "shortcuts://x-callback-url/run-shortcut?name=Calculate%20Tip&input=text&text=24.99.", custom: true, success: "x-success", cancel: "x-cancel", error: "x-error", customXSuccess: false, xSuccess: "shortcuts://callback")
~~~~
