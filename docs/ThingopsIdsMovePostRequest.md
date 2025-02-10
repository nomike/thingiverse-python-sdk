# ThingopsIdsMovePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_collection_id** | **int** | Set the id of the collection where the specified thing is located | 
**target_collection_id** | **int** | Set the id of the collection where the specified thing will be moved | 

## Example

```python
from openapi_client.models.thingops_ids_move_post_request import ThingopsIdsMovePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ThingopsIdsMovePostRequest from a JSON string
thingops_ids_move_post_request_instance = ThingopsIdsMovePostRequest.from_json(json)
# print the JSON string representation of the object
print(ThingopsIdsMovePostRequest.to_json())

# convert the object into a dict
thingops_ids_move_post_request_dict = thingops_ids_move_post_request_instance.to_dict()
# create an instance of ThingopsIdsMovePostRequest from a dict
thingops_ids_move_post_request_from_dict = ThingopsIdsMovePostRequest.from_dict(thingops_ids_move_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


