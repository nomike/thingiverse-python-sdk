# CommentsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Set the body of the reply | 
**recaptcha_token** | **str** | Set the recaptcha token to confirm that the user is not a bot | 
**target_type** | **str** | What is the type this comment should be posted on (thing, make, etc) | 
**target_id** | **int** |  | 
**parent_id** | **int** | If it&#39;s a nested comment, set the id of the parent comment here. (optional!) | [optional] 

## Example

```python
from openapi_client.models.comments_post_request import CommentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsPostRequest from a JSON string
comments_post_request_instance = CommentsPostRequest.from_json(json)
# print the JSON string representation of the object
print(CommentsPostRequest.to_json())

# convert the object into a dict
comments_post_request_dict = comments_post_request_instance.to_dict()
# create an instance of CommentsPostRequest from a dict
comments_post_request_from_dict = CommentsPostRequest.from_dict(comments_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


