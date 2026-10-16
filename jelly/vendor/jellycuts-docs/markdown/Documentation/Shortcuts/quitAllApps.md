Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/quitAllApps.html

# Quit All Apps

macOS 12 +

## Notes

Quit's all the apps currently open. It will not quit any apps put in the exceptions array.

## Syntax

~~~~text
quitAllApps(except: <#AppArray#>, askToSave: <#Boolean (Optional)#>)
~~~~

## Example

~~~~text
quitAllApps(except: com.zlineman.jellyfish, askToSave: true)
~~~~
