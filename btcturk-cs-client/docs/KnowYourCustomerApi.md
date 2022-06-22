# IO.Swagger.Api.KnowYourCustomerApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3AccountKycPost**](KnowYourCustomerApi.md#apiv3accountkycpost) | **POST** /api/v3/account/kyc | 

<a name="apiv3accountkycpost"></a>
# **ApiV3AccountKycPost**
> void ApiV3AccountKycPost (JumioKycIdentityVerificationRequestModel body = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3AccountKycPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new KnowYourCustomerApi();
            var body = new JumioKycIdentityVerificationRequestModel(); // JumioKycIdentityVerificationRequestModel |  (optional) 

            try
            {
                apiInstance.ApiV3AccountKycPost(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling KnowYourCustomerApi.ApiV3AccountKycPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JumioKycIdentityVerificationRequestModel**](JumioKycIdentityVerificationRequestModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
