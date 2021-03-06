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
 * The SystemNotificationCountModel model module.
 * @module model/SystemNotificationCountModel
 * @version 3.0
 */
export class SystemNotificationCountModel {
  /**
   * Constructs a new <code>SystemNotificationCountModel</code>.
   * @alias module:model/SystemNotificationCountModel
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>SystemNotificationCountModel</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/SystemNotificationCountModel} obj Optional instance to populate.
   * @return {module:model/SystemNotificationCountModel} The populated <code>SystemNotificationCountModel</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new SystemNotificationCountModel();
      if (data.hasOwnProperty('t'))
        obj.t = ApiClient.convertToType(data['t'], 'String');
      if (data.hasOwnProperty('c'))
        obj.c = ApiClient.convertToType(data['c'], 'Number');
      if (data.hasOwnProperty('r'))
        obj.r = ApiClient.convertToType(data['r'], 'Boolean');
    }
    return obj;
  }
}

/**
 * @member {String} t
 */
SystemNotificationCountModel.prototype.t = undefined;

/**
 * @member {Number} c
 */
SystemNotificationCountModel.prototype.c = undefined;

/**
 * @member {Boolean} r
 */
SystemNotificationCountModel.prototype.r = undefined;

