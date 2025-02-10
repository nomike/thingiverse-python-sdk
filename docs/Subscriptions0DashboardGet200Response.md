# Subscriptions0DashboardGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Subscriptions0DashboardGet200ResponseItemsInner]**](Subscriptions0DashboardGet200ResponseItemsInner.md) |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.subscriptions0_dashboard_get200_response import Subscriptions0DashboardGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Subscriptions0DashboardGet200Response from a JSON string
subscriptions0_dashboard_get200_response_instance = Subscriptions0DashboardGet200Response.from_json(json)
# print the JSON string representation of the object
print(Subscriptions0DashboardGet200Response.to_json())

# convert the object into a dict
subscriptions0_dashboard_get200_response_dict = subscriptions0_dashboard_get200_response_instance.to_dict()
# create an instance of Subscriptions0DashboardGet200Response from a dict
subscriptions0_dashboard_get200_response_from_dict = Subscriptions0DashboardGet200Response.from_dict(subscriptions0_dashboard_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


