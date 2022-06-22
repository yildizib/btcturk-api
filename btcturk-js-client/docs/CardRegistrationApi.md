# BtcTurkAp30.CardRegistrationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3CardRegistrationGet**](CardRegistrationApi.md#apiV3CardRegistrationGet) | **GET** /api/v3/card-registration | 
[**apiV3CardRegistrationPost**](CardRegistrationApi.md#apiV3CardRegistrationPost) | **POST** /api/v3/card-registration | 

<a name="apiV3CardRegistrationGet"></a>
# **apiV3CardRegistrationGet**
> apiV3CardRegistrationGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.CardRegistrationApi();
apiInstance.apiV3CardRegistrationGet((error, data, response) => {
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

<a name="apiV3CardRegistrationPost"></a>
# **apiV3CardRegistrationPost**
> apiV3CardRegistrationPost(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.CardRegistrationApi();
let opts = { 
  'body': new BtcTurkAp30.CardRegistrationRequestViewModel() // CardRegistrationRequestViewModel | 
};
apiInstance.apiV3CardRegistrationPost(opts, (error, data, response) => {
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
 **body** | [**CardRegistrationRequestViewModel**](CardRegistrationRequestViewModel.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

