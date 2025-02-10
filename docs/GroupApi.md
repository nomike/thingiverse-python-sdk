# openapi_client.GroupApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_get**](GroupApi.md#groups_get) | **GET** /groups/ | List of groups
[**groups_group_id_delete**](GroupApi.md#groups_group_id_delete) | **DELETE** /groups/{group_id} | Delete a group
[**groups_group_id_forum_by_slug_forum_slug_get**](GroupApi.md#groups_group_id_forum_by_slug_forum_slug_get) | **GET** /groups/{group_id}/forum-by-slug/{forum_slug} | Get group forum by slug
[**groups_group_id_forum_forum_id_delete**](GroupApi.md#groups_group_id_forum_forum_id_delete) | **DELETE** /groups/{group_id}/forum/{forum_id} | Delete group forum
[**groups_group_id_forum_topics_forum_id_get**](GroupApi.md#groups_group_id_forum_topics_forum_id_get) | **GET** /groups/{group_id}/forum-topics/{forum_id} | Get all topics for the group forum
[**groups_group_id_get**](GroupApi.md#groups_group_id_get) | **GET** /groups/{group_id} | Get group by id
[**groups_group_id_group_forums_get**](GroupApi.md#groups_group_id_group_forums_get) | **GET** /groups/{group_id}/group-forums | List of group forums
[**groups_group_id_group_forums_post**](GroupApi.md#groups_group_id_group_forums_post) | **POST** /groups/{group_id}/group-forums | Create a new forum
[**groups_group_id_group_topics_forum_slug_post**](GroupApi.md#groups_group_id_group_topics_forum_slug_post) | **POST** /groups/{group_id}/group-topics/{forum_slug} | Create a new Group Topic
[**groups_group_id_group_topics_get**](GroupApi.md#groups_group_id_group_topics_get) | **GET** /groups/{group_id}/group-topics | List of group topics
[**groups_group_id_image_post**](GroupApi.md#groups_group_id_image_post) | **POST** /groups/{group_id}/image | Upload a new image of group
[**groups_group_id_members_delete**](GroupApi.md#groups_group_id_members_delete) | **DELETE** /groups/{group_id}/members | Leave group
[**groups_group_id_members_get**](GroupApi.md#groups_group_id_members_get) | **GET** /groups/{group_id}/members | List of group members
[**groups_group_id_members_post**](GroupApi.md#groups_group_id_members_post) | **POST** /groups/{group_id}/members | Join to group
[**groups_group_id_patch**](GroupApi.md#groups_group_id_patch) | **PATCH** /groups/{group_id} | Update an existing group
[**groups_group_id_things_get**](GroupApi.md#groups_group_id_things_get) | **GET** /groups/{group_id}/things | List of group things
[**groups_group_id_things_thing_id_delete**](GroupApi.md#groups_group_id_things_thing_id_delete) | **DELETE** /groups/{group_id}/things/{thing_id} | Delete thing from group
[**groups_group_id_things_thing_id_post**](GroupApi.md#groups_group_id_things_thing_id_post) | **POST** /groups/{group_id}/things/{thing_id} | Add thing to group
[**groups_group_id_update_group_forum_forum_id_post**](GroupApi.md#groups_group_id_update_group_forum_forum_id_post) | **POST** /groups/{group_id}/update-group-forum/{forum_id} | Update a certain forum of group
[**groups_post**](GroupApi.md#groups_post) | **POST** /groups/ | Create a new group


# **groups_get**
> List[GroupSchema] groups_get()

List of groups

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.group_schema import GroupSchema
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
    api_instance = openapi_client.GroupApi(api_client)

    try:
        # List of groups
        api_response = api_instance.groups_get()
        print("The response of GroupApi->groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GroupSchema]**](GroupSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of groups. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_delete**
> ThingsThingIdDelete200Response groups_group_id_delete(group_id)

Delete a group

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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected

    try:
        # Delete a group
        api_response = api_instance.groups_group_id_delete(group_id)
        print("The response of GroupApi->groups_group_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 

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

# **groups_group_id_forum_by_slug_forum_slug_get**
> object groups_group_id_forum_by_slug_forum_slug_get(group_id, forum_slug)

Get group forum by slug

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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected
    forum_slug = 'general' # str | The slug of the forum

    try:
        # Get group forum by slug
        api_response = api_instance.groups_group_id_forum_by_slug_forum_slug_get(group_id, forum_slug)
        print("The response of GroupApi->groups_group_id_forum_by_slug_forum_slug_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_forum_by_slug_forum_slug_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 
 **forum_slug** | **str**| The slug of the forum | 

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
**200** | Forum object with top tags |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_forum_forum_id_delete**
> int groups_group_id_forum_forum_id_delete(group_id, forum_id)

Delete group forum

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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected
    forum_id = 15561 # int | The id of the forum

    try:
        # Delete group forum
        api_response = api_instance.groups_group_id_forum_forum_id_delete(group_id, forum_id)
        print("The response of GroupApi->groups_group_id_forum_forum_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_forum_forum_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 
 **forum_id** | **int**| The id of the forum | 

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
**200** | id of the deleted Forum |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_forum_topics_forum_id_get**
> List[TopicSchema] groups_group_id_forum_topics_forum_id_get(group_id, forum_id, page=page, per_page=per_page)

Get all topics for the group forum

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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected
    forum_id = 15561 # int | The id of the forum
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get all topics for the group forum
        api_response = api_instance.groups_group_id_forum_topics_forum_id_get(group_id, forum_id, page=page, per_page=per_page)
        print("The response of GroupApi->groups_group_id_forum_topics_forum_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_forum_topics_forum_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 
 **forum_id** | **int**| The id of the forum | 
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 

### Return type

[**List[TopicSchema]**](TopicSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of group forum topics. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_get**
> GroupSchema groups_group_id_get(group_id)

Get group by id

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.group_schema import GroupSchema
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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected

    try:
        # Get group by id
        api_response = api_instance.groups_group_id_get(group_id)
        print("The response of GroupApi->groups_group_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 

### Return type

[**GroupSchema**](GroupSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object representing the group requested |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_group_forums_get**
> List[ForumSchema] groups_group_id_group_forums_get(group_id)

List of group forums

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.forum_schema import ForumSchema
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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected

    try:
        # List of group forums
        api_response = api_instance.groups_group_id_group_forums_get(group_id)
        print("The response of GroupApi->groups_group_id_group_forums_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_group_forums_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 

### Return type

[**List[ForumSchema]**](ForumSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of group forums. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_group_forums_post**
> ForumSchema groups_group_id_group_forums_post(group_id, name, description, filename=filename, file=file)

Create a new forum

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.forum_schema import ForumSchema
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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected
    name = 'name_example' # str | Set the name of the forum
    description = 'description_example' # str | Set the description.
    filename = 'filename_example' # str | Set the file name. (optional)
    file = None # bytearray | Set the image. Available formats are jpeg, jpg, gif, png (optional)

    try:
        # Create a new forum
        api_response = api_instance.groups_group_id_group_forums_post(group_id, name, description, filename=filename, file=file)
        print("The response of GroupApi->groups_group_id_group_forums_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_group_forums_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 
 **name** | **str**| Set the name of the forum | 
 **description** | **str**| Set the description. | 
 **filename** | **str**| Set the file name. | [optional] 
 **file** | **bytearray**| Set the image. Available formats are jpeg, jpg, gif, png | [optional] 

### Return type

[**ForumSchema**](ForumSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly created forum. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_group_topics_forum_slug_post**
> TopicSchema groups_group_id_group_topics_forum_slug_post(group_id, forum_slug, name, body, tags=tags, filenames=filenames, files=files)

Create a new Group Topic

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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected
    forum_slug = 'general' # str | The slug of the forum
    name = 'name_example' # str | Name of Topic
    body = 'body_example' # str | Body text of Topic
    tags = None # List[object] | Array of tags (optional)
    filenames = None # List[object] | Array of filenames to be uploaded (optional)
    files = ['files_example'] # List[str] | Array of files to be uploaded (optional)

    try:
        # Create a new Group Topic
        api_response = api_instance.groups_group_id_group_topics_forum_slug_post(group_id, forum_slug, name, body, tags=tags, filenames=filenames, files=files)
        print("The response of GroupApi->groups_group_id_group_topics_forum_slug_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_group_topics_forum_slug_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 
 **forum_slug** | **str**| The slug of the forum | 
 **name** | **str**| Name of Topic | 
 **body** | **str**| Body text of Topic | 
 **tags** | [**List[object]**](object.md)| Array of tags | [optional] 
 **filenames** | [**List[object]**](object.md)| Array of filenames to be uploaded | [optional] 
 **files** | [**List[str]**](str.md)| Array of files to be uploaded | [optional] 

### Return type

[**TopicSchema**](TopicSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly created topic |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_group_topics_get**
> List[TopicSchema] groups_group_id_group_topics_get(group_id, filter=filter, sort=sort, page=page, per_page=per_page)

List of group topics

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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected
    filter = 'pinned' # str | Optional filter. Supports my-started-topics, my-topics, pinned. Default is all (optional)
    sort = 'popular' # str | Supports popular, date (date is by last modified). Returns in DESC order. Default is date (optional)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # List of group topics
        api_response = api_instance.groups_group_id_group_topics_get(group_id, filter=filter, sort=sort, page=page, per_page=per_page)
        print("The response of GroupApi->groups_group_id_group_topics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_group_topics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 
 **filter** | **str**| Optional filter. Supports my-started-topics, my-topics, pinned. Default is all | [optional] 
 **sort** | **str**| Supports popular, date (date is by last modified). Returns in DESC order. Default is date | [optional] 
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 

### Return type

[**List[TopicSchema]**](TopicSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of group topics. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_image_post**
> ThingsThingIdDelete200Response groups_group_id_image_post(group_id, filename, file)

Upload a new image of group

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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected
    filename = 'filename_example' # str | Set the file name.
    file = None # bytearray | Set the image. Available formats are jpeg, jpg, gif, png

    try:
        # Upload a new image of group
        api_response = api_instance.groups_group_id_image_post(group_id, filename, file)
        print("The response of GroupApi->groups_group_id_image_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_image_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 
 **filename** | **str**| Set the file name. | 
 **file** | **bytearray**| Set the image. Available formats are jpeg, jpg, gif, png | 

### Return type

[**ThingsThingIdDelete200Response**](ThingsThingIdDelete200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_members_delete**
> ThingsThingIdDelete200Response groups_group_id_members_delete(group_id)

Leave group

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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected

    try:
        # Leave group
        api_response = api_instance.groups_group_id_members_delete(group_id)
        print("The response of GroupApi->groups_group_id_members_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_members_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 

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

# **groups_group_id_members_get**
> List[MemberSchema] groups_group_id_members_get(group_id, page=page, per_page=per_page)

List of group members

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.member_schema import MemberSchema
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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # List of group members
        api_response = api_instance.groups_group_id_members_get(group_id, page=page, per_page=per_page)
        print("The response of GroupApi->groups_group_id_members_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_members_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 

### Return type

[**List[MemberSchema]**](MemberSchema.md)

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

# **groups_group_id_members_post**
> ThingsThingIdDelete200Response groups_group_id_members_post(group_id)

Join to group

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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected

    try:
        # Join to group
        api_response = api_instance.groups_group_id_members_post(group_id)
        print("The response of GroupApi->groups_group_id_members_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_members_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 

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

# **groups_group_id_patch**
> GroupSchema groups_group_id_patch(group_id, groups_group_id_patch_request=groups_group_id_patch_request)

Update an existing group

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.group_schema import GroupSchema
from openapi_client.models.groups_group_id_patch_request import GroupsGroupIdPatchRequest
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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected
    groups_group_id_patch_request = openapi_client.GroupsGroupIdPatchRequest() # GroupsGroupIdPatchRequest |  (optional)

    try:
        # Update an existing group
        api_response = api_instance.groups_group_id_patch(group_id, groups_group_id_patch_request=groups_group_id_patch_request)
        print("The response of GroupApi->groups_group_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 
 **groups_group_id_patch_request** | [**GroupsGroupIdPatchRequest**](GroupsGroupIdPatchRequest.md)|  | [optional] 

### Return type

[**GroupSchema**](GroupSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated group data |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_things_get**
> List[ThingSchema] groups_group_id_things_get(group_id, page=page, per_page=per_page)

List of group things

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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # List of group things
        api_response = api_instance.groups_group_id_things_get(group_id, page=page, per_page=per_page)
        print("The response of GroupApi->groups_group_id_things_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_things_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 
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
**200** | The list of group things. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_things_thing_id_delete**
> ThingsThingIdDelete200Response groups_group_id_things_thing_id_delete(group_id, thing_id)

Delete thing from group

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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Delete thing from group
        api_response = api_instance.groups_group_id_things_thing_id_delete(group_id, thing_id)
        print("The response of GroupApi->groups_group_id_things_thing_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_things_thing_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 
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

# **groups_group_id_things_thing_id_post**
> ThingsThingIdDelete200Response groups_group_id_things_thing_id_post(group_id, thing_id)

Add thing to group

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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected
    thing_id = 1004996 # int | The id of the thing affected

    try:
        # Add thing to group
        api_response = api_instance.groups_group_id_things_thing_id_post(group_id, thing_id)
        print("The response of GroupApi->groups_group_id_things_thing_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_things_thing_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 
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

# **groups_group_id_update_group_forum_forum_id_post**
> GroupforumSchema groups_group_id_update_group_forum_forum_id_post(group_id, forum_id, name, description, filename=filename, file=file)

Update a certain forum of group

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.groupforum_schema import GroupforumSchema
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
    api_instance = openapi_client.GroupApi(api_client)
    group_id = 25 # int | The id of the group affected
    forum_id = 15561 # int | The id of the forum
    name = 'name_example' # str | Set the name of the forum
    description = 'description_example' # str | Set the description of the forum
    filename = 'filename_example' # str | Set the file name (optional)
    file = None # bytearray | Set the image. Available formats are jpeg, jpg, gif, png (optional)

    try:
        # Update a certain forum of group
        api_response = api_instance.groups_group_id_update_group_forum_forum_id_post(group_id, forum_id, name, description, filename=filename, file=file)
        print("The response of GroupApi->groups_group_id_update_group_forum_forum_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_group_id_update_group_forum_forum_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| The id of the group affected | 
 **forum_id** | **int**| The id of the forum | 
 **name** | **str**| Set the name of the forum | 
 **description** | **str**| Set the description of the forum | 
 **filename** | **str**| Set the file name | [optional] 
 **file** | **bytearray**| Set the image. Available formats are jpeg, jpg, gif, png | [optional] 

### Return type

[**GroupforumSchema**](GroupforumSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated forum |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_post**
> GroupSchema groups_post(name, slug, description, filename=filename, file=file)

Create a new group

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.group_schema import GroupSchema
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
    api_instance = openapi_client.GroupApi(api_client)
    name = 'name_example' # str | Set the name of the group
    slug = 'slug_example' # str | Set the slug of the group
    description = 'description_example' # str | Set the description.
    filename = 'filename_example' # str | Set the file name. (optional)
    file = None # bytearray | Set the image. Available formats are jpeg, jpg, gif, png (optional)

    try:
        # Create a new group
        api_response = api_instance.groups_post(name, slug, description, filename=filename, file=file)
        print("The response of GroupApi->groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Set the name of the group | 
 **slug** | **str**| Set the slug of the group | 
 **description** | **str**| Set the description. | 
 **filename** | **str**| Set the file name. | [optional] 
 **file** | **bytearray**| Set the image. Available formats are jpeg, jpg, gif, png | [optional] 

### Return type

[**GroupSchema**](GroupSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly created group. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

