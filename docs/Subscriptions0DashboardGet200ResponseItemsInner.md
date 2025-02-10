# Subscriptions0DashboardGet200ResponseItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**image** | [**Subscriptions0DashboardGet200ResponseItemsInnerImage**](Subscriptions0DashboardGet200ResponseItemsInnerImage.md) |  | [optional] 
**type** | **str** |  | [optional] 
**is_subscribed** | **bool** |  | [optional] 
**user** | [**UserSchema**](UserSchema.md) |  | [optional] 
**is_personal** | **bool** |  | [optional] 
**time** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**content** | [**Subscriptions0DashboardGet200ResponseItemsInnerContent**](Subscriptions0DashboardGet200ResponseItemsInnerContent.md) |  | [optional] 

## Example

```python
from openapi_client.models.subscriptions0_dashboard_get200_response_items_inner import Subscriptions0DashboardGet200ResponseItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Subscriptions0DashboardGet200ResponseItemsInner from a JSON string
subscriptions0_dashboard_get200_response_items_inner_instance = Subscriptions0DashboardGet200ResponseItemsInner.from_json(json)
# print the JSON string representation of the object
print(Subscriptions0DashboardGet200ResponseItemsInner.to_json())

# convert the object into a dict
subscriptions0_dashboard_get200_response_items_inner_dict = subscriptions0_dashboard_get200_response_items_inner_instance.to_dict()
# create an instance of Subscriptions0DashboardGet200ResponseItemsInner from a dict
subscriptions0_dashboard_get200_response_items_inner_from_dict = Subscriptions0DashboardGet200ResponseItemsInner.from_dict(subscriptions0_dashboard_get200_response_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


