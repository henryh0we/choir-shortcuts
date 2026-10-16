Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/spokenAudioFromText.html

# Make Spoken Audio from Text

iOS 15 +

## Notes

Create's spoken audio from the given text

## Syntax

~~~~text
spokenAudioFromText(text: <#String (Allows Variables)#>, language: <#Enumeration (WFSpeakTextLanguage) (Optional)#>, pitch: <#Number (Optional)#>, rate: <#Number (Optional)#>, voice: <#Enumeration (WFSpeakTextVoice) (Optional)#>)
~~~~

## Example

~~~~text
spokenAudioFromText(text: "Hello World!", language: en-US, pitch: 1.0, rate: 0.5, voice: Alex)
~~~~
