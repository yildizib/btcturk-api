# IO.Swagger.Api.UserDonationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3UserDonationBanksGet**](UserDonationApi.md#apiv3userdonationbanksget) | **GET** /api/v3/user-donation/banks | Bağış kampanyasına ait kullanılabilir bankalar
[**ApiV3UserDonationGet**](UserDonationApi.md#apiv3userdonationget) | **GET** /api/v3/user-donation | Bağış durumu
[**ApiV3UserDonationPost**](UserDonationApi.md#apiv3userdonationpost) | **POST** /api/v3/user-donation | Yeni bağış kaydı

<a name="apiv3userdonationbanksget"></a>
# **ApiV3UserDonationBanksGet**
> void ApiV3UserDonationBanksGet ()

Bağış kampanyasına ait kullanılabilir bankalar

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3UserDonationBanksGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new UserDonationApi();

            try
            {
                // Bağış kampanyasına ait kullanılabilir bankalar
                apiInstance.ApiV3UserDonationBanksGet();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling UserDonationApi.ApiV3UserDonationBanksGet: " + e.Message );
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
<a name="apiv3userdonationget"></a>
# **ApiV3UserDonationGet**
> void ApiV3UserDonationGet ()

Bağış durumu

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3UserDonationGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new UserDonationApi();

            try
            {
                // Bağış durumu
                apiInstance.ApiV3UserDonationGet();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling UserDonationApi.ApiV3UserDonationGet: " + e.Message );
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
<a name="apiv3userdonationpost"></a>
# **ApiV3UserDonationPost**
> void ApiV3UserDonationPost (UserDonationRequestModel body = null)

Yeni bağış kaydı

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3UserDonationPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new UserDonationApi();
            var body = new UserDonationRequestModel(); // UserDonationRequestModel |  (optional) 

            try
            {
                // Yeni bağış kaydı
                apiInstance.ApiV3UserDonationPost(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling UserDonationApi.ApiV3UserDonationPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserDonationRequestModel**](UserDonationRequestModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
