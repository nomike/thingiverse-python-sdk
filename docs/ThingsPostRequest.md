# ThingsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Set the name of the thing | 
**license** | **str** | One of cc, cc-sa, cc-nd, cc-nc-sa, cc-nc-nd, pd0, gpl, lgpl, bsd. Set license. | 
**category** | **str** | Set the category of the thing. Uses full category name (eg. \&quot;3D Printer Parts\&quot;) | 
**description** | **str** | Set the description. | [optional] 
**instructions** | **str** | Set the instructions. | [optional] 
**is_wip** | **bool** | Toggle whether this thing is a work in progress. Default is false. | [optional] 
**tags** | **List[str]** | An array of strings containing tag names. Sets all current tags. | [optional] 
**ancestors** | **List[int]** | An array of thing ids that this thing is derived from. | [optional] 
**is_remix** | **bool** | Is this thing remixed from another thing | [optional] 

## Example

```python
from openapi_client.models.things_post_request import ThingsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ThingsPostRequest from a JSON string
things_post_request_instance = ThingsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ThingsPostRequest.to_json())

# convert the object into a dict
things_post_request_dict = things_post_request_instance.to_dict()
# create an instance of ThingsPostRequest from a dict
things_post_request_from_dict = ThingsPostRequest.from_dict(things_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


