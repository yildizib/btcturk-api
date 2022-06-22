# BtcTurkAp30.ExchangeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3ExchangeCommissionsGet**](ExchangeApi.md#apiV3ExchangeCommissionsGet) | **GET** /api/v3/exchange/commissions | 
[**apiV3ExchangeLimitsGet**](ExchangeApi.md#apiV3ExchangeLimitsGet) | **GET** /api/v3/exchange/limits | 

<a name="apiV3ExchangeCommissionsGet"></a>
# **apiV3ExchangeCommissionsGet**
> CommissionOutputModel apiV3ExchangeCommissionsGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.ExchangeApi();
apiInstance.apiV3ExchangeCommissionsGet((error, data, response) => {
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

[**CommissionOutputModel**](CommissionOutputModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3ExchangeLimitsGet"></a>
# **apiV3ExchangeLimitsGet**
> LimitOutputModel apiV3ExchangeLimitsGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.ExchangeApi();
apiInstance.apiV3ExchangeLimitsGet((error, data, response) => {
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

[**LimitOutputModel**](LimitOutputModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

