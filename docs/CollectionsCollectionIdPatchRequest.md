# CollectionsCollectionIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Name of the collection | [optional] 
**description** | **object** | Description of the collection | [optional] 
**featured_thing_id** | **object** | Featured Thing id from the collection | [optional] 

## Example

```python
from openapi_client.models.collections_collection_id_patch_request import CollectionsCollectionIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsCollectionIdPatchRequest from a JSON string
collections_collection_id_patch_request_instance = CollectionsCollectionIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionsCollectionIdPatchRequest.to_json())

# convert the object into a dict
collections_collection_id_patch_request_dict = collections_collection_id_patch_request_instance.to_dict()
# create an instance of CollectionsCollectionIdPatchRequest from a dict
collections_collection_id_patch_request_from_dict = CollectionsCollectionIdPatchRequest.from_dict(collections_collection_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


