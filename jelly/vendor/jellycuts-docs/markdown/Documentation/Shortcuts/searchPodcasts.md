Source: https://github.com/Jellycuts/docs.jellycuts.com/blob/19306be1dd30c20e12058ebe144dd8342e64ca39/Documentation/Shortcuts/searchPodcasts.html

# Search Podcasts

iOS 14 +

## Notes

Search Apple Podcasts based on the given search terms.

## Syntax

~~~~text
searchPodcasts(query: <#String (Allows Variables)#>, by: <#Enumeration (WFAttribute) (Optional)#>, results: <#Enumeration (WFEntity) (Optional)#>, country: <#Enumeration (WFCountry) (Optional)#>, items: <#Number (Allows Variables) (Optional)#>)
~~~~

## Example

~~~~text
searchPodcasts(query: "ATP", by: All, results: iPhone, country: United States, items: 1)
~~~~
