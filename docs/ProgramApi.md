# openapi_client.ProgramApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**programs0_all_get**](ProgramApi.md#programs0_all_get) | **GET** /programs/0/all | Get a list of programs


# **programs0_all_get**
> Programs0AllGet200Response programs0_all_get()

Get a list of programs

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.programs0_all_get200_response import Programs0AllGet200Response
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
    api_instance = openapi_client.ProgramApi(api_client)

    try:
        # Get a list of programs
        api_response = api_instance.programs0_all_get()
        print("The response of ProgramApi->programs0_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProgramApi->programs0_all_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Programs0AllGet200Response**](Programs0AllGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

