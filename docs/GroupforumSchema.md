# GroupforumSchema


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
from openapi_client.models.groupforum_schema import GroupforumSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupforumSchema from a JSON string
groupforum_schema_instance = GroupforumSchema.from_json(json)
# print the JSON string representation of the object
print(GroupforumSchema.to_json())

# convert the object into a dict
groupforum_schema_dict = groupforum_schema_instance.to_dict()
# create an instance of GroupforumSchema from a dict
groupforum_schema_from_dict = GroupforumSchema.from_dict(groupforum_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


