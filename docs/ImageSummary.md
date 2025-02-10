# ImageSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**sizes** | [**List[ImageSummarySizesInner]**](ImageSummarySizesInner.md) |  | [optional] 
**added** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.image_summary import ImageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ImageSummary from a JSON string
image_summary_instance = ImageSummary.from_json(json)
# print the JSON string representation of the object
print(ImageSummary.to_json())

# convert the object into a dict
image_summary_dict = image_summary_instance.to_dict()
# create an instance of ImageSummary from a dict
image_summary_from_dict = ImageSummary.from_dict(image_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


