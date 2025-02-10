# SitewidenotificationSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**notification** | **str** |  | [optional] 
**notification_html** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sitewidenotification_schema import SitewidenotificationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SitewidenotificationSchema from a JSON string
sitewidenotification_schema_instance = SitewidenotificationSchema.from_json(json)
# print the JSON string representation of the object
print(SitewidenotificationSchema.to_json())

# convert the object into a dict
sitewidenotification_schema_dict = sitewidenotification_schema_instance.to_dict()
# create an instance of SitewidenotificationSchema from a dict
sitewidenotification_schema_from_dict = SitewidenotificationSchema.from_dict(sitewidenotification_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


