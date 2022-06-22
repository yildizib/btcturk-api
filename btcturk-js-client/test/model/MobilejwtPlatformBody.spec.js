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
    describe('MobilejwtPlatformBody', function() {
      beforeEach(function() {
        instance = new BtcTurkAp30.MobilejwtPlatformBody();
      });

      it('should create an instance of MobilejwtPlatformBody', function() {
        // TODO: update the code to test MobilejwtPlatformBody
        expect(instance).to.be.a(BtcTurkAp30.MobilejwtPlatformBody);
      });

      it('should have the property userToken (base name: "user_token")', function() {
        // TODO: update the code to test the property userToken
        expect(instance).to.have.property('userToken');
        // expect(instance.userToken).to.be(expectedValueLiteral);
      });

    });
  });

}));