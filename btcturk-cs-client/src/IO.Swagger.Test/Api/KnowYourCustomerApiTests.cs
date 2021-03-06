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
    ///  Class for testing KnowYourCustomerApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by Swagger Codegen.
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    [TestFixture]
    public class KnowYourCustomerApiTests
    {
        private KnowYourCustomerApi instance;

        /// <summary>
        /// Setup before each unit test
        /// </summary>
        [SetUp]
        public void Init()
        {
            instance = new KnowYourCustomerApi();
        }

        /// <summary>
        /// Clean up after each unit test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of KnowYourCustomerApi
        /// </summary>
        [Test]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsInstanceOfType' KnowYourCustomerApi
            //Assert.IsInstanceOfType(typeof(KnowYourCustomerApi), instance, "instance is a KnowYourCustomerApi");
        }

        /// <summary>
        /// Test ApiV3AccountKycPost
        /// </summary>
        [Test]
        public void ApiV3AccountKycPostTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //JumioKycIdentityVerificationRequestModel body = null;
            //instance.ApiV3AccountKycPost(body);
            
        }
    }

}
