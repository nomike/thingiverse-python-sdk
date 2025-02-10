# UsersUsernameSearchTermGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**hits** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.users_username_search_term_get200_response import UsersUsernameSearchTermGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUsernameSearchTermGet200Response from a JSON string
users_username_search_term_get200_response_instance = UsersUsernameSearchTermGet200Response.from_json(json)
# print the JSON string representation of the object
print(UsersUsernameSearchTermGet200Response.to_json())

# convert the object into a dict
users_username_search_term_get200_response_dict = users_username_search_term_get200_response_instance.to_dict()
# create an instance of UsersUsernameSearchTermGet200Response from a dict
users_username_search_term_get200_response_from_dict = UsersUsernameSearchTermGet200Response.from_dict(users_username_search_term_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


