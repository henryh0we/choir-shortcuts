Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/encodeAudio.html

# Encode Audio

iOS 14 +

## Notes

Encodes the given audio.

## Syntax

~~~~text
encodeAudio(media: <#Variable#>, format: <#Enumeration (WFMediaAudioFormat) (Optional)#>, speed: <#Enumeration (WFMediaSpeed) (Optional)#>, customSpeed: <#String (Allows Variables) (Optional)#>, title: <#String (Allows Variables) (Optional)#>, artist: <#String (Allows Variables) (Optional)#>, album: <#String (Allows Variables) (Optional)#>, genre: <#String (Allows Variables) (Optional)#>, year: <#Number (Allows Variables) (Optional)#>, artwork: <#Variable (Optional)#>)
~~~~

## Example

~~~~text
encodeAudio(media: ShortcutInput, format: M4A, speed: Normal, customSpeed: "0", title: "Awesome Audio", artist: "Zachary", album: "Music", genre: "Indie", year: 2021, artwork: Image)
~~~~
