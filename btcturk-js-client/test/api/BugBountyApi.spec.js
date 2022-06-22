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
    instance = new BtcTurkAp30.BugBountyApi();
  });

  describe('(package)', function() {
    describe('BugBountyApi', function() {
      describe('apiV3BugBountiesHallOfFameGet', function() {
        it('should call apiV3BugBountiesHallOfFameGet successfully', function(done) {
          // TODO: uncomment apiV3BugBountiesHallOfFameGet call and complete the assertions
          /*

          instance.apiV3BugBountiesHallOfFameGet(function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            let dataCtr = data;
            expect(dataCtr).to.be.an(Array);
            expect(dataCtr).to.not.be.empty();
            for (let p in dataCtr) {
              let data = dataCtr[p];
              expect(data).to.be.a(BtcTurkAp30.HallOfFrameResponseModel);
            }

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
      describe('apiV3BugBountiesPost', function() {
        it('should call apiV3BugBountiesPost successfully', function(done) {
          // TODO: uncomment, update parameter values for apiV3BugBountiesPost call
          /*
          var opts = {};

          instance.apiV3BugBountiesPost(opts, function(error, data, response) {
            if (error) {
              done(error);
              return;
            }

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