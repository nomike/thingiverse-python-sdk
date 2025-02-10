# openapi_client.EmailApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_post**](EmailApi.md#email_post) | **POST** /email | Queuing emails
[**email_thingiverse_enqueue_support_post**](EmailApi.md#email_thingiverse_enqueue_support_post) | **POST** /email/thingiverse/enqueue-support | Queue email to Thingiverse support
[**email_type_enqueue_dmca_post**](EmailApi.md#email_type_enqueue_dmca_post) | **POST** /email/{type}/enqueue-dmca | Queue email to Thingiverse support (DMCA)


# **email_post**
> EmailSchema email_post(email_post_request=email_post_request)

Queuing emails

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.email_post_request import EmailPostRequest
from openapi_client.models.email_schema import EmailSchema
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
    api_instance = openapi_client.EmailApi(api_client)
    email_post_request = openapi_client.EmailPostRequest() # EmailPostRequest |  (optional)

    try:
        # Queuing emails
        api_response = api_instance.email_post(email_post_request=email_post_request)
        print("The response of EmailApi->email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_post_request** | [**EmailPostRequest**](EmailPostRequest.md)|  | [optional] 

### Return type

[**EmailSchema**](EmailSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_thingiverse_enqueue_support_post**
> object email_thingiverse_enqueue_support_post(email_thingiverse_enqueue_support_post_request=email_thingiverse_enqueue_support_post_request)

Queue email to Thingiverse support

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.email_thingiverse_enqueue_support_post_request import EmailThingiverseEnqueueSupportPostRequest
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
    api_instance = openapi_client.EmailApi(api_client)
    email_thingiverse_enqueue_support_post_request = openapi_client.EmailThingiverseEnqueueSupportPostRequest() # EmailThingiverseEnqueueSupportPostRequest |  (optional)

    try:
        # Queue email to Thingiverse support
        api_response = api_instance.email_thingiverse_enqueue_support_post(email_thingiverse_enqueue_support_post_request=email_thingiverse_enqueue_support_post_request)
        print("The response of EmailApi->email_thingiverse_enqueue_support_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_thingiverse_enqueue_support_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_thingiverse_enqueue_support_post_request** | [**EmailThingiverseEnqueueSupportPostRequest**](EmailThingiverseEnqueueSupportPostRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_type_enqueue_dmca_post**
> ThingsThingIdDelete200Response email_type_enqueue_dmca_post(type, email_type_enqueue_dmca_post_request=email_type_enqueue_dmca_post_request)

Queue email to Thingiverse support (DMCA)

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.email_type_enqueue_dmca_post_request import EmailTypeEnqueueDmcaPostRequest
from openapi_client.models.things_thing_id_delete200_response import ThingsThingIdDelete200Response
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
    api_instance = openapi_client.EmailApi(api_client)
    type = 'type_example' # str | The type of message, in order to determine which address to send the message
    email_type_enqueue_dmca_post_request = openapi_client.EmailTypeEnqueueDmcaPostRequest() # EmailTypeEnqueueDmcaPostRequest |  (optional)

    try:
        # Queue email to Thingiverse support (DMCA)
        api_response = api_instance.email_type_enqueue_dmca_post(type, email_type_enqueue_dmca_post_request=email_type_enqueue_dmca_post_request)
        print("The response of EmailApi->email_type_enqueue_dmca_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_type_enqueue_dmca_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of message, in order to determine which address to send the message | 
 **email_type_enqueue_dmca_post_request** | [**EmailTypeEnqueueDmcaPostRequest**](EmailTypeEnqueueDmcaPostRequest.md)|  | [optional] 

### Return type

[**ThingsThingIdDelete200Response**](ThingsThingIdDelete200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

