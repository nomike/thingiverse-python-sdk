# UserSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**thumbnail** | **str** |  | [optional] 
**count_of_followers** | **int** |  | [optional] 
**count_of_following** | **int** |  | [optional] 
**count_of_designs** | **int** |  | [optional] 
**make_count** | **int** |  | [optional] 
**accepts_tips** | **bool** |  | [optional] 
**is_following** | **bool** |  | [optional] 
**location** | **str** |  | [optional] 
**cover** | **str** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**is_moderator** | **bool** |  | [optional] 
**is_featured** | **bool** |  | [optional] 
**is_verified** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.user_summary import UserSummary

# TODO update the JSON string below
json = "{}"
# create an instance of UserSummary from a JSON string
user_summary_instance = UserSummary.from_json(json)
# print the JSON string representation of the object
print(UserSummary.to_json())

# convert the object into a dict
user_summary_dict = user_summary_instance.to_dict()
# create an instance of UserSummary from a dict
user_summary_from_dict = UserSummary.from_dict(user_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


