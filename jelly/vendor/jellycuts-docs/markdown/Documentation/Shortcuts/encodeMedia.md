Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/encodeMedia.html

# Encode Media

iOS 14 +

## Notes

Encodes the given media into a video.

## Syntax

~~~~text
encodeMedia(media: <#Variable#>, size: <#Enumeration (WFMediaSize) (Optional)#>, speed: <#Enumeration (WFMediaSpeed) (Optional)#>, customSpeed: <#String (Allows Variables) (Optional)#>, title: <#String (Allows Variables) (Optional)#>, artist: <#String (Allows Variables) (Optional)#>, album: <#String (Allows Variables) (Optional)#>, genre: <#String (Allows Variables) (Optional)#>, year: <#Number (Allows Variables) (Optional)#>, artwork: <#Variable (Optional)#>)
~~~~

## Example

~~~~text
encodeMedia(media: ShortcutInput, size: 1920x1080, speed: Normal, customSpeed: "0", title: "Awesome Video", artist: "Zachary", album: "Videos", genre: "Indie", year: 2021, artwork: Image)
~~~~
