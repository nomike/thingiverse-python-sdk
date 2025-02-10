# openapi_client.SearchApi

All URIs are relative to *https://api.thingiverse.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_tag_tag_get**](SearchApi.md#search_tag_tag_get) | **GET** /search/{tag}/tag | 
[**search_term_autocomplete_get**](SearchApi.md#search_term_autocomplete_get) | **GET** /search/{term}/autocomplete | 
[**search_term_typecollections_get**](SearchApi.md#search_term_typecollections_get) | **GET** /search/{term}/?type&#x3D;collections | Search for Collections
[**search_term_typemakes_get**](SearchApi.md#search_term_typemakes_get) | **GET** /search/{term}/?type&#x3D;makes | Search for Makes
[**search_term_typethings_get**](SearchApi.md#search_term_typethings_get) | **GET** /search/{term}/?type&#x3D;things | Search for Things
[**search_term_typeusers_get**](SearchApi.md#search_term_typeusers_get) | **GET** /search/{term}/?type&#x3D;users | Search for Users


# **search_tag_tag_get**
> search_tag_tag_get(tag=tag)



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
    api_instance = openapi_client.SearchApi(api_client)
    tag = 'test' # str |  (optional)

    try:
        api_instance.search_tag_tag_get(tag=tag)
    except Exception as e:
        print("Exception when calling SearchApi->search_tag_tag_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  | [optional] 

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

# **search_term_autocomplete_get**
> search_term_autocomplete_get(term=term)



Search data by term for autocomplete

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
    api_instance = openapi_client.SearchApi(api_client)
    term = 'test' # str | The search query to perform (optional)

    try:
        api_instance.search_term_autocomplete_get(term=term)
    except Exception as e:
        print("Exception when calling SearchApi->search_term_autocomplete_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| The search query to perform | [optional] 

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

# **search_term_typecollections_get**
> SearchTermTypeCollectionsGet200Response search_term_typecollections_get(term=term, page=page, per_page=per_page, sort=sort, is_featured=is_featured, liked_by=liked_by)

Search for Collections

See [page](https://www.notion.so/makerbot/Thingiverse-Search-API-f7ce7608d54d44f7a2b902a83194a8b2) for complete documentation and all possible parameters.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.search_term_type_collections_get200_response import SearchTermTypeCollectionsGet200Response
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
    api_instance = openapi_client.SearchApi(api_client)
    term = 'test' # str | The search query to perform (optional)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)
    sort = 'sort_example' # str | Sort method (optional)
    is_featured = 56 # int | Only show Collections that have been featured (optional)
    liked_by = 56 # int | Only show Collections liked by this user ID (optional)

    try:
        # Search for Collections
        api_response = api_instance.search_term_typecollections_get(term=term, page=page, per_page=per_page, sort=sort, is_featured=is_featured, liked_by=liked_by)
        print("The response of SearchApi->search_term_typecollections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_term_typecollections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| The search query to perform | [optional] 
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 
 **sort** | **str**| Sort method | [optional] 
 **is_featured** | **int**| Only show Collections that have been featured | [optional] 
 **liked_by** | **int**| Only show Collections liked by this user ID | [optional] 

### Return type

[**SearchTermTypeCollectionsGet200Response**](SearchTermTypeCollectionsGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of items matching the search |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_term_typemakes_get**
> SearchTermTypeMakesGet200Response search_term_typemakes_get(term=term, page=page, per_page=per_page, sort=sort, user_id=user_id)

Search for Makes

See [page](https://www.notion.so/makerbot/Thingiverse-Search-API-f7ce7608d54d44f7a2b902a83194a8b2) for complete documentation and all possible parameters.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.search_term_type_makes_get200_response import SearchTermTypeMakesGet200Response
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
    api_instance = openapi_client.SearchApi(api_client)
    term = 'test' # str | The search query to perform (optional)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)
    sort = 'sort_example' # str | Sort method (optional)
    user_id = 56 # int | Only show Makes made by this user ID (optional)

    try:
        # Search for Makes
        api_response = api_instance.search_term_typemakes_get(term=term, page=page, per_page=per_page, sort=sort, user_id=user_id)
        print("The response of SearchApi->search_term_typemakes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_term_typemakes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| The search query to perform | [optional] 
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 
 **sort** | **str**| Sort method | [optional] 
 **user_id** | **int**| Only show Makes made by this user ID | [optional] 

### Return type

[**SearchTermTypeMakesGet200Response**](SearchTermTypeMakesGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of items matching the search |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_term_typethings_get**
> SearchTermTypeThingsGet200Response search_term_typethings_get(term=term, page=page, per_page=per_page, sort=sort, posted_before=posted_before, posted_after=posted_after, is_edu_approved=is_edu_approved, subjects=subjects, grades=grades, standards=standards, license=license, customizable=customizable, show_customized=show_customized, order_print=order_print, has_makes=has_makes, is_featured=is_featured, is_fis_challenge_winnereatured=is_fis_challenge_winnereatured, liked_by=liked_by, collected_by=collected_by, made_by=made_by, is_derivative=is_derivative, category_id=category_id)

Search for Things

See [page](https://www.notion.so/makerbot/Thingiverse-Search-API-f7ce7608d54d44f7a2b902a83194a8b2) for complete documentation and all possible parameters.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.search_term_type_things_get200_response import SearchTermTypeThingsGet200Response
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
    api_instance = openapi_client.SearchApi(api_client)
    term = 'test' # str | The search query to perform (optional)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)
    sort = 'sort_example' # str | Sort method (optional)
    posted_before = 'posted_before_example' # str | Only show Things posted before this date. Check out the Elasticsearch date math [docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#date-math) (optional)
    posted_after = 'posted_after_example' # str | Only show Things posted after this date. Check out the Elasticsearch date math [docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#date-math) (optional)
    is_edu_approved = 'is_edu_approved_example' # str | EDU - Only show educational Things (optional)
    subjects = 'subjects_example' # str | EDU - Only show Things marked as for these subject IDs (optional)
    grades = 'grades_example' # str | EDU - Only show Things marked as for these grade IDs (optional)
    standards = 'standards_example' # str | EDU - Only show Things marked as for these standard IDs (optional)
    license = 'license_example' # str | Only show Things with this license (e.g. \"ccsa\" for Creative Commons - Attribution - Share Alike) (optional)
    customizable = 'customizable_example' # str | Only show customizable Things (optional)
    show_customized = 'show_customized_example' # str | Also include Things that have been customized from a different Thing. By default these are filtered out (optional)
    order_print = 'order_print_example' # str | Only show Things that have the \"Order A Print\" feature enabled (optional)
    has_makes = 56 # int | Only show Things that have Makes (optional)
    is_featured = 56 # int | Only show Things that have Makes (optional)
    is_fis_challenge_winnereatured = 56 # int | Only show Things that are marked as a challenge winner (optional)
    liked_by = 'liked_by_example' # str | Only show Things liked by this user ID (optional)
    collected_by = 'collected_by_example' # str | Only show Things collected by this user ID (optional)
    made_by = 'made_by_example' # str | Only show Things made by this user ID (optional)
    is_derivative = 56 # int | Only show remixes (optional)
    category_id = 56 # int | Only show Things in this category ID (optional)

    try:
        # Search for Things
        api_response = api_instance.search_term_typethings_get(term=term, page=page, per_page=per_page, sort=sort, posted_before=posted_before, posted_after=posted_after, is_edu_approved=is_edu_approved, subjects=subjects, grades=grades, standards=standards, license=license, customizable=customizable, show_customized=show_customized, order_print=order_print, has_makes=has_makes, is_featured=is_featured, is_fis_challenge_winnereatured=is_fis_challenge_winnereatured, liked_by=liked_by, collected_by=collected_by, made_by=made_by, is_derivative=is_derivative, category_id=category_id)
        print("The response of SearchApi->search_term_typethings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_term_typethings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| The search query to perform | [optional] 
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 
 **sort** | **str**| Sort method | [optional] 
 **posted_before** | **str**| Only show Things posted before this date. Check out the Elasticsearch date math [docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#date-math) | [optional] 
 **posted_after** | **str**| Only show Things posted after this date. Check out the Elasticsearch date math [docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#date-math) | [optional] 
 **is_edu_approved** | **str**| EDU - Only show educational Things | [optional] 
 **subjects** | **str**| EDU - Only show Things marked as for these subject IDs | [optional] 
 **grades** | **str**| EDU - Only show Things marked as for these grade IDs | [optional] 
 **standards** | **str**| EDU - Only show Things marked as for these standard IDs | [optional] 
 **license** | **str**| Only show Things with this license (e.g. \&quot;ccsa\&quot; for Creative Commons - Attribution - Share Alike) | [optional] 
 **customizable** | **str**| Only show customizable Things | [optional] 
 **show_customized** | **str**| Also include Things that have been customized from a different Thing. By default these are filtered out | [optional] 
 **order_print** | **str**| Only show Things that have the \&quot;Order A Print\&quot; feature enabled | [optional] 
 **has_makes** | **int**| Only show Things that have Makes | [optional] 
 **is_featured** | **int**| Only show Things that have Makes | [optional] 
 **is_fis_challenge_winnereatured** | **int**| Only show Things that are marked as a challenge winner | [optional] 
 **liked_by** | **str**| Only show Things liked by this user ID | [optional] 
 **collected_by** | **str**| Only show Things collected by this user ID | [optional] 
 **made_by** | **str**| Only show Things made by this user ID | [optional] 
 **is_derivative** | **int**| Only show remixes | [optional] 
 **category_id** | **int**| Only show Things in this category ID | [optional] 

### Return type

[**SearchTermTypeThingsGet200Response**](SearchTermTypeThingsGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of items matching the search |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_term_typeusers_get**
> SearchTermTypeUsersGet200Response search_term_typeusers_get(term=term, page=page, per_page=per_page, sort=sort, users_thing_count=users_thing_count, users_user_types=users_user_types, skill_level=skill_level, programs=programs)

Search for Users

See [page](https://www.notion.so/makerbot/Thingiverse-Search-API-f7ce7608d54d44f7a2b902a83194a8b2) for complete documentation and all possible parameters.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.search_term_type_users_get200_response import SearchTermTypeUsersGet200Response
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
    api_instance = openapi_client.SearchApi(api_client)
    term = 'test' # str | The search query to perform (optional)
    page = 1 # int | Page for pagination (optional)
    per_page = 30 # int | Amount of results to show per page (optional)
    sort = 'sort_example' # str | Sort method (optional)
    users_thing_count = 56 # int | Only show users that have at least 1 published Thing (optional)
    users_user_types = 4 # int | Only show users that are of this type (optional)
    skill_level = 'skill_level_example' # str | Only show users that are of this skill level (optional)
    programs = 35 # int | Only show users that use this design program (optional)

    try:
        # Search for Users
        api_response = api_instance.search_term_typeusers_get(term=term, page=page, per_page=per_page, sort=sort, users_thing_count=users_thing_count, users_user_types=users_user_types, skill_level=skill_level, programs=programs)
        print("The response of SearchApi->search_term_typeusers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_term_typeusers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| The search query to perform | [optional] 
 **page** | **int**| Page for pagination | [optional] 
 **per_page** | **int**| Amount of results to show per page | [optional] 
 **sort** | **str**| Sort method | [optional] 
 **users_thing_count** | **int**| Only show users that have at least 1 published Thing | [optional] 
 **users_user_types** | **int**| Only show users that are of this type | [optional] 
 **skill_level** | **str**| Only show users that are of this skill level | [optional] 
 **programs** | **int**| Only show users that use this design program | [optional] 

### Return type

[**SearchTermTypeUsersGet200Response**](SearchTermTypeUsersGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of items matching the search |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Attempting to fetch |  -  |
**404** | Invalid or deleted item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

