Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Language_Guide/importing.html

# Importing Libraries

In Jelly you can include libraries that contain function calls for other Shortcuts apps. The current list of supported lists is below

- Shortcuts

- An Otter RSS

- Actions

- Apollo

- a-Shell

- a-Shell mini

- CARROT Weather

- Data Jar

- Drafts

- Focused Work

- GizmoPack

- Jellycuts

- LinkBin

- Nudget

- Progress

- Recurrence

- Rubyist

- Scriptable

- The Wallpaper App

- Toolbox Pro

- WidgetPack

Importing a library into Jelly is super easy. Like other languages you can just place a simple import statement at the top of the file. An example of these looks like the following

~~~~text
import Shortcuts
~~~~

### Important Note

When you import a library into a Jellycut, it is available for the functions following it. So if you import a library halfway down a file it is only available after the import statement. It is recommended to just place imports at the top of a
file.
