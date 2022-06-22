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
    describe('CreateAlarmRequest', function() {
      beforeEach(function() {
        instance = new BtcTurkAp30.CreateAlarmRequest();
      });

      it('should create an instance of CreateAlarmRequest', function() {
        // TODO: update the code to test CreateAlarmRequest
        expect(instance).to.be.a(BtcTurkAp30.CreateAlarmRequest);
      });

      it('should have the property pair (base name: "pair")', function() {
        // TODO: update the code to test the property pair
        expect(instance).to.have.property('pair');
        // expect(instance.pair).to.be(expectedValueLiteral);
      });

      it('should have the property triggerValue (base name: "triggerValue")', function() {
        // TODO: update the code to test the property triggerValue
        expect(instance).to.have.property('triggerValue');
        // expect(instance.triggerValue).to.be(expectedValueLiteral);
      });

      it('should have the property alarmType (base name: "alarmType")', function() {
        // TODO: update the code to test the property alarmType
        expect(instance).to.have.property('alarmType');
        // expect(instance.alarmType).to.be(expectedValueLiteral);
      });

      it('should have the property vector (base name: "vector")', function() {
        // TODO: update the code to test the property vector
        expect(instance).to.have.property('vector');
        // expect(instance.vector).to.be(expectedValueLiteral);
      });

      it('should have the property ınterval (base name: "interval")', function() {
        // TODO: update the code to test the property ınterval
        expect(instance).to.have.property('ınterval');
        // expect(instance.ınterval).to.be(expectedValueLiteral);
      });

      it('should have the property repeatInterval (base name: "repeatInterval")', function() {
        // TODO: update the code to test the property repeatInterval
        expect(instance).to.have.property('repeatInterval');
        // expect(instance.repeatInterval).to.be(expectedValueLiteral);
      });

      it('should have the property repeatMax (base name: "repeatMax")', function() {
        // TODO: update the code to test the property repeatMax
        expect(instance).to.have.property('repeatMax');
        // expect(instance.repeatMax).to.be(expectedValueLiteral);
      });

      it('should have the property smsAlert (base name: "smsAlert")', function() {
        // TODO: update the code to test the property smsAlert
        expect(instance).to.have.property('smsAlert');
        // expect(instance.smsAlert).to.be(expectedValueLiteral);
      });

      it('should have the property emailAlert (base name: "emailAlert")', function() {
        // TODO: update the code to test the property emailAlert
        expect(instance).to.have.property('emailAlert');
        // expect(instance.emailAlert).to.be(expectedValueLiteral);
      });

      it('should have the property pushNotificationAlert (base name: "pushNotificationAlert")', function() {
        // TODO: update the code to test the property pushNotificationAlert
        expect(instance).to.have.property('pushNotificationAlert');
        // expect(instance.pushNotificationAlert).to.be(expectedValueLiteral);
      });

    });
  });

}));