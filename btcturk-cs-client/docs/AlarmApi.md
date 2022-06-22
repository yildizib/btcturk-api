# IO.Swagger.Api.AlarmApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3AlarmGet**](AlarmApi.md#apiv3alarmget) | **GET** /api/v3/alarm | 
[**ApiV3AlarmIdDelete**](AlarmApi.md#apiv3alarmıddelete) | **DELETE** /api/v3/alarm/{id} | 
[**ApiV3AlarmPost**](AlarmApi.md#apiv3alarmpost) | **POST** /api/v3/alarm | 
[**ApiV3AlarmPut**](AlarmApi.md#apiv3alarmput) | **PUT** /api/v3/alarm | 

<a name="apiv3alarmget"></a>
# **ApiV3AlarmGet**
> void ApiV3AlarmGet (bool? ısCompleted = null, int? type = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3AlarmGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new AlarmApi();
            var ısCompleted = true;  // bool? |  (optional) 
            var type = 56;  // int? |  (optional) 

            try
            {
                apiInstance.ApiV3AlarmGet(ısCompleted, type);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AlarmApi.ApiV3AlarmGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ısCompleted** | **bool?**|  | [optional] 
 **type** | **int?**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3alarmıddelete"></a>
# **ApiV3AlarmIdDelete**
> void ApiV3AlarmIdDelete (long? ıd)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3AlarmIdDeleteExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new AlarmApi();
            var ıd = 789;  // long? | 

            try
            {
                apiInstance.ApiV3AlarmIdDelete(ıd);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AlarmApi.ApiV3AlarmIdDelete: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ıd** | **long?**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3alarmpost"></a>
# **ApiV3AlarmPost**
> void ApiV3AlarmPost (CreateAlarmRequest body = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3AlarmPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new AlarmApi();
            var body = new CreateAlarmRequest(); // CreateAlarmRequest |  (optional) 

            try
            {
                apiInstance.ApiV3AlarmPost(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AlarmApi.ApiV3AlarmPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAlarmRequest**](CreateAlarmRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3alarmput"></a>
# **ApiV3AlarmPut**
> void ApiV3AlarmPut (List<long?> body = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3AlarmPutExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new AlarmApi();
            var body = new List<long?>(); // List<long?> |  (optional) 

            try
            {
                apiInstance.ApiV3AlarmPut(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AlarmApi.ApiV3AlarmPut: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**List&lt;long?&gt;**](long?.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
