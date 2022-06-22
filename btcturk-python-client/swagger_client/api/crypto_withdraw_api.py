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


class CryptoWithdrawApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v3_withdrawals_crypto_confirm_code_delete(self, code, **kwargs):  # noqa: E501
        """api_v3_withdrawals_crypto_confirm_code_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_withdrawals_crypto_confirm_code_delete(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_withdrawals_crypto_confirm_code_delete_with_http_info(code, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_withdrawals_crypto_confirm_code_delete_with_http_info(code, **kwargs)  # noqa: E501
            return data

    def api_v3_withdrawals_crypto_confirm_code_delete_with_http_info(self, code, **kwargs):  # noqa: E501
        """api_v3_withdrawals_crypto_confirm_code_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_withdrawals_crypto_confirm_code_delete_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_withdrawals_crypto_confirm_code_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `api_v3_withdrawals_crypto_confirm_code_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

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
            '/api/v3/withdrawals/crypto/confirm/{code}', 'DELETE',
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

    def api_v3_withdrawals_crypto_confirm_code_get(self, code, **kwargs):  # noqa: E501
        """api_v3_withdrawals_crypto_confirm_code_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_withdrawals_crypto_confirm_code_get(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: (required)
        :return: CryptoWithdrawValidationResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_withdrawals_crypto_confirm_code_get_with_http_info(code, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_withdrawals_crypto_confirm_code_get_with_http_info(code, **kwargs)  # noqa: E501
            return data

    def api_v3_withdrawals_crypto_confirm_code_get_with_http_info(self, code, **kwargs):  # noqa: E501
        """api_v3_withdrawals_crypto_confirm_code_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_withdrawals_crypto_confirm_code_get_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: (required)
        :return: CryptoWithdrawValidationResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_withdrawals_crypto_confirm_code_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `api_v3_withdrawals_crypto_confirm_code_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

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
            '/api/v3/withdrawals/crypto/confirm/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CryptoWithdrawValidationResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v3_withdrawals_crypto_confirm_post(self, **kwargs):  # noqa: E501
        """api_v3_withdrawals_crypto_confirm_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_withdrawals_crypto_confirm_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CryptoWithdrawalDeleteInputModel body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_withdrawals_crypto_confirm_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_withdrawals_crypto_confirm_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v3_withdrawals_crypto_confirm_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_v3_withdrawals_crypto_confirm_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_withdrawals_crypto_confirm_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CryptoWithdrawalDeleteInputModel body:
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
                    " to method api_v3_withdrawals_crypto_confirm_post" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/withdrawals/crypto/confirm', 'POST',
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

    def api_v3_withdrawals_crypto_validation_code_get(self, code, **kwargs):  # noqa: E501
        """api_v3_withdrawals_crypto_validation_code_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_withdrawals_crypto_validation_code_get(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: (required)
        :return: CryptoWithdrawValidationResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v3_withdrawals_crypto_validation_code_get_with_http_info(code, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v3_withdrawals_crypto_validation_code_get_with_http_info(code, **kwargs)  # noqa: E501
            return data

    def api_v3_withdrawals_crypto_validation_code_get_with_http_info(self, code, **kwargs):  # noqa: E501
        """api_v3_withdrawals_crypto_validation_code_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v3_withdrawals_crypto_validation_code_get_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: (required)
        :return: CryptoWithdrawValidationResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v3_withdrawals_crypto_validation_code_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `api_v3_withdrawals_crypto_validation_code_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

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
            '/api/v3/withdrawals/crypto/validation/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CryptoWithdrawValidationResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
