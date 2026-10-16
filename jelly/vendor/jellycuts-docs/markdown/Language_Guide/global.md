Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Language_Guide/global.html

# Global Variables

Global variables, like magic variables are not mutable. These variables are available anywhere in a shortcut, and are used like any other variable that you would normally declare. They can be used within text, by using the
`${}` syntax just like any other variable.

## Available Global Variables

- Shortcut Input

- Clipboard

- Current Date

- Ask

## Shortcut Input

Shortcut input can be used to retrieve whatever input was sent into the Shortcut. Shortcut input can be any of the following

- App Store Apps

- Articles

- Contacts

- Dates

- Email Addresses

- Files

- Images

- iTunes Products

- Locations

- Map Links

- Media

- PDFs

- Phone Numbers

- Rich Text

- Safari Web Pages

- Text

- URLs

### Usage

~~~~text
//Inside Text
Text("Hello ${Shortcut Input}")

//Assiging a variable to the shortcut input
var input = Shortcut Input
~~~~

## Clipboard

This global variable will get the current item in the clipboard.

### Usage

~~~~text
//Inside Text
Text("Hello ${Clipboard}")

//Assiging a variable to the current clipboard
var clippy = Clipboard
~~~~

## Current Date

This global variable will get the current date.

### Usage

~~~~text
//Inside Text
Text("Hello ${Current Date}")

//Assiging a variable to the current Current Date
var bestDayEver = Current Date
~~~~

## Ask

This variable will tell shortcuts that it needs to ask the user for the value it should represent. So if you wanted to ask the user their name to say hello, you could put ask into a string with the text hello in front of it. 

### Usage

~~~~text
//Ask the user there name
Text("Hello ${Ask}")

//Assiging a variable to a varaible the user should input
var bestDayEver = Ask
~~~~

## Global Variables within a string

Check out the [Strings](https://docs.jellycuts.com/Language_Guide/strings.html) documentation to see how to place a global variable into a string
