Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Language_Guide/variables.html

# Traditional Variables

Variables in Jelly are mutable (meaning their value can be edited). When you create a variable, it can be used in the input of functions needing a variable. You can also set them to new values using the same syntax you use to set them in the first
place. To set a variable there are a few different options, `Strings`, `Numbers`,
`Magic Variables`, and `Global Variables`. 

## Variable with a String value

If you want to declare a variable with the value of a string, you can use the following syntax

~~~~text
var HelloWorld = "Hello World"
~~~~

This will automatically be converted into the following Shortcuts actions

- Text: Hello World

- Variable: Linking to the text action

### Multiline String Value

If you want your variable to have multiple lines of text (a newline character \n), you will want to use a multiline variable. These are declared with the following syntax

~~~~text
var HelloWorldLong = """
Hello World!
I have multiple lines
"""
~~~~

Notice how you use triple quotes on either side of the string you want to set.

## Variable with a Number value

If you want to declare a variable with the value of a number, you can use the following syntax

~~~~text
var MeaningOfLife = 42
~~~~

This will automatically be converted into the following Shortcuts actions

- Number: 42

- Variable: Linking to the text action

## Variable with a Magic Variable value

If you wish to convert a magic variable into a regular variable, you can set a variable to the value of a magic variable. Since magic variables are not mutable, this is how you will want to mutate the value you get in return of a function. To
do this you can use the following syntax

~~~~text
var MyVariable = FunctionOutput
~~~~

## Variable with a Global Variable value

Just like magic variables, global variables are not mutable. To edit them you will need to set a variable to the global variable. This can be done with the following syntax

~~~~text
var MutableGlobalVar = Shortcut Input
~~~~

## Variable within a string

Check out the [Strings](https://docs.jellycuts.com/Language_Guide/strings.html) documentation to see how to place a variable into a string

# Assigning data to a variable

## Assignment after initialization

If you want to assign data to a variable, after it's initialization you can use the following syntax

~~~~text
// Initial Value
var x = Shortcut Input

// New Value
x = "Hello World!"
// or
var x = "Hello World!"
~~~~

## Addition after initialization

If you want to add an item to a variable, you can use the following syntax

~~~~text
// Initial Value
var x = Shortcut Input

// New Value
x += "Hello World!"
// or
var x += "Hello World!"
~~~~

This will turn the variable into an array, just like the shortcuts add to variable action.

## Expression Assignments

Variable assignments also support expression right-hand sides. This includes list literals, function calls, binary math, and index lookups.

~~~~text
var adjectives = ["Quick", "Happy", "Bright"]
var randomIndex = randomInteger(min: 0, max: lengthOfList(adjectives) - 1)
var selected = adjectives[randomIndex]
var emphasis = randomIndex + 2
~~~~

These expression forms now resolve without being misclassified as deprecated variable names.
