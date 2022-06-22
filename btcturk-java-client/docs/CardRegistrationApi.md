# CardRegistrationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3CardRegistrationGet**](CardRegistrationApi.md#apiV3CardRegistrationGet) | **GET** /api/v3/card-registration | 
[**apiV3CardRegistrationPost**](CardRegistrationApi.md#apiV3CardRegistrationPost) | **POST** /api/v3/card-registration | 

<a name="apiV3CardRegistrationGet"></a>
# **apiV3CardRegistrationGet**
> apiV3CardRegistrationGet()



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.CardRegistrationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

CardRegistrationApi apiInstance = new CardRegistrationApi();
try {
    apiInstance.apiV3CardRegistrationGet();
} catch (ApiException e) {
    System.err.println("Exception when calling CardRegistrationApi#apiV3CardRegistrationGet");
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

<a name="apiV3CardRegistrationPost"></a>
# **apiV3CardRegistrationPost**
> apiV3CardRegistrationPost(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.CardRegistrationApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: Bearer
ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
Bearer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.setApiKeyPrefix("Token");

CardRegistrationApi apiInstance = new CardRegistrationApi();
CardRegistrationRequestViewModel body = new CardRegistrationRequestViewModel(); // CardRegistrationRequestViewModel | 
try {
    apiInstance.apiV3CardRegistrationPost(body);
} catch (ApiException e) {
    System.err.println("Exception when calling CardRegistrationApi#apiV3CardRegistrationPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CardRegistrationRequestViewModel**](CardRegistrationRequestViewModel.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

