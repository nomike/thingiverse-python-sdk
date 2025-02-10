# Sitewidenotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**notification** | **str** |  | [optional] 
**notification_html** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sitewidenotification import Sitewidenotification

# TODO update the JSON string below
json = "{}"
# create an instance of Sitewidenotification from a JSON string
sitewidenotification_instance = Sitewidenotification.from_json(json)
# print the JSON string representation of the object
print(Sitewidenotification.to_json())

# convert the object into a dict
sitewidenotification_dict = sitewidenotification_instance.to_dict()
# create an instance of Sitewidenotification from a dict
sitewidenotification_from_dict = Sitewidenotification.from_dict(sitewidenotification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


