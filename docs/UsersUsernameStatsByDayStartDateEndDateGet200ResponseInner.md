# UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**views** | **int** |  | [optional] 
**downloads** | **int** |  | [optional] 
**likes** | **int** |  | [optional] 
**collects** | **int** |  | [optional] 
**watches** | **int** |  | [optional] 
**comments** | **int** |  | [optional] 
**makes** | **int** |  | [optional] 
**derivatives** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.users_username_stats_by_day_start_date_end_date_get200_response_inner import UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner from a JSON string
users_username_stats_by_day_start_date_end_date_get200_response_inner_instance = UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner.to_json())

# convert the object into a dict
users_username_stats_by_day_start_date_end_date_get200_response_inner_dict = users_username_stats_by_day_start_date_end_date_get200_response_inner_instance.to_dict()
# create an instance of UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner from a dict
users_username_stats_by_day_start_date_end_date_get200_response_inner_from_dict = UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner.from_dict(users_username_stats_by_day_start_date_end_date_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


