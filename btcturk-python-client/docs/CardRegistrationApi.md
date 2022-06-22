# swagger_client.CardRegistrationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_card_registration_get**](CardRegistrationApi.md#api_v3_card_registration_get) | **GET** /api/v3/card-registration | 
[**api_v3_card_registration_post**](CardRegistrationApi.md#api_v3_card_registration_post) | **POST** /api/v3/card-registration | 

# **api_v3_card_registration_get**
> api_v3_card_registration_get()



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
api_instance = swagger_client.CardRegistrationApi(swagger_client.ApiClient(configuration))

try:
    api_instance.api_v3_card_registration_get()
except ApiException as e:
    print("Exception when calling CardRegistrationApi->api_v3_card_registration_get: %s\n" % e)
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

# **api_v3_card_registration_post**
> api_v3_card_registration_post(body=body)



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
api_instance = swagger_client.CardRegistrationApi(swagger_client.ApiClient(configuration))
body = swagger_client.CardRegistrationRequestViewModel() # CardRegistrationRequestViewModel |  (optional)

try:
    api_instance.api_v3_card_registration_post(body=body)
except ApiException as e:
    print("Exception when calling CardRegistrationApi->api_v3_card_registration_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CardRegistrationRequestViewModel**](CardRegistrationRequestViewModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

