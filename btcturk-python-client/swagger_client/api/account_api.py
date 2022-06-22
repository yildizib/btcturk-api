# coding: utf-8

"""
    BtcTurk API 3.0

    White label exchange API documentation.  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: development@btctrader.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AccountApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v3_account_address_put(self, **kwargs):  # noqa: E501
        """api_v3_account_address_put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_account_address_put(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountAddressModel body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_account_address_put_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_account_address_put_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v3_account_address_put_with_http_info(self, **kwargs):  # noqa: E501
        """api_v3_account_address_put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_account_address_put_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountAddressModel body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_account_address_put" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/account/address', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v3_account_buy_sell_ınfo_get(self, **kwargs):  # noqa: E501
        """api_v3_account_buy_sell_ınfo_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_account_buy_sell_ınfo_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_account_buy_sell_ınfo_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_account_buy_sell_ınfo_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v3_account_buy_sell_ınfo_get_with_http_info(self, **kwargs):  # noqa: E501
        """api_v3_account_buy_sell_ınfo_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_account_buy_sell_ınfo_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_account_buy_sell_ınfo_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/account/buy-sell-info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v3_account_features_get(self, **kwargs):  # noqa: E501
        """api_v3_account_features_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_account_features_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_account_features_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_account_features_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v3_account_features_get_with_http_info(self, **kwargs):  # noqa: E501
        """api_v3_account_features_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_account_features_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_account_features_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/account/features', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v3_account_limits_get(self, **kwargs):  # noqa: E501
        """api_v3_account_limits_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_account_limits_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency_symbol:
        :return: UserAllLimitsModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_account_limits_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_account_limits_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v3_account_limits_get_with_http_info(self, **kwargs):  # noqa: E501
        """api_v3_account_limits_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_account_limits_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency_symbol:
        :return: UserAllLimitsModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency_symbol']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_account_limits_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency_symbol' in params:
            query_params.append(('currencySymbol', params['currency_symbol']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/account/limits', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserAllLimitsModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v3_account_pdpa_post(self, **kwargs):  # noqa: E501
        """api_v3_account_pdpa_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_account_pdpa_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str value:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_account_pdpa_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_account_pdpa_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v3_account_pdpa_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_v3_account_pdpa_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_account_pdpa_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str value:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_account_pdpa_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'value' in params:
            query_params.append(('value', params['value']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/account/pdpa', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v3_account_splash_screen_login_post(self, **kwargs):  # noqa: E501
        """api_v3_account_splash_screen_login_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_account_splash_screen_login_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateSplashScreenLoginRequestModel body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_account_splash_screen_login_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_account_splash_screen_login_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v3_account_splash_screen_login_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_v3_account_splash_screen_login_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_account_splash_screen_login_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateSplashScreenLoginRequestModel body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_account_splash_screen_login_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/account/splash-screen-login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v3_account_trade_fee_rates_get(self, **kwargs):  # noqa: E501
        """api_v3_account_trade_fee_rates_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_account_trade_fee_rates_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OrderMethod order_method:
        :param str pair_symbol:
        :return: UserTradeFeeRateOutputModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_account_trade_fee_rates_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_account_trade_fee_rates_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v3_account_trade_fee_rates_get_with_http_info(self, **kwargs):  # noqa: E501
        """api_v3_account_trade_fee_rates_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_account_trade_fee_rates_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OrderMethod order_method:
        :param str pair_symbol:
        :return: UserTradeFeeRateOutputModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_method', 'pair_symbol']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_account_trade_fee_rates_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_method' in params:
            query_params.append(('orderMethod', params['order_method']))  # noqa: E501
        if 'pair_symbol' in params:
            query_params.append(('pairSymbol', params['pair_symbol']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/account/trade-fee-rates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserTradeFeeRateOutputModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
