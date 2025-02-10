# ThingsThingIdCommentsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Set the body of the reply | 
**recaptcha_token** | **str** | Set the recaptcha token to confirm that the user is not a bot | 

## Example

```python
from openapi_client.models.things_thing_id_comments_post_request import ThingsThingIdCommentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ThingsThingIdCommentsPostRequest from a JSON string
things_thing_id_comments_post_request_instance = ThingsThingIdCommentsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ThingsThingIdCommentsPostRequest.to_json())

# convert the object into a dict
things_thing_id_comments_post_request_dict = things_thing_id_comments_post_request_instance.to_dict()
# create an instance of ThingsThingIdCommentsPostRequest from a dict
things_thing_id_comments_post_request_from_dict = ThingsThingIdCommentsPostRequest.from_dict(things_thing_id_comments_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


