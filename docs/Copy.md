# Copy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**added** | **datetime** |  | [optional] 
**like_count** | **int** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**description_html** | **str** |  | [optional] 
**is_liked** | **bool** |  | [optional] 
**creator** | [**UserSummarySchema1**](UserSummarySchema1.md) |  | [optional] 
**thing** | [**ThingSchema**](ThingSchema.md) |  | [optional] 
**thumbnail** | **str** |  | [optional] 
**preview_image** | **str** |  | [optional] 
**images_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**needs_moderation** | **bool** |  | [optional] 
**type_name** | **str** |  | [optional] 
**view_count** | **int** |  | [optional] 
**category_name** | **str** |  | [optional] 
**category_url** | **str** |  | [optional] 
**details_parts** | **List[str]** |  | [optional] 
**details** | **str** |  | [optional] 
**root_comment_count** | **int** |  | [optional] 
**is_watched** | **bool** |  | [optional] 
**is_comments_disabled** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.copy import Copy

# TODO update the JSON string below
json = "{}"
# create an instance of Copy from a JSON string
copy_instance = Copy.from_json(json)
# print the JSON string representation of the object
print(Copy.to_json())

# convert the object into a dict
copy_dict = copy_instance.to_dict()
# create an instance of Copy from a dict
copy_from_dict = Copy.from_dict(copy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


