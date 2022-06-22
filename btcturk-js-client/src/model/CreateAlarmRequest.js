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
import {AlarmInterval} from './AlarmInterval';
import {AlarmTypes} from './AlarmTypes';
import {AlarmVector} from './AlarmVector';

/**
 * The CreateAlarmRequest model module.
 * @module model/CreateAlarmRequest
 * @version 3.0
 */
export class CreateAlarmRequest {
  /**
   * Constructs a new <code>CreateAlarmRequest</code>.
   * @alias module:model/CreateAlarmRequest
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>CreateAlarmRequest</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/CreateAlarmRequest} obj Optional instance to populate.
   * @return {module:model/CreateAlarmRequest} The populated <code>CreateAlarmRequest</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new CreateAlarmRequest();
      if (data.hasOwnProperty('pair'))
        obj.pair = ApiClient.convertToType(data['pair'], 'String');
      if (data.hasOwnProperty('triggerValue'))
        obj.triggerValue = ApiClient.convertToType(data['triggerValue'], 'Number');
      if (data.hasOwnProperty('alarmType'))
        obj.alarmType = AlarmTypes.constructFromObject(data['alarmType']);
      if (data.hasOwnProperty('vector'))
        obj.vector = AlarmVector.constructFromObject(data['vector']);
      if (data.hasOwnProperty('interval'))
        obj.ınterval = AlarmInterval.constructFromObject(data['interval']);
      if (data.hasOwnProperty('repeatInterval'))
        obj.repeatInterval = ApiClient.convertToType(data['repeatInterval'], 'Number');
      if (data.hasOwnProperty('repeatMax'))
        obj.repeatMax = ApiClient.convertToType(data['repeatMax'], 'Number');
      if (data.hasOwnProperty('smsAlert'))
        obj.smsAlert = ApiClient.convertToType(data['smsAlert'], 'Boolean');
      if (data.hasOwnProperty('emailAlert'))
        obj.emailAlert = ApiClient.convertToType(data['emailAlert'], 'Boolean');
      if (data.hasOwnProperty('pushNotificationAlert'))
        obj.pushNotificationAlert = ApiClient.convertToType(data['pushNotificationAlert'], 'Boolean');
    }
    return obj;
  }
}

/**
 * @member {String} pair
 */
CreateAlarmRequest.prototype.pair = undefined;

/**
 * @member {Number} triggerValue
 */
CreateAlarmRequest.prototype.triggerValue = undefined;

/**
 * @member {module:model/AlarmTypes} alarmType
 */
CreateAlarmRequest.prototype.alarmType = undefined;

/**
 * @member {module:model/AlarmVector} vector
 */
CreateAlarmRequest.prototype.vector = undefined;

/**
 * @member {module:model/AlarmInterval} ınterval
 */
CreateAlarmRequest.prototype.ınterval = undefined;

/**
 * @member {Number} repeatInterval
 */
CreateAlarmRequest.prototype.repeatInterval = undefined;

/**
 * @member {Number} repeatMax
 */
CreateAlarmRequest.prototype.repeatMax = undefined;

/**
 * @member {Boolean} smsAlert
 */
CreateAlarmRequest.prototype.smsAlert = undefined;

/**
 * @member {Boolean} emailAlert
 */
CreateAlarmRequest.prototype.emailAlert = undefined;

/**
 * @member {Boolean} pushNotificationAlert
 */
CreateAlarmRequest.prototype.pushNotificationAlert = undefined;
