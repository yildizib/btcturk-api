# KnowYourCustomerApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3AccountKycPost**](KnowYourCustomerApi.md#apiV3AccountKycPost) | **POST** /api/v3/account/kyc | 

<a name="apiV3AccountKycPost"></a>
# **apiV3AccountKycPost**
> apiV3AccountKycPost(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.KnowYourCustomerApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

KnowYourCustomerApi apiInstance = new KnowYourCustomerApi();
JumioKycIdentityVerificationRequestModel body = new JumioKycIdentityVerificationRequestModel(); // JumioKycIdentityVerificationRequestModel | 
try {
    apiInstance.apiV3AccountKycPost(body);
} catch (ApiException e) {
    System.err.println("Exception when calling KnowYourCustomerApi#apiV3AccountKycPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JumioKycIdentityVerificationRequestModel**](JumioKycIdentityVerificationRequestModel.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

