# HomeBanner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**button_name** | **str** |  | [optional] 
**button_url** | **str** |  | [optional] 
**background_color** | **str** |  | [optional] 
**background_image_url** | **str** |  | [optional] 
**tablet_image_url** | **str** |  | [optional] 
**mobile_image_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**thing** | [**ThingSchema**](ThingSchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.home_banner import HomeBanner

# TODO update the JSON string below
json = "{}"
# create an instance of HomeBanner from a JSON string
home_banner_instance = HomeBanner.from_json(json)
# print the JSON string representation of the object
print(HomeBanner.to_json())

# convert the object into a dict
home_banner_dict = home_banner_instance.to_dict()
# create an instance of HomeBanner from a dict
home_banner_from_dict = HomeBanner.from_dict(home_banner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


