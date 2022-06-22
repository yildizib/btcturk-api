# swagger_client.BugBountyApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_bug_bounties_hall_of_fame_get**](BugBountyApi.md#api_v3_bug_bounties_hall_of_fame_get) | **GET** /api/v3/bug-bounties/hall-of-fame | 
[**api_v3_bug_bounties_post**](BugBountyApi.md#api_v3_bug_bounties_post) | **POST** /api/v3/bug-bounties | 

# **api_v3_bug_bounties_hall_of_fame_get**
> list[HallOfFrameResponseModel] api_v3_bug_bounties_hall_of_fame_get()



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
api_instance = swagger_client.BugBountyApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.api_v3_bug_bounties_hall_of_fame_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BugBountyApi->api_v3_bug_bounties_hall_of_fame_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[HallOfFrameResponseModel]**](HallOfFrameResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_bug_bounties_post**
> api_v3_bug_bounties_post(body=body, x_client_id=x_client_id)



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
api_instance = swagger_client.BugBountyApi(swagger_client.ApiClient(configuration))
body = swagger_client.BugBountyNoticeRequestModel() # BugBountyNoticeRequestModel |  (optional)
x_client_id = 'x_client_id_example' # str |  (optional)

try:
    api_instance.api_v3_bug_bounties_post(body=body, x_client_id=x_client_id)
except ApiException as e:
    print("Exception when calling BugBountyApi->api_v3_bug_bounties_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BugBountyNoticeRequestModel**](BugBountyNoticeRequestModel.md)|  | [optional] 
 **x_client_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

