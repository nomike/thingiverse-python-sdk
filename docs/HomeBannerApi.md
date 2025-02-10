# openapi_client.HomeBannerApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**homebanner_get**](HomeBannerApi.md#homebanner_get) | **GET** /homebanner | Get the banner on the home page


# **homebanner_get**
> HomebannerSchema homebanner_get()

Get the banner on the home page

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.homebanner_schema import HomebannerSchema
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
    api_instance = openapi_client.HomeBannerApi(api_client)

    try:
        # Get the banner on the home page
        api_response = api_instance.homebanner_get()
        print("The response of HomeBannerApi->homebanner_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HomeBannerApi->homebanner_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HomebannerSchema**](HomebannerSchema.md)

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

