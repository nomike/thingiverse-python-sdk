# AppSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**thumbnail** | **str** |  | [optional] 
**creator** | [**UserSummarySchema1**](UserSummarySchema1.md) |  | [optional] 
**is_published** | **bool** |  | [optional] 
**is_approved** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.app_schema import AppSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AppSchema from a JSON string
app_schema_instance = AppSchema.from_json(json)
# print the JSON string representation of the object
print(AppSchema.to_json())

# convert the object into a dict
app_schema_dict = app_schema_instance.to_dict()
# create an instance of AppSchema from a dict
app_schema_from_dict = AppSchema.from_dict(app_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


