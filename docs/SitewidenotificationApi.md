# openapi_client.SitewidenotificationApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sitewidenotification_get**](SitewidenotificationApi.md#sitewidenotification_get) | **GET** /sitewidenotification | Get a sitewidenotification
[**sitewidenotification_id_get**](SitewidenotificationApi.md#sitewidenotification_id_get) | **GET** /sitewidenotification/{id} | Get a sitewidenotification by id


# **sitewidenotification_get**
> SitewidenotificationSchema sitewidenotification_get()

Get a sitewidenotification

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.sitewidenotification_schema import SitewidenotificationSchema
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
    api_instance = openapi_client.SitewidenotificationApi(api_client)

    try:
        # Get a sitewidenotification
        api_response = api_instance.sitewidenotification_get()
        print("The response of SitewidenotificationApi->sitewidenotification_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitewidenotificationApi->sitewidenotification_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SitewidenotificationSchema**](SitewidenotificationSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sitewidenotification_id_get**
> SitewidenotificationSchema sitewidenotification_id_get(id)

Get a sitewidenotification by id

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.sitewidenotification_schema import SitewidenotificationSchema
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
    api_instance = openapi_client.SitewidenotificationApi(api_client)
    id = 1 # int | The id of the sitewidenotification to get

    try:
        # Get a sitewidenotification by id
        api_response = api_instance.sitewidenotification_id_get(id)
        print("The response of SitewidenotificationApi->sitewidenotification_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitewidenotificationApi->sitewidenotification_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the sitewidenotification to get | 

### Return type

[**SitewidenotificationSchema**](SitewidenotificationSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

