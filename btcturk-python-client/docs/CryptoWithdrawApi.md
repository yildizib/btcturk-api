# swagger_client.CryptoWithdrawApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_withdrawals_crypto_confirm_code_delete**](CryptoWithdrawApi.md#api_v3_withdrawals_crypto_confirm_code_delete) | **DELETE** /api/v3/withdrawals/crypto/confirm/{code} | 
[**api_v3_withdrawals_crypto_confirm_code_get**](CryptoWithdrawApi.md#api_v3_withdrawals_crypto_confirm_code_get) | **GET** /api/v3/withdrawals/crypto/confirm/{code} | 
[**api_v3_withdrawals_crypto_confirm_post**](CryptoWithdrawApi.md#api_v3_withdrawals_crypto_confirm_post) | **POST** /api/v3/withdrawals/crypto/confirm | 
[**api_v3_withdrawals_crypto_validation_code_get**](CryptoWithdrawApi.md#api_v3_withdrawals_crypto_validation_code_get) | **GET** /api/v3/withdrawals/crypto/validation/{code} | 

# **api_v3_withdrawals_crypto_confirm_code_delete**
> api_v3_withdrawals_crypto_confirm_code_delete(code)



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
api_instance = swagger_client.CryptoWithdrawApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | 

try:
    api_instance.api_v3_withdrawals_crypto_confirm_code_delete(code)
except ApiException as e:
    print("Exception when calling CryptoWithdrawApi->api_v3_withdrawals_crypto_confirm_code_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_withdrawals_crypto_confirm_code_get**
> CryptoWithdrawValidationResponseModel api_v3_withdrawals_crypto_confirm_code_get(code)



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
api_instance = swagger_client.CryptoWithdrawApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | 

try:
    api_response = api_instance.api_v3_withdrawals_crypto_confirm_code_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoWithdrawApi->api_v3_withdrawals_crypto_confirm_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**CryptoWithdrawValidationResponseModel**](CryptoWithdrawValidationResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_withdrawals_crypto_confirm_post**
> api_v3_withdrawals_crypto_confirm_post(body=body)



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
api_instance = swagger_client.CryptoWithdrawApi(swagger_client.ApiClient(configuration))
body = swagger_client.CryptoWithdrawalDeleteInputModel() # CryptoWithdrawalDeleteInputModel |  (optional)

try:
    api_instance.api_v3_withdrawals_crypto_confirm_post(body=body)
except ApiException as e:
    print("Exception when calling CryptoWithdrawApi->api_v3_withdrawals_crypto_confirm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CryptoWithdrawalDeleteInputModel**](CryptoWithdrawalDeleteInputModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_withdrawals_crypto_validation_code_get**
> CryptoWithdrawValidationResponseModel api_v3_withdrawals_crypto_validation_code_get(code)



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
api_instance = swagger_client.CryptoWithdrawApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | 

try:
    api_response = api_instance.api_v3_withdrawals_crypto_validation_code_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoWithdrawApi->api_v3_withdrawals_crypto_validation_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**CryptoWithdrawValidationResponseModel**](CryptoWithdrawValidationResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

