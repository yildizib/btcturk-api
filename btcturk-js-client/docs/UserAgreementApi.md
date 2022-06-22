# BtcTurkAp30.UserAgreementApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3UserAgreementGet**](UserAgreementApi.md#apiV3UserAgreementGet) | **GET** /api/v3/UserAgreement | 
[**apiV3UserAgreementPost**](UserAgreementApi.md#apiV3UserAgreementPost) | **POST** /api/v3/UserAgreement | 
[**apiV3UserAgreementRiskDisclosureCurrencySymbolGet**](UserAgreementApi.md#apiV3UserAgreementRiskDisclosureCurrencySymbolGet) | **GET** /api/v3/user-agreement/risk-disclosure/currency/{symbol} | 
[**apiV3UserAgreementRiskDisclosurePairPairSymbolGet**](UserAgreementApi.md#apiV3UserAgreementRiskDisclosurePairPairSymbolGet) | **GET** /api/v3/user-agreement/risk-disclosure/pair/{pairSymbol} | 
[**apiV3UserAgreementSlugGet**](UserAgreementApi.md#apiV3UserAgreementSlugGet) | **GET** /api/v3/UserAgreement/{slug} | 
[**apiV3UserAgreementSlugGet_0**](UserAgreementApi.md#apiV3UserAgreementSlugGet_0) | **GET** /api/v3/user-agreement/{slug} | 
[**apiV3UserAgreementSlugPost**](UserAgreementApi.md#apiV3UserAgreementSlugPost) | **POST** /api/v3/user-agreement/{slug} | 

<a name="apiV3UserAgreementGet"></a>
# **apiV3UserAgreementGet**
> [UserAgreementModel] apiV3UserAgreementGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.UserAgreementApi();
apiInstance.apiV3UserAgreementGet((error, data, response) => {
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

[**[UserAgreementModel]**](UserAgreementModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3UserAgreementPost"></a>
# **apiV3UserAgreementPost**
> apiV3UserAgreementPost(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.UserAgreementApi();
let opts = { 
  'body': new BtcTurkAp30.UserAgreementApproveModel() // UserAgreementApproveModel | Approve id
};
apiInstance.apiV3UserAgreementPost(opts, (error, data, response) => {
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
 **body** | [**UserAgreementApproveModel**](UserAgreementApproveModel.md)| Approve id | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

<a name="apiV3UserAgreementRiskDisclosureCurrencySymbolGet"></a>
# **apiV3UserAgreementRiskDisclosureCurrencySymbolGet**
> CheckCurrencyRiskAgreementResponseModel apiV3UserAgreementRiskDisclosureCurrencySymbolGet(symbol, opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.UserAgreementApi();
let symbol = "symbol_example"; // String | 
let opts = { 
  'transferType': new BtcTurkAp30.CurrencyTransferType() // CurrencyTransferType | 
};
apiInstance.apiV3UserAgreementRiskDisclosureCurrencySymbolGet(symbol, opts, (error, data, response) => {
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
 **symbol** | **String**|  | 
 **transferType** | [**CurrencyTransferType**](.md)|  | [optional] 

### Return type

[**CheckCurrencyRiskAgreementResponseModel**](CheckCurrencyRiskAgreementResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3UserAgreementRiskDisclosurePairPairSymbolGet"></a>
# **apiV3UserAgreementRiskDisclosurePairPairSymbolGet**
> CheckPairRiskAgreementResponseModel apiV3UserAgreementRiskDisclosurePairPairSymbolGet(pairSymbol)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.UserAgreementApi();
let pairSymbol = "pairSymbol_example"; // String | 

apiInstance.apiV3UserAgreementRiskDisclosurePairPairSymbolGet(pairSymbol, (error, data, response) => {
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
 **pairSymbol** | **String**|  | 

### Return type

[**CheckPairRiskAgreementResponseModel**](CheckPairRiskAgreementResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3UserAgreementSlugGet"></a>
# **apiV3UserAgreementSlugGet**
> UserAgreementModel apiV3UserAgreementSlugGet(slug)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.UserAgreementApi();
let slug = "slug_example"; // String | 

apiInstance.apiV3UserAgreementSlugGet(slug, (error, data, response) => {
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
 **slug** | **String**|  | 

### Return type

[**UserAgreementModel**](UserAgreementModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3UserAgreementSlugGet_0"></a>
# **apiV3UserAgreementSlugGet_0**
> UserAgreementModel apiV3UserAgreementSlugGet_0(slug)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.UserAgreementApi();
let slug = "slug_example"; // String | 

apiInstance.apiV3UserAgreementSlugGet_0(slug, (error, data, response) => {
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
 **slug** | **String**|  | 

### Return type

[**UserAgreementModel**](UserAgreementModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3UserAgreementSlugPost"></a>
# **apiV3UserAgreementSlugPost**
> apiV3UserAgreementSlugPost(slug)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.UserAgreementApi();
let slug = "slug_example"; // String | 

apiInstance.apiV3UserAgreementSlugPost(slug, (error, data, response) => {
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
 **slug** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

