# openapi_client.TagApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags0_popular_get**](TagApi.md#tags0_popular_get) | **GET** /tags/0/popular | Get the list of random popular tags.
[**tags_get**](TagApi.md#tags_get) | **GET** /tags/ | Get the list of tags.
[**tags_tag_get**](TagApi.md#tags_tag_get) | **GET** /tags/{tag}/ | Return a representation of the given tag
[**tags_tag_search_tags_get**](TagApi.md#tags_tag_search_tags_get) | **GET** /tags/{tag}/search-tags | Search tags by tag name.
[**tags_tag_things_get**](TagApi.md#tags_tag_things_get) | **GET** /tags/{tag}/things | Get the latest things with the specified tag


# **tags0_popular_get**
> List[TagSchema] tags0_popular_get()

Get the list of random popular tags.

returns a list of popular tags which reset every day.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tag_schema import TagSchema
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
    api_instance = openapi_client.TagApi(api_client)

    try:
        # Get the list of random popular tags.
        api_response = api_instance.tags0_popular_get()
        print("The response of TagApi->tags0_popular_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->tags0_popular_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TagSchema]**](TagSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of tags. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_get**
> List[TagSchema] tags_get()

Get the list of tags.

returns a list of all tags in alphabetical order.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tag_schema import TagSchema
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
    api_instance = openapi_client.TagApi(api_client)

    try:
        # Get the list of tags.
        api_response = api_instance.tags_get()
        print("The response of TagApi->tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->tags_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TagSchema]**](TagSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of tags. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_tag_get**
> TagSchema tags_tag_get(tag)

Return a representation of the given tag

Tags are normalized before searching by converting whitespace to underscores and stripping out all characters except alphanumerics, underscores, and dashes ('-').

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tag_schema import TagSchema
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
    api_instance = openapi_client.TagApi(api_client)
    tag = '3d' # str | The name of the tag affected

    try:
        # Return a representation of the given tag
        api_response = api_instance.tags_tag_get(tag)
        print("The response of TagApi->tags_tag_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->tags_tag_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| The name of the tag affected | 

### Return type

[**TagSchema**](TagSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag objects |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_tag_search_tags_get**
> List[TagsTagSearchTagsGet200ResponseInner] tags_tag_search_tags_get(tag)

Search tags by tag name.

Returns a list of all tags where the search word is included in the name.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tags_tag_search_tags_get200_response_inner import TagsTagSearchTagsGet200ResponseInner
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
    api_instance = openapi_client.TagApi(api_client)
    tag = '3d' # str | The name of the tag affected

    try:
        # Search tags by tag name.
        api_response = api_instance.tags_tag_search_tags_get(tag)
        print("The response of TagApi->tags_tag_search_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->tags_tag_search_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| The name of the tag affected | 

### Return type

[**List[TagsTagSearchTagsGet200ResponseInner]**](TagsTagSearchTagsGet200ResponseInner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of tags. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_tag_things_get**
> List[ThingSchema] tags_tag_things_get(tag)

Get the latest things with the specified tag

Tags are normalized before searching by converting whitespace to underscores and stripping out all characters except alphanumerics, underscores, and dashes ('-').

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.thing_schema import ThingSchema
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
    api_instance = openapi_client.TagApi(api_client)
    tag = '3d' # str | The name of the tag affected

    try:
        # Get the latest things with the specified tag
        api_response = api_instance.tags_tag_things_get(tag)
        print("The response of TagApi->tags_tag_things_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->tags_tag_things_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| The name of the tag affected | 

### Return type

[**List[ThingSchema]**](ThingSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thing objects |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

