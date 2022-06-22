# CryptoWithdrawApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3WithdrawalsCryptoConfirmCodeDelete**](CryptoWithdrawApi.md#apiV3WithdrawalsCryptoConfirmCodeDelete) | **DELETE** /api/v3/withdrawals/crypto/confirm/{code} | 
[**apiV3WithdrawalsCryptoConfirmCodeGet**](CryptoWithdrawApi.md#apiV3WithdrawalsCryptoConfirmCodeGet) | **GET** /api/v3/withdrawals/crypto/confirm/{code} | 
[**apiV3WithdrawalsCryptoConfirmPost**](CryptoWithdrawApi.md#apiV3WithdrawalsCryptoConfirmPost) | **POST** /api/v3/withdrawals/crypto/confirm | 
[**apiV3WithdrawalsCryptoValidationCodeGet**](CryptoWithdrawApi.md#apiV3WithdrawalsCryptoValidationCodeGet) | **GET** /api/v3/withdrawals/crypto/validation/{code} | 

<a name="apiV3WithdrawalsCryptoConfirmCodeDelete"></a>
# **apiV3WithdrawalsCryptoConfirmCodeDelete**
> apiV3WithdrawalsCryptoConfirmCodeDelete(code)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.CryptoWithdrawApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

CryptoWithdrawApi apiInstance = new CryptoWithdrawApi();
String code = "code_example"; // String | 
try {
    apiInstance.apiV3WithdrawalsCryptoConfirmCodeDelete(code);
} catch (ApiException e) {
    System.err.println("Exception when calling CryptoWithdrawApi#apiV3WithdrawalsCryptoConfirmCodeDelete");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **String**|  |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3WithdrawalsCryptoConfirmCodeGet"></a>
# **apiV3WithdrawalsCryptoConfirmCodeGet**
> CryptoWithdrawValidationResponseModel apiV3WithdrawalsCryptoConfirmCodeGet(code)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.CryptoWithdrawApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

CryptoWithdrawApi apiInstance = new CryptoWithdrawApi();
String code = "code_example"; // String | 
try {
    CryptoWithdrawValidationResponseModel result = apiInstance.apiV3WithdrawalsCryptoConfirmCodeGet(code);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CryptoWithdrawApi#apiV3WithdrawalsCryptoConfirmCodeGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **String**|  |

### Return type

[**CryptoWithdrawValidationResponseModel**](CryptoWithdrawValidationResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3WithdrawalsCryptoConfirmPost"></a>
# **apiV3WithdrawalsCryptoConfirmPost**
> apiV3WithdrawalsCryptoConfirmPost(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.CryptoWithdrawApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

CryptoWithdrawApi apiInstance = new CryptoWithdrawApi();
CryptoWithdrawalDeleteInputModel body = new CryptoWithdrawalDeleteInputModel(); // CryptoWithdrawalDeleteInputModel | 
try {
    apiInstance.apiV3WithdrawalsCryptoConfirmPost(body);
} catch (ApiException e) {
    System.err.println("Exception when calling CryptoWithdrawApi#apiV3WithdrawalsCryptoConfirmPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CryptoWithdrawalDeleteInputModel**](CryptoWithdrawalDeleteInputModel.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: application/json

<a name="apiV3WithdrawalsCryptoValidationCodeGet"></a>
# **apiV3WithdrawalsCryptoValidationCodeGet**
> CryptoWithdrawValidationResponseModel apiV3WithdrawalsCryptoValidationCodeGet(code)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.CryptoWithdrawApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

CryptoWithdrawApi apiInstance = new CryptoWithdrawApi();
String code = "code_example"; // String | 
try {
    CryptoWithdrawValidationResponseModel result = apiInstance.apiV3WithdrawalsCryptoValidationCodeGet(code);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CryptoWithdrawApi#apiV3WithdrawalsCryptoValidationCodeGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **String**|  |

### Return type

[**CryptoWithdrawValidationResponseModel**](CryptoWithdrawValidationResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

