# IO.Swagger.Api.HomeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiResourcesLanguageGet**](HomeApi.md#apiresourceslanguageget) | **GET** /api/resources/language | 
[**ApiResourcesLanguageJsonGet**](HomeApi.md#apiresourceslanguagejsonget) | **GET** /api/resources/{language}.json | 
[**ApiResourcesLocationGet**](HomeApi.md#apiresourceslocationget) | **GET** /api/resources/location | 

<a name="apiresourceslanguageget"></a>
# **ApiResourcesLanguageGet**
> void ApiResourcesLanguageGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiResourcesLanguageGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new HomeApi();

            try
            {
                apiInstance.ApiResourcesLanguageGet();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling HomeApi.ApiResourcesLanguageGet: " + e.Message );
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
<a name="apiresourceslanguagejsonget"></a>
# **ApiResourcesLanguageJsonGet**
> void ApiResourcesLanguageJsonGet (string language, int? brokerId = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiResourcesLanguageJsonGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new HomeApi();
            var language = language_example;  // string | 
            var brokerId = 56;  // int? |  (optional) 

            try
            {
                apiInstance.ApiResourcesLanguageJsonGet(language, brokerId);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling HomeApi.ApiResourcesLanguageJsonGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **string**|  | 
 **brokerId** | **int?**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiresourceslocationget"></a>
# **ApiResourcesLocationGet**
> void ApiResourcesLocationGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiResourcesLocationGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new HomeApi();

            try
            {
                apiInstance.ApiResourcesLocationGet();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling HomeApi.ApiResourcesLocationGet: " + e.Message );
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
