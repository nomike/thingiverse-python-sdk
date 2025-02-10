# ShortThingSchema


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
**is_private** | **int** |  | [optional] 
**is_purchased** | **int** |  | [optional] 
**is_published** | **int** |  | [optional] 
**like_count** | **int** |  | [optional] 
**collect_count** | **int** |  | [optional] 
**make_count** | **int** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**tags** | [**List[TagSchema]**](TagSchema.md) |  | [optional] 
**is_nsfw** | **bool** |  | [optional] 
**rank** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.short_thing_schema import ShortThingSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ShortThingSchema from a JSON string
short_thing_schema_instance = ShortThingSchema.from_json(json)
# print the JSON string representation of the object
print(ShortThingSchema.to_json())

# convert the object into a dict
short_thing_schema_dict = short_thing_schema_instance.to_dict()
# create an instance of ShortThingSchema from a dict
short_thing_schema_from_dict = ShortThingSchema.from_dict(short_thing_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


