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
import {AnnouncementDetailModel} from './AnnouncementDetailModel';

/**
 * The AnnouncementDetailModelIPagedList model module.
 * @module model/AnnouncementDetailModelIPagedList
 * @version 3.0
 */
export class AnnouncementDetailModelIPagedList {
  /**
   * Constructs a new <code>AnnouncementDetailModelIPagedList</code>.
   * @alias module:model/AnnouncementDetailModelIPagedList
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>AnnouncementDetailModelIPagedList</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/AnnouncementDetailModelIPagedList} obj Optional instance to populate.
   * @return {module:model/AnnouncementDetailModelIPagedList} The populated <code>AnnouncementDetailModelIPagedList</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new AnnouncementDetailModelIPagedList();
      if (data.hasOwnProperty('indexFrom'))
        obj.ındexFrom = ApiClient.convertToType(data['indexFrom'], 'Number');
      if (data.hasOwnProperty('pageIndex'))
        obj.pageIndex = ApiClient.convertToType(data['pageIndex'], 'Number');
      if (data.hasOwnProperty('pageSize'))
        obj.pageSize = ApiClient.convertToType(data['pageSize'], 'Number');
      if (data.hasOwnProperty('totalCount'))
        obj.totalCount = ApiClient.convertToType(data['totalCount'], 'Number');
      if (data.hasOwnProperty('totalPages'))
        obj.totalPages = ApiClient.convertToType(data['totalPages'], 'Number');
      if (data.hasOwnProperty('items'))
        obj.ıtems = ApiClient.convertToType(data['items'], [AnnouncementDetailModel]);
      if (data.hasOwnProperty('hasPreviousPage'))
        obj.hasPreviousPage = ApiClient.convertToType(data['hasPreviousPage'], 'Boolean');
      if (data.hasOwnProperty('hasNextPage'))
        obj.hasNextPage = ApiClient.convertToType(data['hasNextPage'], 'Boolean');
    }
    return obj;
  }
}

/**
 * @member {Number} ındexFrom
 */
AnnouncementDetailModelIPagedList.prototype.ındexFrom = undefined;

/**
 * @member {Number} pageIndex
 */
AnnouncementDetailModelIPagedList.prototype.pageIndex = undefined;

/**
 * @member {Number} pageSize
 */
AnnouncementDetailModelIPagedList.prototype.pageSize = undefined;

/**
 * @member {Number} totalCount
 */
AnnouncementDetailModelIPagedList.prototype.totalCount = undefined;

/**
 * @member {Number} totalPages
 */
AnnouncementDetailModelIPagedList.prototype.totalPages = undefined;

/**
 * @member {Array.<module:model/AnnouncementDetailModel>} ıtems
 */
AnnouncementDetailModelIPagedList.prototype.ıtems = undefined;

/**
 * @member {Boolean} hasPreviousPage
 */
AnnouncementDetailModelIPagedList.prototype.hasPreviousPage = undefined;

/**
 * @member {Boolean} hasNextPage
 */
AnnouncementDetailModelIPagedList.prototype.hasNextPage = undefined;
