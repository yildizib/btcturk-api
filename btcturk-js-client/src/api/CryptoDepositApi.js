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
import {CryptoCurrencySymbol} from '../model/CryptoCurrencySymbol';

/**
* CryptoDeposit service.
* @module api/CryptoDepositApi
* @version 3.0
*/
export class CryptoDepositApi {

    /**
    * Constructs a new CryptoDepositApi. 
    * @alias module:api/CryptoDepositApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instanc
    e} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }

    /**
     * Callback function to receive the result of the apiV3DepositsCryptoCurrencySymbolGet operation.
     * @callback moduleapi/CryptoDepositApi~apiV3DepositsCryptoCurrencySymbolGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:model/CryptoCurrencySymbol} currencySymbol 
     * @param {Object} opts Optional parameters
     * @param {Boolean} opts.autoAddressDisabled 
     * @param {module:api/CryptoDepositApi~apiV3DepositsCryptoCurrencySymbolGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV3DepositsCryptoCurrencySymbolGet(currencySymbol, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'currencySymbol' is set
      if (currencySymbol === undefined || currencySymbol === null) {
        throw new Error("Missing the required parameter 'currencySymbol' when calling apiV3DepositsCryptoCurrencySymbolGet");
      }

      let pathParams = {
        'currencySymbol': currencySymbol
      };
      let queryParams = {
        'autoAddressDisabled': opts['autoAddressDisabled']
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
        '/api/v3/deposits/crypto/{currencySymbol}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
    /**
     * Callback function to receive the result of the apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet operation.
     * @callback moduleapi/CryptoDepositApi~apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:model/CryptoCurrencySymbol} currencySymbol 
     * @param {String} address 
     * @param {module:api/CryptoDepositApi~apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet(currencySymbol, address, callback) {
      
      let postBody = null;
      // verify the required parameter 'currencySymbol' is set
      if (currencySymbol === undefined || currencySymbol === null) {
        throw new Error("Missing the required parameter 'currencySymbol' when calling apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet");
      }
      // verify the required parameter 'address' is set
      if (address === undefined || address === null) {
        throw new Error("Missing the required parameter 'address' when calling apiV3DepositsCryptoGetnewcryptoaddressCurrencySymbolAddressGet");
      }

      let pathParams = {
        'currencySymbol': currencySymbol,'address': address
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
        '/api/v3/deposits/crypto/getnewcryptoaddress/{currencySymbol}/{address}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

}