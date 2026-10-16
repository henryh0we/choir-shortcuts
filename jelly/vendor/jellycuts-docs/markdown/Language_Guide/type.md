Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Language_Guide/type.html

# Type Casting

Since variables in Jelly have no specific type when they are declared, you will need to tell some functions how they should treat a variable. To get started add the following syntax after a variable
`.as(<#Casting Type#>)`. This will tell Jelly how it should treat the given variable.

An example of this in action, is creating a variable named `textInput` and assigning it to the Shortcut Input as text. This will create a variable that maps to the Shortcut Input casted to Text

~~~~text
var textInput = Shortcut Input.as(Text)
~~~~

## Casting Types

- AppStore

- Article

- Boolean

- Contact

- Date

- Dictionary

- Email

- File

- Image

- iMedia

- iProduct

- Location

- MapLink

- Media

- Number

- PDF

- PhoneNumber

- Photo

- Place

- RichText

- Webpage

- Text

- URL

- VCard
