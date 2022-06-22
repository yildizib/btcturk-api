# IO.Swagger.Api.MobileApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3MobileInitGet**](MobileApi.md#apiv3mobileınitget) | **GET** /api/v3/mobile/init | 

<a name="apiv3mobileınitget"></a>
# **ApiV3MobileInitGet**
> MobileSettingModel ApiV3MobileInitGet (int? brokerId = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3MobileInitGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new MobileApi();
            var brokerId = 56;  // int? |  (optional) 

            try
            {
                MobileSettingModel result = apiInstance.ApiV3MobileInitGet(brokerId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling MobileApi.ApiV3MobileInitGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brokerId** | **int?**|  | [optional] 

### Return type

[**MobileSettingModel**](MobileSettingModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
