# IO.Swagger.Api.FiatWithdrawalCommissionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3FiatWithdrawalCommissionsGet**](FiatWithdrawalCommissionsApi.md#apiv3fiatwithdrawalcommissionsget) | **GET** /api/v3/fiat-withdrawal-commissions | 

<a name="apiv3fiatwithdrawalcommissionsget"></a>
# **ApiV3FiatWithdrawalCommissionsGet**
> void ApiV3FiatWithdrawalCommissionsGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3FiatWithdrawalCommissionsGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new FiatWithdrawalCommissionsApi();

            try
            {
                apiInstance.ApiV3FiatWithdrawalCommissionsGet();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling FiatWithdrawalCommissionsApi.ApiV3FiatWithdrawalCommissionsGet: " + e.Message );
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
