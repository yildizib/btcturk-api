# IO.Swagger.Api.BugBountyApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3BugBountiesHallOfFameGet**](BugBountyApi.md#apiv3bugbountieshalloffameget) | **GET** /api/v3/bug-bounties/hall-of-fame | 
[**ApiV3BugBountiesPost**](BugBountyApi.md#apiv3bugbountiespost) | **POST** /api/v3/bug-bounties | 

<a name="apiv3bugbountieshalloffameget"></a>
# **ApiV3BugBountiesHallOfFameGet**
> List<HallOfFrameResponseModel> ApiV3BugBountiesHallOfFameGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3BugBountiesHallOfFameGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new BugBountyApi();

            try
            {
                List&lt;HallOfFrameResponseModel&gt; result = apiInstance.ApiV3BugBountiesHallOfFameGet();
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling BugBountyApi.ApiV3BugBountiesHallOfFameGet: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List<HallOfFrameResponseModel>**](HallOfFrameResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3bugbountiespost"></a>
# **ApiV3BugBountiesPost**
> void ApiV3BugBountiesPost (BugBountyNoticeRequestModel body = null, string xClientİd = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3BugBountiesPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new BugBountyApi();
            var body = new BugBountyNoticeRequestModel(); // BugBountyNoticeRequestModel |  (optional) 
            var xClientİd = xClientİd_example;  // string |  (optional) 

            try
            {
                apiInstance.ApiV3BugBountiesPost(body, xClientİd);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling BugBountyApi.ApiV3BugBountiesPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BugBountyNoticeRequestModel**](BugBountyNoticeRequestModel.md)|  | [optional] 
 **xClientİd** | **string**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
