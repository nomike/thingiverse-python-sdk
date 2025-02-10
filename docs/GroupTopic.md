# GroupTopic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | [optional] 
**user** | [**MemberSchema**](MemberSchema.md) |  | [optional] 
**group_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**comments** | [**GroupTopicComments**](GroupTopicComments.md) |  | [optional] 
**added** | **datetime** |  | [optional] 
**modified** | [**CommentModified**](CommentModified.md) |  | [optional] 
**pinned** | **int** |  | [optional] 
**comment_of_topic** | [**CommentSchema**](CommentSchema.md) |  | [optional] 
**tags** | [**GroupTopicTags**](GroupTopicTags.md) |  | [optional] 
**watched** | **bool** |  | [optional] 
**type_name** | **str** |  | [optional] 
**root_comment_count** | **int** |  | [optional] 
**can_comment** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.group_topic import GroupTopic

# TODO update the JSON string below
json = "{}"
# create an instance of GroupTopic from a JSON string
group_topic_instance = GroupTopic.from_json(json)
# print the JSON string representation of the object
print(GroupTopic.to_json())

# convert the object into a dict
group_topic_dict = group_topic_instance.to_dict()
# create an instance of GroupTopic from a dict
group_topic_from_dict = GroupTopic.from_dict(group_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


