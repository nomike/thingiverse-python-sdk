# FeaturedSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**thumbnail** | **str** |  | [optional] 
**preview_image** | **str** |  | [optional] 
**creator** | [**UserSummarySchema1**](UserSummarySchema1.md) |  | [optional] 
**is_private** | **bool** |  | [optional] 
**is_purchased** | **bool** |  | [optional] 
**is_published** | **bool** |  | [optional] 
**like_count** | **int** |  | [optional] 
**collect_count** | **int** |  | [optional] 
**make_count** | **int** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**tags** | [**List[TagSchema]**](TagSchema.md) |  | [optional] 
**is_nsfw** | **bool** |  | [optional] 
**rank** | **int** |  | [optional] 
**spotlight_images** | [**FeaturedSpotlightImages**](FeaturedSpotlightImages.md) |  | [optional] 

## Example

```python
from openapi_client.models.featured_schema import FeaturedSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturedSchema from a JSON string
featured_schema_instance = FeaturedSchema.from_json(json)
# print the JSON string representation of the object
print(FeaturedSchema.to_json())

# convert the object into a dict
featured_schema_dict = featured_schema_instance.to_dict()
# create an instance of FeaturedSchema from a dict
featured_schema_from_dict = FeaturedSchema.from_dict(featured_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


