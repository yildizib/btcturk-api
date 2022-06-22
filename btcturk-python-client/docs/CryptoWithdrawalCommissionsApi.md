# swagger_client.CryptoWithdrawalCommissionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_crypto_withdrawal_commissions_get**](CryptoWithdrawalCommissionsApi.md#api_v3_crypto_withdrawal_commissions_get) | **GET** /api/v3/crypto/withdrawal/commissions | 

# **api_v3_crypto_withdrawal_commissions_get**
> list[CryptoWithdrawalCommissionsResponseModel] api_v3_crypto_withdrawal_commissions_get()



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
api_instance = swagger_client.CryptoWithdrawalCommissionsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.api_v3_crypto_withdrawal_commissions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoWithdrawalCommissionsApi->api_v3_crypto_withdrawal_commissions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CryptoWithdrawalCommissionsResponseModel]**](CryptoWithdrawalCommissionsResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

