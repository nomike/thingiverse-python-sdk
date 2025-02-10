# File


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**download_url** | **str** |  | [optional] 
**threejs_url** | **str** |  | [optional] 
**thumbnail** | **str** |  | [optional] 
**default_image** | [**ImageSummarySchema**](ImageSummarySchema.md) |  | [optional] 
**var_date** | **str** |  | [optional] 
**formatted_size** | **str** | a formatted string of a filesize | [optional] 
**meta_data** | **List[str]** |  | [optional] 
**download_count** | **int** |  | [optional] 
**direct_url** | **str** | This will return null if it&#39;s not in the &#39;printable&#39; file list (eg a pdf) | [optional] 

## Example

```python
from openapi_client.models.file import File

# TODO update the JSON string below
json = "{}"
# create an instance of File from a JSON string
file_instance = File.from_json(json)
# print the JSON string representation of the object
print(File.to_json())

# convert the object into a dict
file_dict = file_instance.to_dict()
# create an instance of File from a dict
file_from_dict = File.from_dict(file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


