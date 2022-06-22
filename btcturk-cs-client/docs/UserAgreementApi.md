# IO.Swagger.Api.UserAgreementApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3UserAgreementGet**](UserAgreementApi.md#apiv3useragreementget) | **GET** /api/v3/UserAgreement | 
[**ApiV3UserAgreementPost**](UserAgreementApi.md#apiv3useragreementpost) | **POST** /api/v3/UserAgreement | 
[**ApiV3UserAgreementRiskDisclosureCurrencySymbolGet**](UserAgreementApi.md#apiv3useragreementriskdisclosurecurrencysymbolget) | **GET** /api/v3/user-agreement/risk-disclosure/currency/{symbol} | 
[**ApiV3UserAgreementRiskDisclosurePairPairSymbolGet**](UserAgreementApi.md#apiv3useragreementriskdisclosurepairpairsymbolget) | **GET** /api/v3/user-agreement/risk-disclosure/pair/{pairSymbol} | 
[**ApiV3UserAgreementSlugGet**](UserAgreementApi.md#apiv3useragreementslugget) | **GET** /api/v3/UserAgreement/{slug} | 
[**ApiV3UserAgreementSlugGet_0**](UserAgreementApi.md#apiv3useragreementslugget_0) | **GET** /api/v3/user-agreement/{slug} | 
[**ApiV3UserAgreementSlugPost**](UserAgreementApi.md#apiv3useragreementslugpost) | **POST** /api/v3/user-agreement/{slug} | 

<a name="apiv3useragreementget"></a>
# **ApiV3UserAgreementGet**
> List<UserAgreementModel> ApiV3UserAgreementGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3UserAgreementGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new UserAgreementApi();

            try
            {
                List&lt;UserAgreementModel&gt; result = apiInstance.ApiV3UserAgreementGet();
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling UserAgreementApi.ApiV3UserAgreementGet: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List<UserAgreementModel>**](UserAgreementModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3useragreementpost"></a>
# **ApiV3UserAgreementPost**
> void ApiV3UserAgreementPost (UserAgreementApproveModel body = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3UserAgreementPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new UserAgreementApi();
            var body = new UserAgreementApproveModel(); // UserAgreementApproveModel | Approve id (optional) 

            try
            {
                apiInstance.ApiV3UserAgreementPost(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling UserAgreementApi.ApiV3UserAgreementPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAgreementApproveModel**](UserAgreementApproveModel.md)| Approve id | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3useragreementriskdisclosurecurrencysymbolget"></a>
# **ApiV3UserAgreementRiskDisclosureCurrencySymbolGet**
> CheckCurrencyRiskAgreementResponseModel ApiV3UserAgreementRiskDisclosureCurrencySymbolGet (string symbol, CurrencyTransferType transferType = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3UserAgreementRiskDisclosureCurrencySymbolGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new UserAgreementApi();
            var symbol = symbol_example;  // string | 
            var transferType = new CurrencyTransferType(); // CurrencyTransferType |  (optional) 

            try
            {
                CheckCurrencyRiskAgreementResponseModel result = apiInstance.ApiV3UserAgreementRiskDisclosureCurrencySymbolGet(symbol, transferType);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling UserAgreementApi.ApiV3UserAgreementRiskDisclosureCurrencySymbolGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **string**|  | 
 **transferType** | [**CurrencyTransferType**](CurrencyTransferType.md)|  | [optional] 

### Return type

[**CheckCurrencyRiskAgreementResponseModel**](CheckCurrencyRiskAgreementResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3useragreementriskdisclosurepairpairsymbolget"></a>
# **ApiV3UserAgreementRiskDisclosurePairPairSymbolGet**
> CheckPairRiskAgreementResponseModel ApiV3UserAgreementRiskDisclosurePairPairSymbolGet (string pairSymbol)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3UserAgreementRiskDisclosurePairPairSymbolGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new UserAgreementApi();
            var pairSymbol = pairSymbol_example;  // string | 

            try
            {
                CheckPairRiskAgreementResponseModel result = apiInstance.ApiV3UserAgreementRiskDisclosurePairPairSymbolGet(pairSymbol);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling UserAgreementApi.ApiV3UserAgreementRiskDisclosurePairPairSymbolGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pairSymbol** | **string**|  | 

### Return type

[**CheckPairRiskAgreementResponseModel**](CheckPairRiskAgreementResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3useragreementslugget"></a>
# **ApiV3UserAgreementSlugGet**
> UserAgreementModel ApiV3UserAgreementSlugGet (string slug)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3UserAgreementSlugGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new UserAgreementApi();
            var slug = slug_example;  // string | 

            try
            {
                UserAgreementModel result = apiInstance.ApiV3UserAgreementSlugGet(slug);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling UserAgreementApi.ApiV3UserAgreementSlugGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **string**|  | 

### Return type

[**UserAgreementModel**](UserAgreementModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3useragreementslugget_0"></a>
# **ApiV3UserAgreementSlugGet_0**
> UserAgreementModel ApiV3UserAgreementSlugGet_0 (string slug)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3UserAgreementSlugGet_0Example
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new UserAgreementApi();
            var slug = slug_example;  // string | 

            try
            {
                UserAgreementModel result = apiInstance.ApiV3UserAgreementSlugGet_0(slug);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling UserAgreementApi.ApiV3UserAgreementSlugGet_0: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **string**|  | 

### Return type

[**UserAgreementModel**](UserAgreementModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3useragreementslugpost"></a>
# **ApiV3UserAgreementSlugPost**
> void ApiV3UserAgreementSlugPost (string slug)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3UserAgreementSlugPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new UserAgreementApi();
            var slug = slug_example;  // string | 

            try
            {
                apiInstance.ApiV3UserAgreementSlugPost(slug);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling UserAgreementApi.ApiV3UserAgreementSlugPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **string**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
