# BtcTurkAp30.UserDeviceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3UserDevicesDeviceIdDelete**](UserDeviceApi.md#apiV3UserDevicesDeviceIdDelete) | **DELETE** /api/v3/user-devices/{deviceId} | 
[**apiV3UserDevicesGet**](UserDeviceApi.md#apiV3UserDevicesGet) | **GET** /api/v3/user-devices | Cihaz listesi

<a name="apiV3UserDevicesDeviceIdDelete"></a>
# **apiV3UserDevicesDeviceIdDelete**
> apiV3UserDevicesDeviceIdDelete(deviceId)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.UserDeviceApi();
let deviceId = 789; // Number | 

apiInstance.apiV3UserDevicesDeviceIdDelete(deviceId, (error, data, response) => {
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
 **deviceId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiV3UserDevicesGet"></a>
# **apiV3UserDevicesGet**
> apiV3UserDevicesGet()

Cihaz listesi

### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.UserDeviceApi();
apiInstance.apiV3UserDevicesGet((error, data, response) => {
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

