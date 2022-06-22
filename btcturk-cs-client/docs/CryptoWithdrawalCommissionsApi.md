# IO.Swagger.Api.CryptoWithdrawalCommissionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3CryptoWithdrawalCommissionsGet**](CryptoWithdrawalCommissionsApi.md#apiv3cryptowithdrawalcommissionsget) | **GET** /api/v3/crypto/withdrawal/commissions | 

<a name="apiv3cryptowithdrawalcommissionsget"></a>
# **ApiV3CryptoWithdrawalCommissionsGet**
> List<CryptoWithdrawalCommissionsResponseModel> ApiV3CryptoWithdrawalCommissionsGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3CryptoWithdrawalCommissionsGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CryptoWithdrawalCommissionsApi();

            try
            {
                List&lt;CryptoWithdrawalCommissionsResponseModel&gt; result = apiInstance.ApiV3CryptoWithdrawalCommissionsGet();
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CryptoWithdrawalCommissionsApi.ApiV3CryptoWithdrawalCommissionsGet: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List<CryptoWithdrawalCommissionsResponseModel>**](CryptoWithdrawalCommissionsResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
