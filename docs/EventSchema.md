# EventSchema


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
from openapi_client.models.event_schema import EventSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchema from a JSON string
event_schema_instance = EventSchema.from_json(json)
# print the JSON string representation of the object
print(EventSchema.to_json())

# convert the object into a dict
event_schema_dict = event_schema_instance.to_dict()
# create an instance of EventSchema from a dict
event_schema_from_dict = EventSchema.from_dict(event_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


