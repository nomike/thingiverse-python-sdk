# openapi_client.FileApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**files0_upload_file_post**](FileApi.md#files0_upload_file_post) | **POST** /files/0/uploadFile | Upload a file as pendingupload
[**files_file_id_download_get**](FileApi.md#files_file_id_download_get) | **GET** /files/{file_id}/download | Get tracked download URL
[**files_file_id_get**](FileApi.md#files_file_id_get) | **GET** /files/{file_id}/ | Get info about a file by id


# **files0_upload_file_post**
> Files0UploadFilePost200Response files0_upload_file_post(file=file)

Upload a file as pendingupload

Upload a file to the storageBucket as \"pendingUpload\". The file will be stored in a temporary folder until it is finalized (eg; associated with a thing/make/comment/etc) via the /finalize endpoint.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.files0_upload_file_post200_response import Files0UploadFilePost200Response
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
    api_instance = openapi_client.FileApi(api_client)
    file = None # bytearray |  (optional)

    try:
        # Upload a file as pendingupload
        api_response = api_instance.files0_upload_file_post(file=file)
        print("The response of FileApi->files0_upload_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->files0_upload_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 

### Return type

[**Files0UploadFilePost200Response**](Files0UploadFilePost200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The id of the pendingupload. You will need this one when finalizing the upload. |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**400** | Server cannot or will not process the request due to something that is perceived to be a client error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_file_id_download_get**
> files_file_id_download_get(file_id)

Get tracked download URL

Redirects to the requested file and adds an entry to the user's download history for use with the GET /users/{$username}/downloads endpoint, as opposed to the public url which is anonymous.

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
    api_instance = openapi_client.FileApi(api_client)
    file_id = 1 # int | The id of the file

    try:
        # Get tracked download URL
        api_instance.files_file_id_download_get(file_id)
    except Exception as e:
        print("Exception when calling FileApi->files_file_id_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The id of the file | 

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

# **files_file_id_get**
> FileSchema files_file_id_get(file_id)

Get info about a file by id

Get basic information about how to access a file. For relevant files, a thumbnail image or three.js json file may be available.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.file_schema import FileSchema
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
    api_instance = openapi_client.FileApi(api_client)
    file_id = 1 # int | The id of the file

    try:
        # Get info about a file by id
        api_response = api_instance.files_file_id_get(file_id)
        print("The response of FileApi->files_file_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->files_file_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The id of the file | 

### Return type

[**FileSchema**](FileSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object with urls of the file requested |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

