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
 * The MobilejwtPlatformBody model module.
 * @module model/MobilejwtPlatformBody
 * @version 3.0
 */
export class MobilejwtPlatformBody {
  /**
   * Constructs a new <code>MobilejwtPlatformBody</code>.
   * @alias module:model/MobilejwtPlatformBody
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>MobilejwtPlatformBody</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/MobilejwtPlatformBody} obj Optional instance to populate.
   * @return {module:model/MobilejwtPlatformBody} The populated <code>MobilejwtPlatformBody</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new MobilejwtPlatformBody();
      if (data.hasOwnProperty('user_token'))
        obj.userToken = ApiClient.convertToType(data['user_token'], 'String');
    }
    return obj;
  }
}

/**
 * @member {String} userToken
 */
MobilejwtPlatformBody.prototype.userToken = undefined;

