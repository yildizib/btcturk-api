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
    instance = new BtcTurkAp30.SupportPlatformsApi();
  });

  describe('(package)', function() {
    describe('SupportPlatformsApi', function() {
      describe('apiV3SupportPlatformsGet', function() {
        it('should call apiV3SupportPlatformsGet successfully', function(done) {
          // TODO: uncomment apiV3SupportPlatformsGet call
          /*

          instance.apiV3SupportPlatformsGet(function(error, data, response) {
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
      describe('apiV3SupportPlatformsZendeskChatJwtPlatformGet', function() {
        it('should call apiV3SupportPlatformsZendeskChatJwtPlatformGet successfully', function(done) {
          // TODO: uncomment, update parameter values for apiV3SupportPlatformsZendeskChatJwtPlatformGet call
          /*

          instance.apiV3SupportPlatformsZendeskChatJwtPlatformGet(platform, function(error, data, response) {
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
      describe('apiV3SupportPlatformsZendeskMobileJwtPlatformPost', function() {
        it('should call apiV3SupportPlatformsZendeskMobileJwtPlatformPost successfully', function(done) {
          // TODO: uncomment, update parameter values for apiV3SupportPlatformsZendeskMobileJwtPlatformPost call
          /*
          var opts = {};

          instance.apiV3SupportPlatformsZendeskMobileJwtPlatformPost(platform, opts, function(error, data, response) {
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
      describe('apiV3SupportPlatformsZendeskSessionsPost', function() {
        it('should call apiV3SupportPlatformsZendeskSessionsPost successfully', function(done) {
          // TODO: uncomment apiV3SupportPlatformsZendeskSessionsPost call
          /*

          instance.apiV3SupportPlatformsZendeskSessionsPost(function(error, data, response) {
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