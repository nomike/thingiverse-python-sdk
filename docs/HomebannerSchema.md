# HomebannerSchema


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
from openapi_client.models.homebanner_schema import HomebannerSchema

# TODO update the JSON string below
json = "{}"
# create an instance of HomebannerSchema from a JSON string
homebanner_schema_instance = HomebannerSchema.from_json(json)
# print the JSON string representation of the object
print(HomebannerSchema.to_json())

# convert the object into a dict
homebanner_schema_dict = homebanner_schema_instance.to_dict()
# create an instance of HomebannerSchema from a dict
homebanner_schema_from_dict = HomebannerSchema.from_dict(homebanner_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


