# Event


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 
**targets** | [**List[EventTargetsInner]**](EventTargetsInner.md) |  | [optional] 
**sources** | [**List[EventSourcesInner]**](EventSourcesInner.md) |  | [optional] 
**subscription** | [**EventSubscription**](EventSubscription.md) |  | [optional] 

## Example

```python
from openapi_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


