# IO.Swagger.Api.NotificationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3NotificationsAnnouncementGet**](NotificationApi.md#apiv3notificationsannouncementget) | **GET** /api/v3/notifications/announcement | 
[**ApiV3NotificationsAnnouncementSlugGet**](NotificationApi.md#apiv3notificationsannouncementslugget) | **GET** /api/v3/notifications/announcement/{slug} | 
[**ApiV3NotificationsCountGet**](NotificationApi.md#apiv3notificationscountget) | **GET** /api/v3/notifications/count | Notification summary.  Unread, read, total
[**ApiV3NotificationsGet**](NotificationApi.md#apiv3notificationsget) | **GET** /api/v3/notifications | 
[**ApiV3NotificationsIdGet**](NotificationApi.md#apiv3notificationsıdget) | **GET** /api/v3/notifications/{id} | 
[**ApiV3NotificationsInitGet**](NotificationApi.md#apiv3notificationsınitget) | **GET** /api/v3/notifications/init | 
[**ApiV3NotificationsModulesGet**](NotificationApi.md#apiv3notificationsmodulesget) | **GET** /api/v3/notifications/modules | 
[**ApiV3NotificationsReadAllPost**](NotificationApi.md#apiv3notificationsreadallpost) | **POST** /api/v3/notifications/read/all | 
[**ApiV3NotificationsReadPost**](NotificationApi.md#apiv3notificationsreadpost) | **POST** /api/v3/notifications/read | 
[**ApiV3NotificationsUnreadGet**](NotificationApi.md#apiv3notificationsunreadget) | **GET** /api/v3/notifications/unread | 

<a name="apiv3notificationsannouncementget"></a>
# **ApiV3NotificationsAnnouncementGet**
> AnnouncementModelIPagedList ApiV3NotificationsAnnouncementGet (int? pageIndex = null, int? pageSize = null, NotificationShowType showType = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3NotificationsAnnouncementGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new NotificationApi();
            var pageIndex = 56;  // int? |  (optional) 
            var pageSize = 56;  // int? |  (optional) 
            var showType = new NotificationShowType(); // NotificationShowType |  (optional) 

            try
            {
                AnnouncementModelIPagedList result = apiInstance.ApiV3NotificationsAnnouncementGet(pageIndex, pageSize, showType);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling NotificationApi.ApiV3NotificationsAnnouncementGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageIndex** | **int?**|  | [optional] 
 **pageSize** | **int?**|  | [optional] 
 **showType** | [**NotificationShowType**](NotificationShowType.md)|  | [optional] 

### Return type

[**AnnouncementModelIPagedList**](AnnouncementModelIPagedList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3notificationsannouncementslugget"></a>
# **ApiV3NotificationsAnnouncementSlugGet**
> AnnouncementDetailModelIPagedList ApiV3NotificationsAnnouncementSlugGet (string slug)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3NotificationsAnnouncementSlugGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new NotificationApi();
            var slug = slug_example;  // string | 

            try
            {
                AnnouncementDetailModelIPagedList result = apiInstance.ApiV3NotificationsAnnouncementSlugGet(slug);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling NotificationApi.ApiV3NotificationsAnnouncementSlugGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **string**|  | 

### Return type

[**AnnouncementDetailModelIPagedList**](AnnouncementDetailModelIPagedList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3notificationscountget"></a>
# **ApiV3NotificationsCountGet**
> List<SystemNotificationCountModel> ApiV3NotificationsCountGet ()

Notification summary.  Unread, read, total

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3NotificationsCountGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new NotificationApi();

            try
            {
                // Notification summary.  Unread, read, total
                List&lt;SystemNotificationCountModel&gt; result = apiInstance.ApiV3NotificationsCountGet();
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling NotificationApi.ApiV3NotificationsCountGet: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List<SystemNotificationCountModel>**](SystemNotificationCountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3notificationsget"></a>
# **ApiV3NotificationsGet**
> SystemNotificationModelIPagedList ApiV3NotificationsGet (int? pageIndex = null, int? pageSize = null, bool? read = null, long? moduleId = null, SystemNotificationRequestType type = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3NotificationsGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new NotificationApi();
            var pageIndex = 56;  // int? |  (optional) 
            var pageSize = 56;  // int? |  (optional) 
            var read = true;  // bool? |  (optional) 
            var moduleId = 789;  // long? |  (optional) 
            var type = new SystemNotificationRequestType(); // SystemNotificationRequestType |  (optional) 

            try
            {
                SystemNotificationModelIPagedList result = apiInstance.ApiV3NotificationsGet(pageIndex, pageSize, read, moduleId, type);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling NotificationApi.ApiV3NotificationsGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageIndex** | **int?**|  | [optional] 
 **pageSize** | **int?**|  | [optional] 
 **read** | **bool?**|  | [optional] 
 **moduleId** | **long?**|  | [optional] 
 **type** | [**SystemNotificationRequestType**](SystemNotificationRequestType.md)|  | [optional] 

### Return type

[**SystemNotificationModelIPagedList**](SystemNotificationModelIPagedList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3notificationsıdget"></a>
# **ApiV3NotificationsIdGet**
> SystemNotificationContentModel ApiV3NotificationsIdGet (long? ıd)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3NotificationsIdGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new NotificationApi();
            var ıd = 789;  // long? | 

            try
            {
                SystemNotificationContentModel result = apiInstance.ApiV3NotificationsIdGet(ıd);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling NotificationApi.ApiV3NotificationsIdGet: " + e.Message );
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

[**SystemNotificationContentModel**](SystemNotificationContentModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3notificationsınitget"></a>
# **ApiV3NotificationsInitGet**
> SystemNotificationContentModel ApiV3NotificationsInitGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3NotificationsInitGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new NotificationApi();

            try
            {
                SystemNotificationContentModel result = apiInstance.ApiV3NotificationsInitGet();
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling NotificationApi.ApiV3NotificationsInitGet: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemNotificationContentModel**](SystemNotificationContentModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3notificationsmodulesget"></a>
# **ApiV3NotificationsModulesGet**
> void ApiV3NotificationsModulesGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3NotificationsModulesGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new NotificationApi();

            try
            {
                apiInstance.ApiV3NotificationsModulesGet();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling NotificationApi.ApiV3NotificationsModulesGet: " + e.Message );
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
<a name="apiv3notificationsreadallpost"></a>
# **ApiV3NotificationsReadAllPost**
> void ApiV3NotificationsReadAllPost ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3NotificationsReadAllPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new NotificationApi();

            try
            {
                apiInstance.ApiV3NotificationsReadAllPost();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling NotificationApi.ApiV3NotificationsReadAllPost: " + e.Message );
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
<a name="apiv3notificationsreadpost"></a>
# **ApiV3NotificationsReadPost**
> void ApiV3NotificationsReadPost (SystemNotificationReadModel body = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3NotificationsReadPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new NotificationApi();
            var body = new SystemNotificationReadModel(); // SystemNotificationReadModel |  (optional) 

            try
            {
                apiInstance.ApiV3NotificationsReadPost(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling NotificationApi.ApiV3NotificationsReadPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemNotificationReadModel**](SystemNotificationReadModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3notificationsunreadget"></a>
# **ApiV3NotificationsUnreadGet**
> SystemNotificationCountModel ApiV3NotificationsUnreadGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3NotificationsUnreadGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new NotificationApi();

            try
            {
                SystemNotificationCountModel result = apiInstance.ApiV3NotificationsUnreadGet();
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling NotificationApi.ApiV3NotificationsUnreadGet: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemNotificationCountModel**](SystemNotificationCountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
