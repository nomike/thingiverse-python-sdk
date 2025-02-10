# openapi_client.MakeApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copies_copy_id_comments_get**](MakeApi.md#copies_copy_id_comments_get) | **GET** /copies/{copy_id}/comments | Get an unthreaded paginated list of comment objects.
[**copies_copy_id_comments_post**](MakeApi.md#copies_copy_id_comments_post) | **POST** /copies/{copy_id}/comments | Post a comment
[**copies_copy_id_delete**](MakeApi.md#copies_copy_id_delete) | **DELETE** /copies/{copy_id}/ | Softdelete copy by id
[**copies_copy_id_get**](MakeApi.md#copies_copy_id_get) | **GET** /copies/{copy_id}/ | Get make (copy) by id
[**copies_copy_id_images_get**](MakeApi.md#copies_copy_id_images_get) | **GET** /copies/{copy_id}/images | Get images for a copy
[**copies_copy_id_images_image_id_delete**](MakeApi.md#copies_copy_id_images_image_id_delete) | **DELETE** /copies/{copy_id}/images/{image_id} | Delete an image from a copy
[**copies_copy_id_images_image_id_patch**](MakeApi.md#copies_copy_id_images_image_id_patch) | **PATCH** /copies/{copy_id}/images/{image_id} | Update an existing image
[**copies_copy_id_images_post**](MakeApi.md#copies_copy_id_images_post) | **POST** /copies/{copy_id}/images | Upload image to a copy
[**copies_copy_id_likes_delete**](MakeApi.md#copies_copy_id_likes_delete) | **DELETE** /copies/{copy_id}/likes | Delete a like
[**copies_copy_id_likes_post**](MakeApi.md#copies_copy_id_likes_post) | **POST** /copies/{copy_id}/likes | Like a copy
[**copies_copy_id_patch**](MakeApi.md#copies_copy_id_patch) | **PATCH** /copies/{copy_id}/ | Update an existing copy
[**copies_copy_id_restore_post**](MakeApi.md#copies_copy_id_restore_post) | **POST** /copies/{copy_id}/restore | Restore a previously soft-deleted make
[**copies_copy_id_root_comments_get**](MakeApi.md#copies_copy_id_root_comments_get) | **GET** /copies/{copy_id}/root-comments | Get an unthreaded paginated list of root comment objects
[**copies_copy_id_threaded_comments_get**](MakeApi.md#copies_copy_id_threaded_comments_get) | **GET** /copies/{copy_id}/threaded-comments | Get all comments for this copy in a quick pre-threaded view.
[**copies_copy_id_toggle_watch_post**](MakeApi.md#copies_copy_id_toggle_watch_post) | **POST** /copies/{copy_id}/toggle-watch | Watch/unwatch a Make
[**copies_get**](MakeApi.md#copies_get) | **GET** /copies/ | Get the list of latest makes (copies).
[**copiesreturncomplete_get**](MakeApi.md#copiesreturncomplete_get) | **GET** /copies?return&#x3D;complete | Get the list of latest makes (copies). The return complete ensures that the full thinginfo and image info is returned


# **copies_copy_id_comments_get**
> List[MakeCommentSchema] copies_copy_id_comments_get(copy_id)

Get an unthreaded paginated list of comment objects.

See also GET /copies/id/threaded-comments

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.make_comment_schema import MakeCommentSchema
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
    api_instance = openapi_client.MakeApi(api_client)
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id

    try:
        # Get an unthreaded paginated list of comment objects.
        api_response = api_instance.copies_copy_id_comments_get(copy_id)
        print("The response of MakeApi->copies_copy_id_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 

### Return type

[**List[MakeCommentSchema]**](MakeCommentSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array containing a list of comments on this copy |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copies_copy_id_comments_post**
> MakeCommentSchema copies_copy_id_comments_post(copy_id, copies_copy_id_comments_post_request=copies_copy_id_comments_post_request)

Post a comment

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.copies_copy_id_comments_post_request import CopiesCopyIdCommentsPostRequest
from openapi_client.models.make_comment_schema import MakeCommentSchema
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
    api_instance = openapi_client.MakeApi(api_client)
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id
    copies_copy_id_comments_post_request = openapi_client.CopiesCopyIdCommentsPostRequest() # CopiesCopyIdCommentsPostRequest |  (optional)

    try:
        # Post a comment
        api_response = api_instance.copies_copy_id_comments_post(copy_id, copies_copy_id_comments_post_request=copies_copy_id_comments_post_request)
        print("The response of MakeApi->copies_copy_id_comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 
 **copies_copy_id_comments_post_request** | [**CopiesCopyIdCommentsPostRequest**](CopiesCopyIdCommentsPostRequest.md)|  | [optional] 

### Return type

[**MakeCommentSchema**](MakeCommentSchema.md)

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

# **copies_copy_id_delete**
> copies_copy_id_delete(copy_id)

Softdelete copy by id

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
    api_instance = openapi_client.MakeApi(api_client)
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id

    try:
        # Softdelete copy by id
        api_instance.copies_copy_id_delete(copy_id)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 

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

# **copies_copy_id_get**
> CopySchema copies_copy_id_get(copy_id)

Get make (copy) by id

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.copy_schema import CopySchema
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
    api_instance = openapi_client.MakeApi(api_client)
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id

    try:
        # Get make (copy) by id
        api_response = api_instance.copies_copy_id_get(copy_id)
        print("The response of MakeApi->copies_copy_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 

### Return type

[**CopySchema**](CopySchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object representing the copy requested. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copies_copy_id_images_get**
> List[ImageSummarySchema] copies_copy_id_images_get(copy_id)

Get images for a copy

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.image_summary_schema import ImageSummarySchema
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
    api_instance = openapi_client.MakeApi(api_client)
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id

    try:
        # Get images for a copy
        api_response = api_instance.copies_copy_id_images_get(copy_id)
        print("The response of MakeApi->copies_copy_id_images_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_images_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 

### Return type

[**List[ImageSummarySchema]**](ImageSummarySchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of images associated with the copy |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copies_copy_id_images_image_id_delete**
> ThingsThingIdDelete200Response copies_copy_id_images_image_id_delete(copy_id, image_id)

Delete an image from a copy

Must use the DELETE method. This cannot be undone.

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
    api_instance = openapi_client.MakeApi(api_client)
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id
    image_id = 1 # int | The id of the image affected

    try:
        # Delete an image from a copy
        api_response = api_instance.copies_copy_id_images_image_id_delete(copy_id, image_id)
        print("The response of MakeApi->copies_copy_id_images_image_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_images_image_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 
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

# **copies_copy_id_images_image_id_patch**
> ThingsThingIdDelete200Response copies_copy_id_images_image_id_patch(rank, featured, copy_id, image_id)

Update an existing image

Must use the PATCH method

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
    api_instance = openapi_client.MakeApi(api_client)
    rank = 1 # int | 
    featured = True # bool | 
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id
    image_id = 1 # int | The id of the image affected

    try:
        # Update an existing image
        api_response = api_instance.copies_copy_id_images_image_id_patch(rank, featured, copy_id, image_id)
        print("The response of MakeApi->copies_copy_id_images_image_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_images_image_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rank** | **int**|  | 
 **featured** | **bool**|  | 
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 
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

# **copies_copy_id_images_post**
> ImageSummarySchema copies_copy_id_images_post(copy_id, copies_copy_id_images_post_request=copies_copy_id_images_post_request)

Upload image to a copy

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.copies_copy_id_images_post_request import CopiesCopyIdImagesPostRequest
from openapi_client.models.image_summary_schema import ImageSummarySchema
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
    api_instance = openapi_client.MakeApi(api_client)
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id
    copies_copy_id_images_post_request = openapi_client.CopiesCopyIdImagesPostRequest() # CopiesCopyIdImagesPostRequest |  (optional)

    try:
        # Upload image to a copy
        api_response = api_instance.copies_copy_id_images_post(copy_id, copies_copy_id_images_post_request=copies_copy_id_images_post_request)
        print("The response of MakeApi->copies_copy_id_images_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_images_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 
 **copies_copy_id_images_post_request** | [**CopiesCopyIdImagesPostRequest**](CopiesCopyIdImagesPostRequest.md)|  | [optional] 

### Return type

[**ImageSummarySchema**](ImageSummarySchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The data needed to upload this copy&#39;s image file via an HTTP POST with multipart/form-data encoding. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copies_copy_id_likes_delete**
> ThingsThingIdDelete200Response copies_copy_id_likes_delete(copy_id)

Delete a like

Must use the DELETE method Result will be 404 Not Found if the copy doesn't exist. Result will be 400 Bad Request if the user is trying to \"unlike\" their own copy.

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
    api_instance = openapi_client.MakeApi(api_client)
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id

    try:
        # Delete a like
        api_response = api_instance.copies_copy_id_likes_delete(copy_id)
        print("The response of MakeApi->copies_copy_id_likes_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_likes_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 

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
**400** | Server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copies_copy_id_likes_post**
> ThingsThingIdDelete200Response copies_copy_id_likes_post(copy_id)

Like a copy

Must use the POST method Result will be 404 Not Found if the copy doesn't exist. Result will be 400 Bad Request if the user is trying to like their own copy.

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
    api_instance = openapi_client.MakeApi(api_client)
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id

    try:
        # Like a copy
        api_response = api_instance.copies_copy_id_likes_post(copy_id)
        print("The response of MakeApi->copies_copy_id_likes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_likes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 

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
**400** | Server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copies_copy_id_patch**
> CopySchema copies_copy_id_patch(copy_id, copies_copy_id_patch_request=copies_copy_id_patch_request)

Update an existing copy

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.copies_copy_id_patch_request import CopiesCopyIdPatchRequest
from openapi_client.models.copy_schema import CopySchema
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
    api_instance = openapi_client.MakeApi(api_client)
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id
    copies_copy_id_patch_request = openapi_client.CopiesCopyIdPatchRequest() # CopiesCopyIdPatchRequest |  (optional)

    try:
        # Update an existing copy
        api_response = api_instance.copies_copy_id_patch(copy_id, copies_copy_id_patch_request=copies_copy_id_patch_request)
        print("The response of MakeApi->copies_copy_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 
 **copies_copy_id_patch_request** | [**CopiesCopyIdPatchRequest**](CopiesCopyIdPatchRequest.md)|  | [optional] 

### Return type

[**CopySchema**](CopySchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated make. |  -  |
**400** | Server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copies_copy_id_restore_post**
> CopySchema copies_copy_id_restore_post(copy_id)

Restore a previously soft-deleted make

If a make was previously softdeleted (so deleted but not yet permanently), this will restore it.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.copy_schema import CopySchema
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
    api_instance = openapi_client.MakeApi(api_client)
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id

    try:
        # Restore a previously soft-deleted make
        api_response = api_instance.copies_copy_id_restore_post(copy_id)
        print("The response of MakeApi->copies_copy_id_restore_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_restore_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 

### Return type

[**CopySchema**](CopySchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object representing the restored copy |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copies_copy_id_root_comments_get**
> List[MakeCommentSchema] copies_copy_id_root_comments_get(copy_id)

Get an unthreaded paginated list of root comment objects

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.make_comment_schema import MakeCommentSchema
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
    api_instance = openapi_client.MakeApi(api_client)
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id

    try:
        # Get an unthreaded paginated list of root comment objects
        api_response = api_instance.copies_copy_id_root_comments_get(copy_id)
        print("The response of MakeApi->copies_copy_id_root_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_root_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 

### Return type

[**List[MakeCommentSchema]**](MakeCommentSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array containing a list of root comments on this copy |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copies_copy_id_threaded_comments_get**
> CopiesCopyIdThreadedCommentsGet200Response copies_copy_id_threaded_comments_get(copy_id)

Get all comments for this copy in a quick pre-threaded view.

This is an alternative to GET /copies/id/comments

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.copies_copy_id_threaded_comments_get200_response import CopiesCopyIdThreadedCommentsGet200Response
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
    api_instance = openapi_client.MakeApi(api_client)
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id

    try:
        # Get all comments for this copy in a quick pre-threaded view.
        api_response = api_instance.copies_copy_id_threaded_comments_get(copy_id)
        print("The response of MakeApi->copies_copy_id_threaded_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_threaded_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 

### Return type

[**CopiesCopyIdThreadedCommentsGet200Response**](CopiesCopyIdThreadedCommentsGet200Response.md)

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

# **copies_copy_id_toggle_watch_post**
> object copies_copy_id_toggle_watch_post(copy_id)

Watch/unwatch a Make

If currently watching the specified Make, the current user will unwatch the Make, and vice versa. Only works in user context.

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
    api_instance = openapi_client.MakeApi(api_client)
    copy_id = 1 # int | The id of the affected copy. This is also known as the make_id

    try:
        # Watch/unwatch a Make
        api_response = api_instance.copies_copy_id_toggle_watch_post(copy_id)
        print("The response of MakeApi->copies_copy_id_toggle_watch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_copy_id_toggle_watch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_id** | **int**| The id of the affected copy. This is also known as the make_id | 

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

# **copies_get**
> List[CopySchema] copies_get(page=page, per_page=per_page)

Get the list of latest makes (copies).

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.copy_schema import CopySchema
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
    api_instance = openapi_client.MakeApi(api_client)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get the list of latest makes (copies).
        api_response = api_instance.copies_get(page=page, per_page=per_page)
        print("The response of MakeApi->copies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 

### Return type

[**List[CopySchema]**](CopySchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of makes |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copiesreturncomplete_get**
> List[str] copiesreturncomplete_get(page=page, per_page=per_page)

Get the list of latest makes (copies). The return complete ensures that the full thinginfo and image info is returned

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
    api_instance = openapi_client.MakeApi(api_client)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get the list of latest makes (copies). The return complete ensures that the full thinginfo and image info is returned
        api_response = api_instance.copiesreturncomplete_get(page=page, per_page=per_page)
        print("The response of MakeApi->copiesreturncomplete_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MakeApi->copiesreturncomplete_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | List of makes |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

