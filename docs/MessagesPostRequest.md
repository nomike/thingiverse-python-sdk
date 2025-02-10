# MessagesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_user** | **str** | Set the username to whom the message will be sent. | 
**subject** | **str** | Set the subject of message | 
**body** | **str** | The contents of the message | 

## Example

```python
from openapi_client.models.messages_post_request import MessagesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesPostRequest from a JSON string
messages_post_request_instance = MessagesPostRequest.from_json(json)
# print the JSON string representation of the object
print(MessagesPostRequest.to_json())

# convert the object into a dict
messages_post_request_dict = messages_post_request_instance.to_dict()
# create an instance of MessagesPostRequest from a dict
messages_post_request_from_dict = MessagesPostRequest.from_dict(messages_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


