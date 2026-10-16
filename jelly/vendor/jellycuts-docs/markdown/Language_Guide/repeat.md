Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Language_Guide/repeat.html

# Repeat

Repeats are pretty straight forward. They just repeat whatever code you have in them a certain amount of times. Inside a repeat statement you can access a local variable named `repeat index`. This variable will give you the current
index of the repeat statement. To declare a repeat you use the following syntax.

~~~~text
repeat(<#Integer or Variable#>) {
    <#Code#>
}
~~~~

Below are examples of a fully constructed repeat statement

~~~~text
//Repeat with an integer
repeat(3) {
    wait(Repeat index)
}
//Repeat with a variable
repeat(seconds) {
    wait(Repeat index)
}
~~~~

# Repeat Each

`repeatEach` is equivalent to shortcuts `Repeat With Each`. This is basically a
`forEach` in other programming languages. This allows you to repeat through every item in a variable array and access each individual item as you loop through. Inside a `repeatEach` statement you have access to two local
variables `Repeat Index` and `Repeat Item`. `Repeat Index` will get the current index of the repeat each statement, and `Repeat Item` will get the current item of the repeat each statement.

Below is the syntax for a repeat statement

~~~~text
repeatEach(<#Variable#>) {
    <#Code#>
}
~~~~

Below is an example of a fully constructed repeat each statement

~~~~text
repeatEach(assignments) {
    quicklook(Repeat Item)
}
~~~~
