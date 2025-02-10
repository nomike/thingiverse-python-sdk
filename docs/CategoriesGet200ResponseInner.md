# CategoriesGet200ResponseInner


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
from openapi_client.models.categories_get200_response_inner import CategoriesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesGet200ResponseInner from a JSON string
categories_get200_response_inner_instance = CategoriesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(CategoriesGet200ResponseInner.to_json())

# convert the object into a dict
categories_get200_response_inner_dict = categories_get200_response_inner_instance.to_dict()
# create an instance of CategoriesGet200ResponseInner from a dict
categories_get200_response_inner_from_dict = CategoriesGet200ResponseInner.from_dict(categories_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


