# openapi_client.DeprecatedApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**featured_get**](DeprecatedApi.md#featured_get) | **GET** /featured | Get the list of featured things
[**files0_finalize_files_post**](DeprecatedApi.md#files0_finalize_files_post) | **POST** /files/0/FinalizeFiles | Finalize multiple uploaded files. DEPRECATED, use FinalizeFiles endpoint instead
[**files_file_id_finalize_get**](DeprecatedApi.md#files_file_id_finalize_get) | **GET** /files/{file_id}/finalize | Finalize an uploaded file. DEPRECATED.
[**files_file_id_finalize_post**](DeprecatedApi.md#files_file_id_finalize_post) | **POST** /files/{file_id}/finalize | Finalize an uploaded file. DEPRECATED, use FinalizeFiles endpoint instead
[**newest_get**](DeprecatedApi.md#newest_get) | **GET** /newest | Get a list of the latest things
[**popular_get**](DeprecatedApi.md#popular_get) | **GET** /popular | Get the most popular things


# **featured_get**
> List[FeaturedSchema] featured_get(page=page, per_page=per_page)

Get the list of featured things

You can use `GET /search` with the `is_featured=1` parameter now.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.featured_schema import FeaturedSchema
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
    api_instance = openapi_client.DeprecatedApi(api_client)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get the list of featured things
        api_response = api_instance.featured_get(page=page, per_page=per_page)
        print("The response of DeprecatedApi->featured_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->featured_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 

### Return type

[**List[FeaturedSchema]**](FeaturedSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of featured things |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files0_finalize_files_post**
> ThingsThingIdDelete200Response files0_finalize_files_post(body=body)

Finalize multiple uploaded files. DEPRECATED, use FinalizeFiles endpoint instead

Finalize multiple \"pendingUploads\" at once by associating them with something (Thing/make/comment). In order to use this, you will need to first use the uploadFile endpoint

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
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
    api_instance = openapi_client.DeprecatedApi(api_client)
    body = None # object |  (optional)

    try:
        # Finalize multiple uploaded files. DEPRECATED, use FinalizeFiles endpoint instead
        api_response = api_instance.files0_finalize_files_post(body=body)
        print("The response of DeprecatedApi->files0_finalize_files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->files0_finalize_files_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | [optional] 

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
**400** | Server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_file_id_finalize_get**
> files_file_id_finalize_get(file_id)

Finalize an uploaded file. DEPRECATED.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
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
    api_instance = openapi_client.DeprecatedApi(api_client)
    file_id = 1 # int | The id of the file

    try:
        # Finalize an uploaded file. DEPRECATED.
        api_instance.files_file_id_finalize_get(file_id)
    except Exception as e:
        print("Exception when calling DeprecatedApi->files_file_id_finalize_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The id of the file | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | None |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_file_id_finalize_post**
> FileSchema files_file_id_finalize_post(file_id)

Finalize an uploaded file. DEPRECATED, use FinalizeFiles endpoint instead

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.file_schema import FileSchema
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
    api_instance = openapi_client.DeprecatedApi(api_client)
    file_id = 1 # int | The id of the file

    try:
        # Finalize an uploaded file. DEPRECATED, use FinalizeFiles endpoint instead
        api_response = api_instance.files_file_id_finalize_post(file_id)
        print("The response of DeprecatedApi->files_file_id_finalize_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->files_file_id_finalize_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The id of the file | 

### Return type

[**FileSchema**](FileSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary of the ObjectFile or Image that was created |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **newest_get**
> List[ShortThingSchema] newest_get(page=page, per_page=per_page)

Get a list of the latest things

You can use `GET /search` with the `sort=newest` parameter now.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.short_thing_schema import ShortThingSchema
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
    api_instance = openapi_client.DeprecatedApi(api_client)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get a list of the latest things
        api_response = api_instance.newest_get(page=page, per_page=per_page)
        print("The response of DeprecatedApi->newest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->newest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 

### Return type

[**List[ShortThingSchema]**](ShortThingSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of the latest things |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **popular_get**
> List[ShortThingSchema] popular_get(page=page, per_page=per_page)

Get the most popular things

You can use `GET /search` with the `sort=popular` parameter now.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.short_thing_schema import ShortThingSchema
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
    api_instance = openapi_client.DeprecatedApi(api_client)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get the most popular things
        api_response = api_instance.popular_get(page=page, per_page=per_page)
        print("The response of DeprecatedApi->popular_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->popular_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 

### Return type

[**List[ShortThingSchema]**](ShortThingSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of popular things |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

