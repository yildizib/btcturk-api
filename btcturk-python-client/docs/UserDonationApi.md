# swagger_client.UserDonationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_user_donation_banks_get**](UserDonationApi.md#api_v3_user_donation_banks_get) | **GET** /api/v3/user-donation/banks | Bağış kampanyasına ait kullanılabilir bankalar
[**api_v3_user_donation_get**](UserDonationApi.md#api_v3_user_donation_get) | **GET** /api/v3/user-donation | Bağış durumu
[**api_v3_user_donation_post**](UserDonationApi.md#api_v3_user_donation_post) | **POST** /api/v3/user-donation | Yeni bağış kaydı

# **api_v3_user_donation_banks_get**
> api_v3_user_donation_banks_get()

Bağış kampanyasına ait kullanılabilir bankalar

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
api_instance = swagger_client.UserDonationApi(swagger_client.ApiClient(configuration))

try:
    # Bağış kampanyasına ait kullanılabilir bankalar
    api_instance.api_v3_user_donation_banks_get()
except ApiException as e:
    print("Exception when calling UserDonationApi->api_v3_user_donation_banks_get: %s\n" % e)
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

# **api_v3_user_donation_get**
> api_v3_user_donation_get()

Bağış durumu

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
api_instance = swagger_client.UserDonationApi(swagger_client.ApiClient(configuration))

try:
    # Bağış durumu
    api_instance.api_v3_user_donation_get()
except ApiException as e:
    print("Exception when calling UserDonationApi->api_v3_user_donation_get: %s\n" % e)
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

# **api_v3_user_donation_post**
> api_v3_user_donation_post(body=body)

Yeni bağış kaydı

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
api_instance = swagger_client.UserDonationApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserDonationRequestModel() # UserDonationRequestModel |  (optional)

try:
    # Yeni bağış kaydı
    api_instance.api_v3_user_donation_post(body=body)
except ApiException as e:
    print("Exception when calling UserDonationApi->api_v3_user_donation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserDonationRequestModel**](UserDonationRequestModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

