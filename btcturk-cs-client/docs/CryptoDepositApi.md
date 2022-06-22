# IO.Swagger.Api.CryptoDepositApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3DepositsCryptoCurrencySymbolGet**](CryptoDepositApi.md#apiv3depositscryptocurrencysymbolget) | **GET** /api/v3/deposits/crypto/{currencySymbol} | 
[**ApiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet**](CryptoDepositApi.md#apiv3depositscryptogetnewcryptoaddresscurrencysymboladdressget) | **GET** /api/v3/deposits/crypto/getnewcryptoaddress/{currencySymbol}/{address} | 

<a name="apiv3depositscryptocurrencysymbolget"></a>
# **ApiV3DepositsCryptoCurrencySymbolGet**
> void ApiV3DepositsCryptoCurrencySymbolGet (CryptoCurrencySymbol currencySymbol, bool? autoAddressDisabled = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3DepositsCryptoCurrencySymbolGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CryptoDepositApi();
            var currencySymbol = new CryptoCurrencySymbol(); // CryptoCurrencySymbol | 
            var autoAddressDisabled = true;  // bool? |  (optional) 

            try
            {
                apiInstance.ApiV3DepositsCryptoCurrencySymbolGet(currencySymbol, autoAddressDisabled);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CryptoDepositApi.ApiV3DepositsCryptoCurrencySymbolGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencySymbol** | [**CryptoCurrencySymbol**](CryptoCurrencySymbol.md)|  | 
 **autoAddressDisabled** | **bool?**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3depositscryptogetnewcryptoaddresscurrencysymboladdressget"></a>
# **ApiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet**
> void ApiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet (CryptoCurrencySymbol currencySymbol, string address)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CryptoDepositApi();
            var currencySymbol = new CryptoCurrencySymbol(); // CryptoCurrencySymbol | 
            var address = address_example;  // string | 

            try
            {
                apiInstance.ApiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet(currencySymbol, address);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CryptoDepositApi.ApiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencySymbol** | [**CryptoCurrencySymbol**](CryptoCurrencySymbol.md)|  | 
 **address** | **string**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
