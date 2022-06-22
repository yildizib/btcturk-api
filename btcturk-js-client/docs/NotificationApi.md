# BtcTurkAp30.NotificationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV3NotificationsAnnouncementGet**](NotificationApi.md#apiV3NotificationsAnnouncementGet) | **GET** /api/v3/notifications/announcement | 
[**apiV3NotificationsAnnouncementSlugGet**](NotificationApi.md#apiV3NotificationsAnnouncementSlugGet) | **GET** /api/v3/notifications/announcement/{slug} | 
[**apiV3NotificationsCountGet**](NotificationApi.md#apiV3NotificationsCountGet) | **GET** /api/v3/notifications/count | Notification summary.  Unread, read, total
[**apiV3NotificationsGet**](NotificationApi.md#apiV3NotificationsGet) | **GET** /api/v3/notifications | 
[**apiV3NotificationsIdGet**](NotificationApi.md#apiV3NotificationsIdGet) | **GET** /api/v3/notifications/{id} | 
[**apiV3NotificationsInitGet**](NotificationApi.md#apiV3NotificationsInitGet) | **GET** /api/v3/notifications/init | 
[**apiV3NotificationsModulesGet**](NotificationApi.md#apiV3NotificationsModulesGet) | **GET** /api/v3/notifications/modules | 
[**apiV3NotificationsReadAllPost**](NotificationApi.md#apiV3NotificationsReadAllPost) | **POST** /api/v3/notifications/read/all | 
[**apiV3NotificationsReadPost**](NotificationApi.md#apiV3NotificationsReadPost) | **POST** /api/v3/notifications/read | 
[**apiV3NotificationsUnreadGet**](NotificationApi.md#apiV3NotificationsUnreadGet) | **GET** /api/v3/notifications/unread | 

<a name="apiV3NotificationsAnnouncementGet"></a>
# **apiV3NotificationsAnnouncementGet**
> AnnouncementModelIPagedList apiV3NotificationsAnnouncementGet(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.NotificationApi();
let opts = { 
  'pageIndex': 56, // Number | 
  'pageSize': 56, // Number | 
  'showType': new BtcTurkAp30.NotificationShowType() // NotificationShowType | 
};
apiInstance.apiV3NotificationsAnnouncementGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageIndex** | **Number**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **showType** | [**NotificationShowType**](.md)|  | [optional] 

### Return type

[**AnnouncementModelIPagedList**](AnnouncementModelIPagedList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3NotificationsAnnouncementSlugGet"></a>
# **apiV3NotificationsAnnouncementSlugGet**
> AnnouncementDetailModelIPagedList apiV3NotificationsAnnouncementSlugGet(slug)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.NotificationApi();
let slug = "slug_example"; // String | 

apiInstance.apiV3NotificationsAnnouncementSlugGet(slug, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **String**|  | 

### Return type

[**AnnouncementDetailModelIPagedList**](AnnouncementDetailModelIPagedList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3NotificationsCountGet"></a>
# **apiV3NotificationsCountGet**
> [SystemNotificationCountModel] apiV3NotificationsCountGet()

Notification summary.  Unread, read, total

### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.NotificationApi();
apiInstance.apiV3NotificationsCountGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[SystemNotificationCountModel]**](SystemNotificationCountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3NotificationsGet"></a>
# **apiV3NotificationsGet**
> SystemNotificationModelIPagedList apiV3NotificationsGet(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.NotificationApi();
let opts = { 
  'pageIndex': 56, // Number | 
  'pageSize': 56, // Number | 
  'read': true, // Boolean | 
  'moduleId': 789, // Number | 
  'type': new BtcTurkAp30.SystemNotificationRequestType() // SystemNotificationRequestType | 
};
apiInstance.apiV3NotificationsGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageIndex** | **Number**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **read** | **Boolean**|  | [optional] 
 **moduleId** | **Number**|  | [optional] 
 **type** | [**SystemNotificationRequestType**](.md)|  | [optional] 

### Return type

[**SystemNotificationModelIPagedList**](SystemNotificationModelIPagedList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3NotificationsIdGet"></a>
# **apiV3NotificationsIdGet**
> SystemNotificationContentModel apiV3NotificationsIdGet(ıd)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.NotificationApi();
let ıd = 789; // Number | 

apiInstance.apiV3NotificationsIdGet(ıd, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ıd** | **Number**|  | 

### Return type

[**SystemNotificationContentModel**](SystemNotificationContentModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3NotificationsInitGet"></a>
# **apiV3NotificationsInitGet**
> SystemNotificationContentModel apiV3NotificationsInitGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.NotificationApi();
apiInstance.apiV3NotificationsInitGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemNotificationContentModel**](SystemNotificationContentModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiV3NotificationsModulesGet"></a>
# **apiV3NotificationsModulesGet**
> apiV3NotificationsModulesGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.NotificationApi();
apiInstance.apiV3NotificationsModulesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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

<a name="apiV3NotificationsReadAllPost"></a>
# **apiV3NotificationsReadAllPost**
> apiV3NotificationsReadAllPost()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.NotificationApi();
apiInstance.apiV3NotificationsReadAllPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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

<a name="apiV3NotificationsReadPost"></a>
# **apiV3NotificationsReadPost**
> apiV3NotificationsReadPost(opts)



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.NotificationApi();
let opts = { 
  'body': new BtcTurkAp30.SystemNotificationReadModel() // SystemNotificationReadModel | 
};
apiInstance.apiV3NotificationsReadPost(opts, (error, data, response) => {
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
 **body** | [**SystemNotificationReadModel**](SystemNotificationReadModel.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/_*+json
 - **Accept**: Not defined

<a name="apiV3NotificationsUnreadGet"></a>
# **apiV3NotificationsUnreadGet**
> SystemNotificationCountModel apiV3NotificationsUnreadGet()



### Example
```javascript
import {BtcTurkAp30} from 'btc_turk_ap_30';
let defaultClient = BtcTurkAp30.ApiClient.instance;

// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new BtcTurkAp30.NotificationApi();
apiInstance.apiV3NotificationsUnreadGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemNotificationCountModel**](SystemNotificationCountModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

