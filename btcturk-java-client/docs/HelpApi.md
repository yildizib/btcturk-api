# HelpApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3HelpBuySellCommissionsGet**](HelpApi.md#apiV3HelpBuySellCommissionsGet) | **GET** /api/v3/help/buy-sell-commissions | 

<a name="apiV3HelpBuySellCommissionsGet"></a>
# **apiV3HelpBuySellCommissionsGet**
> apiV3HelpBuySellCommissionsGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.HelpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

HelpApi apiInstance = new HelpApi();
try {
    apiInstance.apiV3HelpBuySellCommissionsGet();
} catch (ApiException e) {
    System.err.println("Exception when calling HelpApi#apiV3HelpBuySellCommissionsGet");
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

