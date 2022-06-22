# BtcTurkAp30.CryptoWithdrawApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3WithdrawalsCryptoConfirmCodeDelete**](CryptoWithdrawApi.md#apiV3WithdrawalsCryptoConfirmCodeDelete) | **DELETE** /api/v3/withdrawals/crypto/confirm/{code} | 
[**apiV3WithdrawalsCryptoConfirmCodeGet**](CryptoWithdrawApi.md#apiV3WithdrawalsCryptoConfirmCodeGet) | **GET** /api/v3/withdrawals/crypto/confirm/{code} | 
[**apiV3WithdrawalsCryptoConfirmPost**](CryptoWithdrawApi.md#apiV3WithdrawalsCryptoConfirmPost) | **POST** /api/v3/withdrawals/crypto/confirm | 
[**apiV3WithdrawalsCryptoValidationCodeGet**](CryptoWithdrawApi.md#apiV3WithdrawalsCryptoValidationCodeGet) | **GET** /api/v3/withdrawals/crypto/validation/{code} | 

<a name="apiV3WithdrawalsCryptoConfirmCodeDelete"></a>
# **apiV3WithdrawalsCryptoConfirmCodeDelete**
> apiV3WithdrawalsCryptoConfirmCodeDelete(code)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.CryptoWithdrawApi();
let code = "code_example"; // String | 

apiInstance.apiV3WithdrawalsCryptoConfirmCodeDelete(code, (error, data, response) => {
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
 **code** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3WithdrawalsCryptoConfirmCodeGet"></a>
# **apiV3WithdrawalsCryptoConfirmCodeGet**
> CryptoWithdrawValidationResponseModel apiV3WithdrawalsCryptoConfirmCodeGet(code)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.CryptoWithdrawApi();
let code = "code_example"; // String | 

apiInstance.apiV3WithdrawalsCryptoConfirmCodeGet(code, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **String**|  | 

### Return type

[**CryptoWithdrawValidationResponseModel**](CryptoWithdrawValidationResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3WithdrawalsCryptoConfirmPost"></a>
# **apiV3WithdrawalsCryptoConfirmPost**
> apiV3WithdrawalsCryptoConfirmPost(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.CryptoWithdrawApi();
let opts = { 
  'body': new BtcTurkAp30.CryptoWithdrawalDeleteInputModel() // CryptoWithdrawalDeleteInputModel | 
};
apiInstance.apiV3WithdrawalsCryptoConfirmPost(opts, (error, data, response) => {
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
 **body** | [**CryptoWithdrawalDeleteInputModel**](CryptoWithdrawalDeleteInputModel.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: application/json

<a name="apiV3WithdrawalsCryptoValidationCodeGet"></a>
# **apiV3WithdrawalsCryptoValidationCodeGet**
> CryptoWithdrawValidationResponseModel apiV3WithdrawalsCryptoValidationCodeGet(code)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.CryptoWithdrawApi();
let code = "code_example"; // String | 

apiInstance.apiV3WithdrawalsCryptoValidationCodeGet(code, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **String**|  | 

### Return type

[**CryptoWithdrawValidationResponseModel**](CryptoWithdrawValidationResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

