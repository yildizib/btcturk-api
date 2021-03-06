/*
 * BtcTurk API 3.0
 * White label exchange API documentation.
 *
 * OpenAPI spec version: 3.0
 * Contact: development@btctrader.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.api;

import io.swagger.client.model.CommissionOutputModel;
import io.swagger.client.model.LimitOutputModel;
import org.junit.Test;
import org.junit.Ignore;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


/**
 * API tests for ExchangeApi
 */
@Ignore
public class ExchangeApiTest {

    private final ExchangeApi api = new ExchangeApi();

    /**
     * 
     *
     * 
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void apiV3ExchangeCommissionsGetTest() throws Exception {
        CommissionOutputModel response = api.apiV3ExchangeCommissionsGet();

        // TODO: test validations
    }
    /**
     * 
     *
     * 
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void apiV3ExchangeLimitsGetTest() throws Exception {
        LimitOutputModel response = api.apiV3ExchangeLimitsGet();

        // TODO: test validations
    }
}
