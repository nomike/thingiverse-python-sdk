# SubscriptionsTagSetSubscribeStatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Set the type of action | 
**target_type** | **str** | Set the type of target to which the user will be subscribed | 

## Example

```python
from openapi_client.models.subscriptions_tag_set_subscribe_state_post_request import SubscriptionsTagSetSubscribeStatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionsTagSetSubscribeStatePostRequest from a JSON string
subscriptions_tag_set_subscribe_state_post_request_instance = SubscriptionsTagSetSubscribeStatePostRequest.from_json(json)
# print the JSON string representation of the object
print(SubscriptionsTagSetSubscribeStatePostRequest.to_json())

# convert the object into a dict
subscriptions_tag_set_subscribe_state_post_request_dict = subscriptions_tag_set_subscribe_state_post_request_instance.to_dict()
# create an instance of SubscriptionsTagSetSubscribeStatePostRequest from a dict
subscriptions_tag_set_subscribe_state_post_request_from_dict = SubscriptionsTagSetSubscribeStatePostRequest.from_dict(subscriptions_tag_set_subscribe_state_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


