# ProgramSchemaBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.program_schema_body import ProgramSchemaBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramSchemaBody from a JSON string
program_schema_body_instance = ProgramSchemaBody.from_json(json)
# print the JSON string representation of the object
print(ProgramSchemaBody.to_json())

# convert the object into a dict
program_schema_body_dict = program_schema_body_instance.to_dict()
# create an instance of ProgramSchemaBody from a dict
program_schema_body_from_dict = ProgramSchemaBody.from_dict(program_schema_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


