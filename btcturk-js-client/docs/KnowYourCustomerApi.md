# BtcTurkAp30.KnowYourCustomerApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3AccountKycPost**](KnowYourCustomerApi.md#apiV3AccountKycPost) | **POST** /api/v3/account/kyc | 

<a name="apiV3AccountKycPost"></a>
# **apiV3AccountKycPost**
> apiV3AccountKycPost(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.KnowYourCustomerApi();
let opts = { 
  'body': new BtcTurkAp30.JumioKycIdentityVerificationRequestModel() // JumioKycIdentityVerificationRequestModel | 
};
apiInstance.apiV3AccountKycPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JumioKycIdentityVerificationRequestModel**](JumioKycIdentityVerificationRequestModel.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

