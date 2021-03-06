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


class UserAgreementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v3_user_agreement_get(self, **kwargs):  # noqa: E501
        """api_v3_user_agreement_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_user_agreement_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[UserAgreementModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_user_agreement_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_user_agreement_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v3_user_agreement_get_with_http_info(self, **kwargs):  # noqa: E501
        """api_v3_user_agreement_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_user_agreement_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[UserAgreementModel]
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
                    " to method api_v3_user_agreement_get" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/UserAgreement', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[UserAgreementModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v3_user_agreement_post(self, **kwargs):  # noqa: E501
        """api_v3_user_agreement_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_user_agreement_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserAgreementApproveModel body: Approve id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_user_agreement_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_user_agreement_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v3_user_agreement_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_v3_user_agreement_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_user_agreement_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserAgreementApproveModel body: Approve id
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
                    " to method api_v3_user_agreement_post" % key
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
            '/api/v3/UserAgreement', 'POST',
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

    def api_v3_user_agreement_risk_disclosure_currency_symbol_get(self, symbol, **kwargs):  # noqa: E501
        """api_v3_user_agreement_risk_disclosure_currency_symbol_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_user_agreement_risk_disclosure_currency_symbol_get(symbol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: (required)
        :param CurrencyTransferType transfer_type:
        :return: CheckCurrencyRiskAgreementResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_user_agreement_risk_disclosure_currency_symbol_get_with_http_info(symbol, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_user_agreement_risk_disclosure_currency_symbol_get_with_http_info(symbol, **kwargs)  # noqa: E501
            return data

    def api_v3_user_agreement_risk_disclosure_currency_symbol_get_with_http_info(self, symbol, **kwargs):  # noqa: E501
        """api_v3_user_agreement_risk_disclosure_currency_symbol_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_user_agreement_risk_disclosure_currency_symbol_get_with_http_info(symbol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: (required)
        :param CurrencyTransferType transfer_type:
        :return: CheckCurrencyRiskAgreementResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol', 'transfer_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_user_agreement_risk_disclosure_currency_symbol_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `api_v3_user_agreement_risk_disclosure_currency_symbol_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501

        query_params = []
        if 'transfer_type' in params:
            query_params.append(('transferType', params['transfer_type']))  # noqa: E501

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
            '/api/v3/user-agreement/risk-disclosure/currency/{symbol}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CheckCurrencyRiskAgreementResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get(self, pair_symbol, **kwargs):  # noqa: E501
        """api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get(pair_symbol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pair_symbol: (required)
        :return: CheckPairRiskAgreementResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get_with_http_info(pair_symbol, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get_with_http_info(pair_symbol, **kwargs)  # noqa: E501
            return data

    def api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get_with_http_info(self, pair_symbol, **kwargs):  # noqa: E501
        """api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get_with_http_info(pair_symbol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pair_symbol: (required)
        :return: CheckPairRiskAgreementResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pair_symbol']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pair_symbol' is set
        if ('pair_symbol' not in params or
                params['pair_symbol'] is None):
            raise ValueError("Missing the required parameter `pair_symbol` when calling `api_v3_user_agreement_risk_disclosure_pair_pair_symbol_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pair_symbol' in params:
            path_params['pairSymbol'] = params['pair_symbol']  # noqa: E501

        query_params = []

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
            '/api/v3/user-agreement/risk-disclosure/pair/{pairSymbol}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CheckPairRiskAgreementResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v3_user_agreement_slug_get(self, slug, **kwargs):  # noqa: E501
        """api_v3_user_agreement_slug_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_user_agreement_slug_get(slug, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: (required)
        :return: UserAgreementModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_user_agreement_slug_get_with_http_info(slug, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_user_agreement_slug_get_with_http_info(slug, **kwargs)  # noqa: E501
            return data

    def api_v3_user_agreement_slug_get_with_http_info(self, slug, **kwargs):  # noqa: E501
        """api_v3_user_agreement_slug_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_user_agreement_slug_get_with_http_info(slug, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: (required)
        :return: UserAgreementModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slug']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_user_agreement_slug_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slug' is set
        if ('slug' not in params or
                params['slug'] is None):
            raise ValueError("Missing the required parameter `slug` when calling `api_v3_user_agreement_slug_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slug' in params:
            path_params['slug'] = params['slug']  # noqa: E501

        query_params = []

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
            '/api/v3/UserAgreement/{slug}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserAgreementModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v3_user_agreement_slug_get_0(self, slug, **kwargs):  # noqa: E501
        """api_v3_user_agreement_slug_get_0  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_user_agreement_slug_get_0(slug, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: (required)
        :return: UserAgreementModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_user_agreement_slug_get_0_with_http_info(slug, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_user_agreement_slug_get_0_with_http_info(slug, **kwargs)  # noqa: E501
            return data

    def api_v3_user_agreement_slug_get_0_with_http_info(self, slug, **kwargs):  # noqa: E501
        """api_v3_user_agreement_slug_get_0  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_user_agreement_slug_get_0_with_http_info(slug, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: (required)
        :return: UserAgreementModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slug']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_user_agreement_slug_get_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slug' is set
        if ('slug' not in params or
                params['slug'] is None):
            raise ValueError("Missing the required parameter `slug` when calling `api_v3_user_agreement_slug_get_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slug' in params:
            path_params['slug'] = params['slug']  # noqa: E501

        query_params = []

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
            '/api/v3/user-agreement/{slug}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserAgreementModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v3_user_agreement_slug_post(self, slug, **kwargs):  # noqa: E501
        """api_v3_user_agreement_slug_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_user_agreement_slug_post(slug, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_user_agreement_slug_post_with_http_info(slug, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_user_agreement_slug_post_with_http_info(slug, **kwargs)  # noqa: E501
            return data

    def api_v3_user_agreement_slug_post_with_http_info(self, slug, **kwargs):  # noqa: E501
        """api_v3_user_agreement_slug_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_user_agreement_slug_post_with_http_info(slug, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slug: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slug']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_user_agreement_slug_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slug' is set
        if ('slug' not in params or
                params['slug'] is None):
            raise ValueError("Missing the required parameter `slug` when calling `api_v3_user_agreement_slug_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slug' in params:
            path_params['slug'] = params['slug']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/user-agreement/{slug}', 'POST',
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
