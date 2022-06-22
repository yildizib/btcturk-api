# UserAgreementApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3UserAgreementGet**](UserAgreementApi.md#apiV3UserAgreementGet) | **GET** /api/v3/UserAgreement | 
[**apiV3UserAgreementPost**](UserAgreementApi.md#apiV3UserAgreementPost) | **POST** /api/v3/UserAgreement | 
[**apiV3UserAgreementRiskDisclosureCurrencySymbolGet**](UserAgreementApi.md#apiV3UserAgreementRiskDisclosureCurrencySymbolGet) | **GET** /api/v3/user-agreement/risk-disclosure/currency/{symbol} | 
[**apiV3UserAgreementRiskDisclosurePairPairSymbolGet**](UserAgreementApi.md#apiV3UserAgreementRiskDisclosurePairPairSymbolGet) | **GET** /api/v3/user-agreement/risk-disclosure/pair/{pairSymbol} | 
[**apiV3UserAgreementSlugGet**](UserAgreementApi.md#apiV3UserAgreementSlugGet) | **GET** /api/v3/UserAgreement/{slug} | 
[**apiV3UserAgreementSlugGet_0**](UserAgreementApi.md#apiV3UserAgreementSlugGet_0) | **GET** /api/v3/user-agreement/{slug} | 
[**apiV3UserAgreementSlugPost**](UserAgreementApi.md#apiV3UserAgreementSlugPost) | **POST** /api/v3/user-agreement/{slug} | 

<a name="apiV3UserAgreementGet"></a>
# **apiV3UserAgreementGet**
> List&lt;UserAgreementModel&gt; apiV3UserAgreementGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.UserAgreementApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

UserAgreementApi apiInstance = new UserAgreementApi();
try {
    List<UserAgreementModel> result = apiInstance.apiV3UserAgreementGet();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UserAgreementApi#apiV3UserAgreementGet");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;UserAgreementModel&gt;**](UserAgreementModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3UserAgreementPost"></a>
# **apiV3UserAgreementPost**
> apiV3UserAgreementPost(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.UserAgreementApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

UserAgreementApi apiInstance = new UserAgreementApi();
UserAgreementApproveModel body = new UserAgreementApproveModel(); // UserAgreementApproveModel | Approve id
try {
    apiInstance.apiV3UserAgreementPost(body);
} catch (ApiException e) {
    System.err.println("Exception when calling UserAgreementApi#apiV3UserAgreementPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAgreementApproveModel**](UserAgreementApproveModel.md)| Approve id | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

<a name="apiV3UserAgreementRiskDisclosureCurrencySymbolGet"></a>
# **apiV3UserAgreementRiskDisclosureCurrencySymbolGet**
> CheckCurrencyRiskAgreementResponseModel apiV3UserAgreementRiskDisclosureCurrencySymbolGet(symbol, transferType)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.UserAgreementApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

UserAgreementApi apiInstance = new UserAgreementApi();
String symbol = "symbol_example"; // String | 
CurrencyTransferType transferType = new CurrencyTransferType(); // CurrencyTransferType | 
try {
    CheckCurrencyRiskAgreementResponseModel result = apiInstance.apiV3UserAgreementRiskDisclosureCurrencySymbolGet(symbol, transferType);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UserAgreementApi#apiV3UserAgreementRiskDisclosureCurrencySymbolGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **String**|  |
 **transferType** | [**CurrencyTransferType**](.md)|  | [optional]

### Return type

[**CheckCurrencyRiskAgreementResponseModel**](CheckCurrencyRiskAgreementResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3UserAgreementRiskDisclosurePairPairSymbolGet"></a>
# **apiV3UserAgreementRiskDisclosurePairPairSymbolGet**
> CheckPairRiskAgreementResponseModel apiV3UserAgreementRiskDisclosurePairPairSymbolGet(pairSymbol)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.UserAgreementApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

UserAgreementApi apiInstance = new UserAgreementApi();
String pairSymbol = "pairSymbol_example"; // String | 
try {
    CheckPairRiskAgreementResponseModel result = apiInstance.apiV3UserAgreementRiskDisclosurePairPairSymbolGet(pairSymbol);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UserAgreementApi#apiV3UserAgreementRiskDisclosurePairPairSymbolGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pairSymbol** | **String**|  |

### Return type

[**CheckPairRiskAgreementResponseModel**](CheckPairRiskAgreementResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3UserAgreementSlugGet"></a>
# **apiV3UserAgreementSlugGet**
> UserAgreementModel apiV3UserAgreementSlugGet(slug)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.UserAgreementApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

UserAgreementApi apiInstance = new UserAgreementApi();
String slug = "slug_example"; // String | 
try {
    UserAgreementModel result = apiInstance.apiV3UserAgreementSlugGet(slug);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UserAgreementApi#apiV3UserAgreementSlugGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **String**|  |

### Return type

[**UserAgreementModel**](UserAgreementModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3UserAgreementSlugGet_0"></a>
# **apiV3UserAgreementSlugGet_0**
> UserAgreementModel apiV3UserAgreementSlugGet_0(slug)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.UserAgreementApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

UserAgreementApi apiInstance = new UserAgreementApi();
String slug = "slug_example"; // String | 
try {
    UserAgreementModel result = apiInstance.apiV3UserAgreementSlugGet_0(slug);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UserAgreementApi#apiV3UserAgreementSlugGet_0");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **String**|  |

### Return type

[**UserAgreementModel**](UserAgreementModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3UserAgreementSlugPost"></a>
# **apiV3UserAgreementSlugPost**
> apiV3UserAgreementSlugPost(slug)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.UserAgreementApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

UserAgreementApi apiInstance = new UserAgreementApi();
String slug = "slug_example"; // String | 
try {
    apiInstance.apiV3UserAgreementSlugPost(slug);
} catch (ApiException e) {
    System.err.println("Exception when calling UserAgreementApi#apiV3UserAgreementSlugPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **String**|  |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

