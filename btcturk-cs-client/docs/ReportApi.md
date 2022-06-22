# IO.Swagger.Api.ReportApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3ReportDepositAndWithdrawalPost**](ReportApi.md#apiv3reportdepositandwithdrawalpost) | **POST** /api/v3/report/deposit-and-withdrawal | 
[**ApiV3ReportGet**](ReportApi.md#apiv3reportget) | **GET** /api/v3/report | 
[**ApiV3ReportTradeHistoryPost**](ReportApi.md#apiv3reporttradehistorypost) | **POST** /api/v3/report/trade-history | 
[**ApiV3ReportTransactionHistoryPost**](ReportApi.md#apiv3reporttransactionhistorypost) | **POST** /api/v3/report/transaction-history | 

<a name="apiv3reportdepositandwithdrawalpost"></a>
# **ApiV3ReportDepositAndWithdrawalPost**
> void ApiV3ReportDepositAndWithdrawalPost (ReportDepositWithdrawalInputModel body = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3ReportDepositAndWithdrawalPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new ReportApi();
            var body = new ReportDepositWithdrawalInputModel(); // ReportDepositWithdrawalInputModel |  (optional) 

            try
            {
                apiInstance.ApiV3ReportDepositAndWithdrawalPost(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling ReportApi.ApiV3ReportDepositAndWithdrawalPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportDepositWithdrawalInputModel**](ReportDepositWithdrawalInputModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3reportget"></a>
# **ApiV3ReportGet**
> void ApiV3ReportGet ()



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3ReportGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new ReportApi();

            try
            {
                apiInstance.ApiV3ReportGet();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling ReportApi.ApiV3ReportGet: " + e.Message );
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
<a name="apiv3reporttradehistorypost"></a>
# **ApiV3ReportTradeHistoryPost**
> void ApiV3ReportTradeHistoryPost (ReportTradeHistoryInputModel body = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3ReportTradeHistoryPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new ReportApi();
            var body = new ReportTradeHistoryInputModel(); // ReportTradeHistoryInputModel |  (optional) 

            try
            {
                apiInstance.ApiV3ReportTradeHistoryPost(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling ReportApi.ApiV3ReportTradeHistoryPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportTradeHistoryInputModel**](ReportTradeHistoryInputModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3reporttransactionhistorypost"></a>
# **ApiV3ReportTransactionHistoryPost**
> void ApiV3ReportTransactionHistoryPost (ReportTransactionHistoryInputModel body = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3ReportTransactionHistoryPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new ReportApi();
            var body = new ReportTransactionHistoryInputModel(); // ReportTransactionHistoryInputModel |  (optional) 

            try
            {
                apiInstance.ApiV3ReportTransactionHistoryPost(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling ReportApi.ApiV3ReportTransactionHistoryPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportTransactionHistoryInputModel**](ReportTransactionHistoryInputModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
