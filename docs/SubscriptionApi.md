# openapi_client.SubscriptionApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events0_read_all_post**](SubscriptionApi.md#events0_read_all_post) | **POST** /events/0/read-all | Read all subscription-events of user
[**events_id_delete**](SubscriptionApi.md#events_id_delete) | **DELETE** /events/{id} | Delete event by id
[**subscriptions0_analytics_get**](SubscriptionApi.md#subscriptions0_analytics_get) | **GET** /subscriptions/0/analytics | Get activity analytics from the last 30 Days of a certain user
[**subscriptions0_dashboard_get**](SubscriptionApi.md#subscriptions0_dashboard_get) | **GET** /subscriptions/0/dashboard | Get activities of User in Dashboard page
[**subscriptions0_dashboard_sources_get**](SubscriptionApi.md#subscriptions0_dashboard_sources_get) | **GET** /subscriptions/0/dashboard-sources | Get activity sources for editing the dashboard feed
[**subscriptions_tag_is_user_subscribed_to_tag_get**](SubscriptionApi.md#subscriptions_tag_is_user_subscribed_to_tag_get) | **GET** /subscriptions/{tag}/is-user-subscribed-to-tag | Check if user is subscribed to the tag
[**subscriptions_tag_set_subscribe_state_post**](SubscriptionApi.md#subscriptions_tag_set_subscribe_state_post) | **POST** /subscriptions/{tag}/set-subscribe-state | Subscribe a user to a tag


# **events0_read_all_post**
> ThingsThingIdDelete200Response events0_read_all_post(id)

Read all subscription-events of user

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
    api_instance = openapi_client.SubscriptionApi(api_client)
    id = 2858045 # int | A id of an existing user.

    try:
        # Read all subscription-events of user
        api_response = api_instance.events0_read_all_post(id)
        print("The response of SubscriptionApi->events0_read_all_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->events0_read_all_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A id of an existing user. | 

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
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_id_delete**
> ThingsThingIdDelete200Response events_id_delete(id)

Delete event by id

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
    api_instance = openapi_client.SubscriptionApi(api_client)
    id = 1 # int | id of event

    try:
        # Delete event by id
        api_response = api_instance.events_id_delete(id)
        print("The response of SubscriptionApi->events_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->events_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of event | 

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

# **subscriptions0_analytics_get**
> Subscriptions0AnalyticsGet200Response subscriptions0_analytics_get()

Get activity analytics from the last 30 Days of a certain user

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.subscriptions0_analytics_get200_response import Subscriptions0AnalyticsGet200Response
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
    api_instance = openapi_client.SubscriptionApi(api_client)

    try:
        # Get activity analytics from the last 30 Days of a certain user
        api_response = api_instance.subscriptions0_analytics_get()
        print("The response of SubscriptionApi->subscriptions0_analytics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions0_analytics_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Subscriptions0AnalyticsGet200Response**](Subscriptions0AnalyticsGet200Response.md)

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

# **subscriptions0_dashboard_get**
> Subscriptions0DashboardGet200Response subscriptions0_dashboard_get(type, page=page, per_page=per_page)

Get activities of User in Dashboard page

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.subscriptions0_dashboard_get200_response import Subscriptions0DashboardGet200Response
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
    api_instance = openapi_client.SubscriptionApi(api_client)
    type = 'type_example' # str | Type of user activity
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # Get activities of User in Dashboard page
        api_response = api_instance.subscriptions0_dashboard_get(type, page=page, per_page=per_page)
        print("The response of SubscriptionApi->subscriptions0_dashboard_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions0_dashboard_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of user activity | 
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 

### Return type

[**Subscriptions0DashboardGet200Response**](Subscriptions0DashboardGet200Response.md)

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

# **subscriptions0_dashboard_sources_get**
> Dict[str, List[Subscriptions0DashboardSourcesGet200ResponseValueInner]] subscriptions0_dashboard_sources_get()

Get activity sources for editing the dashboard feed

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.subscriptions0_dashboard_sources_get200_response_value_inner import Subscriptions0DashboardSourcesGet200ResponseValueInner
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
    api_instance = openapi_client.SubscriptionApi(api_client)

    try:
        # Get activity sources for editing the dashboard feed
        api_response = api_instance.subscriptions0_dashboard_sources_get()
        print("The response of SubscriptionApi->subscriptions0_dashboard_sources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions0_dashboard_sources_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, List[Subscriptions0DashboardSourcesGet200ResponseValueInner]]**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_tag_is_user_subscribed_to_tag_get**
> bool subscriptions_tag_is_user_subscribed_to_tag_get(tag)

Check if user is subscribed to the tag

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
    api_instance = openapi_client.SubscriptionApi(api_client)
    tag = 'laser' # str | A tag that is valid (already exists)

    try:
        # Check if user is subscribed to the tag
        api_response = api_instance.subscriptions_tag_is_user_subscribed_to_tag_get(tag)
        print("The response of SubscriptionApi->subscriptions_tag_is_user_subscribed_to_tag_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_tag_is_user_subscribed_to_tag_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| A tag that is valid (already exists) | 

### Return type

**bool**

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

# **subscriptions_tag_set_subscribe_state_post**
> bool subscriptions_tag_set_subscribe_state_post(tag, subscriptions_tag_set_subscribe_state_post_request=subscriptions_tag_set_subscribe_state_post_request)

Subscribe a user to a tag

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.subscriptions_tag_set_subscribe_state_post_request import SubscriptionsTagSetSubscribeStatePostRequest
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
    api_instance = openapi_client.SubscriptionApi(api_client)
    tag = 'laser' # str | A tag that is valid (already exists)
    subscriptions_tag_set_subscribe_state_post_request = openapi_client.SubscriptionsTagSetSubscribeStatePostRequest() # SubscriptionsTagSetSubscribeStatePostRequest |  (optional)

    try:
        # Subscribe a user to a tag
        api_response = api_instance.subscriptions_tag_set_subscribe_state_post(tag, subscriptions_tag_set_subscribe_state_post_request=subscriptions_tag_set_subscribe_state_post_request)
        print("The response of SubscriptionApi->subscriptions_tag_set_subscribe_state_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_tag_set_subscribe_state_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| A tag that is valid (already exists) | 
 **subscriptions_tag_set_subscribe_state_post_request** | [**SubscriptionsTagSetSubscribeStatePostRequest**](SubscriptionsTagSetSubscribeStatePostRequest.md)|  | [optional] 

### Return type

**bool**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

