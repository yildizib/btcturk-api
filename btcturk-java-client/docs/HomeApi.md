# HomeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiResourcesLanguageGet**](HomeApi.md#apiResourcesLanguageGet) | **GET** /api/resources/language | 
[**apiResourcesLanguageJsonGet**](HomeApi.md#apiResourcesLanguageJsonGet) | **GET** /api/resources/{language}.json | 
[**apiResourcesLocationGet**](HomeApi.md#apiResourcesLocationGet) | **GET** /api/resources/location | 

<a name="apiResourcesLanguageGet"></a>
# **apiResourcesLanguageGet**
> apiResourcesLanguageGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.HomeApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

HomeApi apiInstance = new HomeApi();
try {
    apiInstance.apiResourcesLanguageGet();
} catch (ApiException e) {
    System.err.println("Exception when calling HomeApi#apiResourcesLanguageGet");
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

<a name="apiResourcesLanguageJsonGet"></a>
# **apiResourcesLanguageJsonGet**
> apiResourcesLanguageJsonGet(language, brokerId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.HomeApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

HomeApi apiInstance = new HomeApi();
String language = "language_example"; // String | 
Integer brokerId = 56; // Integer | 
try {
    apiInstance.apiResourcesLanguageJsonGet(language, brokerId);
} catch (ApiException e) {
    System.err.println("Exception when calling HomeApi#apiResourcesLanguageJsonGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **String**|  |
 **brokerId** | **Integer**|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiResourcesLocationGet"></a>
# **apiResourcesLocationGet**
> apiResourcesLocationGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.HomeApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

HomeApi apiInstance = new HomeApi();
try {
    apiInstance.apiResourcesLocationGet();
} catch (ApiException e) {
    System.err.println("Exception when calling HomeApi#apiResourcesLocationGet");
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

