# BtcTurkAp30.CryptoDepositApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3DepositsCryptoCurrencySymbolGet**](CryptoDepositApi.md#apiV3DepositsCryptoCurrencySymbolGet) | **GET** /api/v3/deposits/crypto/{currencySymbol} | 
[**apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet**](CryptoDepositApi.md#apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet) | **GET** /api/v3/deposits/crypto/getnewcryptoaddress/{currencySymbol}/{address} | 

<a name="apiV3DepositsCryptoCurrencySymbolGet"></a>
# **apiV3DepositsCryptoCurrencySymbolGet**
> apiV3DepositsCryptoCurrencySymbolGet(currencySymbol, opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.CryptoDepositApi();
let currencySymbol = new BtcTurkAp30.CryptoCurrencySymbol(); // CryptoCurrencySymbol | 
let opts = { 
  'autoAddressDisabled': true // Boolean | 
};
apiInstance.apiV3DepositsCryptoCurrencySymbolGet(currencySymbol, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.CryptoDepositApi();
let currencySymbol = new BtcTurkAp30.CryptoCurrencySymbol(); // CryptoCurrencySymbol | 
let address = "address_example"; // String | 

apiInstance.apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet(currencySymbol, address, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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

