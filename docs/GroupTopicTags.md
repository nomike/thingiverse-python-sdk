# GroupTopicTags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | [**UrlSchema**](UrlSchema.md) |  | [optional] 
**count** | **int** |  | [optional] 
**absolute_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.group_topic_tags import GroupTopicTags

# TODO update the JSON string below
json = "{}"
# create an instance of GroupTopicTags from a JSON string
group_topic_tags_instance = GroupTopicTags.from_json(json)
# print the JSON string representation of the object
print(GroupTopicTags.to_json())

# convert the object into a dict
group_topic_tags_dict = group_topic_tags_instance.to_dict()
# create an instance of GroupTopicTags from a dict
group_topic_tags_from_dict = GroupTopicTags.from_dict(group_topic_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


