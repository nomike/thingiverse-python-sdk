# ChangelogSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**highlights** | [**List[ChangelogSchemaHighlightsInner]**](ChangelogSchemaHighlightsInner.md) |  | [optional] 
**features** | **List[str]** |  | [optional] 
**bugfixes** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.changelog_schema import ChangelogSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ChangelogSchema from a JSON string
changelog_schema_instance = ChangelogSchema.from_json(json)
# print the JSON string representation of the object
print(ChangelogSchema.to_json())

# convert the object into a dict
changelog_schema_dict = changelog_schema_instance.to_dict()
# create an instance of ChangelogSchema from a dict
changelog_schema_from_dict = ChangelogSchema.from_dict(changelog_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


