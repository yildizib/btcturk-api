# swagger_client.AlarmApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_alarm_get**](AlarmApi.md#api_v3_alarm_get) | **GET** /api/v3/alarm | 
[**api_v3_alarm_post**](AlarmApi.md#api_v3_alarm_post) | **POST** /api/v3/alarm | 
[**api_v3_alarm_put**](AlarmApi.md#api_v3_alarm_put) | **PUT** /api/v3/alarm | 
[**api_v3_alarm_ıd_delete**](AlarmApi.md#api_v3_alarm_ıd_delete) | **DELETE** /api/v3/alarm/{id} | 

# **api_v3_alarm_get**
> api_v3_alarm_get(is_completed=is_completed, type=type)



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
api_instance = swagger_client.AlarmApi(swagger_client.ApiClient(configuration))
is_completed = true # bool |  (optional)
type = 56 # int |  (optional)

try:
    api_instance.api_v3_alarm_get(is_completed=is_completed, type=type)
except ApiException as e:
    print("Exception when calling AlarmApi->api_v3_alarm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_completed** | **bool**|  | [optional] 
 **type** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_alarm_post**
> api_v3_alarm_post(body=body)



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
api_instance = swagger_client.AlarmApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateAlarmRequest() # CreateAlarmRequest |  (optional)

try:
    api_instance.api_v3_alarm_post(body=body)
except ApiException as e:
    print("Exception when calling AlarmApi->api_v3_alarm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAlarmRequest**](CreateAlarmRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_alarm_put**
> api_v3_alarm_put(body=body)



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
api_instance = swagger_client.AlarmApi(swagger_client.ApiClient(configuration))
body = [56] # list[int] |  (optional)

try:
    api_instance.api_v3_alarm_put(body=body)
except ApiException as e:
    print("Exception when calling AlarmApi->api_v3_alarm_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_alarm_ıd_delete**
> api_v3_alarm_ıd_delete(id)



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
api_instance = swagger_client.AlarmApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_instance.api_v3_alarm_ıd_delete(id)
except ApiException as e:
    print("Exception when calling AlarmApi->api_v3_alarm_ıd_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

