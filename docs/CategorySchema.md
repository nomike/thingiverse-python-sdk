# CategorySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**things_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.category_schema import CategorySchema

# TODO update the JSON string below
json = "{}"
# create an instance of CategorySchema from a JSON string
category_schema_instance = CategorySchema.from_json(json)
# print the JSON string representation of the object
print(CategorySchema.to_json())

# convert the object into a dict
category_schema_dict = category_schema_instance.to_dict()
# create an instance of CategorySchema from a dict
category_schema_from_dict = CategorySchema.from_dict(category_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


