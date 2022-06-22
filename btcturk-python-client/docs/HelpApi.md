# swagger_client.HelpApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_help_buy_sell_commissions_get**](HelpApi.md#api_v3_help_buy_sell_commissions_get) | **GET** /api/v3/help/buy-sell-commissions | 

# **api_v3_help_buy_sell_commissions_get**
> api_v3_help_buy_sell_commissions_get()



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
api_instance = swagger_client.HelpApi(swagger_client.ApiClient(configuration))

try:
    api_instance.api_v3_help_buy_sell_commissions_get()
except ApiException as e:
    print("Exception when calling HelpApi->api_v3_help_buy_sell_commissions_get: %s\n" % e)
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

