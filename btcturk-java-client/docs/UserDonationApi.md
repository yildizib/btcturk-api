# UserDonationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3UserDonationBanksGet**](UserDonationApi.md#apiV3UserDonationBanksGet) | **GET** /api/v3/user-donation/banks | Bağış kampanyasına ait kullanılabilir bankalar
[**apiV3UserDonationGet**](UserDonationApi.md#apiV3UserDonationGet) | **GET** /api/v3/user-donation | Bağış durumu
[**apiV3UserDonationPost**](UserDonationApi.md#apiV3UserDonationPost) | **POST** /api/v3/user-donation | Yeni bağış kaydı

<a name="apiV3UserDonationBanksGet"></a>
# **apiV3UserDonationBanksGet**
> apiV3UserDonationBanksGet()

Bağış kampanyasına ait kullanılabilir bankalar

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.UserDonationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

UserDonationApi apiInstance = new UserDonationApi();
try {
    apiInstance.apiV3UserDonationBanksGet();
} catch (ApiException e) {
    System.err.println("Exception when calling UserDonationApi#apiV3UserDonationBanksGet");
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

<a name="apiV3UserDonationGet"></a>
# **apiV3UserDonationGet**
> apiV3UserDonationGet()

Bağış durumu

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.UserDonationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

UserDonationApi apiInstance = new UserDonationApi();
try {
    apiInstance.apiV3UserDonationGet();
} catch (ApiException e) {
    System.err.println("Exception when calling UserDonationApi#apiV3UserDonationGet");
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

<a name="apiV3UserDonationPost"></a>
# **apiV3UserDonationPost**
> apiV3UserDonationPost(body)

Yeni bağış kaydı

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.UserDonationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

UserDonationApi apiInstance = new UserDonationApi();
UserDonationRequestModel body = new UserDonationRequestModel(); // UserDonationRequestModel | 
try {
    apiInstance.apiV3UserDonationPost(body);
} catch (ApiException e) {
    System.err.println("Exception when calling UserDonationApi#apiV3UserDonationPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserDonationRequestModel**](UserDonationRequestModel.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: application/json

