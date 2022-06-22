/*
 * BtcTurk API 3.0
 * White label exchange API documentation.
 *
 * OpenAPI spec version: 3.0
 * Contact: development@btctrader.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.api;

import io.swagger.client.ApiCallback;
import io.swagger.client.ApiClient;
import io.swagger.client.ApiException;
import io.swagger.client.ApiResponse;
import io.swagger.client.Configuration;
import io.swagger.client.Pair;
import io.swagger.client.ProgressRequestBody;
import io.swagger.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import io.swagger.client.model.MobileSettingModel;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MobileApi {
    private ApiClient apiClient;

    public MobileApi() {
        this(Configuration.getDefaultApiClient());
    }

    public MobileApi(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return apiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    /**
     * Build call for apiV3MobileInitGet
     * @param brokerId  (optional)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call apiV3MobileInitGetCall(Integer brokerId, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = null;
        
        // create path and map variables
        String localVarPath = "/api/v3/mobile/init";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        if (brokerId != null)
        localVarQueryParams.addAll(apiClient.parameterToPair("brokerId", brokerId));

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) localVarHeaderParams.put("Accept", localVarAccept);

        final String[] localVarContentTypes = {
            
        };
        final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        if(progressListener != null) {
            apiClient.getHttpClient().networkInterceptors().add(new com.squareup.okhttp.Interceptor() {
                @Override
                public com.squareup.okhttp.Response intercept(com.squareup.okhttp.Interceptor.Chain chain) throws IOException {
                    com.squareup.okhttp.Response originalResponse = chain.proceed(chain.request());
                    return originalResponse.newBuilder()
                    .body(new ProgressResponseBody(originalResponse.body(), progressListener))
                    .build();
                }
            });
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return apiClient.buildCall(localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, progressRequestListener);
    }
    
    @SuppressWarnings("rawtypes")
    private com.squareup.okhttp.Call apiV3MobileInitGetValidateBeforeCall(Integer brokerId, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        
        com.squareup.okhttp.Call call = apiV3MobileInitGetCall(brokerId, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * 
     * 
     * @param brokerId  (optional)
     * @return MobileSettingModel
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public MobileSettingModel apiV3MobileInitGet(Integer brokerId) throws ApiException {
        ApiResponse<MobileSettingModel> resp = apiV3MobileInitGetWithHttpInfo(brokerId);
        return resp.getData();
    }

    /**
     * 
     * 
     * @param brokerId  (optional)
     * @return ApiResponse&lt;MobileSettingModel&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<MobileSettingModel> apiV3MobileInitGetWithHttpInfo(Integer brokerId) throws ApiException {
        com.squareup.okhttp.Call call = apiV3MobileInitGetValidateBeforeCall(brokerId, null, null);
        Type localVarReturnType = new TypeToken<MobileSettingModel>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param brokerId  (optional)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call apiV3MobileInitGetAsync(Integer brokerId, final ApiCallback<MobileSettingModel> callback) throws ApiException {

        ProgressResponseBody.ProgressListener progressListener = null;
        ProgressRequestBody.ProgressRequestListener progressRequestListener = null;

        if (callback != null) {
            progressListener = new ProgressResponseBody.ProgressListener() {
                @Override
                public void update(long bytesRead, long contentLength, boolean done) {
                    callback.onDownloadProgress(bytesRead, contentLength, done);
                }
            };

            progressRequestListener = new ProgressRequestBody.ProgressRequestListener() {
                @Override
                public void onRequestProgress(long bytesWritten, long contentLength, boolean done) {
                    callback.onUploadProgress(bytesWritten, contentLength, done);
                }
            };
        }

        com.squareup.okhttp.Call call = apiV3MobileInitGetValidateBeforeCall(brokerId, progressListener, progressRequestListener);
        Type localVarReturnType = new TypeToken<MobileSettingModel>(){}.getType();
        apiClient.executeAsync(call, localVarReturnType, callback);
        return call;
    }
}