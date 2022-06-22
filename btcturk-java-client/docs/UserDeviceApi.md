# UserDeviceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3UserDevicesDeviceIdDelete**](UserDeviceApi.md#apiV3UserDevicesDeviceIdDelete) | **DELETE** /api/v3/user-devices/{deviceId} | 
[**apiV3UserDevicesGet**](UserDeviceApi.md#apiV3UserDevicesGet) | **GET** /api/v3/user-devices | Cihaz listesi

<a name="apiV3UserDevicesDeviceIdDelete"></a>
# **apiV3UserDevicesDeviceIdDelete**
> apiV3UserDevicesDeviceIdDelete(deviceId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.UserDeviceApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

UserDeviceApi apiInstance = new UserDeviceApi();
Long deviceId = 789L; // Long | 
try {
    apiInstance.apiV3UserDevicesDeviceIdDelete(deviceId);
} catch (ApiException e) {
    System.err.println("Exception when calling UserDeviceApi#apiV3UserDevicesDeviceIdDelete");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **Long**|  |

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
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.UserDeviceApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

UserDeviceApi apiInstance = new UserDeviceApi();
try {
    apiInstance.apiV3UserDevicesGet();
} catch (ApiException e) {
    System.err.println("Exception when calling UserDeviceApi#apiV3UserDevicesGet");
    e.printStackTrace();
}
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

