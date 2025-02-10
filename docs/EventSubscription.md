# EventSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.event_subscription import EventSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of EventSubscription from a JSON string
event_subscription_instance = EventSubscription.from_json(json)
# print the JSON string representation of the object
print(EventSubscription.to_json())

# convert the object into a dict
event_subscription_dict = event_subscription_instance.to_dict()
# create an instance of EventSubscription from a dict
event_subscription_from_dict = EventSubscription.from_dict(event_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


