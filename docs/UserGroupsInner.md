# UserGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_groups_inner import UserGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupsInner from a JSON string
user_groups_inner_instance = UserGroupsInner.from_json(json)
# print the JSON string representation of the object
print(UserGroupsInner.to_json())

# convert the object into a dict
user_groups_inner_dict = user_groups_inner_instance.to_dict()
# create an instance of UserGroupsInner from a dict
user_groups_inner_from_dict = UserGroupsInner.from_dict(user_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


