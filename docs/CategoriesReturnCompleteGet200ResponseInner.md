# CategoriesReturnCompleteGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**children** | [**List[CategoriesGet200ResponseInner]**](CategoriesGet200ResponseInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.categories_return_complete_get200_response_inner import CategoriesReturnCompleteGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesReturnCompleteGet200ResponseInner from a JSON string
categories_return_complete_get200_response_inner_instance = CategoriesReturnCompleteGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(CategoriesReturnCompleteGet200ResponseInner.to_json())

# convert the object into a dict
categories_return_complete_get200_response_inner_dict = categories_return_complete_get200_response_inner_instance.to_dict()
# create an instance of CategoriesReturnCompleteGet200ResponseInner from a dict
categories_return_complete_get200_response_inner_from_dict = CategoriesReturnCompleteGet200ResponseInner.from_dict(categories_return_complete_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


