# IO.Swagger.Api.FiatDepositApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3DepositsFiatBankGet**](FiatDepositApi.md#apiv3depositsfiatbankget) | **GET** /api/v3/deposits/fiat/bank | 
[**ApiV3DepositsFiatBankSendSmsSlugGet**](FiatDepositApi.md#apiv3depositsfiatbanksendsmsslugget) | **GET** /api/v3/deposits/fiat/bank/send-sms/{slug} | 
[**ApiV3DepositsFiatBankSlugGet**](FiatDepositApi.md#apiv3depositsfiatbankslugget) | **GET** /api/v3/deposits/fiat/bank/{slug} | 

<a name="apiv3depositsfiatbankget"></a>
# **ApiV3DepositsFiatBankGet**
> List<FiatDepositBankAccountModel> ApiV3DepositsFiatBankGet (string currencySymbol = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3DepositsFiatBankGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new FiatDepositApi();
            var currencySymbol = currencySymbol_example;  // string |  (optional) 

            try
            {
                List&lt;FiatDepositBankAccountModel&gt; result = apiInstance.ApiV3DepositsFiatBankGet(currencySymbol);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling FiatDepositApi.ApiV3DepositsFiatBankGet: " + e.Message );
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

[**List<FiatDepositBankAccountModel>**](FiatDepositBankAccountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3depositsfiatbanksendsmsslugget"></a>
# **ApiV3DepositsFiatBankSendSmsSlugGet**
> void ApiV3DepositsFiatBankSendSmsSlugGet (string slug, string currencySymbol = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3DepositsFiatBankSendSmsSlugGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new FiatDepositApi();
            var slug = slug_example;  // string | 
            var currencySymbol = currencySymbol_example;  // string |  (optional) 

            try
            {
                apiInstance.ApiV3DepositsFiatBankSendSmsSlugGet(slug, currencySymbol);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling FiatDepositApi.ApiV3DepositsFiatBankSendSmsSlugGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **string**|  | 
 **currencySymbol** | **string**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3depositsfiatbankslugget"></a>
# **ApiV3DepositsFiatBankSlugGet**
> FiatDepositBankAccountModel ApiV3DepositsFiatBankSlugGet (string slug, string currencySymbol = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3DepositsFiatBankSlugGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new FiatDepositApi();
            var slug = slug_example;  // string | 
            var currencySymbol = currencySymbol_example;  // string |  (optional) 

            try
            {
                FiatDepositBankAccountModel result = apiInstance.ApiV3DepositsFiatBankSlugGet(slug, currencySymbol);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling FiatDepositApi.ApiV3DepositsFiatBankSlugGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **string**|  | 
 **currencySymbol** | **string**|  | [optional] 

### Return type

[**FiatDepositBankAccountModel**](FiatDepositBankAccountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
