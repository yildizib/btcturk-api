# BtcTurkAp30.SupportPlatformsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3SupportPlatformsGet**](SupportPlatformsApi.md#apiV3SupportPlatformsGet) | **GET** /api/v3/support-platforms | 
[**apiV3SupportPlatformsZendeskChatJwtPlatformGet**](SupportPlatformsApi.md#apiV3SupportPlatformsZendeskChatJwtPlatformGet) | **GET** /api/v3/support-platforms/zendesk/chat-jwt/{platform} | 
[**apiV3SupportPlatformsZendeskMobileJwtPlatformPost**](SupportPlatformsApi.md#apiV3SupportPlatformsZendeskMobileJwtPlatformPost) | **POST** /api/v3/support-platforms/zendesk/mobile-jwt/{platform} | 
[**apiV3SupportPlatformsZendeskSessionsPost**](SupportPlatformsApi.md#apiV3SupportPlatformsZendeskSessionsPost) | **POST** /api/v3/support-platforms/zendesk/sessions | 

<a name="apiV3SupportPlatformsGet"></a>
# **apiV3SupportPlatformsGet**
> apiV3SupportPlatformsGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.SupportPlatformsApi();
apiInstance.apiV3SupportPlatformsGet((error, data, response) => {
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

<a name="apiV3SupportPlatformsZendeskChatJwtPlatformGet"></a>
# **apiV3SupportPlatformsZendeskChatJwtPlatformGet**
> apiV3SupportPlatformsZendeskChatJwtPlatformGet(platform)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.SupportPlatformsApi();
let platform = "platform_example"; // String | 

apiInstance.apiV3SupportPlatformsZendeskChatJwtPlatformGet(platform, (error, data, response) => {
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
 **platform** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiV3SupportPlatformsZendeskMobileJwtPlatformPost"></a>
# **apiV3SupportPlatformsZendeskMobileJwtPlatformPost**
> apiV3SupportPlatformsZendeskMobileJwtPlatformPost(platform, opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.SupportPlatformsApi();
let platform = "platform_example"; // String | 
let opts = { 
  'userToken': "userToken_example" // String | 
};
apiInstance.apiV3SupportPlatformsZendeskMobileJwtPlatformPost(platform, opts, (error, data, response) => {
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
 **platform** | **String**|  | 
 **userToken** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

<a name="apiV3SupportPlatformsZendeskSessionsPost"></a>
# **apiV3SupportPlatformsZendeskSessionsPost**
> apiV3SupportPlatformsZendeskSessionsPost()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.SupportPlatformsApi();
apiInstance.apiV3SupportPlatformsZendeskSessionsPost((error, data, response) => {
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

