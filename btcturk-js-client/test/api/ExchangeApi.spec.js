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

  beforeEach(function() {
    instance = new BtcTurkAp30.ExchangeApi();
  });

  describe('(package)', function() {
    describe('ExchangeApi', function() {
      describe('apiV3ExchangeCommissionsGet', function() {
        it('should call apiV3ExchangeCommissionsGet successfully', function(done) {
          // TODO: uncomment apiV3ExchangeCommissionsGet call and complete the assertions
          /*

          instance.apiV3ExchangeCommissionsGet(function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            expect(data).to.be.a(BtcTurkAp30.CommissionOutputModel);

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
      describe('apiV3ExchangeLimitsGet', function() {
        it('should call apiV3ExchangeLimitsGet successfully', function(done) {
          // TODO: uncomment apiV3ExchangeLimitsGet call and complete the assertions
          /*

          instance.apiV3ExchangeLimitsGet(function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            expect(data).to.be.a(BtcTurkAp30.LimitOutputModel);

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
    });
  });

}));
