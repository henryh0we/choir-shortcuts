Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/sendNotification.html

# Send Notification

iOS 14 +

## Notes

Sends the user a notifcation.

## Syntax

~~~~text
sendNotification(body: <#String (Allows Variables)#>, title: <#String (Allows Variables) (Optional)#>, sound: <#Boolean (Optional)#>, attachment: <#Variable (Optional)#>)
~~~~

## Example

~~~~text
sendNotification(body: "Hello World!", title: "My First Jellycut", sound: false, attachment: ShortcutInput)
~~~~
