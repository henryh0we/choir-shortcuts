Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/runSSH.html

# Run Script Over SSH

iOS 14 +

## Notes

Runs the given script over an SSH connection.

## Syntax

~~~~text
runSSH(host: <#String (Allows Variables)#>, port: <#String (Allows Variables)#>, user: <#String (Allows Variables)#>, auth: <#Enumeration (WFSSHAuthenticationType)#>, password: <#String (Allows Variables) (Optional)#>, input: <#Variable (Optional)#>, script: <#String (Allows Variables)#>)
~~~~

## Example

~~~~text
runSSH(host: "pi_address", port: "22", user: "raspberry", auth: password, password: "••••••••", input: ShortcutInput, script: "Clipboard")
~~~~
