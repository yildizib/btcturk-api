# swagger_client.SupportPlatformsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_support_platforms_get**](SupportPlatformsApi.md#api_v3_support_platforms_get) | **GET** /api/v3/support-platforms | 
[**api_v3_support_platforms_zendesk_chat_jwt_platform_get**](SupportPlatformsApi.md#api_v3_support_platforms_zendesk_chat_jwt_platform_get) | **GET** /api/v3/support-platforms/zendesk/chat-jwt/{platform} | 
[**api_v3_support_platforms_zendesk_mobile_jwt_platform_post**](SupportPlatformsApi.md#api_v3_support_platforms_zendesk_mobile_jwt_platform_post) | **POST** /api/v3/support-platforms/zendesk/mobile-jwt/{platform} | 
[**api_v3_support_platforms_zendesk_sessions_post**](SupportPlatformsApi.md#api_v3_support_platforms_zendesk_sessions_post) | **POST** /api/v3/support-platforms/zendesk/sessions | 

# **api_v3_support_platforms_get**
> api_v3_support_platforms_get()



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
api_instance = swagger_client.SupportPlatformsApi(swagger_client.ApiClient(configuration))

try:
    api_instance.api_v3_support_platforms_get()
except ApiException as e:
    print("Exception when calling SupportPlatformsApi->api_v3_support_platforms_get: %s\n" % e)
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

# **api_v3_support_platforms_zendesk_chat_jwt_platform_get**
> api_v3_support_platforms_zendesk_chat_jwt_platform_get(platform)



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
api_instance = swagger_client.SupportPlatformsApi(swagger_client.ApiClient(configuration))
platform = 'platform_example' # str | 

try:
    api_instance.api_v3_support_platforms_zendesk_chat_jwt_platform_get(platform)
except ApiException as e:
    print("Exception when calling SupportPlatformsApi->api_v3_support_platforms_zendesk_chat_jwt_platform_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_support_platforms_zendesk_mobile_jwt_platform_post**
> api_v3_support_platforms_zendesk_mobile_jwt_platform_post(platform, user_token=user_token)



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
api_instance = swagger_client.SupportPlatformsApi(swagger_client.ApiClient(configuration))
platform = 'platform_example' # str | 
user_token = 'user_token_example' # str |  (optional)

try:
    api_instance.api_v3_support_platforms_zendesk_mobile_jwt_platform_post(platform, user_token=user_token)
except ApiException as e:
    print("Exception when calling SupportPlatformsApi->api_v3_support_platforms_zendesk_mobile_jwt_platform_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  | 
 **user_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_support_platforms_zendesk_sessions_post**
> api_v3_support_platforms_zendesk_sessions_post()



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
api_instance = swagger_client.SupportPlatformsApi(swagger_client.ApiClient(configuration))

try:
    api_instance.api_v3_support_platforms_zendesk_sessions_post()
except ApiException as e:
    print("Exception when calling SupportPlatformsApi->api_v3_support_platforms_zendesk_sessions_post: %s\n" % e)
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

