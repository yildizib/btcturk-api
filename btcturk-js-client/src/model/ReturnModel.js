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
import {ReturnCodeType} from './ReturnCodeType';

/**
 * The ReturnModel model module.
 * @module model/ReturnModel
 * @version 3.0
 */
export class ReturnModel {
  /**
   * Constructs a new <code>ReturnModel</code>.
   * @alias module:model/ReturnModel
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>ReturnModel</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/ReturnModel} obj Optional instance to populate.
   * @return {module:model/ReturnModel} The populated <code>ReturnModel</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new ReturnModel();
      if (data.hasOwnProperty('success'))
        obj.success = ApiClient.convertToType(data['success'], 'Boolean');
      if (data.hasOwnProperty('message'))
        obj.message = ApiClient.convertToType(data['message'], 'String');
      if (data.hasOwnProperty('code'))
        obj.code = ReturnCodeType.constructFromObject(data['code']);
    }
    return obj;
  }
}

/**
 * @member {Boolean} success
 */
ReturnModel.prototype.success = undefined;

/**
 * @member {String} message
 */
ReturnModel.prototype.message = undefined;

/**
 * @member {module:model/ReturnCodeType} code
 */
ReturnModel.prototype.code = undefined;

