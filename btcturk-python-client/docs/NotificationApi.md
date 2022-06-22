# swagger_client.NotificationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_notifications_announcement_get**](NotificationApi.md#api_v3_notifications_announcement_get) | **GET** /api/v3/notifications/announcement | 
[**api_v3_notifications_announcement_slug_get**](NotificationApi.md#api_v3_notifications_announcement_slug_get) | **GET** /api/v3/notifications/announcement/{slug} | 
[**api_v3_notifications_count_get**](NotificationApi.md#api_v3_notifications_count_get) | **GET** /api/v3/notifications/count | Notification summary.  Unread, read, total
[**api_v3_notifications_get**](NotificationApi.md#api_v3_notifications_get) | **GET** /api/v3/notifications | 
[**api_v3_notifications_modules_get**](NotificationApi.md#api_v3_notifications_modules_get) | **GET** /api/v3/notifications/modules | 
[**api_v3_notifications_read_all_post**](NotificationApi.md#api_v3_notifications_read_all_post) | **POST** /api/v3/notifications/read/all | 
[**api_v3_notifications_read_post**](NotificationApi.md#api_v3_notifications_read_post) | **POST** /api/v3/notifications/read | 
[**api_v3_notifications_unread_get**](NotificationApi.md#api_v3_notifications_unread_get) | **GET** /api/v3/notifications/unread | 
[**api_v3_notifications_ıd_get**](NotificationApi.md#api_v3_notifications_ıd_get) | **GET** /api/v3/notifications/{id} | 
[**api_v3_notifications_ınit_get**](NotificationApi.md#api_v3_notifications_ınit_get) | **GET** /api/v3/notifications/init | 

# **api_v3_notifications_announcement_get**
> AnnouncementModelIPagedList api_v3_notifications_announcement_get(page_ındex=page_ındex, page_size=page_size, show_type=show_type)



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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
page_ındex = 56 # int |  (optional)
page_size = 56 # int |  (optional)
show_type = swagger_client.NotificationShowType() # NotificationShowType |  (optional)

try:
    api_response = api_instance.api_v3_notifications_announcement_get(page_ındex=page_ındex, page_size=page_size, show_type=show_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->api_v3_notifications_announcement_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_ındex** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **show_type** | [**NotificationShowType**](.md)|  | [optional] 

### Return type

[**AnnouncementModelIPagedList**](AnnouncementModelIPagedList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_notifications_announcement_slug_get**
> AnnouncementDetailModelIPagedList api_v3_notifications_announcement_slug_get(slug)



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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | 

try:
    api_response = api_instance.api_v3_notifications_announcement_slug_get(slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->api_v3_notifications_announcement_slug_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**AnnouncementDetailModelIPagedList**](AnnouncementDetailModelIPagedList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_notifications_count_get**
> list[SystemNotificationCountModel] api_v3_notifications_count_get()

Notification summary.  Unread, read, total

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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))

try:
    # Notification summary.  Unread, read, total
    api_response = api_instance.api_v3_notifications_count_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->api_v3_notifications_count_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SystemNotificationCountModel]**](SystemNotificationCountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_notifications_get**
> SystemNotificationModelIPagedList api_v3_notifications_get(page_ındex=page_ındex, page_size=page_size, read=read, module_ıd=module_ıd, type=type)



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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
page_ındex = 56 # int |  (optional)
page_size = 56 # int |  (optional)
read = true # bool |  (optional)
module_ıd = 789 # int |  (optional)
type = swagger_client.SystemNotificationRequestType() # SystemNotificationRequestType |  (optional)

try:
    api_response = api_instance.api_v3_notifications_get(page_ındex=page_ındex, page_size=page_size, read=read, module_ıd=module_ıd, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->api_v3_notifications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_ındex** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **read** | **bool**|  | [optional] 
 **module_ıd** | **int**|  | [optional] 
 **type** | [**SystemNotificationRequestType**](.md)|  | [optional] 

### Return type

[**SystemNotificationModelIPagedList**](SystemNotificationModelIPagedList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_notifications_modules_get**
> api_v3_notifications_modules_get()



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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))

try:
    api_instance.api_v3_notifications_modules_get()
except ApiException as e:
    print("Exception when calling NotificationApi->api_v3_notifications_modules_get: %s\n" % e)
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

# **api_v3_notifications_read_all_post**
> api_v3_notifications_read_all_post()



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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))

try:
    api_instance.api_v3_notifications_read_all_post()
except ApiException as e:
    print("Exception when calling NotificationApi->api_v3_notifications_read_all_post: %s\n" % e)
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

# **api_v3_notifications_read_post**
> api_v3_notifications_read_post(body=body)



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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
body = swagger_client.SystemNotificationReadModel() # SystemNotificationReadModel |  (optional)

try:
    api_instance.api_v3_notifications_read_post(body=body)
except ApiException as e:
    print("Exception when calling NotificationApi->api_v3_notifications_read_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemNotificationReadModel**](SystemNotificationReadModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_notifications_unread_get**
> SystemNotificationCountModel api_v3_notifications_unread_get()



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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.api_v3_notifications_unread_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->api_v3_notifications_unread_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemNotificationCountModel**](SystemNotificationCountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_notifications_ıd_get**
> SystemNotificationContentModel api_v3_notifications_ıd_get(id)



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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.api_v3_notifications_ıd_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->api_v3_notifications_ıd_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SystemNotificationContentModel**](SystemNotificationContentModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_notifications_ınit_get**
> SystemNotificationContentModel api_v3_notifications_ınit_get()



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
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.api_v3_notifications_ınit_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->api_v3_notifications_ınit_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemNotificationContentModel**](SystemNotificationContentModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

