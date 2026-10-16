Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/makeDiskImage.html

# Make Disk Image

macOS 12 +

## Notes

Create's a disk image with the given parameters.

## Syntax

~~~~text
makeDiskImage(files: <#Variable (Optional)#>, name: <#String (Allows Variables)#>, encrypt: <#Boolean (Optional)#>, sizetofit: <#Boolean (Optional)#>, size: <#Measurement Quantity (Optional)#>)
~~~~

## Example

~~~~text
makeDiskImage(files: Ask, name: "New Volume", encrypt: true, sizetofit: false, size: 16 GB)
~~~~
