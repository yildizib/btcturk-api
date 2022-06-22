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
import {ApiClient} from '../ApiClient';

/**
 * The CryptoCommissionOutputModel model module.
 * @module model/CryptoCommissionOutputModel
 * @version 3.0
 */
export class CryptoCommissionOutputModel {
  /**
   * Constructs a new <code>CryptoCommissionOutputModel</code>.
   * @alias module:model/CryptoCommissionOutputModel
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>CryptoCommissionOutputModel</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/CryptoCommissionOutputModel} obj Optional instance to populate.
   * @return {module:model/CryptoCommissionOutputModel} The populated <code>CryptoCommissionOutputModel</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new CryptoCommissionOutputModel();
      if (data.hasOwnProperty('currencySymbol'))
        obj.currencySymbol = ApiClient.convertToType(data['currencySymbol'], 'String');
      if (data.hasOwnProperty('deposit'))
        obj.deposit = ApiClient.convertToType(data['deposit'], 'Number');
      if (data.hasOwnProperty('withdrawal'))
        obj.withdrawal = ApiClient.convertToType(data['withdrawal'], 'Number');
    }
    return obj;
  }
}

/**
 * @member {String} currencySymbol
 */
CryptoCommissionOutputModel.prototype.currencySymbol = undefined;

/**
 * @member {Number} deposit
 */
CryptoCommissionOutputModel.prototype.deposit = undefined;

/**
 * @member {Number} withdrawal
 */
CryptoCommissionOutputModel.prototype.withdrawal = undefined;
