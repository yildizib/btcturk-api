# BtcTurkAp30.UserDonationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3UserDonationBanksGet**](UserDonationApi.md#apiV3UserDonationBanksGet) | **GET** /api/v3/user-donation/banks | Bağış kampanyasına ait kullanılabilir bankalar
[**apiV3UserDonationGet**](UserDonationApi.md#apiV3UserDonationGet) | **GET** /api/v3/user-donation | Bağış durumu
[**apiV3UserDonationPost**](UserDonationApi.md#apiV3UserDonationPost) | **POST** /api/v3/user-donation | Yeni bağış kaydı

<a name="apiV3UserDonationBanksGet"></a>
# **apiV3UserDonationBanksGet**
> apiV3UserDonationBanksGet()

Bağış kampanyasına ait kullanılabilir bankalar

### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.UserDonationApi();
apiInstance.apiV3UserDonationBanksGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiV3UserDonationGet"></a>
# **apiV3UserDonationGet**
> apiV3UserDonationGet()

Bağış durumu

### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.UserDonationApi();
apiInstance.apiV3UserDonationGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiV3UserDonationPost"></a>
# **apiV3UserDonationPost**
> apiV3UserDonationPost(opts)

Yeni bağış kaydı

### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.UserDonationApi();
let opts = { 
  'body': new BtcTurkAp30.UserDonationRequestModel() // UserDonationRequestModel | 
};
apiInstance.apiV3UserDonationPost(opts, (error, data, response) => {
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
 **body** | [**UserDonationRequestModel**](UserDonationRequestModel.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: application/json

