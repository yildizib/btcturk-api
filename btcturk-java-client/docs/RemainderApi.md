# RemainderApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3RemainderGet**](RemainderApi.md#apiV3RemainderGet) | **GET** /api/v3/remainder | 
[**apiV3RemainderPost**](RemainderApi.md#apiV3RemainderPost) | **POST** /api/v3/remainder | 

<a name="apiV3RemainderGet"></a>
# **apiV3RemainderGet**
> apiV3RemainderGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RemainderApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

RemainderApi apiInstance = new RemainderApi();
try {
    apiInstance.apiV3RemainderGet();
} catch (ApiException e) {
    System.err.println("Exception when calling RemainderApi#apiV3RemainderGet");
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

<a name="apiV3RemainderPost"></a>
# **apiV3RemainderPost**
> apiV3RemainderPost(currencyId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RemainderApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

RemainderApi apiInstance = new RemainderApi();
Long currencyId = 789L; // Long | 
try {
    apiInstance.apiV3RemainderPost(currencyId);
} catch (ApiException e) {
    System.err.println("Exception when calling RemainderApi#apiV3RemainderPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencyId** | **Long**|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

