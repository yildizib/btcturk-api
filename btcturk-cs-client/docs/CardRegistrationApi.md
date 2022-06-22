# IO.Swagger.Api.CardRegistrationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3CardRegistrationGet**](CardRegistrationApi.md#apiv3cardregistrationget) | **GET** /api/v3/card-registration | 
[**ApiV3CardRegistrationPost**](CardRegistrationApi.md#apiv3cardregistrationpost) | **POST** /api/v3/card-registration | 

<a name="apiv3cardregistrationget"></a>
# **ApiV3CardRegistrationGet**
> void ApiV3CardRegistrationGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3CardRegistrationGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CardRegistrationApi();

            try
            {
                apiInstance.ApiV3CardRegistrationGet();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CardRegistrationApi.ApiV3CardRegistrationGet: " + e.Message );
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
<a name="apiv3cardregistrationpost"></a>
# **ApiV3CardRegistrationPost**
> void ApiV3CardRegistrationPost (CardRegistrationRequestViewModel body = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3CardRegistrationPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CardRegistrationApi();
            var body = new CardRegistrationRequestViewModel(); // CardRegistrationRequestViewModel |  (optional) 

            try
            {
                apiInstance.ApiV3CardRegistrationPost(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CardRegistrationApi.ApiV3CardRegistrationPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CardRegistrationRequestViewModel**](CardRegistrationRequestViewModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
