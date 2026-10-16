Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Getting_Started/language_overview.html

# Language Overview

The Jelly language was created for Siri
Shortcuts because I was not satisfied with the GUI of Shortcuts. I wanted a way to write Shortcuts in a text based language. That is why I created Jellycuts and
the Jelly language.

The Jelly language is currently focused on creating a simple way to write Shortcuts without much hassle. That is why the language is geared towards calling the Shortcuts actions as function. However in the future I plan to alter the way the language
is interpreted so you are able to write code in a Swift or Javascript like fashion and have it translated into a Shortcut or even write and compile it like any other
language.

## Editor + Diagnostics (March 14, 2026)

The March 14, 2026 update improved day-to-day editing stability in Jellycuts and Firefly, especially for long scripts and base64-heavy workflows.

- Wrap Text While Coding behavior is now more stable and wrap preference persists across reopen flows.

- When wrap is off, long lines keep predictable horizontal scrolling.

- Caret visibility in wrapped text was improved so typing position remains reachable.

- Console output was cleaned up with clearer line markers, emphasized variable names, and tap-to-jump source navigation.

- Diagnostics now carry richer position detail, including column number support.

## Getting Started

The first place to start is setting up your IDE. The current IDE for Jelly is the Jellycuts iOS App.

Once you have set up your IDE you can head over too [Writing Your First Script](https://docs.jellycuts.com/Getting_Started/writing_first_script.html) to learn how to write your first Jellycut script.
