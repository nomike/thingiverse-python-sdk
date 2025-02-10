# ThingSchema


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
**modified** | **datetime** |  | [optional] 
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
**details_parts** | **List[object]** |  | [optional] 
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
**needs_moderation** | **int** |  | [optional] 
**is_decoy** | **int** |  | [optional] 
**zip_data** | [**ThingZipData**](ThingZipData.md) |  | [optional] 

## Example

```python
from openapi_client.models.thing_schema import ThingSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ThingSchema from a JSON string
thing_schema_instance = ThingSchema.from_json(json)
# print the JSON string representation of the object
print(ThingSchema.to_json())

# convert the object into a dict
thing_schema_dict = thing_schema_instance.to_dict()
# create an instance of ThingSchema from a dict
thing_schema_from_dict = ThingSchema.from_dict(thing_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


