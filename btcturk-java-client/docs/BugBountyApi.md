# BugBountyApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3BugBountiesHallOfFameGet**](BugBountyApi.md#apiV3BugBountiesHallOfFameGet) | **GET** /api/v3/bug-bounties/hall-of-fame | 
[**apiV3BugBountiesPost**](BugBountyApi.md#apiV3BugBountiesPost) | **POST** /api/v3/bug-bounties | 

<a name="apiV3BugBountiesHallOfFameGet"></a>
# **apiV3BugBountiesHallOfFameGet**
> List&lt;HallOfFrameResponseModel&gt; apiV3BugBountiesHallOfFameGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.BugBountyApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

BugBountyApi apiInstance = new BugBountyApi();
try {
    List<HallOfFrameResponseModel> result = apiInstance.apiV3BugBountiesHallOfFameGet();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling BugBountyApi#apiV3BugBountiesHallOfFameGet");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;HallOfFrameResponseModel&gt;**](HallOfFrameResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3BugBountiesPost"></a>
# **apiV3BugBountiesPost**
> apiV3BugBountiesPost(body, xClientİd)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.BugBountyApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

BugBountyApi apiInstance = new BugBountyApi();
BugBountyNoticeRequestModel body = new BugBountyNoticeRequestModel(); // BugBountyNoticeRequestModel | 
String xClientİd = "xClientİd_example"; // String | 
try {
    apiInstance.apiV3BugBountiesPost(body, xClientİd);
} catch (ApiException e) {
    System.err.println("Exception when calling BugBountyApi#apiV3BugBountiesPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BugBountyNoticeRequestModel**](BugBountyNoticeRequestModel.md)|  | [optional]
 **xClientİd** | **String**|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: application/json

