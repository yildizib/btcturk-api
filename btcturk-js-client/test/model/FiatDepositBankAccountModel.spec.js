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
    describe('FiatDepositBankAccountModel', function() {
      beforeEach(function() {
        instance = new BtcTurkAp30.FiatDepositBankAccountModel();
      });

      it('should create an instance of FiatDepositBankAccountModel', function() {
        // TODO: update the code to test FiatDepositBankAccountModel
        expect(instance).to.be.a(BtcTurkAp30.FiatDepositBankAccountModel);
      });

      it('should have the property slug (base name: "slug")', function() {
        // TODO: update the code to test the property slug
        expect(instance).to.have.property('slug');
        // expect(instance.slug).to.be(expectedValueLiteral);
      });

      it('should have the property code (base name: "code")', function() {
        // TODO: update the code to test the property code
        expect(instance).to.have.property('code');
        // expect(instance.code).to.be(expectedValueLiteral);
      });

      it('should have the property name (base name: "name")', function() {
        // TODO: update the code to test the property name
        expect(instance).to.have.property('name');
        // expect(instance.name).to.be(expectedValueLiteral);
      });

      it('should have the property statusTransfer (base name: "statusTransfer")', function() {
        // TODO: update the code to test the property statusTransfer
        expect(instance).to.have.property('statusTransfer');
        // expect(instance.statusTransfer).to.be(expectedValueLiteral);
      });

      it('should have the property statusAcceptEFT (base name: "statusAcceptEFT")', function() {
        // TODO: update the code to test the property statusAcceptEFT
        expect(instance).to.have.property('statusAcceptEFT');
        // expect(instance.statusAcceptEFT).to.be(expectedValueLiteral);
      });

      it('should have the property ??ban (base name: "iban")', function() {
        // TODO: update the code to test the property ??ban
        expect(instance).to.have.property('??ban');
        // expect(instance.??ban).to.be(expectedValueLiteral);
      });

      it('should have the property owner (base name: "owner")', function() {
        // TODO: update the code to test the property owner
        expect(instance).to.have.property('owner');
        // expect(instance.owner).to.be(expectedValueLiteral);
      });

      it('should have the property darkLogo (base name: "darkLogo")', function() {
        // TODO: update the code to test the property darkLogo
        expect(instance).to.have.property('darkLogo');
        // expect(instance.darkLogo).to.be(expectedValueLiteral);
      });

      it('should have the property lightLogo (base name: "lightLogo")', function() {
        // TODO: update the code to test the property lightLogo
        expect(instance).to.have.property('lightLogo');
        // expect(instance.lightLogo).to.be(expectedValueLiteral);
      });

      it('should have the property currencySymbol (base name: "currencySymbol")', function() {
        // TODO: update the code to test the property currencySymbol
        expect(instance).to.have.property('currencySymbol');
        // expect(instance.currencySymbol).to.be(expectedValueLiteral);
      });

    });
  });

}));
