/*
 * BtcTurk API 3.0
 * White label exchange API documentation.
 *
 * OpenAPI spec version: 3.0
 * Contact: development@btctrader.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.34
 *
 * Do not edit the class manually.
 *
 */
import {ApiClient} from "../ApiClient";

/**
* FiatWithdrawalCommissions service.
* @module api/FiatWithdrawalCommissionsApi
* @version 3.0
*/
export class FiatWithdrawalCommissionsApi {

    /**
    * Constructs a new FiatWithdrawalCommissionsApi. 
    * @alias module:api/FiatWithdrawalCommissionsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instanc
    e} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }

    /**
     * Callback function to receive the result of the apiV3FiatWithdrawalCommissionsGet operation.
     * @callback moduleapi/FiatWithdrawalCommissionsApi~apiV3FiatWithdrawalCommissionsGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:api/FiatWithdrawalCommissionsApi~apiV3FiatWithdrawalCommissionsGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV3FiatWithdrawalCommissionsGet(callback) {
      
      let postBody = null;

      let pathParams = {
        
      };
      let queryParams = {
        
      };
      let headerParams = {
        
      };
      let formParams = {
        
      };

      let authNames = ['Bearer'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;

      return this.apiClient.callApi(
        '/api/v3/fiat-withdrawal-commissions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

}