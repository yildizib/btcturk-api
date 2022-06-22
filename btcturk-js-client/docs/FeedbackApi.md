# BtcTurkAp30.FeedbackApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3FeedbackAppRatingPost**](FeedbackApi.md#apiV3FeedbackAppRatingPost) | **POST** /api/v3/feedback/app-rating | 
[**apiV3FeedbackSupportPlatformsGet**](FeedbackApi.md#apiV3FeedbackSupportPlatformsGet) | **GET** /api/v3/feedback/support-platforms | 

<a name="apiV3FeedbackAppRatingPost"></a>
# **apiV3FeedbackAppRatingPost**
> apiV3FeedbackAppRatingPost(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.FeedbackApi();
let opts = { 
  'body': new BtcTurkAp30.AppRatingRequestModel() // AppRatingRequestModel | 
};
apiInstance.apiV3FeedbackAppRatingPost(opts, (error, data, response) => {
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
 **body** | [**AppRatingRequestModel**](AppRatingRequestModel.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: application/json

<a name="apiV3FeedbackSupportPlatformsGet"></a>
# **apiV3FeedbackSupportPlatformsGet**
> apiV3FeedbackSupportPlatformsGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.FeedbackApi();
apiInstance.apiV3FeedbackSupportPlatformsGet((error, data, response) => {
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

