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

import io.swagger.client.model.BadRequestResponseModel;
import io.swagger.client.model.UserDonationRequestModel;
import org.junit.Test;
import org.junit.Ignore;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


/**
 * API tests for UserDonationApi
 */
@Ignore
public class UserDonationApiTest {

    private final UserDonationApi api = new UserDonationApi();

    /**
     * Bağış kampanyasına ait kullanılabilir bankalar
     *
     * 
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void apiV3UserDonationBanksGetTest() throws Exception {
        api.apiV3UserDonationBanksGet();

        // TODO: test validations
    }
    /**
     * Bağış durumu
     *
     * 
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void apiV3UserDonationGetTest() throws Exception {
        api.apiV3UserDonationGet();

        // TODO: test validations
    }
    /**
     * Yeni bağış kaydı
     *
     * 
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void apiV3UserDonationPostTest() throws Exception {
        UserDonationRequestModel body = null;
        api.apiV3UserDonationPost(body);

        // TODO: test validations
    }
}
