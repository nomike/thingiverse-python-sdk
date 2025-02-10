# Group


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**creator** | **int** |  | [optional] 
**is_member** | **bool** |  | [optional] 
**members** | [**GroupMembers**](GroupMembers.md) |  | [optional] 
**things** | [**GroupMembers**](GroupMembers.md) |  | [optional] 
**group_topics** | [**GroupMembers**](GroupMembers.md) |  | [optional] 
**featured** | [**List[GroupFeaturedInner]**](GroupFeaturedInner.md) |  | [optional] 
**featured_images** | [**List[GroupFeaturedImagesInner]**](GroupFeaturedImagesInner.md) |  | [optional] 
**pinned_topics** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


