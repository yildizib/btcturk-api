# NotificationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3NotificationsAnnouncementGet**](NotificationApi.md#apiV3NotificationsAnnouncementGet) | **GET** /api/v3/notifications/announcement | 
[**apiV3NotificationsAnnouncementSlugGet**](NotificationApi.md#apiV3NotificationsAnnouncementSlugGet) | **GET** /api/v3/notifications/announcement/{slug} | 
[**apiV3NotificationsCountGet**](NotificationApi.md#apiV3NotificationsCountGet) | **GET** /api/v3/notifications/count | Notification summary.  Unread, read, total
[**apiV3NotificationsGet**](NotificationApi.md#apiV3NotificationsGet) | **GET** /api/v3/notifications | 
[**apiV3NotificationsIdGet**](NotificationApi.md#apiV3NotificationsIdGet) | **GET** /api/v3/notifications/{id} | 
[**apiV3NotificationsInitGet**](NotificationApi.md#apiV3NotificationsInitGet) | **GET** /api/v3/notifications/init | 
[**apiV3NotificationsModulesGet**](NotificationApi.md#apiV3NotificationsModulesGet) | **GET** /api/v3/notifications/modules | 
[**apiV3NotificationsReadAllPost**](NotificationApi.md#apiV3NotificationsReadAllPost) | **POST** /api/v3/notifications/read/all | 
[**apiV3NotificationsReadPost**](NotificationApi.md#apiV3NotificationsReadPost) | **POST** /api/v3/notifications/read | 
[**apiV3NotificationsUnreadGet**](NotificationApi.md#apiV3NotificationsUnreadGet) | **GET** /api/v3/notifications/unread | 

<a name="apiV3NotificationsAnnouncementGet"></a>
# **apiV3NotificationsAnnouncementGet**
> AnnouncementModelIPagedList apiV3NotificationsAnnouncementGet(pageIndex, pageSize, showType)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NotificationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

NotificationApi apiInstance = new NotificationApi();
Integer pageIndex = 56; // Integer | 
Integer pageSize = 56; // Integer | 
NotificationShowType showType = new NotificationShowType(); // NotificationShowType | 
try {
    AnnouncementModelIPagedList result = apiInstance.apiV3NotificationsAnnouncementGet(pageIndex, pageSize, showType);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling NotificationApi#apiV3NotificationsAnnouncementGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageIndex** | **Integer**|  | [optional]
 **pageSize** | **Integer**|  | [optional]
 **showType** | [**NotificationShowType**](.md)|  | [optional]

### Return type

[**AnnouncementModelIPagedList**](AnnouncementModelIPagedList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3NotificationsAnnouncementSlugGet"></a>
# **apiV3NotificationsAnnouncementSlugGet**
> AnnouncementDetailModelIPagedList apiV3NotificationsAnnouncementSlugGet(slug)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NotificationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

NotificationApi apiInstance = new NotificationApi();
String slug = "slug_example"; // String | 
try {
    AnnouncementDetailModelIPagedList result = apiInstance.apiV3NotificationsAnnouncementSlugGet(slug);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling NotificationApi#apiV3NotificationsAnnouncementSlugGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **String**|  |

### Return type

[**AnnouncementDetailModelIPagedList**](AnnouncementDetailModelIPagedList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3NotificationsCountGet"></a>
# **apiV3NotificationsCountGet**
> List&lt;SystemNotificationCountModel&gt; apiV3NotificationsCountGet()

Notification summary.  Unread, read, total

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NotificationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

NotificationApi apiInstance = new NotificationApi();
try {
    List<SystemNotificationCountModel> result = apiInstance.apiV3NotificationsCountGet();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling NotificationApi#apiV3NotificationsCountGet");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;SystemNotificationCountModel&gt;**](SystemNotificationCountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3NotificationsGet"></a>
# **apiV3NotificationsGet**
> SystemNotificationModelIPagedList apiV3NotificationsGet(pageIndex, pageSize, read, moduleId, type)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NotificationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

NotificationApi apiInstance = new NotificationApi();
Integer pageIndex = 56; // Integer | 
Integer pageSize = 56; // Integer | 
Boolean read = true; // Boolean | 
Long moduleId = 789L; // Long | 
SystemNotificationRequestType type = new SystemNotificationRequestType(); // SystemNotificationRequestType | 
try {
    SystemNotificationModelIPagedList result = apiInstance.apiV3NotificationsGet(pageIndex, pageSize, read, moduleId, type);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling NotificationApi#apiV3NotificationsGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageIndex** | **Integer**|  | [optional] [enum: ]
 **pageSize** | **Integer**|  | [optional] [enum: ]
 **read** | **Boolean**|  | [optional]
 **moduleId** | **Long**|  | [optional]
 **type** | [**SystemNotificationRequestType**](.md)|  | [optional]

### Return type

[**SystemNotificationModelIPagedList**](SystemNotificationModelIPagedList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3NotificationsIdGet"></a>
# **apiV3NotificationsIdGet**
> SystemNotificationContentModel apiV3NotificationsIdGet(ıd)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NotificationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

NotificationApi apiInstance = new NotificationApi();
Long ıd = 789L; // Long | 
try {
    SystemNotificationContentModel result = apiInstance.apiV3NotificationsIdGet(ıd);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling NotificationApi#apiV3NotificationsIdGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ıd** | **Long**|  |

### Return type

[**SystemNotificationContentModel**](SystemNotificationContentModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3NotificationsInitGet"></a>
# **apiV3NotificationsInitGet**
> SystemNotificationContentModel apiV3NotificationsInitGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NotificationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

NotificationApi apiInstance = new NotificationApi();
try {
    SystemNotificationContentModel result = apiInstance.apiV3NotificationsInitGet();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling NotificationApi#apiV3NotificationsInitGet");
    e.printStackTrace();
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

<a name="apiV3NotificationsModulesGet"></a>
# **apiV3NotificationsModulesGet**
> apiV3NotificationsModulesGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NotificationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

NotificationApi apiInstance = new NotificationApi();
try {
    apiInstance.apiV3NotificationsModulesGet();
} catch (ApiException e) {
    System.err.println("Exception when calling NotificationApi#apiV3NotificationsModulesGet");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiV3NotificationsReadAllPost"></a>
# **apiV3NotificationsReadAllPost**
> apiV3NotificationsReadAllPost()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NotificationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

NotificationApi apiInstance = new NotificationApi();
try {
    apiInstance.apiV3NotificationsReadAllPost();
} catch (ApiException e) {
    System.err.println("Exception when calling NotificationApi#apiV3NotificationsReadAllPost");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiV3NotificationsReadPost"></a>
# **apiV3NotificationsReadPost**
> apiV3NotificationsReadPost(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NotificationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

NotificationApi apiInstance = new NotificationApi();
SystemNotificationReadModel body = new SystemNotificationReadModel(); // SystemNotificationReadModel | 
try {
    apiInstance.apiV3NotificationsReadPost(body);
} catch (ApiException e) {
    System.err.println("Exception when calling NotificationApi#apiV3NotificationsReadPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemNotificationReadModel**](SystemNotificationReadModel.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

<a name="apiV3NotificationsUnreadGet"></a>
# **apiV3NotificationsUnreadGet**
> SystemNotificationCountModel apiV3NotificationsUnreadGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NotificationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

NotificationApi apiInstance = new NotificationApi();
try {
    SystemNotificationCountModel result = apiInstance.apiV3NotificationsUnreadGet();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling NotificationApi#apiV3NotificationsUnreadGet");
    e.printStackTrace();
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

