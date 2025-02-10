# CopiesCopyIdThreadedCommentsGet200ResponseCommentsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**add_date** | **datetime** |  | [optional] 
**modified_date** | [**CopiesCopyIdThreadedCommentsGet200ResponseCommentsValueModifiedDate**](CopiesCopyIdThreadedCommentsGet200ResponseCommentsValueModifiedDate.md) |  | [optional] 
**body** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 
**needs_moderation** | **int** |  | [optional] 
**assets** | **List[str]** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**parent_user_name** | **str** |  | [optional] 
**parent_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.copies_copy_id_threaded_comments_get200_response_comments_value import CopiesCopyIdThreadedCommentsGet200ResponseCommentsValue

# TODO update the JSON string below
json = "{}"
# create an instance of CopiesCopyIdThreadedCommentsGet200ResponseCommentsValue from a JSON string
copies_copy_id_threaded_comments_get200_response_comments_value_instance = CopiesCopyIdThreadedCommentsGet200ResponseCommentsValue.from_json(json)
# print the JSON string representation of the object
print(CopiesCopyIdThreadedCommentsGet200ResponseCommentsValue.to_json())

# convert the object into a dict
copies_copy_id_threaded_comments_get200_response_comments_value_dict = copies_copy_id_threaded_comments_get200_response_comments_value_instance.to_dict()
# create an instance of CopiesCopyIdThreadedCommentsGet200ResponseCommentsValue from a dict
copies_copy_id_threaded_comments_get200_response_comments_value_from_dict = CopiesCopyIdThreadedCommentsGet200ResponseCommentsValue.from_dict(copies_copy_id_threaded_comments_get200_response_comments_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


