# openapi_client.MessageApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**messages_post**](MessageApi.md#messages_post) | **POST** /messages | Create a new message to share a thing


# **messages_post**
> MessagesPost200Response messages_post(messages_post_request=messages_post_request)

Create a new message to share a thing

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.messages_post200_response import MessagesPost200Response
from openapi_client.models.messages_post_request import MessagesPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thingiverse.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.thingiverse.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MessageApi(api_client)
    messages_post_request = openapi_client.MessagesPostRequest() # MessagesPostRequest |  (optional)

    try:
        # Create a new message to share a thing
        api_response = api_instance.messages_post(messages_post_request=messages_post_request)
        print("The response of MessageApi->messages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessageApi->messages_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **messages_post_request** | [**MessagesPostRequest**](MessagesPostRequest.md)|  | [optional] 

### Return type

[**MessagesPost200Response**](MessagesPost200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The id of newly created message |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |
**400** | Server cannot or will not process the request due to something that is perceived to be a client error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

