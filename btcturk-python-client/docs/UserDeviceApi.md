# swagger_client.UserDeviceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_user_devices_device_ıd_delete**](UserDeviceApi.md#api_v3_user_devices_device_ıd_delete) | **DELETE** /api/v3/user-devices/{deviceId} | 
[**api_v3_user_devices_get**](UserDeviceApi.md#api_v3_user_devices_get) | **GET** /api/v3/user-devices | Cihaz listesi

# **api_v3_user_devices_device_ıd_delete**
> api_v3_user_devices_device_ıd_delete(device_ıd)



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
api_instance = swagger_client.UserDeviceApi(swagger_client.ApiClient(configuration))
device_ıd = 789 # int | 

try:
    api_instance.api_v3_user_devices_device_ıd_delete(device_ıd)
except ApiException as e:
    print("Exception when calling UserDeviceApi->api_v3_user_devices_device_ıd_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ıd** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_user_devices_get**
> api_v3_user_devices_get()

Cihaz listesi

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
api_instance = swagger_client.UserDeviceApi(swagger_client.ApiClient(configuration))

try:
    # Cihaz listesi
    api_instance.api_v3_user_devices_get()
except ApiException as e:
    print("Exception when calling UserDeviceApi->api_v3_user_devices_get: %s\n" % e)
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

