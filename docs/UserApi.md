# openapi_client.UserApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_username_all_collected_things_get**](UserApi.md#users_username_all_collected_things_get) | **GET** /users/{username}/all-collected-things | Get latest downloaded things by user
[**users_username_avatar_image_post**](UserApi.md#users_username_avatar_image_post) | **POST** /users/{username}/avatar-image | Update the avatar image
[**users_username_collections_get**](UserApi.md#users_username_collections_get) | **GET** /users/{username}/collections | Get latest copies by user
[**users_username_copies_get**](UserApi.md#users_username_copies_get) | **GET** /users/{username}/copies | Get latest copies by user
[**users_username_cover_image_post**](UserApi.md#users_username_cover_image_post) | **POST** /users/{username}/cover-image | Update the cover image
[**users_username_delete**](UserApi.md#users_username_delete) | **DELETE** /users/{username} | Soft delete a user&#39;s account
[**users_username_downloads_get**](UserApi.md#users_username_downloads_get) | **GET** /users/{username}/downloads | Get latest downloaded things by user
[**users_username_event_count_get**](UserApi.md#users_username_event_count_get) | **GET** /users/{username}/event-count | Get the count of events for user since the timestamp sent
[**users_username_favorites_get**](UserApi.md#users_username_favorites_get) | **GET** /users/{username}/favorites | Get favorites by user
[**users_username_followers_delete**](UserApi.md#users_username_followers_delete) | **DELETE** /users/{username}/followers | Unfollow an user
[**users_username_followers_get**](UserApi.md#users_username_followers_get) | **GET** /users/{username}/followers | Get followers
[**users_username_followers_post**](UserApi.md#users_username_followers_post) | **POST** /users/{username}/followers | Follow an user
[**users_username_following_get**](UserApi.md#users_username_following_get) | **GET** /users/{username}/following | Get array of users that requested user is following
[**users_username_get**](UserApi.md#users_username_get) | **GET** /users/{username} | Get the specified user
[**users_username_likes_get**](UserApi.md#users_username_likes_get) | **GET** /users/{username}/likes | Get things liked by user
[**users_username_likesids_get**](UserApi.md#users_username_likesids_get) | **GET** /users/{username}/likesids | Get all things id&#39;s like by user
[**users_username_patch**](UserApi.md#users_username_patch) | **PATCH** /users/{username} | Update the user&#39;s profile
[**users_username_recommended_tags_get**](UserApi.md#users_username_recommended_tags_get) | **GET** /users/{username}/recommended-tags | Get the list of personal tags.
[**users_username_recommended_things_get**](UserApi.md#users_username_recommended_things_get) | **GET** /users/{username}/recommended-things | Get a bunch random things from categories based on the users likes and collected things
[**users_username_search_term_get**](UserApi.md#users_username_search_term_get) | **GET** /users/{username}/search/{term} | Search data by user
[**users_username_stats_by_day_start_date_end_date_get**](UserApi.md#users_username_stats_by_day_start_date_end_date_get) | **GET** /users/{username}/stats-by-day/{startDate}/{endDate} | Get user&#39;s analytics of viewing and downloading things per day
[**users_username_stats_by_thing_start_date_end_date_get**](UserApi.md#users_username_stats_by_thing_start_date_end_date_get) | **GET** /users/{username}/stats-by-thing/{startDate}/{endDate} | Get user&#39;s analytics of viewing and downloading by things
[**users_username_things_get**](UserApi.md#users_username_things_get) | **GET** /users/{username}/things | Get things by user
[**users_username_unread_message_count_get**](UserApi.md#users_username_unread_message_count_get) | **GET** /users/{username}/unread-message-count | Get the count of messages for user


# **users_username_all_collected_things_get**
> object users_username_all_collected_things_get(username)

Get latest downloaded things by user

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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected

    try:
        # Get latest downloaded things by user
        api_response = api_instance.users_username_all_collected_things_get(username)
        print("The response of UserApi->users_username_all_collected_things_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_all_collected_things_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 

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
**200** | All things that the user added to the collection |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_avatar_image_post**
> object users_username_avatar_image_post(username, users_username_avatar_image_post_request=users_username_avatar_image_post_request)

Update the avatar image

Must use the POST method

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.users_username_avatar_image_post_request import UsersUsernameAvatarImagePostRequest
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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected
    users_username_avatar_image_post_request = openapi_client.UsersUsernameAvatarImagePostRequest() # UsersUsernameAvatarImagePostRequest |  (optional)

    try:
        # Update the avatar image
        api_response = api_instance.users_username_avatar_image_post(username, users_username_avatar_image_post_request=users_username_avatar_image_post_request)
        print("The response of UserApi->users_username_avatar_image_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_avatar_image_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 
 **users_username_avatar_image_post_request** | [**UsersUsernameAvatarImagePostRequest**](UsersUsernameAvatarImagePostRequest.md)|  | [optional] 

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
**200** | The data needed to upload a file via an HTTP POST with multipart/form-data encoding. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_collections_get**
> List[str] users_username_collections_get(username, page=page, per_page=per_page)

Get latest copies by user

If the user doesn't exist, result is 404 Not Found.

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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get latest copies by user
        api_response = api_instance.users_username_collections_get(username, page=page, per_page=per_page)
        print("The response of UserApi->users_username_collections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_collections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 
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
**200** | Collection objects |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_copies_get**
> List[str] users_username_copies_get(username, page=page, per_page=per_page)

Get latest copies by user

If the user doesn't exist, result is 404 Not Found.

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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get latest copies by user
        api_response = api_instance.users_username_copies_get(username, page=page, per_page=per_page)
        print("The response of UserApi->users_username_copies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_copies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 
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
**200** | Copy objects |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_cover_image_post**
> object users_username_cover_image_post(username, users_username_avatar_image_post_request=users_username_avatar_image_post_request)

Update the cover image

Must use the POST method

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.users_username_avatar_image_post_request import UsersUsernameAvatarImagePostRequest
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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected
    users_username_avatar_image_post_request = openapi_client.UsersUsernameAvatarImagePostRequest() # UsersUsernameAvatarImagePostRequest |  (optional)

    try:
        # Update the cover image
        api_response = api_instance.users_username_cover_image_post(username, users_username_avatar_image_post_request=users_username_avatar_image_post_request)
        print("The response of UserApi->users_username_cover_image_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_cover_image_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 
 **users_username_avatar_image_post_request** | [**UsersUsernameAvatarImagePostRequest**](UsersUsernameAvatarImagePostRequest.md)|  | [optional] 

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
**200** | The data needed to upload a file via an HTTP POST with multipart/form-data encoding. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_delete**
> ThingsThingIdDelete200Response users_username_delete(username)

Soft delete a user's account

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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected

    try:
        # Soft delete a user's account
        api_response = api_instance.users_username_delete(username)
        print("The response of UserApi->users_username_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 

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

# **users_username_downloads_get**
> List[ThingSchema] users_username_downloads_get(username, page=page, per_page=per_page)

Get latest downloaded things by user

If the user doesn't exist, result is 404 Not Found.

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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get latest downloaded things by user
        api_response = api_instance.users_username_downloads_get(username, page=page, per_page=per_page)
        print("The response of UserApi->users_username_downloads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_downloads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 
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
**200** | Thing objects |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_event_count_get**
> UsersUsernameEventCountGet200Response users_username_event_count_get(username, timestamp=timestamp)

Get the count of events for user since the timestamp sent

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.users_username_event_count_get200_response import UsersUsernameEventCountGet200Response
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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected
    timestamp = 'timestamp_example' # str | The timestamp to check against UTC (YYYY-MM-DDThh:mm:ssTZD) (optional)

    try:
        # Get the count of events for user since the timestamp sent
        api_response = api_instance.users_username_event_count_get(username, timestamp=timestamp)
        print("The response of UserApi->users_username_event_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_event_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 
 **timestamp** | **str**| The timestamp to check against UTC (YYYY-MM-DDThh:mm:ssTZD) | [optional] 

### Return type

[**UsersUsernameEventCountGet200Response**](UsersUsernameEventCountGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The count of events |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_favorites_get**
> List[str] users_username_favorites_get(username, page=page, per_page=per_page)

Get favorites by user

If an authenticated user is requesting their own list of favorites, If the user doesn't exist, result is 404 Not Found

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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get favorites by user
        api_response = api_instance.users_username_favorites_get(username, page=page, per_page=per_page)
        print("The response of UserApi->users_username_favorites_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_favorites_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 
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
**200** | Favorite objects. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_followers_delete**
> object users_username_followers_delete(username)

Unfollow an user

Must use the DELETE method Result will be 404 Not Found if the user doesn't exist.

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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected

    try:
        # Unfollow an user
        api_response = api_instance.users_username_followers_delete(username)
        print("The response of UserApi->users_username_followers_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_followers_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 

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
**200** | The \&quot;ok\&quot; object. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_followers_get**
> List[UserSummarySchema] users_username_followers_get(username)

Get followers

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.user_summary_schema import UserSummarySchema
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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected

    try:
        # Get followers
        api_response = api_instance.users_username_followers_get(username)
        print("The response of UserApi->users_username_followers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_followers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 

### Return type

[**List[UserSummarySchema]**](UserSummarySchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of users |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_followers_post**
> object users_username_followers_post(username)

Follow an user

Must use the POST method Result will be 404 Not Found if the user doesn't exist. Result will be 400 Bad Request if the user is trying to follow itself.

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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected

    try:
        # Follow an user
        api_response = api_instance.users_username_followers_post(username)
        print("The response of UserApi->users_username_followers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_followers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 

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
**200** | The \&quot;ok\&quot; object. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_following_get**
> List[UserSummarySchema] users_username_following_get(username)

Get array of users that requested user is following

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.user_summary_schema import UserSummarySchema
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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected

    try:
        # Get array of users that requested user is following
        api_response = api_instance.users_username_following_get(username)
        print("The response of UserApi->users_username_following_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_following_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 

### Return type

[**List[UserSummarySchema]**](UserSummarySchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of users |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_get**
> UserSchema users_username_get(username)

Get the specified user

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.user_schema import UserSchema
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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected

    try:
        # Get the specified user
        api_response = api_instance.users_username_get(username)
        print("The response of UserApi->users_username_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 

### Return type

[**UserSchema**](UserSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_likes_get**
> List[ThingSchema] users_username_likes_get(username, page=page, per_page=per_page)

Get things liked by user

If the user doesn't exist, result is 404 Not Found

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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get things liked by user
        api_response = api_instance.users_username_likes_get(username, page=page, per_page=per_page)
        print("The response of UserApi->users_username_likes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_likes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 
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
**200** | Thing objects |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_likesids_get**
> List[int] users_username_likesids_get(username)

Get all things id's like by user

If the user doesn't exist, result is 404 Not Found

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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected

    try:
        # Get all things id's like by user
        api_response = api_instance.users_username_likesids_get(username)
        print("The response of UserApi->users_username_likesids_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_likesids_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 

### Return type

**List[int]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | array of thing ids |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_patch**
> UserSchema users_username_patch(username, users_username_patch_request=users_username_patch_request)

Update the user's profile

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.users_username_patch_request import UsersUsernamePatchRequest
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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected
    users_username_patch_request = openapi_client.UsersUsernamePatchRequest() # UsersUsernamePatchRequest |  (optional)

    try:
        # Update the user's profile
        api_response = api_instance.users_username_patch(username, users_username_patch_request=users_username_patch_request)
        print("The response of UserApi->users_username_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 
 **users_username_patch_request** | [**UsersUsernamePatchRequest**](UsersUsernamePatchRequest.md)|  | [optional] 

### Return type

[**UserSchema**](UserSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated user |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_recommended_tags_get**
> List[TagSchema] users_username_recommended_tags_get(username)

Get the list of personal tags.

returns a list of Recommended tags which are based on the users likes and collected things.

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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected

    try:
        # Get the list of personal tags.
        api_response = api_instance.users_username_recommended_tags_get(username)
        print("The response of UserApi->users_username_recommended_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_recommended_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 

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

# **users_username_recommended_things_get**
> List[ThingSchema] users_username_recommended_things_get(username, page=page, per_page=per_page)

Get a bunch random things from categories based on the users likes and collected things

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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get a bunch random things from categories based on the users likes and collected things
        api_response = api_instance.users_username_recommended_things_get(username, page=page, per_page=per_page)
        print("The response of UserApi->users_username_recommended_things_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_recommended_things_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 
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
**200** | An array of objects with thing and category |  * total-count - How many results in total does this have. Note that this can be higher than the results you got. In that case you can use the page query to get the others. <br>  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_search_term_get**
> UsersUsernameSearchTermGet200Response users_username_search_term_get(username, term=term)

Search data by user

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.users_username_search_term_get200_response import UsersUsernameSearchTermGet200Response
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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected
    term = 'term_example' # str | The search query to perform (optional)

    try:
        # Search data by user
        api_response = api_instance.users_username_search_term_get(username, term=term)
        print("The response of UserApi->users_username_search_term_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_search_term_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 
 **term** | **str**| The search query to perform | [optional] 

### Return type

[**UsersUsernameSearchTermGet200Response**](UsersUsernameSearchTermGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The returned hits can either be things, makes, users or collections |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_stats_by_day_start_date_end_date_get**
> List[UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner] users_username_stats_by_day_start_date_end_date_get(username, start_date, end_date)

Get user's analytics of viewing and downloading things per day

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.users_username_stats_by_day_start_date_end_date_get200_response_inner import UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner
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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected
    start_date = '2023-03-28' # str | The day from which analytics are shown
    end_date = '2023-04-27' # str | The day till which analytics are shown

    try:
        # Get user's analytics of viewing and downloading things per day
        api_response = api_instance.users_username_stats_by_day_start_date_end_date_get(username, start_date, end_date)
        print("The response of UserApi->users_username_stats_by_day_start_date_end_date_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_stats_by_day_start_date_end_date_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 
 **start_date** | **str**| The day from which analytics are shown | 
 **end_date** | **str**| The day till which analytics are shown | 

### Return type

[**List[UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner]**](UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of stats per day |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | There are no published things |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_stats_by_thing_start_date_end_date_get**
> List[UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner] users_username_stats_by_thing_start_date_end_date_get(username, start_date, end_date)

Get user's analytics of viewing and downloading by things

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.users_username_stats_by_day_start_date_end_date_get200_response_inner import UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner
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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected
    start_date = '2023-03-28' # str | The day from which analytics are shown
    end_date = '2023-04-27' # str | The day till which analytics are shown

    try:
        # Get user's analytics of viewing and downloading by things
        api_response = api_instance.users_username_stats_by_thing_start_date_end_date_get(username, start_date, end_date)
        print("The response of UserApi->users_username_stats_by_thing_start_date_end_date_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_stats_by_thing_start_date_end_date_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 
 **start_date** | **str**| The day from which analytics are shown | 
 **end_date** | **str**| The day till which analytics are shown | 

### Return type

[**List[UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner]**](UsersUsernameStatsByDayStartDateEndDateGet200ResponseInner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of stats per day |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | There are no published things |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_things_get**
> List[ThingSchema] users_username_things_get(username, page=page, per_page=per_page)

Get things by user

If an authenticated user is requesting their own list of things, unpublished things will also appear in the list. If the user doesn't exist, result is 404 Not Found

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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get things by user
        api_response = api_instance.users_username_things_get(username, page=page, per_page=per_page)
        print("The response of UserApi->users_username_things_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_things_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 
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
**200** | Thing objects. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_unread_message_count_get**
> object users_username_unread_message_count_get(username)

Get the count of messages for user

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
    api_instance = openapi_client.UserApi(api_client)
    username = 'thingiverse' # str | The username of the user affected

    try:
        # Get the count of messages for user
        api_response = api_instance.users_username_unread_message_count_get(username)
        print("The response of UserApi->users_username_unread_message_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_username_unread_message_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user affected | 

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
**200** | The count of messages |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

