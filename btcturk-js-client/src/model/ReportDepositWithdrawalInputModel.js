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
 * The ReportDepositWithdrawalInputModel model module.
 * @module model/ReportDepositWithdrawalInputModel
 * @version 3.0
 */
export class ReportDepositWithdrawalInputModel {
  /**
   * Constructs a new <code>ReportDepositWithdrawalInputModel</code>.
   * @alias module:model/ReportDepositWithdrawalInputModel
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>ReportDepositWithdrawalInputModel</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/ReportDepositWithdrawalInputModel} obj Optional instance to populate.
   * @return {module:model/ReportDepositWithdrawalInputModel} The populated <code>ReportDepositWithdrawalInputModel</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new ReportDepositWithdrawalInputModel();
      if (data.hasOwnProperty('types'))
        obj.types = ApiClient.convertToType(data['types'], ['Number']);
      if (data.hasOwnProperty('currencies'))
        obj.currencies = ApiClient.convertToType(data['currencies'], ['Number']);
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
 * @member {Array.<Number>} types
 */
ReportDepositWithdrawalInputModel.prototype.types = undefined;

/**
 * @member {Array.<Number>} currencies
 */
ReportDepositWithdrawalInputModel.prototype.currencies = undefined;

/**
 * @member {Date} beginDate
 */
ReportDepositWithdrawalInputModel.prototype.beginDate = undefined;

/**
 * @member {Date} endDate
 */
ReportDepositWithdrawalInputModel.prototype.endDate = undefined;

/**
 * @member {module:model/DocumentFileType} documentFileType
 */
ReportDepositWithdrawalInputModel.prototype.documentFileType = undefined;

