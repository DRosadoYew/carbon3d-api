# coding: utf-8

"""
    Carbon API (Draft)

    An API to interact with Carbon's Manufacturing Cloud including 3D model upload, automated order processing and part history.  Getting started ---------------  - [Generate and download an API key](https://carbon3d.print.carbon3d.com/api_keys)   - Your API key and client secret will be downloaded into a secret.json file.  - [Use generated API key to generate a JWT token](/token_generator) from the api key.   - If your API key is revoked, this token will no longer work.  - Authorize with generated token  - Upload mesh files  - Create orders  - Monitor order status   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.part import Part  # noqa: E501
from carbon3d.rest import ApiException

class TestPart(unittest.TestCase):
    """Part unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Part
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.part.Part()  # noqa: E501
        if include_optional :
            return Part(
                uuid = '0', 
                part_number = '0', 
                model_uuid = '0'
            )
        else :
            return Part(
                uuid = '0',
                part_number = '0',
                model_uuid = '0',
        )

    def testPart(self):
        """Test Part"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
