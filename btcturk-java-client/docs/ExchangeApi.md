# ExchangeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3ExchangeCommissionsGet**](ExchangeApi.md#apiV3ExchangeCommissionsGet) | **GET** /api/v3/exchange/commissions | 
[**apiV3ExchangeLimitsGet**](ExchangeApi.md#apiV3ExchangeLimitsGet) | **GET** /api/v3/exchange/limits | 

<a name="apiV3ExchangeCommissionsGet"></a>
# **apiV3ExchangeCommissionsGet**
> CommissionOutputModel apiV3ExchangeCommissionsGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.ExchangeApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

ExchangeApi apiInstance = new ExchangeApi();
try {
    CommissionOutputModel result = apiInstance.apiV3ExchangeCommissionsGet();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ExchangeApi#apiV3ExchangeCommissionsGet");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CommissionOutputModel**](CommissionOutputModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3ExchangeLimitsGet"></a>
# **apiV3ExchangeLimitsGet**
> LimitOutputModel apiV3ExchangeLimitsGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.ExchangeApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

ExchangeApi apiInstance = new ExchangeApi();
try {
    LimitOutputModel result = apiInstance.apiV3ExchangeLimitsGet();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ExchangeApi#apiV3ExchangeLimitsGet");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LimitOutputModel**](LimitOutputModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

