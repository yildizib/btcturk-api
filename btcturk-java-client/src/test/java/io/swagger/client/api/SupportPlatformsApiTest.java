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

import org.junit.Test;
import org.junit.Ignore;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


/**
 * API tests for SupportPlatformsApi
 */
@Ignore
public class SupportPlatformsApiTest {

    private final SupportPlatformsApi api = new SupportPlatformsApi();

    /**
     * 
     *
     * 
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void apiV3SupportPlatformsGetTest() throws Exception {
        api.apiV3SupportPlatformsGet();

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
    public void apiV3SupportPlatformsZendeskChatJwtPlatformGetTest() throws Exception {
        String platform = null;
        api.apiV3SupportPlatformsZendeskChatJwtPlatformGet(platform);

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
    public void apiV3SupportPlatformsZendeskMobileJwtPlatformPostTest() throws Exception {
        String platform = null;
        String userToken = null;
        api.apiV3SupportPlatformsZendeskMobileJwtPlatformPost(platform, userToken);

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
    public void apiV3SupportPlatformsZendeskSessionsPostTest() throws Exception {
        api.apiV3SupportPlatformsZendeskSessionsPost();

        // TODO: test validations
    }
}