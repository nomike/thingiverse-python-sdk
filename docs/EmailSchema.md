# EmailSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**EmailBody**](EmailBody.md) |  | [optional] 

## Example

```python
from openapi_client.models.email_schema import EmailSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSchema from a JSON string
email_schema_instance = EmailSchema.from_json(json)
# print the JSON string representation of the object
print(EmailSchema.to_json())

# convert the object into a dict
email_schema_dict = email_schema_instance.to_dict()
# create an instance of EmailSchema from a dict
email_schema_from_dict = EmailSchema.from_dict(email_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


