# openapi_client.GroupTopicApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grouptopics_grouptopic_id_comments_get**](GroupTopicApi.md#grouptopics_grouptopic_id_comments_get) | **GET** /grouptopics/{grouptopic_id}/comments | Get all comments for this topic in a quick pre-threaded view
[**grouptopics_grouptopic_id_comments_post**](GroupTopicApi.md#grouptopics_grouptopic_id_comments_post) | **POST** /grouptopics/{grouptopic_id}/comments | Post a comment
[**grouptopics_grouptopic_id_delete**](GroupTopicApi.md#grouptopics_grouptopic_id_delete) | **DELETE** /grouptopics/{grouptopic_id}/ | Delete Group Topic by id
[**grouptopics_grouptopic_id_forumtopics_comments_get**](GroupTopicApi.md#grouptopics_grouptopic_id_forumtopics_comments_get) | **GET** /grouptopics/{grouptopic_id}/forumtopics-comments | Get list topics and comments of a certain forum
[**grouptopics_grouptopic_id_get**](GroupTopicApi.md#grouptopics_grouptopic_id_get) | **GET** /grouptopics/{grouptopic_id}/ | Get a group topic by id
[**grouptopics_grouptopic_id_patch**](GroupTopicApi.md#grouptopics_grouptopic_id_patch) | **PATCH** /grouptopics/{grouptopic_id}/ | Update a group topic
[**grouptopics_grouptopic_id_pin_delete**](GroupTopicApi.md#grouptopics_grouptopic_id_pin_delete) | **DELETE** /grouptopics/{grouptopic_id}/pin | Unpin the group topic
[**grouptopics_grouptopic_id_pin_post**](GroupTopicApi.md#grouptopics_grouptopic_id_pin_post) | **POST** /grouptopics/{grouptopic_id}/pin | Pin the group topic
[**grouptopics_grouptopic_id_root_comments_get**](GroupTopicApi.md#grouptopics_grouptopic_id_root_comments_get) | **GET** /grouptopics/{grouptopic_id}/root-comments | Get an unthreaded paginated list of root comment objects
[**grouptopics_grouptopic_id_update_post**](GroupTopicApi.md#grouptopics_grouptopic_id_update_post) | **POST** /grouptopics/{grouptopic_id}/update | Update GroupTopic
[**grouptopics_grouptopic_id_watch_delete**](GroupTopicApi.md#grouptopics_grouptopic_id_watch_delete) | **DELETE** /grouptopics/{grouptopic_id}/watch | Unwatch the group topic
[**grouptopics_grouptopic_id_watch_post**](GroupTopicApi.md#grouptopics_grouptopic_id_watch_post) | **POST** /grouptopics/{grouptopic_id}/watch | Watch the group topic


# **grouptopics_grouptopic_id_comments_get**
> List[CommentSchema] grouptopics_grouptopic_id_comments_get(grouptopic_id)

Get all comments for this topic in a quick pre-threaded view

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.comment_schema import CommentSchema
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
    api_instance = openapi_client.GroupTopicApi(api_client)
    grouptopic_id = 2 # int | The id of the group topic

    try:
        # Get all comments for this topic in a quick pre-threaded view
        api_response = api_instance.grouptopics_grouptopic_id_comments_get(grouptopic_id)
        print("The response of GroupTopicApi->grouptopics_grouptopic_id_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupTopicApi->grouptopics_grouptopic_id_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouptopic_id** | **int**| The id of the group topic | 

### Return type

[**List[CommentSchema]**](CommentSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of group members. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grouptopics_grouptopic_id_comments_post**
> CommentSchema grouptopics_grouptopic_id_comments_post(grouptopic_id, grouptopics_grouptopic_id_comments_post_request=grouptopics_grouptopic_id_comments_post_request)

Post a comment

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.comment_schema import CommentSchema
from openapi_client.models.grouptopics_grouptopic_id_comments_post_request import GrouptopicsGrouptopicIdCommentsPostRequest
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
    api_instance = openapi_client.GroupTopicApi(api_client)
    grouptopic_id = 2 # int | The id of the group topic
    grouptopics_grouptopic_id_comments_post_request = openapi_client.GrouptopicsGrouptopicIdCommentsPostRequest() # GrouptopicsGrouptopicIdCommentsPostRequest |  (optional)

    try:
        # Post a comment
        api_response = api_instance.grouptopics_grouptopic_id_comments_post(grouptopic_id, grouptopics_grouptopic_id_comments_post_request=grouptopics_grouptopic_id_comments_post_request)
        print("The response of GroupTopicApi->grouptopics_grouptopic_id_comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupTopicApi->grouptopics_grouptopic_id_comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouptopic_id** | **int**| The id of the group topic | 
 **grouptopics_grouptopic_id_comments_post_request** | [**GrouptopicsGrouptopicIdCommentsPostRequest**](GrouptopicsGrouptopicIdCommentsPostRequest.md)|  | [optional] 

### Return type

[**CommentSchema**](CommentSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly created comment |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grouptopics_grouptopic_id_delete**
> int grouptopics_grouptopic_id_delete(grouptopic_id)

Delete Group Topic by id

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
    api_instance = openapi_client.GroupTopicApi(api_client)
    grouptopic_id = 2 # int | The id of the group topic

    try:
        # Delete Group Topic by id
        api_response = api_instance.grouptopics_grouptopic_id_delete(grouptopic_id)
        print("The response of GroupTopicApi->grouptopics_grouptopic_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupTopicApi->grouptopics_grouptopic_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouptopic_id** | **int**| The id of the group topic | 

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
**200** | id of the deleted Group Topic |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grouptopics_grouptopic_id_forumtopics_comments_get**
> GrouptopicsGrouptopicIdForumtopicsCommentsGet200Response grouptopics_grouptopic_id_forumtopics_comments_get(grouptopic_id, search=search, page=page, per_page=per_page)

Get list topics and comments of a certain forum

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.grouptopics_grouptopic_id_forumtopics_comments_get200_response import GrouptopicsGrouptopicIdForumtopicsCommentsGet200Response
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
    api_instance = openapi_client.GroupTopicApi(api_client)
    grouptopic_id = 2 # int | The id of the group topic
    search = '3d' # str | The search query to perform (optional)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get list topics and comments of a certain forum
        api_response = api_instance.grouptopics_grouptopic_id_forumtopics_comments_get(grouptopic_id, search=search, page=page, per_page=per_page)
        print("The response of GroupTopicApi->grouptopics_grouptopic_id_forumtopics_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupTopicApi->grouptopics_grouptopic_id_forumtopics_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouptopic_id** | **int**| The id of the group topic | 
 **search** | **str**| The search query to perform | [optional] 
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 

### Return type

[**GrouptopicsGrouptopicIdForumtopicsCommentsGet200Response**](GrouptopicsGrouptopicIdForumtopicsCommentsGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object representing the forum topics and comments requested |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grouptopics_grouptopic_id_get**
> GrouptopicSchema grouptopics_grouptopic_id_get(grouptopic_id)

Get a group topic by id

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.grouptopic_schema import GrouptopicSchema
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
    api_instance = openapi_client.GroupTopicApi(api_client)
    grouptopic_id = 2 # int | The id of the group topic

    try:
        # Get a group topic by id
        api_response = api_instance.grouptopics_grouptopic_id_get(grouptopic_id)
        print("The response of GroupTopicApi->grouptopics_grouptopic_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupTopicApi->grouptopics_grouptopic_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouptopic_id** | **int**| The id of the group topic | 

### Return type

[**GrouptopicSchema**](GrouptopicSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object representing the group topic requested |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grouptopics_grouptopic_id_patch**
> GrouptopicSchema grouptopics_grouptopic_id_patch(grouptopic_id, grouptopics_grouptopic_id_patch_request=grouptopics_grouptopic_id_patch_request)

Update a group topic

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.grouptopic_schema import GrouptopicSchema
from openapi_client.models.grouptopics_grouptopic_id_patch_request import GrouptopicsGrouptopicIdPatchRequest
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
    api_instance = openapi_client.GroupTopicApi(api_client)
    grouptopic_id = 2 # int | The id of the group topic
    grouptopics_grouptopic_id_patch_request = openapi_client.GrouptopicsGrouptopicIdPatchRequest() # GrouptopicsGrouptopicIdPatchRequest |  (optional)

    try:
        # Update a group topic
        api_response = api_instance.grouptopics_grouptopic_id_patch(grouptopic_id, grouptopics_grouptopic_id_patch_request=grouptopics_grouptopic_id_patch_request)
        print("The response of GroupTopicApi->grouptopics_grouptopic_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupTopicApi->grouptopics_grouptopic_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouptopic_id** | **int**| The id of the group topic | 
 **grouptopics_grouptopic_id_patch_request** | [**GrouptopicsGrouptopicIdPatchRequest**](GrouptopicsGrouptopicIdPatchRequest.md)|  | [optional] 

### Return type

[**GrouptopicSchema**](GrouptopicSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated a group topic |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grouptopics_grouptopic_id_pin_delete**
> TopicSchema grouptopics_grouptopic_id_pin_delete(grouptopic_id)

Unpin the group topic

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.topic_schema import TopicSchema
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
    api_instance = openapi_client.GroupTopicApi(api_client)
    grouptopic_id = 2 # int | The id of the group topic

    try:
        # Unpin the group topic
        api_response = api_instance.grouptopics_grouptopic_id_pin_delete(grouptopic_id)
        print("The response of GroupTopicApi->grouptopics_grouptopic_id_pin_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupTopicApi->grouptopics_grouptopic_id_pin_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouptopic_id** | **int**| The id of the group topic | 

### Return type

[**TopicSchema**](TopicSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unpinned topic |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grouptopics_grouptopic_id_pin_post**
> TopicSchema grouptopics_grouptopic_id_pin_post(grouptopic_id)

Pin the group topic

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.topic_schema import TopicSchema
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
    api_instance = openapi_client.GroupTopicApi(api_client)
    grouptopic_id = 2 # int | The id of the group topic

    try:
        # Pin the group topic
        api_response = api_instance.grouptopics_grouptopic_id_pin_post(grouptopic_id)
        print("The response of GroupTopicApi->grouptopics_grouptopic_id_pin_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupTopicApi->grouptopics_grouptopic_id_pin_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouptopic_id** | **int**| The id of the group topic | 

### Return type

[**TopicSchema**](TopicSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pinned topic |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grouptopics_grouptopic_id_root_comments_get**
> List[str] grouptopics_grouptopic_id_root_comments_get(grouptopic_id, page=page, per_page=per_page)

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
    api_instance = openapi_client.GroupTopicApi(api_client)
    grouptopic_id = 2 # int | The id of the group topic
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get an unthreaded paginated list of root comment objects
        api_response = api_instance.grouptopics_grouptopic_id_root_comments_get(grouptopic_id, page=page, per_page=per_page)
        print("The response of GroupTopicApi->grouptopics_grouptopic_id_root_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupTopicApi->grouptopics_grouptopic_id_root_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouptopic_id** | **int**| The id of the group topic | 
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
**200** | An array containing a list of root comments on this topic |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grouptopics_grouptopic_id_update_post**
> ThingsThingIdDelete200Response grouptopics_grouptopic_id_update_post(grouptopic_id, grouptopics_grouptopic_id_update_post_request=grouptopics_grouptopic_id_update_post_request)

Update GroupTopic

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.grouptopics_grouptopic_id_update_post_request import GrouptopicsGrouptopicIdUpdatePostRequest
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
    api_instance = openapi_client.GroupTopicApi(api_client)
    grouptopic_id = 2 # int | The id of the group topic
    grouptopics_grouptopic_id_update_post_request = openapi_client.GrouptopicsGrouptopicIdUpdatePostRequest() # GrouptopicsGrouptopicIdUpdatePostRequest |  (optional)

    try:
        # Update GroupTopic
        api_response = api_instance.grouptopics_grouptopic_id_update_post(grouptopic_id, grouptopics_grouptopic_id_update_post_request=grouptopics_grouptopic_id_update_post_request)
        print("The response of GroupTopicApi->grouptopics_grouptopic_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupTopicApi->grouptopics_grouptopic_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouptopic_id** | **int**| The id of the group topic | 
 **grouptopics_grouptopic_id_update_post_request** | [**GrouptopicsGrouptopicIdUpdatePostRequest**](GrouptopicsGrouptopicIdUpdatePostRequest.md)|  | [optional] 

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

# **grouptopics_grouptopic_id_watch_delete**
> TopicSchema grouptopics_grouptopic_id_watch_delete(grouptopic_id)

Unwatch the group topic

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.topic_schema import TopicSchema
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
    api_instance = openapi_client.GroupTopicApi(api_client)
    grouptopic_id = 2 # int | The id of the group topic

    try:
        # Unwatch the group topic
        api_response = api_instance.grouptopics_grouptopic_id_watch_delete(grouptopic_id)
        print("The response of GroupTopicApi->grouptopics_grouptopic_id_watch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupTopicApi->grouptopics_grouptopic_id_watch_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouptopic_id** | **int**| The id of the group topic | 

### Return type

[**TopicSchema**](TopicSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unwatched topic |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grouptopics_grouptopic_id_watch_post**
> TopicSchema grouptopics_grouptopic_id_watch_post(grouptopic_id)

Watch the group topic

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.topic_schema import TopicSchema
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
    api_instance = openapi_client.GroupTopicApi(api_client)
    grouptopic_id = 2 # int | The id of the group topic

    try:
        # Watch the group topic
        api_response = api_instance.grouptopics_grouptopic_id_watch_post(grouptopic_id)
        print("The response of GroupTopicApi->grouptopics_grouptopic_id_watch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupTopicApi->grouptopics_grouptopic_id_watch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grouptopic_id** | **int**| The id of the group topic | 

### Return type

[**TopicSchema**](TopicSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Watched topic |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

