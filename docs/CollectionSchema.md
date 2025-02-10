# CollectionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**description_html** | **str** |  | [optional] 
**added** | **datetime** |  | 
**modified** | **datetime** |  | 
**creator** | [**UserSummarySchema1**](UserSummarySchema1.md) |  | 
**url** | **str** |  | 
**count** | **int** |  | 
**is_editable** | **bool** |  | 
**is_featured** | **bool** |  | 
**is_liked** | **bool** |  | [optional] 
**is_watched** | **bool** |  | 
**featured_on** | **str** | When thing was featured. Is only set when is_featured is true | [optional] 
**featured_thing_id** | **int** | ID of the thing that is marked by the creator as being the \&quot;primary\&quot; thing. | 
**preview_image** | **str** |  | 
**absolute_url** | **str** |  | 
**thumbnail** | **str** |  | 

## Example

```python
from openapi_client.models.collection_schema import CollectionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionSchema from a JSON string
collection_schema_instance = CollectionSchema.from_json(json)
# print the JSON string representation of the object
print(CollectionSchema.to_json())

# convert the object into a dict
collection_schema_dict = collection_schema_instance.to_dict()
# create an instance of CollectionSchema from a dict
collection_schema_from_dict = CollectionSchema.from_dict(collection_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


