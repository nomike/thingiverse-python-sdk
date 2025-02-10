# SearchTermTypeThingsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**hits** | [**List[ThingSchema]**](ThingSchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.search_term_type_things_get200_response import SearchTermTypeThingsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTermTypeThingsGet200Response from a JSON string
search_term_type_things_get200_response_instance = SearchTermTypeThingsGet200Response.from_json(json)
# print the JSON string representation of the object
print(SearchTermTypeThingsGet200Response.to_json())

# convert the object into a dict
search_term_type_things_get200_response_dict = search_term_type_things_get200_response_instance.to_dict()
# create an instance of SearchTermTypeThingsGet200Response from a dict
search_term_type_things_get200_response_from_dict = SearchTermTypeThingsGet200Response.from_dict(search_term_type_things_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


