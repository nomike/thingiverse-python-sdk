# UrlSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**pathname** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**search** | **str** |  | [optional] 
**slashes** | **bool** |  | [optional] 
**port** | [**UrlSchemaPort**](UrlSchemaPort.md) |  | [optional] 
**query** | [**UrlSchemaQuery**](UrlSchemaQuery.md) |  | [optional] 

## Example

```python
from openapi_client.models.url_schema import UrlSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UrlSchema from a JSON string
url_schema_instance = UrlSchema.from_json(json)
# print the JSON string representation of the object
print(UrlSchema.to_json())

# convert the object into a dict
url_schema_dict = url_schema_instance.to_dict()
# create an instance of UrlSchema from a dict
url_schema_from_dict = UrlSchema.from_dict(url_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


