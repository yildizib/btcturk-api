# swagger_client.FiatDepositApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_deposits_fiat_bank_get**](FiatDepositApi.md#api_v3_deposits_fiat_bank_get) | **GET** /api/v3/deposits/fiat/bank | 
[**api_v3_deposits_fiat_bank_send_sms_slug_get**](FiatDepositApi.md#api_v3_deposits_fiat_bank_send_sms_slug_get) | **GET** /api/v3/deposits/fiat/bank/send-sms/{slug} | 
[**api_v3_deposits_fiat_bank_slug_get**](FiatDepositApi.md#api_v3_deposits_fiat_bank_slug_get) | **GET** /api/v3/deposits/fiat/bank/{slug} | 

# **api_v3_deposits_fiat_bank_get**
> list[FiatDepositBankAccountModel] api_v3_deposits_fiat_bank_get(currency_symbol=currency_symbol)



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
api_instance = swagger_client.FiatDepositApi(swagger_client.ApiClient(configuration))
currency_symbol = 'currency_symbol_example' # str |  (optional)

try:
    api_response = api_instance.api_v3_deposits_fiat_bank_get(currency_symbol=currency_symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FiatDepositApi->api_v3_deposits_fiat_bank_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_symbol** | **str**|  | [optional] 

### Return type

[**list[FiatDepositBankAccountModel]**](FiatDepositBankAccountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_deposits_fiat_bank_send_sms_slug_get**
> api_v3_deposits_fiat_bank_send_sms_slug_get(slug, currency_symbol=currency_symbol)



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
api_instance = swagger_client.FiatDepositApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | 
currency_symbol = 'currency_symbol_example' # str |  (optional)

try:
    api_instance.api_v3_deposits_fiat_bank_send_sms_slug_get(slug, currency_symbol=currency_symbol)
except ApiException as e:
    print("Exception when calling FiatDepositApi->api_v3_deposits_fiat_bank_send_sms_slug_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **currency_symbol** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_deposits_fiat_bank_slug_get**
> FiatDepositBankAccountModel api_v3_deposits_fiat_bank_slug_get(slug, currency_symbol=currency_symbol)



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
api_instance = swagger_client.FiatDepositApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | 
currency_symbol = 'currency_symbol_example' # str |  (optional)

try:
    api_response = api_instance.api_v3_deposits_fiat_bank_slug_get(slug, currency_symbol=currency_symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FiatDepositApi->api_v3_deposits_fiat_bank_slug_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **currency_symbol** | **str**|  | [optional] 

### Return type

[**FiatDepositBankAccountModel**](FiatDepositBankAccountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

