# carbon3d.PartsApi

All URIs are relative to *https://api.carbon3d.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_part**](PartsApi.md#create_part) | **POST** /parts | Create a Part
[**get_part**](PartsApi.md#get_part) | **GET** /parts/{uuid} | Fetch a Part
[**get_parts**](PartsApi.md#get_parts) | **GET** /parts | Fetch parts


# **create_part**
> Part create_part(part_request=part_request)

Create a Part

Create a part from a model.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import carbon3d
from carbon3d.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.carbon3d.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = carbon3d.Configuration(
    host = "https://api.carbon3d.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = carbon3d.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with carbon3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = carbon3d.PartsApi(api_client)
    part_request = carbon3d.PartRequest() # PartRequest | A new Part to be created. (optional)

    try:
        # Create a Part
        api_response = api_instance.create_part(part_request=part_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartsApi->create_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **part_request** | [**PartRequest**](PartRequest.md)| A new Part to be created. | [optional] 

### Return type

[**Part**](Part.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_part**
> Part get_part(uuid)

Fetch a Part

Fetch the details of a single Part.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import carbon3d
from carbon3d.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.carbon3d.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = carbon3d.Configuration(
    host = "https://api.carbon3d.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = carbon3d.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with carbon3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = carbon3d.PartsApi(api_client)
    uuid = 'uuid_example' # str | A unique identifier for a Part.

    try:
        # Fetch a Part
        api_response = api_instance.get_part(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartsApi->get_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A unique identifier for a Part. | 

### Return type

[**Part**](Part.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**404** | The part does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parts**
> PartsResponse get_parts(limit, offset, model_uuid=model_uuid, sort=sort)

Fetch parts

Gets a list of `Part` entities (most recent first)

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import carbon3d
from carbon3d.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.carbon3d.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = carbon3d.Configuration(
    host = "https://api.carbon3d.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = carbon3d.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with carbon3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = carbon3d.PartsApi(api_client)
    limit = 100 # int | Max records to return (default to 100)
offset = 0 # int | Number of items to skip (default to 0)
model_uuid = 'model_uuid_example' # str | Model UUID (optional)
sort = ['sort_example'] # list[str] | Field(s) to sort by. Ascending order by default, use `sort=field,desc` to specify descending order. Sortable fields are: `part_number` (optional)

    try:
        # Fetch parts
        api_response = api_instance.get_parts(limit, offset, model_uuid=model_uuid, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartsApi->get_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max records to return | [default to 100]
 **offset** | **int**| Number of items to skip | [default to 0]
 **model_uuid** | **str**| Model UUID | [optional] 
 **sort** | [**list[str]**](str.md)| Field(s) to sort by. Ascending order by default, use &#x60;sort&#x3D;field,desc&#x60; to specify descending order. Sortable fields are: &#x60;part_number&#x60; | [optional] 

### Return type

[**PartsResponse**](PartsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

