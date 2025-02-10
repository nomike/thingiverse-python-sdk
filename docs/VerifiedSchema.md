# VerifiedSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**created_at** | **date** |  | [optional] 
**thumbnail** | **str** |  | [optional] 
**preview_image** | **str** |  | [optional] 
**creator** | [**UserSummarySchema1**](UserSummarySchema1.md) |  | [optional] 
**is_private** | **bool** |  | [optional] 
**is_purchased** | **bool** |  | [optional] 
**is_published** | **bool** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**make_count** | **int** |  | [optional] 
**like_count** | **int** |  | [optional] 
**tags** | [**List[TagSchema]**](TagSchema.md) |  | [optional] 
**is_nsfw** | **bool** |  | [optional] 
**rank** | **int** |  | [optional] 
**collect_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.verified_schema import VerifiedSchema

# TODO update the JSON string below
json = "{}"
# create an instance of VerifiedSchema from a JSON string
verified_schema_instance = VerifiedSchema.from_json(json)
# print the JSON string representation of the object
print(VerifiedSchema.to_json())

# convert the object into a dict
verified_schema_dict = verified_schema_instance.to_dict()
# create an instance of VerifiedSchema from a dict
verified_schema_from_dict = VerifiedSchema.from_dict(verified_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


