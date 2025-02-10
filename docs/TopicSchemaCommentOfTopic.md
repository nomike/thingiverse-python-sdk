# TopicSchemaCommentOfTopic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**topic_name** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**body_html** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**target_url** | **str** |  | [optional] 
**target_type** | **str** |  | [optional] 
**target_id** | **int** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**parent_url** | **str** |  | [optional] 
**has_children** | **bool** |  | [optional] 
**needs_moderation** | **bool** |  | [optional] 
**is_root_comment** | **bool** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**added** | **datetime** |  | [optional] 
**modified** | [**CommentModified**](CommentModified.md) |  | [optional] 
**attachments** | [**List[CommentAttachmentsInner]**](CommentAttachmentsInner.md) |  | [optional] 
**user** | [**UserSummarySchema1**](UserSummarySchema1.md) |  | [optional] 
**things** | [**List[TopicSchemaCommentOfTopicThingsInner]**](TopicSchemaCommentOfTopicThingsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.topic_schema_comment_of_topic import TopicSchemaCommentOfTopic

# TODO update the JSON string below
json = "{}"
# create an instance of TopicSchemaCommentOfTopic from a JSON string
topic_schema_comment_of_topic_instance = TopicSchemaCommentOfTopic.from_json(json)
# print the JSON string representation of the object
print(TopicSchemaCommentOfTopic.to_json())

# convert the object into a dict
topic_schema_comment_of_topic_dict = topic_schema_comment_of_topic_instance.to_dict()
# create an instance of TopicSchemaCommentOfTopic from a dict
topic_schema_comment_of_topic_from_dict = TopicSchemaCommentOfTopic.from_dict(topic_schema_comment_of_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


