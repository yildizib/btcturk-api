# IO.Swagger.Api.AccountApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3AccountAddressPut**](AccountApi.md#apiv3accountaddressput) | **PUT** /api/v3/account/address | 
[**ApiV3AccountBuySellInfoGet**](AccountApi.md#apiv3accountbuysellınfoget) | **GET** /api/v3/account/buy-sell-info | 
[**ApiV3AccountFeaturesGet**](AccountApi.md#apiv3accountfeaturesget) | **GET** /api/v3/account/features | 
[**ApiV3AccountLimitsGet**](AccountApi.md#apiv3accountlimitsget) | **GET** /api/v3/account/limits | 
[**ApiV3AccountPdpaPost**](AccountApi.md#apiv3accountpdpapost) | **POST** /api/v3/account/pdpa | 
[**ApiV3AccountSplashScreenLoginPost**](AccountApi.md#apiv3accountsplashscreenloginpost) | **POST** /api/v3/account/splash-screen-login | 
[**ApiV3AccountTradeFeeRatesGet**](AccountApi.md#apiv3accounttradefeeratesget) | **GET** /api/v3/account/trade-fee-rates | 

<a name="apiv3accountaddressput"></a>
# **ApiV3AccountAddressPut**
> void ApiV3AccountAddressPut (AccountAddressModel body = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3AccountAddressPutExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new AccountApi();
            var body = new AccountAddressModel(); // AccountAddressModel |  (optional) 

            try
            {
                apiInstance.ApiV3AccountAddressPut(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AccountApi.ApiV3AccountAddressPut: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountAddressModel**](AccountAddressModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3accountbuysellınfoget"></a>
# **ApiV3AccountBuySellInfoGet**
> void ApiV3AccountBuySellInfoGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3AccountBuySellInfoGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new AccountApi();

            try
            {
                apiInstance.ApiV3AccountBuySellInfoGet();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AccountApi.ApiV3AccountBuySellInfoGet: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3accountfeaturesget"></a>
# **ApiV3AccountFeaturesGet**
> void ApiV3AccountFeaturesGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3AccountFeaturesGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new AccountApi();

            try
            {
                apiInstance.ApiV3AccountFeaturesGet();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AccountApi.ApiV3AccountFeaturesGet: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3accountlimitsget"></a>
# **ApiV3AccountLimitsGet**
> UserAllLimitsModel ApiV3AccountLimitsGet (string currencySymbol = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3AccountLimitsGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new AccountApi();
            var currencySymbol = currencySymbol_example;  // string |  (optional) 

            try
            {
                UserAllLimitsModel result = apiInstance.ApiV3AccountLimitsGet(currencySymbol);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AccountApi.ApiV3AccountLimitsGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencySymbol** | **string**|  | [optional] 

### Return type

[**UserAllLimitsModel**](UserAllLimitsModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3accountpdpapost"></a>
# **ApiV3AccountPdpaPost**
> void ApiV3AccountPdpaPost (string value = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3AccountPdpaPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new AccountApi();
            var value = value_example;  // string |  (optional) 

            try
            {
                apiInstance.ApiV3AccountPdpaPost(value);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AccountApi.ApiV3AccountPdpaPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **string**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3accountsplashscreenloginpost"></a>
# **ApiV3AccountSplashScreenLoginPost**
> void ApiV3AccountSplashScreenLoginPost (CreateSplashScreenLoginRequestModel body = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3AccountSplashScreenLoginPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new AccountApi();
            var body = new CreateSplashScreenLoginRequestModel(); // CreateSplashScreenLoginRequestModel |  (optional) 

            try
            {
                apiInstance.ApiV3AccountSplashScreenLoginPost(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AccountApi.ApiV3AccountSplashScreenLoginPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSplashScreenLoginRequestModel**](CreateSplashScreenLoginRequestModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3accounttradefeeratesget"></a>
# **ApiV3AccountTradeFeeRatesGet**
> UserTradeFeeRateOutputModel ApiV3AccountTradeFeeRatesGet (OrderMethod orderMethod = null, string pairSymbol = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3AccountTradeFeeRatesGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new AccountApi();
            var orderMethod = new OrderMethod(); // OrderMethod |  (optional) 
            var pairSymbol = pairSymbol_example;  // string |  (optional) 

            try
            {
                UserTradeFeeRateOutputModel result = apiInstance.ApiV3AccountTradeFeeRatesGet(orderMethod, pairSymbol);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AccountApi.ApiV3AccountTradeFeeRatesGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderMethod** | [**OrderMethod**](OrderMethod.md)|  | [optional] 
 **pairSymbol** | **string**|  | [optional] 

### Return type

[**UserTradeFeeRateOutputModel**](UserTradeFeeRateOutputModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
