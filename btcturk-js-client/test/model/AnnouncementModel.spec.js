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
    describe('AnnouncementModel', function() {
      beforeEach(function() {
        instance = new BtcTurkAp30.AnnouncementModel();
      });

      it('should create an instance of AnnouncementModel', function() {
        // TODO: update the code to test AnnouncementModel
        expect(instance).to.be.a(BtcTurkAp30.AnnouncementModel);
      });

      it('should have the property title (base name: "title")', function() {
        // TODO: update the code to test the property title
        expect(instance).to.have.property('title');
        // expect(instance.title).to.be(expectedValueLiteral);
      });

      it('should have the property seoUrl (base name: "seoUrl")', function() {
        // TODO: update the code to test the property seoUrl
        expect(instance).to.have.property('seoUrl');
        // expect(instance.seoUrl).to.be(expectedValueLiteral);
      });

      it('should have the property releaseDate (base name: "releaseDate")', function() {
        // TODO: update the code to test the property releaseDate
        expect(instance).to.have.property('releaseDate');
        // expect(instance.releaseDate).to.be(expectedValueLiteral);
      });

    });
  });

}));