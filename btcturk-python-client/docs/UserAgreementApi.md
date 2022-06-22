# swagger_client.UserAgreementApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_user_agreement_get**](UserAgreementApi.md#api_v3_user_agreement_get) | **GET** /api/v3/UserAgreement | 
[**api_v3_user_agreement_post**](UserAgreementApi.md#api_v3_user_agreement_post) | **POST** /api/v3/UserAgreement | 
[**api_v3_user_agreement_risk_disclosure_currency_symbol_get**](UserAgreementApi.md#api_v3_user_agreement_risk_disclosure_currency_symbol_get) | **GET** /api/v3/user-agreement/risk-disclosure/currency/{symbol} | 
[**api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get**](UserAgreementApi.md#api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get) | **GET** /api/v3/user-agreement/risk-disclosure/pair/{pairSymbol} | 
[**api_v3_user_agreement_slug_get**](UserAgreementApi.md#api_v3_user_agreement_slug_get) | **GET** /api/v3/UserAgreement/{slug} | 
[**api_v3_user_agreement_slug_get_0**](UserAgreementApi.md#api_v3_user_agreement_slug_get_0) | **GET** /api/v3/user-agreement/{slug} | 
[**api_v3_user_agreement_slug_post**](UserAgreementApi.md#api_v3_user_agreement_slug_post) | **POST** /api/v3/user-agreement/{slug} | 

# **api_v3_user_agreement_get**
> list[UserAgreementModel] api_v3_user_agreement_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserAgreementApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.api_v3_user_agreement_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAgreementApi->api_v3_user_agreement_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserAgreementModel]**](UserAgreementModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_user_agreement_post**
> api_v3_user_agreement_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserAgreementApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserAgreementApproveModel() # UserAgreementApproveModel | Approve id (optional)

try:
    api_instance.api_v3_user_agreement_post(body=body)
except ApiException as e:
    print("Exception when calling UserAgreementApi->api_v3_user_agreement_post: %s\n" % e)
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_user_agreement_risk_disclosure_currency_symbol_get**
> CheckCurrencyRiskAgreementResponseModel api_v3_user_agreement_risk_disclosure_currency_symbol_get(symbol, transfer_type=transfer_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserAgreementApi(swagger_client.ApiClient(configuration))
symbol = 'symbol_example' # str | 
transfer_type = swagger_client.CurrencyTransferType() # CurrencyTransferType |  (optional)

try:
    api_response = api_instance.api_v3_user_agreement_risk_disclosure_currency_symbol_get(symbol, transfer_type=transfer_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAgreementApi->api_v3_user_agreement_risk_disclosure_currency_symbol_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 
 **transfer_type** | [**CurrencyTransferType**](.md)|  | [optional] 

### Return type

[**CheckCurrencyRiskAgreementResponseModel**](CheckCurrencyRiskAgreementResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get**
> CheckPairRiskAgreementResponseModel api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get(pair_symbol)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserAgreementApi(swagger_client.ApiClient(configuration))
pair_symbol = 'pair_symbol_example' # str | 

try:
    api_response = api_instance.api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get(pair_symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAgreementApi->api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_symbol** | **str**|  | 

### Return type

[**CheckPairRiskAgreementResponseModel**](CheckPairRiskAgreementResponseModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_user_agreement_slug_get**
> UserAgreementModel api_v3_user_agreement_slug_get(slug)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserAgreementApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | 

try:
    api_response = api_instance.api_v3_user_agreement_slug_get(slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAgreementApi->api_v3_user_agreement_slug_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**UserAgreementModel**](UserAgreementModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_user_agreement_slug_get_0**
> UserAgreementModel api_v3_user_agreement_slug_get_0(slug)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserAgreementApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | 

try:
    api_response = api_instance.api_v3_user_agreement_slug_get_0(slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAgreementApi->api_v3_user_agreement_slug_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**UserAgreementModel**](UserAgreementModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_user_agreement_slug_post**
> api_v3_user_agreement_slug_post(slug)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserAgreementApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | 

try:
    api_instance.api_v3_user_agreement_slug_post(slug)
except ApiException as e:
    print("Exception when calling UserAgreementApi->api_v3_user_agreement_slug_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

