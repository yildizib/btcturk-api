# SupportPlatformsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3SupportPlatformsGet**](SupportPlatformsApi.md#apiV3SupportPlatformsGet) | **GET** /api/v3/support-platforms | 
[**apiV3SupportPlatformsZendeskChatJwtPlatformGet**](SupportPlatformsApi.md#apiV3SupportPlatformsZendeskChatJwtPlatformGet) | **GET** /api/v3/support-platforms/zendesk/chat-jwt/{platform} | 
[**apiV3SupportPlatformsZendeskMobileJwtPlatformPost**](SupportPlatformsApi.md#apiV3SupportPlatformsZendeskMobileJwtPlatformPost) | **POST** /api/v3/support-platforms/zendesk/mobile-jwt/{platform} | 
[**apiV3SupportPlatformsZendeskSessionsPost**](SupportPlatformsApi.md#apiV3SupportPlatformsZendeskSessionsPost) | **POST** /api/v3/support-platforms/zendesk/sessions | 

<a name="apiV3SupportPlatformsGet"></a>
# **apiV3SupportPlatformsGet**
> apiV3SupportPlatformsGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.SupportPlatformsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

SupportPlatformsApi apiInstance = new SupportPlatformsApi();
try {
    apiInstance.apiV3SupportPlatformsGet();
} catch (ApiException e) {
    System.err.println("Exception when calling SupportPlatformsApi#apiV3SupportPlatformsGet");
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

<a name="apiV3SupportPlatformsZendeskChatJwtPlatformGet"></a>
# **apiV3SupportPlatformsZendeskChatJwtPlatformGet**
> apiV3SupportPlatformsZendeskChatJwtPlatformGet(platform)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.SupportPlatformsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

SupportPlatformsApi apiInstance = new SupportPlatformsApi();
String platform = "platform_example"; // String | 
try {
    apiInstance.apiV3SupportPlatformsZendeskChatJwtPlatformGet(platform);
} catch (ApiException e) {
    System.err.println("Exception when calling SupportPlatformsApi#apiV3SupportPlatformsZendeskChatJwtPlatformGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **String**|  |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiV3SupportPlatformsZendeskMobileJwtPlatformPost"></a>
# **apiV3SupportPlatformsZendeskMobileJwtPlatformPost**
> apiV3SupportPlatformsZendeskMobileJwtPlatformPost(platform, userToken)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.SupportPlatformsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

SupportPlatformsApi apiInstance = new SupportPlatformsApi();
String platform = "platform_example"; // String | 
String userToken = "userToken_example"; // String | 
try {
    apiInstance.apiV3SupportPlatformsZendeskMobileJwtPlatformPost(platform, userToken);
} catch (ApiException e) {
    System.err.println("Exception when calling SupportPlatformsApi#apiV3SupportPlatformsZendeskMobileJwtPlatformPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **String**|  |
 **userToken** | **String**|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

<a name="apiV3SupportPlatformsZendeskSessionsPost"></a>
# **apiV3SupportPlatformsZendeskSessionsPost**
> apiV3SupportPlatformsZendeskSessionsPost()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.SupportPlatformsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

SupportPlatformsApi apiInstance = new SupportPlatformsApi();
try {
    apiInstance.apiV3SupportPlatformsZendeskSessionsPost();
} catch (ApiException e) {
    System.err.println("Exception when calling SupportPlatformsApi#apiV3SupportPlatformsZendeskSessionsPost");
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

