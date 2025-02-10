# CopiesCopyIdCommentsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | 
**recaptcha_token** | **str** | Set the recaptcha token to confirm that the user is not a bot | 

## Example

```python
from openapi_client.models.copies_copy_id_comments_post_request import CopiesCopyIdCommentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CopiesCopyIdCommentsPostRequest from a JSON string
copies_copy_id_comments_post_request_instance = CopiesCopyIdCommentsPostRequest.from_json(json)
# print the JSON string representation of the object
print(CopiesCopyIdCommentsPostRequest.to_json())

# convert the object into a dict
copies_copy_id_comments_post_request_dict = copies_copy_id_comments_post_request_instance.to_dict()
# create an instance of CopiesCopyIdCommentsPostRequest from a dict
copies_copy_id_comments_post_request_from_dict = CopiesCopyIdCommentsPostRequest.from_dict(copies_copy_id_comments_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


