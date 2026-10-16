Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Getting_Started/writing_first_script.html

# Writing Your First Script

## Downloading the iOS App

If you have not already you can get the iOS App on the App Store. When you have downloaded the App go through the tutorial inside the app to get connected to Shortcuts. 

Once you have completed that you can open "Starter Jellycut" to get started with this tutorial.

## Let's get started

This is what you will first see when you either, create a new project or open "Starter Jellycut". At the very top of the file you will see an import Statement. This important statement is importing the [Standard Shortcuts Library](https://docs.jellycuts.com/Shortcuts_Standard/index.html)            with a version of 1092.6 (What this means is covered more in the article on the Standard Shortcuts Library). The next line will be the metadata definition. This metadata tell's Jellycuts some things about the how it should export the Shortcut,
such as the Color and Icon. The full list of values for these flags can be found on the page covering [Metadata](https://docs.jellycuts.com/Language_Guide/metadata.html).

~~~~text
            
import Shortcuts
#Color: red, #Icon: shortcuts
        
~~~~

### Hello World!

Let's start off where learning always starts, the Hello World! program. In Jelly this is fairly simple, the first step is to add a text block to the script

~~~~text
            
text(text: "Hello World!")
        
~~~~

Next you want to add a [Magic Variable](https://docs.jellycuts.com/Language_Guide/magic_variables.html) to the end of this line so we can get the value out of the text block and into our display function

~~~~text
            
text(text: "Hello World!") >> introduction
        
~~~~

After that we are going to add in our display function. Currently the best way to display a short amount of text to a the user is to show it in an alert. As you can see we are using String interpolation to insert our variable into the alert text.
This is gone over more in depth in the [Strings](https://docs.jellycuts.com/Language_Guide/strings.html) article.

~~~~text
            
alert(alert: "${introduction}")
        
~~~~

Once that is all done you should have this as your final script! You can now export this out of Jellycuts into Shortcuts and run it. 

~~~~text
            
import Shortcuts
#Color: red, #Icon: shortcuts

text(text: "Hello World!") >> introduction
alert(alert: "${introduction}")
        
~~~~

## Next steps

Now that you have written your first Jellycut, you can either jump right into writing more or read the more of the documentation. To start I would recommend reading over the [Language Guide](https://docs.jellycuts.com/Language_Guide/basics.html) to find more
information about the Jelly language.
