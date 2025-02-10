# GrouptopicsGrouptopicIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Set the name of group topic | 
**body** | **str** | Set the body of group topic | 

## Example

```python
from openapi_client.models.grouptopics_grouptopic_id_patch_request import GrouptopicsGrouptopicIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GrouptopicsGrouptopicIdPatchRequest from a JSON string
grouptopics_grouptopic_id_patch_request_instance = GrouptopicsGrouptopicIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(GrouptopicsGrouptopicIdPatchRequest.to_json())

# convert the object into a dict
grouptopics_grouptopic_id_patch_request_dict = grouptopics_grouptopic_id_patch_request_instance.to_dict()
# create an instance of GrouptopicsGrouptopicIdPatchRequest from a dict
grouptopics_grouptopic_id_patch_request_from_dict = GrouptopicsGrouptopicIdPatchRequest.from_dict(grouptopics_grouptopic_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


