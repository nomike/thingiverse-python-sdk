# TopicSchemaCommentOfTopicThingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**thumbnail** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**creator** | [**UserSummarySchema1**](UserSummarySchema1.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**is_published** | **bool** |  | [optional] 
**is_nsfw** | **bool** |  | [optional] 
**is_purchased** | **bool** |  | [optional] 
**is_private** | **bool** |  | [optional] 
**collect_count** | **int** |  | [optional] 
**comment_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.topic_schema_comment_of_topic_things_inner import TopicSchemaCommentOfTopicThingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TopicSchemaCommentOfTopicThingsInner from a JSON string
topic_schema_comment_of_topic_things_inner_instance = TopicSchemaCommentOfTopicThingsInner.from_json(json)
# print the JSON string representation of the object
print(TopicSchemaCommentOfTopicThingsInner.to_json())

# convert the object into a dict
topic_schema_comment_of_topic_things_inner_dict = topic_schema_comment_of_topic_things_inner_instance.to_dict()
# create an instance of TopicSchemaCommentOfTopicThingsInner from a dict
topic_schema_comment_of_topic_things_inner_from_dict = TopicSchemaCommentOfTopicThingsInner.from_dict(topic_schema_comment_of_topic_things_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


