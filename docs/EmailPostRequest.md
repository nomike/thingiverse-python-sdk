# EmailPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Set the client ID of app | [optional] 
**email_type** | **str** | Set the type of email | 
**site** | **str** | Set the parameter of site. Site parameter&#39;s value should be either &#39;tv&#39; or &#39;mb&#39; | 
**user_id** | **int** | Set the ID of the user who will receive the email | 
**forgot_email** | **str** | Set the forgotten email. In this case, set the email type as a forgot | [optional] 

## Example

```python
from openapi_client.models.email_post_request import EmailPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailPostRequest from a JSON string
email_post_request_instance = EmailPostRequest.from_json(json)
# print the JSON string representation of the object
print(EmailPostRequest.to_json())

# convert the object into a dict
email_post_request_dict = email_post_request_instance.to_dict()
# create an instance of EmailPostRequest from a dict
email_post_request_from_dict = EmailPostRequest.from_dict(email_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


