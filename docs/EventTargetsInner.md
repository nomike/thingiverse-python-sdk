# EventTargetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbnail** | **str** |  | [optional] 
**things_url** | **str** |  | [optional] 
**default_image** | [**ImageSummarySchema**](ImageSummarySchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.event_targets_inner import EventTargetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EventTargetsInner from a JSON string
event_targets_inner_instance = EventTargetsInner.from_json(json)
# print the JSON string representation of the object
print(EventTargetsInner.to_json())

# convert the object into a dict
event_targets_inner_dict = event_targets_inner_instance.to_dict()
# create an instance of EventTargetsInner from a dict
event_targets_inner_from_dict = EventTargetsInner.from_dict(event_targets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


