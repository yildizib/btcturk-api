# BtcTurkAp30.HalvingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3HalvingGet**](HalvingApi.md#apiV3HalvingGet) | **GET** /api/v3/halving | 

<a name="apiV3HalvingGet"></a>
# **apiV3HalvingGet**
> apiV3HalvingGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.HalvingApi();
apiInstance.apiV3HalvingGet((error, data, response) => {
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

