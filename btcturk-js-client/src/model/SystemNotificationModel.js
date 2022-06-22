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
 * The SystemNotificationModel model module.
 * @module model/SystemNotificationModel
 * @version 3.0
 */
export class SystemNotificationModel {
  /**
   * Constructs a new <code>SystemNotificationModel</code>.
   * @alias module:model/SystemNotificationModel
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>SystemNotificationModel</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/SystemNotificationModel} obj Optional instance to populate.
   * @return {module:model/SystemNotificationModel} The populated <code>SystemNotificationModel</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new SystemNotificationModel();
      if (data.hasOwnProperty('id'))
        obj.ıd = ApiClient.convertToType(data['id'], 'Number');
      if (data.hasOwnProperty('subtitle'))
        obj.subtitle = ApiClient.convertToType(data['subtitle'], 'String');
      if (data.hasOwnProperty('activity'))
        obj.activity = ApiClient.convertToType(data['activity'], 'String');
      if (data.hasOwnProperty('code'))
        obj.code = ApiClient.convertToType(data['code'], 'String');
      if (data.hasOwnProperty('createdDate'))
        obj.createdDate = ApiClient.convertToType(data['createdDate'], 'Number');
      if (data.hasOwnProperty('pin'))
        obj.pin = ApiClient.convertToType(data['pin'], 'Boolean');
      if (data.hasOwnProperty('read'))
        obj.read = ApiClient.convertToType(data['read'], 'Boolean');
    }
    return obj;
  }
}

/**
 * @member {Number} ıd
 */
SystemNotificationModel.prototype.ıd = undefined;

/**
 * @member {String} subtitle
 */
SystemNotificationModel.prototype.subtitle = undefined;

/**
 * @member {String} activity
 */
SystemNotificationModel.prototype.activity = undefined;

/**
 * @member {String} code
 */
SystemNotificationModel.prototype.code = undefined;

/**
 * @member {Number} createdDate
 */
SystemNotificationModel.prototype.createdDate = undefined;

/**
 * @member {Boolean} pin
 */
SystemNotificationModel.prototype.pin = undefined;

/**
 * @member {Boolean} read
 */
SystemNotificationModel.prototype.read = undefined;
