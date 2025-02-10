# GroupTopicComments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**threaded_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.group_topic_comments import GroupTopicComments

# TODO update the JSON string below
json = "{}"
# create an instance of GroupTopicComments from a JSON string
group_topic_comments_instance = GroupTopicComments.from_json(json)
# print the JSON string representation of the object
print(GroupTopicComments.to_json())

# convert the object into a dict
group_topic_comments_dict = group_topic_comments_instance.to_dict()
# create an instance of GroupTopicComments from a dict
group_topic_comments_from_dict = GroupTopicComments.from_dict(group_topic_comments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


