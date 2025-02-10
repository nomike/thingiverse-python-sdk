# Subscriptions0DashboardGet200ResponseItemsInnerContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**thumbnail** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**creator** | [**UserSummarySchema1**](UserSummarySchema1.md) |  | [optional] 
**added** | **datetime** |  | [optional] 
**modified** | [**CommentModified**](CommentModified.md) |  | [optional] 
**is_published** | **int** |  | [optional] 
**is_wip** | **int** |  | [optional] 
**is_featured** | **bool** |  | [optional] 
**is_nsfw** | **bool** |  | [optional] 
**is_ai** | **bool** |  | [optional] 
**like_count** | **int** |  | [optional] 
**is_liked** | **bool** |  | [optional] 
**collect_count** | **int** |  | [optional] 
**is_collected** | **bool** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**is_watched** | **bool** |  | [optional] 
**default_image** | [**ImageSummarySchema**](ImageSummarySchema.md) |  | [optional] 
**description** | **str** |  | [optional] 
**instructions** | **str** |  | [optional] 
**description_html** | **str** |  | [optional] 
**instructions_html** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**details_parts** | **List[str]** |  | [optional] 
**edu_details** | **str** |  | [optional] 
**edu_details_parts** | **List[object]** |  | [optional] 
**license** | **str** |  | [optional] 
**allows_derivatives** | **bool** |  | [optional] 
**files_url** | **str** |  | [optional] 
**images_url** | **str** |  | [optional] 
**likes_url** | **str** |  | [optional] 
**ancestors_url** | **str** |  | [optional] 
**derivatives_url** | **str** |  | [optional] 
**tags_url** | **str** |  | [optional] 
**tags** | [**List[TagSchema]**](TagSchema.md) |  | [optional] 
**categories_url** | **str** |  | [optional] 
**file_count** | **int** |  | [optional] 
**is_purchased** | **int** |  | [optional] 
**app_id** | **int** |  | [optional] 
**download_count** | **int** |  | [optional] 
**view_count** | **int** |  | [optional] 
**education** | [**ThingEducation**](ThingEducation.md) |  | [optional] 
**remix_count** | **int** |  | [optional] 
**make_count** | **int** |  | [optional] 
**app_count** | **int** |  | [optional] 
**root_comment_count** | **int** |  | [optional] 
**moderation** | **str** |  | [optional] 
**is_derivative** | **bool** |  | [optional] 
**ancestors** | **List[str]** |  | [optional] 
**can_comment** | **bool** |  | [optional] 
**type_name** | **str** |  | [optional] 
**is_banned** | **bool** |  | [optional] 
**is_comments_disabled** | **bool** |  | [optional] 
**needs_moderation** | **bool** |  | [optional] 
**is_decoy** | **int** |  | [optional] 
**zip_data** | [**ThingZipData**](ThingZipData.md) |  | [optional] 
**thing** | [**ThingSchema**](ThingSchema.md) |  | [optional] 
**preview_image** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**category_url** | **str** |  | [optional] 
**target_type** | **str** |  | [optional] 
**target_id** | **int** |  | [optional] 
**target_url** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**body_html** | **str** |  | [optional] 
**user** | [**UserSummarySchema1**](UserSummarySchema1.md) |  | [optional] 
**parent_id** | **int** |  | [optional] 
**parent_url** | **str** |  | [optional] 
**parent_user_name** | **str** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**attachments** | [**List[CommentAttachmentsInner]**](CommentAttachmentsInner.md) |  | [optional] 
**is_root_comment** | **bool** |  | [optional] 
**has_children** | **bool** |  | [optional] 
**recaptcha_token** | **str** |  | [optional] 
**things** | [**List[ThingSchema]**](ThingSchema.md) |  | [optional] 
**count** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**things_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.subscriptions0_dashboard_get200_response_items_inner_content import Subscriptions0DashboardGet200ResponseItemsInnerContent

# TODO update the JSON string below
json = "{}"
# create an instance of Subscriptions0DashboardGet200ResponseItemsInnerContent from a JSON string
subscriptions0_dashboard_get200_response_items_inner_content_instance = Subscriptions0DashboardGet200ResponseItemsInnerContent.from_json(json)
# print the JSON string representation of the object
print(Subscriptions0DashboardGet200ResponseItemsInnerContent.to_json())

# convert the object into a dict
subscriptions0_dashboard_get200_response_items_inner_content_dict = subscriptions0_dashboard_get200_response_items_inner_content_instance.to_dict()
# create an instance of Subscriptions0DashboardGet200ResponseItemsInnerContent from a dict
subscriptions0_dashboard_get200_response_items_inner_content_from_dict = Subscriptions0DashboardGet200ResponseItemsInnerContent.from_dict(subscriptions0_dashboard_get200_response_items_inner_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


