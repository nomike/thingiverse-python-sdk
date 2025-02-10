# EmailBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**email_sent** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.email_body import EmailBody

# TODO update the JSON string below
json = "{}"
# create an instance of EmailBody from a JSON string
email_body_instance = EmailBody.from_json(json)
# print the JSON string representation of the object
print(EmailBody.to_json())

# convert the object into a dict
email_body_dict = email_body_instance.to_dict()
# create an instance of EmailBody from a dict
email_body_from_dict = EmailBody.from_dict(email_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


