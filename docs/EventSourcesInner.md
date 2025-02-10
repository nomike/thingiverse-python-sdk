# EventSourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbnail** | **str** |  | [optional] 
**default_image** | [**ImageSummarySchema**](ImageSummarySchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.event_sources_inner import EventSourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of EventSourcesInner from a JSON string
event_sources_inner_instance = EventSourcesInner.from_json(json)
# print the JSON string representation of the object
print(EventSourcesInner.to_json())

# convert the object into a dict
event_sources_inner_dict = event_sources_inner_instance.to_dict()
# create an instance of EventSourcesInner from a dict
event_sources_inner_from_dict = EventSourcesInner.from_dict(event_sources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


