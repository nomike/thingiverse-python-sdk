# ThingopsIdsRemovePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **int** | Set the id of the collection from which the specified thing will be removed | 

## Example

```python
from openapi_client.models.thingops_ids_remove_post_request import ThingopsIdsRemovePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ThingopsIdsRemovePostRequest from a JSON string
thingops_ids_remove_post_request_instance = ThingopsIdsRemovePostRequest.from_json(json)
# print the JSON string representation of the object
print(ThingopsIdsRemovePostRequest.to_json())

# convert the object into a dict
thingops_ids_remove_post_request_dict = thingops_ids_remove_post_request_instance.to_dict()
# create an instance of ThingopsIdsRemovePostRequest from a dict
thingops_ids_remove_post_request_from_dict = ThingopsIdsRemovePostRequest.from_dict(thingops_ids_remove_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


