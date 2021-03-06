/* 
 * BtcTurk API 3.0
 *
 * White label exchange API documentation.
 *
 * OpenAPI spec version: 3.0
 * Contact: development@btctrader.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection;
using RestSharp;
using NUnit.Framework;

using IO.Swagger.Client;
using IO.Swagger.Api;
using IO.Swagger.Model;

namespace IO.Swagger.Test
{
    /// <summary>
    ///  Class for testing CryptoWithdrawApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by Swagger Codegen.
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    [TestFixture]
    public class CryptoWithdrawApiTests
    {
        private CryptoWithdrawApi instance;

        /// <summary>
        /// Setup before each unit test
        /// </summary>
        [SetUp]
        public void Init()
        {
            instance = new CryptoWithdrawApi();
        }

        /// <summary>
        /// Clean up after each unit test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of CryptoWithdrawApi
        /// </summary>
        [Test]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsInstanceOfType' CryptoWithdrawApi
            //Assert.IsInstanceOfType(typeof(CryptoWithdrawApi), instance, "instance is a CryptoWithdrawApi");
        }

        /// <summary>
        /// Test ApiV3WithdrawalsCryptoConfirmCodeDelete
        /// </summary>
        [Test]
        public void ApiV3WithdrawalsCryptoConfirmCodeDeleteTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string code = null;
            //instance.ApiV3WithdrawalsCryptoConfirmCodeDelete(code);
            
        }
        /// <summary>
        /// Test ApiV3WithdrawalsCryptoConfirmCodeGet
        /// </summary>
        [Test]
        public void ApiV3WithdrawalsCryptoConfirmCodeGetTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string code = null;
            //var response = instance.ApiV3WithdrawalsCryptoConfirmCodeGet(code);
            //Assert.IsInstanceOf<CryptoWithdrawValidationResponseModel> (response, "response is CryptoWithdrawValidationResponseModel");
        }
        /// <summary>
        /// Test ApiV3WithdrawalsCryptoConfirmPost
        /// </summary>
        [Test]
        public void ApiV3WithdrawalsCryptoConfirmPostTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //CryptoWithdrawalDeleteInputModel body = null;
            //instance.ApiV3WithdrawalsCryptoConfirmPost(body);
            
        }
        /// <summary>
        /// Test ApiV3WithdrawalsCryptoValidationCodeGet
        /// </summary>
        [Test]
        public void ApiV3WithdrawalsCryptoValidationCodeGetTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string code = null;
            //var response = instance.ApiV3WithdrawalsCryptoValidationCodeGet(code);
            //Assert.IsInstanceOf<CryptoWithdrawValidationResponseModel> (response, "response is CryptoWithdrawValidationResponseModel");
        }
    }

}
