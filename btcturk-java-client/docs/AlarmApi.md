# AlarmApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3AlarmGet**](AlarmApi.md#apiV3AlarmGet) | **GET** /api/v3/alarm | 
[**apiV3AlarmIdDelete**](AlarmApi.md#apiV3AlarmIdDelete) | **DELETE** /api/v3/alarm/{id} | 
[**apiV3AlarmPost**](AlarmApi.md#apiV3AlarmPost) | **POST** /api/v3/alarm | 
[**apiV3AlarmPut**](AlarmApi.md#apiV3AlarmPut) | **PUT** /api/v3/alarm | 

<a name="apiV3AlarmGet"></a>
# **apiV3AlarmGet**
> apiV3AlarmGet(ısCompleted, type)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.AlarmApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

AlarmApi apiInstance = new AlarmApi();
Boolean ısCompleted = true; // Boolean | 
Integer type = 56; // Integer | 
try {
    apiInstance.apiV3AlarmGet(ısCompleted, type);
} catch (ApiException e) {
    System.err.println("Exception when calling AlarmApi#apiV3AlarmGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ısCompleted** | **Boolean**|  | [optional]
 **type** | **Integer**|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiV3AlarmIdDelete"></a>
# **apiV3AlarmIdDelete**
> apiV3AlarmIdDelete(ıd)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.AlarmApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

AlarmApi apiInstance = new AlarmApi();
Long ıd = 789L; // Long | 
try {
    apiInstance.apiV3AlarmIdDelete(ıd);
} catch (ApiException e) {
    System.err.println("Exception when calling AlarmApi#apiV3AlarmIdDelete");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ıd** | **Long**|  |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiV3AlarmPost"></a>
# **apiV3AlarmPost**
> apiV3AlarmPost(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.AlarmApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

AlarmApi apiInstance = new AlarmApi();
CreateAlarmRequest body = new CreateAlarmRequest(); // CreateAlarmRequest | 
try {
    apiInstance.apiV3AlarmPost(body);
} catch (ApiException e) {
    System.err.println("Exception when calling AlarmApi#apiV3AlarmPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAlarmRequest**](CreateAlarmRequest.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

<a name="apiV3AlarmPut"></a>
# **apiV3AlarmPut**
> apiV3AlarmPut(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.AlarmApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

AlarmApi apiInstance = new AlarmApi();
List<Long> body = Arrays.asList(56L); // List<Long> | 
try {
    apiInstance.apiV3AlarmPut(body);
} catch (ApiException e) {
    System.err.println("Exception when calling AlarmApi#apiV3AlarmPut");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**List&lt;Long&gt;**](Long.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

