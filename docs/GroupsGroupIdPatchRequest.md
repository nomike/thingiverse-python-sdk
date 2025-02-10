# GroupsGroupIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Replace the name of the group | [optional] 
**description** | **str** | Replace the description of the group | [optional] 
**featured_things** | **List[object]** | Replace the featured things of the group | [optional] 

## Example

```python
from openapi_client.models.groups_group_id_patch_request import GroupsGroupIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsGroupIdPatchRequest from a JSON string
groups_group_id_patch_request_instance = GroupsGroupIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(GroupsGroupIdPatchRequest.to_json())

# convert the object into a dict
groups_group_id_patch_request_dict = groups_group_id_patch_request_instance.to_dict()
# create an instance of GroupsGroupIdPatchRequest from a dict
groups_group_id_patch_request_from_dict = GroupsGroupIdPatchRequest.from_dict(groups_group_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


