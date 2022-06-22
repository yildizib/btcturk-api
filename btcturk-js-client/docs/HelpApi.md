# BtcTurkAp30.HelpApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3HelpBuySellCommissionsGet**](HelpApi.md#apiV3HelpBuySellCommissionsGet) | **GET** /api/v3/help/buy-sell-commissions | 

<a name="apiV3HelpBuySellCommissionsGet"></a>
# **apiV3HelpBuySellCommissionsGet**
> apiV3HelpBuySellCommissionsGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.HelpApi();
apiInstance.apiV3HelpBuySellCommissionsGet((error, data, response) => {
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

