# swagger_client.CryptoDepositApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_deposits_crypto_currency_symbol_get**](CryptoDepositApi.md#api_v3_deposits_crypto_currency_symbol_get) | **GET** /api/v3/deposits/crypto/{currencySymbol} | 
[**api_v3_deposits_crypto_getnewcryptoaddress_currency_symbol_address_get**](CryptoDepositApi.md#api_v3_deposits_crypto_getnewcryptoaddress_currency_symbol_address_get) | **GET** /api/v3/deposits/crypto/getnewcryptoaddress/{currencySymbol}/{address} | 

# **api_v3_deposits_crypto_currency_symbol_get**
> api_v3_deposits_crypto_currency_symbol_get(currency_symbol, auto_address_disabled=auto_address_disabled)



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
api_instance = swagger_client.CryptoDepositApi(swagger_client.ApiClient(configuration))
currency_symbol = swagger_client.CryptoCurrencySymbol() # CryptoCurrencySymbol | 
auto_address_disabled = true # bool |  (optional)

try:
    api_instance.api_v3_deposits_crypto_currency_symbol_get(currency_symbol, auto_address_disabled=auto_address_disabled)
except ApiException as e:
    print("Exception when calling CryptoDepositApi->api_v3_deposits_crypto_currency_symbol_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_symbol** | [**CryptoCurrencySymbol**](.md)|  | 
 **auto_address_disabled** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_deposits_crypto_getnewcryptoaddress_currency_symbol_address_get**
> api_v3_deposits_crypto_getnewcryptoaddress_currency_symbol_address_get(currency_symbol, address)



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
api_instance = swagger_client.CryptoDepositApi(swagger_client.ApiClient(configuration))
currency_symbol = swagger_client.CryptoCurrencySymbol() # CryptoCurrencySymbol | 
address = 'address_example' # str | 

try:
    api_instance.api_v3_deposits_crypto_getnewcryptoaddress_currency_symbol_address_get(currency_symbol, address)
except ApiException as e:
    print("Exception when calling CryptoDepositApi->api_v3_deposits_crypto_getnewcryptoaddress_currency_symbol_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_symbol** | [**CryptoCurrencySymbol**](.md)|  | 
 **address** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

