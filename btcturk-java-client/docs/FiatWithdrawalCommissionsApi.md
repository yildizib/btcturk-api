# FiatWithdrawalCommissionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3FiatWithdrawalCommissionsGet**](FiatWithdrawalCommissionsApi.md#apiV3FiatWithdrawalCommissionsGet) | **GET** /api/v3/fiat-withdrawal-commissions | 

<a name="apiV3FiatWithdrawalCommissionsGet"></a>
# **apiV3FiatWithdrawalCommissionsGet**
> apiV3FiatWithdrawalCommissionsGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.FiatWithdrawalCommissionsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

FiatWithdrawalCommissionsApi apiInstance = new FiatWithdrawalCommissionsApi();
try {
    apiInstance.apiV3FiatWithdrawalCommissionsGet();
} catch (ApiException e) {
    System.err.println("Exception when calling FiatWithdrawalCommissionsApi#apiV3FiatWithdrawalCommissionsGet");
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

