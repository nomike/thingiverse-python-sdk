# SearchTermTypeMakesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**hits** | [**List[CopySchema]**](CopySchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.search_term_type_makes_get200_response import SearchTermTypeMakesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTermTypeMakesGet200Response from a JSON string
search_term_type_makes_get200_response_instance = SearchTermTypeMakesGet200Response.from_json(json)
# print the JSON string representation of the object
print(SearchTermTypeMakesGet200Response.to_json())

# convert the object into a dict
search_term_type_makes_get200_response_dict = search_term_type_makes_get200_response_instance.to_dict()
# create an instance of SearchTermTypeMakesGet200Response from a dict
search_term_type_makes_get200_response_from_dict = SearchTermTypeMakesGet200Response.from_dict(search_term_type_makes_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


