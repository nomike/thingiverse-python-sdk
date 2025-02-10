# openapi_client.ChangelogApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changelogs_get**](ChangelogApi.md#changelogs_get) | **GET** /changelogs | Get changelogs


# **changelogs_get**
> List[ChangelogSchema] changelogs_get()

Get changelogs

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.changelog_schema import ChangelogSchema
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
    api_instance = openapi_client.ChangelogApi(api_client)

    try:
        # Get changelogs
        api_response = api_instance.changelogs_get()
        print("The response of ChangelogApi->changelogs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChangelogApi->changelogs_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ChangelogSchema]**](ChangelogSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list representing the Changelog |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

