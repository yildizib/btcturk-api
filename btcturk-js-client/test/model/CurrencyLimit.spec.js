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
    describe('CurrencyLimit', function() {
      beforeEach(function() {
        instance = new BtcTurkAp30.CurrencyLimit();
      });

      it('should create an instance of CurrencyLimit', function() {
        // TODO: update the code to test CurrencyLimit
        expect(instance).to.be.a(BtcTurkAp30.CurrencyLimit);
      });

      it('should have the property symbol (base name: "symbol")', function() {
        // TODO: update the code to test the property symbol
        expect(instance).to.have.property('symbol');
        // expect(instance.symbol).to.be(expectedValueLiteral);
      });

      it('should have the property name (base name: "name")', function() {
        // TODO: update the code to test the property name
        expect(instance).to.have.property('name');
        // expect(instance.name).to.be(expectedValueLiteral);
      });

      it('should have the property minDeposit (base name: "minDeposit")', function() {
        // TODO: update the code to test the property minDeposit
        expect(instance).to.have.property('minDeposit');
        // expect(instance.minDeposit).to.be(expectedValueLiteral);
      });

      it('should have the property minWithdrawal (base name: "minWithdrawal")', function() {
        // TODO: update the code to test the property minWithdrawal
        expect(instance).to.have.property('minWithdrawal');
        // expect(instance.minWithdrawal).to.be(expectedValueLiteral);
      });

      it('should have the property levelLimits (base name: "levelLimits")', function() {
        // TODO: update the code to test the property levelLimits
        expect(instance).to.have.property('levelLimits');
        // expect(instance.levelLimits).to.be(expectedValueLiteral);
      });

      it('should have the property type (base name: "type")', function() {
        // TODO: update the code to test the property type
        expect(instance).to.have.property('type');
        // expect(instance.type).to.be(expectedValueLiteral);
      });

      it('should have the property order (base name: "order")', function() {
        // TODO: update the code to test the property order
        expect(instance).to.have.property('order');
        // expect(instance.order).to.be(expectedValueLiteral);
      });

    });
  });

}));
