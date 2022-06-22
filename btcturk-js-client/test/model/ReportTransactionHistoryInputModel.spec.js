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
(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.BtcTurkAp30);
  }
}(this, function(expect, BtcTurkAp30) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('ReportTransactionHistoryInputModel', function() {
      beforeEach(function() {
        instance = new BtcTurkAp30.ReportTransactionHistoryInputModel();
      });

      it('should create an instance of ReportTransactionHistoryInputModel', function() {
        // TODO: update the code to test ReportTransactionHistoryInputModel
        expect(instance).to.be.a(BtcTurkAp30.ReportTransactionHistoryInputModel);
      });

      it('should have the property types (base name: "types")', function() {
        // TODO: update the code to test the property types
        expect(instance).to.have.property('types');
        // expect(instance.types).to.be(expectedValueLiteral);
      });

      it('should have the property currencies (base name: "currencies")', function() {
        // TODO: update the code to test the property currencies
        expect(instance).to.have.property('currencies');
        // expect(instance.currencies).to.be(expectedValueLiteral);
      });

      it('should have the property beginDate (base name: "beginDate")', function() {
        // TODO: update the code to test the property beginDate
        expect(instance).to.have.property('beginDate');
        // expect(instance.beginDate).to.be(expectedValueLiteral);
      });

      it('should have the property endDate (base name: "endDate")', function() {
        // TODO: update the code to test the property endDate
        expect(instance).to.have.property('endDate');
        // expect(instance.endDate).to.be(expectedValueLiteral);
      });

      it('should have the property documentFileType (base name: "documentFileType")', function() {
        // TODO: update the code to test the property documentFileType
        expect(instance).to.have.property('documentFileType');
        // expect(instance.documentFileType).to.be(expectedValueLiteral);
      });

    });
  });

}));
