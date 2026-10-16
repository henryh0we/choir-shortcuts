Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Language_Guide/menus.html

# Menu Statements

Menus act as a way for the user to select from different options. This directly corresponds to shortcut's Menu Action. Any code put inside a `case` statement will be executed when the user selected that case. The Array in the declaration tells the menu what cases should be recognized. If a case is not in this array, it will not be recognized.  

~~~~text
menu(<#String (Allows Variables)#>, <#Array#>) {
  case(<#String (No Variables)#>):
    <#Code#>
          
  case(<#String (No Variables)#>):
    <#Code#>
          
}
~~~~

The following is an example of a filled out menu.

~~~~text
menu("Select an action", ["Log Water", "Workout"]) {
  case("Log Water"):
    runShortcut(Log Water)
  case("Workout"):
    runShortcut(Workout)
}
~~~~
