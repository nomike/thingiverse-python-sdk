# openapi_client.PrinterApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**printers0_brands_get**](PrinterApi.md#printers0_brands_get) | **GET** /printers/0/brands | Get a list of all known printer brands
[**printers0_models_get**](PrinterApi.md#printers0_models_get) | **GET** /printers/0/models | Get a list of known printers


# **printers0_brands_get**
> List[Printers0BrandsGet200ResponseInner] printers0_brands_get(include_user_defined=include_user_defined)

Get a list of all known printer brands

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.printers0_brands_get200_response_inner import Printers0BrandsGet200ResponseInner
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
    api_instance = openapi_client.PrinterApi(api_client)
    include_user_defined = True # bool | Should brands / printers defined by users be included? (optional)

    try:
        # Get a list of all known printer brands
        api_response = api_instance.printers0_brands_get(include_user_defined=include_user_defined)
        print("The response of PrinterApi->printers0_brands_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterApi->printers0_brands_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_user_defined** | **bool**| Should brands / printers defined by users be included? | [optional] 

### Return type

[**List[Printers0BrandsGet200ResponseInner]**](Printers0BrandsGet200ResponseInner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of printer brands |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **printers0_models_get**
> List[Printers0ModelsGet200ResponseInner] printers0_models_get(include_user_defined=include_user_defined, brand=brand)

Get a list of known printers

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.printers0_models_get200_response_inner import Printers0ModelsGet200ResponseInner
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
    api_instance = openapi_client.PrinterApi(api_client)
    include_user_defined = True # bool | Should brands / printers defined by users be included? (optional)
    brand = 'Ultimaker' # str | By what brand should the results be filtered? (optional)

    try:
        # Get a list of known printers
        api_response = api_instance.printers0_models_get(include_user_defined=include_user_defined, brand=brand)
        print("The response of PrinterApi->printers0_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterApi->printers0_models_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_user_defined** | **bool**| Should brands / printers defined by users be included? | [optional] 
 **brand** | **str**| By what brand should the results be filtered? | [optional] 

### Return type

[**List[Printers0ModelsGet200ResponseInner]**](Printers0ModelsGet200ResponseInner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of known printers |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

