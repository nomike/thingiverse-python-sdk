# openapi_client.CommentApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comments0_markdown_post**](CommentApi.md#comments0_markdown_post) | **POST** /comments/0/markdown | Convert text to markdown
[**comments_comment_id_delete**](CommentApi.md#comments_comment_id_delete) | **DELETE** /comments/{comment_id}/ | Softdelete a comment
[**comments_comment_id_get**](CommentApi.md#comments_comment_id_get) | **GET** /comments/{comment_id}/ | Get a comment by id
[**comments_comment_id_patch**](CommentApi.md#comments_comment_id_patch) | **PATCH** /comments/{comment_id}/ | Update a comment
[**comments_comment_id_replies_get**](CommentApi.md#comments_comment_id_replies_get) | **GET** /comments/{comment_id}/replies | Get replies of a certain comment
[**comments_comment_id_reply_post**](CommentApi.md#comments_comment_id_reply_post) | **POST** /comments/{comment_id}/reply | Reply to a comment
[**comments_comment_id_restore_post**](CommentApi.md#comments_comment_id_restore_post) | **POST** /comments/{comment_id}/restore | Restore a deleted comment
[**comments_comment_id_spam_post**](CommentApi.md#comments_comment_id_spam_post) | **POST** /comments/{comment_id}/spam | Mark comment as a spam
[**comments_get**](CommentApi.md#comments_get) | **GET** /comments/ | Get the latest comments
[**comments_post**](CommentApi.md#comments_post) | **POST** /comments/ | Reply to a comment


# **comments0_markdown_post**
> str comments0_markdown_post(comments0_markdown_post_request=comments0_markdown_post_request)

Convert text to markdown

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.comments0_markdown_post_request import Comments0MarkdownPostRequest
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
    api_instance = openapi_client.CommentApi(api_client)
    comments0_markdown_post_request = openapi_client.Comments0MarkdownPostRequest() # Comments0MarkdownPostRequest |  (optional)

    try:
        # Convert text to markdown
        api_response = api_instance.comments0_markdown_post(comments0_markdown_post_request=comments0_markdown_post_request)
        print("The response of CommentApi->comments0_markdown_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentApi->comments0_markdown_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments0_markdown_post_request** | [**Comments0MarkdownPostRequest**](Comments0MarkdownPostRequest.md)|  | [optional] 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The marked text |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_comment_id_delete**
> ThingsThingIdDelete200Response comments_comment_id_delete(comment_id)

Softdelete a comment

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
    api_instance = openapi_client.CommentApi(api_client)
    comment_id = 285620 # int | The id of the comment

    try:
        # Softdelete a comment
        api_response = api_instance.comments_comment_id_delete(comment_id)
        print("The response of CommentApi->comments_comment_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentApi->comments_comment_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| The id of the comment | 

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

# **comments_comment_id_get**
> CommentSchema comments_comment_id_get(comment_id)

Get a comment by id

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
    api_instance = openapi_client.CommentApi(api_client)
    comment_id = 285620 # int | The id of the comment

    try:
        # Get a comment by id
        api_response = api_instance.comments_comment_id_get(comment_id)
        print("The response of CommentApi->comments_comment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentApi->comments_comment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| The id of the comment | 

### Return type

[**CommentSchema**](CommentSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object representing the comment requested |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_comment_id_patch**
> CommentSchema comments_comment_id_patch(comment_id, comment_schema=comment_schema)

Update a comment

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
    api_instance = openapi_client.CommentApi(api_client)
    comment_id = 285620 # int | The id of the comment
    comment_schema = openapi_client.CommentSchema() # CommentSchema |  (optional)

    try:
        # Update a comment
        api_response = api_instance.comments_comment_id_patch(comment_id, comment_schema=comment_schema)
        print("The response of CommentApi->comments_comment_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentApi->comments_comment_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| The id of the comment | 
 **comment_schema** | [**CommentSchema**](CommentSchema.md)|  | [optional] 

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
**200** | Updated a comment |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_comment_id_replies_get**
> List[CommentSchema] comments_comment_id_replies_get(comment_id)

Get replies of a certain comment

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
    api_instance = openapi_client.CommentApi(api_client)
    comment_id = 285620 # int | The id of the comment

    try:
        # Get replies of a certain comment
        api_response = api_instance.comments_comment_id_replies_get(comment_id)
        print("The response of CommentApi->comments_comment_id_replies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentApi->comments_comment_id_replies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| The id of the comment | 

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
**200** | The list of comment replies |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_comment_id_reply_post**
> CommentSchema comments_comment_id_reply_post(comment_id, things_thing_id_comments_post_request=things_thing_id_comments_post_request)

Reply to a comment

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.comment_schema import CommentSchema
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
    api_instance = openapi_client.CommentApi(api_client)
    comment_id = 285620 # int | The id of the comment
    things_thing_id_comments_post_request = openapi_client.ThingsThingIdCommentsPostRequest() # ThingsThingIdCommentsPostRequest |  (optional)

    try:
        # Reply to a comment
        api_response = api_instance.comments_comment_id_reply_post(comment_id, things_thing_id_comments_post_request=things_thing_id_comments_post_request)
        print("The response of CommentApi->comments_comment_id_reply_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentApi->comments_comment_id_reply_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| The id of the comment | 
 **things_thing_id_comments_post_request** | [**ThingsThingIdCommentsPostRequest**](ThingsThingIdCommentsPostRequest.md)|  | [optional] 

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
**200** | A new reply to a comment |  -  |
**400** | Server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_comment_id_restore_post**
> CommentSchema comments_comment_id_restore_post(comment_id)

Restore a deleted comment

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
    api_instance = openapi_client.CommentApi(api_client)
    comment_id = 285620 # int | The id of the comment

    try:
        # Restore a deleted comment
        api_response = api_instance.comments_comment_id_restore_post(comment_id)
        print("The response of CommentApi->comments_comment_id_restore_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentApi->comments_comment_id_restore_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| The id of the comment | 

### Return type

[**CommentSchema**](CommentSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Restored comment |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_comment_id_spam_post**
> CommentSchema comments_comment_id_spam_post(comment_id)

Mark comment as a spam

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
    api_instance = openapi_client.CommentApi(api_client)
    comment_id = 285620 # int | The id of the comment

    try:
        # Mark comment as a spam
        api_response = api_instance.comments_comment_id_spam_post(comment_id)
        print("The response of CommentApi->comments_comment_id_spam_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentApi->comments_comment_id_spam_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| The id of the comment | 

### Return type

[**CommentSchema**](CommentSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The marked comment |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_get**
> List[CommentSchema] comments_get(page=page, per_page=per_page)

Get the latest comments

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
    api_instance = openapi_client.CommentApi(api_client)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get the latest comments
        api_response = api_instance.comments_get(page=page, per_page=per_page)
        print("The response of CommentApi->comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentApi->comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 

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
**200** | The list of comments |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_post**
> CommentSchema comments_post(comment_id, comments_post_request=comments_post_request)

Reply to a comment

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.comment_schema import CommentSchema
from openapi_client.models.comments_post_request import CommentsPostRequest
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
    api_instance = openapi_client.CommentApi(api_client)
    comment_id = 285620 # int | The id of the comment
    comments_post_request = openapi_client.CommentsPostRequest() # CommentsPostRequest |  (optional)

    try:
        # Reply to a comment
        api_response = api_instance.comments_post(comment_id, comments_post_request=comments_post_request)
        print("The response of CommentApi->comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentApi->comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| The id of the comment | 
 **comments_post_request** | [**CommentsPostRequest**](CommentsPostRequest.md)|  | [optional] 

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
**200** | The comment object |  -  |
**400** | Server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

