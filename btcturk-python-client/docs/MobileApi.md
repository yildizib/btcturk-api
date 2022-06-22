# swagger_client.MobileApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_mobile_ınit_get**](MobileApi.md#api_v3_mobile_ınit_get) | **GET** /api/v3/mobile/init | 

# **api_v3_mobile_ınit_get**
> MobileSettingModel api_v3_mobile_ınit_get(broker_ıd=broker_ıd)



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
api_instance = swagger_client.MobileApi(swagger_client.ApiClient(configuration))
broker_ıd = 56 # int |  (optional)

try:
    api_response = api_instance.api_v3_mobile_ınit_get(broker_ıd=broker_ıd)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->api_v3_mobile_ınit_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_ıd** | **int**|  | [optional] 

### Return type

[**MobileSettingModel**](MobileSettingModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

