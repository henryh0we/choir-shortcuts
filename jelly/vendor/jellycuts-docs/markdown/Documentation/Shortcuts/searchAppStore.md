Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/searchAppStore.html

# Search App Store

iOS 14 +

## Notes

Searches the app store using the given parameters.

## Syntax

~~~~text
searchAppStore(input: <#String (Allows Variables)#>, by: <#Enumeration (WFAttribute) (Optional)#>, region: <#Enumeration (WFCountry) (Optional)#>, device: <#Enumeration (WFEntity) (Optional)#>, limit: <#Number (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
searchAppStore(input: "Jellycuts", by: All, region: United States, device: iPhone, limit: 1)
~~~~
