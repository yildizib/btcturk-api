# BtcTurkAp30.ReportApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3ReportDepositAndWithdrawalPost**](ReportApi.md#apiV3ReportDepositAndWithdrawalPost) | **POST** /api/v3/report/deposit-and-withdrawal | 
[**apiV3ReportGet**](ReportApi.md#apiV3ReportGet) | **GET** /api/v3/report | 
[**apiV3ReportTradeHistoryPost**](ReportApi.md#apiV3ReportTradeHistoryPost) | **POST** /api/v3/report/trade-history | 
[**apiV3ReportTransactionHistoryPost**](ReportApi.md#apiV3ReportTransactionHistoryPost) | **POST** /api/v3/report/transaction-history | 

<a name="apiV3ReportDepositAndWithdrawalPost"></a>
# **apiV3ReportDepositAndWithdrawalPost**
> apiV3ReportDepositAndWithdrawalPost(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.ReportApi();
let opts = { 
  'body': new BtcTurkAp30.ReportDepositWithdrawalInputModel() // ReportDepositWithdrawalInputModel | 
};
apiInstance.apiV3ReportDepositAndWithdrawalPost(opts, (error, data, response) => {
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
 **body** | [**ReportDepositWithdrawalInputModel**](ReportDepositWithdrawalInputModel.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

<a name="apiV3ReportGet"></a>
# **apiV3ReportGet**
> apiV3ReportGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.ReportApi();
apiInstance.apiV3ReportGet((error, data, response) => {
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

<a name="apiV3ReportTradeHistoryPost"></a>
# **apiV3ReportTradeHistoryPost**
> apiV3ReportTradeHistoryPost(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.ReportApi();
let opts = { 
  'body': new BtcTurkAp30.ReportTradeHistoryInputModel() // ReportTradeHistoryInputModel | 
};
apiInstance.apiV3ReportTradeHistoryPost(opts, (error, data, response) => {
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
 **body** | [**ReportTradeHistoryInputModel**](ReportTradeHistoryInputModel.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

<a name="apiV3ReportTransactionHistoryPost"></a>
# **apiV3ReportTransactionHistoryPost**
> apiV3ReportTransactionHistoryPost(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.ReportApi();
let opts = { 
  'body': new BtcTurkAp30.ReportTransactionHistoryInputModel() // ReportTransactionHistoryInputModel | 
};
apiInstance.apiV3ReportTransactionHistoryPost(opts, (error, data, response) => {
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
 **body** | [**ReportTransactionHistoryInputModel**](ReportTransactionHistoryInputModel.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

