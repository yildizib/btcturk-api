# IO.Swagger.Api.FeedbackApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3FeedbackAppRatingPost**](FeedbackApi.md#apiv3feedbackappratingpost) | **POST** /api/v3/feedback/app-rating | 
[**ApiV3FeedbackSupportPlatformsGet**](FeedbackApi.md#apiv3feedbacksupportplatformsget) | **GET** /api/v3/feedback/support-platforms | 

<a name="apiv3feedbackappratingpost"></a>
# **ApiV3FeedbackAppRatingPost**
> void ApiV3FeedbackAppRatingPost (AppRatingRequestModel body = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3FeedbackAppRatingPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new FeedbackApi();
            var body = new AppRatingRequestModel(); // AppRatingRequestModel |  (optional) 

            try
            {
                apiInstance.ApiV3FeedbackAppRatingPost(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling FeedbackApi.ApiV3FeedbackAppRatingPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppRatingRequestModel**](AppRatingRequestModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3feedbacksupportplatformsget"></a>
# **ApiV3FeedbackSupportPlatformsGet**
> void ApiV3FeedbackSupportPlatformsGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3FeedbackSupportPlatformsGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new FeedbackApi();

            try
            {
                apiInstance.ApiV3FeedbackSupportPlatformsGet();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling FeedbackApi.ApiV3FeedbackSupportPlatformsGet: " + e.Message );
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
