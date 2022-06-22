# ReportApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3ReportDepositAndWithdrawalPost**](ReportApi.md#apiV3ReportDepositAndWithdrawalPost) | **POST** /api/v3/report/deposit-and-withdrawal | 
[**apiV3ReportGet**](ReportApi.md#apiV3ReportGet) | **GET** /api/v3/report | 
[**apiV3ReportTradeHistoryPost**](ReportApi.md#apiV3ReportTradeHistoryPost) | **POST** /api/v3/report/trade-history | 
[**apiV3ReportTransactionHistoryPost**](ReportApi.md#apiV3ReportTransactionHistoryPost) | **POST** /api/v3/report/transaction-history | 

<a name="apiV3ReportDepositAndWithdrawalPost"></a>
# **apiV3ReportDepositAndWithdrawalPost**
> apiV3ReportDepositAndWithdrawalPost(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.ReportApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

ReportApi apiInstance = new ReportApi();
ReportDepositWithdrawalInputModel body = new ReportDepositWithdrawalInputModel(); // ReportDepositWithdrawalInputModel | 
try {
    apiInstance.apiV3ReportDepositAndWithdrawalPost(body);
} catch (ApiException e) {
    System.err.println("Exception when calling ReportApi#apiV3ReportDepositAndWithdrawalPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportDepositWithdrawalInputModel**](ReportDepositWithdrawalInputModel.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

<a name="apiV3ReportGet"></a>
# **apiV3ReportGet**
> apiV3ReportGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.ReportApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

ReportApi apiInstance = new ReportApi();
try {
    apiInstance.apiV3ReportGet();
} catch (ApiException e) {
    System.err.println("Exception when calling ReportApi#apiV3ReportGet");
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

<a name="apiV3ReportTradeHistoryPost"></a>
# **apiV3ReportTradeHistoryPost**
> apiV3ReportTradeHistoryPost(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.ReportApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

ReportApi apiInstance = new ReportApi();
ReportTradeHistoryInputModel body = new ReportTradeHistoryInputModel(); // ReportTradeHistoryInputModel | 
try {
    apiInstance.apiV3ReportTradeHistoryPost(body);
} catch (ApiException e) {
    System.err.println("Exception when calling ReportApi#apiV3ReportTradeHistoryPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportTradeHistoryInputModel**](ReportTradeHistoryInputModel.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

<a name="apiV3ReportTransactionHistoryPost"></a>
# **apiV3ReportTransactionHistoryPost**
> apiV3ReportTransactionHistoryPost(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.ReportApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

ReportApi apiInstance = new ReportApi();
ReportTransactionHistoryInputModel body = new ReportTransactionHistoryInputModel(); // ReportTransactionHistoryInputModel | 
try {
    apiInstance.apiV3ReportTransactionHistoryPost(body);
} catch (ApiException e) {
    System.err.println("Exception when calling ReportApi#apiV3ReportTransactionHistoryPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportTransactionHistoryInputModel**](ReportTransactionHistoryInputModel.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

