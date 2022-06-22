# FiatDepositApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3DepositsFiatBankGet**](FiatDepositApi.md#apiV3DepositsFiatBankGet) | **GET** /api/v3/deposits/fiat/bank | 
[**apiV3DepositsFiatBankSendSmsSlugGet**](FiatDepositApi.md#apiV3DepositsFiatBankSendSmsSlugGet) | **GET** /api/v3/deposits/fiat/bank/send-sms/{slug} | 
[**apiV3DepositsFiatBankSlugGet**](FiatDepositApi.md#apiV3DepositsFiatBankSlugGet) | **GET** /api/v3/deposits/fiat/bank/{slug} | 

<a name="apiV3DepositsFiatBankGet"></a>
# **apiV3DepositsFiatBankGet**
> List&lt;FiatDepositBankAccountModel&gt; apiV3DepositsFiatBankGet(currencySymbol)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.FiatDepositApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

FiatDepositApi apiInstance = new FiatDepositApi();
String currencySymbol = "currencySymbol_example"; // String | 
try {
    List<FiatDepositBankAccountModel> result = apiInstance.apiV3DepositsFiatBankGet(currencySymbol);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FiatDepositApi#apiV3DepositsFiatBankGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencySymbol** | **String**|  | [optional]

### Return type

[**List&lt;FiatDepositBankAccountModel&gt;**](FiatDepositBankAccountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3DepositsFiatBankSendSmsSlugGet"></a>
# **apiV3DepositsFiatBankSendSmsSlugGet**
> apiV3DepositsFiatBankSendSmsSlugGet(slug, currencySymbol)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.FiatDepositApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

FiatDepositApi apiInstance = new FiatDepositApi();
String slug = "slug_example"; // String | 
String currencySymbol = "currencySymbol_example"; // String | 
try {
    apiInstance.apiV3DepositsFiatBankSendSmsSlugGet(slug, currencySymbol);
} catch (ApiException e) {
    System.err.println("Exception when calling FiatDepositApi#apiV3DepositsFiatBankSendSmsSlugGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **String**|  |
 **currencySymbol** | **String**|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiV3DepositsFiatBankSlugGet"></a>
# **apiV3DepositsFiatBankSlugGet**
> FiatDepositBankAccountModel apiV3DepositsFiatBankSlugGet(slug, currencySymbol)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.FiatDepositApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

FiatDepositApi apiInstance = new FiatDepositApi();
String slug = "slug_example"; // String | 
String currencySymbol = "currencySymbol_example"; // String | 
try {
    FiatDepositBankAccountModel result = apiInstance.apiV3DepositsFiatBankSlugGet(slug, currencySymbol);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FiatDepositApi#apiV3DepositsFiatBankSlugGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **String**|  |
 **currencySymbol** | **String**|  | [optional]

### Return type

[**FiatDepositBankAccountModel**](FiatDepositBankAccountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

