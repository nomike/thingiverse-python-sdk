# GroupForum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**thumbnail** | **str** |  | [optional] 
**topic_count** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.group_forum import GroupForum

# TODO update the JSON string below
json = "{}"
# create an instance of GroupForum from a JSON string
group_forum_instance = GroupForum.from_json(json)
# print the JSON string representation of the object
print(GroupForum.to_json())

# convert the object into a dict
group_forum_dict = group_forum_instance.to_dict()
# create an instance of GroupForum from a dict
group_forum_from_dict = GroupForum.from_dict(group_forum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


