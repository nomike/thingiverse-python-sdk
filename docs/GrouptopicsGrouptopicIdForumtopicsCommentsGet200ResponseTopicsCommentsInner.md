# GrouptopicsGrouptopicIdForumtopicsCommentsGet200ResponseTopicsCommentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | [optional] 
**user** | [**UserSummarySchema1**](UserSummarySchema1.md) |  | [optional] 
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
**target_type** | **str** |  | [optional] 
**target_id** | **int** |  | [optional] 
**target_url** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**body_html** | **str** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**parent_url** | **str** |  | [optional] 
**parent_user_name** | **str** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**attachments** | [**List[CommentAttachmentsInner]**](CommentAttachmentsInner.md) |  | [optional] 
**needs_moderation** | **bool** |  | [optional] 
**is_root_comment** | **bool** |  | [optional] 
**has_children** | **bool** |  | [optional] 
**recaptcha_token** | **str** |  | [optional] 
**things** | [**List[ThingSchema]**](ThingSchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.grouptopics_grouptopic_id_forumtopics_comments_get200_response_topics_comments_inner import GrouptopicsGrouptopicIdForumtopicsCommentsGet200ResponseTopicsCommentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GrouptopicsGrouptopicIdForumtopicsCommentsGet200ResponseTopicsCommentsInner from a JSON string
grouptopics_grouptopic_id_forumtopics_comments_get200_response_topics_comments_inner_instance = GrouptopicsGrouptopicIdForumtopicsCommentsGet200ResponseTopicsCommentsInner.from_json(json)
# print the JSON string representation of the object
print(GrouptopicsGrouptopicIdForumtopicsCommentsGet200ResponseTopicsCommentsInner.to_json())

# convert the object into a dict
grouptopics_grouptopic_id_forumtopics_comments_get200_response_topics_comments_inner_dict = grouptopics_grouptopic_id_forumtopics_comments_get200_response_topics_comments_inner_instance.to_dict()
# create an instance of GrouptopicsGrouptopicIdForumtopicsCommentsGet200ResponseTopicsCommentsInner from a dict
grouptopics_grouptopic_id_forumtopics_comments_get200_response_topics_comments_inner_from_dict = GrouptopicsGrouptopicIdForumtopicsCommentsGet200ResponseTopicsCommentsInner.from_dict(grouptopics_grouptopic_id_forumtopics_comments_get200_response_topics_comments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


