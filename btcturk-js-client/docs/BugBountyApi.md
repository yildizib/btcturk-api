# BtcTurkAp30.BugBountyApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3BugBountiesHallOfFameGet**](BugBountyApi.md#apiV3BugBountiesHallOfFameGet) | **GET** /api/v3/bug-bounties/hall-of-fame | 
[**apiV3BugBountiesPost**](BugBountyApi.md#apiV3BugBountiesPost) | **POST** /api/v3/bug-bounties | 

<a name="apiV3BugBountiesHallOfFameGet"></a>
# **apiV3BugBountiesHallOfFameGet**
> [HallOfFrameResponseModel] apiV3BugBountiesHallOfFameGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.BugBountyApi();
apiInstance.apiV3BugBountiesHallOfFameGet((error, data, response) => {
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

[**[HallOfFrameResponseModel]**](HallOfFrameResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3BugBountiesPost"></a>
# **apiV3BugBountiesPost**
> apiV3BugBountiesPost(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.BugBountyApi();
let opts = { 
  'body': new BtcTurkAp30.BugBountyNoticeRequestModel(), // BugBountyNoticeRequestModel | 
  'xClientİd': "xClientİd_example" // String | 
};
apiInstance.apiV3BugBountiesPost(opts, (error, data, response) => {
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
 **body** | [**BugBountyNoticeRequestModel**](BugBountyNoticeRequestModel.md)|  | [optional] 
 **xClientİd** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: application/json

