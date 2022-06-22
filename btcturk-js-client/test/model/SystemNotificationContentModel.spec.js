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
    describe('SystemNotificationContentModel', function() {
      beforeEach(function() {
        instance = new BtcTurkAp30.SystemNotificationContentModel();
      });

      it('should create an instance of SystemNotificationContentModel', function() {
        // TODO: update the code to test SystemNotificationContentModel
        expect(instance).to.be.a(BtcTurkAp30.SystemNotificationContentModel);
      });

      it('should have the property ıd (base name: "id")', function() {
        // TODO: update the code to test the property ıd
        expect(instance).to.have.property('ıd');
        // expect(instance.ıd).to.be(expectedValueLiteral);
      });

      it('should have the property subtitle (base name: "subtitle")', function() {
        // TODO: update the code to test the property subtitle
        expect(instance).to.have.property('subtitle');
        // expect(instance.subtitle).to.be(expectedValueLiteral);
      });

      it('should have the property activity (base name: "activity")', function() {
        // TODO: update the code to test the property activity
        expect(instance).to.have.property('activity');
        // expect(instance.activity).to.be(expectedValueLiteral);
      });

      it('should have the property code (base name: "code")', function() {
        // TODO: update the code to test the property code
        expect(instance).to.have.property('code');
        // expect(instance.code).to.be(expectedValueLiteral);
      });

      it('should have the property createdDate (base name: "createdDate")', function() {
        // TODO: update the code to test the property createdDate
        expect(instance).to.have.property('createdDate');
        // expect(instance.createdDate).to.be(expectedValueLiteral);
      });

      it('should have the property pin (base name: "pin")', function() {
        // TODO: update the code to test the property pin
        expect(instance).to.have.property('pin');
        // expect(instance.pin).to.be(expectedValueLiteral);
      });

      it('should have the property content (base name: "content")', function() {
        // TODO: update the code to test the property content
        expect(instance).to.have.property('content');
        // expect(instance.content).to.be(expectedValueLiteral);
      });

      it('should have the property read (base name: "read")', function() {
        // TODO: update the code to test the property read
        expect(instance).to.have.property('read');
        // expect(instance.read).to.be(expectedValueLiteral);
      });

    });
  });

}));