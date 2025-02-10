# openapi_client.ThingApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**things0_random_get**](ThingApi.md#things0_random_get) | **GET** /things/0/random | Get 5 random things with minimal 1000 likes
[**things_post**](ThingApi.md#things_post) | **POST** /things/ | Create a new thing
[**things_thing_id_ancestors_get**](ThingApi.md#things_thing_id_ancestors_get) | **GET** /things/{thing_id}/ancestors | Get a list of thing ancestors
[**things_thing_id_categories_get**](ThingApi.md#things_thing_id_categories_get) | **GET** /things/{thing_id}/categories | Get thing category
[**things_thing_id_collections_delete**](ThingApi.md#things_thing_id_collections_delete) | **DELETE** /things/{thing_id}/collections | Delete a thing from all user&#39;s collections
[**things_thing_id_comments_get**](ThingApi.md#things_thing_id_comments_get) | **GET** /things/{thing_id}/comments | Get an unthreaded paginated list of comment objects
[**things_thing_id_comments_post**](ThingApi.md#things_thing_id_comments_post) | **POST** /things/{thing_id}/comments | Post a comment
[**things_thing_id_copies_get**](ThingApi.md#things_thing_id_copies_get) | **GET** /things/{thing_id}/copies | Get copies/makes of a thing
[**things_thing_id_copies_post**](ThingApi.md#things_thing_id_copies_post) | **POST** /things/{thing_id}/copies | Upload image for new copy
[**things_thing_id_delete**](ThingApi.md#things_thing_id_delete) | **DELETE** /things/{thing_id} | Delete a thing
[**things_thing_id_derivatives_get**](ThingApi.md#things_thing_id_derivatives_get) | **GET** /things/{thing_id}/derivatives | Get a list of thing derivatives
[**things_thing_id_files_file_id_delete**](ThingApi.md#things_thing_id_files_file_id_delete) | **DELETE** /things/{thing_id}/files/{file_id} | Delete a file from a thing
[**things_thing_id_files_file_id_get**](ThingApi.md#things_thing_id_files_file_id_get) | **GET** /things/{thing_id}/files/{file_id} | Get file by thing
[**things_thing_id_files_get**](ThingApi.md#things_thing_id_files_get) | **GET** /things/{thing_id}/files | Get files by thing
[**things_thing_id_get**](ThingApi.md#things_thing_id_get) | **GET** /things/{thing_id} | Get thing by id
[**things_thing_id_images_get**](ThingApi.md#things_thing_id_images_get) | **GET** /things/{thing_id}/images | Get image(s) by thing
[**things_thing_id_images_image_id_delete**](ThingApi.md#things_thing_id_images_image_id_delete) | **DELETE** /things/{thing_id}/images/{image_id} | Delete an image from a thing
[**things_thing_id_images_image_id_get**](ThingApi.md#things_thing_id_images_image_id_get) | **GET** /things/{thing_id}/images/{image_id} | Get image(s) by thing
[**things_thing_id_images_image_id_patch**](ThingApi.md#things_thing_id_images_image_id_patch) | **PATCH** /things/{thing_id}/images/{image_id} | Update an existing image
[**things_thing_id_likes_delete**](ThingApi.md#things_thing_id_likes_delete) | **DELETE** /things/{thing_id}/likes | Delete a like
[**things_thing_id_likes_get**](ThingApi.md#things_thing_id_likes_get) | **GET** /things/{thing_id}/likes | Get users who liked this thing
[**things_thing_id_likes_post**](ThingApi.md#things_thing_id_likes_post) | **POST** /things/{thing_id}/likes | Like a thing
[**things_thing_id_patch**](ThingApi.md#things_thing_id_patch) | **PATCH** /things/{thing_id} | Update an existing thing
[**things_thing_id_prints_get**](ThingApi.md#things_thing_id_prints_get) | **GET** /things/{thing_id}/prints | Get a list of prints associated with a thing
[**things_thing_id_publish_post**](ThingApi.md#things_thing_id_publish_post) | **POST** /things/{thing_id}/publish | Publish a thing
[**things_thing_id_root_comments_get**](ThingApi.md#things_thing_id_root_comments_get) | **GET** /things/{thing_id}/root-comments | Get an unthreaded paginated list of root comment objects
[**things_thing_id_tags_get**](ThingApi.md#things_thing_id_tags_get) | **GET** /things/{thing_id}/tags | Get tags on this thing
[**things_thing_id_threaded_comments_get**](ThingApi.md#things_thing_id_threaded_comments_get) | **GET** /things/{thing_id}/threaded-comments | Get all comments for this thing in a quick pre-threaded view
[**things_thing_id_toggle_watch_post**](ThingApi.md#things_thing_id_toggle_watch_post) | **POST** /things/{thing_id}/toggle-watch | Watch/unwatch a Thing


# **things0_random_get**
> List[str] things0_random_get()

Get 5 random things with minimal 1000 likes

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
    api_instance = openapi_client.ThingApi(api_client)

    try:
        # Get 5 random things with minimal 1000 likes
        api_response = api_instance.things0_random_get()
        print("The response of ThingApi->things0_random_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things0_random_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The thing id&#39;s of the random things |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_post**
> ThingSchema things_post(things_post_request=things_post_request)

Create a new thing

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.thing_schema import ThingSchema
from openapi_client.models.things_post_request import ThingsPostRequest
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
    api_instance = openapi_client.ThingApi(api_client)
    things_post_request = openapi_client.ThingsPostRequest() # ThingsPostRequest |  (optional)

    try:
        # Create a new thing
        api_response = api_instance.things_post(things_post_request=things_post_request)
        print("The response of ThingApi->things_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **things_post_request** | [**ThingsPostRequest**](ThingsPostRequest.md)|  | [optional] 

### Return type

[**ThingSchema**](ThingSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly created thing. |  -  |
**400** | Server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_ancestors_get**
> List[ThingSchema] things_thing_id_ancestors_get(thing_id)

Get a list of thing ancestors

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Get a list of thing ancestors
        api_response = api_instance.things_thing_id_ancestors_get(thing_id)
        print("The response of ThingApi->things_thing_id_ancestors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_ancestors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

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
**200** | An array containing a list of things this thing is derived from |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_categories_get**
> List[str] things_thing_id_categories_get(thing_id)

Get thing category

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Get thing category
        api_response = api_instance.things_thing_id_categories_get(thing_id)
        print("The response of ThingApi->things_thing_id_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array containing a list of categories this thing is in |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_collections_delete**
> ThingsThingIdDelete200Response things_thing_id_collections_delete(thing_id)

Delete a thing from all user's collections

This cannot be undone.

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Delete a thing from all user's collections
        api_response = api_instance.things_thing_id_collections_delete(thing_id)
        print("The response of ThingApi->things_thing_id_collections_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_collections_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

[**ThingsThingIdDelete200Response**](ThingsThingIdDelete200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_comments_get**
> List[str] things_thing_id_comments_get(thing_id)

Get an unthreaded paginated list of comment objects

See also GET /things/id/threaded_comments

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Get an unthreaded paginated list of comment objects
        api_response = api_instance.things_thing_id_comments_get(thing_id)
        print("The response of ThingApi->things_thing_id_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array containing a list of comments on this thing |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_comments_post**
> object things_thing_id_comments_post(thing_id, things_thing_id_comments_post_request=things_thing_id_comments_post_request)

Post a comment

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.things_thing_id_comments_post_request import ThingsThingIdCommentsPostRequest
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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected
    things_thing_id_comments_post_request = openapi_client.ThingsThingIdCommentsPostRequest() # ThingsThingIdCommentsPostRequest |  (optional)

    try:
        # Post a comment
        api_response = api_instance.things_thing_id_comments_post(thing_id, things_thing_id_comments_post_request=things_thing_id_comments_post_request)
        print("The response of ThingApi->things_thing_id_comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 
 **things_thing_id_comments_post_request** | [**ThingsThingIdCommentsPostRequest**](ThingsThingIdCommentsPostRequest.md)|  | [optional] 

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
**200** | The newly created comment |  -  |
**400** | Server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_copies_get**
> List[str] things_thing_id_copies_get(thing_id, page=page, per_page=per_page)

Get copies/makes of a thing

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get copies/makes of a thing
        api_response = api_instance.things_thing_id_copies_get(thing_id, page=page, per_page=per_page)
        print("The response of ThingApi->things_thing_id_copies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_copies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of copies (and their images) associated with a thing |  * total-count - How many results in total does this have. Note that this can be higher than the results you got. In that case you can use the page query to get the others. <br>  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_copies_post**
> ThingsPost401Response things_thing_id_copies_post(thing_id, things_thing_id_copies_post_request=things_thing_id_copies_post_request)

Upload image for new copy

The data needed to upload this copy's image file via an HTTP POST with multipart/form-data encoding.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.things_post401_response import ThingsPost401Response
from openapi_client.models.things_thing_id_copies_post_request import ThingsThingIdCopiesPostRequest
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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected
    things_thing_id_copies_post_request = openapi_client.ThingsThingIdCopiesPostRequest() # ThingsThingIdCopiesPostRequest |  (optional)

    try:
        # Upload image for new copy
        api_response = api_instance.things_thing_id_copies_post(thing_id, things_thing_id_copies_post_request=things_thing_id_copies_post_request)
        print("The response of ThingApi->things_thing_id_copies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_copies_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 
 **things_thing_id_copies_post_request** | [**ThingsThingIdCopiesPostRequest**](ThingsThingIdCopiesPostRequest.md)|  | [optional] 

### Return type

[**ThingsPost401Response**](ThingsPost401Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_delete**
> ThingsThingIdDelete200Response things_thing_id_delete(thing_id)

Delete a thing

This cannot be undone.

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Delete a thing
        api_response = api_instance.things_thing_id_delete(thing_id)
        print("The response of ThingApi->things_thing_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

[**ThingsThingIdDelete200Response**](ThingsThingIdDelete200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_derivatives_get**
> List[ThingSchema] things_thing_id_derivatives_get(thing_id, page=page, per_page=per_page)

Get a list of thing derivatives

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get a list of thing derivatives
        api_response = api_instance.things_thing_id_derivatives_get(thing_id, page=page, per_page=per_page)
        print("The response of ThingApi->things_thing_id_derivatives_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_derivatives_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 

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
**200** | An array containing a list of things that derive from this thing |  * total-count - How many results in total does this have. Note that this can be higher than the results you got. In that case you can use the page query to get the others. <br>  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_files_file_id_delete**
> ThingsThingIdDelete200Response things_thing_id_files_file_id_delete(thing_id, file_id)

Delete a file from a thing

This cannot be undone.

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected
    file_id = 56 # int | The id of the file to delete

    try:
        # Delete a file from a thing
        api_response = api_instance.things_thing_id_files_file_id_delete(thing_id, file_id)
        print("The response of ThingApi->things_thing_id_files_file_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_files_file_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 
 **file_id** | **int**| The id of the file to delete | 

### Return type

[**ThingsThingIdDelete200Response**](ThingsThingIdDelete200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_files_file_id_get**
> FileSchema things_thing_id_files_file_id_get(thing_id, file_id=file_id)

Get file by thing

Gets more detailed info about a specific file belonging to this thing.

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected
    file_id = 56 # int | Optional id of the file to get more details for (optional)

    try:
        # Get file by thing
        api_response = api_instance.things_thing_id_files_file_id_get(thing_id, file_id=file_id)
        print("The response of ThingApi->things_thing_id_files_file_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_files_file_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 
 **file_id** | **int**| Optional id of the file to get more details for | [optional] 

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
**200** | The details about the specific file |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_files_get**
> List[FileSchema] things_thing_id_files_get(thing_id, file_id=file_id)

Get files by thing

Get a list of files associated with a thing or

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected
    file_id = 56 # int | Optional id of the file to get more details for (optional)

    try:
        # Get files by thing
        api_response = api_instance.things_thing_id_files_get(thing_id, file_id=file_id)
        print("The response of ThingApi->things_thing_id_files_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_files_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 
 **file_id** | **int**| Optional id of the file to get more details for | [optional] 

### Return type

[**List[FileSchema]**](FileSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of files associated with a thing or detail about a specific file |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_get**
> ThingSchema things_thing_id_get(thing_id)

Get thing by id

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Get thing by id
        api_response = api_instance.things_thing_id_get(thing_id)
        print("The response of ThingApi->things_thing_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

[**ThingSchema**](ThingSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object representing the thing requested |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_images_get**
> object things_thing_id_images_get(thing_id, size=size, type=type)

Get image(s) by thing

Gets summary information for all images associated with a thing.

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected
    size = 'size_example' # str | Optional size of image to get (optional)
    type = 'type_example' # str | Optional type of image to get. Required if `size` is specified (optional)

    try:
        # Get image(s) by thing
        api_response = api_instance.things_thing_id_images_get(thing_id, size=size, type=type)
        print("The response of ThingApi->things_thing_id_images_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_images_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 
 **size** | **str**| Optional size of image to get | [optional] 
 **type** | **str**| Optional type of image to get. Required if &#x60;size&#x60; is specified | [optional] 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of images associated with a thing |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_images_image_id_delete**
> ThingsThingIdDelete200Response things_thing_id_images_image_id_delete(thing_id, image_id)

Delete an image from a thing

This cannot be undone.

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected
    image_id = 1 # int | The id of the image affected

    try:
        # Delete an image from a thing
        api_response = api_instance.things_thing_id_images_image_id_delete(thing_id, image_id)
        print("The response of ThingApi->things_thing_id_images_image_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_images_image_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 
 **image_id** | **int**| The id of the image affected | 

### Return type

[**ThingsThingIdDelete200Response**](ThingsThingIdDelete200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_images_image_id_get**
> object things_thing_id_images_image_id_get(thing_id, image_id=image_id, size=size, type=type)

Get image(s) by thing

Gets more detailed information about a specific image.

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected
    image_id = 56 # int | Optional id of image to get details for (optional)
    size = 'size_example' # str | Optional size of image to get (optional)
    type = 'type_example' # str | Optional type of image to get. Required if `size` is specified (optional)

    try:
        # Get image(s) by thing
        api_response = api_instance.things_thing_id_images_image_id_get(thing_id, image_id=image_id, size=size, type=type)
        print("The response of ThingApi->things_thing_id_images_image_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_images_image_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 
 **image_id** | **int**| Optional id of image to get details for | [optional] 
 **size** | **str**| Optional size of image to get | [optional] 
 **type** | **str**| Optional type of image to get. Required if &#x60;size&#x60; is specified | [optional] 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed info about a specific image |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_images_image_id_patch**
> ThingsThingIdDelete200Response things_thing_id_images_image_id_patch(thing_id, image_id, things_thing_id_images_image_id_patch_request=things_thing_id_images_image_id_patch_request)

Update an existing image

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.things_thing_id_delete200_response import ThingsThingIdDelete200Response
from openapi_client.models.things_thing_id_images_image_id_patch_request import ThingsThingIdImagesImageIdPatchRequest
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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected
    image_id = 1 # int | The id of the image affected
    things_thing_id_images_image_id_patch_request = openapi_client.ThingsThingIdImagesImageIdPatchRequest() # ThingsThingIdImagesImageIdPatchRequest |  (optional)

    try:
        # Update an existing image
        api_response = api_instance.things_thing_id_images_image_id_patch(thing_id, image_id, things_thing_id_images_image_id_patch_request=things_thing_id_images_image_id_patch_request)
        print("The response of ThingApi->things_thing_id_images_image_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_images_image_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 
 **image_id** | **int**| The id of the image affected | 
 **things_thing_id_images_image_id_patch_request** | [**ThingsThingIdImagesImageIdPatchRequest**](ThingsThingIdImagesImageIdPatchRequest.md)|  | [optional] 

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

# **things_thing_id_likes_delete**
> ThingsThingIdDelete200Response things_thing_id_likes_delete(thing_id)

Delete a like

This cannot be undone.

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Delete a like
        api_response = api_instance.things_thing_id_likes_delete(thing_id)
        print("The response of ThingApi->things_thing_id_likes_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_likes_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

[**ThingsThingIdDelete200Response**](ThingsThingIdDelete200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | if the user is trying to \&quot;unlike\&quot; their own thing |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_likes_get**
> List[str] things_thing_id_likes_get(thing_id)

Get users who liked this thing

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Get users who liked this thing
        api_response = api_instance.things_thing_id_likes_get(thing_id)
        print("The response of ThingApi->things_thing_id_likes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_likes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of users who liked this thing |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_likes_post**
> ThingsThingIdDelete200Response things_thing_id_likes_post(thing_id)

Like a thing

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Like a thing
        api_response = api_instance.things_thing_id_likes_post(thing_id)
        print("The response of ThingApi->things_thing_id_likes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_likes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

[**ThingsThingIdDelete200Response**](ThingsThingIdDelete200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | the user is trying to like their own thing |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_patch**
> object things_thing_id_patch(thing_id, things_thing_id_patch_request=things_thing_id_patch_request)

Update an existing thing

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.things_thing_id_patch_request import ThingsThingIdPatchRequest
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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected
    things_thing_id_patch_request = openapi_client.ThingsThingIdPatchRequest() # ThingsThingIdPatchRequest |  (optional)

    try:
        # Update an existing thing
        api_response = api_instance.things_thing_id_patch(thing_id, things_thing_id_patch_request=things_thing_id_patch_request)
        print("The response of ThingApi->things_thing_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 
 **things_thing_id_patch_request** | [**ThingsThingIdPatchRequest**](ThingsThingIdPatchRequest.md)|  | [optional] 

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
**200** | The updated thing |  -  |
**400** | Server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_prints_get**
> List[str] things_thing_id_prints_get(thing_id)

Get a list of prints associated with a thing

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Get a list of prints associated with a thing
        api_response = api_instance.things_thing_id_prints_get(thing_id)
        print("The response of ThingApi->things_thing_id_prints_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_prints_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of prints associated with a thing |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_publish_post**
> ThingsPost401Response things_thing_id_publish_post(thing_id)

Publish a thing

If the Thing cannot be published (for example, because the Thing's name or description is blank),  returns an HTTP status of 400 Bad Request and a body containing a JSON object of the form: {\"errors\":[\"<%= reason %>\", ...]}  

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.things_post401_response import ThingsPost401Response
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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Publish a thing
        api_response = api_instance.things_thing_id_publish_post(thing_id)
        print("The response of ThingApi->things_thing_id_publish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_publish_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

[**ThingsPost401Response**](ThingsPost401Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_root_comments_get**
> List[str] things_thing_id_root_comments_get(thing_id)

Get an unthreaded paginated list of root comment objects

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Get an unthreaded paginated list of root comment objects
        api_response = api_instance.things_thing_id_root_comments_get(thing_id)
        print("The response of ThingApi->things_thing_id_root_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_root_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array containing a list of root comments on this thing |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_tags_get**
> List[str] things_thing_id_tags_get(thing_id)

Get tags on this thing

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Get tags on this thing
        api_response = api_instance.things_thing_id_tags_get(thing_id)
        print("The response of ThingApi->things_thing_id_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array containing a list of things that derive from this thing |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_threaded_comments_get**
> object things_thing_id_threaded_comments_get(thing_id)

Get all comments for this thing in a quick pre-threaded view

This is an alternative to GET /things/id/comments

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Get all comments for this thing in a quick pre-threaded view
        api_response = api_instance.things_thing_id_threaded_comments_get(thing_id)
        print("The response of ThingApi->things_thing_id_threaded_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_threaded_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing comment threads indexed by comment parent id (blank for top level comments) and users indexed by user id used in those comments |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_thing_id_toggle_watch_post**
> object things_thing_id_toggle_watch_post(thing_id)

Watch/unwatch a Thing

If currently watching the specified Thing, the current user will unwatch the Thing, and vice versa. Only works in user context.

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
    api_instance = openapi_client.ThingApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Watch/unwatch a Thing
        api_response = api_instance.things_thing_id_toggle_watch_post(thing_id)
        print("The response of ThingApi->things_thing_id_toggle_watch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingApi->things_thing_id_toggle_watch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

