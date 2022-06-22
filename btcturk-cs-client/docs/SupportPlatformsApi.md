# IO.Swagger.Api.SupportPlatformsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3SupportPlatformsGet**](SupportPlatformsApi.md#apiv3supportplatformsget) | **GET** /api/v3/support-platforms | 
[**ApiV3SupportPlatformsZendeskChatJwtPlatformGet**](SupportPlatformsApi.md#apiv3supportplatformszendeskchatjwtplatformget) | **GET** /api/v3/support-platforms/zendesk/chat-jwt/{platform} | 
[**ApiV3SupportPlatformsZendeskMobileJwtPlatformPost**](SupportPlatformsApi.md#apiv3supportplatformszendeskmobilejwtplatformpost) | **POST** /api/v3/support-platforms/zendesk/mobile-jwt/{platform} | 
[**ApiV3SupportPlatformsZendeskSessionsPost**](SupportPlatformsApi.md#apiv3supportplatformszendesksessionspost) | **POST** /api/v3/support-platforms/zendesk/sessions | 

<a name="apiv3supportplatformsget"></a>
# **ApiV3SupportPlatformsGet**
> void ApiV3SupportPlatformsGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3SupportPlatformsGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new SupportPlatformsApi();

            try
            {
                apiInstance.ApiV3SupportPlatformsGet();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling SupportPlatformsApi.ApiV3SupportPlatformsGet: " + e.Message );
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
<a name="apiv3supportplatformszendeskchatjwtplatformget"></a>
# **ApiV3SupportPlatformsZendeskChatJwtPlatformGet**
> void ApiV3SupportPlatformsZendeskChatJwtPlatformGet (string platform)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3SupportPlatformsZendeskChatJwtPlatformGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new SupportPlatformsApi();
            var platform = platform_example;  // string | 

            try
            {
                apiInstance.ApiV3SupportPlatformsZendeskChatJwtPlatformGet(platform);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling SupportPlatformsApi.ApiV3SupportPlatformsZendeskChatJwtPlatformGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **string**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3supportplatformszendeskmobilejwtplatformpost"></a>
# **ApiV3SupportPlatformsZendeskMobileJwtPlatformPost**
> void ApiV3SupportPlatformsZendeskMobileJwtPlatformPost (string platform, string userToken = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3SupportPlatformsZendeskMobileJwtPlatformPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new SupportPlatformsApi();
            var platform = platform_example;  // string | 
            var userToken = userToken_example;  // string |  (optional) 

            try
            {
                apiInstance.ApiV3SupportPlatformsZendeskMobileJwtPlatformPost(platform, userToken);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling SupportPlatformsApi.ApiV3SupportPlatformsZendeskMobileJwtPlatformPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **string**|  | 
 **userToken** | **string**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3supportplatformszendesksessionspost"></a>
# **ApiV3SupportPlatformsZendeskSessionsPost**
> void ApiV3SupportPlatformsZendeskSessionsPost ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3SupportPlatformsZendeskSessionsPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new SupportPlatformsApi();

            try
            {
                apiInstance.ApiV3SupportPlatformsZendeskSessionsPost();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling SupportPlatformsApi.ApiV3SupportPlatformsZendeskSessionsPost: " + e.Message );
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
