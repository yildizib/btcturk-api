# MobileApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3MobileInitGet**](MobileApi.md#apiV3MobileInitGet) | **GET** /api/v3/mobile/init | 

<a name="apiV3MobileInitGet"></a>
# **apiV3MobileInitGet**
> MobileSettingModel apiV3MobileInitGet(brokerId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.MobileApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

MobileApi apiInstance = new MobileApi();
Integer brokerId = 56; // Integer | 
try {
    MobileSettingModel result = apiInstance.apiV3MobileInitGet(brokerId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling MobileApi#apiV3MobileInitGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brokerId** | **Integer**|  | [optional]

### Return type

[**MobileSettingModel**](MobileSettingModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

