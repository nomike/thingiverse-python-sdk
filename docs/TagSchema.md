# TagSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**things_url** | **str** |  | [optional] 
**absolute_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tag_schema import TagSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TagSchema from a JSON string
tag_schema_instance = TagSchema.from_json(json)
# print the JSON string representation of the object
print(TagSchema.to_json())

# convert the object into a dict
tag_schema_dict = tag_schema_instance.to_dict()
# create an instance of TagSchema from a dict
tag_schema_from_dict = TagSchema.from_dict(tag_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


