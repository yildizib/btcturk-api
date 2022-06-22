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
    describe('BankCommissionOutputModel', function() {
      beforeEach(function() {
        instance = new BtcTurkAp30.BankCommissionOutputModel();
      });

      it('should create an instance of BankCommissionOutputModel', function() {
        // TODO: update the code to test BankCommissionOutputModel
        expect(instance).to.be.a(BtcTurkAp30.BankCommissionOutputModel);
      });

      it('should have the property depositFee (base name: "depositFee")', function() {
        // TODO: update the code to test the property depositFee
        expect(instance).to.have.property('depositFee');
        // expect(instance.depositFee).to.be(expectedValueLiteral);
      });

      it('should have the property withdrawalFee (base name: "withdrawalFee")', function() {
        // TODO: update the code to test the property withdrawalFee
        expect(instance).to.have.property('withdrawalFee');
        // expect(instance.withdrawalFee).to.be(expectedValueLiteral);
      });

      it('should have the property depositTax (base name: "depositTax")', function() {
        // TODO: update the code to test the property depositTax
        expect(instance).to.have.property('depositTax');
        // expect(instance.depositTax).to.be(expectedValueLiteral);
      });

      it('should have the property withdrawalTax (base name: "withdrawalTax")', function() {
        // TODO: update the code to test the property withdrawalTax
        expect(instance).to.have.property('withdrawalTax');
        // expect(instance.withdrawalTax).to.be(expectedValueLiteral);
      });

      it('should have the property currency (base name: "currency")', function() {
        // TODO: update the code to test the property currency
        expect(instance).to.have.property('currency');
        // expect(instance.currency).to.be(expectedValueLiteral);
      });

    });
  });

}));
