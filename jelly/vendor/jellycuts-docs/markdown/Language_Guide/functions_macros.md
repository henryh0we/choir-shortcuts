Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Language_Guide/functions_macros.html

# Functions & Macros

Functions and Macros are close to each other but not the same. There is one big difference between the two. A macro will copy the code inside it to wherever you call it. And a function will create a call to the code that is inside it. The rest of this page will dive into how the two differ, along with how they are represented inside shortcuts.

#### Important Note

Both functions & macros must be defined before they are called. You can not call a function before it has been defined. For example:

~~~~text
// This is valid
func test() { }
test()
~~~~

~~~~text
// This is not valid
test()
func test() { }
~~~~

### Typed Parameters

Functions and macros can use typed parameter hints in the form `name: type`. Supported hints include `str`, `int`, `bool`, `list`, `dict`, `date`, and `any`.

~~~~text
func echo(value: str) {
    return value
}

var output = echo(value: "Hello")
~~~~

### Returning Expressions

Return statements now resolve expression right-hand sides directly, including math, function calls, list literals, and list indexing.

~~~~text
func add40(input: int) {
    return input + 40
}

func pickItem(items: list, index: int) {
    return items[index]
}
~~~~

## Functions

In the following code, we create a function called `lookAt` which takes the parameter input. Inside the function, you are able to use the input parameter as a mutable variable, however it will not mutate the variable you pass when the function as called. This is because on a function call, the parameter values are copied, not referenced.

~~~~text
// Function in Jelly
func lookAt(input) {
    quicklook(input: input)
    var x = 42
}
        
lookAt(Shortcut Input)
~~~~

The below section is what the above code will produce in Shortcuts. As you can see, the function makes a call to the current shortcut that it is running in, with a dictionary that instructs the shortcut on what part of the shortcut it should run. This allows for function variables to be completely separate from the rest of your shortcuts variables.

~~~~text
// Transcribed Shortcuts Actions
IF Shortcut Input AS Dictionary WITH Key FUNCTION_CALL_NAME IS lookAt {
    // Your function code
    var input = Shortcut Input AS Dictionary WITH Key input
    QUICKLOOK input
} else {
    // Your unction Call
    DICTIONARY dictionary = {"FUNCTION_CALL_NAME": "lookAt", input: Shortcut Input}
    RUNSHORTCUT shortcut_name WITH dictionary
}
~~~~

### Returning data from functions

If you want to return data out of a function, it is a two-step process. First, you must include a `return` statement inside your function. Next, you need to add a magic variable to the end of the function call. 

A quick example of this:

~~~~text
func add40(input) {
    calculate("${input} + 40") >> hold
    return hold
}

var almostMeaningOfLife = 2
add40(almostMeaningOfLife) >> meaningOfLife
quicklook(meaningOfLife)
~~~~

In this example we have a function, `add40` which takes in our input and adds 40 to it. Then we return this newly calculated value by using the `return` statement followed by our variable name. To extract the variable output from the function, we use the `>>` operator followed by the new magic variable name.

## Macros

In the following code, we will replicate the function `lookAt` that we created above, but this time we are going to define it as a macro. Defining it as a macro means that we will now be copying the code from inside the macro to where we call it. 

~~~~text
// Macro in Jelly
macro lookAt(input) {
    quicklook(input: input)
}
        
lookAt(Shortcut Input)
~~~~

The shortcuts actions that are created are much shorter now because there is no need for restructuring. The code is simply copied from inside the macro to where it is called, and a variable is created to represent the parameters.

~~~~text
// Transcribed Shortcuts Actions
var input = Shortcut Input
QUICKLOOK input
~~~~

Because of the nature of macros, it is possible to edit variables that have been created before the macro is called, inside the macro. This can look like the following:

~~~~text
var x = Current Date
        
macro lookAt(input) {
    x = Current Date
    quicklook(input: input)
    y = Current Date
}

    var y = Current Date
        
    lookAt(input: Shortcut Input)
~~~~

### Returning data from macros

Returning data from a macro is exactly the same as a function. It is also a two-step process that starts with including a `return` statement in the macro, followed by adding a magic variable to the macro call.

A quick example of this:

~~~~text
macro subtract40(input) {
    calculate("${input} + 40") >> hold
    return hold
}
        
var almostMeaningOfLife = 82
subtract40(almostMeaningOfLife) >> meaningOfLife
quicklook(meaningOfLife)
~~~~

In this example we have a macro, `subtract40` which takes in our input and subtracts 40 from it. Then we return this newly calculated value by using the `return` statement followed by our variable name. To extract the variable output from the macro, we use the `>>` operator followed by the new magic variable name.
