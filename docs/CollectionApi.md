# openapi_client.CollectionApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collections_collection_id_delete**](CollectionApi.md#collections_collection_id_delete) | **DELETE** /collections/{collection_id}/ | Delete a collection
[**collections_collection_id_get**](CollectionApi.md#collections_collection_id_get) | **GET** /collections/{collection_id}/ | Get a collection by id
[**collections_collection_id_like_post**](CollectionApi.md#collections_collection_id_like_post) | **POST** /collections/{collection_id}/like | Like/unlike Collection
[**collections_collection_id_move_thing_id_post**](CollectionApi.md#collections_collection_id_move_thing_id_post) | **POST** /collections/{collection_id}/move/{thing_id} | Move a thing between collections
[**collections_collection_id_patch**](CollectionApi.md#collections_collection_id_patch) | **PATCH** /collections/{collection_id}/ | Update a collection
[**collections_collection_id_thing_thing_id_delete**](CollectionApi.md#collections_collection_id_thing_thing_id_delete) | **DELETE** /collections/{collection_id}/thing/{thing_id} | Removes a thing from a collection
[**collections_collection_id_thing_thing_id_post**](CollectionApi.md#collections_collection_id_thing_thing_id_post) | **POST** /collections/{collection_id}/thing/{thing_id} | Add a thing to a collection
[**collections_collection_id_things_get**](CollectionApi.md#collections_collection_id_things_get) | **GET** /collections/{collection_id}/things | Get Things in a collection
[**collections_collection_id_watch_post**](CollectionApi.md#collections_collection_id_watch_post) | **POST** /collections/{collection_id}/watch | Watch/unwatch Collection
[**collections_get**](CollectionApi.md#collections_get) | **GET** /collections/ | Get list of the latest collections
[**collections_post**](CollectionApi.md#collections_post) | **POST** /collections/ | Create a new collection
[**collections_thing_id_by_thing_id_get**](CollectionApi.md#collections_thing_id_by_thing_id_get) | **GET** /collections/{thing_id}/by-thing-id | Get a collection by id


# **collections_collection_id_delete**
> ThingsThingIdDelete200Response collections_collection_id_delete(collection_id)

Delete a collection

Apps can only delete collections they've created.

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
    api_instance = openapi_client.CollectionApi(api_client)
    collection_id = 1 # int | ID of the collection affected

    try:
        # Delete a collection
        api_response = api_instance.collections_collection_id_delete(collection_id)
        print("The response of CollectionApi->collections_collection_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collections_collection_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| ID of the collection affected | 

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

# **collections_collection_id_get**
> CollectionSchema collections_collection_id_get(collection_id)

Get a collection by id

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.collection_schema import CollectionSchema
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
    api_instance = openapi_client.CollectionApi(api_client)
    collection_id = 1 # int | ID of the collection affected

    try:
        # Get a collection by id
        api_response = api_instance.collections_collection_id_get(collection_id)
        print("The response of CollectionApi->collections_collection_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collections_collection_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| ID of the collection affected | 

### Return type

[**CollectionSchema**](CollectionSchema.md)

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

# **collections_collection_id_like_post**
> object collections_collection_id_like_post(collection_id)

Like/unlike Collection

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
    api_instance = openapi_client.CollectionApi(api_client)
    collection_id = 1 # int | ID of the collection affected

    try:
        # Like/unlike Collection
        api_response = api_instance.collections_collection_id_like_post(collection_id)
        print("The response of CollectionApi->collections_collection_id_like_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collections_collection_id_like_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| ID of the collection affected | 

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
**200** | Was collection liked or unliked |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_id_move_thing_id_post**
> ThingsThingIdDelete200Response collections_collection_id_move_thing_id_post(collection_id, thing_id, collections_collection_id_thing_thing_id_post_request=collections_collection_id_thing_thing_id_post_request)

Move a thing between collections

Things can move a thing to any collection the user owns.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.collections_collection_id_thing_thing_id_post_request import CollectionsCollectionIdThingThingIdPostRequest
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
    api_instance = openapi_client.CollectionApi(api_client)
    collection_id = 1 # int | ID of the collection affected
    thing_id = 1004996 # int | The id of the thing affected
    collections_collection_id_thing_thing_id_post_request = openapi_client.CollectionsCollectionIdThingThingIdPostRequest() # CollectionsCollectionIdThingThingIdPostRequest |  (optional)

    try:
        # Move a thing between collections
        api_response = api_instance.collections_collection_id_move_thing_id_post(collection_id, thing_id, collections_collection_id_thing_thing_id_post_request=collections_collection_id_thing_thing_id_post_request)
        print("The response of CollectionApi->collections_collection_id_move_thing_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collections_collection_id_move_thing_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| ID of the collection affected | 
 **thing_id** | **int**| The id of the thing affected | 
 **collections_collection_id_thing_thing_id_post_request** | [**CollectionsCollectionIdThingThingIdPostRequest**](CollectionsCollectionIdThingThingIdPostRequest.md)|  | [optional] 

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

# **collections_collection_id_patch**
> CollectionSchema collections_collection_id_patch(collection_id, collections_collection_id_patch_request=collections_collection_id_patch_request)

Update a collection

Apps can only update collections they've created.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.collection_schema import CollectionSchema
from openapi_client.models.collections_collection_id_patch_request import CollectionsCollectionIdPatchRequest
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
    api_instance = openapi_client.CollectionApi(api_client)
    collection_id = 1 # int | ID of the collection affected
    collections_collection_id_patch_request = openapi_client.CollectionsCollectionIdPatchRequest() # CollectionsCollectionIdPatchRequest |  (optional)

    try:
        # Update a collection
        api_response = api_instance.collections_collection_id_patch(collection_id, collections_collection_id_patch_request=collections_collection_id_patch_request)
        print("The response of CollectionApi->collections_collection_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collections_collection_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| ID of the collection affected | 
 **collections_collection_id_patch_request** | [**CollectionsCollectionIdPatchRequest**](CollectionsCollectionIdPatchRequest.md)|  | [optional] 

### Return type

[**CollectionSchema**](CollectionSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated collection. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_id_thing_thing_id_delete**
> int collections_collection_id_thing_thing_id_delete(collection_id, thing_id)

Removes a thing from a collection

Apps may only remove things that they've added to a collection.

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
    api_instance = openapi_client.CollectionApi(api_client)
    collection_id = 1 # int | ID of the collection affected
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Removes a thing from a collection
        api_response = api_instance.collections_collection_id_thing_thing_id_delete(collection_id, thing_id)
        print("The response of CollectionApi->collections_collection_id_thing_thing_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collections_collection_id_thing_thing_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| ID of the collection affected | 
 **thing_id** | **int**| The id of the thing affected | 

### Return type

**int**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The id of thing that was deleted |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_id_thing_thing_id_post**
> ThingsThingIdDelete200Response collections_collection_id_thing_thing_id_post(collection_id, thing_id, collections_collection_id_thing_thing_id_post_request=collections_collection_id_thing_thing_id_post_request)

Add a thing to a collection

Apps can add to any collection the user owns. Do not abuse or we'll change that.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.collections_collection_id_thing_thing_id_post_request import CollectionsCollectionIdThingThingIdPostRequest
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
    api_instance = openapi_client.CollectionApi(api_client)
    collection_id = 1 # int | ID of the collection affected
    thing_id = 1004996 # int | The id of the thing affected
    collections_collection_id_thing_thing_id_post_request = openapi_client.CollectionsCollectionIdThingThingIdPostRequest() # CollectionsCollectionIdThingThingIdPostRequest |  (optional)

    try:
        # Add a thing to a collection
        api_response = api_instance.collections_collection_id_thing_thing_id_post(collection_id, thing_id, collections_collection_id_thing_thing_id_post_request=collections_collection_id_thing_thing_id_post_request)
        print("The response of CollectionApi->collections_collection_id_thing_thing_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collections_collection_id_thing_thing_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| ID of the collection affected | 
 **thing_id** | **int**| The id of the thing affected | 
 **collections_collection_id_thing_thing_id_post_request** | [**CollectionsCollectionIdThingThingIdPostRequest**](CollectionsCollectionIdThingThingIdPostRequest.md)|  | [optional] 

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

# **collections_collection_id_things_get**
> List[ShortThingSchema] collections_collection_id_things_get(collection_id, sort=sort, search=search, page=page, per_page=per_page, image_type=image_type, image_size=image_size)

Get Things in a collection

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
    api_instance = openapi_client.CollectionApi(api_client)
    collection_id = 1 # int | ID of the collection affected
    sort = 'sort_example' # str | Supports newest, popular. Returns in DESC order. Default is newest. Not supported for search. (optional)
    search = 'search_example' # str | Sort returns in relevant order. (optional)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)
    image_type = 'display' # str | With what image type should the things be returned. Can be thumb, display or preview (optional)
    image_size = 'large' # str | With what image size should the things be returned. Can be large, medium, small, tiny when image_type is thumb. Can be featured, card, large, medium, small, birdwing, tiny, tinycard when preview. Can be large, medium, small when display (optional)

    try:
        # Get Things in a collection
        api_response = api_instance.collections_collection_id_things_get(collection_id, sort=sort, search=search, page=page, per_page=per_page, image_type=image_type, image_size=image_size)
        print("The response of CollectionApi->collections_collection_id_things_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collections_collection_id_things_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| ID of the collection affected | 
 **sort** | **str**| Supports newest, popular. Returns in DESC order. Default is newest. Not supported for search. | [optional] 
 **search** | **str**| Sort returns in relevant order. | [optional] 
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 
 **image_type** | **str**| With what image type should the things be returned. Can be thumb, display or preview | [optional] 
 **image_size** | **str**| With what image size should the things be returned. Can be large, medium, small, tiny when image_type is thumb. Can be featured, card, large, medium, small, birdwing, tiny, tinycard when preview. Can be large, medium, small when display | [optional] 

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
**200** | An array of Things in this collection |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_id_watch_post**
> object collections_collection_id_watch_post(collection_id)

Watch/unwatch Collection

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
    api_instance = openapi_client.CollectionApi(api_client)
    collection_id = 1 # int | ID of the collection affected

    try:
        # Watch/unwatch Collection
        api_response = api_instance.collections_collection_id_watch_post(collection_id)
        print("The response of CollectionApi->collections_collection_id_watch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collections_collection_id_watch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| ID of the collection affected | 

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
**200** | Was collection watched or unwatched |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_get**
> List[CollectionSchema] collections_get(page=page, per_page=per_page)

Get list of the latest collections

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.collection_schema import CollectionSchema
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
    api_instance = openapi_client.CollectionApi(api_client)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get list of the latest collections
        api_response = api_instance.collections_get(page=page, per_page=per_page)
        print("The response of CollectionApi->collections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 

### Return type

[**List[CollectionSchema]**](CollectionSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of collections |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_post**
> CollectionSchema collections_post(collections_post_request=collections_post_request)

Create a new collection

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.collection_schema import CollectionSchema
from openapi_client.models.collections_post_request import CollectionsPostRequest
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
    api_instance = openapi_client.CollectionApi(api_client)
    collections_post_request = openapi_client.CollectionsPostRequest() # CollectionsPostRequest |  (optional)

    try:
        # Create a new collection
        api_response = api_instance.collections_post(collections_post_request=collections_post_request)
        print("The response of CollectionApi->collections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_post_request** | [**CollectionsPostRequest**](CollectionsPostRequest.md)|  | [optional] 

### Return type

[**CollectionSchema**](CollectionSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly created collection. |  -  |
**400** | Server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_thing_id_by_thing_id_get**
> CollectionSchema collections_thing_id_by_thing_id_get(thing_id)

Get a collection by id

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.collection_schema import CollectionSchema
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
    api_instance = openapi_client.CollectionApi(api_client)
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Get a collection by id
        api_response = api_instance.collections_thing_id_by_thing_id_get(thing_id)
        print("The response of CollectionApi->collections_thing_id_by_thing_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->collections_thing_id_by_thing_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_id** | **int**| The id of the thing affected | 

### Return type

[**CollectionSchema**](CollectionSchema.md)

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

