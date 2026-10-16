Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/logWorkout.html

# Log Workout

iOS 14 +

## Notes

Logs a workout to the health app.

## Syntax

~~~~text
logWorkout(type: <#Enumeration (WFWorkoutReadableActivityType)#>, date: <#Date (Optional)#>, duration: <#Time Span#>, calories: <#Measurement Quantity (Optional)#>, distance: <#Measurement Quantity (Optional)#>)
~~~~

## Example

~~~~text
logWorkout(type: Cycling, date: December 1st 2020, duration: 10 Minutes, calories: 214 cal, distance: 1 mi)
~~~~
