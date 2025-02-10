# ThingZipData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[ThingZipDataFilesInner]**](ThingZipDataFilesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.thing_zip_data import ThingZipData

# TODO update the JSON string below
json = "{}"
# create an instance of ThingZipData from a JSON string
thing_zip_data_instance = ThingZipData.from_json(json)
# print the JSON string representation of the object
print(ThingZipData.to_json())

# convert the object into a dict
thing_zip_data_dict = thing_zip_data_instance.to_dict()
# create an instance of ThingZipData from a dict
thing_zip_data_from_dict = ThingZipData.from_dict(thing_zip_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


