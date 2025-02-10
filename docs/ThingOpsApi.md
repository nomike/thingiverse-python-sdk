# openapi_client.ThingOpsApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**thingops_ids_copy_post**](ThingOpsApi.md#thingops_ids_copy_post) | **POST** /thingops/{ids}/copy | Copy a thing(s) to a new collection
[**thingops_ids_move_post**](ThingOpsApi.md#thingops_ids_move_post) | **POST** /thingops/{ids}/move | Move a thing(s) to a new collection
[**thingops_ids_remove_post**](ThingOpsApi.md#thingops_ids_remove_post) | **POST** /thingops/{ids}/remove | Remove a thing(s) from a collection


# **thingops_ids_copy_post**
> ThingopsIdsMovePost200Response thingops_ids_copy_post(ids, thingops_ids_copy_post_request=thingops_ids_copy_post_request)

Copy a thing(s) to a new collection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.thingops_ids_copy_post_request import ThingopsIdsCopyPostRequest
from openapi_client.models.thingops_ids_move_post200_response import ThingopsIdsMovePost200Response
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
    api_instance = openapi_client.ThingOpsApi(api_client)
    ids = '2' # str | The ids of the thing(s) to copy
    thingops_ids_copy_post_request = openapi_client.ThingopsIdsCopyPostRequest() # ThingopsIdsCopyPostRequest |  (optional)

    try:
        # Copy a thing(s) to a new collection
        api_response = api_instance.thingops_ids_copy_post(ids, thingops_ids_copy_post_request=thingops_ids_copy_post_request)
        print("The response of ThingOpsApi->thingops_ids_copy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingOpsApi->thingops_ids_copy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| The ids of the thing(s) to copy | 
 **thingops_ids_copy_post_request** | [**ThingopsIdsCopyPostRequest**](ThingopsIdsCopyPostRequest.md)|  | [optional] 

### Return type

[**ThingopsIdsMovePost200Response**](ThingopsIdsMovePost200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of Thing ids |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thingops_ids_move_post**
> ThingopsIdsMovePost200Response thingops_ids_move_post(ids, thingops_ids_move_post_request=thingops_ids_move_post_request)

Move a thing(s) to a new collection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.thingops_ids_move_post200_response import ThingopsIdsMovePost200Response
from openapi_client.models.thingops_ids_move_post_request import ThingopsIdsMovePostRequest
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
    api_instance = openapi_client.ThingOpsApi(api_client)
    ids = '2' # str | The ids of the thing(s) to move
    thingops_ids_move_post_request = openapi_client.ThingopsIdsMovePostRequest() # ThingopsIdsMovePostRequest |  (optional)

    try:
        # Move a thing(s) to a new collection
        api_response = api_instance.thingops_ids_move_post(ids, thingops_ids_move_post_request=thingops_ids_move_post_request)
        print("The response of ThingOpsApi->thingops_ids_move_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingOpsApi->thingops_ids_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| The ids of the thing(s) to move | 
 **thingops_ids_move_post_request** | [**ThingopsIdsMovePostRequest**](ThingopsIdsMovePostRequest.md)|  | [optional] 

### Return type

[**ThingopsIdsMovePost200Response**](ThingopsIdsMovePost200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of Thing ids |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thingops_ids_remove_post**
> ThingopsIdsMovePost200Response thingops_ids_remove_post(ids, thingops_ids_remove_post_request=thingops_ids_remove_post_request)

Remove a thing(s) from a collection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.thingops_ids_move_post200_response import ThingopsIdsMovePost200Response
from openapi_client.models.thingops_ids_remove_post_request import ThingopsIdsRemovePostRequest
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
    api_instance = openapi_client.ThingOpsApi(api_client)
    ids = '2' # str | The ids of the thing(s) to remove
    thingops_ids_remove_post_request = openapi_client.ThingopsIdsRemovePostRequest() # ThingopsIdsRemovePostRequest |  (optional)

    try:
        # Remove a thing(s) from a collection
        api_response = api_instance.thingops_ids_remove_post(ids, thingops_ids_remove_post_request=thingops_ids_remove_post_request)
        print("The response of ThingOpsApi->thingops_ids_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingOpsApi->thingops_ids_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| The ids of the thing(s) to remove | 
 **thingops_ids_remove_post_request** | [**ThingopsIdsRemovePostRequest**](ThingopsIdsRemovePostRequest.md)|  | [optional] 

### Return type

[**ThingopsIdsMovePost200Response**](ThingopsIdsMovePost200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of Thing ids |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

