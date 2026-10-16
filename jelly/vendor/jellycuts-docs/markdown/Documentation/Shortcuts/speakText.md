Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/speakText.html

# Speak Text

iOS 14 +

## Notes

Speaks the given text.

## Syntax

~~~~text
speakText(text: <#String (Allows Variables)#>, wait: <#Boolean (Optional)#>, rate: <#Number (Optional)#>, pitch: <#Number (Optional)#>, language: <#Enumeration (WFSpeakTextLanguage) (Optional)#>)
~~~~

## Example

~~~~text
speakText(text: "Hello World!", wait: false, rate: 1, pitch: 1, language: en-US)
~~~~
