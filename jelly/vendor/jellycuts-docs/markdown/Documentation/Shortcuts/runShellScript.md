Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/runShellScript.html

# Run Shell Script

macOS 12 +

## Notes

Runs the given shell script

## Syntax

~~~~text
runShellScript(input: <#Variable (Optional)#>, script: <#String (Allows Variables)#>, shell: <#Enumeration (Shell) (Optional)#>, inputMode: <#Enumeration (InputMode) (Optional)#>)
~~~~

## Example

~~~~text
runShellScript(input: ShortcutInput, script: "echo \", shell: , inputMode: /bin/zsh)
~~~~
