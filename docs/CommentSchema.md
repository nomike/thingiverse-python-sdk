# CommentSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**url** | **str** |  | [optional] 
**target_type** | **str** |  | [optional] 
**target_id** | **int** |  | [optional] 
**public_url** | **str** |  | [optional] 
**target_url** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**body_html** | **str** |  | [optional] 
**user** | [**UserSummarySchema1**](UserSummarySchema1.md) |  | [optional] 
**added** | **datetime** |  | [optional] 
**modified** | [**CommentModified**](CommentModified.md) |  | [optional] 
**parent_id** | **int** |  | [optional] 
**parent_url** | **str** |  | [optional] 
**parent_user_name** | **str** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**attachments** | [**List[CommentAttachmentsInner]**](CommentAttachmentsInner.md) |  | [optional] 
**needs_moderation** | **bool** |  | [optional] 
**is_root_comment** | **bool** |  | [optional] 
**has_children** | **bool** |  | [optional] 
**recaptcha_token** | **str** |  | [optional] 
**can_comment** | **bool** |  | [optional] 
**things** | [**List[ThingSchema]**](ThingSchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.comment_schema import CommentSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CommentSchema from a JSON string
comment_schema_instance = CommentSchema.from_json(json)
# print the JSON string representation of the object
print(CommentSchema.to_json())

# convert the object into a dict
comment_schema_dict = comment_schema_instance.to_dict()
# create an instance of CommentSchema from a dict
comment_schema_from_dict = CommentSchema.from_dict(comment_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


