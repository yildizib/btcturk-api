# BtcTurkAp30.FiatDepositApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3DepositsFiatBankGet**](FiatDepositApi.md#apiV3DepositsFiatBankGet) | **GET** /api/v3/deposits/fiat/bank | 
[**apiV3DepositsFiatBankSendSmsSlugGet**](FiatDepositApi.md#apiV3DepositsFiatBankSendSmsSlugGet) | **GET** /api/v3/deposits/fiat/bank/send-sms/{slug} | 
[**apiV3DepositsFiatBankSlugGet**](FiatDepositApi.md#apiV3DepositsFiatBankSlugGet) | **GET** /api/v3/deposits/fiat/bank/{slug} | 

<a name="apiV3DepositsFiatBankGet"></a>
# **apiV3DepositsFiatBankGet**
> [FiatDepositBankAccountModel] apiV3DepositsFiatBankGet(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.FiatDepositApi();
let opts = { 
  'currencySymbol': "currencySymbol_example" // String | 
};
apiInstance.apiV3DepositsFiatBankGet(opts, (error, data, response) => {
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

[**[FiatDepositBankAccountModel]**](FiatDepositBankAccountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3DepositsFiatBankSendSmsSlugGet"></a>
# **apiV3DepositsFiatBankSendSmsSlugGet**
> apiV3DepositsFiatBankSendSmsSlugGet(slug, opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.FiatDepositApi();
let slug = "slug_example"; // String | 
let opts = { 
  'currencySymbol': "currencySymbol_example" // String | 
};
apiInstance.apiV3DepositsFiatBankSendSmsSlugGet(slug, opts, (error, data, response) => {
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
 **currencySymbol** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiV3DepositsFiatBankSlugGet"></a>
# **apiV3DepositsFiatBankSlugGet**
> FiatDepositBankAccountModel apiV3DepositsFiatBankSlugGet(slug, opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.FiatDepositApi();
let slug = "slug_example"; // String | 
let opts = { 
  'currencySymbol': "currencySymbol_example" // String | 
};
apiInstance.apiV3DepositsFiatBankSlugGet(slug, opts, (error, data, response) => {
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
 **currencySymbol** | **String**|  | [optional] 

### Return type

[**FiatDepositBankAccountModel**](FiatDepositBankAccountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

