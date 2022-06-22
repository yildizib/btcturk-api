# AccountApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3AccountAddressPut**](AccountApi.md#apiV3AccountAddressPut) | **PUT** /api/v3/account/address | 
[**apiV3AccountBuySellInfoGet**](AccountApi.md#apiV3AccountBuySellInfoGet) | **GET** /api/v3/account/buy-sell-info | 
[**apiV3AccountFeaturesGet**](AccountApi.md#apiV3AccountFeaturesGet) | **GET** /api/v3/account/features | 
[**apiV3AccountLimitsGet**](AccountApi.md#apiV3AccountLimitsGet) | **GET** /api/v3/account/limits | 
[**apiV3AccountPdpaPost**](AccountApi.md#apiV3AccountPdpaPost) | **POST** /api/v3/account/pdpa | 
[**apiV3AccountSplashScreenLoginPost**](AccountApi.md#apiV3AccountSplashScreenLoginPost) | **POST** /api/v3/account/splash-screen-login | 
[**apiV3AccountTradeFeeRatesGet**](AccountApi.md#apiV3AccountTradeFeeRatesGet) | **GET** /api/v3/account/trade-fee-rates | 

<a name="apiV3AccountAddressPut"></a>
# **apiV3AccountAddressPut**
> apiV3AccountAddressPut(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.AccountApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

AccountApi apiInstance = new AccountApi();
AccountAddressModel body = new AccountAddressModel(); // AccountAddressModel | 
try {
    apiInstance.apiV3AccountAddressPut(body);
} catch (ApiException e) {
    System.err.println("Exception when calling AccountApi#apiV3AccountAddressPut");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountAddressModel**](AccountAddressModel.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

<a name="apiV3AccountBuySellInfoGet"></a>
# **apiV3AccountBuySellInfoGet**
> apiV3AccountBuySellInfoGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.AccountApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

AccountApi apiInstance = new AccountApi();
try {
    apiInstance.apiV3AccountBuySellInfoGet();
} catch (ApiException e) {
    System.err.println("Exception when calling AccountApi#apiV3AccountBuySellInfoGet");
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

<a name="apiV3AccountFeaturesGet"></a>
# **apiV3AccountFeaturesGet**
> apiV3AccountFeaturesGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.AccountApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

AccountApi apiInstance = new AccountApi();
try {
    apiInstance.apiV3AccountFeaturesGet();
} catch (ApiException e) {
    System.err.println("Exception when calling AccountApi#apiV3AccountFeaturesGet");
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

<a name="apiV3AccountLimitsGet"></a>
# **apiV3AccountLimitsGet**
> UserAllLimitsModel apiV3AccountLimitsGet(currencySymbol)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.AccountApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

AccountApi apiInstance = new AccountApi();
String currencySymbol = "currencySymbol_example"; // String | 
try {
    UserAllLimitsModel result = apiInstance.apiV3AccountLimitsGet(currencySymbol);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling AccountApi#apiV3AccountLimitsGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencySymbol** | **String**|  | [optional]

### Return type

[**UserAllLimitsModel**](UserAllLimitsModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3AccountPdpaPost"></a>
# **apiV3AccountPdpaPost**
> apiV3AccountPdpaPost(value)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.AccountApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

AccountApi apiInstance = new AccountApi();
String value = "value_example"; // String | 
try {
    apiInstance.apiV3AccountPdpaPost(value);
} catch (ApiException e) {
    System.err.println("Exception when calling AccountApi#apiV3AccountPdpaPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **String**|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiV3AccountSplashScreenLoginPost"></a>
# **apiV3AccountSplashScreenLoginPost**
> apiV3AccountSplashScreenLoginPost(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.AccountApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

AccountApi apiInstance = new AccountApi();
CreateSplashScreenLoginRequestModel body = new CreateSplashScreenLoginRequestModel(); // CreateSplashScreenLoginRequestModel | 
try {
    apiInstance.apiV3AccountSplashScreenLoginPost(body);
} catch (ApiException e) {
    System.err.println("Exception when calling AccountApi#apiV3AccountSplashScreenLoginPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSplashScreenLoginRequestModel**](CreateSplashScreenLoginRequestModel.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

<a name="apiV3AccountTradeFeeRatesGet"></a>
# **apiV3AccountTradeFeeRatesGet**
> UserTradeFeeRateOutputModel apiV3AccountTradeFeeRatesGet(orderMethod, pairSymbol)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.AccountApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

AccountApi apiInstance = new AccountApi();
OrderMethod orderMethod = new OrderMethod(); // OrderMethod | 
String pairSymbol = "pairSymbol_example"; // String | 
try {
    UserTradeFeeRateOutputModel result = apiInstance.apiV3AccountTradeFeeRatesGet(orderMethod, pairSymbol);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling AccountApi#apiV3AccountTradeFeeRatesGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderMethod** | [**OrderMethod**](.md)|  | [optional]
 **pairSymbol** | **String**|  | [optional]

### Return type

[**UserTradeFeeRateOutputModel**](UserTradeFeeRateOutputModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

