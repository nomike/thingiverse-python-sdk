# openapi_client.BannerApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**banner0_page_ad_get**](BannerApi.md#banner0_page_ad_get) | **GET** /banner/0/page-ad | Get banner (ad) for a certain page
[**banner_get**](BannerApi.md#banner_get) | **GET** /banner | Get a banner (ad)


# **banner0_page_ad_get**
> Banner0PageAdGet200Response banner0_page_ad_get(location, query=query, category_id=category_id, type=type, search=search)

Get banner (ad) for a certain page

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.banner0_page_ad_get200_response import Banner0PageAdGet200Response
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
    api_instance = openapi_client.BannerApi(api_client)
    location = 'location_example' # str | This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page
    query = '3D' # str | This parameter is used as a keyword to perform a search in link parameter of banner (optional)
    category_id = 63 # int | The id of thing category (optional)
    type = 'type_example' # str | The type of link of the banner (optional)
    search = 'q=test&page=1&type=things&sort=relevant' # str | This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner (optional)

    try:
        # Get banner (ad) for a certain page
        api_response = api_instance.banner0_page_ad_get(location, query=query, category_id=category_id, type=type, search=search)
        print("The response of BannerApi->banner0_page_ad_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BannerApi->banner0_page_ad_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page | 
 **query** | **str**| This parameter is used as a keyword to perform a search in link parameter of banner | [optional] 
 **category_id** | **int**| The id of thing category | [optional] 
 **type** | **str**| The type of link of the banner | [optional] 
 **search** | **str**| This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner | [optional] 

### Return type

[**Banner0PageAdGet200Response**](Banner0PageAdGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object representing the banner requested |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **banner_get**
> BannerSchema banner_get(location, query=query, category_id=category_id, type=type, search=search)

Get a banner (ad)

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.banner_schema import BannerSchema
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
    api_instance = openapi_client.BannerApi(api_client)
    location = 'location_example' # str | This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page
    query = '3D' # str | This parameter is used as a keyword to perform a search by link parameter of banner (optional)
    category_id = 63 # int | The id of thing category (optional)
    type = 'type_example' # str | The type of link of the banner (optional)
    search = 'q=test&page=1&type=things&sort=relevant' # str | This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner (optional)

    try:
        # Get a banner (ad)
        api_response = api_instance.banner_get(location, query=query, category_id=category_id, type=type, search=search)
        print("The response of BannerApi->banner_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BannerApi->banner_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page | 
 **query** | **str**| This parameter is used as a keyword to perform a search by link parameter of banner | [optional] 
 **category_id** | **int**| The id of thing category | [optional] 
 **type** | **str**| The type of link of the banner | [optional] 
 **search** | **str**| This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner | [optional] 

### Return type

[**BannerSchema**](BannerSchema.md)

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

