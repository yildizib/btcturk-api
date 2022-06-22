# swagger_client.RemainderApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_remainder_get**](RemainderApi.md#api_v3_remainder_get) | **GET** /api/v3/remainder | 
[**api_v3_remainder_post**](RemainderApi.md#api_v3_remainder_post) | **POST** /api/v3/remainder | 

# **api_v3_remainder_get**
> api_v3_remainder_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RemainderApi(swagger_client.ApiClient(configuration))

try:
    api_instance.api_v3_remainder_get()
except ApiException as e:
    print("Exception when calling RemainderApi->api_v3_remainder_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_remainder_post**
> api_v3_remainder_post(currency_ıd=currency_ıd)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RemainderApi(swagger_client.ApiClient(configuration))
currency_ıd = 789 # int |  (optional)

try:
    api_instance.api_v3_remainder_post(currency_ıd=currency_ıd)
except ApiException as e:
    print("Exception when calling RemainderApi->api_v3_remainder_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_ıd** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

