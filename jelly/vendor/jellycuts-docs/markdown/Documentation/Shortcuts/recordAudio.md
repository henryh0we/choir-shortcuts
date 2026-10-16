Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/recordAudio.html

# Record Audio

iOS 14 +

## Notes

Records audio with the given parameters.

## Syntax

~~~~text
recordAudio(quality: <#Enumeration (WFRecordingCompression) (Optional)#>, start: <#Enumeration (WFRecordingStart) (Optional)#>, end: <#Enumeration (WFRecordingEnd) (Optional)#>, duration: <#Time Interval (Optional)#>)
~~~~

## Example

~~~~text
recordAudio(quality: Normal, start: On Tap, end: After Time, duration: 10 min 15 sec)
~~~~
