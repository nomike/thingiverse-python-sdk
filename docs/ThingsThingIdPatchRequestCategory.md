# ThingsThingIdPatchRequestCategory

Replace the category of the thing with an category id. This field also supports the old way of providing the full category name (eg. \"3D Printer Parts\") as string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openapi_client.models.things_thing_id_patch_request_category import ThingsThingIdPatchRequestCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ThingsThingIdPatchRequestCategory from a JSON string
things_thing_id_patch_request_category_instance = ThingsThingIdPatchRequestCategory.from_json(json)
# print the JSON string representation of the object
print(ThingsThingIdPatchRequestCategory.to_json())

# convert the object into a dict
things_thing_id_patch_request_category_dict = things_thing_id_patch_request_category_instance.to_dict()
# create an instance of ThingsThingIdPatchRequestCategory from a dict
things_thing_id_patch_request_category_from_dict = ThingsThingIdPatchRequestCategory.from_dict(things_thing_id_patch_request_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


