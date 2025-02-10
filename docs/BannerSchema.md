# BannerSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner_image** | **str** |  | [optional] 
**big_banner_image** | **str** |  | [optional] 
**banner_tablet_image** | **str** |  | [optional] 
**banner_mobile_image** | **str** |  | [optional] 
**banner_url** | **str** |  | [optional] 
**banner_video** | **str** |  | [optional] 
**big_banner_video** | **str** |  | [optional] 
**banner_tablet_video** | **str** |  | [optional] 
**banner_mobile_video** | **str** |  | [optional] 
**location** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.banner_schema import BannerSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BannerSchema from a JSON string
banner_schema_instance = BannerSchema.from_json(json)
# print the JSON string representation of the object
print(BannerSchema.to_json())

# convert the object into a dict
banner_schema_dict = banner_schema_instance.to_dict()
# create an instance of BannerSchema from a dict
banner_schema_from_dict = BannerSchema.from_dict(banner_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


