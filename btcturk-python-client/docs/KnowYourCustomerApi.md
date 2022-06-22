# swagger_client.KnowYourCustomerApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_account_kyc_post**](KnowYourCustomerApi.md#api_v3_account_kyc_post) | **POST** /api/v3/account/kyc | 

# **api_v3_account_kyc_post**
> api_v3_account_kyc_post(body=body)



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
api_instance = swagger_client.KnowYourCustomerApi(swagger_client.ApiClient(configuration))
body = swagger_client.JumioKycIdentityVerificationRequestModel() # JumioKycIdentityVerificationRequestModel |  (optional)

try:
    api_instance.api_v3_account_kyc_post(body=body)
except ApiException as e:
    print("Exception when calling KnowYourCustomerApi->api_v3_account_kyc_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JumioKycIdentityVerificationRequestModel**](JumioKycIdentityVerificationRequestModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

