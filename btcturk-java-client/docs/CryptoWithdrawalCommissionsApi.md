# CryptoWithdrawalCommissionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3CryptoWithdrawalCommissionsGet**](CryptoWithdrawalCommissionsApi.md#apiV3CryptoWithdrawalCommissionsGet) | **GET** /api/v3/crypto/withdrawal/commissions | 

<a name="apiV3CryptoWithdrawalCommissionsGet"></a>
# **apiV3CryptoWithdrawalCommissionsGet**
> List&lt;CryptoWithdrawalCommissionsResponseModel&gt; apiV3CryptoWithdrawalCommissionsGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.CryptoWithdrawalCommissionsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

CryptoWithdrawalCommissionsApi apiInstance = new CryptoWithdrawalCommissionsApi();
try {
    List<CryptoWithdrawalCommissionsResponseModel> result = apiInstance.apiV3CryptoWithdrawalCommissionsGet();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CryptoWithdrawalCommissionsApi#apiV3CryptoWithdrawalCommissionsGet");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;CryptoWithdrawalCommissionsResponseModel&gt;**](CryptoWithdrawalCommissionsResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

