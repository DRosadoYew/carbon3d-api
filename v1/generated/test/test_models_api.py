# coding: utf-8

"""
    Carbon API (Draft)

    An API to interact with Carbon's Manufacturing Cloud including 3D model upload, automated order processing and part history.  Getting started ---------------  - [Generate and download an API key](https://carbon3d.print.carbon3d.com/api_keys)   - Your API key and client secret will be downloaded into a secret.json file.  - [Use generated API key to generate a JWT token](/token_generator) from the api key.   - If your API key is revoked, this token will no longer work.  - Authorize with generated token  - Upload mesh files  - Create orders  - Monitor order status   # noqa: E501

    The version of the OpenAPI document: 1.0.1
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
