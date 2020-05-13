# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  A Carbon DLS API token ([JWT](https://en.wikipedia.org/wiki/JSON_Web_Token)) must be included with each request to the API.  Steps to create API tokens: - Create and download an API key [here](https://print.carbon3d.com/api_keys) - For testing: Generate JWT tokens using the [token generator](/token_generator) - For production: Generate JWT tokens dynamically (<em>see authtoken-create.py example</em>) - A valid Carbon API token must be included as <code>Authorization: Bearer [token]</code> HTTP header.  This API provides a programmatic interface for submitting part (and soon build) orders. The general process for creating an order is as follows:  - Upload model files to the API with the [/models](#/Models) endpoint - Create parts that reference a model and a part number with the [/parts](#/Parts) endpoint   -  Part numbers can be created [here](https://print.carbon3d.com/catalog_parts) - Create an order with the [/orders](#/Orders) endpoint  Uploaded models, parts and orders can be retrieved either in bulk or by UUID at the [/models](#/Models), [/parts](#/Parts) and [/orders](#/Orders) endpoints, respectively.  Once a part order is submitted, automatic packing will create one or more builds (for mass-customization applications only).  Builds can be retrieved either in bulk or by UUID at the [/builds](#/Builds) endpoint. - Build attachments (traveler, slice video) can be retrieved by UUID at the [/attachments](#/Attachments) endpoint.  This API also provides a programmatic interface to access [printer](#/Printers) (fleet) status and query for [prints](#/Prints).   # noqa: E501

    The version of the OpenAPI document: 0.0.4
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from carbon3d.api_client import ApiClient
from carbon3d.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PrintersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_printer(self, name, **kwargs):  # noqa: E501
        """Fetch a specific printer's status information  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_printer(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str name: e.g. L1001 (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Printer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_printer_with_http_info(name, **kwargs)  # noqa: E501

    def get_printer_with_http_info(self, name, **kwargs):  # noqa: E501
        """Fetch a specific printer's status information  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_printer_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str name: e.g. L1001 (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Printer, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'name'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_printer" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                        local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `get_printer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/printers/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Printer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_printers(self, limit, offset, **kwargs):  # noqa: E501
        """Fetch all printer's status information  # noqa: E501

        Fetch all printers and their relevant attached information like status and sliding print window (past/current/next). Sorted by name, ascending.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_printers(limit, offset, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Max records to return (required)
        :param int offset: Number of items to skip (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PrintersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_printers_with_http_info(limit, offset, **kwargs)  # noqa: E501

    def get_printers_with_http_info(self, limit, offset, **kwargs):  # noqa: E501
        """Fetch all printer's status information  # noqa: E501

        Fetch all printers and their relevant attached information like status and sliding print window (past/current/next). Sorted by name, ascending.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_printers_with_http_info(limit, offset, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Max records to return (required)
        :param int offset: Number of items to skip (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PrintersResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'offset'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_printers" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'limit' is set
        if self.api_client.client_side_validation and ('limit' not in local_var_params or  # noqa: E501
                                                        local_var_params['limit'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `limit` when calling `get_printers`")  # noqa: E501
        # verify the required parameter 'offset' is set
        if self.api_client.client_side_validation and ('offset' not in local_var_params or  # noqa: E501
                                                        local_var_params['offset'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `offset` when calling `get_printers`")  # noqa: E501

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_printers`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_printers`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_printers`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/printers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrintersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
