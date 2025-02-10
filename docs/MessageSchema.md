# MessageSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**from_user_id** | **int** |  | [optional] 
**to_user_id** | **int** |  | [optional] 
**subject** | **str** |  | [optional] 
**add_date** | **datetime** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**comment_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.message_schema import MessageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MessageSchema from a JSON string
message_schema_instance = MessageSchema.from_json(json)
# print the JSON string representation of the object
print(MessageSchema.to_json())

# convert the object into a dict
message_schema_dict = message_schema_instance.to_dict()
# create an instance of MessageSchema from a dict
message_schema_from_dict = MessageSchema.from_dict(message_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


