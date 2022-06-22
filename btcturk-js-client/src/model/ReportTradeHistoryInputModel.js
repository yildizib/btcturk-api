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
import {DocumentFileType} from './DocumentFileType';

/**
 * The ReportTradeHistoryInputModel model module.
 * @module model/ReportTradeHistoryInputModel
 * @version 3.0
 */
export class ReportTradeHistoryInputModel {
  /**
   * Constructs a new <code>ReportTradeHistoryInputModel</code>.
   * @alias module:model/ReportTradeHistoryInputModel
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>ReportTradeHistoryInputModel</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/ReportTradeHistoryInputModel} obj Optional instance to populate.
   * @return {module:model/ReportTradeHistoryInputModel} The populated <code>ReportTradeHistoryInputModel</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new ReportTradeHistoryInputModel();
      if (data.hasOwnProperty('pairs'))
        obj.pairs = ApiClient.convertToType(data['pairs'], ['Number']);
      if (data.hasOwnProperty('orderTypes'))
        obj.orderTypes = ApiClient.convertToType(data['orderTypes'], ['Number']);
      if (data.hasOwnProperty('beginDate'))
        obj.beginDate = ApiClient.convertToType(data['beginDate'], 'Date');
      if (data.hasOwnProperty('endDate'))
        obj.endDate = ApiClient.convertToType(data['endDate'], 'Date');
      if (data.hasOwnProperty('documentFileType'))
        obj.documentFileType = DocumentFileType.constructFromObject(data['documentFileType']);
    }
    return obj;
  }
}

/**
 * @member {Array.<Number>} pairs
 */
ReportTradeHistoryInputModel.prototype.pairs = undefined;

/**
 * @member {Array.<Number>} orderTypes
 */
ReportTradeHistoryInputModel.prototype.orderTypes = undefined;

/**
 * @member {Date} beginDate
 */
ReportTradeHistoryInputModel.prototype.beginDate = undefined;

/**
 * @member {Date} endDate
 */
ReportTradeHistoryInputModel.prototype.endDate = undefined;

/**
 * @member {module:model/DocumentFileType} documentFileType
 */
ReportTradeHistoryInputModel.prototype.documentFileType = undefined;

