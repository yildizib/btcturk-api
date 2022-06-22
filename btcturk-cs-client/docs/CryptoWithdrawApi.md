# IO.Swagger.Api.CryptoWithdrawApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV3WithdrawalsCryptoConfirmCodeDelete**](CryptoWithdrawApi.md#apiv3withdrawalscryptoconfirmcodedelete) | **DELETE** /api/v3/withdrawals/crypto/confirm/{code} | 
[**ApiV3WithdrawalsCryptoConfirmCodeGet**](CryptoWithdrawApi.md#apiv3withdrawalscryptoconfirmcodeget) | **GET** /api/v3/withdrawals/crypto/confirm/{code} | 
[**ApiV3WithdrawalsCryptoConfirmPost**](CryptoWithdrawApi.md#apiv3withdrawalscryptoconfirmpost) | **POST** /api/v3/withdrawals/crypto/confirm | 
[**ApiV3WithdrawalsCryptoValidationCodeGet**](CryptoWithdrawApi.md#apiv3withdrawalscryptovalidationcodeget) | **GET** /api/v3/withdrawals/crypto/validation/{code} | 

<a name="apiv3withdrawalscryptoconfirmcodedelete"></a>
# **ApiV3WithdrawalsCryptoConfirmCodeDelete**
> void ApiV3WithdrawalsCryptoConfirmCodeDelete (string code)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3WithdrawalsCryptoConfirmCodeDeleteExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CryptoWithdrawApi();
            var code = code_example;  // string | 

            try
            {
                apiInstance.ApiV3WithdrawalsCryptoConfirmCodeDelete(code);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CryptoWithdrawApi.ApiV3WithdrawalsCryptoConfirmCodeDelete: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **string**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3withdrawalscryptoconfirmcodeget"></a>
# **ApiV3WithdrawalsCryptoConfirmCodeGet**
> CryptoWithdrawValidationResponseModel ApiV3WithdrawalsCryptoConfirmCodeGet (string code)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3WithdrawalsCryptoConfirmCodeGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CryptoWithdrawApi();
            var code = code_example;  // string | 

            try
            {
                CryptoWithdrawValidationResponseModel result = apiInstance.ApiV3WithdrawalsCryptoConfirmCodeGet(code);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CryptoWithdrawApi.ApiV3WithdrawalsCryptoConfirmCodeGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **string**|  | 

### Return type

[**CryptoWithdrawValidationResponseModel**](CryptoWithdrawValidationResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3withdrawalscryptoconfirmpost"></a>
# **ApiV3WithdrawalsCryptoConfirmPost**
> void ApiV3WithdrawalsCryptoConfirmPost (CryptoWithdrawalDeleteInputModel body = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3WithdrawalsCryptoConfirmPostExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CryptoWithdrawApi();
            var body = new CryptoWithdrawalDeleteInputModel(); // CryptoWithdrawalDeleteInputModel |  (optional) 

            try
            {
                apiInstance.ApiV3WithdrawalsCryptoConfirmPost(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CryptoWithdrawApi.ApiV3WithdrawalsCryptoConfirmPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CryptoWithdrawalDeleteInputModel**](CryptoWithdrawalDeleteInputModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="apiv3withdrawalscryptovalidationcodeget"></a>
# **ApiV3WithdrawalsCryptoValidationCodeGet**
> CryptoWithdrawValidationResponseModel ApiV3WithdrawalsCryptoValidationCodeGet (string code)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV3WithdrawalsCryptoValidationCodeGetExample
    {
        public void main()
        {
            // Configure API key authorization: Bearer
            Configuration.Default.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CryptoWithdrawApi();
            var code = code_example;  // string | 

            try
            {
                CryptoWithdrawValidationResponseModel result = apiInstance.ApiV3WithdrawalsCryptoValidationCodeGet(code);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CryptoWithdrawApi.ApiV3WithdrawalsCryptoValidationCodeGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **string**|  | 

### Return type

[**CryptoWithdrawValidationResponseModel**](CryptoWithdrawValidationResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
