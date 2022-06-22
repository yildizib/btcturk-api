# BtcTurkAp30.AccountApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3AccountAddressPut**](AccountApi.md#apiV3AccountAddressPut) | **PUT** /api/v3/account/address | 
[**apiV3AccountBuySellInfoGet**](AccountApi.md#apiV3AccountBuySellInfoGet) | **GET** /api/v3/account/buy-sell-info | 
[**apiV3AccountFeaturesGet**](AccountApi.md#apiV3AccountFeaturesGet) | **GET** /api/v3/account/features | 
[**apiV3AccountLimitsGet**](AccountApi.md#apiV3AccountLimitsGet) | **GET** /api/v3/account/limits | 
[**apiV3AccountPdpaPost**](AccountApi.md#apiV3AccountPdpaPost) | **POST** /api/v3/account/pdpa | 
[**apiV3AccountSplashScreenLoginPost**](AccountApi.md#apiV3AccountSplashScreenLoginPost) | **POST** /api/v3/account/splash-screen-login | 
[**apiV3AccountTradeFeeRatesGet**](AccountApi.md#apiV3AccountTradeFeeRatesGet) | **GET** /api/v3/account/trade-fee-rates | 

<a name="apiV3AccountAddressPut"></a>
# **apiV3AccountAddressPut**
> apiV3AccountAddressPut(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.AccountApi();
let opts = { 
  'body': new BtcTurkAp30.AccountAddressModel() // AccountAddressModel | 
};
apiInstance.apiV3AccountAddressPut(opts, (error, data, response) => {
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
 **body** | [**AccountAddressModel**](AccountAddressModel.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

<a name="apiV3AccountBuySellInfoGet"></a>
# **apiV3AccountBuySellInfoGet**
> apiV3AccountBuySellInfoGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.AccountApi();
apiInstance.apiV3AccountBuySellInfoGet((error, data, response) => {
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

<a name="apiV3AccountFeaturesGet"></a>
# **apiV3AccountFeaturesGet**
> apiV3AccountFeaturesGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.AccountApi();
apiInstance.apiV3AccountFeaturesGet((error, data, response) => {
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

<a name="apiV3AccountLimitsGet"></a>
# **apiV3AccountLimitsGet**
> UserAllLimitsModel apiV3AccountLimitsGet(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.AccountApi();
let opts = { 
  'currencySymbol': "currencySymbol_example" // String | 
};
apiInstance.apiV3AccountLimitsGet(opts, (error, data, response) => {
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
 **currencySymbol** | **String**|  | [optional] 

### Return type

[**UserAllLimitsModel**](UserAllLimitsModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3AccountPdpaPost"></a>
# **apiV3AccountPdpaPost**
> apiV3AccountPdpaPost(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.AccountApi();
let opts = { 
  'value': "value_example" // String | 
};
apiInstance.apiV3AccountPdpaPost(opts, (error, data, response) => {
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
 **value** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiV3AccountSplashScreenLoginPost"></a>
# **apiV3AccountSplashScreenLoginPost**
> apiV3AccountSplashScreenLoginPost(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.AccountApi();
let opts = { 
  'body': new BtcTurkAp30.CreateSplashScreenLoginRequestModel() // CreateSplashScreenLoginRequestModel | 
};
apiInstance.apiV3AccountSplashScreenLoginPost(opts, (error, data, response) => {
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
 **body** | [**CreateSplashScreenLoginRequestModel**](CreateSplashScreenLoginRequestModel.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

<a name="apiV3AccountTradeFeeRatesGet"></a>
# **apiV3AccountTradeFeeRatesGet**
> UserTradeFeeRateOutputModel apiV3AccountTradeFeeRatesGet(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.AccountApi();
let opts = { 
  'orderMethod': new BtcTurkAp30.OrderMethod(), // OrderMethod | 
  'pairSymbol': "pairSymbol_example" // String | 
};
apiInstance.apiV3AccountTradeFeeRatesGet(opts, (error, data, response) => {
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
 **orderMethod** | [**OrderMethod**](.md)|  | [optional] 
 **pairSymbol** | **String**|  | [optional] 

### Return type

[**UserTradeFeeRateOutputModel**](UserTradeFeeRateOutputModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

