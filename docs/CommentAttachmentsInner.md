# CommentAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**download_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.comment_attachments_inner import CommentAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommentAttachmentsInner from a JSON string
comment_attachments_inner_instance = CommentAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(CommentAttachmentsInner.to_json())

# convert the object into a dict
comment_attachments_inner_dict = comment_attachments_inner_instance.to_dict()
# create an instance of CommentAttachmentsInner from a dict
comment_attachments_inner_from_dict = CommentAttachmentsInner.from_dict(comment_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


