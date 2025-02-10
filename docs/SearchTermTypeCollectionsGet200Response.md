# SearchTermTypeCollectionsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**hits** | [**List[CollectionSchema]**](CollectionSchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.search_term_type_collections_get200_response import SearchTermTypeCollectionsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTermTypeCollectionsGet200Response from a JSON string
search_term_type_collections_get200_response_instance = SearchTermTypeCollectionsGet200Response.from_json(json)
# print the JSON string representation of the object
print(SearchTermTypeCollectionsGet200Response.to_json())

# convert the object into a dict
search_term_type_collections_get200_response_dict = search_term_type_collections_get200_response_instance.to_dict()
# create an instance of SearchTermTypeCollectionsGet200Response from a dict
search_term_type_collections_get200_response_from_dict = SearchTermTypeCollectionsGet200Response.from_dict(search_term_type_collections_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


