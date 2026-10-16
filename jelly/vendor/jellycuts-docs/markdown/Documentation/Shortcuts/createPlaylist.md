Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/createPlaylist.html

# Create Playlist

iOS 14 +

## Notes

Creates a playlist with the given music, name, author and description.

## Syntax

~~~~text
createPlaylist(name: <#String (Allows Variables)#>, music: <#Variable (Optional)#>, author: <#String (Allows Variables) (Optional)#>, description: <#String (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
createPlaylist(name: "${Name}'s Playlist", music: New Music, author: "${Name}", description: "${Name}'s favorite songs from 2021")
~~~~
