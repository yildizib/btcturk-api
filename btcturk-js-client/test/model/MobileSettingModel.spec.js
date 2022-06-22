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
    describe('MobileSettingModel', function() {
      beforeEach(function() {
        instance = new BtcTurkAp30.MobileSettingModel();
      });

      it('should create an instance of MobileSettingModel', function() {
        // TODO: update the code to test MobileSettingModel
        expect(instance).to.be.a(BtcTurkAp30.MobileSettingModel);
      });

      it('should have the property languageSettings (base name: "languageSettings")', function() {
        // TODO: update the code to test the property languageSettings
        expect(instance).to.have.property('languageSettings');
        // expect(instance.languageSettings).to.be(expectedValueLiteral);
      });

      it('should have the property rating (base name: "rating")', function() {
        // TODO: update the code to test the property rating
        expect(instance).to.have.property('rating');
        // expect(instance.rating).to.be(expectedValueLiteral);
      });

      it('should have the property euroIsEnable (base name: "euroIsEnable")', function() {
        // TODO: update the code to test the property euroIsEnable
        expect(instance).to.have.property('euroIsEnable');
        // expect(instance.euroIsEnable).to.be(expectedValueLiteral);
      });

      it('should have the property countryCode (base name: "countryCode")', function() {
        // TODO: update the code to test the property countryCode
        expect(instance).to.have.property('countryCode');
        // expect(instance.countryCode).to.be(expectedValueLiteral);
      });

    });
  });

}));