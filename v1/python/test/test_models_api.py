# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  A Carbon DLS API token ([JWT](https://en.wikipedia.org/wiki/JSON_Web_Token)) must be included with each request to the API.  Steps to create API tokens: - Create and download an API key [here](https://print.carbon3d.com/api_keys) - For testing: Generate JWT tokens using the [token generator](/token_generator) - For production: Generate JWT tokens dynamically (<em>see authtoken-create.py example</em>) - A valid Carbon API token must be included as <code>Authorization: Bearer [token]</code> HTTP header.  This API provides a programmatic interface for submitting part (and soon build) orders. The general process for creating an order is as follows:  - Upload model files to the API with the [/models](#/Models) endpoint - Create parts that reference a model and a part number with the [/parts](#/Parts) endpoint   -  Part numbers can be created [here](https://print.carbon3d.com/catalog_parts) - Create an order with the [/orders](#/Orders) endpoint  Uploaded models, parts and orders can be retrieved either in bulk or by UUID at the [/models](#/Models), [/parts](#/Parts) and [/orders](#/Orders) endpoints, respectively.  Once a part order is submitted, automatic packing will create one or more builds (for mass-customization applications only).  Builds can be retrieved either in bulk or by UUID at the [/builds](#/Builds) endpoint. - Build attachments (traveler, slice video) can be retrieved by UUID at the [/attachments](#/Attachments) endpoint.  This API also provides a programmatic interface to access [printer](#/Printers) (fleet) status and query for [prints](#/Prints).   # noqa: E501

    The version of the OpenAPI document: 0.0.4
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import carbon3d
from carbon3d.api.models_api import ModelsApi  # noqa: E501
from carbon3d.rest import ApiException


class TestModelsApi(unittest.TestCase):
    """ModelsApi unit test stubs"""

    def setUp(self):
        self.api = carbon3d.api.models_api.ModelsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_model(self):
        """Test case for get_model

        Get a model by UUID  # noqa: E501
        """
        pass

    def test_get_models(self):
        """Test case for get_models

        Fetch models  # noqa: E501
        """
        pass

    def test_upload_model(self):
        """Test case for upload_model

        Upload a model  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
