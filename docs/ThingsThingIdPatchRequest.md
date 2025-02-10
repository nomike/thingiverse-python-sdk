# ThingsThingIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Replace the name of the thing | [optional] 
**license** | **str** | One of cc, cc-sa, cc-nd, cc-nc-sa, cc-nc-nd, pd0, gpl, lgpl, bsd. Replace license | [optional] 
**category** | [**ThingsThingIdPatchRequestCategory**](ThingsThingIdPatchRequestCategory.md) |  | [optional] 
**description** | **str** | Replace the description. | [optional] 
**instructions** | **str** | Replace the instructions. | [optional] 
**is_wip** | **bool** | Toggle whether this thing is a work in progress. | [optional] 
**tags** | **List[str]** | An array of strings containing tag names. Replaces all current tags. | [optional] 
**ancestors** | **List[str]** | array of id&#39;s of all things that this was remixed from. Note that is_remix should be set to true as well | [optional] 
**is_remix** | **bool** | Is this thing remixed from another thing | [optional] 

## Example

```python
from openapi_client.models.things_thing_id_patch_request import ThingsThingIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ThingsThingIdPatchRequest from a JSON string
things_thing_id_patch_request_instance = ThingsThingIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ThingsThingIdPatchRequest.to_json())

# convert the object into a dict
things_thing_id_patch_request_dict = things_thing_id_patch_request_instance.to_dict()
# create an instance of ThingsThingIdPatchRequest from a dict
things_thing_id_patch_request_from_dict = ThingsThingIdPatchRequest.from_dict(things_thing_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


