# CryptoDepositApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3DepositsCryptoCurrencySymbolGet**](CryptoDepositApi.md#apiV3DepositsCryptoCurrencySymbolGet) | **GET** /api/v3/deposits/crypto/{currencySymbol} | 
[**apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet**](CryptoDepositApi.md#apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet) | **GET** /api/v3/deposits/crypto/getnewcryptoaddress/{currencySymbol}/{address} | 

<a name="apiV3DepositsCryptoCurrencySymbolGet"></a>
# **apiV3DepositsCryptoCurrencySymbolGet**
> apiV3DepositsCryptoCurrencySymbolGet(currencySymbol, autoAddressDisabled)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.CryptoDepositApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

CryptoDepositApi apiInstance = new CryptoDepositApi();
CryptoCurrencySymbol currencySymbol = new CryptoCurrencySymbol(); // CryptoCurrencySymbol | 
Boolean autoAddressDisabled = true; // Boolean | 
try {
    apiInstance.apiV3DepositsCryptoCurrencySymbolGet(currencySymbol, autoAddressDisabled);
} catch (ApiException e) {
    System.err.println("Exception when calling CryptoDepositApi#apiV3DepositsCryptoCurrencySymbolGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencySymbol** | [**CryptoCurrencySymbol**](.md)|  |
 **autoAddressDisabled** | **Boolean**|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet"></a>
# **apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet**
> apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet(currencySymbol, address)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.CryptoDepositApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

CryptoDepositApi apiInstance = new CryptoDepositApi();
CryptoCurrencySymbol currencySymbol = new CryptoCurrencySymbol(); // CryptoCurrencySymbol | 
String address = "address_example"; // String | 
try {
    apiInstance.apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet(currencySymbol, address);
} catch (ApiException e) {
    System.err.println("Exception when calling CryptoDepositApi#apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencySymbol** | [**CryptoCurrencySymbol**](.md)|  |
 **address** | **String**|  |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

