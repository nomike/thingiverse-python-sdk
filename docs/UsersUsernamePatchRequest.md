# UsersUsernamePatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Replace the first name of this user. | [optional] 
**last_name** | **str** | Replace the last name of this user. | [optional] 
**bio** | **str** | Replace the biography for this user. | [optional] 
**location** | **str** | Replace the location for this user. | [optional] 
**default_license** | **str** | One of cc, cc-sa, cc-nd, cc-nc, cc-nc-sa, cc-nc-nd, pd0, gpl, lgpl, bsd. Update default license. | [optional] 

## Example

```python
from openapi_client.models.users_username_patch_request import UsersUsernamePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUsernamePatchRequest from a JSON string
users_username_patch_request_instance = UsersUsernamePatchRequest.from_json(json)
# print the JSON string representation of the object
print(UsersUsernamePatchRequest.to_json())

# convert the object into a dict
users_username_patch_request_dict = users_username_patch_request_instance.to_dict()
# create an instance of UsersUsernamePatchRequest from a dict
users_username_patch_request_from_dict = UsersUsernamePatchRequest.from_dict(users_username_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


