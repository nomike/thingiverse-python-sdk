# TopicSchemaComments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**threaded_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.topic_schema_comments import TopicSchemaComments

# TODO update the JSON string below
json = "{}"
# create an instance of TopicSchemaComments from a JSON string
topic_schema_comments_instance = TopicSchemaComments.from_json(json)
# print the JSON string representation of the object
print(TopicSchemaComments.to_json())

# convert the object into a dict
topic_schema_comments_dict = topic_schema_comments_instance.to_dict()
# create an instance of TopicSchemaComments from a dict
topic_schema_comments_from_dict = TopicSchemaComments.from_dict(topic_schema_comments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


