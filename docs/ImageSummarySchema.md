# ImageSummarySchema


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
from openapi_client.models.image_summary_schema import ImageSummarySchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImageSummarySchema from a JSON string
image_summary_schema_instance = ImageSummarySchema.from_json(json)
# print the JSON string representation of the object
print(ImageSummarySchema.to_json())

# convert the object into a dict
image_summary_schema_dict = image_summary_schema_instance.to_dict()
# create an instance of ImageSummarySchema from a dict
image_summary_schema_from_dict = ImageSummarySchema.from_dict(image_summary_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


