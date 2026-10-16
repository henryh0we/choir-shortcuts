Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/setVoiceData.html

# Set Voice Data

iOS 14 +

## Notes

Set's the devices cellular data settings. Can be used to change the current sim, and cell mode (4G, LTE, 5G).

## Syntax

~~~~text
setVoiceData(mode: <#Enumeration (ratMode)#>, sim: <#String (Optional)#>)
~~~~

## Example

~~~~text
setVoiceData(mode: 4G, sim: "Primary")
~~~~
