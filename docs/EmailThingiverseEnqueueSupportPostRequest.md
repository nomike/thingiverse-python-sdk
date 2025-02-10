# EmailThingiverseEnqueueSupportPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Email subject | 
**text** | **str** | Email text | 
**html** | **str** | Email as HTML | [optional] 

## Example

```python
from openapi_client.models.email_thingiverse_enqueue_support_post_request import EmailThingiverseEnqueueSupportPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailThingiverseEnqueueSupportPostRequest from a JSON string
email_thingiverse_enqueue_support_post_request_instance = EmailThingiverseEnqueueSupportPostRequest.from_json(json)
# print the JSON string representation of the object
print(EmailThingiverseEnqueueSupportPostRequest.to_json())

# convert the object into a dict
email_thingiverse_enqueue_support_post_request_dict = email_thingiverse_enqueue_support_post_request_instance.to_dict()
# create an instance of EmailThingiverseEnqueueSupportPostRequest from a dict
email_thingiverse_enqueue_support_post_request_from_dict = EmailThingiverseEnqueueSupportPostRequest.from_dict(email_thingiverse_enqueue_support_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


