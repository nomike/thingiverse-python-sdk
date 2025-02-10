# ForumSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**thumbnail** | **str** |  | [optional] 
**topic_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.forum_schema import ForumSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ForumSchema from a JSON string
forum_schema_instance = ForumSchema.from_json(json)
# print the JSON string representation of the object
print(ForumSchema.to_json())

# convert the object into a dict
forum_schema_dict = forum_schema_instance.to_dict()
# create an instance of ForumSchema from a dict
forum_schema_from_dict = ForumSchema.from_dict(forum_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


