# MessagesPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**is_read** | **int** |  | [optional] 
**subject** | **str** |  | [optional] 
**user** | [**MessagesPost200ResponseUser**](MessagesPost200ResponseUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.messages_post200_response import MessagesPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesPost200Response from a JSON string
messages_post200_response_instance = MessagesPost200Response.from_json(json)
# print the JSON string representation of the object
print(MessagesPost200Response.to_json())

# convert the object into a dict
messages_post200_response_dict = messages_post200_response_instance.to_dict()
# create an instance of MessagesPost200Response from a dict
messages_post200_response_from_dict = MessagesPost200Response.from_dict(messages_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


