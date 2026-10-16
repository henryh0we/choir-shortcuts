Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Language_Guide/if_else.html

# If Statements

If statements in Jelly work like a lot of other languages. The following syntax is an outline of the if statement syntax.

~~~~text
//If statement with a variable
if(<#Variable#> <#Condition#> <#Variable#>) {
    <#Code#>
}
//or you can use a string
if(<#Variable#> <#Condition#> <#String (Allows Variables)#>) {
    <#Code#>
}
~~~~

The following is an example of a filled out if statement

~~~~text
if(name .contains "TestName") {
    quicklook(name)
}
~~~~

# If-Else Statements

An else statement is tacked onto the end of an if statement. Currently Jelly does not support `if else`, only simple `else` statements. Below is an example of an else statement

~~~~text
if(name .contains "TestName") {
    quicklook(name)
} else {
    exit(name)
}
~~~~

# Conditions

Condition
Shortcut Equivalent

==
Is

!=
Is not

!= nil
Has any value

== nil
Does not have any value

.contains
Contains

!contains
Does not contain

.beginsWith
Begins With

!beginsWith
Does not begin with

.endsWith
Ends with

<
Less than

<=
Less than or equal to

>
Greater than

>=
Greater than or equal to

.between numb1...numb2
Between number
