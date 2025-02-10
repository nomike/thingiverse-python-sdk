# TopicSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**group_url** | **str** |  | [optional] 
**pinned** | **int** |  | [optional] 
**public_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**added** | **datetime** |  | [optional] 
**modified** | [**CommentModified**](CommentModified.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**comments** | [**TopicSchemaComments**](TopicSchemaComments.md) |  | [optional] 
**comment_of_topic** | [**TopicSchemaCommentOfTopic**](TopicSchemaCommentOfTopic.md) |  | [optional] 

## Example

```python
from openapi_client.models.topic_schema import TopicSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TopicSchema from a JSON string
topic_schema_instance = TopicSchema.from_json(json)
# print the JSON string representation of the object
print(TopicSchema.to_json())

# convert the object into a dict
topic_schema_dict = topic_schema_instance.to_dict()
# create an instance of TopicSchema from a dict
topic_schema_from_dict = TopicSchema.from_dict(topic_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


