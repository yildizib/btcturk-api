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
import {CommissionOutputModel} from '../model/CommissionOutputModel';
import {LimitOutputModel} from '../model/LimitOutputModel';

/**
* Exchange service.
* @module api/ExchangeApi
* @version 3.0
*/
export class ExchangeApi {

    /**
    * Constructs a new ExchangeApi. 
    * @alias module:api/ExchangeApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instanc
    e} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }

    /**
     * Callback function to receive the result of the apiV3ExchangeCommissionsGet operation.
     * @callback moduleapi/ExchangeApi~apiV3ExchangeCommissionsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CommissionOutputModel{ data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:api/ExchangeApi~apiV3ExchangeCommissionsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link <&vendorExtensions.x-jsdoc-type>}
     */
    apiV3ExchangeCommissionsGet(callback) {
      
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
      let accepts = ['application/json'];
      let returnType = CommissionOutputModel;

      return this.apiClient.callApi(
        '/api/v3/exchange/commissions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
    /**
     * Callback function to receive the result of the apiV3ExchangeLimitsGet operation.
     * @callback moduleapi/ExchangeApi~apiV3ExchangeLimitsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LimitOutputModel{ data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:api/ExchangeApi~apiV3ExchangeLimitsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link <&vendorExtensions.x-jsdoc-type>}
     */
    apiV3ExchangeLimitsGet(callback) {
      
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
      let accepts = ['application/json'];
      let returnType = LimitOutputModel;

      return this.apiClient.callApi(
        '/api/v3/exchange/limits', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

}