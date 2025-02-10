# openapi_client.EventApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_get**](EventApi.md#events_get) | **GET** /events | List of events
[**events_id_get**](EventApi.md#events_id_get) | **GET** /events/{id} | Get event by id


# **events_get**
> List[EventSchema] events_get(page=page, per_page=per_page)

List of events

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.event_schema import EventSchema
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
    api_instance = openapi_client.EventApi(api_client)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)

    try:
        # List of events
        api_response = api_instance.events_get(page=page, per_page=per_page)
        print("The response of EventApi->events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 

### Return type

[**List[EventSchema]**](EventSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of events |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_id_get**
> EventSchema events_id_get(id)

Get event by id

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.event_schema import EventSchema
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
    api_instance = openapi_client.EventApi(api_client)
    id = 99 # int | The id of the event to get

    try:
        # Get event by id
        api_response = api_instance.events_id_get(id)
        print("The response of EventApi->events_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->events_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the event to get | 

### Return type

[**EventSchema**](EventSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object representing the event requested |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

