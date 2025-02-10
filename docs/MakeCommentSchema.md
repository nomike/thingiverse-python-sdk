# MakeCommentSchema


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
**user** | [**UserSchema**](UserSchema.md) |  | [optional] 
**added** | **datetime** |  | [optional] 
**modified** | [**CommentModified**](CommentModified.md) |  | [optional] 
**parent_id** | **int** |  | [optional] 
**parent_url** | **str** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**attachments** | [**List[CommentAttachmentsInner]**](CommentAttachmentsInner.md) |  | [optional] 
**needs_moderation** | **bool** |  | [optional] 
**is_root_comment** | **bool** |  | [optional] 
**has_children** | **bool** |  | [optional] 
**topic_name** | **str** |  | [optional] 
**things** | [**List[ShortThingSchema]**](ShortThingSchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.make_comment_schema import MakeCommentSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MakeCommentSchema from a JSON string
make_comment_schema_instance = MakeCommentSchema.from_json(json)
# print the JSON string representation of the object
print(MakeCommentSchema.to_json())

# convert the object into a dict
make_comment_schema_dict = make_comment_schema_instance.to_dict()
# create an instance of MakeCommentSchema from a dict
make_comment_schema_from_dict = MakeCommentSchema.from_dict(make_comment_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


