# CategoriesSlugGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**things_url** | **str** |  | [optional] 
**thumbnail** | **str** |  | [optional] 
**preview_image** | **str** |  | [optional] 
**children** | [**List[CategorySchema]**](CategorySchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.categories_slug_get200_response import CategoriesSlugGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesSlugGet200Response from a JSON string
categories_slug_get200_response_instance = CategoriesSlugGet200Response.from_json(json)
# print the JSON string representation of the object
print(CategoriesSlugGet200Response.to_json())

# convert the object into a dict
categories_slug_get200_response_dict = categories_slug_get200_response_instance.to_dict()
# create an instance of CategoriesSlugGet200Response from a dict
categories_slug_get200_response_from_dict = CategoriesSlugGet200Response.from_dict(categories_slug_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


