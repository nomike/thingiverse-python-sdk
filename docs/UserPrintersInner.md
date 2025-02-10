# UserPrintersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_printers_inner import UserPrintersInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserPrintersInner from a JSON string
user_printers_inner_instance = UserPrintersInner.from_json(json)
# print the JSON string representation of the object
print(UserPrintersInner.to_json())

# convert the object into a dict
user_printers_inner_dict = user_printers_inner_instance.to_dict()
# create an instance of UserPrintersInner from a dict
user_printers_inner_from_dict = UserPrintersInner.from_dict(user_printers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


