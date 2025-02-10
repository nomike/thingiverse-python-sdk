# CollectionsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Name of the collection | 
**description** | **object** | Description of the collection | [optional] 

## Example

```python
from openapi_client.models.collections_post_request import CollectionsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsPostRequest from a JSON string
collections_post_request_instance = CollectionsPostRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionsPostRequest.to_json())

# convert the object into a dict
collections_post_request_dict = collections_post_request_instance.to_dict()
# create an instance of CollectionsPostRequest from a dict
collections_post_request_from_dict = CollectionsPostRequest.from_dict(collections_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


