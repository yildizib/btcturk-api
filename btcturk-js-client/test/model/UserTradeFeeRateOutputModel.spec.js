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
    describe('UserTradeFeeRateOutputModel', function() {
      beforeEach(function() {
        instance = new BtcTurkAp30.UserTradeFeeRateOutputModel();
      });

      it('should create an instance of UserTradeFeeRateOutputModel', function() {
        // TODO: update the code to test UserTradeFeeRateOutputModel
        expect(instance).to.be.a(BtcTurkAp30.UserTradeFeeRateOutputModel);
      });

      it('should have the property pairId (base name: "pairId")', function() {
        // TODO: update the code to test the property pairId
        expect(instance).to.have.property('pairId');
        // expect(instance.pairId).to.be(expectedValueLiteral);
      });

      it('should have the property pairSymbol (base name: "pairSymbol")', function() {
        // TODO: update the code to test the property pairSymbol
        expect(instance).to.have.property('pairSymbol');
        // expect(instance.pairSymbol).to.be(expectedValueLiteral);
      });

      it('should have the property orderMethod (base name: "orderMethod")', function() {
        // TODO: update the code to test the property orderMethod
        expect(instance).to.have.property('orderMethod');
        // expect(instance.orderMethod).to.be(expectedValueLiteral);
      });

      it('should have the property makerFeePercentage (base name: "makerFeePercentage")', function() {
        // TODO: update the code to test the property makerFeePercentage
        expect(instance).to.have.property('makerFeePercentage');
        // expect(instance.makerFeePercentage).to.be(expectedValueLiteral);
      });

      it('should have the property takerFeePercentage (base name: "takerFeePercentage")', function() {
        // TODO: update the code to test the property takerFeePercentage
        expect(instance).to.have.property('takerFeePercentage');
        // expect(instance.takerFeePercentage).to.be(expectedValueLiteral);
      });

      it('should have the property taxPercentage (base name: "taxPercentage")', function() {
        // TODO: update the code to test the property taxPercentage
        expect(instance).to.have.property('taxPercentage');
        // expect(instance.taxPercentage).to.be(expectedValueLiteral);
      });

      it('should have the property hasActiveCoupon (base name: "hasActiveCoupon")', function() {
        // TODO: update the code to test the property hasActiveCoupon
        expect(instance).to.have.property('hasActiveCoupon');
        // expect(instance.hasActiveCoupon).to.be(expectedValueLiteral);
      });

    });
  });

}));
