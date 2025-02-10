# GrouptopicsGrouptopicIdUpdatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Set the name of the topic | [optional] 
**body** | **str** | Set the body of the topic | [optional] 
**tags** | **List[str]** | Set the category of the thing. Uses full category name (eg. \&quot;3D Printer Parts\&quot;) | [optional] 
**filenames** | **List[str]** | Array of names of the files | [optional] 
**files** | **List[str]** | Array of files | [optional] 
**attachments** | **List[str]** | Array of atachments ids to update | [optional] 

## Example

```python
from openapi_client.models.grouptopics_grouptopic_id_update_post_request import GrouptopicsGrouptopicIdUpdatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GrouptopicsGrouptopicIdUpdatePostRequest from a JSON string
grouptopics_grouptopic_id_update_post_request_instance = GrouptopicsGrouptopicIdUpdatePostRequest.from_json(json)
# print the JSON string representation of the object
print(GrouptopicsGrouptopicIdUpdatePostRequest.to_json())

# convert the object into a dict
grouptopics_grouptopic_id_update_post_request_dict = grouptopics_grouptopic_id_update_post_request_instance.to_dict()
# create an instance of GrouptopicsGrouptopicIdUpdatePostRequest from a dict
grouptopics_grouptopic_id_update_post_request_from_dict = GrouptopicsGrouptopicIdUpdatePostRequest.from_dict(grouptopics_grouptopic_id_update_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


