# FeedbackApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3FeedbackAppRatingPost**](FeedbackApi.md#apiV3FeedbackAppRatingPost) | **POST** /api/v3/feedback/app-rating | 
[**apiV3FeedbackSupportPlatformsGet**](FeedbackApi.md#apiV3FeedbackSupportPlatformsGet) | **GET** /api/v3/feedback/support-platforms | 

<a name="apiV3FeedbackAppRatingPost"></a>
# **apiV3FeedbackAppRatingPost**
> apiV3FeedbackAppRatingPost(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.FeedbackApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

FeedbackApi apiInstance = new FeedbackApi();
AppRatingRequestModel body = new AppRatingRequestModel(); // AppRatingRequestModel | 
try {
    apiInstance.apiV3FeedbackAppRatingPost(body);
} catch (ApiException e) {
    System.err.println("Exception when calling FeedbackApi#apiV3FeedbackAppRatingPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppRatingRequestModel**](AppRatingRequestModel.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: application/json

<a name="apiV3FeedbackSupportPlatformsGet"></a>
# **apiV3FeedbackSupportPlatformsGet**
> apiV3FeedbackSupportPlatformsGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.FeedbackApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

FeedbackApi apiInstance = new FeedbackApi();
try {
    apiInstance.apiV3FeedbackSupportPlatformsGet();
} catch (ApiException e) {
    System.err.println("Exception when calling FeedbackApi#apiV3FeedbackSupportPlatformsGet");
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

