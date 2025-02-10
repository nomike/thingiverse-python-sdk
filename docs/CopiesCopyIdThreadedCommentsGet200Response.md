# CopiesCopyIdThreadedCommentsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**Dict[str, CopiesCopyIdThreadedCommentsGet200ResponseCommentsValue]**](CopiesCopyIdThreadedCommentsGet200ResponseCommentsValue.md) |  | [optional] 
**users** | [**Dict[str, CopiesCopyIdThreadedCommentsGet200ResponseUsersValue]**](CopiesCopyIdThreadedCommentsGet200ResponseUsersValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.copies_copy_id_threaded_comments_get200_response import CopiesCopyIdThreadedCommentsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CopiesCopyIdThreadedCommentsGet200Response from a JSON string
copies_copy_id_threaded_comments_get200_response_instance = CopiesCopyIdThreadedCommentsGet200Response.from_json(json)
# print the JSON string representation of the object
print(CopiesCopyIdThreadedCommentsGet200Response.to_json())

# convert the object into a dict
copies_copy_id_threaded_comments_get200_response_dict = copies_copy_id_threaded_comments_get200_response_instance.to_dict()
# create an instance of CopiesCopyIdThreadedCommentsGet200Response from a dict
copies_copy_id_threaded_comments_get200_response_from_dict = CopiesCopyIdThreadedCommentsGet200Response.from_dict(copies_copy_id_threaded_comments_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


