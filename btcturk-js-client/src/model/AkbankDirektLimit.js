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
 * The AkbankDirektLimit model module.
 * @module model/AkbankDirektLimit
 * @version 3.0
 */
export class AkbankDirektLimit {
  /**
   * Constructs a new <code>AkbankDirektLimit</code>.
   * @alias module:model/AkbankDirektLimit
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>AkbankDirektLimit</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/AkbankDirektLimit} obj Optional instance to populate.
   * @return {module:model/AkbankDirektLimit} The populated <code>AkbankDirektLimit</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new AkbankDirektLimit();
      if (data.hasOwnProperty('maxDepositFeeAmount'))
        obj.maxDepositFeeAmount = ApiClient.convertToType(data['maxDepositFeeAmount'], 'Number');
      if (data.hasOwnProperty('minDepositAmount'))
        obj.minDepositAmount = ApiClient.convertToType(data['minDepositAmount'], 'Number');
      if (data.hasOwnProperty('maxDepositAmount'))
        obj.maxDepositAmount = ApiClient.convertToType(data['maxDepositAmount'], 'Number');
    }
    return obj;
  }
}

/**
 * @member {Number} maxDepositFeeAmount
 */
AkbankDirektLimit.prototype.maxDepositFeeAmount = undefined;

/**
 * @member {Number} minDepositAmount
 */
AkbankDirektLimit.prototype.minDepositAmount = undefined;

/**
 * @member {Number} maxDepositAmount
 */
AkbankDirektLimit.prototype.maxDepositAmount = undefined;
