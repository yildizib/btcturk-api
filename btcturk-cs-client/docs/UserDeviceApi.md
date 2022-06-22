# IO.Swagger.Api.UserDeviceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3UserDevicesDeviceIdDelete**](UserDeviceApi.md#apiv3userdevicesdeviceıddelete) | **DELETE** /api/v3/user-devices/{deviceId} | 
[**ApiV3UserDevicesGet**](UserDeviceApi.md#apiv3userdevicesget) | **GET** /api/v3/user-devices | Cihaz listesi

<a name="apiv3userdevicesdeviceıddelete"></a>
# **ApiV3UserDevicesDeviceIdDelete**
> void ApiV3UserDevicesDeviceIdDelete (long? deviceId)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3UserDevicesDeviceIdDeleteExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new UserDeviceApi();
            var deviceId = 789;  // long? | 

            try
            {
                apiInstance.ApiV3UserDevicesDeviceIdDelete(deviceId);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling UserDeviceApi.ApiV3UserDevicesDeviceIdDelete: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **long?**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3userdevicesget"></a>
# **ApiV3UserDevicesGet**
> void ApiV3UserDevicesGet ()

Cihaz listesi

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3UserDevicesGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new UserDeviceApi();

            try
            {
                // Cihaz listesi
                apiInstance.ApiV3UserDevicesGet();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling UserDeviceApi.ApiV3UserDevicesGet: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
