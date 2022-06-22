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
import {AppRatingEnum} from './AppRatingEnum';

/**
 * The AppRatingRequestModel model module.
 * @module model/AppRatingRequestModel
 * @version 3.0
 */
export class AppRatingRequestModel {
  /**
   * Constructs a new <code>AppRatingRequestModel</code>.
   * @alias module:model/AppRatingRequestModel
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>AppRatingRequestModel</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/AppRatingRequestModel} obj Optional instance to populate.
   * @return {module:model/AppRatingRequestModel} The populated <code>AppRatingRequestModel</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new AppRatingRequestModel();
      if (data.hasOwnProperty('rate'))
        obj.rate = AppRatingEnum.constructFromObject(data['rate']);
    }
    return obj;
  }
}

/**
 * @member {module:model/AppRatingEnum} rate
 */
AppRatingRequestModel.prototype.rate = undefined;
