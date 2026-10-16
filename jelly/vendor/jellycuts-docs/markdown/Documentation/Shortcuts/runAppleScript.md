Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/runAppleScript.html

# Run Apple Script

macOS 12 +

## Notes

Runs the given Apple Script code. For code to run when the action is executed, you must include it inside
on run {input, parameters}
(* Your script goes here *)
return input
end run

## Syntax

~~~~text
runAppleScript(input: <#Variable (Optional)#>, script: <#String (Allows Variables)#>)
~~~~

## Example

~~~~text
runAppleScript(input: ShortcutInput, script: "log \")
~~~~
