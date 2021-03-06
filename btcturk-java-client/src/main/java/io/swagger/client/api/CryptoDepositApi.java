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


import io.swagger.client.model.CryptoCurrencySymbol;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CryptoDepositApi {
    private ApiClient apiClient;

    public CryptoDepositApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CryptoDepositApi(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return apiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    /**
     * Build call for apiV3DepositsCryptoCurrencySymbolGet
     * @param currencySymbol  (required)
     * @param autoAddressDisabled  (optional)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call apiV3DepositsCryptoCurrencySymbolGetCall(CryptoCurrencySymbol currencySymbol, Boolean autoAddressDisabled, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = null;
        
        // create path and map variables
        String localVarPath = "/api/v3/deposits/crypto/{currencySymbol}"
            .replaceAll("\\{" + "currencySymbol" + "\\}", apiClient.escapeString(currencySymbol.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        if (autoAddressDisabled != null)
        localVarQueryParams.addAll(apiClient.parameterToPair("autoAddressDisabled", autoAddressDisabled));

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            
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
    private com.squareup.okhttp.Call apiV3DepositsCryptoCurrencySymbolGetValidateBeforeCall(CryptoCurrencySymbol currencySymbol, Boolean autoAddressDisabled, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        // verify the required parameter 'currencySymbol' is set
        if (currencySymbol == null) {
            throw new ApiException("Missing the required parameter 'currencySymbol' when calling apiV3DepositsCryptoCurrencySymbolGet(Async)");
        }
        
        com.squareup.okhttp.Call call = apiV3DepositsCryptoCurrencySymbolGetCall(currencySymbol, autoAddressDisabled, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * 
     * 
     * @param currencySymbol  (required)
     * @param autoAddressDisabled  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public void apiV3DepositsCryptoCurrencySymbolGet(CryptoCurrencySymbol currencySymbol, Boolean autoAddressDisabled) throws ApiException {
        apiV3DepositsCryptoCurrencySymbolGetWithHttpInfo(currencySymbol, autoAddressDisabled);
    }

    /**
     * 
     * 
     * @param currencySymbol  (required)
     * @param autoAddressDisabled  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<Void> apiV3DepositsCryptoCurrencySymbolGetWithHttpInfo(CryptoCurrencySymbol currencySymbol, Boolean autoAddressDisabled) throws ApiException {
        com.squareup.okhttp.Call call = apiV3DepositsCryptoCurrencySymbolGetValidateBeforeCall(currencySymbol, autoAddressDisabled, null, null);
        return apiClient.execute(call);
    }

    /**
     *  (asynchronously)
     * 
     * @param currencySymbol  (required)
     * @param autoAddressDisabled  (optional)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call apiV3DepositsCryptoCurrencySymbolGetAsync(CryptoCurrencySymbol currencySymbol, Boolean autoAddressDisabled, final ApiCallback<Void> callback) throws ApiException {

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

        com.squareup.okhttp.Call call = apiV3DepositsCryptoCurrencySymbolGetValidateBeforeCall(currencySymbol, autoAddressDisabled, progressListener, progressRequestListener);
        apiClient.executeAsync(call, callback);
        return call;
    }
    /**
     * Build call for apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet
     * @param currencySymbol  (required)
     * @param address  (required)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGetCall(CryptoCurrencySymbol currencySymbol, String address, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = null;
        
        // create path and map variables
        String localVarPath = "/api/v3/deposits/crypto/getnewcryptoaddress/{currencySymbol}/{address}"
            .replaceAll("\\{" + "currencySymbol" + "\\}", apiClient.escapeString(currencySymbol.toString()))
            .replaceAll("\\{" + "address" + "\\}", apiClient.escapeString(address.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            
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
    private com.squareup.okhttp.Call apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGetValidateBeforeCall(CryptoCurrencySymbol currencySymbol, String address, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        // verify the required parameter 'currencySymbol' is set
        if (currencySymbol == null) {
            throw new ApiException("Missing the required parameter 'currencySymbol' when calling apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet(Async)");
        }
        // verify the required parameter 'address' is set
        if (address == null) {
            throw new ApiException("Missing the required parameter 'address' when calling apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet(Async)");
        }
        
        com.squareup.okhttp.Call call = apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGetCall(currencySymbol, address, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * 
     * 
     * @param currencySymbol  (required)
     * @param address  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public void apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet(CryptoCurrencySymbol currencySymbol, String address) throws ApiException {
        apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGetWithHttpInfo(currencySymbol, address);
    }

    /**
     * 
     * 
     * @param currencySymbol  (required)
     * @param address  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<Void> apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGetWithHttpInfo(CryptoCurrencySymbol currencySymbol, String address) throws ApiException {
        com.squareup.okhttp.Call call = apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGetValidateBeforeCall(currencySymbol, address, null, null);
        return apiClient.execute(call);
    }

    /**
     *  (asynchronously)
     * 
     * @param currencySymbol  (required)
     * @param address  (required)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGetAsync(CryptoCurrencySymbol currencySymbol, String address, final ApiCallback<Void> callback) throws ApiException {

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

        com.squareup.okhttp.Call call = apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGetValidateBeforeCall(currencySymbol, address, progressListener, progressRequestListener);
        apiClient.executeAsync(call, callback);
        return call;
    }
}
