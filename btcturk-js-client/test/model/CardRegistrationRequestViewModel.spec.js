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
    describe('CardRegistrationRequestViewModel', function() {
      beforeEach(function() {
        instance = new BtcTurkAp30.CardRegistrationRequestViewModel();
      });

      it('should create an instance of CardRegistrationRequestViewModel', function() {
        // TODO: update the code to test CardRegistrationRequestViewModel
        expect(instance).to.be.a(BtcTurkAp30.CardRegistrationRequestViewModel);
      });

      it('should have the property addressName (base name: "addressName")', function() {
        // TODO: update the code to test the property addressName
        expect(instance).to.have.property('addressName');
        // expect(instance.addressName).to.be(expectedValueLiteral);
      });

      it('should have the property address (base name: "address")', function() {
        // TODO: update the code to test the property address
        expect(instance).to.have.property('address');
        // expect(instance.address).to.be(expectedValueLiteral);
      });

      it('should have the property cityId (base name: "cityId")', function() {
        // TODO: update the code to test the property cityId
        expect(instance).to.have.property('cityId');
        // expect(instance.cityId).to.be(expectedValueLiteral);
      });

      it('should have the property districtId (base name: "districtId")', function() {
        // TODO: update the code to test the property districtId
        expect(instance).to.have.property('districtId');
        // expect(instance.districtId).to.be(expectedValueLiteral);
      });

    });
  });

}));
