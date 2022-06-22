# BtcTurkAp30.CryptoWithdrawalCommissionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3CryptoWithdrawalCommissionsGet**](CryptoWithdrawalCommissionsApi.md#apiV3CryptoWithdrawalCommissionsGet) | **GET** /api/v3/crypto/withdrawal/commissions | 

<a name="apiV3CryptoWithdrawalCommissionsGet"></a>
# **apiV3CryptoWithdrawalCommissionsGet**
> [CryptoWithdrawalCommissionsResponseModel] apiV3CryptoWithdrawalCommissionsGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.CryptoWithdrawalCommissionsApi();
apiInstance.apiV3CryptoWithdrawalCommissionsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[CryptoWithdrawalCommissionsResponseModel]**](CryptoWithdrawalCommissionsResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

