# BtcTurkAp30.MobileApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3MobileInitGet**](MobileApi.md#apiV3MobileInitGet) | **GET** /api/v3/mobile/init | 

<a name="apiV3MobileInitGet"></a>
# **apiV3MobileInitGet**
> MobileSettingModel apiV3MobileInitGet(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.MobileApi();
let opts = { 
  'brokerId': 56 // Number | 
};
apiInstance.apiV3MobileInitGet(opts, (error, data, response) => {
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
 **brokerId** | **Number**|  | [optional] 

### Return type

[**MobileSettingModel**](MobileSettingModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

